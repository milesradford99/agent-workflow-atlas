---
id: AWF-0060
name: Spec-to-ticket planning
kingdom: TEC
phylum: PRD
class: PM
deliverable: ticketed-project-plan
shape: "spec in docs → agent reads spec + codebase → draft breakdown (tasks, order, deps, touched files) → 🛑 plan (push back, iterate) → create project + tickets in tracker via MCP → 🛑 review (PM + eng) → 🛑 handoff (to implementers)"
autonomy: checkpointed
checkpoints: [plan, review, handoff]
patterns: [chain]
variants: [claude-code-linear-mcp, notion-mcp, gh-cli-issues]
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Spec-to-ticket planning

`TEC › PRD › PM` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `spec in docs → agent reads spec + codebase → draft breakdown (tasks, order, deps, touched files) → 🛑 plan (push back, iterate) → create project + tickets in tracker via MCP → 🛑 review (PM + eng) → 🛑 handoff (to implementers)`
**How it differs:** AWF-0001 plan-gated build: its plan gate leads to a code PR. Here the deliverable stops at a reviewed ticket set in the tracker, and code work is handed off.
**Variants:** `claude-code-linear-mcp` · `notion-mcp` · `gh-cli-issues`

## Steps
1. The PM writes the spec as usual (problem, goals, metrics, user stories, constraints) in Notion [[1]](#sources). In the solo variant it is a roadmap README [[2]](#sources).
2. The PM or an engineer points Claude Code at the spec through the Notion MCP and asks for a project plan. The agent proposes tasks, order, dependencies and what each one touches in the codebase [[1]](#sources).
3. 🛑 **Plan**: the human reads the breakdown and pushes back ('why split X and Y? they touch the same file', 'you missed the migration step') over a few rounds until it is tight [[1]](#sources).
4. Push the plan into Linear through MCP: a project with every ticket carrying priority, description, and both product and technical context [[1]](#sources). The variant uses GitHub issues via the gh CLI [[2]](#sources).
5. 🛑 **Review**: the PM and engineering both review the created tickets. They move, kill or reprioritise tickets and flag missing pieces [[1]](#sources).
6. 🛑 **Handoff**: tickets go to engineers or coding agents. Before implementing a ticket, the owner re-reviews its requirements for data modelling and edge cases [[2]](#sources).

**Output:** A structured Linear (or GitHub) project with scoped, prioritised tickets, ready for sprint or agent pickup.
**Failure modes → guards:** Tickets scoped without codebase knowledge → the agent reads the repo during breakdown. A perfectly rational user assumed, with edge cases and microinteractions missed → human re-review before implementation [[2]](#sources). Agent is fast but not accountable → mandatory PM + eng review [[1]](#sources).

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [João Matos, The bottleneck has moved](https://joaomatos.me/notes/bottleneck-moved-fixed-it) (2026-04-10). Notion spec to reviewed Linear project via Claude Code and MCP. "The review usually takes 15–30 minutes"; "Total time from Notion doc to ready-to-work Linear project: under an hour.". *First-hand: yes; confidence: high.*
- [Marcus Moretti, Claude Code for Product Managers](https://every.to/source-code/claude-code-for-product-managers) (n.d.). Roadmap README to GitHub issues; PM re-reviews each ticket before implementing. "Claude produced about 100 detailed tickets". *First-hand: yes; confidence: high.*

## Sources

1. João Matos, The bottleneck has moved. Here's how we fixed it., 2026-04-10. https://joaomatos.me/notes/bottleneck-moved-fixed-it
2. Marcus Moretti (Every / Spiral), Claude Code for Product Managers, Every. https://every.to/source-code/claude-code-for-product-managers
