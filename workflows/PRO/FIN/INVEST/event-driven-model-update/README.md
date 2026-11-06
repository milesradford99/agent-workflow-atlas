---
id: AWF-0023
name: Event-driven model update
kingdom: PRO
phylum: FIN
class: INVEST
deliverable: research-note
shape: "load consensus + guidance → new release, filing or transcript → each KPI: extract with citation → compare to model → update Excel drivers with per-cell comments → transcript themes → note → 🛑 review → 🛑 sign-off (compliance) → publish"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [parallel, chain]
variants: [claude-excel, hebbia, alphasense, rogo]
tags: {risk: medium}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Event-driven model update

`PRO › FIN › INVEST` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `load consensus + guidance → new release, filing or transcript → each KPI: extract with citation → compare to model → update Excel drivers with per-cell comments → transcript themes → note → 🛑 review → 🛑 sign-off (compliance) → publish`
**Variants:** `claude-excel` (Claude for Excel beta since October 2025 [[23]](#sources)) · `hebbia` · `alphasense` · `rogo`

## Public runs

Coverage as of 2026-11-06: **None found**: no public first-hand run yet. A real example run would be the first. From [Where are the real runs?](../../../../../research/2026-11-real-runs.md); every number was re-checked against its page.

- [Financial Datasets, *EarningsBench*](https://financialdatasets.ai/blogs/earningsbench) (2026-06-29). KPI extraction from 60 releases, checked by hand: a benchmark, not a model update. "Opus 4.6 with Extended Thinking hit 99.3% accuracy". *First-hand: no (benchmark); confidence: low.*

## Sources

23. VentureBeat, Claude for Financial Services (July 2025). https://venturebeat.com/ai/anthropic-rolls-out-claude-ai-for-finance-integrates-with-excel-to-rival · Anthropic, *Advancing Claude for Financial Services*. https://anthropic.com/news/advancing-claude-for-financial-services
