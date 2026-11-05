---
id: AWF-0020
name: Research-then-personalize outbound
kingdom: COM
phylum: SAL
class: PROSPECT
deliverable: outbound-sequence
shape: "ICP → build list → each account: waterfall enrichment → research agent answers fixed questions with source URLs → score and tier → each contact: first line from research only → 🛑 plan (20-row sample) → 🛑 sample (5–10%) → 🛑 action → launch sequence → route replies"
autonomy: checkpointed
checkpoints: [plan, sample, action]
patterns: [parallel, chain]
variants: []
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Research-then-personalize outbound

`COM › SAL › PROSPECT` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `ICP → build list → each account: waterfall enrichment → research agent answers fixed questions with source URLs → score and tier → each contact: first line from research only → 🛑 plan (20-row sample) → 🛑 sample (5–10%) → 🛑 action → launch sequence → route replies`
**Practitioner pattern:** run cheap enrichment first, and spend agent-research credits (Claygent) only on accounts that fit the ICP [[20]](#sources).

## Sources

20. Lindy, *Clay review*. https://wf.lindy.ai/blog/clay-review
