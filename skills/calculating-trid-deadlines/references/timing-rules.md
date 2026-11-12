# TRID timing rules behind the calculator

The rules and the counting procedure for TRID dates, with citations to Regulation Z (12 CFR Part 1026). Read this before computing any date. Regulation text: https://www.consumerfinance.gov/rules-policy/regulations/1026/19/ and https://www.consumerfinance.gov/rules-policy/regulations/1026/2/

## Business day: two definitions (1026.2(a)(6))

| Definition | Meaning | Applies to |
|---|---|---|
| General | A day on which the creditor's offices are open to the public for carrying on substantially all of its business functions | LE delivery deadline, 1026.19(e)(1)(iii)(A); revised LE delivery, 1026.19(e)(4)(i) |
| Specific | All calendar days except Sundays and the legal public holidays in 5 U.S.C. 6103(a) | LE waiting period (e)(1)(iii)(B); receipt presumptions (e)(1)(iv) and (f)(1)(iii); revised LE receipt (e)(4)(ii); CD timing (f)(1)(ii) |

Legal public holidays in 5 U.S.C. 6103(a): New Year's Day, Birthday of Martin Luther King Jr., Washington's Birthday, Memorial Day, Juneteenth National Independence Day, Independence Day, Labor Day, Columbus Day, Veterans Day, Thanksgiving Day, Christmas Day.

Comment 2(a)(6)-2: for the specific definition, a fixed-date holiday counts on its actual date. If July 4 is a Saturday and offices observe it on Friday July 3, that Friday is a business day. The comment names the four fixed-date holidays that existed when it was written; the script treats Juneteenth (added to 6103(a) in 2021) the same way.

## The rules

| Step | Rule | Citation | Definition |
|---|---|---|---|
| Deliver or mail the LE | No later than the third business day after the creditor receives the application | 1026.19(e)(1)(iii)(A) | General |
| Earliest consummation | LE delivered or mailed no later than the seventh business day before consummation | 1026.19(e)(1)(iii)(B) | Specific |
| LE or revised LE receipt when not in person | Considered received three business days after it is delivered or mailed | 1026.19(e)(1)(iv) | Specific |
| Deliver a revised LE | Within three business days of receiving information that establishes a valid reason for revision | 1026.19(e)(4)(i) | General |
| Last revised LE | Must be received no later than four business days before consummation; no revised LE on or after the day the CD is provided | 1026.19(e)(4)(ii) | Specific |
| CD receipt | Consumer must receive it no later than three business days before consummation | 1026.19(f)(1)(ii)(A) | Specific |
| CD receipt when not in person | Considered received three business days after it is delivered or mailed | 1026.19(f)(1)(iii) | Specific |
| New CD waiting period | Required if the APR becomes inaccurate, the loan product changes, or a prepayment penalty is added | 1026.19(f)(2)(ii) | Specific |

"Application" for these rules means the consumer's name, income, Social Security number to obtain a credit report, the property address, an estimate of the property's value and the loan amount sought (1026.2(a)(3)(ii)).

## Counting procedure

1. **"Nth business day after" a date:** the starting date is day 0. Move forward one calendar day at a time. Count a day only if it is a business day under the definition that applies. Stop at the Nth counted day.
2. **"N business days before" consummation:** consummation is day 0. Move back one calendar day at a time, counting only business days, and stop at the Nth.
3. **Specific definition:** skip Sundays and the dates in the holiday table below. Count every other day, Saturdays included.
4. **General definition:** count only days the creditor's offices are open. Default: Monday to Friday, skipping the days federal offices observe a holiday (a Saturday holiday is observed the Friday before; a Sunday holiday the Monday after). Use the creditor's own days if the user gives them.

Dates to compute, in order:

| Date | How |
|---|---|
| LE delivery deadline | 3rd general business day after the application date |
| Earliest consummation | 7th specific business day after the LE was delivered or mailed |
| CD receipt deadline | 3 specific business days before consummation |
| CD send-by date, if not given in person | 3 specific business days before the CD receipt deadline |
| Last revised LE receipt | 4 specific business days before consummation |
| Revised LE send-by date, if not given in person | 3 specific business days before that |
| Revised LE delivery deadline | 3rd general business day after the creditor learned of the change |

## Holiday table (5 U.S.C. 6103(a), actual dates)

| Holiday | Rule | 2026 | 2027 | 2028 |
|---|---|---|---|---|
| New Year's Day | January 1 | Thu Jan 1 | Fri Jan 1 | Sat Jan 1 |
| Birthday of Martin Luther King, Jr. | 3rd Monday of January | Jan 19 | Jan 18 | Jan 17 |
| Washington's Birthday | 3rd Monday of February | Feb 16 | Feb 15 | Feb 21 |
| Memorial Day | Last Monday of May | May 25 | May 31 | May 29 |
| Juneteenth | June 19 | Fri Jun 19 | Sat Jun 19 | Mon Jun 19 |
| Independence Day | July 4 | Sat Jul 4 | Sun Jul 4 | Tue Jul 4 |
| Labor Day | 1st Monday of September | Sep 7 | Sep 6 | Sep 4 |
| Columbus Day | 2nd Monday of October | Oct 12 | Oct 11 | Oct 9 |
| Veterans Day | November 11 | Wed Nov 11 | Thu Nov 11 | Sat Nov 11 |
| Thanksgiving Day | 4th Thursday of November | Nov 26 | Nov 25 | Nov 23 |
| Christmas Day | December 25 | Fri Dec 25 | Sat Dec 25 | Mon Dec 25 |

For other years, derive the dates from the Rule column. For the specific definition use the actual date in this table, never the observed weekday.

## Check cases

Use these to confirm a count or a piece of code before trusting it. The first is from official comment 19(e)(1)(iii)-2; the rest follow from the rules above.

| Input | Expected |
|---|---|
| LE mailed Monday 2015-06-01 | Earliest consummation Tuesday 2015-06-09 (Saturday June 6 counts) |
| Application received Monday 2015-06-01, creditor open Monday to Friday | LE delivery deadline Thursday 2015-06-04 |
| Application received Thursday 2026-07-02, creditor open Monday to Friday | LE delivery deadline Wednesday 2026-07-08 (Friday July 3 is the observed holiday, so the office is closed) |
| Consummation Thursday 2026-03-12 | CD received by Monday 2026-03-09; sent by Thursday 2026-03-05 if not in person; last revised LE received by Saturday 2026-03-07 |
| LE mailed Monday 2026-06-29 | Earliest consummation Wednesday 2026-07-08 (Friday July 3 counts; Saturday July 4 and Sunday July 5 do not) |
| Consummation Wednesday 2026-07-08 | CD received by Friday 2026-07-03 |

## Not modelled

State-law waiting periods, investor requirements, the timeshare exception in 1026.19(e)(1)(iii)(C), waiver for a bona fide personal financial emergency, rescission under 1026.23, and the restart of the CD waiting period under 1026.19(f)(2)(ii).
