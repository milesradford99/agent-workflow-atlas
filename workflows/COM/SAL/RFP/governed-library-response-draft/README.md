---
id: AWF-0051
name: Governed-library response draft
kingdom: COM
phylum: SAL
class: RFP
deliverable: rfp-response-draft
shape: "intake RFP/questionnaire → fit check (reject wrong docs) → parse into questions → each question: retrieve from verified library + draft with source trace → flag unanswerable → 🛑 review (SME/GRC on flagged) → (SE comments ⟲ regenerate) → 🛑 sign-off → export in buyer format → feed approved edits back to library"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [chain, route, eval-opt]
variants: [in-house-agentic-rag, conveyor, responsive]
tags: {risk: medium}
evidence: A
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Governed-library response draft

`COM › SAL › RFP` · checkpointed · evidence A · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `intake RFP/questionnaire → fit check (reject wrong docs) → parse into questions → each question: retrieve from verified library + draft with source trace → flag unanswerable → 🛑 review (SME/GRC on flagged) → (SE comments ⟲ regenerate) → 🛑 sign-off → export in buyer format → feed approved edits back to library`
**How it differs:** None close. AWF-0024 Playbook contract review reviews inbound contracts against a playbook; this workflow drafts outbound answers from an approved library.
**Variants:** `in-house-agentic-rag` · `conveyor` · `responsive`

## Steps
1. Build the knowledge base only from verified, continuously updated product documentation and compliance certificates [[1]](#sources). Zapier connected 434 knowledge items and 2,675 past answers into one library [[2]](#sources).
2. The salesperson or sales engineer uploads the request where sales already works. The agent first checks it can answer this document, rejecting the wrong one and telling the seller what is needed [[2]](#sources).
3. Agentic retrieval checks each question against the approved corpus and traces every answer to its source. The agent cannot invent features or claim compliance the company lacks [[1]](#sources).
4. 🛑 **Review**: the security/GRC team is tagged only where a human eye is actually needed [[2]](#sources). The sales engineer comments on the draft and the AI regenerates updated versions [[1]](#sources).
5. 🛑 **Sign-off**: the sales engineer edits for the customer's goals and approves the final response. The system learns from each interaction [[1]](#sources).

**Output:** A completed RFP, RFI or security questionnaire in the buyer's format, ready to submit, and a library improved by the approved edits.
**Failure modes → guards:** Stale or deprecated specs get into answers → only a governed corpus with lineage per answer [[1]](#sources). The agent answers off-scope documents → intake fit check [[2]](#sources). Over-reliance hides gaps → route flagged questions to the security team [[2]](#sources).

## Public runs

Coverage as of 2026-11-06: **Strong**: a first-hand, detailed run that matches most of the shape. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Palo Alto Networks, From Weeks to Minutes](https://www.paloaltonetworks.com/perspectives/from-weeks-to-minutes-how-we-applied-an-ai-first-transformation-to-the-rfp-bottleneck/) (2026-03-26). Internal 'customer zero' RFP copilot; SEs edit and regenerate AI drafts grounded in a verified corpus. "delivering RFPs in days instead of weeks". *First-hand: yes; confidence: high.*
- [Conveyor, Zapier playbook](https://www.conveyor.com/blog/steal-the-playbook-zapier) (2026-02-24). Zapier GRC team reviews only flagged questions from agent-drafted questionnaires. "only 20% of security questions require a security team member which is down from 90%". *First-hand: vendor; confidence: med.*

## Sources

1. Sandeep Uttamchandani / Palo Alto Networks, From Weeks to Minutes: How We Applied an AI-First Transformation to the RFP Bottleneck, 2026-03-26. https://www.paloaltonetworks.com/perspectives/from-weeks-to-minutes-how-we-applied-an-ai-first-transformation-to-the-rfp-bottleneck/
2. Marcus Andrews / Conveyor, Steal the Playbook: How Zapier made 80% of customer security reviews touchless, 2026-02-24. https://www.conveyor.com/blog/steal-the-playbook-zapier
