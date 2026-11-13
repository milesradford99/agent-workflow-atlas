---
id: AWF-0018
name: 聚类简报成文内容
summary: "把关键词聚类成 SEO 文章简报，结合专家意见起草；选题计划和每篇文章发布前均由人工审核。"
deliverable: 网页文章
shape: "种子主题 → SEO API → 关键词聚类 → 🛑 plan → 每个文章：搜索结果前 10 名 → 简报 → 产品文档 + 专家意见 → 起草 → 事实、文风、链接检查 → 🛑 review → CMS → 第 30/90 天检查排名 → 更新"
source_hash: ee020ab89e25
---

# 聚类简报成文内容

**约束：** Google 2024 年 3 月的“规模化内容滥用”（"scaled content abuse"）政策针对的是主要为了排名而批量生成、没有增加价值的页面，无论是否自动化 [[19]](#sources)。这就是为什么专家意见环节和编辑审阅是这个物种的组成部分，而不是可选项。

## 步骤

1. 拉取种子主题和搜索数据。一个实例通过 MCP 服务器（`mcp-server-gsc`）从 Claude Code 调用 Google Search Console API，并把原始 JSON 存到磁盘 [[20]](#sources)。另一个实例把目标关键词喂给 SEO 工具（Semrush ContentShake、Also Asked），并让 AI 按搜索意图给大型关键词清单分组 [[21]](#sources)。
2. 建立关键词聚类和页面计划。由脚本计算变化量并把查询映射到页面，另有一个智能体读取未匹配的查询，标出需要新建页面的空缺 [[20]](#sources)。
3. 🛑 **计划**：由编辑批准撰写或修改哪些聚类和页面。按 Google 的规模化内容政策，只有在排名之外还能增加价值的内容才会推进 [[19]](#sources)。
4. 对每篇文章，研究排名靠前的结果并写简报：目标关键词、用户提出的问题、竞品的切入角度和字数建议。详细的简报产出的草稿，比只给一个主题提示词好得多 [[21]](#sources)。
5. 加入产品文档和专家意见：独家案例、客户成果、原创数据 [[21]](#sources)。在通用 LLM（Claude 或 ChatGPT）里以简报为上下文起草，把结果当作原材料 [[21]](#sources)。
6. 检查事实、文风和链接。对照一手来源核实每个论断，去掉套路化的 AI 措辞，对照排名靠前的页面给术语覆盖度打分（Surfer、Clearscope）但不堆砌关键词，让格式匹配搜索意图，并加入 AI 建议的内链 [[21]](#sources)。
7. 🛑 **审阅**：编辑在发布前审阅草稿。在 FutureSearch 的循环里，建议的修改以 PR 加报告的形式送达，一位非技术成员花约 20 分钟挑选采用哪些。没有任何内容自动生效 [[20]](#sources)。
8. 带着生成的元数据发布到 CMS [[21]](#sources)。
9. 在第 30 天和第 90 天检查排名并更新。把每次改动记入每个页面的 `experiment_history`，附前后数据和结果（改善、持平或倒退），并让下一轮运行在提出新改动前先读取这份历史 [[20]](#sources)。

**产出：** CMS 中已发布、经编辑批准的文章，外加驱动下一轮更新的、按页面记录的实验日志。
**失败模式 → 防护：** 编造事实，例如不存在的以太坊升级，或把功能归到错误的链上 → 强制对照一手来源或专家做事实核查 [[21]](#sources)。页面先上榜，随后因互动数据暴露意图不匹配而下滑 → 依据搜索意图选择格式 [[21]](#sources)。与竞品混为一谈的通用页面，或主要为排名而批量生成的页面 → 专家意见和原创数据 [[19]](#sources) [[21]](#sources)。工具的激进建议导致关键词堆砌 → 自然覆盖，并做可读性检查 [[21]](#sources)。全站标题千篇一律 → 轮换标题格式 [[20]](#sources)。智能体未经审核就改线上页面 → 改动走 PR，由人来应用 [[20]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Daniel Hnyk, FutureSearch](https://futuresearch.ai/blog/self-optimizing-seo-pipeline/) (2026-03-18)。Search Console → 按页面的分析智能体 → PR；由人挑选做哪些改动。"69 changes proposed"；"The human spends 20 minutes deciding"。*第一手：是；可信度：高。*
- [Victoria Olsina, *AI for SEO Content: 6-Month Test*](https://victoriaolsina.com/blog/ai-seo-content/) (2025-12-26)。简报 → AI 草稿 → 创始人补充意见 → 人工编辑和事实核查。"from 2-3 to 8-10 long-form articles monthly"。*第一手：是（未点名网站）；可信度：中。*
- [The SEO Agent Team](https://www.theseoagent.ai/blog/ai-seo-case-study) (updated 2026-09-19)。关键词队列 → 8 个聚类 → 草稿 → 检查 → 发布，没有说明人工关卡。"61 new pages in roughly fifteen weeks"。*第一手：厂商（自家网站）；可信度：中。*
