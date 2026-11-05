---
id: AWF-0011
name: Bible-driven novel draft
kingdom: CRE
phylum: WRI
class: FICTION
deliverable: novel-manuscript
shape: "premise + voice samples → story bible via interview → 🛑 plan → beats → chapters → scene cards → 🛑 plan → each scene in order: load card, bible, summary, last ~2k words → draft → continuity check → style check → 🛑 review → update bible and summary"
autonomy: assist
checkpoints: [plan, review]
patterns: [role-crew, eval-opt]
variants: []
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Bible-driven novel draft

`CRE › WRI › FICTION` · assist · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `premise + voice samples → story bible via interview → 🛑 plan → beats → chapters → scene cards → 🛑 plan → each scene in order: load card, bible, summary, last ~2k words → draft → continuity check → style check → 🛑 review → update bible and summary`

| Role | Responsibility | Variants |
|---|---|---|
| Bible keeper | Characters, places, timeline, rules | Sudowrite Story Bible, a guided pipeline from braindump → synopsis → outline → scenes [[10]](#sources); NovelCrafter Codex, wiki entries linked into the manuscript with bring-your-own model [[10]](#sources); Markdown vault + Claude Code |
| Outliner | Beats → scene cards (goal, conflict, outcome, POV, information revealed) | Same |
| Drafter | Scene prose | LLM with long context |
| Continuity checker | Fresh context; flags contradictions (eye color, travel time, premature knowledge) | Separate agent |
| Line editor | Style sheet: banned clichés, POV, tense | Critic agent |

**Checkpoints:** 🛑 the author owns the bible and the outline (both **Plan**), where most creative control is exercised. The author also rewrites every chapter (**Review**).
**Tag note:** Amazon KDP requires disclosure of AI-*generated* text, images, and translations, even when heavily edited afterward. Purely AI-*assisted* work doesn't need disclosure [[11]](#sources). Record which applies in each example.

## Sources

10. Sudowrite, *Story Bible template*. https://sudowrite.com/blog/story-bible-template/ · *Sudowrite vs NovelCrafter (2026)*. https://www.inkfluenceai.com/blog/sudowrite-vs-novelcrafter-2026
11. Authors Guild, *Amazon's new disclosure policy for AI-generated book content* (September 2023). https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/
