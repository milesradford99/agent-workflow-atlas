---
id: AWF-0033
name: Coordinator-reviewed prescreen
kingdom: PRO
phylum: HLT
class: CLINTRIAL
deliverable: prescreen-worklist
shape: "onboard trial (PI amends IRB, criteria chosen) → 🛑 plan → each patient: label each criterion + rationale + source note → rank by % met → 🛑 review (coordinator rules on each criterion) → (update criterion prompt ⟲ coordinator agreement) → 🛑 handoff (trial team approach + consent)"
autonomy: checkpointed
checkpoints: [plan, review, handoff]
patterns: [chain, route, eval-opt]
variants: [rag-gpt-ehr-pipeline, neurosymbolic-abstraction]
tags: {risk: high}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Coordinator-reviewed prescreen

`PRO › HLT › CLINTRIAL` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `onboard trial (PI amends IRB, criteria chosen) → 🛑 plan → each patient: label each criterion + rationale + source note → rank by % met → 🛑 review (coordinator rules on each criterion) → (update criterion prompt ⟲ coordinator agreement) → 🛑 handoff (trial team approach + consent)`
**How it differs:** AWF-0009 Screening funnel (LITREV) screens papers for a review. This screens patients against live trial criteria, with per-criterion coordinator confirmation and an enrollment handoff.
**Variants:** `rag-gpt-ehr-pipeline` · `neurosymbolic-abstraction`

## Steps
1. Onboarding: the PI amends the trial's IRB-approved protocol to add AI-team members as study personnel. The study team selects the criteria to automate, split into two tiers. Approach, consent and enrollment decisions stay with the trial team [[1]](#sources).
2. 🛑 **Plan**: The study team signs off the criteria configuration before prescreening starts [[1]](#sources).
3. A retrieval-augmented LLM reads structured EHR data and free-text notes. It labels each criterion met, likely met, likely not met, not met, uncertain, or no documentation found, with a rationale, a confidence level and the note ID/date of the evidence [[1]](#sources).
4. Patients above a threshold share of met or likely-met criteria go to a sorted coordinator dashboard. Coordinators must review those meeting ≥50% of criteria at first, tightening to ≥75% as performance improves. Reminders fire if a patient is not reviewed within four days [[1]](#sources).
5. 🛑 **Review**: Coordinators mark each criterion met, not met or insufficient data, and give a reason when they disagree with the AI. Discordances get junior-to-senior re-assessment or senior single-reviewer adjudication [[1]](#sources).
6. Coordinator feedback updates the criteria prompts. Missed patients trigger fixes to the workflow or the AI logic [[1]](#sources).
7. 🛑 **Handoff**: The study team sets each patient's status (prescreen success/failure, screening, enrolled) and owns approach and consent [[1]](#sources).

**Output:** A per-trial ranked prescreen worklist with criterion-level evidence. Confirmed candidates go to the trial team for approach and consent.
**Failure modes → guards:** Lower specificity (0.81) produces false positives → coordinators confirm every criterion [[1]](#sources). Automation bias limited accuracy in some criteria domains in a randomized trial → keep human abstraction and an adjudication step [[2]](#sources). Speed gains may not appear: time per chart was 37.4 vs 37.8 min [[2]](#sources).

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Dohopolski et al., UTSW human-in-the-loop prescreening](https://doi.org/10.64898/2026.03.20.26348890) (2026-03-27). Prospective deployment across 26 active trials, with coordinator review and prompt updates from feedback. "39,182 patients were prescreened by our LLM-workflow across 26 (21 oncology and 5 non-oncology) studies". *First-hand: yes; confidence: high.*
- [Parikh et al., Human-AI prescreening RCT](https://www.nature.com/articles/s41467-026-68873-8) (2026-02-03). Randomized comparison of coordinators with and without AI annotations on 355 charts. "Human-alone (76.5% vs. 71.1%)". *First-hand: study (randomized, on past records; funded by the AI vendor Mendel.ai); confidence: high.*

## Sources

1. Dohopolski M.J. et al. (UT Southwestern), Implementation of Human-in-the-Loop ChatGPT-based Patient Screening Across Multiple Diverse Clinical Trials, medRxiv, 2026-03-27. https://doi.org/10.64898/2026.03.20.26348890
2. Parikh R.B. et al., Human-AI teaming to improve accuracy and efficiency of eligibility criteria prescreening for oncology trials, Nature Communications, 2026-02-03. https://www.nature.com/articles/s41467-026-68873-8
