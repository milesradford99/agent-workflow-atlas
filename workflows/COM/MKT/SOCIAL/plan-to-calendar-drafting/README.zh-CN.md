---
id: AWF-0053
name: 计划转日历的社媒排期
summary: "按渠道起草社媒帖子并排入发布日历；计划、每条内容审核及发布均需人工批准。"
deliverable: 已排期的帖子日历
shape: "素材盘点 + 规划文档（选题 + 日期）→ 🛑 plan → 每个帖子：按渠道起草 → 以草稿形式放入排期工具 → 🛑 review (核实事实、把关口吻) → 🛑 action (批准发布) → 已排期 → 数据周报"
source_hash: 4395377f882a
---

# 计划转日历的社媒排期

**与相近工作流的区别：** AWF-0018 聚类—简报—起草（Cluster-brief-draft）产出长篇 SEO 文章。AWF-0019 广告变体矩阵（Ad variant matrix）产出用于测试的付费广告变体。本工作流则填充自然流量的、按日期排布的社媒日历，每条帖子的发布都需要批准。
**工具变体：** `claude-oktopost` · `multi-agent-linkedin-x` · `openclaw-deepseek-wechat`

## 步骤

1. 维护一份现有素材的清单，按行业、使用场景和买家阶段对应，并找出覆盖缺口 [[2]](#sources)。把原有帖子改写成每条多个不同的切入角度 [[1]](#sources)。
2. 🛑 **计划**：由人制定规划文档（帖子选题和发布日期）并批准日历计划；智能体不决定发布什么 [[1]](#sources)[[2]](#sources)。
3. 为每个渠道起草帖子，并以草稿形式放到排期工具（Oktopost，或微信的草稿箱）中对应的日期上 [[1]](#sources)[[3]](#sources)。
4. 🛑 **审阅**：由人审阅、核实事实并修改每条帖子，使其读起来像真人写的 [[1]](#sources)。在人工审阅之前，增加一道自动合规检查，筛查夸张标题和敏感词 [[3]](#sources)。
5. 🛑 **操作**：由人批准并发布或排期。在中国的平台上，智能体写入草稿，由人定时发送（人工定时发送）[[1]](#sources)[[3]](#sources)。
6. 把每日数据（阅读、点赞、评论关键词）汇总成报告，用来指导下一批选题 [[3]](#sources)。

**产出：** 一个月份的已批准帖子，排入社媒排期工具，外加一份为下一轮计划提供输入的数据周报。
**失败模式 → 防护：** 文案千篇一律或带 AI 腔 → 必须由人修改 [[1]](#sources)。全自动发布会触发平台风控，导致限流或封号（小红书）→ 半自动发布，加人工审阅 [[3]](#sources)。事实有误 → 每条帖子都核实事实 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Oktopost, I gave an AI the keys to Oktopost](https://www.oktopost.com/blog/i-gave-an-ai-the-keys-to-oktopost/) (2026-07-28)。内容经理让 Claude 起草 LinkedIn 日历并排入 Oktopost；每条帖子都经人工批准。"A task that would usually take me a couple of days was finished in around an hour."。*第一手：厂商（Oktopost 员工使用 Oktopost）；可信度：高。*
- [Alberto Farronato, Content Marketing Agent Loop](https://www.linkedin.com/posts/albertofarronato_agenticai-gtmengineering-marketingops-activity-7475624768231133184-zWjj) (2026-06-24)。由 Librarian/Scout/Strategist/Drafter/Scheduler 几个智能体组成；每个阶段都有人签字确认。"Mapping 200+ assets across 15 campaigns"。*第一手：是；可信度：中。*
- [见实, 用OpenClaw跑通内容自动化](https://www.woshipm.com/ai/6361404.html) (2026-03-23)。选题→创作→审核Agent→半自动发布→复盘；公众号草稿，人工定时发送。"以前这需要一个5人团队（编辑、设计、运营、数据分析）"。*第一手：访谈；可信度：中。*
