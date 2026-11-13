# Entry standard

What every workflow entry must contain, and how to write it. [templates/workflow/README.md](templates/workflow/README.md) is the blank form. Four finished entries, one per agent form, are the models to copy:

| Form | Model entry |
|---|---|
| `skill` | [AWF-0024 Playbook contract review](workflows/PRO/LEG/CONTRACT/playbook-contract-review/) |
| `project` | [AWF-0001 Plan-gated build](workflows/TEC/SWE/FEAT/plan-gated-build/) |
| `service` | [AWF-0164 Exception-only reconciliation run](workflows/PRO/FIN/CLOSE/exception-only-reconciliation/) |
| `platform` | [AWF-0137 Gated AI 漫剧 line](workflows/CRE/MED/SHORTDRAMA/gated-ai-manju-line/) |

An entry answers three questions, in this order:

1. **What is this job?** A reader from another field must be able to follow it. → `## Background`
2. **How would I run it with an agent today?** → `## Build it with an agent`
3. **What did people who ran it actually do, and how do we know?** → `## Steps`, `## Public runs`, `## Sources`

The third part is evidence and stays tied to its sources. The first two are written by the catalog and are held to different rules, set out below.

An entry is in this format once its front matter has a `build` field. `python scripts/validate.py` checks those entries against this page and reports how many are done. Entries without `build` are in the older format and still pass, so the catalog can be converted in batches ([research/prompts/convert.md](research/prompts/convert.md) is the brief for that work).

## 1. Layout

```
front matter            adds  build: <form>  and  method_checked: YYYY-MM
# Name
badge line · **Shape:** · **Agent kit:** (if any) · **Variants:** · generated diagram
## Background
## Build it with an agent
## Steps                then **Output:**, **Failure modes → guards:**, **How it differs:**
## Public runs
## Sources
```

`**How it differs:**` moves from the top of the entry to the end of Steps. It compares catalog entries with each other, which matters to maintainers and not to a first-time reader. `**Input:**` and `**Roles/Tools:**` lines are dropped; their content goes into **You need** (§3).

## 2. Background

Three to six sentences in plain words, then an optional term list. Write for someone who has never worked in this field.

Cover, in this order:

1. **The job:** what the work is, who does it, and what triggers it.
2. **Why it is slow or risky by hand.**
3. **What the agent takes over and what stays with a person**, and why that person cannot be removed (legal duty, money, judgement).

Then, if the entry uses words a general reader would not know:

```
**Terms:**
- **accrual**: an expense recorded in the month it was incurred, before the invoice arrives.
- **抽卡**: generating many candidates for one shot and keeping the best, named after drawing cards in games.
```

Rules:

- Define every trade term, abbreviation and Chinese industry term the entry uses, here or at first use. Keep Chinese terms as written and gloss them once.
- General knowledge about a profession needs no citation. Anything about a particular organisation, and every number, does, and belongs in Steps or Public runs instead.
- No product names unless the job cannot be described without them.
- At least 40 words before the term list. `validate.py` checks this.

## 3. Build it with an agent

How to run this workflow with a general-purpose agent, using the smallest setup that works. It is a design written by the catalog from the entry's steps and the tool documentation. It is not evidence, and it must say so.

Fixed parts, in this order:

```
**Form:** `skill`. One sentence on why this is the smallest form that works.

**You need:** the files, connectors and permissions the agent must have before it starts.

| Step | Built as |
|---|---|
| each step or group of steps from the shape | the building block that does it |

**Checkpoints:** for each 🛑 type in the shape, written as `plan`, `review` and so on: how the agent is made to stop, and what the person sees.

**Since the sources:** what the sources built by hand that current tooling now provides, what the build above leaves out, and what still cannot be done with a general agent. Write "Nothing material." if that is the case.

*A design based on this entry's steps and the tool documentation as of YYYY-MM, not a reported run.*
```

If the entry has a kit in `variants/claude-code.md`, link it in the **Form** line. The kit is the build written out as files.

### Choosing the form

Pick the first row that fits. `build` in the front matter carries the same word.

| Form | Use it when | What it consists of |
|---|---|---|
| `skill` | One person runs one item at a time and stays in the conversation. | One `SKILL.md` (plus reference files or scripts beside it), run in Claude Code or any app that loads skills. It may use built-in subagents for parallel checks. Checkpoints are places where the skill tells the agent to stop and ask. |
| `project` | A skill is not enough: the work needs a rule that must hold every time, a reviewer that has not seen the work, custom parallel workers, or standing project knowledge. | A Claude Code project: `CLAUDE.md`, one or more skills, custom subagents, hooks, MCP connections. Package it as a plugin to share it. |
| `service` | Nobody is at the keyboard when it starts: it runs on a schedule, on an event, or on a queue, and people see only exceptions, samples or approval requests. | The same skills and subagents, run headless by a cloud scheduled task, `claude -p`, or an Agent SDK program. State lives in a store outside the conversation. Checkpoints become messages to a queue, ticket or chat channel that a person answers later. |
| `platform` | A core step needs something a general agent cannot substitute: a specialist model (video, speech, protein), a regulated or embedded system (an EHR, a core banking system), or physical equipment. | Say which steps a general agent can run in one of the three forms above, and which steps need the platform. |

Do not choose a larger form because the source used one. A source that built seven named agents on a cloud platform may be describing work that one skill with three parallel checks does today. Say so in **Since the sources**.

### Building blocks

Use these names, with these meanings, in the **Built as** column. They were checked against the Claude Code and Agent SDK documentation in 2026-11. Do not name a feature that is not in this table unless you have opened its documentation page and cite it in **Since the sources**.

| Block | What it does | Use it for | Docs |
|---|---|---|---|
| `CLAUDE.md` | Instructions loaded into every session. A request to the agent, not an enforced rule. | Conventions, commands, "never do X". | [memory](https://code.claude.com/docs/en/memory) |
| Skill | A Markdown file of instructions and reference material, loaded on demand or by `/name`. | The procedure itself; playbooks, checklists, templates. | [skills](https://code.claude.com/docs/en/skills) |
| Subagent | A worker with its own context that returns a summary. | Parallel checks, reading many files, a reviewer that has not seen the work. | [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| Dynamic workflow | A script the agent writes that runs dozens to hundreds of subagents and can cross-check their results. It cannot take user input mid-run. | Fan-out over many items between two checkpoints. | [workflows](https://code.claude.com/docs/en/workflows) |
| Hook | A script that runs on a lifecycle event, whatever the agent decides. Can block a tool call. | Rules that must hold every time: block an edit, block a send, log every action. | [hooks](https://code.claude.com/docs/en/hooks-guide) |
| MCP server (connector) | Tools and data from an outside system. | Reading or writing the ticket system, CRM, database, mail. | [mcp](https://code.claude.com/docs/en/mcp) |
| Permission rule or mode | Which tool calls run without asking, which ask, which are denied. Plan mode reads without editing. | `action` checkpoints; keeping an agent read-only. | [permissions](https://code.claude.com/docs/en/permissions) |
| Plugin | A package of skills, subagents, hooks and MCP servers. | Sharing a `project` build with a team. | [plugins](https://code.claude.com/docs/en/plugins/overview) |
| Cloud scheduled task | A saved prompt, repositories and connectors that run in the cloud on a schedule, an API call or a GitHub event. Research preview. | `service` builds that need no code of your own. | [routines](https://code.claude.com/docs/en/routines) |
| `claude -p` (headless) | Claude Code run from a script or CI job with no interactive prompt. | `service` builds triggered by your own scheduler or pipeline. | [headless](https://code.claude.com/docs/en/headless) |
| Agent SDK | Claude Code as a Python or TypeScript library. `canUseTool` receives each approval request and each question; a `PreToolUse` hook can defer a call so the process exits and resumes when a person answers. | `service` builds with their own approval screen, queue or state store. | [agent-sdk](https://code.claude.com/docs/en/agent-sdk/overview) |

Entries describe one vendor's blocks because the catalog's kits target Claude Code. Other agent tools have equivalents for most of them (an `AGENTS.md` file, skills, subagents, headless runs); the form choice carries over.

### How checkpoints are held

| Checkpoint | `skill` or `project` | `service` |
|---|---|---|
| `plan` | The skill writes the plan to a file and stops until the person approves; or plan mode. | The run ends after posting the plan; an approved plan starts the next run. |
| `action` | A permission rule set to ask for that tool; a `PreToolUse` hook for a rule that must never be skipped. | `canUseTool` routes the request to an approver; or the agent only prepares the action (a parked entry, a draft) and has no tool to commit it. |
| `review` | The skill stops and presents the draft. | The draft goes to a review queue; the agent has no send or publish tool. |
| `sample` | Not applicable: a person is present for every item. | A fixed share of outputs is copied to a review queue; results feed back into thresholds. |
| `sign-off` | The skill stops; the named professional acts in their own system. The agent has no tool to send, file, pay or publish. | The same: the final act is outside the agent's tools. |
| `handoff` | The skill stops and states what it could not decide and why. | The item goes to a person's queue with the evidence gathered so far. |

An instruction in a skill or `CLAUDE.md` asks the agent to stop. Where a missed stop would cost money, break a law or reach a customer, the build must also remove the tool or block it with a hook or permission rule, and **Checkpoints** must say which.

### Rules for this section

- Write only what follows from the entry's steps and from documentation you have opened. No performance claims, no time or cost savings, no "works well".
- Do not describe the build as something anyone ran. Reported runs go in Public runs; a contributor's own run goes in `examples/`.
- Every 🛑 type in `checkpoints` must appear in **Checkpoints** in backticks. `validate.py` checks this.
- Name data the agent must not hold or send where the field has such limits (client-privileged documents, patient records, personal data), under **You need**.

## 4. Steps

Steps remain the record of what the sources report. In this format they must also be readable without the source open:

- Start each step with who acts: the agent, a named role, or a system.
- Replace a source's infrastructure names with what the component does ("a scheduled job checks the ERP for purchase orders that need an accrual"). Keep a product name only when it is the point; the full stack belongs in `variants`.
- Use the terms defined in Background. Do not introduce new undefined ones.
- Keep every citation, number and 🛑 marker. Do not add steps the sources do not support.
- Open the section with `*As reported by the sources.*` when the build above differs from it.

## 5. Two dates

| Field | Means | Set it when |
|---|---|---|
| `last_verified` | The entry's sources and public runs were re-opened and still say what the entry says. | After re-opening them ([MAINTAINING.md](MAINTAINING.md), "Re-checking an entry"). |
| `method_checked` | The Build section was compared with current agent tooling: the form is still the smallest that works and every named building block still exists under that name. | After writing or re-reading the Build section against the documentation. |

The first date says the evidence is intact. The second says the advice is current. An entry can have recent evidence and an old method, or the reverse.

## 6. Chinese version

`README.zh-CN.md` carries the same two sections as `## 背景` and `## 用智能体搭建`, with the labels **术语：**, **形态：**, **需要：**, **检查点：**, **与来源相比：** and the same closing note. Keep the form word, the building-block names, the checkpoint words in backticks, the table rows, links and numbers identical to the English. [i18n/TRANSLATING.md](i18n/TRANSLATING.md) has the full rules.

## 7. When an entry does not survive conversion

Converting an entry sometimes shows that it is not a workflow a reader could rerun: the source is a press release with no steps, or the "agent" is one product feature. Do not pad it. Write the Background, set `build: platform`, say in **Since the sources** that the public material does not support a build, and list the entry in your conversion report for a maintainer to consider retiring (TAXONOMY.md rule 6).
