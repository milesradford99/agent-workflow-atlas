# Example run: where are the real runs?

| | |
|---|---|
| **Date of run** | 2026-11 |
| **Variant** | `claude-code` (Claude Code desktop app, Opus 5.5, general-purpose subagents with web search and fetch, Slides artifact for the deck) |
| **Who ran it** | milesradford99 |
| **Scale** | solo |
| **Evidence** | A once this repo is public: the plan, the briefs, the claims table and the run log are all in the repo |

## Setup

- One Claude Code session in this repo, with the subagent tool and web search and fetch enabled. No paid APIs apart from the subscription.
- The briefs the agents ran from are in [`context/`](context/):
  - [`branch-brief.md`](context/branch-brief.md): the per-branch research brief, the same for all five branches except the workflow list and the language note;
  - [`checker-brief.md`](context/checker-brief.md): the re-fetch brief.
- To rerun: pick a key question, build the tree, get the plan approved, then send one branch brief per branch in a single message so they run in parallel.

## Run log

Times are UTC, on 2026-11-06.

1. **05:35. Key question.** The maintainer picked one of four suggested questions: for each of the 31 workflows, where is there a public, detailed, first-hand run whose author could contribute an example?
2. **05:35. MECE issue tree.** The tree split by kingdom (TEC, PRO, CRE, COM, ORG), so each workflow belongs to exactly one branch. Each workflow got four sub-questions: does a first-hand account exist, is it detailed, does it match the shape, and can its author contribute.
3. **05:36. 🛑 Plan.** The maintainer approved the tree, the rules and the deliverables as proposed, with no changes:
   - first-hand runs only;
   - public channels only, no personal contact details;
   - nobody is contacted.
4. **05:36–05:43. Each branch: deep research.** Five subagents ran in parallel, taking 3.6 to 6.5 minutes each. The CRE branch searched in Chinese as well.
5. **05:44–05:47. Each number: re-fetch source.** Four new checker agents re-opened all 65 sources. Every page loaded and every key number was found on its page. They made about 20 corrections, mostly authors, dates and exact wording. One correction: the MKT1 post is by Emily Kramer, dated 2026-05-06. No source was dropped.
6. **05:47–06:19. Claims table and so-what pages.** The lead agent merged the results into [research/2026-11-real-runs.md](../../../../../../../research/2026-11-real-runs.md), graded each workflow's coverage, and wrote four so-whats.
7. **06:19. Deck from firm template.** An 11-slide deck was built as a private Slides artifact. The maintainer chose their own Design System as the template, but it had no tokens or README yet, so the deck used a plain research style instead.
8. **06:20. 🛑 Review.** The maintainer approved the findings as they were.

## Input → output

- Input: [`sample/input.md`](sample/input.md), the key question and the approved plan.
- Output: [research/2026-11-real-runs.md](../../../../../../../research/2026-11-real-runs.md), with the claims table, coverage and outreach list, plus the deck. The deck is a private artifact that only its owner can open, so the repo copy of the content is the Markdown file.

## Numbers

| | |
|---|---|
| Brief to approved findings | 45 minutes elapsed |
| Human time | 4 decisions: choosing the question, 🛑 plan, choosing the deck template, 🛑 review |
| Research | 5 parallel agents, about 99 searches, about 101 page fetches attempted |
| Re-check | 65 sources re-opened by 4 separate agents; 0 dropped; about 20 corrections |
| Subagent tokens | about 690k for research and about 310k for checking |
| Result | 31 workflows graded: 10 strong, 13 partial, 2 weak, 6 none; top 10 outreach list |

No by-hand baseline was measured.

## What went wrong

- **The firm template was empty.** The chosen Design System had no tokens, so "deck from firm template" fell back to a generic look. Fill in the template before the run, not during it.
- **One branch didn't open its sources.** The CRE researcher read about 20 pages only through search-result text. The re-fetch step caught this, and every number still checked out, but the branch brief should require a direct fetch.
- **Blocked sites.** Zhihu, some openai.com and Medium pages, and a few others blocked fetches. Mirrors worked for some; Zhihu wasn't checked at all, which leaves a gap in the 网文 evidence.
- **The coverage grades were never checked.** The re-fetch confirmed the numbers, but the strong/partial/weak grades were one agent's judgment and no second agent reviewed them. A rerun should have the checker grade the shape match too.

## Fit

| AWF-0030 step | This run |
|---|---|
| key question → MECE issue tree | ✓ split by kingdom, so each workflow is in exactly one branch |
| 🛑 plan | ✓ approved before any research |
| each branch: deep research | ✓ 5 parallel subagents |
| claims table (claim, number, source, date, confidence) | ✓ |
| each number: re-fetch source | ✓ every source, by separate agents |
| so-what pages → 🛑 review | ✓ |
| deck from firm template | deck ✓; template empty, so a generic look was used |
