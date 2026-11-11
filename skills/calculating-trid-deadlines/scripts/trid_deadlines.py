#!/usr/bin/env python3
"""TRID disclosure-timing calculator (12 CFR 1026.19(e) and (f)).

Computes Loan Estimate and Closing Disclosure dates from an application date
and/or a planned consummation date. Standard library only; no network access.

Two definitions of "business day" apply (12 CFR 1026.2(a)(6)):

* General: a day the creditor's offices are open to the public for carrying on
  substantially all of its business functions. Used for the Loan Estimate
  delivery deadline, 1026.19(e)(1)(iii)(A), and the revised-estimate deadline,
  1026.19(e)(4)(i). It depends on the creditor, so it is configurable here.
* Specific: every calendar day except Sundays and the legal public holidays in
  5 U.S.C. 6103(a). Used for the waiting periods and receipt presumptions,
  1026.19(e)(1)(iii)(B), (e)(1)(iv), (e)(4)(ii), (f)(1)(ii) and (f)(1)(iii).
  Under comment 2(a)(6)-2, a fixed-date holiday counts on its actual date; the
  weekday on which it is merely observed is a business day.

The output is a planning aid for a licensed professional to check. It is not
legal advice and it does not cover state law, rescission or timeshares.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta

WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def _nth_weekday(year: int, month: int, weekday: int, n: int) -> date:
    """Return the n-th given weekday (0=Monday) of a month."""
    first = date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return first + timedelta(days=offset + 7 * (n - 1))


def _last_weekday(year: int, month: int, weekday: int) -> date:
    """Return the last given weekday (0=Monday) of a month."""
    next_month = date(year + (month == 12), month % 12 + 1, 1)
    last = next_month - timedelta(days=1)
    return last - timedelta(days=(last.weekday() - weekday) % 7)


def legal_public_holidays(year: int) -> dict[date, str]:
    """Legal public holidays listed in 5 U.S.C. 6103(a), on their actual dates."""
    holidays = {
        date(year, 1, 1): "New Year's Day",
        _nth_weekday(year, 1, 0, 3): "Birthday of Martin Luther King, Jr.",
        _nth_weekday(year, 2, 0, 3): "Washington's Birthday",
        _last_weekday(year, 5, 0): "Memorial Day",
        date(year, 7, 4): "Independence Day",
        _nth_weekday(year, 9, 0, 1): "Labor Day",
        _nth_weekday(year, 10, 0, 2): "Columbus Day",
        date(year, 11, 11): "Veterans Day",
        _nth_weekday(year, 11, 3, 4): "Thanksgiving Day",
        date(year, 12, 25): "Christmas Day",
    }
    # Juneteenth was added to 5 U.S.C. 6103(a) on June 17, 2021.
    if year >= 2021:
        holidays[date(year, 6, 19)] = "Juneteenth National Independence Day"
    return holidays


def observed_holidays(year: int) -> set[date]:
    """Weekdays on which federal offices observe the holidays (5 U.S.C. 6103(b)).

    Used only as the default guess for when a creditor's offices are closed.
    """
    observed = set()
    for year_ in (year, year + 1):  # Jan 1 of next year can be observed Dec 31.
        for day in legal_public_holidays(year_):
            if day.weekday() == 5:
                day -= timedelta(days=1)
            elif day.weekday() == 6:
                day += timedelta(days=1)
            if day.year == year:
                observed.add(day)
    return observed


def is_specific_business_day(day: date) -> bool:
    return day.weekday() != 6 and day not in legal_public_holidays(day.year)


class GeneralCalendar:
    """Days the creditor's offices are open (the general definition)."""

    def __init__(self, open_weekdays: set[int], closed_dates: set[date]):
        self.open_weekdays = open_weekdays
        self.closed_dates = closed_dates

    def is_business_day(self, day: date) -> bool:
        if day.weekday() not in self.open_weekdays:
            return False
        if day in self.closed_dates:
            return False
        return day not in observed_holidays(day.year)


def add_business_days(start: date, count: int, is_business_day) -> date:
    """Return the count-th business day after start (start itself is day 0)."""
    day = start
    while count > 0:
        day += timedelta(days=1)
        if is_business_day(day):
            count -= 1
    return day


def subtract_business_days(start: date, count: int, is_business_day) -> date:
    """Return the count-th business day before start (start itself is day 0)."""
    day = start
    while count > 0:
        day -= timedelta(days=1)
        if is_business_day(day):
            count -= 1
    return day


def _parse_date(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{text}' is not a date in YYYY-MM-DD form (example: 2026-03-02)"
        )


def _parse_weekdays(text: str) -> set[int]:
    names = [part.strip().lower()[:3] for part in text.split(",") if part.strip()]
    unknown = [name for name in names if name not in WEEKDAYS]
    if unknown or not names:
        raise argparse.ArgumentTypeError(
            "use comma-separated weekday names, for example mon,tue,wed,thu,fri"
        )
    return {WEEKDAYS.index(name) for name in names}


def _entry(key: str, label: str, day: date, rule: str, note: str = "") -> dict:
    return {
        "key": key,
        "label": label,
        "date": day.isoformat(),
        "weekday": day.strftime("%A"),
        "rule": rule,
        "note": note,
    }


def compute(args: argparse.Namespace) -> dict:
    general = GeneralCalendar(args.open_days, set(args.closed_date or []))
    dates: list[dict] = []
    warnings: list[str] = []

    le_sent = args.le_sent
    if args.application_date:
        le_due = add_business_days(args.application_date, 3, general.is_business_day)
        dates.append(_entry(
            "le_delivery_deadline",
            "Deliver or mail the Loan Estimate no later than",
            le_due,
            "12 CFR 1026.19(e)(1)(iii)(A)",
            "Third business day after the application is received (general definition).",
        ))
        if le_sent and le_sent > le_due:
            warnings.append(
                f"The Loan Estimate date {le_sent.isoformat()} is after the delivery "
                f"deadline {le_due.isoformat()}."
            )
        if le_sent and le_sent < args.application_date:
            warnings.append("The Loan Estimate date is before the application date.")

    if le_sent:
        earliest_close = add_business_days(le_sent, 7, is_specific_business_day)
        dates.append(_entry(
            "earliest_consummation",
            "Earliest consummation after the Loan Estimate waiting period",
            earliest_close,
            "12 CFR 1026.19(e)(1)(iii)(B)",
            "Seventh business day after the Loan Estimate was delivered or mailed "
            "(specific definition).",
        ))
        if args.consummation_date and args.consummation_date < earliest_close:
            warnings.append(
                f"Planned consummation {args.consummation_date.isoformat()} is before the "
                f"end of the seven-business-day waiting period ({earliest_close.isoformat()})."
            )

    if args.consummation_date:
        close = args.consummation_date
        if not is_specific_business_day(close):
            warnings.append(
                f"Planned consummation {close.isoformat()} is a Sunday or a legal public holiday."
            )
        cd_receipt = subtract_business_days(close, 3, is_specific_business_day)
        dates.append(_entry(
            "cd_receipt_deadline",
            "Consumer must receive the Closing Disclosure no later than",
            cd_receipt,
            "12 CFR 1026.19(f)(1)(ii)(A)",
            "Three business days before consummation (specific definition).",
        ))
        cd_send = subtract_business_days(cd_receipt, 3, is_specific_business_day)
        dates.append(_entry(
            "cd_send_deadline_if_not_in_person",
            "If not given in person, send the Closing Disclosure no later than",
            cd_send,
            "12 CFR 1026.19(f)(1)(iii)",
            "Presumed received three business days after it is mailed or delivered. "
            "Evidence of earlier actual receipt can be relied on instead.",
        ))
        revised_le_receipt = subtract_business_days(close, 4, is_specific_business_day)
        dates.append(_entry(
            "revised_le_receipt_deadline",
            "Consumer must receive any revised Loan Estimate no later than",
            revised_le_receipt,
            "12 CFR 1026.19(e)(4)(ii)",
            "Four business days before consummation (specific definition). A revised "
            "Loan Estimate cannot be provided on or after the Closing Disclosure date.",
        ))
        revised_le_send = subtract_business_days(
            revised_le_receipt, 3, is_specific_business_day
        )
        dates.append(_entry(
            "revised_le_send_deadline_if_not_in_person",
            "If not given in person, send any revised Loan Estimate no later than",
            revised_le_send,
            "12 CFR 1026.19(e)(1)(iv)",
            "Presumed received three business days after it is mailed or delivered.",
        ))

    if args.change_date:
        revised_due = add_business_days(args.change_date, 3, general.is_business_day)
        dates.append(_entry(
            "revised_le_delivery_deadline",
            "Deliver or mail the revised Loan Estimate no later than",
            revised_due,
            "12 CFR 1026.19(e)(4)(i)",
            "Within three business days of receiving information that establishes a "
            "valid reason for revision (general definition).",
        ))

    open_names = [WEEKDAYS[index] for index in sorted(args.open_days)]
    return {
        "inputs": {
            "application_date": args.application_date.isoformat() if args.application_date else None,
            "le_sent": le_sent.isoformat() if le_sent else None,
            "consummation_date": args.consummation_date.isoformat() if args.consummation_date else None,
            "change_date": args.change_date.isoformat() if args.change_date else None,
        },
        "assumptions": [
            "General business days: creditor open " + ", ".join(open_names)
            + "; closed on federal holidays as observed"
            + (" and on " + ", ".join(sorted(d.isoformat() for d in args.closed_date))
               if args.closed_date else "") + ".",
            "Specific business days: every day except Sundays and the legal public "
            "holidays in 5 U.S.C. 6103(a), counted on their actual dates.",
            "A new three-business-day waiting period is needed if the corrected Closing "
            "Disclosure has an inaccurate APR, a changed loan product or an added "
            "prepayment penalty (12 CFR 1026.19(f)(2)(ii)); this tool does not model that.",
        ],
        "dates": dates,
        "warnings": warnings,
        "disclaimer": "Planning aid only. A licensed professional must confirm every "
                      "date against the regulation, investor rules and state law.",
    }


def render_text(result: dict) -> str:
    lines = ["TRID timing (planning aid: confirm before relying on it)", ""]
    for item in result["dates"]:
        lines.append(f"{item['label']}:")
        lines.append(f"  {item['weekday']}, {item['date']}  [{item['rule']}]")
        if item["note"]:
            lines.append(f"  {item['note']}")
    if result["warnings"]:
        lines.append("")
        lines.append("Warnings:")
        lines.extend(f"  - {warning}" for warning in result["warnings"])
    lines.append("")
    lines.append("Assumptions:")
    lines.extend(f"  - {assumption}" for assumption in result["assumptions"])
    lines.append("")
    lines.append(result["disclaimer"])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compute TRID Loan Estimate and Closing Disclosure dates.",
        epilog="Example: trid_deadlines.py --application-date 2026-03-02 "
               "--consummation-date 2026-04-02",
    )
    parser.add_argument("--application-date", type=_parse_date,
                        help="Date the creditor received the application (YYYY-MM-DD).")
    parser.add_argument("--le-sent", type=_parse_date,
                        help="Date the Loan Estimate was delivered or mailed.")
    parser.add_argument("--consummation-date", type=_parse_date,
                        help="Planned consummation (closing) date.")
    parser.add_argument("--change-date", type=_parse_date,
                        help="Date the creditor received information establishing a "
                             "valid reason to revise the Loan Estimate.")
    parser.add_argument("--open-days", type=_parse_weekdays,
                        default={0, 1, 2, 3, 4},
                        help="Weekdays the creditor's offices are open "
                             "(default: mon,tue,wed,thu,fri).")
    parser.add_argument("--closed-date", type=_parse_date, action="append",
                        help="Extra date the creditor's offices are closed (repeatable).")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not (args.application_date or args.le_sent or args.consummation_date
            or args.change_date):
        parser.error("give at least one of --application-date, --le-sent, "
                     "--consummation-date or --change-date")
    result = compute(args)
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
