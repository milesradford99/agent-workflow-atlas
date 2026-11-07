---
id: AWF-0041
name: Review-ready 1040 prep
kingdom: PRO
phylum: FIN
class: TAX
deliverable: reviewed-tax-return
shape: "client uploads source docs → extract fields with confidence → 🛑 review (preparer validates low-confidence fields + mapping) → workpaper + push to tax software → AI second-pass review (missing forms, YoY, firm checks) → 🛑 review (preparer resolves flags) → 🛑 sign-off (senior reviewer signs + files)"
autonomy: checkpointed
checkpoints: [review, sign-off]
patterns: [chain, eval-opt]
variants: [juno, filed]
tags: {risk: high}
evidence: B
status: draft
reference_example: null
inputs_from: []
merged_into: null
last_verified: 2026-11
---

# Review-ready 1040 prep

`PRO › FIN › TAX` · checkpointed · evidence B · **draft: needs a reference example** ([how to add one](../../../../../CONTRIBUTING.md#1-add-an-example-run))

**Shape:** `client uploads source docs → extract fields with confidence → 🛑 review (preparer validates low-confidence fields + mapping) → workpaper + push to tax software → AI second-pass review (missing forms, YoY, firm checks) → 🛑 review (preparer resolves flags) → 🛑 sign-off (senior reviewer signs + files)`
**How it differs:** AWF-0022 Invoice extract-match-route (AP) extracts invoices for payment. This prepares a regulated filing with preparer and CPA sign-off.
**Variants:** `juno` · `filed`

## Steps
1. The client uploads W-2s, 1099s, K-1s and brokerage statements to the firm's portal [[1]](#sources).
2. The AI extracts fields and gives a confidence score for each [[1]](#sources).
3. 🛑 **Review**: The preparer checks extracted values against the source PDF, low-confidence fields first. For business returns, the preparer confirms the chart-of-accounts mapping [[1]](#sources).
4. The system builds the workpaper and pushes data into the tax software. The AI runs data entry and diagnostics [[1]](#sources)[[2]](#sources).
5. The draft return goes back to the AI reviewer, which flags missing forms, year-over-year swings and firm-specific checks into a review plan [[1]](#sources).
6. 🛑 **Review**: The preparer works through and resolves the flagged items [[1]](#sources).
7. 🛑 **Sign-off**: The senior reviewer or CPA reviews everything, corrects, signs and files [[1]](#sources)[[2]](#sources).

**Output:** A CPA-signed, e-filed return with an evidence-linked workpaper and a resolved review checklist.
**Failure modes → guards:** Misread source fields → confidence scores with human validation [[1]](#sources). Missed forms → prior-year comparison checks [[1]](#sources). Treat the AI like a junior preparer: review everything [[2]](#sources).

## Public runs

Coverage as of 2026-11-06: **Weak**: only anonymous, vendor-linked or journalist-told accounts. Collected and re-checked in [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md).

- [Filed, Teel Accounting](https://www.filed.com/cases/teel-accounting) (2026). Solo CPA ran returns through AI data entry and diagnostics, reviewing each in ProConnect. "processing 50% of all returns through Filed for data entry and diagnostics". *First-hand: vendor; confidence: med.*
- [Juno, How AI tax preparation works](https://juno.tax/blog/how-ai-tax-preparation-works) (2026-03-06). Vendor founder's step-by-step workflow as used inside firms. *First-hand: vendor; confidence: low.*

## Sources

1. Haase D., How AI tax preparation works: step-by-step, Juno, 2026-03-06. https://juno.tax/blog/how-ai-tax-preparation-works
2. Filed, Teel Accounting Case Study: 1,100 returns. A 5 p.m. finish., 2026. https://www.filed.com/cases/teel-accounting
