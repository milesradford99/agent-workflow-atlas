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

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. From [Where are the real runs?](../../../../../research/2026-11-real-runs.md); every number was re-checked against its page.

- [Goel & Tetali, Dashverse](https://insiders.dashverse.ai/building-an-ai-dubbing-pipeline-for-micro-dramas/) (2026-10-12). Diarized script rebuild → per-show glossary → duration-fit translation → cast TTS → human review of every show. "about 1,400 hours of micro-dramas across 16 languages"; reviewers kept "about 95%…89%…96%". *First-hand: yes; confidence: high.*
- [传神语联 via 数据猿, Tencent Cloud](https://developer.cloud.tencent.com/article/2708997) (Transn multilingual short-drama case, 2026-07-14). Story understanding → AI translation → post-edit with duration fit → voice-clone dubbing → AI and human QA. "每月配音短剧数量300部起，配音集数超2000集"; "AI负责约85%". *First-hand: vendor; confidence: med.*
- [娱乐资本论 on 钛媒体](https://www.tmtpost.com/7526126.html) (Who holds the key to AI dubbing?, 2025-04-08). A studio reruns a client drama through an AI dubbing tool, with human re-checks mandatory. "把一周的工作压缩到了一天". *First-hand: interview (studio unnamed); confidence: low.*

## Sources

18. Short-drama app revenue, Sensor Tower Q1 2025 data, via https://www.webull.com/news/12816921610159104 and https://gamebiz.jp/news/406943
