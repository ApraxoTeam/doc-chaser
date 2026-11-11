#!/usr/bin/env python3
"""Estimate what a firm spends chasing clients for documents.

Every number comes from the firm's own inputs. The script contains no industry
benchmarks; the reduction scenarios are illustrations, not predictions.
Standard library only; no network access.
"""

from __future__ import annotations

import argparse
import json
import sys


def positive(text: str) -> float:
    try:
        value = float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a number")
    if value < 0:
        raise argparse.ArgumentTypeError("the value cannot be negative")
    return value


def percent_list(text: str) -> list[float]:
    values = []
    for part in text.split(","):
        value = positive(part.strip())
        if value > 100:
            raise argparse.ArgumentTypeError("a reduction cannot exceed 100 percent")
        values.append(value)
    return values


def compute(clients: float, engagements: float, minutes: float, rate: float,
            reductions: list[float]) -> dict:
    hours = clients * engagements * minutes / 60
    cost = hours * rate
    scenarios = [
        {
            "reduction_percent": reduction,
            "hours_saved": round(hours * reduction / 100, 1),
            "cost_saved": round(cost * reduction / 100, 2),
        }
        for reduction in reductions
    ]
    return {
        "inputs": {
            "clients": clients,
            "engagements_per_client_per_year": engagements,
            "chasing_minutes_per_engagement": minutes,
            "hourly_rate": rate,
        },
        "annual_hours": round(hours, 1),
        "annual_cost": round(cost, 2),
        "cost_per_client": round(cost / clients, 2) if clients else 0.0,
        "full_time_weeks": round(hours / 40, 1),
        "scenarios": scenarios,
        "note": "Scenarios show what a given reduction would be worth. They are "
                "illustrations chosen by the user, not predicted results.",
    }


def render_text(result: dict) -> str:
    inputs = result["inputs"]
    lines = [
        "Cost of chasing clients for documents (from your inputs)",
        "",
        f"Clients: {inputs['clients']:g}",
        f"Engagements per client per year: {inputs['engagements_per_client_per_year']:g}",
        f"Chasing time per engagement: {inputs['chasing_minutes_per_engagement']:g} minutes",
        f"Hourly rate: {inputs['hourly_rate']:,.2f}",
        "",
        f"Hours per year: {result['annual_hours']:,.1f} "
        f"(about {result['full_time_weeks']:g} forty-hour weeks)",
        f"Cost per year: {result['annual_cost']:,.2f}",
        f"Cost per client: {result['cost_per_client']:,.2f}",
        "",
        "If chasing time fell by:",
    ]
    for scenario in result["scenarios"]:
        lines.append(
            f"  {scenario['reduction_percent']:g}%: {scenario['hours_saved']:,.1f} hours "
            f"and {scenario['cost_saved']:,.2f} saved per year"
        )
    lines += ["", result["note"]]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Estimate the yearly cost of chasing clients for documents.",
        epilog="Example: chasing_cost.py --clients 200 --minutes 45 --rate 85",
    )
    parser.add_argument("--clients", type=positive, required=True,
                        help="Number of active clients.")
    parser.add_argument("--engagements", type=positive, default=1,
                        help="Engagements per client per year that need documents "
                             "(default: 1).")
    parser.add_argument("--minutes", type=positive, required=True,
                        help="Staff minutes spent chasing documents per engagement.")
    parser.add_argument("--rate", type=positive, required=True,
                        help="Loaded hourly cost or billing rate of the staff who chase.")
    parser.add_argument("--reductions", type=percent_list, default=[25, 50, 75],
                        help="Comma-separated reduction scenarios in percent "
                             "(default: 25,50,75).")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    result = compute(args.clients, args.engagements, args.minutes, args.rate,
                     args.reductions)
    print(json.dumps(result, indent=2) if args.format == "json" else render_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
