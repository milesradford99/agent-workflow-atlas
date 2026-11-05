---
id: AWF-0025
name: Grounded legal memo
kingdom: PRO
phylum: LEG
class: RESEARCH
deliverable: research-memo
shape: "issue + jurisdiction → 🛑 plan → (search grounded database ⟲ draft IRAC memo) → each citation: verify exists, quote, holding, still good law → 🛑 sign-off"
autonomy: assist
checkpoints: [plan, sign-off]
patterns: [chain, parallel]
variants: []
tags: {risk: high}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Grounded legal memo

`PRO › LEG › RESEARCH` · assist · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `issue + jurisdiction → 🛑 plan → (search grounded database ⟲ draft IRAC memo) → each citation: verify exists, quote, holding, still good law → 🛑 sign-off`

## Steps
1. Frame the issue and jurisdiction. 🛑 **Plan**.
2. Search primary law in a grounded database (Westlaw/CoCounsel, Lexis+ AI, Harvey), not the open web.
3. Draft an IRAC memo with pinpoint cites.
4. **Run a separate verification pass on every citation**, including a citator check.
5. 🛑 **Sign-off**: the attorney reads every authority cited.

**Why the citation check is mandatory:** in *Mata v. Avianca* (S.D.N.Y., sanctions June 22, 2023), counsel submitted ChatGPT-fabricated opinions with fake quotes and citations [[24]](#sources).

## Sources

24. *Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023). https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
