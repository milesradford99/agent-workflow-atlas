---
id: AWF-0002
name: Fan-out codemod
kingdom: TEC
phylum: SWE
class: MAINT
deliverable: migration-changeset
shape: "pilot on 10–20 files → 🛑 plan → each file: (refactor ⟲ lint → types → tests) → add context to failures → each failure: (retry ⟲ checks) → 🛑 sample → batch PRs → 🛑 review"
autonomy: sampled
checkpoints: [plan, sample, review]
patterns: [parallel, eval-opt, chain]
variants: [claude-code-headless, agent-sdk, codex-exec]
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Fan-out codemod

`TEC › SWE › MAINT` · sampled · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `pilot on 10–20 files → 🛑 plan → each file: (refactor ⟲ lint → types → tests) → add context to failures → each failure: (retry ⟲ checks) → 🛑 sample → batch PRs → 🛑 review`
**Traits:** `parallel, eval-opt, chain` · **Variants:** `claude-code-headless` · `agent-sdk` · `codex-exec`
**Reference example:** Airbnb's Enzyme → React Testing Library migration [[5]](#sources). About 3.5k test files were migrated in roughly 6 weeks, against an estimated 1.5 years by hand. A per-file step state machine retried with error feedback. About 75% of files passed within hours, and the remaining ~900 got richer context and more retries. Fewer than 100 were finished by hand.

## Steps
1. Pilot on 10–20 representative files and tune the prompt and examples. 🛑 **Plan**: freeze the prompt, few-shot examples, and success definition.
2. Run a per-file state machine: refactor → fix lint → fix types → fix tests. Each step is an LLM call that receives its validator's output. Run N parallel headless workers (`claude -p`, Codex exec, Agent SDK), each with a retry budget.
3. Long tail: add context (sibling files, component source, more examples) and rerun. Cluster the failures and patch the prompt [[5]](#sources).
4. 🛑 **Sample**: check semantic fidelity on a random sample, beyond "tests pass."
5. Batch PRs by owner. 🛑 **Review**: code owners review. Hand-fix the residue.

**Output:** a migrated codebase, a failure log, and a reusable migration prompt pack.

## Sources

5. Airbnb Tech, *Accelerating Large-Scale Test Migration with LLMs* (March 2025). https://airbnb.tech/?p=366 · InfoQ coverage: https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/
