---
id: AWF-0081
name: Summary-aided casework decision
kingdom: ORG
phylum: GOV
class: CASEWORK
deliverable: casework-decision
shape: "interview transcript → summarise case → 🛑 review (decision-maker checks summary) → policy questions → search country policy notes with references → decision-maker reads full source → draft decision → 🛑 sign-off (decision-maker decides) → 🛑 sample (quality dip-sampling)"
autonomy: assist
checkpoints: [review, sign-off, sample]
patterns: [chain]
variants: [home-office-acs, home-office-aps]
tags: {region: [UK], risk: high}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Summary-aided casework decision

`ORG › GOV › CASEWORK` · assist · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `interview transcript → summarise case → 🛑 review (decision-maker checks summary) → policy questions → search country policy notes with references → decision-maker reads full source → draft decision → 🛑 sign-off (decision-maker decides) → 🛑 sample (quality dip-sampling)`
**How it differs:** AWF-0021 Procedure agent resolves customer requests by following a procedure. Here the agent only prepares material, and a statutory decision-maker makes and signs every decision (assist autonomy, high risk).
**Variants:** `home-office-acs` · `home-office-aps`

## Steps
1. Feed the asylum interview transcript (it can run to 50 pages or more) to an LLM that writes a concise case summary (Asylum Case Summarisation) [[1]](#sources).
2. Before the pilot, technical specialists reviewed every summary. 9% were judged inaccurate or incomplete and taken out, and those cases went through the usual process [[1]](#sources).
3. 🛑 **Review**: the decision-maker uses the summary to get back up to speed on the case and checks it against the transcript. The summaries have no source references to the transcript, so this check is manual [[1]](#sources).
4. The decision-maker asks case-specific policy questions of a chat search assistant over Country Policy Information Notes and Country of Origin Information Requests (Asylum Policy Search). It returns summaries with references [[1]](#sources).
5. The decision-maker must open the full note or request it cites before relying on it [[1]](#sources).
6. 🛑 **Sign-off**: only the decision-maker decides. The tools cannot make or recommend a decision on their own [[1]](#sources).
7. 🛑 **Sample**: decision quality is dip-sampled with the usual quality framework (Calibre) and compared against a comparison group [[1]](#sources).

**Output:** An asylum decision written and owned by the caseworker, plus a dip-sample quality record. In the pilot the AI summary and policy search answers were working aids only.
**Failure modes → guards:** Inaccurate or incomplete summaries → screen summaries before use (9% were removed in the pilot). Users not fully confident in summaries (23%) → decision-maker re-reads the transcript, which is harder because summaries lack source references. Over-reliance on policy summaries → the full source must be opened. The pilots were small and self-reported → continuous monitoring and a post-deployment evaluation before full rollout [[1]](#sources).

## Public runs

Coverage as of 2026-11-06: **Partial**: first-hand runs that cover part of the shape or put checkpoints elsewhere. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [UK Home Office, Evaluation of AI trials in the asylum decision-making process](https://www.gov.uk/government/publications/evaluation-of-ai-trials-in-the-asylum-decision-making-process/evaluation-of-ai-trials-in-the-asylum-decision-making-process) (2025-04-29). Two pilots, May–Dec 2024. Test vs comparison decision-makers; summary and policy-search time saved; quality dip-sampled. "reviewed transcripts 23 minutes quicker than the comparison group (a 32% time saving)"; policy search "saved on average 37 minutes per case". *First-hand: yes; confidence: med.*

## Sources

1. UK Home Office, Evaluation of AI trials in the asylum decision-making process, 2025-04-29. https://www.gov.uk/government/publications/evaluation-of-ai-trials-in-the-asylum-decision-making-process/evaluation-of-ai-trials-in-the-asylum-decision-making-process
