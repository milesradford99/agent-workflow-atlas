---
id: AWF-0005
name: Alert enrich and adjudicate
kingdom: TEC
phylum: ITS
class: SECOPS
deliverable: alert-verdict
shape: "alert → each source: enrich (threat intel, identity, EDR) → verdict + evidence → benign: auto-close | suspicious: 🛑 handoff · weekly 🛑 sample"
autonomy: sampled
checkpoints: [handoff, sample]
patterns: [parallel, route]
variants: []
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Alert enrich and adjudicate

`TEC › ITS › SECOPS` · sampled · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `alert → each source: enrich (threat intel, identity, EDR) → verdict + evidence → benign: auto-close | suspicious: 🛑 handoff · weekly 🛑 sample`

## Steps
1. Normalize the alert.
2. Run enrichment lookups in parallel.
3. Investigate as an analyst would.
4. Return a verdict with confidence and evidence.
5. Auto-close benign alerts with the evidence attached.
6. 🛑 **Handoff**: send everything else to tier 2 as a prepared case.
7. 🛑 **Sample**: QA auto-closed alerts weekly.

**Metric:** analyst minutes per alert.
