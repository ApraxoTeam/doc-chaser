"""Tests for the bundled scripts. Run from the plugin root: python3 -m unittest discover tests"""

import csv
import io
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRID = ROOT / "skills/calculating-trid-deadlines/scripts/trid_deadlines.py"
COST = ROOT / "skills/estimating-chasing-cost/scripts/chasing_cost.py"
LISTS = ROOT / "skills/building-document-request-lists/scripts/build_request_list.py"
CHECKLISTS = ROOT / "skills/building-document-request-lists/assets/checklists"


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *args],
                          capture_output=True, text=True)


def trid(*args):
    result = run(TRID, *args, "--format", "json")
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    return {item["key"]: item["date"] for item in data["dates"]}, data["warnings"]


class TridTests(unittest.TestCase):
    def test_official_commentary_example(self):
        # Comment 19(e)(1)(iii)-2: mailed Monday June 1 -> consummation Tuesday June 9.
        dates, _ = trid("--le-sent", "2015-06-01")
        self.assertEqual(dates["earliest_consummation"], "2015-06-09")

    def test_le_due_third_business_day(self):
        # Comment 19(e)(1)(iii)-1: application Monday -> deliver by Thursday.
        dates, _ = trid("--application-date", "2015-06-01")
        self.assertEqual(dates["le_delivery_deadline"], "2015-06-04")

    def test_le_due_skips_weekend_and_observed_holiday(self):
        # Thursday July 2, 2026: Friday July 3 is the observed holiday, so the
        # creditor is closed; days 1-3 are Mon July 6, Tue July 7, Wed July 8.
        dates, _ = trid("--application-date", "2026-07-02")
        self.assertEqual(dates["le_delivery_deadline"], "2026-07-08")

    def test_saturday_open_creditor(self):
        dates, _ = trid("--application-date", "2026-03-05",
                        "--open-days", "mon,tue,wed,thu,fri,sat")
        self.assertEqual(dates["le_delivery_deadline"], "2026-03-09")

    def test_cd_three_days_counts_saturday(self):
        # Closing Thursday -> receipt Monday; mail by the prior Thursday.
        dates, _ = trid("--consummation-date", "2026-03-12")
        self.assertEqual(dates["cd_receipt_deadline"], "2026-03-09")
        self.assertEqual(dates["cd_send_deadline_if_not_in_person"], "2026-03-05")
        self.assertEqual(dates["revised_le_receipt_deadline"], "2026-03-07")

    def test_observed_holiday_is_specific_business_day(self):
        # July 4, 2026 is a Saturday. Friday July 3 (observed) still counts.
        dates, _ = trid("--le-sent", "2026-06-29", "--consummation-date", "2026-07-08")
        self.assertEqual(dates["earliest_consummation"], "2026-07-08")
        self.assertEqual(dates["cd_receipt_deadline"], "2026-07-03")

    def test_warns_when_closing_too_early(self):
        _, warnings = trid("--le-sent", "2026-06-29", "--consummation-date", "2026-07-06")
        self.assertTrue(any("waiting period" in warning for warning in warnings))

    def test_bad_date_is_rejected(self):
        result = run(TRID, "--application-date", "03/02/2026")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("YYYY-MM-DD", result.stderr)

    def test_requires_a_date(self):
        self.assertNotEqual(run(TRID).returncode, 0)


class ChasingCostTests(unittest.TestCase):
    def test_basic(self):
        result = run(COST, "--clients", "200", "--minutes", "45", "--rate", "85",
                     "--format", "json")
        data = json.loads(result.stdout)
        self.assertEqual(data["annual_hours"], 150.0)
        self.assertEqual(data["annual_cost"], 12750.0)
        self.assertEqual(data["cost_per_client"], 63.75)
        self.assertEqual(data["scenarios"][1]["cost_saved"], 6375.0)

    def test_zero_clients(self):
        result = run(COST, "--clients", "0", "--minutes", "45", "--rate", "85")
        self.assertEqual(result.returncode, 0)

    def test_rejects_negative(self):
        result = run(COST, "--clients", "-5", "--minutes", "45", "--rate", "85")
        self.assertNotEqual(result.returncode, 0)


class RequestListTests(unittest.TestCase):
    def test_templates_are_well_formed(self):
        files = sorted(CHECKLISTS.glob("*.json"))
        self.assertGreaterEqual(len(files), 6)
        for path in files:
            data = json.loads(path.read_text())
            self.assertEqual(data["id"], path.stem)
            ids = []
            for section in data["sections"]:
                for item in section["items"]:
                    ids.append(item["id"])
                    self.assertIn(item["basis"], data["sources"], f"{path.name}:{item['id']}")
                    for tag in item["when"]:
                        self.assertIn(tag, data["situations"], f"{path.name}:{item['id']}")
            self.assertEqual(len(ids), len(set(ids)), f"duplicate ids in {path.name}")

    def test_situations_filter_items(self):
        result = run(LISTS, "--template", "tax-individual-1040",
                     "--situations", "wages", "--format", "json")
        labels = [item["id"] for item in json.loads(result.stdout)["items"]]
        self.assertIn("w2", labels)
        self.assertIn("ssn", labels)
        self.assertNotIn("ssa-1099", labels)

    def test_csv_has_header_and_rows(self):
        result = run(LISTS, "--template", "mortgage-purchase",
                     "--situations", "gift-funds", "--format", "csv")
        rows = list(csv.reader(io.StringIO(result.stdout)))
        self.assertEqual(rows[0], ["section", "item", "detail", "status", "source"])
        self.assertTrue(any("gift letter" in row[1].lower() for row in rows))

    def test_unknown_tag_is_rejected(self):
        result = run(LISTS, "--template", "mortgage-purchase", "--situations", "nope")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Valid tags", result.stderr)

    def test_list(self):
        result = run(LISTS, "--list")
        self.assertIn("agency-onboarding", result.stdout)


if __name__ == "__main__":
    unittest.main()


STATUS = ROOT / "skills/reviewing-received-documents/scripts/request_status.py"
GAP = ROOT / "skills/assessing-safeguards-readiness/scripts/safeguards_gap.py"
QUESTIONS = ROOT / "skills/assessing-safeguards-readiness/assets/questions.json"


class RequestStatusTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.dir = tempfile.TemporaryDirectory()
        self.csv = Path(self.dir.name) / "list.csv"
        result = run(LISTS, "--template", "mortgage-purchase", "--format", "csv",
                     "--output", str(self.csv))
        self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self):
        self.dir.cleanup()

    def test_summary_of_new_list(self):
        result = run(STATUS, "summary", "--csv", str(self.csv))
        self.assertIn("0 of 7 items received", result.stdout)

    def test_set_received_and_rejected(self):
        run(STATUS, "set", "--csv", str(self.csv), "--item", "W-2", "--status", "received")
        result = run(STATUS, "set", "--csv", str(self.csv), "--item", "bank statements",
                     "--status", "rejected", "--note", "send all pages")
        self.assertIn("1 of 7 items received", result.stdout)
        self.assertIn("send all pages", result.stdout)
        with self.csv.open() as handle:
            rows = list(csv.DictReader(handle))
        self.assertIn("note", rows[0])

    def test_not_applicable_reduces_total(self):
        result = run(STATUS, "set", "--csv", str(self.csv), "--item", "1",
                     "--status", "not-applicable")
        self.assertIn("0 of 6 items received", result.stdout)

    def test_rejected_needs_note(self):
        result = run(STATUS, "set", "--csv", str(self.csv), "--item", "1",
                     "--status", "rejected")
        self.assertNotEqual(result.returncode, 0)

    def test_ambiguous_item(self):
        result = run(STATUS, "set", "--csv", str(self.csv), "--item", "the last",
                     "--status", "received")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("row number", result.stderr)

    def test_missing_file(self):
        result = run(STATUS, "summary", "--csv", str(self.csv) + ".nope")
        self.assertNotEqual(result.returncode, 0)


class SafeguardsGapTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.dir = tempfile.TemporaryDirectory()
        self.answers = Path(self.dir.name) / "answers.json"

    def tearDown(self):
        self.dir.cleanup()

    def report(self, answers, *args):
        self.answers.write_text(json.dumps(answers))
        result = run(GAP, "--answers", str(self.answers), "--format", "json", *args)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        return {item["id"]: item["status"] for item in data["results"]}, data

    def test_exemption_matches_314_6(self):
        data = json.loads(QUESTIONS.read_text())
        exempt = sorted(q["citation"] for q in data["questions"] if q["exempt_under_5000"])
        self.assertEqual(exempt, ["16 CFR 314.4(b)(1)", "16 CFR 314.4(d)(2)",
                                  "16 CFR 314.4(h)", "16 CFR 314.4(i)"])

    def test_small_firm_exemption(self):
        status, data = self.report({"incident-response": "no", "mfa": "no"},
                                   "--consumers", "400")
        self.assertEqual(status["incident-response"], "not required at this size")
        self.assertEqual(status["mfa"], "gap")
        self.assertTrue(data["small_firm_exemption_applied"])

    def test_no_exemption_at_5000_or_unknown_size(self):
        status, _ = self.report({"incident-response": "no"}, "--consumers", "5000")
        self.assertEqual(status["incident-response"], "gap")
        status, _ = self.report({"incident-response": "no"})
        self.assertEqual(status["incident-response"], "gap")

    def test_unanswered_is_unknown_and_gaps_come_first(self):
        status, data = self.report({"mfa": "no", "training": "partial"})
        self.assertEqual(status["encryption"], "unknown")
        self.assertEqual(data["actions"][0]["id"], "mfa")

    def test_bad_answers_rejected(self):
        self.answers.write_text(json.dumps({"mfa": "maybe"}))
        self.assertNotEqual(run(GAP, "--answers", str(self.answers)).returncode, 0)
        self.answers.write_text(json.dumps({"nope": "yes"}))
        self.assertNotEqual(run(GAP, "--answers", str(self.answers)).returncode, 0)

    def test_template_lists_every_question(self):
        template = json.loads(run(GAP, "--template").stdout)
        data = json.loads(QUESTIONS.read_text())
        self.assertEqual(set(template), {q["id"] for q in data["questions"]})
