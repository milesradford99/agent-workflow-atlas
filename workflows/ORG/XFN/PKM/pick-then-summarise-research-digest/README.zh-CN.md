---
id: AWF-0146
name: 先选后读的文献摘要简报
summary: "每日检索 arXiv 和 Scholar 生成简报，再对读者勾选的论文做摘要；由读者核对摘要。"
deliverable: 每日文献简报
shape: "日常定时任务：按主题配置检索 arXiv (每周加 Google Scholar)，跳过已展示的论文 → 简报链接到每日笔记 → 🛑 plan (读者保存选中的 PDF) → 夜间：每个已保存的 PDF：智能体总结方法、效应量、证据 → 摘要出现在次日简报 → 🛑 review (读者在引用或据此行动前核对)"
source_hash: 9c8063ea9ef0
---

# 先选后读的文献摘要简报

**与相近工作流的区别：** AWF-0087 以 diff 审阅的笔记库维护（Diff-reviewed vault upkeep）中，智能体按口述指令编辑已有的笔记库，检查点是对修改做 git diff 审阅。本工作流中，智能体按计划引入新的外部文献。产出是简报加摘要，检查点是读者挑选要处理哪些论文，然后阅读摘要。
**工具变体：** `claude-code` · `obsidian` · `hermes-agent` · `netnewswire` · `github-pages`

## 步骤

1. 维护一份研究主题配置，以及一份已展示论文的记录 [[1]](#sources)。
2. 每天早上由检索脚本查询 arXiv，周日再加上 Google Scholar。新结果进入一份简报，从带日期的 /today 笔记链接过去 [[1]](#sources)。
3. 🛑 **计划**：读者浏览简报，只把有希望的 PDF 保存到研究文件夹，这一步就是防止信息过载的过滤器 [[1]](#sources)。
4. 每晚由脚本找出新保存的 PDF，让 Claude Code 智能体总结方法、效应量和其他证据，而不只是摘要 [[1]](#sources)。
5. 这些摘要出现在次日的简报中 [[1]](#sources)。
6. 🛑 **审阅**：读者在使用之前先阅读并核对每份摘要。Torres 曾借此发现一处方法上的缺陷，并公开撰文论述 [[1]](#sources)。
7. 变体（Research Radar）：每天 09:15 的定时任务按研究画像过滤 20 多个 RSS 源，为每篇论文标注等级（细读、略读、知晓）并附 'why it matters' 说明，10:00 的质检任务检查字段和 DOI。随后页面提交到 GitHub Pages，由作者决定读什么。智能体从不往 Zotero 添加内容，也不删除任何东西 [[2]](#sources)。

**产出：** 每日的新论文简报页面或笔记，加上针对读者所选论文的、聚焦证据的摘要。
**失败模式 → 防护：** 信息过载 → 只有读者保存的 PDF 才会得到深度摘要。摘要误述了方法 → 引用前由读者审阅。格式错误的输出破坏页面 → 单独的质检定时任务修复小问题，拦截严重问题 [[2]](#sources)。重复 → 在配置中记录已见过的论文。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [How I AI, Teresa Torres](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management) (2026-01-19)。每日 arXiv 检索、读者保存 PDF、每晚证据摘要；一份摘要暴露出一处缺陷，她为此撰文。除运行计划外未给出数据（每日 arXiv、周日 Google Scholar、每晚摘要）。*第一手：访谈；可信度：中。*
- [CHEN Yiru, Research Radar](https://chenyiru3.github.io/blog/2026/how-research-radar-works/) (2026-05-15)。个人的每日流水线，带分级推荐、质检定时任务和发布页面；由作者决定读什么。"help me choose the 13 to 15 papers most worth reading that day"。*第一手：是；可信度：中。*
