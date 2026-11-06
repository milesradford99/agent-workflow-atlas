# Example run: researching the taxonomy for this catalog

> **Candidate, not yet the reference example.** This run differs from AWF-0030 at two steps the swap test cares about (no 🛑 plan checkpoint, a report instead of a deck) and one it doesn't (no parallel workers). See [Fit](#fit). A maintainer decides whether it belongs here, as a new workflow, or in `workflows/unplaced/`.

| | |
|---|---|
| **Date of run** | 2026-11 |
| **Variant** | `claude-code` (Claude Code desktop app, Opus 5.5, built-in web search) |
| **Who ran it** | milesradford99 |
| **Scale** | solo |
| **Evidence** | A once this repo is public: the brief, every version of the output and the verification log are in the repo |

## Setup

- Claude Code in an empty folder, one session, no `CLAUDE.md`, playbook or prompt pack. The brief was the only input.
- Tools: web search, file write. No subagents and no web fetch were used.
- Cost: a single subscription session; no separate API spend.

There are no context files for this run; see [`context/`](context/).

## Run log

Times are UTC, taken from the session transcript.

1. **2026-11-03 23:54. Brief.** The user pasted the [research brief](sample/input-brief.md): taxonomy, cross-industry landscape, and 1–2 SOPs per category, judged on actionability, MECE structure and signal-to-noise.
2. **~6 minutes later. v1 written.** The agent went straight from brief to a full report, drafted from model knowledge. It didn't propose an issue tree or plan for approval first, and it ran no searches.
3. **2026-11-04 00:05. 🛑 Review 1.** The user asked to "verify sources" and to make the classification more systematic, along the lines of biological classification.
4. **00:15. v2.** 32 web searches, run one after another, re-checked the report's claims. The result was a verification log of 31 claims and a Linnaean-style taxonomy. v2 is kept at [research/archive/phase1-report-v2.md](../../../../../../../research/archive/phase1-report-v2.md).
5. **2026-11-05 12:59. 🛑 Review 2.** The user found v2 "a bit too complicated" and asked to keep the concept but simplify the rules.
6. **13:04. v3.** The agent cut the rule set down to six rules plus first-match keys, and recorded what it dropped and why (§1.9).
7. **13:30. Accepted.** The user moved on ("Start Phase 2"). v3 became the seed for this repo's 31 workflows.

## Input → output

- Input: [`sample/input-brief.md`](sample/input-brief.md).
- Output: [research/phase1-report.md](../../../../../../../research/phase1-report.md) (v3). It's too large to copy into `sample/`; see [`sample/`](sample/) for what to look at.

## Numbers

| | |
|---|---|
| Time from brief to accepted report | ~37 hours elapsed, almost all of it waiting for review. About 25 minutes of agent work across three versions. |
| Review rounds | 2, both of which changed structure rather than wording |
| Searches | 0 for v1, 32 for v2, 0 for v3 |
| Claims checked (v2 log) | 31: 19 confirmed, 7 corrected, 5 left unresolved and flagged |
| References in the final report | 32 |

No by-hand baseline was measured.

## What went wrong

- **No plan checkpoint.** The agent wrote a complete v1 before the user had agreed on the structure. Both review rounds then reworked the classification, which a plan or issue-tree approval up front might have caught sooner.
- **v1 was unsourced.** The facts in it came from model knowledge, and verification only happened because the user asked. In v2, 7 of the 31 checked claims needed corrections. A rerun should search first and then write.
- **Sequential research.** All 32 searches ran in one thread. Parallel research per branch, as AWF-0030 describes, would have been faster, and each branch would have kept its own sources.
- **Overbuilt v2.** The user's analogy was taken too literally, and v2 grew more rules than the catalog needed. v3 fixed that.

## Fit

Compared step by step with [AWF-0030](../../README.md):

| AWF-0030 step | This run | Swap test |
|---|---|---|
| key question → MECE issue tree | The brief set the question; the agent built the tree itself | ok |
| 🛑 plan | **Missing**: there was no approval before research | **checkpoint differs** |
| each branch: deep research (`orch-workers`, `parallel`) | One agent, sequential searches | pattern only (a trait, not a deciding factor) |
| claims table with sources, dates, confidence | v2 verification log (✓ / ✎ / ⚠ with sources) | ok |
| each number: re-fetch source | Re-searched, not re-fetched | close |
| so-what pages → 🛑 review | Two review rounds | ok |
| deck from firm template | **A Markdown report** instead | **deliverable differs** |

Under rule 4, a different checkpoint set or deliverable makes this a different workflow, not an example. As a rerun with the 🛑 plan step added, it would fit AWF-0030 except for the deliverable. Something like "checkpointed research report" might be a better place for it, and unplaced/ is the fallback.
