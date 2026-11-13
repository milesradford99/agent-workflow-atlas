# Third Collection Pass

**Date:** 2026-11-13
**Question:** which real agentic workflows, documented in 2025–2026, are still missing from the catalog, and what newer evidence exists for the workflows it already has?

## Result

60 new draft workflows, AWF-0156 to AWF-0215, bring the catalog to 215. Twenty existing workflows got newer public runs, sources or practice notes.

| | Count |
|---|---|
| New, placed in an existing class | 51 |
| New, unplaced (waiting for a class) | 9 |
| Evidence A / B | 38 / 22 |
| Public runs on new entries: Strong / Partial / Weak / None found | 31 / 9 / 19 / 1 |
| Risk low / medium / high | 24 / 23 / 13 |
| Existing workflows enriched | 20 |

As in the earlier passes, a workflow went in only if it fails the swap test against every workflow already in its class: a different deliverable, different human checkpoints, or a different autonomy level. Each entry's "How it differs" line names the nearest workflow. Many of the new entries move a checkpoint compared with the existing ones: a bot that approves low-risk PRs itself (AWF-0182), a payer that auto-approves but never auto-denies prior authorizations (AWF-0156), or a supervisor who watches several live AI calls and can take any of them over (AWF-0175).

## Enrichment of existing entries

For each existing workflow in its classes, the research agent looked for first-hand accounts, sources or tool changes from 2025–2026 that the entry did not already cite. New runs went into the entry's Public runs section, and new sources were added to its numbered list. Concrete changes in how teams run the workflow went under a short **Recent practice (2026)** note, each citing its source. Coverage grades were raised where a new run justified it, and never lowered. Two entries moved from evidence B to A because they gained first-hand engineering or operator accounts: AWF-0008 (Doctolib, BILL) and AWF-0148 (C.H. Robinson). Six entries gained tool variants.

## New taxonomy (proposals, not made here)

CONTRIBUTING.md opens a class in a separate pull request once three unplaced workflows would go in it. Two fields now qualify:

- **`PRO/INS/UW` insurance underwriting:** AWF-0149, AWF-0155 and the new AWF-0163 (Aviva and Vitality GP-report summaries).
- **`ORG/LOG/FREIGHT` freight brokerage:** AWF-0150, AWF-0153 and the new AWF-0209 (carrier-call booking agents).

Still short of three:

- construction submittals ×2;
- customs, real estate, agriculture and EHS ×2 each;
- energy interconnection, field-service dispatch and pharmacy ×1 each.

## Method

1. **Plan.** All 155 workflows were exported with their shape lines. The classes were split into seven groups, plus an eighth group for fields outside the taxonomy, and a maintainer approved the split. Each agent was asked for 0–1 new workflows per class.
2. **Research.** Eight agents worked in parallel from [research/prompts/collect.md](prompts/collect.md). The brief had one addition: for the existing workflows in its classes, each agent also returned newer runs and sources in an `enrich` block. The session's plain fetch tool was blocked for most hosts, so the agents read pages through Exa's fetch tool. In total they ran about 100 searches.
3. **Merge.** One candidate, a resident maintenance triage workflow, turned out to be the same workflow as AWF-0108, so its two runs were added to AWF-0108 instead. One candidate was dropped: a simulator-gated PLC build. Its main run came from a tool its developer described as still being finished, and the second source did not mention a simulator gate.
4. **Re-check.** Five separate checkers ([research/prompts/check.md](prompts/check.md)) re-opened all 216 cited links: 145 public runs and 71 sources.
   - All 145 claimed numbers matched the page exactly, and every link opened.
   - Of the 71 sources, 64 support the claim they are cited for. Seven only partly support it and are cited for the narrower claim.
   - The checkers' first-hand labels replaced the researchers' in 7 cases, among them vendor, study and second-hand news.
   - Three new entries fell from evidence A to B because no run was left with a first-hand label: the live-commerce 口播稿 drafting, the PR-reviewed research wiki and the carrier-call booking agent. The spec-to-submittal register also fell to B: its only first-hand run is a prototype benchmark in an academic article, not a deployment.
   - One practice note carried figures (a 16-second median review time and 12% new themes) that no checker had confirmed. They were confirmed by hand on the i.AI evaluation page, which the note now links.
5. **File.** Entries were generated in the standard format, with Chinese names and summaries in `i18n/workflows.zh-CN.yaml`. Diagrams and the index were rebuilt and all checks pass.

## Coverage gaps

- **Not searched for lack of budget:** DRUGDISC, CODECOMP, UI, PROTO, NONFIC, GAMEART, PMO, ADMIN, INBOX and PKM. Start the next sweep with these.
- **Searched, nothing new that passed:** STRAT, PROSPECT, RFP, REVOPS, CATALOG, ADS, SOCIAL, AP, FPA, AUDIT, COURSE, TUTOR, LND, LITREV, GRANT, RESEARCH, DD, FICTION, SHORTDRAMA, AIGCVIDEO, DUB, PM, MLOPS, DS, CAD and MFG.
- **Most existing entries were not re-searched.** Enrichment reached 20 of 155. All 155 still have `last_verified: 2026-11`, so the whole catalog falls due for re-checking together in May 2027.
- **Leads not followed:**
  - Meta's RADAR paper on PR auto-approval (dl.acm.org/doi/10.1145/3832783.3834493);
  - an AWS post on Mary Kay's drift-to-PR system;
  - a deal-desk auto-approval workflow whose only numbered source would not open.

## Caveats

- **Vendor-heavy entries.** Renewals, voice-agent supervision, RFQ quoting, lifecycle decisioning, subrogation, tax notices, records redaction, supplier onboarding and most of the new unplaced fields rest on vendor case studies (evidence B). Treat them as leads until a practitioner adds an example run.
- **Weak single runs.**
  - The renewals entry's main figure comes from a live demo at a vendor conference, not a customer result.
  - The simulation campaign entry describes the vendor's own demo campaign.
  - The code-change doc refresh entry has no public run with a number.
- **Class fit.**
  - Pharmacovigilance case intake sits in `PRO/HLT/CLINTRIAL` because there is no safety class.
  - The end-to-end AI paper (`PRO/RES/WRITE`) produces manuscripts that were submitted to peer review only as disclosed experiments.
- **Risk.** Clinical, legal, regulatory, benefits, hiring-adjacent, pharmacy, energy and records entries are tagged `high`.

## New workflows

| ID | Workflow | Class | Evidence | Public runs |
|---|---|---|---|---|
| AWF-0156 | [Approve-only payer auto-auth](../workflows/PRO/HLT/RCM/approve-only-payer-auto-auth/) | PRO › HLT › RCM | A | strong |
| AWF-0157 | [Nightly hospital-course drafts](../workflows/PRO/HLT/CLINDOC/nightly-hospital-course-drafts/) | PRO › HLT › CLINDOC | A | strong |
| AWF-0158 | [QC-gated safety case intake](../workflows/PRO/HLT/CLINTRIAL/qc-gated-safety-case-intake/) | PRO › HLT › CLINTRIAL | A | strong |
| AWF-0159 | [Sample-tuned contract abstraction](../workflows/PRO/LEG/CONTRACT/sample-tuned-contract-abstraction/) | PRO › LEG › CONTRACT | A | strong |
| AWF-0160 | [Sampled DSAR disclosure](../workflows/PRO/LEG/REG/sampled-dsar-disclosure/) | PRO › LEG › REG | A | partial |
| AWF-0161 | [Page-cited medical chronology](../workflows/PRO/LEG/LITIG/page-cited-medical-chronology/) | PRO › LEG › LITIG | B | weak |
| AWF-0162 | [Subrogation alert triage](../workflows/PRO/INS/CLAIMS/subrogation-alert-triage/) | PRO › INS › CLAIMS | B | weak |
| AWF-0163 | [Summarised GP-report underwriting](../workflows/unplaced/summarised-gp-report-underwriting/) | unplaced (proposed PRO › INS › UW) | A | strong |
| AWF-0164 | [Exception-only reconciliation run](../workflows/PRO/FIN/CLOSE/exception-only-reconciliation/) | PRO › FIN › CLOSE | A | partial |
| AWF-0165 | [Issue-split notice reply](../workflows/PRO/FIN/TAX/issue-split-notice-reply/) | PRO › FIN › TAX | B | weak |
| AWF-0166 | [Challenger-agent IC memo](../workflows/PRO/FIN/INVEST/challenger-agent-ic-memo/) | PRO › FIN › INVEST | A | partial |
| AWF-0167 | [AI-blended comparative judgement](../workflows/PRO/EDU/ASSESS/ai-blended-comparative-judgement/) | PRO › EDU › ASSESS | A | strong |
| AWF-0168 | [Lab-in-the-loop discovery](../workflows/PRO/RES/ANALYSIS/lab-in-the-loop-discovery/) | PRO › RES › ANALYSIS | A | strong |
| AWF-0169 | [End-to-end AI paper](../workflows/PRO/RES/WRITE/end-to-end-ai-paper/) | PRO › RES › WRITE | A | strong |
| AWF-0170 | [Added AI review](../workflows/PRO/RES/PEER/added-ai-review/) | PRO › RES › PEER | A | strong |
| AWF-0171 | [Backtested synthetic panel](../workflows/COM/MKT/MKTRES/backtested-synthetic-panel/) | COM › MKT › MKTRES | A | strong |
| AWF-0172 | [Simulation release gate](../workflows/COM/CSX/QA/simulation-release-gate/) | COM › CSX › QA | A | strong |
| AWF-0173 | [Code-change doc refresh](../workflows/COM/CSX/KB/code-change-doc-refresh/) | COM › CSX › KB | B | none found |
| AWF-0174 | [Autonomous long-tail renewals](../workflows/COM/CSX/CS/autonomous-long-tail-renewals/) | COM › CSX › CS | B | weak |
| AWF-0175 | [Supervised voice agent](../workflows/COM/CSX/RESOLVE/supervised-voice-agent/) | COM › CSX › RESOLVE | B | weak |
| AWF-0176 | [RFQ-to-quote drafting](../workflows/COM/SAL/DEAL/rfq-to-quote-drafting/) | COM › SAL › DEAL | B | weak |
| AWF-0177 | [Live-commerce 口播稿 drafting](../workflows/COM/MKT/CONTENT/live-commerce-script-drafting/) | COM › MKT › CONTENT | B | weak |
| AWF-0178 | [Guardrailed 1:1 decisioning](../workflows/COM/MKT/LIFECYCLE/guardrailed-one-to-one-decisioning/) | COM › MKT › LIFECYCLE | B | weak |
| AWF-0179 | [Spec-PR then agent build](../workflows/TEC/SWE/FEAT/spec-pr-then-agent-build/) | TEC › SWE › FEAT | A | strong |
| AWF-0180 | [Stale-flag cleanup PRs](../workflows/TEC/SWE/MAINT/stale-flag-cleanup-prs/) | TEC › SWE › MAINT | A | strong |
| AWF-0181 | [Scenario release sweep](../workflows/TEC/SWE/TEST/scenario-release-sweep/) | TEC › SWE › TEST | A | strong |
| AWF-0182 | [Risk-gated auto-approval](../workflows/TEC/SWE/REVIEW/risk-gated-auto-approval/) | TEC › SWE › REVIEW | A | strong |
| AWF-0183 | [On-demand alert investigation](../workflows/TEC/SWE/DEBUG/on-demand-alert-investigation/) | TEC › SWE › DEBUG | A | strong |
| AWF-0184 | [Guideline-checked design review](../workflows/TEC/SWE/ARCH/guideline-checked-design-review/) | TEC › SWE › ARCH | A | partial |
| AWF-0185 | [Agent-run war room](../workflows/TEC/ITS/SRE/agent-run-war-room/) | TEC › ITS › SRE | A | partial |
| AWF-0186 | [Plan-verified drift fixes](../workflows/TEC/ITS/INFRA/plan-verified-drift-fixes/) | TEC › ITS › INFRA | A | strong |
| AWF-0187 | [Purple-team detection build](../workflows/TEC/ITS/SECOPS/purple-team-detection-build/) | TEC › ITS › SECOPS | A | strong |
| AWF-0188 | [Scheduled vuln-fix PRs](../workflows/TEC/ITS/APPSEC/scheduled-vuln-fix-prs/) | TEC › ITS › APPSEC | A | partial |
| AWF-0189 | [Self-repair before handoff](../workflows/TEC/ITS/HELPDESK/self-repair-before-handoff/) | TEC › ITS › HELPDESK | A | strong |
| AWF-0190 | [Spec-to-submittal register](../workflows/unplaced/spec-to-submittal-register/) | unplaced (proposed TEC › ENG › SUBMITTAL) | B | strong |
| AWF-0191 | [Unprompted pipeline repair](../workflows/TEC/DAT/DATAENG/unprompted-pipeline-repair/) | TEC › DAT › DATAENG | A | strong |
| AWF-0192 | [Context-tested Slack analyst](../workflows/TEC/DAT/ANALYTICS/context-tested-slack-analyst/) | TEC › DAT › ANALYTICS | A | strong |
| AWF-0193 | [Unattended simulation campaign](../workflows/TEC/ENG/SIM/unattended-simulation-campaign/) | TEC › ENG › SIM | B | weak |
| AWF-0194 | [Agent-eval docs loop](../workflows/TEC/PRD/DSYS/agent-eval-docs-loop/) | TEC › PRD › DSYS | A | strong |
| AWF-0195 | [PR-reviewed research wiki](../workflows/TEC/PRD/UXR/pr-reviewed-research-wiki/) | TEC › PRD › UXR | B | weak |
| AWF-0196 | [Claim-monitoring fact-check desk](../workflows/CRE/WRI/JOURN/claim-monitoring-fact-check-desk/) | CRE › WRI › JOURN | A | strong |
| AWF-0197 | [Journey-based docs audit](../workflows/CRE/WRI/TECHW/journey-based-docs-audit/) | CRE › WRI › TECHW | A | strong |
| AWF-0198 | [AI-first script triage](../workflows/CRE/WRI/SCREEN/ai-first-script-triage/) | CRE › WRI › SCREEN | B | weak |
| AWF-0199 | [QE-routed MT publishing](../workflows/CRE/WRI/TRANS/qe-routed-mt-publishing/) | CRE › WRI › TRANS | A | strong |
| AWF-0200 | [Agent-crew serial with volume audits](../workflows/CRE/WRI/SERIAL/agent-crew-serial-volume-audits/) | CRE › WRI › SERIAL | A | partial |
| AWF-0201 | [House-voice article audio](../workflows/CRE/MED/AUDIO/house-voice-article-audio/) | CRE › MED › AUDIO | B | weak |
| AWF-0202 | [Editor-curated broadcast clips](../workflows/CRE/MED/POST/editor-curated-broadcast-clips/) | CRE › MED › POST | B | weak |
| AWF-0203 | [Supervisor-approved adviser answers](../workflows/ORG/GOV/CASEWORK/supervisor-approved-adviser-answers/) | ORG › GOV › CASEWORK | A | strong |
| AWF-0204 | [Statute-mapped regulatory review](../workflows/ORG/GOV/POLICY/statute-mapped-regulatory-review/) | ORG › GOV › POLICY | A | strong |
| AWF-0205 | [Exemption-cited records redaction](../workflows/ORG/GOV/CIVIC/exemption-cited-records-redaction/) | ORG › GOV › CIVIC | B | weak |
| AWF-0206 | [Contained HR service desk](../workflows/ORG/BIZ/HR/contained-hr-service-desk/) | ORG › BIZ › HR | A | strong |
| AWF-0207 | [Evidence-gated supplier onboarding](../workflows/ORG/BIZ/PROC/evidence-gated-supplier-onboarding/) | ORG › BIZ › PROC | B | weak |
| AWF-0208 | [Confidence-routed meeting tickets](../workflows/ORG/XFN/MEET/confidence-routed-meeting-tickets/) | ORG › XFN › MEET | A | partial |
| AWF-0209 | [Carrier-call booking agent](../workflows/unplaced/carrier-call-booking-agent/) | unplaced (proposed ORG › LOG › FREIGHT) | B | weak |
| AWF-0210 | [Fast-lane tariff classification](../workflows/unplaced/fast-lane-tariff-classification/) | unplaced (proposed ORG › LOG › CUSTOMS) | B | weak |
| AWF-0211 | [Extension-agent mediated advice](../workflows/unplaced/extension-agent-mediated-advice/) | unplaced (proposed ORG › AGR › ADVISORY) | A | strong |
| AWF-0212 | [Incident-to-signed investigation](../workflows/unplaced/incident-to-signed-investigation/) | unplaced (proposed ORG › BIZ › EHS) | B | partial |
| AWF-0213 | [Cited interconnection readiness review](../workflows/unplaced/cited-interconnection-readiness-review/) | unplaced (proposed ORG › ENE › INTERCONNECT) | B | weak |
| AWF-0214 | [Dispatcher-overridden job assignment](../workflows/unplaced/dispatcher-overridden-job-assignment/) | unplaced (proposed ORG › FSV › DISPATCH) | B | weak |
| AWF-0215 | [Pharmacist-verified script entry](../workflows/unplaced/pharmacist-verified-script-entry/) | unplaced (proposed PRO › HLT › PHARMACY) | A | strong |

## Enriched workflows

| ID | Workflow | Added |
|---|---|---|
| AWF-0008 | [Design to code](../workflows/TEC/PRD/DSYS/design-to-code/) | 2 runs, 2 sources, 2 practice notes |
| AWF-0021 | [Procedure agent](../workflows/COM/CSX/RESOLVE/procedure-agent/) | 1 run, 1 source, 1 practice note |
| AWF-0032 | [Criteria-gated prior auth](../workflows/PRO/HLT/RCM/criteria-gated-prior-auth/) | 2 runs, 1 source, 1 practice note |
| AWF-0040 | [Full-population control testing](../workflows/PRO/FIN/AUDIT/full-population-control-testing/) | 1 run, 2 sources, 1 practice note |
| AWF-0046 | [Review-of-review feedback](../workflows/PRO/RES/PEER/review-of-review-feedback/) | 1 run, 3 sources, 1 practice note |
| AWF-0047 | [Calibrated conversation scoring](../workflows/COM/CSX/QA/calibrated-conversation-scoring/) | 1 run, 2 sources, 2 practice notes |
| AWF-0067 | [Sanitizer-bug autopatch](../workflows/TEC/ITS/APPSEC/sanitizer-bug-autopatch/) | 1 run, 1 source, 2 practice notes |
| AWF-0071 | [Reproduce-first bug fix](../workflows/TEC/SWE/DEBUG/reproduce-first-bug-fix/) | 1 run, 1 source, 1 practice note |
| AWF-0075 | [Code-PR docs drafts](../workflows/CRE/WRI/TECHW/code-pr-docs-drafts/) | 3 runs, 2 sources, 1 practice note |
| AWF-0080 | [Theme sign-off consultation analysis](../workflows/ORG/GOV/POLICY/theme-sign-off-consultation-analysis/) | 2 runs, 2 sources, 1 practice note |
| AWF-0104 | [Hypothesis tournament](../workflows/PRO/RES/LITREV/hypothesis-tournament/) | 2 runs, 1 source, 1 practice note |
| AWF-0108 | [Resident maintenance triage](../workflows/COM/CSX/RESOLVE/resident-maintenance-triage/) | 1 run, 1 source |
| AWF-0139 | [Directed AI audiobook](../workflows/CRE/MED/AUDIO/directed-ai-audiobook/) | 3 runs, 1 source, 3 practice notes |
| AWF-0142 | [Visit-recorded care assessment](../workflows/ORG/GOV/CASEWORK/visit-recorded-care-assessment/) | 2 runs, 2 sources, 1 practice note |
| AWF-0147 | [Analyst-verified lease abstracts](../workflows/unplaced/analyst-verified-lease-abstracts/) | 2 runs, 2 sources, 1 practice note |
| AWF-0148 | [Broker-reviewed entry prep](../workflows/unplaced/broker-reviewed-entry-prep/) | 1 run, 1 source, 1 practice note |
| AWF-0149 | [Decision-ready submission triage](../workflows/unplaced/decision-ready-submission-triage/) | 2 sources, 1 practice note |
| AWF-0150 | [Email-to-order freight agents](../workflows/unplaced/email-to-order-freight-agents/) | 2 runs, 2 sources, 1 practice note |
| AWF-0151 | [First-pass submittal review](../workflows/unplaced/first-pass-submittal-review/) | 4 runs, 2 sources, 2 practice notes |
| AWF-0155 | [Underwriter-reviewed broker quote](../workflows/unplaced/underwriter-reviewed-broker-quote/) | 2 runs, 2 sources, 1 practice note |
