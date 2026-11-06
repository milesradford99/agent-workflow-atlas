---
id: AWF-0086
name: Template-driven meeting minutes
kingdom: ORG
phylum: XFN
class: MEET
deliverable: approved-meeting-minutes
shape: "record or upload meeting audio → transcribe with speaker labels → choose meeting template → generate minutes → (AI-chat edits ⟲ 🛑 review (officer corrects)) → export Word → circulate"
autonomy: assist
checkpoints: [review]
patterns: [chain, eval-opt]
variants: [iai-minute, justice-transcribe]
tags: {region: [UK], risk: low}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Template-driven meeting minutes

`ORG › XFN › MEET` · assist · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `record or upload meeting audio → transcribe with speaker labels → choose meeting template → generate minutes → (AI-chat edits ⟲ 🛑 review (officer corrects)) → export Word → circulate`
**How it differs:** AWF-0026 Ambient scribe produces clinical notes under clinical sign-off. This workflow produces general government meeting minutes reviewed by an officer, at low risk.
**Variants:** `iai-minute` · `justice-transcribe`

## Steps
1. Upload the meeting recording. Audio is converted and stored behind a time-limited upload link [[2]](#sources).
2. Transcribe it with speech-to-text, choosing the provider by duration and quality [[2]](#sources).
3. Choose a template: Cabinet meeting, planning committee, care assessment, general meeting, or a custom one [[2]](#sources).
4. The LLM structures the conversation into minutes, applying government tense, grammar and format rules [[2]](#sources).
5. 🛑 **Review**: the officer tweaks and corrects the summary before it is used [[1]](#sources).
6. Circulate the final minutes and pick up follow-up work. In councils this was aimed at speeding up actions after planning meetings and recording supervision sessions [[1]](#sources).

**Output:** Corrected minutes, exported and circulated as the meeting record. Follow-up actions are taken from them by officers.
**Failure modes → guards:** Wrong or misattributed statements → the officer corrects them before circulation. Sensitive meetings → handle data at the right classification, and don't retain audio. Action tracking is not documented as a tool feature, so treat action extraction as manual or template-dependent. The time saving comes from early central-government tests, not an independent evaluation [[1]](#sources).

## Public runs

Coverage as of 2026-11-06: **Partial**: first-hand runs that cover part of the shape or put checkpoints elsewhere. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [GOV.UK, Humphrey helps townhalls](https://www.gov.uk/government/news/ai-experiments-see-humphrey-help-townhalls-cut-costs-and-improve-services) (2025-05-23). Minute trialled by 25 councils, including West Berkshire and Stockton-on-Tees, for planning and social care meetings. "officials are saved from 60-minutes of admin for each hour-long meeting". *First-hand: yes; confidence: low.*

## Sources

1. GOV.UK press release, AI experiments see Humphrey help townhalls cut costs and improve services, 2025-05-23. https://www.gov.uk/government/news/ai-experiments-see-humphrey-help-townhalls-cut-costs-and-improve-services
2. i.AI, minute (GitHub README), accessed 2026-11. https://github.com/i-dot-ai/minute
