---
name: drafting-wisp
description: Drafts a Written Information Security Plan (WISP) for a small tax, accounting or bookkeeping practice, following the IRS Publication 5708 sample structure and the FTC Safeguards Rule, by interviewing the firm and filling a bundled template. Use when the user says "I need a WISP", "write our information security plan", "data security plan for my tax practice", "PTIN renewal asks about a security plan", "Safeguards Rule compliance", or asks to update an existing WISP. Also usable by mortgage brokers covered by the Safeguards Rule. Do NOT use for SOC 2, HIPAA, PCI or enterprise security policies, or to certify that a firm is compliant.
license: MIT
---

# Drafting a WISP

Turn a short interview into a complete first draft of a firm's Written Information Security Plan, in the structure the IRS publishes for tax professionals.

**Important:** The result is a draft. It is not legal advice and it does not make a firm compliant. A plan only counts when it describes what the firm actually does, the owner and the Data Security Coordinator have reviewed and signed it, and the firm follows it.

## Workflow

1. **Check fit.** The template is written for a US tax or accounting practice. For a mortgage broker, keep the structure and replace tax-specific items (IRS Stakeholder Liaison, EFIN checks, tax software vendor) with the firm's own regulators and vendors. For other firms, say the Safeguards Rule may not apply to them (see `references/safeguards-rule.md`) and offer the plan as good practice.

2. **Interview.** Ask the questions below in two or three batches, not one at a time. Accept "not sure" and record it as an open item. If the user has an existing WISP or IT summary, read it first and ask only about gaps.

   - Firm name, owner name and title, number of people with access to client data
   - Who will be the Data Security Coordinator, and who speaks for the firm in an incident
   - What client information the firm holds, and every place it lives: tax software, client portal, cloud storage, email, laptops, paper files, backups
   - Who outside the firm can see client data: software vendors, IT provider, payroll, contractors
   - How clients send documents to the firm today
   - Sign-in security: multi-factor authentication on which systems, password manager, shared logins
   - Devices: computers, servers, phones, printers; encryption; who patches them
   - Remote work and remote access tools
   - Backups: where, how often, tested or not
   - Retention: how long client records are kept, and how they are destroyed
   - Cyber insurance carrier and legal counsel, if any
   - Effective date and annual review month

3. **Fill the template.** Read `assets/wisp-template.md` and replace every `{{PLACEHOLDER}}`. Write the firm's real practice, in the firm's words. Build the risk table from the answers: at least three risks, each with the current safeguard and any gap.

4. **Mark gaps honestly.** Where the firm has no answer or no safeguard, write `[TO COMPLETE: what is needed]`. Where the firm's practice falls short of a Safeguards Rule element (for example no multi-factor authentication), do not write that it complies. Record the gap in the risk table with an action and an owner.

5. **Check coverage.** Run the checklist at the end of `references/safeguards-rule.md`.

6. **Deliver.** Save the plan as a Markdown file (or the format the user asks for), then give a short summary: what is complete, the open `[TO COMPLETE]` items, and the gaps to fix first. Remind the user that the owner and the coordinator must review and sign it, staff must sign Attachment D, and it should be reviewed every year.

## Gotchas

- **Never invent a control.** If the user did not say backups are tested, the plan must not say they are. An inaccurate plan is worse than an incomplete one.
- **Never state that the firm is compliant** or that the plan satisfies the IRS or the FTC. Say what the plan covers and what remains open.
- **The retention period is the firm's decision.** Show the reference table in `references/safeguards-rule.md` and let them choose.
- **Do not drop attachments.** A through F are part of the plan. Empty tables get one example row marked as an example, or a `[TO COMPLETE]` note.
- **State breach laws are out of scope.** Say so, and tell the firm to check each state where its clients live.
- **Do not collect secrets.** Never ask for or record passwords, account numbers or client data. The plan names systems and practices, not credentials.
- **Updating an existing plan.** Keep the firm's wording where it still holds, change what has changed, and list the changes at the end so the coordinator can record them as an addendum.
