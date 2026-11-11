---
name: calculating-trid-deadlines
description: Calculates TRID disclosure timing dates for a US residential mortgage (Loan Estimate delivery deadline, seven-business-day waiting period, Closing Disclosure receipt and mailing deadlines, revised Loan Estimate deadlines) with a holiday-aware script that applies both Regulation Z definitions of business day. Use when the user asks "when does the LE have to go out", "what's the earliest we can close", "when must the CD be received for a closing on a given date", "three-day rule", "can we still close Friday", or gives an application or closing date and wants the timeline. Do NOT use for rescission periods, HELOCs, reverse mortgages, rate-lock math or state-specific waiting periods.
license: MIT
---

# Calculating TRID deadlines

Work out the dates a loan officer or processor needs for the Loan Estimate (LE) and Closing Disclosure (CD), using a script so the business-day counting is exact.

**Important:** The output is a planning aid for a licensed professional to confirm. It is not legal or compliance advice, and it never replaces the creditor's own compliance system.

## Workflow

1. **Get the dates.** Any of these, in any combination:
   - Application date: the day the creditor received all six pieces of information that make an application
   - Date the LE was delivered or mailed
   - Planned consummation (closing) date
   - Date the creditor learned of a change that justifies a revised LE

2. **Ask one question if the LE deadline matters:** which days are the creditor's offices open? The LE delivery deadline uses the creditor's own business days. Default: Monday to Friday, closed on federal holidays as observed.

3. **Run the script.** Never count the days by hand.

   ```bash
   python3 scripts/trid_deadlines.py --application-date 2026-03-02 \
     --le-sent 2026-03-03 --consummation-date 2026-04-02
   ```

   Options: `--change-date` for a revised LE, `--open-days mon,tue,wed,thu,fri,sat` if the creditor is open Saturdays, `--closed-date YYYY-MM-DD` (repeatable) for extra closure days, `--format json`. The path is relative to this skill's directory.

4. **Report.** Give each date with its weekday and the rule it comes from, repeat any warnings the script printed, state the open-days assumption, and close with the reminder to confirm. If the planned closing breaks a waiting period, say so first.

## Gotchas

- **Two definitions of "business day".** The LE delivery deadline counts days the creditor is open. The waiting periods and the mail presumption count every day except Sundays and federal legal holidays, so **Saturdays count**. Mixing them up is the most common error. See `references/timing-rules.md`.
- **Observed holidays are business days for the waiting periods.** When July 4 falls on a Saturday, Friday July 3 still counts. The script handles this; do not "correct" it.
- **Application means six items**: name, income, Social Security number, property address, estimated property value and loan amount sought. The clock starts when the sixth arrives, not when the borrower signs a form.
- **Receipt, not sending, drives the CD rule.** The consumer must receive the CD three business days before consummation. The mail-by date applies only when there is no evidence of earlier receipt. For e-delivery, the creditor's proof of actual receipt can be used instead, but e-delivery needs valid E-Sign consent first.
- **Three changes restart the CD waiting period**: an APR that becomes inaccurate, a changed loan product, or an added prepayment penalty. The script does not model this. If the user mentions a CD change, name the three triggers and tell them to rerun with the corrected CD's date.
- **Waivers exist but are rare.** A consumer can waive a waiting period only for a bona fide personal financial emergency. Do not suggest it as a scheduling tool.
- **Consummation is not always closing.** It is when the consumer becomes contractually obligated, which state law defines. Use the date the user gives and say it was treated as the consummation date.
- **Out of scope:** state waiting periods, investor overlays, rescission, timeshares. Say so when relevant.
