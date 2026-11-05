---
id: AWF-0024
name: Playbook contract review
kingdom: PRO
phylum: LEG
class: CONTRACT
deliverable: contract-redline
shape: "contract → classify type → load playbook → each clause: compare to position (green/yellow/red) → tracked changes + comments → consistency check → 🛑 review → 🛑 sign-off → send"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [route, parallel]
variants: [harvey, spellbook, luminance, claude-playbook-skill]
tags: {risk: high}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Playbook contract review

`PRO › LEG › CONTRACT` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `contract → classify type → load playbook → each clause: compare to position (green/yellow/red) → tracked changes + comments → consistency check → 🛑 review → 🛑 sign-off → send`
**Variants:** `harvey` · `spellbook` · `luminance` · `claude-playbook-skill`

## Steps
1. Classify the agreement and load the matching playbook (standard positions, fallbacks, walk-away points per clause).
2. Segment the clauses, map each to a playbook entry, and flag missing clauses.
3. Analyze clauses in parallel for deviation.
4. Generate Word tracked changes with margin comments explaining each change.
5. Check internal consistency: defined terms, cross-references, liability caps vs. indemnities.
6. 🛑 **Review**: an attorney reviews yellow and red items.
7. 🛑 **Sign-off**: the attorney sends.
