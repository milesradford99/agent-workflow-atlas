# Claude Code kit: Fan-out codemod

This kit sets up Claude Code to run a large mechanical migration as a pilot, then a fan-out of headless `claude -p` workers, one per file, each running a refactor ⟲ lint → types → tests state machine with a retry budget. Failures get richer context and a second pass. The agent automates the pilot, the per-file loop, failure clustering and PR batching. It stops for a person at the three 🛑 checkpoints: **plan** (freeze the prompt pack and success definition after the pilot), **sample** (a human checks semantic fidelity on a random sample, beyond "tests pass") and **review** (code owners review the batched PRs). This is a starter kit written from the workflow's public sources (Airbnb's Enzyme → RTL migration, Slack, Google, Anthropic and Spotify write-ups), not a reported run. See [the workflow](../README.md).

## Files

### `CLAUDE.md` (section to add)

```markdown
## Codemod: <MIGRATION_NAME>
- Prompt pack lives in `migration/` (RULEBOOK.md, examples/, success.md). Treat it as frozen once approved.
- Per-file checks, in order: lint `<LINT_CMD> <file>`, types `<TYPECHECK_CMD>`, tests `<TEST_ONE_CMD> <file>`.
- Change only the file you are given (plus its snapshot if the test runner writes one). Never edit shared helpers, configs or other files; write "NEEDS_SHARED_CHANGE: <why>" to the log instead.
- Never delete or skip a test, or weaken an assertion, to make it pass.
- Stop and ask before changing the frozen prompt pack, before `git push`, and before `gh pr create`.
```

### `migration/RULEBOOK.md` (template)

```markdown
# Migration rulebook: <FROM> → <TO>

## Goal
<one sentence>

## Success definition (frozen at 🛑 plan)
- lint, typecheck and the file's tests pass
- no test removed, skipped or weakened; same number of test cases
- behaviour asserted is the same as before (checked at 🛑 sample)

## Rules
1. <pattern> → <replacement>
2. ...

## Known hard cases (from pilot)
- ...

## Examples
See `migration/examples/` — before/after pairs from the pilot.
```

### `migration/run.sh`

```bash
#!/usr/bin/env bash
# Usage: migration/run.sh files.txt [PARALLEL] [PASS]
# Runs one headless Claude Code worker per file; results go to migration/log/.
set -euo pipefail
LIST="$1"; PAR="${2:-4}"; PASS="${3:-1}"
mkdir -p migration/log
export PASS
xargs -P "$PAR" -I{} bash -c '
  f="{}"; out="migration/log/$(echo "$f" | tr / _).pass$PASS.json"
  claude -p "Use the codemod-file skill on: $f (pass $PASS)" \
    --allowedTools "Read,Edit,Grep,Glob,Bash(<LINT_CMD>:*),Bash(<TYPECHECK_CMD>:*),Bash(<TEST_ONE_CMD>:*)" \
    --max-turns 30 --output-format json > "$out" 2>&1 || true
' < "$LIST"
grep -l "\"STATUS: PASS" migration/log/*.pass"$PASS".json | wc -l | xargs echo "passed:"
```

Run each worker in its own git worktree or container if your checks are not safe to run concurrently in one checkout.

### `.claude/skills/codemod-file/SKILL.md`

```markdown
---
name: codemod-file
description: Migrate exactly one file using the frozen prompt pack in migration/. Used by headless workers started from migration/run.sh; also usable interactively during the pilot.
---
# Migrate one file

1. Read `migration/RULEBOOK.md`, `migration/success.md` and the examples in `migration/examples/`.
2. Read the target file. On pass 2+, also read its log from earlier passes, sibling files, the source of the component/module under test and up to 3 extra examples.
3. **Refactor** the file following the rulebook.
4. **Lint:** run the lint command on the file; on errors, fix and rerun.
5. **Types:** run the typecheck; fix errors in this file only.
6. **Tests:** run the file's tests; fix failures in this file only.
7. Loop steps 4–6 with the validator output as feedback, at most 3 rounds on pass 1 and 5 on later passes.
8. Never delete, skip or weaken tests; never edit other files.
9. End with exactly one line: `STATUS: PASS` or `STATUS: FAIL — <step> — <short reason>`.
```

### `.claude/skills/fan-out-codemod/SKILL.md`

```markdown
---
name: fan-out-codemod
description: Orchestrate a large codemod: pilot, freeze the prompt pack, fan out headless workers, retry failures with more context, sample for fidelity, and batch PRs by owner. Use for migrations touching many similar files.
---
# Fan-out codemod

1. **Inventory.** List target files into `migration/files.txt` (e.g. with `git grep -l <OLD_PATTERN>`). Report the count.
2. **Pilot.** Pick 10–20 representative files (small, large, odd cases). Run the codemod-file skill on each in this session; refine `migration/RULEBOOK.md` and save good before/after pairs to `migration/examples/`. Write the success definition into `migration/success.md`.
3. **STOP (🛑 plan): present the rulebook, examples, success definition and pilot pass/fail table, and wait for the user's approval to freeze the prompt pack.**
4. **Fan out.** Ask the user to run (or approve running) `migration/run.sh migration/files.txt <PARALLEL> 1`. Do not change the prompt pack while workers run.
5. **Collect.** Parse `migration/log/*.pass1.json` into `migration/report.md`: pass/fail per file, failing step and reason.
6. **Add context to failures.** Cluster failures by step and reason. For each cluster, propose a rulebook patch or extra example; after the user agrees, list failing files in `migration/retry.txt` and run pass 2 with the richer context. Repeat at most once more; the rest is residue for hand-fixing.
7. **STOP (🛑 sample): pick a random sample (e.g. `shuf -n <K> migration/passed.txt`), show before/after diffs side by side with notes on any behaviour change, and wait for the user's fidelity verdict.** If problems turn up, patch the rulebook and rerun affected files.
8. **Batch PRs.** Group passed files by owner from `CODEOWNERS`. For each group, prepare a branch and PR body (rule summary, file list, checks run, link to report). STOP and ask before each `git push` / `gh pr create`.
9. **STOP (🛑 review): hand the PR list to the user for code-owner review.** Write the residue list and the final prompt pack location into `migration/report.md`.
```

## Run it

1. Copy the files, fill placeholders (`<LINT_CMD>`, `<TYPECHECK_CMD>`, `<TEST_ONE_CMD>`, patterns), `chmod +x migration/run.sh`, and start on a migration branch.
2. In Claude Code, say "Use the fan-out-codemod skill for <FROM> → <TO>". It inventories files and runs the pilot interactively.
3. 🛑 **Plan:** review the rulebook, examples and pilot table; approve to freeze. Then run `migration/run.sh` yourself and watch the pass rate.
4. Let the agent cluster failures and run the retry pass. 🛑 **Sample:** read the sampled diffs for behaviour changes, not just green tests.
5. Approve each push/PR. 🛑 **Review:** code owners review their batch; hand-fix the residue listed in `migration/report.md`.

## Adapt it

- **Codex CLI:** replace `claude -p ...` with `codex exec "<same prompt>"` and put the CLAUDE.md section plus both skill procedures in `AGENTS.md`. **Agent SDK:** call the same per-file prompt from a script and keep a per-file state record. **Cursor:** use the rulebook as a `.cursor/rules` file for the pilot only.
- Pick parallelism and retry budgets to fit your CI cost and rate limits; start small.
- If an AST codemod handles the easy cases, run it first and give the LLM only the leftovers.
- Safety: workers get only file-scoped tools via `--allowedTools`; no network, no push. Never let a worker edit the prompt pack. Keep secrets out of logs; review logs before sharing them.
