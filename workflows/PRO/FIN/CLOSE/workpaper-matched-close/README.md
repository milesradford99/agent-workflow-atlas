---
id: AWF-0038
name: Workpaper-matched close agents
kingdom: PRO
phylum: FIN
class: CLOSE
deliverable: closed-period-workpapers
shape: "prior-month workpaper + rules → each close area: pull source data → prep workpaper + checks → draft JEs + flux → flag exceptions → 🛑 review (controller reviews everything) → lock books → 🛑 sign-off (close)"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [parallel, chain]
variants: [promptql, puzzle-ai-close]
tags: {risk: medium}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Workpaper-matched close agents

`PRO › FIN › CLOSE` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `prior-month workpaper + rules → each close area: pull source data → prep workpaper + checks → draft JEs + flux → flag exceptions → 🛑 review (controller reviews everything) → lock books → 🛑 sign-off (close)`
**How it differs:** AWF-0022 Invoice extract-match-route (AP) handles single invoices. This produces period-end workpapers and journal entries across many accounts, with controller close sign-off.
**Variants:** `promptql` · `puzzle-ai-close`

## Steps
1. Seed each agent with last month's workpaper ('match this') and the accountant-set rules [[1]](#sources)[[2]](#sources).
2. Transaction matching runs all month. At close, separate agents handle accruals, leases, fixed assets, tax payables, prepaids, reconciliations, payroll, allocations, financials and P&L flux. Each has its own source data, workpaper, checks, journal entries and review points [[1]](#sources).
3. Agents prep workpapers and flag anything that looks off. The AI matches bank items and humans review only the exceptions [[1]](#sources)[[2]](#sources).
4. 🛑 **Review**: The controller feeds context, makes the calls, and reviews everything before close [[1]](#sources).
5. 🛑 **Sign-off**: The close is signed off after the AI has flagged anomalies [[2]](#sources).

**Output:** A closed period with completed workpapers and journal entries for each area, reviewed by the controller and ready for reporting and audit.
**Failure modes → guards:** Payroll timing variances still need chasing → human exception work [[1]](#sources). Agents with bank access → deliberately not granted [[1]](#sources). Bad automation scales errors → accountants set the rules and the AI executes them [[2]](#sources).

## Public runs

Coverage as of 2026-11-06: **Partial**: first-hand runs that cover part of the shape or put checkpoints elsewhere. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [David Kats, PromptQL close agents](https://www.linkedin.com/posts/katsdavid_three-months-ago-i-handed-promptql-a-prior-activity-7498398271866880000-EiIe) (2026-08-26). Assistant controller runs per-area close agents and reviews all output before close. "Now I have 17 agents running different pieces of finance.". *First-hand: yes; confidence: med.*
- [Puzzle, Debit & Co.](https://puzzle.io/case-studies/debit-co) (n.d.). Bookkeeping firm with AI matching and human exception review across client closes. "15 / 15 Clients closed by Day 4". *First-hand: vendor; confidence: med.*

## Sources

1. Kats D. (Assistant Controller, PromptQL), Three months ago I handed PromptQL a prior month's workpaper..., LinkedIn, 2026-08-26. https://www.linkedin.com/posts/katsdavid_three-months-ago-i-handed-promptql-a-prior-activity-7498398271866880000-EiIe
2. Puzzle, How Debit & Co. Closed 15 Clients by the 4th Business Day with Puzzle, n.d. https://puzzle.io/case-studies/debit-co
