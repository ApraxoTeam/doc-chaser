---
name: drafting-client-reminders
description: Drafts document-request messages and follow-up reminder sequences that a tax, accounting, legal, mortgage or agency firm sends to a client who owes documents, signatures or payment. Use when the user says "chase this client", "the client still hasn't sent their documents", "write a reminder", "follow-up email for missing paperwork", "nudge for the signature", "overdue invoice reminder", or wants an email or text sequence for outstanding items. Do NOT use for marketing emails, debt collection demands or legal notices.
license: MIT
---

# Drafting client reminders

Write the messages that get a client to send what is missing: a first request, then reminders that get shorter and more specific, then a final notice that states the consequence.

**Important:** This skill writes drafts. It never sends a message. The professional reviews, edits and sends each one from their own system.

## What to find out

Work from what the user gives. Ask only for what is missing and changes the message:

- Who the client is, and what is outstanding (the specific items, not "your documents")
- The real deadline and what depends on it (a filing date, a closing date, a hearing, a launch)
- How the client should deliver (portal link, upload page, e-signature link)
- How many times the firm has already asked, and by which channel
- Channel wanted: email, text message or both

If the list of outstanding items is long, group it and lead with the item that blocks the most work.

## What every message must do

1. **Name the items.** List exactly what is missing. A client who reads "we still need a few things" does nothing.
2. **Give one action and one place.** One link or one instruction. Not three ways to send.
3. **State the date and the reason.** "By Friday March 6, so we can file before the deadline" beats "as soon as possible".
4. **Make it easy to reply with a problem.** One line: if an item does not apply or cannot be found, say so and the firm will sort it out.
5. **Sound like the firm.** Plain, warm and brief. No guilt, no exclamation marks, no "just checking in".

## Sequence

Use the default cadence in `references/sequences.md` unless the user gives their own or the deadline is close. Shorten the gaps when the deadline is near; never invent a deadline. Each reminder is shorter than the last and repeats only what is still missing.

The final notice states what the firm will do and when (file an extension, pause work, release the rate lock date, move the launch), as a fact and not a threat. Confirm the consequence with the user before writing it: do not invent one.

## Output

Give each message with its send day, channel, subject line and body. Keep text messages under 300 characters with no sensitive details. End with a short note listing anything assumed and anything the professional must confirm (deadline, consequence, link).

## Gotchas

- **Never put sensitive data in a message.** No Social Security numbers, account numbers or case details in email or text. Refer to "your 2025 W-2", not its contents.
- **Never ask a client to send sensitive documents by email or text.** Point to the portal or secure upload link. If the user has not given one, leave a clear placeholder `[secure upload link]`.
- **Text messages need prior consent.** Only draft texts for clients who have agreed to receive them; remind the user of that, and include how to opt out if the firm's texting tool does not add it.
- **Fees and penalties are the firm's call.** Mention a late fee, an extension fee or a penalty only if the user states it.
- **Mortgage and legal messages state facts, not advice.** Do not tell a borrower what a delay will do to their rate or approval, or tell a legal client what a missed deadline means for their case, unless the user supplies that wording.
- **Invoice reminders stay polite.** This skill is for ordinary overdue invoices from the firm's own clients. It does not write collection demands.
- **Match the client's language.** If the user says the client prefers another language, write in it and give the user an English version to check.
