---
name: assessing-safeguards-readiness
description: Runs a self-assessment of a firm against the FTC Safeguards Rule (16 CFR Part 314) and produces a gap report with each requirement's status, its citation and what to fix first, applying the small-firm exemption for firms with information on fewer than 5,000 consumers. Use when a tax preparer, bookkeeper, mortgage broker or other covered firm asks "are we compliant with the Safeguards Rule", "what does the FTC require for data security", "security checklist for my firm", "do we need MFA", or wants to know their gaps before writing or updating a WISP. Do NOT use for SOC 2, HIPAA, PCI, state privacy laws, or to certify compliance.
license: MIT
---

# Assessing Safeguards Rule readiness

Find out where a firm stands against each element of the FTC Safeguards Rule and give it a short, ordered list of what to fix.

**Important:** This is a self-assessment built from the firm's own answers. It is not an audit or legal advice, and it never concludes that a firm is compliant. A qualified professional should confirm the result.

## Workflow

1. **Check the rule applies.** It covers financial institutions under FTC jurisdiction; the FTC's guide names tax preparation firms, mortgage brokers, mortgage lenders, finance companies, collection agencies, and credit counselors and other financial advisors. For a law firm, agency or other business, say the rule may not apply to them and offer the assessment as a good-practice check.

2. **Ask how many consumers** the firm holds information on. Under 16 CFR 314.6, four requirements do not apply to firms with fewer than 5,000: the written risk assessment, continuous monitoring or penetration testing, the written incident response plan, and the annual report to the board.

3. **Get the answers.** Read `assets/questions.json` (path relative to this skill's directory). It holds every question with its `id`, `citation`, `element`, `fix`, `priority` and `exempt_under_5000` flag. Ask the questions in plain language in three or four batches, grouped by element. Record each as `yes`, `partial`, `no` or `unknown`:
   - `yes` only if the control is in place for every system that holds customer information
   - `partial` if it covers some systems or is informal and unwritten
   - `unknown` if the user is not sure, or was not asked. Never upgrade an unsure answer

   If the user has already described their setup (or has a WISP), fill in what that establishes and ask only about the rest.

4. **Work out each status.** Apply these rules in order to every question in the file; do not skip any:

   | Answer | Status |
   |---|---|
   | `yes` | in place |
   | anything else, and the firm has fewer than 5,000 consumers, and `exempt_under_5000` is true | not required at this size |
   | `partial` | partial |
   | `no` | gap |
   | `unknown` | unknown |

   If the number of consumers is not known, treat no question as exempt and say so. Exactly four questions carry the exemption flag: 314.4(b)(1), (d)(2), (h) and (i).

   Build the "Fix first" list from every item whose status is gap, unknown or partial. Order it by `priority` (1 first), then gap before unknown before partial. Give each item's element, status, citation and the `fix` text from the file.

5. **Present it.** Give a summary line with the count of each status, the "Fix first" list, and a table of every question with its status and citation. Open with one sentence saying this is a self-assessment from the firm's own answers, not an audit. Name the source: the FTC guide linked in the file. Add one or two sentences of context for the top gaps in the firm's own terms. Offer to draft or update the written plan with `drafting-wisp`.

## Gotchas

- **Never say the firm is compliant, or not compliant.** Report what is in place, partial, missing and unknown. Compliance is a legal conclusion.
- **Exempt does not mean unimportant.** For a small firm four items are "not required at this size". Say they are still good practice, especially the incident response plan, and never mark other items exempt.
- **"We have antivirus" is not an answer** to any single question. Map what the user says to the specific element, and ask when it does not clearly fit.
- **Multi-factor authentication means every system with customer information**, including email and cloud storage where client documents sit, not only the tax or loan software.
- **An unwritten practice is `partial`.** The rule requires a written program.
- **Do not collect secrets.** Ask whether a control exists, never for passwords, keys, account numbers or client data.
- **Other rules are out of scope.** State breach-notification laws, IRS e-file provider requirements, and lender or investor security requirements apply separately. Say so.
- **The rule can change.** The questions were built from the FTC's guide and 16 CFR 314.4 and 314.6 as read on 2026-11-11. The report links the source; tell the user to check it.
