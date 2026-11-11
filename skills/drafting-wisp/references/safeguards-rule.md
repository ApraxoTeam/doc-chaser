# Safeguards Rule requirements and how the WISP covers them

Use this file to check a finished draft and to answer "is this required?" questions. Each fact names its source; open the source before relying on a detail.

## Contents

- Who is covered
- The nine required elements
- Small-firm exemption
- Breach notification
- IRS materials
- Record retention periods
- Coverage check

## Who is covered

The FTC Safeguards Rule (16 CFR Part 314) applies to financial institutions under FTC jurisdiction. The FTC's guide lists examples that include **tax preparation firms**, **mortgage brokers**, mortgage lenders, finance companies, collection agencies, and credit counselors and other financial advisors.
Source: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know

IRS Publication 5708 states that tax and accounting professionals are considered financial institutions under the rule "regardless of size" and that the plan "must be written and accessible".
Source: https://www.irs.gov/pub/irs-pdf/p5708.pdf

Law firms and agencies are generally not covered by this rule. A written security plan is still good practice for them, but do not tell them the FTC rule requires it.

## The nine required elements (16 CFR 314.4)

| # | Element | What the FTC guide says | WISP section |
|---|---|---|---|
| a | Qualified Individual | Designate one person to implement and supervise the program; may be an employee or a service provider | IV |
| b | Risk assessment | Written, with criteria for evaluating risks; repeated periodically | V |
| c | Safeguards | Access controls; data inventory; encryption at rest and in transit; app security review; multi-factor authentication; secure disposal no later than two years after last use (with exceptions); change management; logging of user activity | VI, VII, Attachments A, E, F |
| d | Monitoring and testing | Continuous monitoring, or annual penetration testing plus vulnerability assessments every six months | V, VII |
| e | Staff training | Security awareness training with refreshers | VII, Attachment D |
| f | Service provider oversight | Select capable providers, require safeguards by contract, reassess | IV, VI |
| g | Keep the program current | Update as operations, risks and personnel change | IV |
| h | Written incident response plan | Goals, roles, communications, remediation, documentation, post-incident review | VI, Attachment C |
| i | Report to the board | Written report at least annually to the board or a senior officer | Not in the template: add if the firm has a board or senior officer other than the DSC |

## Small-firm exemption

Under 16 CFR 314.6, four requirements do not apply to financial institutions that maintain customer information on fewer than 5,000 consumers: 314.4(b)(1) (the written risk assessment), (d)(2) (continuous monitoring, or annual penetration testing with six-monthly vulnerability assessments), (h) (the written incident response plan) and (i) (the annual written report to the board). Every other element still applies, including the Qualified Individual, the written program, multi-factor authentication and encryption.
Source: https://www.law.cornell.edu/cfr/text/16/314.6

A small firm's WISP should still include a risk table and breach procedures: IRS Publication 5708 includes both in its sample, and they cost little.

## Breach notification (16 CFR 314.4(j))

- Trigger: unauthorized acquisition of unencrypted customer information of at least 500 consumers
- Deadline: notify the FTC as soon as possible and no later than 30 days after discovery
- Encrypted data counts as unencrypted if the key was also accessed
- Method: the FTC's online reporting form

State breach-notification laws apply separately and have their own triggers and deadlines. The skill does not cover them: tell the firm to check each state where its clients live.

## IRS materials

| Publication | Use |
|---|---|
| Pub 5708 (Rev. 8-2024) | Sample WISP: the structure of the bundled template |
| Pub 4557, Safeguarding Taxpayer Data | Security checklist for tax professionals |
| Pub 1345 | Privacy and security standards for authorized e-file providers |
| Pub 5293 | Data security resource guide for tax professionals |

All are at https://www.irs.gov/pub/irs-pdf/ under their publication number, for example `p4557.pdf`.

## Record retention periods

Attachment A asks for a maximum retention period. The IRS periods for a taxpayer's own records are a common reference point (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records):

| Situation | Keep records |
|---|---|
| General case | 3 years |
| Claim for credit or refund filed after the return | 3 years from filing or 2 years from paying the tax, whichever is later |
| Loss from worthless securities or bad debt deduction | 7 years |
| Unreported income over 25% of gross income shown | 6 years |
| No return filed, or fraudulent return | Indefinitely |
| Employment tax records | 4 years after the tax is due or paid, whichever is later |

These are the taxpayer's periods. A preparer's own duties (for example keeping copies of returns or signed e-file authorizations), state rules, insurers and professional bodies may require different periods. Offer the table as context and let the firm choose the number; never fill it in for them.

## Coverage check

Before handing over a draft, confirm:

- [ ] A named Data Security Coordinator (Qualified Individual)
- [ ] At least three specific risks in the risk table, each with a safeguard or an action
- [ ] Multi-factor authentication stated for every system that holds PII, or a written exception approved by the DSC
- [ ] Encryption addressed for stored data and for data in transit
- [ ] Every service provider with PII access listed
- [ ] Retention period chosen by the firm
- [ ] Incident contacts filled in (insurer, counsel)
- [ ] Hardware and personnel tables have real rows
- [ ] No `{{PLACEHOLDER}}` remains; unresolved items read `[TO COMPLETE: ...]`
