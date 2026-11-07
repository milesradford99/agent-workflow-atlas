---
id: AWF-0052
name: Propose-confirm pipeline sweep
kingdom: COM
phylum: SAL
class: REVOPS
deliverable: pipeline-exception-report
shape: "daily: read live CRM pipeline → reconcile conversations across Slack/email/calendar/notes → each open deal: dated next step with source, stale / past-close-date / thin-committee checks → run quality self-checks → publish exceptions view → 🛑 action (human confirms write-back) → 🛑 review (weekly pipeline review)"
autonomy: checkpointed
checkpoints: [action, review]
patterns: [parallel, chain]
variants: [claude-salesforce-mcp]
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Propose-confirm pipeline sweep

`COM › SAL › REVOPS` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `daily: read live CRM pipeline → reconcile conversations across Slack/email/calendar/notes → each open deal: dated next step with source, stale / past-close-date / thin-committee checks → run quality self-checks → publish exceptions view → 🛑 action (human confirms write-back) → 🛑 review (weekly pipeline review)`
**How it differs:** The DEAL workflow in this batch makes per-call, rep-approved updates. This one is a book-wide daily sweep owned by RevOps. AWF-0006 Governed query answers ad-hoc questions and does not maintain records.
**Variants:** `claude-salesforce-mcp`

## Steps
1. Every weekday, read the live pipeline, never an export or a saved copy [[1]](#sources).
2. Reconcile conversations across Slack, email, calendar and meeting notes so a relationship isn't flagged cold when someone spoke to the contact yesterday [[1]](#sources).
3. For every open deal, write a dated next step with its source, map the buying committee, and flag stalled deals, close dates already in the past, and missing signers [[1]](#sources).
4. Grade the run on fifteen quality checks and report the failures openly [[1]](#sources).
5. 🛑 **Action**: nothing is written back to Salesforce unless a person clicks [[1]](#sources).
6. 🛑 **Review**: the weekly pipeline review starts from the exceptions view instead of a hand-built deck [[1]](#sources).

**Output:** A daily exceptions view of the whole book, human-confirmed CRM corrections, and a ready pipeline review.
**Failure modes → guards:** Dashboards built on stale snapshots → read live records only [[1]](#sources). False 'cold' flags → reconcile across channels [[1]](#sources). Unsupervised writes damage trust → propose, then a human confirms write-back [[1]](#sources).

## Public runs

Coverage as of 2026-11-06: **Weak**: only anonymous, vendor-linked or journalist-told accounts. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Truffle Corp, Claudeforce on our Salesforce pipeline](https://www.trufflecorp.com/post/claudeforce-salesforce-pipeline) (2026-09-17). Consultancy ran a CRO agent on its own Salesforce for four months; human confirms write-back. "Contact categorization improved from 31% in July to 88% in August and 95% in September". *First-hand: vendor; confidence: med.*

## Sources

1. Truffle Corp, Claudeforce for Revenue Operations: We Put It on Our Salesforce Pipeline, 2026-09-17. https://www.trufflecorp.com/post/claudeforce-salesforce-pipeline
