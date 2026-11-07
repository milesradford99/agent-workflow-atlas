# Second Collection Pass

**Date:** 2026-11-06
**Question:** which real agentic workflows are missing from the catalog, both as second workflows in classes that already have one and in fields the taxonomy doesn't cover yet?

## Result

68 new draft workflows, AWF-0088 to AWF-0155, bring the catalog to 155.

| | Count |
|---|---|
| Placed in an existing class | 52 |
| Placed in the two new phyla, `PRO/INS` (insurance claims) and `COM/RET` (retail catalog) | 7 |
| Unplaced, waiting for more similar workflows before a class opens | 9 |
| Evidence A / B | 52 / 16 |
| Public runs: Strong / Partial / Weak | 34 / 20 / 14 |

A workflow went in as a second entry in a class only if it fails the swap test against the class's existing workflow: a different deliverable, different human checkpoints, or a different autonomy level. A different tool alone counts as a variant, not a new workflow. Each entry's "How it differs" line names the closest existing workflow and what separates it. Several were added because a real run puts the checkpoints somewhere other than the catalog's first entry does. One example is the YC recruiting run: the agent sends rejections when the manager tells it to (`ORG/BIZ/HR`), unlike AWF-0029.

## New taxonomy

- **`PRO/INS` Insurance, class `CLAIMS`**: three claim workflows at Allianz, NFU Mutual and TSI Adjusters. Underwriting has two so far (Hiscox; the Zurich, Arch, Markel and Paragon triage) and stays unplaced.
- **`COM/RET` Retail & e-commerce operations, class `CATALOG`**: Zalando, Instacart with Walmart, and Wayfair, plus JD.com and OTTO's catalog copy. The keys put a storefront's product catalog under `RET`, ahead of `MKT`.
- **Still unplaced:**
  - logistics: freight ×2, customs ×1;
  - insurance underwriting ×2;
  - construction submittals, lease abstraction, safety audits and agronomy advice, ×1 each.

## Method

1. **Plan.** All 87 existing workflows were exported with their shape lines, and the classes split into seven groups, plus an eighth group for fields outside the taxonomy.
2. **Research.** Eight agents worked in parallel using [research/prompts/collect.md](prompts/collect.md), each told to add 0–2 workflows per class and only with first-hand evidence. Classes where they found nothing are listed in each agent's report and get no entry.
3. **Merge.** The Merck clinical study report workflow turned up in two groups. It was filed once, under `PRO/HLT/CLINTRIAL`, with the Novo Nordisk and Sanofi runs added.
4. **Re-check.** Four separate checkers ([research/prompts/check.md](prompts/check.md)) re-opened all 94 public runs.
   - 87 numbers matched the page exactly and 5 closely. Where two runs had no figure, the checker took one from the page.
   - No run was dropped.
   - 7 first-hand labels were corrected, to study, anon, interview or vendor.
5. **File.** Entries were generated in the standard format, with diagrams and index rebuilt and all checks passing.

## Caveats

- **Vendor-heavy fields.** Insurance underwriting, customs, construction submittals and real-estate maintenance rest mainly on vendor case studies (evidence B). Treat them as leads until a practitioner adds an example run.
- **Class fit.** Two choices need a decision:
  - The credit memo (`PRO/FIN/INVEST`) is there because FIN has no lending class.
  - The hypothesis tournament (`PRO/RES/LITREV`) could also sit in `ANALYSIS`.
- **Risk.** Hiring, clinical, legal, credit, benefits and IEP entries are tagged `high`.
- **Thin checkpoints.** The live sports recap (`CRE/MED/POST`) and the safety-audit agents describe their human checkpoint only briefly.

## New workflows

| ID | Workflow | Class | Evidence | Public runs |
|---|---|---|---|---|
| AWF-0088 | [Pre-drafted radiograph reports](../workflows/PRO/HLT/CLINDOC/pre-drafted-radiograph-reports/) | PRO › HLT › CLINDOC | A | strong |
| AWF-0089 | [Routed inbox reply drafts](../workflows/PRO/HLT/CLINDOC/routed-inbox-reply-drafts/) | PRO › HLT › CLINDOC | A | strong |
| AWF-0090 | [Exception-routed autonomous coding](../workflows/PRO/HLT/RCM/exception-routed-autonomous-coding/) | PRO › HLT › RCM | B | weak |
| AWF-0091 | [Writer-reviewed CSR draft](../workflows/PRO/HLT/CLINTRIAL/writer-reviewed-csr-draft/) | PRO › HLT › CLINTRIAL | A | partial |
| AWF-0092 | [Business self-serve drafting](../workflows/PRO/LEG/CONTRACT/business-self-serve-drafting/) | PRO › LEG › CONTRACT | A | partial |
| AWF-0093 | [Calibrated privilege log](../workflows/PRO/LEG/LITIG/calibrated-privilege-log/) | PRO › LEG › LITIG | B | weak |
| AWF-0094 | [Agent-crew claim file](../workflows/PRO/INS/CLAIMS/agent-crew-claim-file/) | PRO › INS › CLAIMS | A | strong |
| AWF-0095 | [Handler-accepted invoice recommendation](../workflows/PRO/INS/CLAIMS/handler-accepted-invoice-recommendation/) | PRO › INS › CLAIMS | A | partial |
| AWF-0096 | [Policy-grounded claim letters](../workflows/PRO/INS/CLAIMS/policy-grounded-claim-letters/) | PRO › INS › CLAIMS | B | weak |
| AWF-0097 | [Policy-cited expense review](../workflows/PRO/FIN/AP/policy-cited-expense-review/) | PRO › FIN › AP | B | weak |
| AWF-0098 | [Underwriter-finalized credit memo](../workflows/PRO/FIN/INVEST/underwriter-finalized-credit-memo/) | PRO › FIN › INVEST | B | weak |
| AWF-0099 | [Data-informed IEP draft](../workflows/PRO/EDU/COURSE/data-informed-iep-draft/) | PRO › EDU › COURSE | A | partial |
| AWF-0100 | [Section-gated lesson build](../workflows/PRO/EDU/COURSE/section-gated-lesson-build/) | PRO › EDU › COURSE | A | strong |
| AWF-0101 | [Generated item bank](../workflows/PRO/EDU/ASSESS/generated-item-bank/) | PRO › EDU › ASSESS | A | strong |
| AWF-0102 | [Guardrailed course tutor](../workflows/PRO/EDU/TUTOR/guardrailed-course-tutor/) | PRO › EDU › TUTOR | A | strong |
| AWF-0103 | [AI role-play practice](../workflows/PRO/EDU/LND/ai-role-play-practice/) | PRO › EDU › LND | B | weak |
| AWF-0104 | [Hypothesis tournament](../workflows/PRO/RES/LITREV/hypothesis-tournament/) | PRO › RES › LITREV | A | strong |
| AWF-0105 | [Funder-side prescreen](../workflows/PRO/RES/GRANT/funder-side-prescreen/) | PRO › RES › GRANT | A | strong |
| AWF-0106 | [Submission intake screen](../workflows/PRO/RES/PEER/submission-intake-screen/) | PRO › RES › PEER | A | partial |
| AWF-0107 | [Human-sent reply drafting](../workflows/COM/CSX/RESOLVE/human-sent-reply-drafting/) | COM › CSX › RESOLVE | A | weak |
| AWF-0108 | [Resident maintenance triage](../workflows/COM/CSX/RESOLVE/resident-maintenance-triage/) | COM › CSX › RESOLVE | B | weak |
| AWF-0109 | [Inbound qualify-and-book agent](../workflows/COM/SAL/PROSPECT/inbound-qualify-and-book/) | COM › SAL › PROSPECT | A | strong |
| AWF-0110 | [Exception-only contract validation](../workflows/COM/SAL/REVOPS/exception-only-contract-validation/) | COM › SAL › REVOPS | A | strong |
| AWF-0111 | [Catalog copy factory](../workflows/COM/RET/CATALOG/catalog-copy-factory/) | COM › RET › CATALOG | A | strong |
| AWF-0112 | [Confidence-sampled attribute extraction](../workflows/COM/RET/CATALOG/confidence-sampled-attribute-extraction/) | COM › RET › CATALOG | A | partial |
| AWF-0113 | [Copilot attribute suggestions](../workflows/COM/RET/CATALOG/copilot-attribute-suggestions/) | COM › RET › CATALOG | A | strong |
| AWF-0114 | [Supplier-confirmed catalog fixes](../workflows/COM/RET/CATALOG/supplier-confirmed-catalog-fixes/) | COM › RET › CATALOG | B | weak |
| AWF-0115 | [Tiered-permission ads optimizer](../workflows/COM/MKT/ADS/tiered-permission-ads-optimizer/) | COM › MKT › ADS | A | strong |
| AWF-0116 | [Agent-drafted PCB schematic](../workflows/TEC/ENG/CAD/agent-drafted-pcb-schematic/) | TEC › ENG › CAD | A | partial |
| AWF-0117 | [Pre-submittal plan check](../workflows/TEC/ENG/CODECOMP/pre-submittal-plan-check/) | TEC › ENG › CODECOMP | B | weak |
| AWF-0118 | [Zoning-rule study crew](../workflows/TEC/ENG/CODECOMP/zoning-rule-study-crew/) | TEC › ENG › CODECOMP | B | weak |
| AWF-0119 | [AI-first CAM program](../workflows/TEC/ENG/MFG/ai-first-cam-program/) | TEC › ENG › MFG | B | partial |
| AWF-0120 | [Agent-run interviews](../workflows/TEC/PRD/UXR/agent-run-interviews/) | TEC › PRD › UXR | A | strong |
| AWF-0121 | [Routed accessibility PR agent](../workflows/TEC/PRD/UI/routed-accessibility-pr-agent/) | TEC › PRD › UI | A | strong |
| AWF-0122 | [Scored token migration](../workflows/TEC/PRD/DSYS/scored-token-migration/) | TEC › PRD › DSYS | A | strong |
| AWF-0123 | [Scheduled metric commentary](../workflows/TEC/DAT/ANALYTICS/scheduled-metric-commentary/) | TEC › DAT › ANALYTICS | A | partial |
| AWF-0124 | [Summoned dbt debugger](../workflows/TEC/DAT/DATAENG/summoned-dbt-debugger/) | TEC › DAT › DATAENG | A | strong |
| AWF-0125 | [Multi-agent readout review](../workflows/TEC/DAT/DS/multi-agent-readout-review/) | TEC › DAT › DS | A | strong |
| AWF-0126 | [Calibrated-judge quality loop](../workflows/TEC/DAT/MLOPS/calibrated-judge-quality-loop/) | TEC › DAT › MLOPS | A | strong |
| AWF-0127 | [Open-loop NOC root cause](../workflows/TEC/ITS/SRE/open-loop-noc-root-cause/) | TEC › ITS › SRE | A | partial |
| AWF-0128 | [Detonate-and-confirm detections](../workflows/TEC/ITS/SECOPS/detonate-and-confirm-detections/) | TEC › ITS › SECOPS | A | partial |
| AWF-0129 | [AI fuzz-target hunting](../workflows/TEC/ITS/APPSEC/ai-fuzz-target-hunting/) | TEC › ITS › APPSEC | A | strong |
| AWF-0130 | [Profile-led perf fixes](../workflows/TEC/SWE/MAINT/profile-led-perf-fixes/) | TEC › SWE › MAINT | A | strong |
| AWF-0131 | [Mutant-guided hardening tests](../workflows/TEC/SWE/TEST/mutant-guided-hardening-tests/) | TEC › SWE › TEST | A | strong |
| AWF-0132 | [Streak-verified flake fix](../workflows/TEC/SWE/TEST/streak-verified-flake-fix/) | TEC › SWE › TEST | A | strong |
| AWF-0133 | [Comment-to-edit suggestions](../workflows/TEC/SWE/REVIEW/comment-to-edit-suggestions/) | TEC › SWE › REVIEW | A | strong |
| AWF-0134 | [Sampled LLM records analysis](../workflows/CRE/WRI/JOURN/sampled-llm-records-analysis/) | CRE › WRI › JOURN | A | partial |
| AWF-0135 | [Release-cycle docs skill](../workflows/CRE/WRI/TECHW/release-cycle-docs-skill/) | CRE › WRI › TECHW | A | strong |
| AWF-0136 | [Term-gated game localisation](../workflows/CRE/WRI/TRANS/term-gated-game-localisation/) | CRE › WRI › TRANS | A | strong |
| AWF-0137 | [Gated AI 漫剧 line](../workflows/CRE/MED/SHORTDRAMA/gated-ai-manju-line/) | CRE › MED › SHORTDRAMA | A | partial |
| AWF-0138 | [Autonomous live recap](../workflows/CRE/MED/POST/autonomous-live-recap/) | CRE › MED › POST | A | partial |
| AWF-0139 | [Directed AI audiobook](../workflows/CRE/MED/AUDIO/directed-ai-audiobook/) | CRE › MED › AUDIO | A | partial |
| AWF-0140 | [Image-to-3D asset packs](../workflows/CRE/MED/GAMEART/image-to-3d-asset-packs/) | CRE › MED › GAMEART | A | strong |
| AWF-0141 | [Gap-checked benefits form fill](../workflows/ORG/GOV/CASEWORK/gap-checked-benefits-form-fill/) | ORG › GOV › CASEWORK | B | partial |
| AWF-0142 | [Visit-recorded care assessment](../workflows/ORG/GOV/CASEWORK/visit-recorded-care-assessment/) | ORG › GOV › CASEWORK | A | strong |
| AWF-0143 | [Officer-checked planning data extraction](../workflows/ORG/GOV/CIVIC/officer-checked-planning-data-extraction/) | ORG › GOV › CIVIC | A | strong |
| AWF-0144 | [Manager-approved pipeline actions](../workflows/ORG/BIZ/HR/manager-approved-pipeline-actions/) | ORG › BIZ › HR | A | strong |
| AWF-0145 | [Calendar time audit](../workflows/ORG/XFN/INBOX/calendar-time-audit/) | ORG › XFN › INBOX | A | partial |
| AWF-0146 | [Pick-then-summarise research digest](../workflows/ORG/XFN/PKM/pick-then-summarise-research-digest/) | ORG › XFN › PKM | A | partial |
| AWF-0147 | [Analyst-verified lease abstracts](../workflows/unplaced/analyst-verified-lease-abstracts/) | unplaced (proposed ORG › RE › LEASEADMIN) | A | strong |
| AWF-0148 | [Broker-reviewed entry prep](../workflows/unplaced/broker-reviewed-entry-prep/) | unplaced (proposed ORG › LOG › CUSTOMS) | B | weak |
| AWF-0149 | [Decision-ready submission triage](../workflows/unplaced/decision-ready-submission-triage/) | unplaced (proposed PRO › INS › UW) | B | partial |
| AWF-0150 | [Email-to-order freight agents](../workflows/unplaced/email-to-order-freight-agents/) | unplaced (proposed ORG › LOG › FREIGHT) | A | strong |
| AWF-0151 | [First-pass submittal review](../workflows/unplaced/first-pass-submittal-review/) | unplaced (proposed TEC › ENG › SUBMITTAL) | B | partial |
| AWF-0152 | [Layered safety audit agents](../workflows/unplaced/layered-safety-audit-agents/) | unplaced (proposed ORG › BIZ › EHS) | B | weak |
| AWF-0153 | [Missed-pickup call-and-decide](../workflows/unplaced/missed-pickup-call-and-decide/) | unplaced (proposed ORG › LOG › FREIGHT) | A | strong |
| AWF-0154 | [Plot-registered agronomy advice](../workflows/unplaced/plot-registered-agronomy-advice/) | unplaced (proposed ORG › AGR › ADVISORY) | A | weak |
| AWF-0155 | [Underwriter-reviewed broker quote](../workflows/unplaced/underwriter-reviewed-broker-quote/) | unplaced (proposed PRO › INS › UW) | A | strong |
