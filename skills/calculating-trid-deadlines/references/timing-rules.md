# TRID timing rules behind the calculator

The rules `scripts/trid_deadlines.py` applies, with citations to Regulation Z (12 CFR Part 1026). Read this when a user asks why a date came out the way it did. Regulation text: https://www.consumerfinance.gov/rules-policy/regulations/1026/19/ and https://www.consumerfinance.gov/rules-policy/regulations/1026/2/

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

## Worked example from the official commentary

Comment 19(e)(1)(iii)-2: an LE mailed on Monday, June 1 allows consummation on or after Tuesday, June 9, the seventh business day after mailing, because Saturday counts. The script reproduces this:

```bash
python3 scripts/trid_deadlines.py --le-sent 2015-06-01
```

## How the script counts

- "Nth business day after" a date: the date itself is day 0; count forward N business days.
- "N business days before" consummation: consummation is day 0; count back N business days.
- Mail-by dates: count back three more specific business days from the receipt deadline.

## Not modelled

State-law waiting periods, investor requirements, the timeshare exception in 1026.19(e)(1)(iii)(C), waiver for a bona fide personal financial emergency, rescission under 1026.23, and the restart of the CD waiting period under 1026.19(f)(2)(ii).
