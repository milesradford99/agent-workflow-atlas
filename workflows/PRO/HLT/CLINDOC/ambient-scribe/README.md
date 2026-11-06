---
id: AWF-0026
name: Ambient scribe
kingdom: PRO
phylum: HLT
class: CLINDOC
deliverable: clinical-note
shape: "🛑 plan (patient consent) → record visit → diarized transcript → load EHR context → note + codes + patient summary → link each sentence to transcript → 🛑 review → 🛑 sign-off → file to EHR"
autonomy: checkpointed
checkpoints: [plan, review, sign-off]
patterns: [chain]
variants: [abridge-epic, dragon-copilot, nabla, ambience]
tags: {risk: high}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Ambient scribe

`PRO › HLT › CLINDOC` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `🛑 plan (patient consent) → record visit → diarized transcript → load EHR context → note + codes + patient summary → link each sentence to transcript → 🛑 review → 🛑 sign-off → file to EHR`

## Steps
1. 🛑 **Plan**: patient consent to recording.
2. Ambient capture in the room or on a phone.
3. Diarized transcription, then a structured note in the specialty template.
4. Each note phrase links to its source audio or transcript. Abridge calls this "Linked Evidence," inside Epic Haiku → Hyperdrive [[26]](#sources).
5. 🛑 **Review**: the clinician edits.
6. 🛑 **Sign-off**: the clinician signs and is the legal author.

**Variants:** `abridge-epic` [[26]](#sources) · `dragon-copilot` (launched March 2025; combines Dragon Medical One dictation with DAX ambient [[25]](#sources)) · `nabla` · `ambience`
**Tags:** risk `high`, HIPAA, BAA required.

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. From [Where are the real runs?](../../../../../research/2026-11-real-runs.md); every number was re-checked against its page.

- [Taylor … Adams, UC Davis Health, JMIR Med Inform 2026;14:e86474](https://escholarship.org/content/qt9r89g3sp/qt9r89g3sp.pdf) (pilot Jul–Aug 2024). 31 physicians, 7,545 notes; 356 rated for omissions and hallucinations; physicians approve each note. "94.7% (337/356) free from significant errors"; "hallucinations (n=41, 11.5%)". *First-hand: yes; confidence: high.*

## Sources

25. Fierce Healthcare / Maginative on Dragon Copilot. https://www.maginative.com/article/microsoft-unveils-dragon-copilot-an-ai-assistant-for-clinicians/ · https://www.fiercehealthcare.com/ai-and-machine-learning/microsoft-debuts-dragon-copilot-ai-clinical-assistant-nurses-expands-access
26. Business Wire, *Abridge Inside with Epic Integration* (February 2024). https://www.businesswire.com/news/home/20240213503774/en
