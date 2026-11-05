---
id: AWF-0000                 # use the "next free id" printed by: python scripts/validate.py
name: Short plain name       # what a practitioner would call it
kingdom: TEC                 # TAXONOMY.md §4, first matching row
phylum: SWE
class: FEAT
deliverable: pull-request    # the thing that leaves the workflow, as a short noun
shape: "step → step → 🛑 plan → each item: (make ⟲ check) → 🛑 review → deliver"
autonomy: checkpointed       # assist | checkpointed | sampled
checkpoints: [plan, review]  # must match the 🛑 words in shape
patterns: [chain]            # chain | route | parallel | orch-workers | eval-opt | auto-loop | role-crew | computer-use
variants: []                 # toolchain slugs, e.g. [claude-code, codex-cli]
tags: {risk: low}            # optional: industry, region, lang; risk is low | medium | high
evidence: B                  # A public detailed write-up · B vendor docs or numbers · C community report
status: draft                # stays draft until a reference example exists
reference_example: null      # e.g. examples/2026-11-my-team/
inputs_from: []              # optional: ids of upstream workflows
merged_into: null
last_verified: 2026-11
---

# Short plain name

One or two sentences: who does this, and what it produces.

**Shape:** `copy the shape line here`

- **Input:** what the workflow starts from, including the context files the agent needs.
- **Roles/Tools:** each agent or tool and what it's responsible for.

## Steps

1. …
2. … 🛑 **Plan**: who approves what, and what they check.
3. …

**Output:** what's delivered, and where it goes next.
**Failure modes → guards:** what goes wrong in practice, and what prevents it.
**How it differs from [nearest workflow](../path/):** the deliverable, checkpoint or autonomy difference that makes this its own entry (the swap test, TAXONOMY.md rule 4).

## Sources

1. Title, publisher, date. URL
