#!/usr/bin/env python3
"""Turn a firm's answers about the FTC Safeguards Rule into a gap report.

Reads the questions in ../assets/questions.json and a JSON file of answers
(question id -> yes | partial | no | unknown). Standard library only; no
network access; writes nothing unless --output is given.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

QUESTIONS_FILE = Path(__file__).resolve().parent.parent / "assets" / "questions.json"
SMALL_FIRM_LIMIT = 5000  # 16 CFR 314.6: "fewer than five thousand consumers"


def load_questions() -> dict:
    try:
        return json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"Cannot read {QUESTIONS_FILE}: {error}")


def load_answers(path: Path, data: dict) -> dict[str, str]:
    try:
        answers = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        sys.exit(f"Cannot read the answers file: {error}")
    except json.JSONDecodeError as error:
        sys.exit(f"The answers file is not valid JSON: {error}")
    if not isinstance(answers, dict):
        sys.exit("The answers file must be a JSON object of question id to answer.")
    known = {question["id"] for question in data["questions"]}
    unknown_ids = sorted(set(answers) - known)
    if unknown_ids:
        sys.exit("Unknown question id(s): " + ", ".join(unknown_ids)
                 + ". Run with --template to see the valid ids.")
    bad = sorted(f"{key}={value}" for key, value in answers.items()
                 if value not in data["answers"])
    if bad:
        sys.exit("Invalid answer(s): " + ", ".join(bad)
                 + ". Use one of: " + ", ".join(data["answers"]) + ".")
    return answers


def assess(data: dict, answers: dict[str, str], consumers: int | None) -> dict:
    small = consumers is not None and consumers < SMALL_FIRM_LIMIT
    results = []
    for question in data["questions"]:
        answer = answers.get(question["id"], "unknown")
        exempt = small and question["exempt_under_5000"]
        if answer == "yes":
            status = "in place"
        elif exempt:
            status = "not required at this size"
        elif answer == "partial":
            status = "partial"
        elif answer == "no":
            status = "gap"
        else:
            status = "unknown"
        results.append({**question, "answer": answer, "status": status})
    order = {"gap": 0, "unknown": 1, "partial": 2}
    actions = sorted((r for r in results if r["status"] in order),
                     key=lambda r: (r["priority"], order[r["status"]]))
    counts = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    return {"consumers": consumers, "small_firm_exemption_applied": small,
            "counts": counts, "results": results, "actions": actions,
            "source": data["source"], "exemption": data["exemption"]}


def render(report: dict) -> str:
    counts = report["counts"]
    lines = ["# Safeguards Rule readiness check", ""]
    lines.append("This is a self-assessment from the firm's own answers. It is not an audit, "
                 "legal advice or a statement that the firm complies with the rule.")
    lines.append("")
    summary = ", ".join(f"{counts[key]} {key}" for key in
                        ("in place", "partial", "gap", "unknown", "not required at this size")
                        if counts.get(key))
    lines.append(f"**Summary:** {summary}.")
    if report["small_firm_exemption_applied"]:
        lines.append("")
        lines.append(f"The firm reported customer information on {report['consumers']:,} consumers. "
                     f"{report['exemption']['text']} ({report['exemption']['citation']}). "
                     "Every other element still applies.")
    elif report["consumers"] is None:
        lines.append("")
        lines.append("The number of consumers was not given, so no element was treated as exempt. "
                     f"See {report['exemption']['citation']}.")
    lines += ["", "## Fix first", ""]
    if report["actions"]:
        for number, item in enumerate(report["actions"], 1):
            lines.append(f"{number}. **{item['element']}: {item['status']}** ({item['citation']}). "
                         f"{item['fix']}")
    else:
        lines.append("No gaps were reported.")
    lines += ["", "## Every element", "",
              "| Element | Requirement | Status | Citation |", "|---|---|---|---|"]
    for item in report["results"]:
        lines.append(f"| {item['element']} | {item['question']} | {item['status']} | "
                     f"{item['citation']} |")
    lines += ["", f"Source: {report['source']['name']}, {report['source']['url']}"]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a Safeguards Rule gap report from a firm's answers.",
        epilog="Start with --template to get a blank answers file.")
    parser.add_argument("--template", action="store_true",
                        help="Print a blank answers file with every question id.")
    parser.add_argument("--questions", action="store_true",
                        help="Print each question with its id and citation.")
    parser.add_argument("--answers", type=Path, help="JSON file of question id to answer.")
    parser.add_argument("--consumers", type=int,
                        help="Number of consumers whose information the firm maintains.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", type=Path, help="Write the report to this file.")
    args = parser.parse_args(argv)

    data = load_questions()
    if args.template:
        print(json.dumps({q["id"]: "unknown" for q in data["questions"]}, indent=2))
        return 0
    if args.questions:
        for question in data["questions"]:
            print(f"{question['id']} [{question['citation']}]: {question['question']}")
        return 0
    if not args.answers:
        parser.error("give --answers, or --template for a blank answers file")
    if args.consumers is not None and args.consumers < 0:
        parser.error("--consumers cannot be negative")

    report = assess(data, load_answers(args.answers, data), args.consumers)
    text = json.dumps(report, indent=2) if args.format == "json" else render(report)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote the report to {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
