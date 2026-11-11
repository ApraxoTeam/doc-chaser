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

2. **Run the calculation.** Do not do the arithmetic by hand.

   ```bash
   python3 scripts/chasing_cost.py --clients 200 --engagements 1 --minutes 45 --rate 85
   ```

   Options: `--reductions 30,60` to change the scenarios, `--format json` for structured output. The path is relative to this skill's directory.

3. **Report it plainly.** Give hours per year, cost per year and cost per client, then the scenarios. State the inputs so the reader can challenge them.

4. **Offer the next step.** If the number is large, the levers are a specific request list (see the `building-document-request-lists` skill) and a consistent reminder sequence (see `drafting-client-reminders`).

## Gotchas

- **Never supply an industry benchmark for chasing time.** There is no reliable published figure. If the user asks for a typical number, say so and help them measure their own.
- **Scenarios are not predictions.** "If chasing time fell by 50%" shows what a reduction would be worth. Never say a tool or process will deliver it.
- **Do not double count.** If several staff chase, use total minutes per engagement across all of them with a blended rate, or run the script once per role and add the results.
- **Seasonal firms.** For a tax practice, minutes per engagement during the season is the right input; an annual weekly average hides the peak.
- **Currency.** The script prints plain numbers. Add the user's currency symbol in the write-up.
