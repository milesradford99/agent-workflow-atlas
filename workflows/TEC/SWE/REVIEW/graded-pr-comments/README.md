---
id: AWF-0070
name: Graded PR comments
kingdom: TEC
phylum: SWE
class: REVIEW
deliverable: pr-review-comments
shape: "diff → filter eligible files → build context (nearby functions, classes, imports) → each assistant (bugs, best practices, security): draft comments → confidence grade → dedupe → drop low-value categories → post inline → 🛑 review (author rates and fixes) → rerun 5x on final commit to measure addressed"
autonomy: sampled
checkpoints: [review]
patterns: [parallel, eval-opt, chain]
variants: [ureview, coderabbit, github-copilot-code-review, graphite-diamond]
tags: {risk: low}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Graded PR comments

`TEC › SWE › REVIEW` · sampled · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `diff → filter eligible files → build context (nearby functions, classes, imports) → each assistant (bugs, best practices, security): draft comments → confidence grade → dedupe → drop low-value categories → post inline → 🛑 review (author rates and fixes) → rerun 5x on final commit to measure addressed`
**How it differs:** AWF-0003 Delegated PR uses bot review inside an agent's own authoring loop. This workflow reviews every human-authored diff company-wide, and its output is comments rather than code.
**Variants:** `ureview` · `coderabbit` · `github-copilot-code-review` · `graphite-diamond`

## Steps
1. On each diff, skip config files, generated code and experimental directories. Build a prompt with nearby functions, class definitions and imports [[1]](#sources).
2. Run specialised assistants in parallel: Standard (bugs, exception handling, logic), Best Practices (in-house conventions) and AppSec (vulnerabilities) [[1]](#sources).
3. A second prompt scores each comment's confidence. Prune with thresholds set per assistant, language and category. Merge overlapping comments with a semantic-similarity filter. Suppress categories that have historically been of low value to developers [[1]](#sources).
4. Post the surviving comments inline on the review platform, with a median of 4 minutes per commit in CI [[1]](#sources).
5. 🛑 **Review**: the author marks each comment Useful or Not Useful and decides whether to act on it. Ratings stream to the warehouse to retune thresholds [[1]](#sources).
6. Measure: rerun the reviewer five times on the final commit. A comment counts as addressed if no rerun reproduces it. Track precision and recall against a human-labelled benchmark and gate rollouts on those numbers [[1]](#sources).

**Output:** Inline review comments on each PR, alongside the human reviewer, with usefulness and addressed-rate metrics feeding back into the thresholds.
**Failure modes → guards:** Noisy, low-value comments erode trust → per-category confidence thresholds, dedupe, and suppressing categories with poor history; hold rollout to new languages until usefulness stays high [[1]](#sources).

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Uber, uReview](https://www.uber.com/us/en/blog/ureview/) (2025-08-12). Three assistants, a grader and a dedupe filter post inline comments; addressed rate measured against human comments. "Engineers who interact with the tool mark 75% of its comments as useful"; 65% addressed vs 51% for human comments. *First-hand: yes; confidence: high.*

## Sources

1. Sonal Mahajan, Shauvik Roy Choudhary, Will Bond (Uber), uReview: Scalable, Trustworthy GenAI for Code Review at Uber, 2025-08-12. https://www.uber.com/us/en/blog/ureview/
