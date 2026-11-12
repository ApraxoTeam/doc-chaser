---
name: estimating-chasing-cost
description: Calculates what a professional-services firm spends each year chasing clients for documents, signatures and answers, from the firm's own client count, time per engagement and hourly rate, and shows what a given reduction would be worth. Use when the user asks "how much does chasing clients cost us", "is a client portal worth it", "ROI of automated reminders", "how many hours do we lose to follow-ups", or wants a business case for fixing document collection. Do NOT use for pricing engagements, utilization or billable-rate calculations.
license: MIT
---

# Estimating chasing cost

Turn "we waste a lot of time chasing clients" into a number the firm can act on, using only the firm's own figures.

## Workflow

1. **Collect four inputs.** Ask for any the user has not given:
   - Active clients
   - Engagements per client per year that need documents (default 1)
   - Staff minutes spent chasing per engagement: writing requests, follow-ups, calls, checking what arrived, re-requesting wrong items
   - Hourly rate of the people who chase (loaded cost, or billing rate to show lost billable time; say which one was used)

   If the user does not know the minutes, help them estimate: follow-ups per client x minutes each, or hours per week during busy season x weeks, divided by clients. Label the result an estimate.

2. **Calculate.** Use these formulas and show the arithmetic in one line each so the reader can check it. If a code execution tool is available, compute with it.

   | Result | Formula |
   |---|---|
   | Hours per year | clients x engagements x minutes / 60 |
   | Cost per year | hours per year x hourly rate |
   | Cost per client | cost per year / clients |
   | Forty-hour weeks | hours per year / 40 |
   | Scenario saving | hours and cost x 25%, 50% and 75% (or the percentages the user asks for) |

   Check case: 200 clients, 1 engagement, 45 minutes, rate 85 gives 150 hours, 12,750 per year and 63.75 per client; a 50% reduction saves 75 hours and 6,375.

3. **Report it plainly.** Give hours per year, cost per year and cost per client, then the scenarios. State the inputs so the reader can challenge them.

4. **Offer the next step.** If the number is large, the levers are a specific request list (see the `building-document-request-lists` skill) and a consistent reminder sequence (see `drafting-client-reminders`).

## Gotchas

- **Never supply an industry benchmark for chasing time.** There is no reliable published figure. If the user asks for a typical number, say so and help them measure their own.
- **Scenarios are not predictions.** "If chasing time fell by 50%" shows what a reduction would be worth. Never say a tool or process will deliver it.
- **Do not double count.** If several staff chase, use total minutes per engagement across all of them with a blended rate, or calculate once per role and add the results.
- **Seasonal firms.** For a tax practice, minutes per engagement during the season is the right input; an annual weekly average hides the peak.
- **Currency.** Use the user's currency symbol; do not assume dollars if they named another.
- **Round at the end.** Keep full precision through the calculation, then round hours to one decimal and money to whole units.
