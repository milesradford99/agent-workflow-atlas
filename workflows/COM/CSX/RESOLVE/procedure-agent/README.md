---
id: AWF-0021
name: Procedure agent
kingdom: COM
phylum: CSX
class: RESOLVE
deliverable: resolved-conversation
shape: "load KB + procedures → each message: route → info: answer | transaction: authenticate → 🛑 action (limits in code) → tool call | sensitive: 🛑 handoff → 🛑 sample (QA) → KB-gap clusters → new articles"
autonomy: sampled
checkpoints: [action, handoff, sample]
patterns: [route]
variants: []
tags: {risk: medium}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Procedure agent

`COM › CSX › RESOLVE` · sampled · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `load KB + procedures → each message: route → info: answer | transaction: authenticate → 🛑 action (limits in code) → tool call | sensitive: 🛑 handoff → 🛑 sample (QA) → KB-gap clusters → new articles`

## Steps
1. Rewrite tribal knowledge as natural-language procedures with explicit conditions and limits. Decagon AOPs compile these into workflows where refunds and identity checks run in code [[21]](#sources). Intercom Fin Procedures and Sierra journeys are equivalent variants.
2. Route each message by intent.
3. Authenticate before any account action.
4. 🛑 **Action**: limits are enforced in code, not in the prompt.
5. 🛑 **Handoff**: hand off with a summary.
6. 🛑 **Sample**: QA scores every conversation; humans review flagged and random ones.
7. Turn weekly KB-gap clusters into new articles.

**Metric caution:** resolution rates aren't defined the same way across vendors. Fin's site reportedly claims a 76% average, while independent and small-business tests cluster at 38–53% [[22]](#sources). Decagon customer figures above 70% come from an analyst write-up [[21]](#sources). All are evidence B.

## Sources

21. Decagon, *AOP*. https://decagon.ai/product/aop · Futurum Group (August 2025). https://futurumgroup.com/press-release/decagon-aims-to-simplify-ai-agent-development-with-natural-language/
22. Fin resolution-rate discussion: https://community.intercom.com/questions/3622 · https://superframeworks.com/articles/best-ai-customer-support-tools
