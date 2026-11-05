---
id: AWF-0003
name: Delegated PR
kingdom: TEC
phylum: SWE
class: FEAT
deliverable: pull-request
shape: "🛑 plan (label suitable issues) → agent reads issue + repo → (code ⟲ tests) → draft PR → (bot review ⟲ fixes) → 🛑 action (run CI) → 🛑 review → merge"
autonomy: sampled
checkpoints: [plan, action, review]
patterns: [auto-loop]
variants: [copilot-coding-agent, claude-code-action, codex-cloud, devin, jules]
tags: {risk: low}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Delegated PR

`TEC › SWE › FEAT` · sampled · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `🛑 plan (label suitable issues) → agent reads issue + repo → (code ⟲ tests) → draft PR → (bot review ⟲ fixes) → 🛑 action (run CI) → 🛑 review → merge`
**How it differs from Plan-gated build:** no planning checkpoint mid-run; the issue *is* the plan, and the agent runs in the cloud.
**Variants:** `copilot-coding-agent` · `claude-code-action` · `codex-cloud` · `devin` · `jules`

## Steps
1. 🛑 **Plan**: only self-contained, testable issues are labeled for agents.
2. Dispatch by assigning the issue to Copilot, which opens a draft PR and runs in an Actions-based environment configured by `.github/workflows/copilot-setup-steps.yml` [[4]](#sources). Alternatively, comment `@claude`, which triggers Claude Code GitHub Actions [[3]](#sources).
3. The agent implements, runs tests, and pushes. Later instructions go as PR comments, because Copilot doesn't see issue comments added after assignment [[4]](#sources).
4. A review bot comments, and the agent addresses the comments for 1–2 rounds.
5. 🛑 **Action**: a human clicks "Approve and run workflows" so CI runs on agent PRs [[4]](#sources).
6. 🛑 **Review**: human review and merge.

**Output:** merged PRs. Track the merge rate per issue label to tune what gets dispatched.

## Sources

3. Claude Code docs, *GitHub Actions*. https://code.claude.com/docs/en/github-actions
4. GitHub Blog, *Onboarding your AI peer programmer: setting up GitHub Copilot coding agent* (July 2025). https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/ · Microsoft Learn, *Assigning, tracking, and troubleshooting Copilot coding agent tasks*. https://learn.microsoft.com/en-us/training/modules/github-copilot-code-agent/3-assign-track-troubleshoot-copilot-code-agent-tasks
