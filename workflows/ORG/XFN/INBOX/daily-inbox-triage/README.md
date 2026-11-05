---
id: AWF-0031
name: Daily inbox triage
kingdom: ORG
phylum: XFN
class: INBOX
deliverable: triaged-inbox
shape: "07:00 schedule: email, calendar, DMs → sort (action / FYI / delegate / archive) → each thread: reply saved as draft → meeting-slot proposals → top-5 brief → 🛑 action (a person sends every message and accepts every invite)"
autonomy: assist
checkpoints: [action]
patterns: [route, parallel]
variants: []
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Daily inbox triage

`ORG › XFN › INBOX` · assist · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `07:00 schedule: email, calendar, DMs → sort (action / FYI / delegate / archive) → each thread: reply saved as draft → meeting-slot proposals → top-5 brief → 🛑 action (a person sends every message and accepts every invite)`
**Guard:** inbound email is untrusted input (prompt-injection surface). The agent may never send on its own.
