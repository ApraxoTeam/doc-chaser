# Where the checklist items come from

Each item in `assets/checklists/*.json` has a `basis` field. This file says what each basis means and how far to trust it. Read it when a user asks where an item comes from or whether a list is complete.

| Basis | Source | Used in | What it covers |
|---|---|---|---|
| `irs` | IRS, "Gather your documents" (https://www.irs.gov/filing/gather-your-documents) | `tax-individual-1040` | Identity details, information returns (W-2, 1099 series, SSA-1099, 1095-A), deduction and credit records, self-employment records |
| `cfpb` | CFPB, "Create a loan application packet" (https://www.consumerfinance.gov/owning-a-home/prepare/create-a-loan-application-packet/) | `mortgage-purchase`, `mortgage-refinance` | Pay stubs (30 days), W-2s and signed federal returns (two years), two most recent bank statements, down payment source with two months' history, ID, Social Security number, name change documents, VA certificate of eligibility, counseling certificate |
| `fnma` | Fannie Mae Selling Guide B3-4.3-04, Personal Gifts (https://selling-guide.fanniemae.com/sel/b3-4.3-04/personal-gifts) | `mortgage-purchase` | Gift letter contents and acceptable evidence that the gift funds were transferred |
| `practice` | Common practice among small firms | All templates | Items with no single official source, such as engagement letters, software access and conflict-check details |

## Limits

- **Official sources are written for consumers.** They list what a typical filer or borrower gathers. A professional's engagement often needs more.
- **`practice` items are a starting point.** No regulator publishes them. The firm should edit them to match its own process.
- **Sources change.** The IRS and CFPB pages are updated without notice, and Fannie Mae revises the Selling Guide several times a year. Before relying on a specific requirement, open the source link and check it.
- **Fannie Mae rules apply to loans sold to Fannie Mae.** FHA, VA, USDA, Freddie Mac and portfolio loans have their own gift and documentation rules.
- **No state or provincial items.** State tax returns, state bar rules and Canadian requirements are not covered.

## Template file format

Add a template by placing a JSON file in `assets/checklists/`:

```json
{
  "id": "file-name-without-extension",
  "title": "Heading shown on the list",
  "industry": "tax | mortgage | legal | agency",
  "jurisdiction": "US federal",
  "note": "One or two sentences printed under the list.",
  "sources": {"practice": {"name": "Common practice", "url": ""}},
  "situations": {"tag": "Plain-language question the tag answers"},
  "sections": [
    {"name": "Section heading", "items": [
      {"id": "unique-id", "label": "What to ask for", "detail": "Optional clarification",
       "when": ["tag"], "basis": "practice"}
    ]}
  ]
}
```

An item with an empty `when` list is always included. An item with several tags is included when any one of them applies.
