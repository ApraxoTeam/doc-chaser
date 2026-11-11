---
name: drafting-gift-letters
description: Drafts a mortgage gift letter for a donor to sign, containing the elements the Fannie Mae Selling Guide requires, flags gift-fund problems before underwriting does, and lists the transfer evidence to collect. Use when the user says "gift letter", "the borrower's parents are giving them the down payment", "down payment gift", "what does the donor need to sign", or asks whether a gift is allowed or how to document gift funds. Do NOT use for gifts of equity, down payment assistance programs, seller concessions, or gift tax questions.
license: MIT
---

# Drafting gift letters

Produce a gift letter that is complete the first time, and catch the facts that would get the gift refused.

**Important:** This is a draft for the loan officer to review and for the donor to read and sign. It is not lending, legal or tax advice. The rules below are Fannie Mae's for conventional loans; the lender's own requirements control.

## Workflow

1. **Confirm the loan type.** The checks below follow Fannie Mae Selling Guide B3-4.3-04. For FHA, VA, USDA, Freddie Mac or portfolio loans, say that those programs have their own gift rules and letter requirements, draft the letter as a starting point, and tell the user to check the program's rules.

2. **Collect the facts.** Ask for whatever is missing, in one message:
   - Borrower name(s), property address, lender name
   - Donor's full name, address, telephone number and relationship to the borrower
   - The actual gift amount, or the maximum amount if not final
   - Occupancy (principal residence, second home, investment), number of units, and whether the loan-to-value ratio is above 80%
   - Where the donor's funds are held, and how and when they will be transferred
   - Whether the gift comes from a trust or estate

3. **Run the checks** in the table below. If one fails, stop and tell the user before drafting.

4. **Fill the template** in `assets/gift-letter-template.md`. Use `[TO COMPLETE]` for anything unknown; never invent a donor detail. For `{{AMOUNT_WORDING}}` write the actual amount in figures and words, or "up to" the maximum. Delete the trust or estate line unless it applies; if it does, name the trust or estate account.

5. **List the transfer evidence** to collect, matching how the money will move.

6. **Hand over** the full text of the letter in the reply (even when it is also saved to a file), then the evidence list and anything the loan officer must confirm.

## Checks before drafting

| Check | Rule (Fannie Mae B3-4.3-04) | If it fails |
|---|---|---|
| Occupancy | Gifts are allowed for a principal residence or second home. "Gifts are not allowed on an investment property." | Stop. Say the gift cannot be used on this loan as described |
| Donor | A relative (by blood, marriage, adoption or legal guardianship), or a non-relative with a familial relationship: a domestic partner or their relative, a person engaged to marry the borrower, a former relative, or someone with a long-standing familial-like or mentorship relationship | Flag for the loan officer; do not decide borderline relationships |
| Donor is not an interested party | The donor may not be, or be affiliated with, the builder, developer, real estate agent or any other interested party. A seller who is an acceptable donor and not affiliated with another interested party may give | Stop and flag |
| Borrower's own contribution | LTV, CLTV or HCLTV of 80% or less: none required. Above 80%: none for a one-unit principal residence; 5% from the borrower's own funds for a two- to four-unit principal residence or a second home | Tell the user the borrower needs 5% of their own funds before gift funds count |
| Use of funds | Gift funds may fund all or part of the down payment, closing costs or financial reserves | Flag any other use |

## Required letter contents

The letter must be signed by the donor and must:

1. Specify the actual or the maximum dollar amount of the gift
2. Include the donor's statement that no repayment is expected
3. Indicate the donor's name, address, telephone number and relationship to the borrower

A gift from a trust or estate: the letter is signed by the donor and lists the name of the trust or estate account. The template's remaining lines (source of funds, borrower signature, interested-party statement) are common lender requests, not Fannie Mae requirements; keep them unless the user says the lender does not want them.

## Transfer evidence

The lender must verify that the donor had the funds or that they were transferred. Acceptable evidence includes:

- A copy of the donor's check and the borrower's deposit slip
- A copy of the donor's withdrawal slip and the borrower's deposit slip
- Evidence of an electronic transfer from the donor's account to the borrower's account or to the closing agent
- A copy of the donor's check to the closing agent
- A settlement statement showing receipt of the donor's check

If the funds are not transferred before settlement, the lender must document that the donor gave the closing agent an electronic transfer, certified check, cashier's check or other official check.

## Gotchas

- **A loan is not a gift.** If the user describes any repayment, however informal, do not draft a gift letter. Say that funds to be repaid must be disclosed to the lender as a debt.
- **Never backdate or adjust facts.** The date is the signing date, the amount is the real amount, the relationship is the real one. If asked to change a fact so the gift qualifies, decline and say why.
- **Amount must match the money.** If the transfer differs from the letter's actual amount, a new letter is needed. Use "up to" wording when the final figure is not known.
- **Do not put account numbers in the letter** unless the lender requires them, and never in chat. The template names the institution and account type only.
- **A donor who has lived with the borrower for the last 12 months** and will share the home as a principal residence: the funds can count as the borrower's own. Flag this to the loan officer; it can remove the 5% problem.
- **Gifts of equity** follow a different topic (B3-4.3-05) and cannot fund reserves. Out of scope: say so.
- **Gift tax** is the donor's question for their own tax adviser. Do not estimate it or state thresholds.
- **The Selling Guide changes.** The rules here were read from the topic dated 02/04/2026. Link the source and tell the user to confirm: https://selling-guide.fanniemae.com/sel/b3-4.3-04/personal-gifts
