---
id: AWF-0009
name: 文献筛选漏斗
summary: "围绕 PICO 问题检索数据库，由两个独立筛选器初筛；人工审批方案、抽检、复核并签核。"
deliverable: 系统综述
shape: "PICO 问题 → 检索式 → 🛑 plan → 每个数据库：检索 → 去重 → 每个记录：两个独立筛选器 → 分歧与纳入项 → 🛑 sample → 每个论文：提取并附引文 + 页码 → 🛑 review → 综合 → 核对引用 → 🛑 sign-off"
source_hash: eef43c9fb49e
---

# 文献筛选漏斗

| 角色 | 工具 |
|---|---|
| 检索策略师 | LLM + PubMed、Scopus、OpenAlex 和 Semantic Scholar API |
| 筛选器 ×2（相互独立） | Elicit、ASReview、Rayyan AI，或自定义分类器 |
| 提取器 | PDF 解析器（如 GROBID）→ LLM 按固定 schema 提取，并引用原文片段 |
| 核查器 | Crossref DOI 解析 + Zotero |

## 步骤

1. 起草布尔检索式和 MeSH 检索式。🛑 **计划**：图书馆员或课题负责人（PI）批准，然后注册研究方案（PROSPERO、OSF）。
2. 检索、去重，并记录各环节数量，用于 PRISMA 流程图。
3. 两个独立的 LLM 筛选器，每个决定都给出理由。**以敏感度而非准确率为调优目标。** 漏掉符合条件的研究会使结果产生偏倚，而已发表的敏感度差异很大：一项荟萃分析的合并值为 0.73，近期预印本中双模型集成约为 96% [[9]](#sources)。🛑 **抽检**：在大规模信任筛选器之前，先用人工筛选过的集合校准（敏感度、Cohen's κ）。所有分歧由人解决。
4. 全文筛选沿用同样的模式，人工介入更紧密。
5. 提取：每个字段都引用原文片段和页码。🛑 **审阅**：人工核对进入荟萃分析的全部数字，比例为 100%。
6. 综合与成稿：偏倚风险表、荟萃分析脚本、叙述性文字。
7. 解析每一条参考文献，并标记缺乏依据的论断。
8. 🛑 **签发**：作者承担责任并披露 AI 的使用。按 ICMJE 的规定，聊天机器人不能作为作者，使用情况必须披露 [[8]](#sources)。

**产出：** PRISMA 流程图、提取数据集、稿件草稿，以及 AI 决策的审计日志。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Fagerberg et al., Socialstyrelsen, medRxiv](https://www.medrxiv.org/content/10.64898/2026.06.02.26354724v1.full) (2026-06)。锁定的 LLM 集成为 24 项指南综述做筛选；两位盲法方法学专家审计预先设定的样本。"screened 74,679 records"；"415 to 34 person-days"；在 600 条被审计的排除项中，"none was confirmed as a final false negative"。*第一手：是；可信度：高。*
- [Gartlehner et al., RTI and partners, medRxiv](https://www.medrxiv.org/node/963738) (2025-03-21)。在 6 项进行中的综述里由 LLM 先做提取、人工核验，并与纯人工提取对比。"9,341 data elements, extracted from 63 studies"；"precision of 98.9%"；"41 minutes per study"。*第一手：是；可信度：高。*
