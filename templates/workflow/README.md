---
id: AWF-0000                 # use the "next free id" printed by: python scripts/validate.py
name: Short plain name       # what a practitioner would call it
summary: "One sentence: what it produces and where a person approves (max 200 characters)."
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
last_verified: 2026-11       # month the sources and public runs were last re-opened
build: skill                 # skill | project | service | platform (STANDARD.md §3)
method_checked: 2026-11      # month the Build section was last compared with current agent tooling
---

# Short plain name

**Shape:** `copy the shape line here`

## Background

Three to six plain sentences for a reader from another field: what the job is, who does it and what triggers it; why it is slow or risky by hand; what the agent takes over and what stays with a person, and why. (STANDARD.md §2)

**Terms:**
- **term**: one-line definition. Define every trade term, abbreviation and Chinese industry term the entry uses.

## Build it with an agent

**Form:** `skill`. One sentence on why this is the smallest form that works.

**You need:** the files, connectors and permissions the agent must have before it starts.

| Step | Built as |
|---|---|
| step from the shape | the building block that does it (names from STANDARD.md §3) |

**Checkpoints:** `plan`: how the agent is made to stop and what the person sees. `review`: …

**Since the sources:** what the sources built by hand that tooling now provides, what this build leaves out, what still cannot be done. Or "Nothing material."

*A design based on this entry's steps and the tool documentation as of YYYY-MM, not a reported run.*

## Steps

*As reported by the sources.*

1. Start each step with who acts. …
2. … 🛑 **Plan**: who approves what, and what they check.
3. …

**Output:** what's delivered, and where it goes next.
**Failure modes → guards:** what goes wrong in practice, and what prevents it.
**How it differs:** from the nearest workflow (give its ID and name): the deliverable, checkpoint or autonomy difference that makes this its own entry (the swap test, TAXONOMY.md rule 4).

## Public runs

Coverage: **Strong**, **Partial**, **Weak** or **None found** (grades as in `research/2026-11-real-runs.md`). One line per first-hand public run of this workflow; leave the list empty if there are none yet.

- [Who, where](URL) (date). What the run shows. "A number, in the page's own words". *First-hand: yes, vendor, interview, anon or no; confidence: high, med or low.*

## Sources

1. Title, publisher, date. URL
