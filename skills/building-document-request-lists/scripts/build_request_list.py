#!/usr/bin/env python3
"""Build a client document request list from a bundled checklist template.

Reads JSON templates from ../assets/checklists/, keeps the items that apply to
the client's situation, and prints Markdown, CSV or JSON. Standard library
only; no network access; writes a file only when --output is given.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "assets" / "checklists"


def load_templates() -> dict[str, dict]:
    templates = {}
    for path in sorted(TEMPLATE_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            sys.exit(f"Template {path.name} is not valid JSON: {error}")
        templates[data["id"]] = data
    if not templates:
        sys.exit(f"No checklist templates found in {TEMPLATE_DIR}")
    return templates


def describe_templates(templates: dict[str, dict]) -> str:
    lines = []
    for template in templates.values():
        lines.append(f"{template['id']}: {template['title']} "
                     f"({template['industry']}, {template['jurisdiction']})")
        for tag, question in template["situations"].items():
            lines.append(f"    {tag}: {question}")
    return "\n".join(lines)


def select_items(template: dict, situations: set[str], include_all: bool) -> list[dict]:
    """Keep items that always apply or match at least one chosen situation."""
    selected = []
    for section in template["sections"]:
        for item in section["items"]:
            conditions = item["when"]
            if include_all or not conditions or situations.intersection(conditions):
                selected.append({**item, "section": section["name"]})
    return selected


def source_name(template: dict, basis: str) -> str:
    return template["sources"].get(basis, {}).get("name", basis)


def render_markdown(template: dict, items: list[dict], client: str, due: str) -> str:
    lines = [f"# {template['title']}", ""]
    if client:
        lines.append(f"Client: {client}")
    if due:
        lines.append(f"Due: {due}")
    if client or due:
        lines.append("")
    current = None
    for item in items:
        if item["section"] != current:
            current = item["section"]
            lines += [f"## {current}", ""]
        line = f"- [ ] {item['label']}"
        if item["detail"]:
            line += f" ({item['detail']})"
        lines.append(line)
    lines += ["", "---", template["note"], "", "Sources:"]
    for source in template["sources"].values():
        lines.append(f"- {source['name']}" + (f": {source['url']}" if source["url"] else ""))
    return "\n".join(lines)


def render_csv(template: dict, items: list[dict]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["section", "item", "detail", "status", "source"])
    for item in items:
        writer.writerow([item["section"], item["label"], item["detail"], "requested",
                         source_name(template, item["basis"])])
    return buffer.getvalue().rstrip("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a client document request list from a checklist template.",
        epilog="Example: build_request_list.py --template tax-individual-1040 "
               "--situations wages,homeowner,itemizing --format csv",
    )
    parser.add_argument("--list", action="store_true",
                        help="Show every template and its situation tags, then exit.")
    parser.add_argument("--template", help="Template id, for example mortgage-purchase.")
    parser.add_argument("--situations", default="",
                        help="Comma-separated situation tags that apply to the client.")
    parser.add_argument("--all", action="store_true",
                        help="Include every item regardless of situation.")
    parser.add_argument("--client", default="", help="Client name for the heading.")
    parser.add_argument("--due", default="", help="Due date text for the heading.")
    parser.add_argument("--format", choices=["markdown", "csv", "json"], default="markdown")
    parser.add_argument("--output", help="Write to this file instead of standard output.")
    args = parser.parse_args(argv)

    templates = load_templates()
    if args.list:
        print(describe_templates(templates))
        return 0
    if not args.template:
        parser.error("give --template, or --list to see the choices")
    if args.template not in templates:
        parser.error(f"unknown template '{args.template}'. Choices: "
                     + ", ".join(templates))

    template = templates[args.template]
    situations = {tag.strip() for tag in args.situations.split(",") if tag.strip()}
    unknown = situations - set(template["situations"])
    if unknown:
        parser.error(f"unknown situation tags for {args.template}: "
                     + ", ".join(sorted(unknown)) + ". Valid tags: "
                     + ", ".join(template["situations"]))

    items = select_items(template, situations, args.all)
    if args.format == "markdown":
        text = render_markdown(template, items, args.client, args.due)
    elif args.format == "csv":
        text = render_csv(template, items)
    else:
        text = json.dumps({"template": template["id"], "title": template["title"],
                           "client": args.client, "due": args.due,
                           "situations": sorted(situations), "items": items,
                           "note": template["note"],
                           "sources": list(template["sources"].values())}, indent=2)

    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {len(items)} items to {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
