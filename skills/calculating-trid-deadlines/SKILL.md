---
name: calculating-trid-deadlines
description: Calculates TRID disclosure timing dates for a US residential mortgage (Loan Estimate delivery deadline, seven-business-day waiting period, Closing Disclosure receipt and mailing deadlines, revised Loan Estimate deadlines) with a holiday-aware counting method that applies both Regulation Z definitions of business day. Use when the user asks "when does the LE have to go out", "what's the earliest we can close", "when must the CD be received for a closing on a given date", "three-day rule", "can we still close Friday", or gives an application or closing date and wants the timeline. Do NOT use for rescission periods, HELOCs, reverse mortgages, rate-lock math or state-specific waiting periods.
license: MIT
---

# Calculating TRID deadlines

Work out the dates a loan officer or processor needs for the Loan Estimate (LE) and Closing Disclosure (CD), using a fixed counting method so the business-day counting is exact.

**Important:** The output is a planning aid for a licensed professional to confirm. It is not legal or compliance advice, and it never replaces the creditor's own compliance system.

## Workflow

1. **Get the dates.** Any of these, in any combination:
   - Application date: the day the creditor received all six pieces of information that make an application
   - Date the LE was delivered or mailed
   - Planned consummation (closing) date
   - Date the creditor learned of a change that justifies a revised LE

2. **Ask one question if the LE deadline matters:** which days are the creditor's offices open? The LE delivery deadline uses the creditor's own business days. Default: Monday to Friday, closed on federal holidays as observed.

3. **Count the days with the method in `references/timing-rules.md`.** Follow its counting procedure and holiday table exactly; do not estimate.
   - If a code execution tool is available, compute the dates in code that implements that procedure, and first confirm the code reproduces the check cases in the reference file.
   - Otherwise count on paper: list every calendar day in the span with its weekday, mark each one counted or skipped with the reason, and number the counted days. Keep that working out of the final answer unless the user asks for it.

4. **Check the result.** For each date, confirm the weekday matches the calendar date, no Sunday or listed holiday was counted in a waiting period, and Saturdays were counted. If the planned closing falls before the end of the Loan Estimate waiting period, or on a Sunday or legal holiday, say so.

5. **Report.** Give each date with its weekday and the rule it comes from, any warning from step 4, the open-days assumption, and close with the reminder to confirm. If the planned closing breaks a waiting period, say so first.

## Gotchas

- **Two definitions of "business day".** The LE delivery deadline counts days the creditor is open. The waiting periods and the mail presumption count every day except Sundays and federal legal holidays, so **Saturdays count**. Mixing them up is the most common error. See `references/timing-rules.md`.
- **Observed holidays are business days for the waiting periods.** When July 4 falls on a Saturday, Friday July 3 still counts. Do not "correct" this.
- **Application means six items**: name, income, Social Security number, property address, estimated property value and loan amount sought. The clock starts when the sixth arrives, not when the borrower signs a form.
- **Receipt, not sending, drives the CD rule.** The consumer must receive the CD three business days before consummation. The mail-by date applies only when there is no evidence of earlier receipt. For e-delivery, the creditor's proof of actual receipt can be used instead, but e-delivery needs valid E-Sign consent first.
- **Three changes restart the CD waiting period**: an APR that becomes inaccurate, a changed loan product, or an added prepayment penalty. If the user mentions a CD change, name the three triggers and recount from the date the corrected CD is received.
- **Waivers exist but are rare.** A consumer can waive a waiting period only for a bona fide personal financial emergency. Do not suggest it as a scheduling tool.
- **Consummation is not always closing.** It is when the consumer becomes contractually obligated, which state law defines. Use the date the user gives and say it was treated as the consummation date.
- **Out of scope:** state waiting periods, investor overlays, rescission, timeshares. Say so when relevant.
