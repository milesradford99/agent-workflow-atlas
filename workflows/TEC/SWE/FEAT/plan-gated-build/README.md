---
id: AWF-0001
name: Plan-gated build
kingdom: TEC
phylum: SWE
class: FEAT
deliverable: pull-request
shape: "read issue + code → plan → 🛑 plan → failing tests → (code ⟲ tests) → fresh review → 🛑 action → open PR → 🛑 review → update context file"
autonomy: checkpointed
checkpoints: [plan, action, review]
patterns: [auto-loop, orch-workers, eval-opt]
variants: [claude-code, codex-cli, cursor-agent]
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Plan-gated build

`TEC › SWE › FEAT` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `read issue + code → plan → 🛑 plan → failing tests → (code ⟲ tests) → fresh review → 🛑 action → open PR → 🛑 review → update context file`
**Traits:** `auto-loop, orch-workers` · **Variants:** `claude-code` · `codex-cli` · `cursor-agent`

- **Input:** an issue with acceptance criteria; a repo with `CLAUDE.md`/`AGENTS.md` (build, test, and lint commands, conventions, no-go areas); a working test suite.
- **Roles/Tools:** the lead agent (read, edit, allow-listed shell); read-only explorer sub-agents; a verifier (formatter and lint hooks, tests, typecheck, browser screenshots for UI); a fresh-context reviewer sub-agent.

## Steps
1. The agent reads the context file, the issue (`gh issue view` or the tracker's MCP), and relevant code. Explorers fan out to map affected modules.
2. In plan mode (read-only), the agent writes a plan: files to touch, approach, test strategy, open questions [[2]](#sources). 🛑 **Plan**: this is the highest-leverage correction point.
3. Write failing tests that encode the acceptance criteria and confirm they fail.
4. Implement in increments, with targeted tests and typecheck after each one. Loop on the failure output, and cap iterations before escalating.
5. A fresh-context reviewer checks the diff against the spec: edge cases, dead code, security.
6. For UI changes, run the dev server, take a screenshot, and compare with the design.
7. 🛑 **Action**: commit, push, and open the PR, unless these were pre-authorized.
8. 🛑 **Review**: a human reviews the PR and CI.
9. Write recurring corrections back into the context file.

**Output:** a reviewed PR with tests, and an updated context file.
**Failure modes → guards:** the agent edits tests to make them pass → forbid test edits after the tests are written. Scope creep → flag any file changed outside the plan's list. Context saturation → clear context between tasks and persist the plan to a file [[2]](#sources).
**Close relative:** a version that asks approval for every edit (`assist`) is a separate species by the swap test.

## Sources

2. Claude Code docs, *Best practices*. https://code.claude.com/docs/en/best-practices
