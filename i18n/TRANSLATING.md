# Translating a workflow into Simplified Chinese

Every workflow folder has a `README.zh-CN.md` next to its `README.md`. The Chinese site pages (`w/<ID>/zh/` and the 中文 view of the catalog) are built from it. It translates the whole entry except the sources.

[AWF-0069 Filtered test augmentation](../workflows/TEC/SWE/TEST/filtered-test-augmentation/README.zh-CN.md) is a complete example.

## The file

```
---
id: AWF-0069
name: 筛选式测试补充
summary: "一句话：产出什么、人在哪里把关（≤120 字）。"
deliverable: 单元测试 diff
shape: "挑选已有测试的类 → 每个 提示词 × 温度：生成补充测试 → … → 🛑 sample (工具作者) → 🛑 review (工程师采纳或拒绝)"
source_hash: 1a2b3c4d5e6f
---

# 筛选式测试补充

**与相近工作流的区别：** …
**工具变体：** `testgen-llm` · `qodo-cover`

## 步骤

1. …
5. 🛑 **抽检**：…
6. 🛑 **审阅**：…

**产出：** …
**失败模式 → 防护：** …

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：……

- [Meta, Automated Unit Test Improvement using LLMs at Meta](https://arxiv.org/abs/2402.09171) (2024-02-14)。中文说明。"73% of its recommendations being accepted for production deployment by Meta software engineers"。*第一手：是；可信度：高。*
```

Start a new one with `python scripts/i18n.py scaffold AWF-XXXX`. It copies the English into the right places and sets `source_hash: TODO`. Translate the file, run `python scripts/i18n.py stamp AWF-XXXX`, and fix any problem it prints. `stamp` records which English version you translated.

## What to translate and what to keep

| Part | Rule |
|---|---|
| `name`, `summary`, `deliverable` | Translate. The summary is one sentence of 120 characters or fewer. |
| `shape` | Translate the step words. Keep every `→ ⟲ ( ) |` exactly where the English has them, and keep `🛑 plan / action / review / sample / sign-off / handoff` in English; the page shows them as 审批计划, 审阅草稿 and so on. Write `each X:` as `每个 X：` (or 每份…：, 每批…：). Any step that starts with 每 and has a colon is read as an "each" group, so for a plain step such as "daily: …" or "weekly: …" drop the colon (每天汇总…, 每周列出…). |
| Intro, steps, Output, Failure modes, Recent practice | Translate. Keep the same numbered steps in the same order. The checkpoint labels become 🛑 **计划** / **操作** / **审阅** / **抽检** / **签发** / **接手**. |
| Public runs | Translate the coverage line and the description of each run. Keep the link text (the source's own title), the URL, the date and the quoted figure in "…" exactly as in the English. Translate the label *First-hand: yes; confidence: high.* as *第一手：是；可信度：高。* |
| Sources | Don't copy them. The page shows the English source list, because titles must match what they cite. |
| Citations `[[3]](#sources)`, links, numbers | Keep every one. Write numbers as Arabic numerals (5, 73%, 2026-08), not 五. |
| Tool slugs, code, file names, product names | Keep as written: `claude-code`, `CODEOWNERS`, `Jira`, `pull request`. |

`python scripts/i18n.py check AWF-XXXX` compares the file with the English: shape structure, step count, checkpoints, public runs, citations, links, quotes and numbers. `validate.py` runs the same checks on every workflow.

## Terms

Use these consistently. Common technical words that Chinese engineers write in English stay in English (PR, diff, CI, API, SQL, prompt is 提示词).

| English | 中文 |
|---|---|
| agent | 智能体（产品名里的 Agent 保留） |
| workflow | 工作流 |
| human checkpoint | 人工检查点 |
| plan / action / review / sample / sign-off / handoff | 计划 / 操作 / 审阅 / 抽检 / 签发 / 接手 |
| assist / checkpointed / sampled | 辅助 / 分段 / 抽检 |
| draft (status) | 草稿 |
| reviewer | 审阅人 |
| owner | 负责人 |
| escalate | 升级 / 转交 |
| ticket | 工单 |
| knowledge base | 知识库 |
| run (a public run) | 实例 |
| evidence A / B / C | 第一手记录 / 厂商材料 / 社区经验 |
| Strong / Partial / Weak / None found | 充分 / 部分 / 薄弱 / 暂无 |
| first-hand: yes / vendor / interview / study / anon / no | 是 / 厂商 / 访谈 / 研究 / 匿名 / 否 |
| confidence: high / med / low | 高 / 中 / 低 |
| How it differs | 与相近工作流的区别 |
| Variants | 工具变体 |
| Input / Roles/Tools | 输入 / 角色与工具 |
| Output | 产出 |
| Failure modes → guards | 失败模式 → 防护 |
| Recent practice (2026) | 近期实践（2026） |
| Metric caution | 指标提示 |

Industry terms already in Chinese stay as written (短剧, 网文, 口播稿, 伏笔). Use the field and class names from `i18n/labels.yaml` when you name a category.

## When the English changes

Edit the English first. If you can, update `README.zh-CN.md` in the same pull request and run `stamp`. If you can't, leave it: `validate.py` warns that the translation is behind, the monthly freshness report lists it, and the Chinese page tells readers to check the English.
