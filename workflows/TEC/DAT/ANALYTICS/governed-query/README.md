---
id: AWF-0006
name: Governed query
kingdom: TEC
phylum: DAT
class: ANALYTICS
deliverable: data-answer
shape: "question → load metric definitions + schema → (SQL ⟲ sanity checks) → chart + summary → 🛑 review → 🛑 sign-off → publish → save to golden queries"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [chain]
variants: []
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Governed query

`TEC › DAT › ANALYTICS` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `question → load metric definitions + schema → (SQL ⟲ sanity checks) → chart + summary → 🛑 review → 🛑 sign-off → publish → save to golden queries`

## Steps
1. Map business terms to governed metric definitions. If a term is ambiguous, ask instead of guessing.
2. Inspect the schema and sample rows.
3. Draft SQL, preferring the semantic layer.
4. Validate: sanity bounds, join fan-out (did row counts explode?), and reconciliation with a canonical dashboard total.
5. Chart the result and attach the SQL.
6. 🛑 **Review**: an analyst reviews the logic.
7. 🛑 **Sign-off**: required before the result goes to execs.
8. Save the verified query to the golden set for reuse.
