---
type: llm
weight: 1
---

Pass only if ALL of these hold:
- The response is a document request list for an individual US tax return.
- It asks for Form W-2, home mortgage interest and property tax records, and brokerage statements or Form 1099-B.
- It asks for last year's tax return or other new-client items, because the client is new.
- It does NOT ask for unrelated items such as Form SSA-1099, Form W-2G or Form 1095-A.
- It says the list is a draft for the preparer to review, or names items the preparer should confirm.
- It does not tell the preparer to collect Social Security numbers by ordinary email.
