<p align="center"><img src=".claude-plugin/icon.png" alt="Apraxo logo" width="120"></p>

# Doc Chaser by Apraxo

Skills for the paperwork side of a professional-services firm: asking clients for the right documents, chasing what is missing, and two compliance chores that small tax and mortgage shops put off.

> **Important:** This plugin helps with firm operations. It does not provide tax, legal, lending or compliance advice. Every output is a draft for a qualified professional to review, edit and send. Nothing is sent to a client and nothing is filed on anyone's behalf.

## What it does

| Skill | Use it when you say | What you get |
|---|---|---|
| `building-document-request-lists` | "What documents do I need from this client?" | A request list tailored to the client's situation, as Markdown or CSV |
| `reviewing-received-documents` | "Check what the client sent. What's still missing?" | Each item marked received, rejected or outstanding, with the exact resend instruction |
| `drafting-client-reminders` | "The client still hasn't sent their W-2. Write a reminder." | A first request, reminders and a final notice, for email or text |
| `estimating-chasing-cost` | "How much does chasing clients cost us?" | Hours and cost per year from your own numbers, with what-if scenarios |
| `drafting-wisp` | "I need a WISP for my tax practice." | A Written Information Security Plan draft in the IRS Publication 5708 structure, with gaps marked |
| `assessing-safeguards-readiness` | "Where do we stand on the FTC Safeguards Rule?" | A gap report: every requirement with its status and citation, and what to fix first |
| `calculating-trid-deadlines` | "When must the borrower have the CD for an April 2 closing?" | Loan Estimate and Closing Disclosure dates, each with its Regulation Z citation |
| `drafting-gift-letters` | "Her parents are gifting the down payment. Draft the gift letter." | A gift letter with the elements Fannie Mae requires, eligibility flags and the transfer evidence to collect |

Bundled request-list templates: individual tax return (Form 1040), bookkeeping onboarding, mortgage purchase, mortgage refinance, legal client intake and agency onboarding.

## Example prompts

- "New client has a W-2 job, a rental condo and sold some crypto. Build the document request list for their 1040 and give me a CSV."
- "Borrower is self-employed and getting a gift from her parents for the down payment. What goes on the needs list?"
- "Priya still owes us her brokerage 1099. Cut-off is April 3. Draft the next two reminders."
- "We have 320 clients and my admin spends about 50 minutes on each chasing documents, at $40 an hour. What does that cost a year?"
- "Draft our WISP. Three people, Drake on two desktops, clients email us documents, no MFA yet."
- "We mailed the LE on June 29. What's the earliest we can close?"
- "She uploaded a January pay stub and half a bank statement. What do I still need, and what do I tell her?"
- "Borrower's mother is wiring $20,000 for the down payment on a primary residence. Draft the gift letter."
- "Two-person tax shop, 400 clients, MFA on the tax software but not on email. Where do we stand on the Safeguards Rule?"

## Install

In Claude Code:

```bash
claude plugin marketplace add ApraxoTeam/doc-chaser
```

```bash
claude plugin install doc-chaser@apraxo-plugins
```

To try it from a local copy without installing:

```bash
claude --plugin-dir .
```

## Requirements

Python 3.9 or later for the five bundled scripts. They use the standard library only; there is nothing to install. The reminder, WISP and gift-letter skills need no scripts.

## What the plugin runs, sends and stores

- **Runs:** five Python scripts, only when a skill calls them: `build_request_list.py`, `request_status.py`, `chasing_cost.py`, `trid_deadlines.py` and `safeguards_gap.py`. Each is plain, readable source in its skill's `scripts/` folder.
- **Sends:** nothing. The plugin has no MCP servers, no hooks and no network calls. The scripts do not open network connections.
- **Stores:** nothing, unless you ask for a file. `build_request_list.py --output <file>` and `safeguards_gap.py --output <file>` write to the path you give, and `request_status.py set` updates the request-list CSV you point it at.
- **Collects:** no personal data, no analytics, no credentials. The skills tell Claude not to ask for passwords, account numbers or Social Security numbers.

Your conversation with Claude is handled under the terms of the Claude product you use; this plugin adds no data handling of its own.

## Where the content comes from

| Content | Source |
|---|---|
| Individual tax return list | IRS, [Gather your documents](https://www.irs.gov/filing/gather-your-documents) |
| Mortgage lists | CFPB, [Create a loan application packet](https://www.consumerfinance.gov/owning-a-home/prepare/create-a-loan-application-packet/); Fannie Mae Selling Guide [B3-4.3-04, Personal Gifts](https://selling-guide.fanniemae.com/sel/b3-4.3-04/personal-gifts) |
| WISP template | IRS [Publication 5708](https://www.irs.gov/pub/irs-pdf/p5708.pdf) (Rev. 8-2024), a US government work, adapted |
| Safeguards Rule questions and summary | FTC, [Safeguards Rule: What Your Business Needs to Know](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know); [16 CFR 314.4](https://www.law.cornell.edu/cfr/text/16/314.4) and [314.6](https://www.law.cornell.edu/cfr/text/16/314.6) |
| Gift letter rules | Fannie Mae Selling Guide [B3-4.3-04, Personal Gifts](https://selling-guide.fanniemae.com/sel/b3-4.3-04/personal-gifts) (topic dated 02/04/2026) |
| Retention reference | IRS, [How long should I keep records?](https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records) |
| TRID timing | Regulation Z, [12 CFR 1026.19](https://www.consumerfinance.gov/rules-policy/regulations/1026/19/) and [1026.2](https://www.consumerfinance.gov/rules-policy/regulations/1026/2/) |
| Bookkeeping, legal and agency lists; reminder cadence; document completeness checks | Common practice. No official source; edit them to fit your firm |

Sources were read on 2026-11-11. Rules and guides change: check the linked source before relying on a specific requirement. The adaptation of government material is not endorsed by any agency.

## Limits

- US federal sources only. No state tax, state bar, state breach-notification or Canadian rules.
- Mortgage lists are the common core. Lender, investor and loan-program rules add conditions.
- The TRID calculator does not model state waiting periods, rescission, timeshares or the restart of the Closing Disclosure waiting period.
- A WISP draft does not make a firm compliant. It must describe what the firm really does and be reviewed and signed by the firm.
- Gift letter checks follow Fannie Mae's rules for conventional loans. FHA, VA, USDA, Freddie Mac and portfolio loans differ.
- The Safeguards check is a self-assessment from your own answers. It is not an audit and never concludes that a firm complies.
- The document review checks completeness. It does not judge whether a document is genuine.
- The chasing-cost calculator uses your numbers only. It contains no industry benchmarks.

## Tests and evals

```bash
python3 -m unittest discover tests
```

```bash
claude plugin validate --profile directory --strict .
```

```bash
claude plugin eval . --allow-tools Bash Write
```

The unit tests check the scripts against worked examples from the Regulation Z official commentary. The `evals/` folder holds nine end-to-end cases with a no-plugin baseline.

## Support

Open an issue at https://github.com/ApraxoTeam/doc-chaser/issues

## About Apraxo

Apraxo builds client-portal software for professional-services firms: document requests, reminders, e-signature and payments in one place. This plugin works on its own and needs no Apraxo account.

## License

MIT. See [LICENSE](LICENSE). The Apraxo name and logo are trademarks of Apraxo and are not covered by the MIT licence. Material adapted from US government publications is in the public domain in the United States.
