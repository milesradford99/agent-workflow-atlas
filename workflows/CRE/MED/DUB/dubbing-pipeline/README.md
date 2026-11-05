---
id: AWF-0017
name: Dubbing pipeline
kingdom: CRE
phylum: MED
class: DUB
deliverable: localized-episode
shape: "episode + script → diarized ASR aligned to script → per-series glossary + cultural notes → 🛑 plan → each language: (translate ⟲ fits line duration) → voice-clone TTS → lip-sync → subtitles → 🛑 sample (native QA: eps 1–10 in full, then sampled) → 🛑 sign-off → publish"
autonomy: sampled
checkpoints: [plan, sample, sign-off]
patterns: [parallel, eval-opt]
variants: []
tags: {risk: medium}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Dubbing pipeline

`CRE › MED › DUB` · sampled · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `episode + script → diarized ASR aligned to script → per-series glossary + cultural notes → 🛑 plan → each language: (translate ⟲ fits line duration) → voice-clone TTS → lip-sync → subtitles → 🛑 sample (native QA: eps 1–10 in full, then sampled) → 🛑 sign-off → publish`
**Tags:** overseas (出海) apps. ReelShort and DramaBox made roughly $130M and $120M in IAP in Q1 2025 [[18]](#sources). Vendor claims for AI dubbing throughput (e.g. "120 minutes in 4–5 hours") are evidence B and unverified.

## Sources

18. Short-drama app revenue, Sensor Tower Q1 2025 data, via https://www.webull.com/news/12816921610159104 and https://gamebiz.jp/news/406943
