# New Workflows for Empty Categories

**Date:** 2026-11-06
**Question:** for each of the 56 classes in `taxonomy.yaml` that had no workflow, what is the best-documented real agentic workflow professionals run, and how strong is the public evidence for it?

## Result

Every one of the 56 empty classes now has a draft workflow, AWF-0032 to AWF-0087. The catalog has gone from 31 to 87 workflows, and every class in the taxonomy is filled. Both phyla that were empty before now have workflows: ENG (physical engineering) and GOV (public sector).

| Public evidence | New workflows |
|---|---|
| **Strong**: first-hand, detailed, high confidence | 22 |
| **Partial**: first-hand, but thinner or medium confidence | 19 |
| **Weak**: only vendor, secondary or anonymous accounts | 15 |

Evidence grades: 36 A, 19 B, 1 C. All of them are `draft` until someone adds a real example run.

## Method

1. **Research:** six agents ran in parallel, one per area (PRO, COM, TEC ×2, CRE, ORG), and searched in English and Chinese. For each class they looked for a workflow that meets the four criteria in [TAXONOMY.md](../TAXONOMY.md). If they found nothing, they were told to say "none found" rather than invent an entry. No class ended up "none found".
2. **Re-check:** four separate checker agents re-opened every public run cited (85 in total) and compared each number with the page's own wording.
   - 74 numbers matched exactly and 6 closely.
   - 2 were dropped: a help-desk blog that now redirects to an unrelated site, and an FEA video whose timing claim couldn't be heard.
   - 12 "first-hand" labels were corrected. Most turned out to be vendor pages, studies, or secondary write-ups.
3. **Entries:** each workflow went into its class folder with the catalog's standard sections: shape, steps, output, failure modes, public runs and sources. Sources that were seen only in search excerpts are marked as such.

## Caveats

- **Thin evidence:**
  - PMO (AWF-0084) rests on one self-promoting post and is graded C.
  - GAMEART, TRANS, MFG and DATAENG lean on vendor or third-party accounts.
  - CAD's best run comes from a maker doing 3D printing, not professional mechanical or AEC design.
- **Possible overlaps to watch:**
  - LND (AWF-0043) with AWF-0027 Backward-design course.
  - GRANT (AWF-0045) with AWF-0010 Reviewer-response revision.
  - HELPDESK (AWF-0068) with AWF-0021 Procedure agent.

  Each entry's "How it differs" line explains the difference.
- **One is not an LLM agent:** CIVIC (AWF-0082) is a classical ML classifier pipeline. It meets the four criteria but is less agentic than the rest.

## New workflows

| ID | Workflow | Class | Evidence | Public runs |
|---|---|---|---|---|
| AWF-0032 | [Criteria-gated prior auth](../workflows/PRO/HLT/RCM/criteria-gated-prior-auth/) | PRO › HLT › RCM | A | strong |
| AWF-0033 | [Coordinator-reviewed prescreen](../workflows/PRO/HLT/CLINTRIAL/coordinator-reviewed-prescreen/) | PRO › HLT › CLINTRIAL | A | strong |
| AWF-0034 | [Chemist-gated DMTA loop](../workflows/PRO/HLT/DRUGDISC/chemist-gated-dmta-loop/) | PRO › HLT › DRUGDISC | B | partial |
| AWF-0035 | [Validated GenAI first-pass](../workflows/PRO/LEG/LITIG/validated-genai-first-pass/) | PRO › LEG › LITIG | A | weak |
| AWF-0036 | [Obligations register build](../workflows/PRO/LEG/REG/obligations-register-build/) | PRO › LEG › REG | A | partial |
| AWF-0037 | [Data-room red-flag review](../workflows/PRO/LEG/DD/data-room-red-flag-review/) | PRO › LEG › DD | B | weak |
| AWF-0038 | [Workpaper-matched close agents](../workflows/PRO/FIN/CLOSE/workpaper-matched-close/) | PRO › FIN › CLOSE | B | partial |
| AWF-0039 | [Drafted variance narratives](../workflows/PRO/FIN/FPA/drafted-variance-narratives/) | PRO › FIN › FPA | B | weak |
| AWF-0040 | [Full-population control testing](../workflows/PRO/FIN/AUDIT/full-population-control-testing/) | PRO › FIN › AUDIT | B | partial |
| AWF-0041 | [Review-ready 1040 prep](../workflows/PRO/FIN/TAX/review-ready-1040-prep/) | PRO › FIN › TAX | B | weak |
| AWF-0042 | [Tutor-approved AI turns](../workflows/PRO/EDU/TUTOR/tutor-approved-ai-turns/) | PRO › EDU › TUTOR | A | strong |
| AWF-0043 | [SME-docs to e-learning](../workflows/PRO/EDU/LND/sme-docs-to-elearning/) | PRO › EDU › LND | B | weak |
| AWF-0044 | [Gated replication run](../workflows/PRO/RES/ANALYSIS/gated-replication-run/) | PRO › RES › ANALYSIS | A | strong |
| AWF-0045 | [Critique-first grant draft](../workflows/PRO/RES/GRANT/critique-first-grant-draft/) | PRO › RES › GRANT | B | weak |
| AWF-0046 | [Review-of-review feedback](../workflows/PRO/RES/PEER/review-of-review-feedback/) | PRO › RES › PEER | A | strong |
| AWF-0047 | [Calibrated conversation scoring](../workflows/COM/CSX/QA/calibrated-conversation-scoring/) | COM › CSX › QA | A | strong |
| AWF-0048 | [Gap-match knowledge upkeep](../workflows/COM/CSX/KB/gap-match-knowledge-upkeep/) | COM › CSX › KB | A | strong |
| AWF-0049 | [Renewal-window risk brief](../workflows/COM/CSX/CS/renewal-window-risk-brief/) | COM › CSX › CS | B | weak |
| AWF-0050 | [Call-to-CRM diff approval](../workflows/COM/SAL/DEAL/call-to-crm-diff-approval/) | COM › SAL › DEAL | B | partial |
| AWF-0051 | [Governed-library response draft](../workflows/COM/SAL/RFP/governed-library-response-draft/) | COM › SAL › RFP | A | strong |
| AWF-0052 | [Propose-confirm pipeline sweep](../workflows/COM/SAL/REVOPS/propose-confirm-pipeline-sweep/) | COM › SAL › REVOPS | B | weak |
| AWF-0053 | [Plan-to-calendar drafting](../workflows/COM/MKT/SOCIAL/plan-to-calendar-drafting/) | COM › MKT › SOCIAL | A | partial |
| AWF-0054 | [Guardrailed campaign build](../workflows/COM/MKT/LIFECYCLE/guardrailed-campaign-build/) | COM › MKT › LIFECYCLE | A | partial |
| AWF-0055 | [Routed competitive digest](../workflows/COM/MKT/MKTRES/routed-competitive-digest/) | COM › MKT › MKTRES | A | partial |
| AWF-0056 | [Phased preview build](../workflows/TEC/ENG/CAD/phased-preview-build/) | TEC › ENG › CAD | A | strong |
| AWF-0057 | [Engineer-checked CFD run](../workflows/TEC/ENG/SIM/engineer-checked-cfd-run/) | TEC › ENG › SIM | A | strong |
| AWF-0058 | [Cited pre-screen checks](../workflows/TEC/ENG/CODECOMP/cited-pre-screen-checks/) | TEC › ENG › CODECOMP | A | strong |
| AWF-0059 | [Drawing-to-route draft](../workflows/TEC/ENG/MFG/drawing-to-route-draft/) | TEC › ENG › MFG | B | weak |
| AWF-0060 | [Spec-to-ticket planning](../workflows/TEC/PRD/PM/spec-to-ticket-planning/) | TEC › PRD › PM | A | strong |
| AWF-0061 | [Quote-verified synthesis](../workflows/TEC/PRD/UXR/quote-verified-synthesis/) | TEC › PRD › UXR | A | strong |
| AWF-0062 | [Spec-bound screen options](../workflows/TEC/PRD/UI/spec-bound-screen-options/) | TEC › PRD › UI | A | strong |
| AWF-0063 | [Diff-proven dbt migration](../workflows/TEC/DAT/DATAENG/diff-proven-dbt-migration/) | TEC › DAT › DATAENG | B | weak |
| AWF-0064 | [Repo-grounded analysis](../workflows/TEC/DAT/DS/repo-grounded-analysis/) | TEC › DAT › DS | A | strong |
| AWF-0065 | [Overnight experiment ratchet](../workflows/TEC/DAT/MLOPS/overnight-experiment-ratchet/) | TEC › DAT › MLOPS | A | strong |
| AWF-0066 | [Chat-to-IaC change](../workflows/TEC/ITS/INFRA/chat-to-iac-change/) | TEC › ITS › INFRA | A | partial |
| AWF-0067 | [Sanitizer-bug autopatch](../workflows/TEC/ITS/APPSEC/sanitizer-bug-autopatch/) | TEC › ITS › APPSEC | A | partial |
| AWF-0068 | [Slack IT request agent](../workflows/TEC/ITS/HELPDESK/slack-it-request-agent/) | TEC › ITS › HELPDESK | B | weak |
| AWF-0069 | [Filtered test augmentation](../workflows/TEC/SWE/TEST/filtered-test-augmentation/) | TEC › SWE › TEST | A | strong |
| AWF-0070 | [Graded PR comments](../workflows/TEC/SWE/REVIEW/graded-pr-comments/) | TEC › SWE › REVIEW | A | strong |
| AWF-0071 | [Reproduce-first bug fix](../workflows/TEC/SWE/DEBUG/reproduce-first-bug-fix/) | TEC › SWE › DEBUG | A | strong |
| AWF-0072 | [Guardrailed design spec](../workflows/TEC/SWE/ARCH/guardrailed-design-spec/) | TEC › SWE › ARCH | A | partial |
| AWF-0073 | [Dossier-to-chapter book](../workflows/CRE/WRI/NONFIC/dossier-to-chapter-book/) | CRE › WRI › NONFIC | A | partial |
| AWF-0074 | [Reporter-notes rewrite desk](../workflows/CRE/WRI/JOURN/reporter-notes-rewrite-desk/) | CRE › WRI › JOURN | A | partial |
| AWF-0075 | [Code-PR docs drafts](../workflows/CRE/WRI/TECHW/code-pr-docs-drafts/) | CRE › WRI › TECHW | A | strong |
| AWF-0076 | [Glossary-backed MTPE serial](../workflows/CRE/WRI/TRANS/glossary-backed-mtpe-serial/) | CRE › WRI › TRANS | B | weak |
| AWF-0077 | [Transcript-first video edit](../workflows/CRE/MED/POST/transcript-first-video-edit/) | CRE › MED › POST | A | partial |
| AWF-0078 | [Episode post-production chain](../workflows/CRE/MED/AUDIO/episode-post-production-chain/) | CRE › MED › AUDIO | A | partial |
| AWF-0079 | [Concept-led SD asset stream](../workflows/CRE/MED/GAMEART/concept-led-sd-asset-stream/) | CRE › MED › GAMEART | B | partial |
| AWF-0080 | [Theme sign-off consultation analysis](../workflows/ORG/GOV/POLICY/theme-sign-off-consultation-analysis/) | ORG › GOV › POLICY | A | strong |
| AWF-0081 | [Summary-aided casework decision](../workflows/ORG/GOV/CASEWORK/summary-aided-casework-decision/) | ORG › GOV › CASEWORK | A | partial |
| AWF-0082 | [Model-triaged records release](../workflows/ORG/GOV/CIVIC/model-triaged-records-release/) | ORG › GOV › CIVIC | A | strong |
| AWF-0083 | [Bounded tail-spend negotiation](../workflows/ORG/BIZ/PROC/bounded-tail-spend-negotiation/) | ORG › BIZ › PROC | B | weak |
| AWF-0084 | [Data-pulled status report](../workflows/ORG/BIZ/PMO/data-pulled-status-report/) | ORG › BIZ › PMO | C | weak |
| AWF-0085 | [Policy-checked expense audit](../workflows/ORG/BIZ/ADMIN/policy-checked-expense-audit/) | ORG › BIZ › ADMIN | B | weak |
| AWF-0086 | [Template-driven meeting minutes](../workflows/ORG/XFN/MEET/template-driven-meeting-minutes/) | ORG › XFN › MEET | B | partial |
| AWF-0087 | [Diff-reviewed vault upkeep](../workflows/ORG/XFN/PKM/diff-reviewed-vault-upkeep/) | ORG › XFN › PKM | A | partial |
