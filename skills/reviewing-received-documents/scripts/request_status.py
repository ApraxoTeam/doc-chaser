#!/usr/bin/env python3
"""Track which items on a document request list have arrived.

Works on the CSV written by build_request_list.py (columns: section, item,
detail, status, source). Adds a "note" column when needed. Standard library
only; no network access; changes only the CSV file it is given.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

STATUSES = ["requested", "received", "rejected", "not-applicable"]
REQUIRED = ["section", "item", "status"]


def read_rows(path: Path) -> tuple[list[str], list[dict]]:
    if not path.exists():
        sys.exit(f"File not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    missing = [name for name in REQUIRED if name not in fields]
    if missing:
        sys.exit(f"{path.name} is missing the column(s): {', '.join(missing)}. "
                 "Expected the CSV made by build_request_list.py.")
    if "note" not in fields:
        fields.append("note")
    for row in rows:
        row.setdefault("note", "")
        row["note"] = row["note"] or ""
        if row["status"] not in STATUSES:
            sys.exit(f"Unknown status '{row['status']}' for item '{row['item']}'. "
                     f"Use one of: {', '.join(STATUSES)}.")
    return fields, rows


def write_rows(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def find_row(rows: list[dict], selector: str) -> int:
    """Find a row by 1-based number or by a unique case-insensitive substring."""
    if selector.isdigit():
        index = int(selector) - 1
        if 0 <= index < len(rows):
            return index
        sys.exit(f"Row {selector} does not exist; the list has {len(rows)} items.")
    matches = [i for i, row in enumerate(rows) if selector.lower() in row["item"].lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        sys.exit(f"No item contains '{selector}'. Run the summary command to see the items.")
    options = "; ".join(f"{i + 1}: {rows[i]['item']}" for i in matches)
    sys.exit(f"'{selector}' matches several items. Use a row number instead. {options}")


def summary(rows: list[dict]) -> str:
    counts = {status: 0 for status in STATUSES}
    for row in rows:
        counts[row["status"]] += 1
    needed = len(rows) - counts["not-applicable"]
    lines = [
        f"{counts['received']} of {needed} items received"
        + (f" ({counts['not-applicable']} marked not applicable)"
           if counts["not-applicable"] else ""),
        "",
    ]
    for status, heading in (("rejected", "Rejected: client must resend"),
                            ("requested", "Still outstanding")):
        chosen = [(i, row) for i, row in enumerate(rows) if row["status"] == status]
        if not chosen:
            continue
        lines.append(f"{heading} ({len(chosen)}):")
        for i, row in chosen:
            note = f" -- {row['note']}" if row["note"] else ""
            lines.append(f"  {i + 1}. [{row['section']}] {row['item']}{note}")
        lines.append("")
    if counts["received"] == needed:
        lines.append("Everything needed has been received.")
    return "\n".join(lines).rstrip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Track the status of items on a document request list CSV.")
    commands = parser.add_subparsers(dest="command", required=True)

    show = commands.add_parser("summary", help="Show counts and what is outstanding.")
    show.add_argument("--csv", required=True, type=Path)

    update = commands.add_parser("set", help="Set the status of one item.")
    update.add_argument("--csv", required=True, type=Path)
    update.add_argument("--item", required=True,
                        help="Row number, or text that appears in exactly one item.")
    update.add_argument("--status", required=True, choices=STATUSES)
    update.add_argument("--note", default="",
                        help="Why it was rejected, or what was received.")

    args = parser.parse_args(argv)
    fields, rows = read_rows(args.csv)

    if args.command == "set":
        if args.status == "rejected" and not args.note:
            parser.error("a rejected item needs --note saying what the client must resend")
        index = find_row(rows, args.item)
        rows[index]["status"] = args.status
        rows[index]["note"] = args.note
        write_rows(args.csv, fields, rows)
        print(f"Row {index + 1} set to {args.status}: {rows[index]['item']}")
        print()

    print(summary(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
