---
id: AWF-0004
name: Triage then remediate
kingdom: TEC
phylum: ITS
class: SRE
deliverable: incident-resolution
shape: "alert → route to runbook → each signal: investigate (metrics, logs, traces, deploys) → ranked hypotheses → 🛑 action → runbook step → check SLO → draft postmortem → 🛑 review → update runbook"
autonomy: checkpointed
checkpoints: [action, review]
patterns: [route, parallel]
variants: []
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Triage then remediate

`TEC › ITS › SRE` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `alert → route to runbook → each signal: investigate (metrics, logs, traces, deploys) → ranked hypotheses → 🛑 action → runbook step → check SLO → draft postmortem → 🛑 review → update runbook`

## Steps
1. An alert starts the agent, which routes by service tag to the matching runbook.
2. Read-only investigation runs in parallel: the error spike, deploys in the window, exemplar traces, and the suspect diff.
3. Post ranked hypotheses with evidence links to the incident channel.
4. 🛑 **Action**: the on-call engineer approves a specific runbook command (rollback, scale, restart).
5. Verify recovery against the SLO.
6. Draft the postmortem. 🛑 **Review**: the incident owner edits it, especially root cause and action items.
7. Update the runbook.

**Guard:** write tools are restricted to an allow-list of runbook commands, enforced in code.
