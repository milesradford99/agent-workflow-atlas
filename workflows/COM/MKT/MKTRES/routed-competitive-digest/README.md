---
id: AWF-0055
name: Routed competitive digest
kingdom: COM
phylum: MKT
class: MKTRES
deliverable: competitive-digest
shape: "weekly: pull last 7 days from deal channels + competitor-news channels + launch hub → triage against bar (repeat objection, confirmed public move, battlecard gap) → drop noise → structured digest, each item tagged to owning PMM with update recommendation → 🛑 review (CI lead) → 🛑 handoff (owning PMM updates battlecard)"
autonomy: checkpointed
checkpoints: [review, handoff]
patterns: [chain, route]
variants: [claude-cowork-skill-slack-notion]
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Routed competitive digest

`COM › MKT › MKTRES` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `weekly: pull last 7 days from deal channels + competitor-news channels + launch hub → triage against bar (repeat objection, confirmed public move, battlecard gap) → drop noise → structured digest, each item tagged to owning PMM with update recommendation → 🛑 review (CI lead) → 🛑 handoff (owning PMM updates battlecard)`
**How it differs:** AWF-0030 Issue-tree research builds a one-off strategy answer. This workflow is a recurring scan of internal deal signals routed to battlecard owners.
**Variants:** `claude-cowork-skill-slack-notion`

## Steps
1. Each week, pull from internal Slack channels (competitor news, deal collaboration, active deal rooms) and the Notion product launch hub, filtered to the last 7 days [[1]](#sources).
2. Triage against a written bar: an objection appearing in 2+ deals, a confirmed public move by a competitor, or a gap in an existing battlecard. Filter out one-off mentions [[1]](#sources).
3. Draft a structured digest. Tag each item to the PMM who owns that product area, with a recommendation on what to update and where [[1]](#sources).
4. 🛑 **Review**: the competitive-intel lead stays in the loop on the drafted digest posted to the PMM channel [[1]](#sources).
5. 🛑 **Handoff**: the owning PMM, as subject-matter expert, acts on the item and updates the battlecard [[1]](#sources).

**Output:** A weekly PMM-channel digest with owner-tagged battlecard updates.
**Failure modes → guards:** Noise floods the channel → an explicit triage bar [[1]](#sources). A single person is the bottleneck → route items to owner PMMs instead of a central analyst [[1]](#sources). Context limits on wide source pulls (raised by commenters) → limit the sources per run.

## Public runs

Coverage as of 2026-11-06: **Partial**: first-hand runs that cover part of the shape or put checkpoints elsewhere. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Andy McCotter-Bicknell, Apollo competitive intel skill](https://www.linkedin.com/posts/andrewmccotterbicknell_i-used-to-be-apollos-competitive-intel-bottleneck-activity-7447707923620724736-e1t7) (2026-04-08). Weekly Claude Cowork scan of Slack/Notion; digest routed to owning PMMs. "if an objection is showing up in 2+ deals". *First-hand: yes; confidence: med.*

## Sources

1. Andy McCotter-Bicknell (Apollo), I used to be Apollo's competitive intel bottleneck (LinkedIn), 2026-04-08. https://www.linkedin.com/posts/andrewmccotterbicknell_i-used-to-be-apollos-competitive-intel-bottleneck-activity-7447707923620724736-e1t7
