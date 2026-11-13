---
id: AWF-0055
name: 分发式竞品周报
summary: "汇总销售和竞品动态生成每周竞品简报并分派给负责人；CI 负责人审核，PMM 更新竞争卡片。"
deliverable: 竞品简报
shape: "每周从商机频道 + 竞品新闻频道 + 发布中心拉取最近 7 天内容 → 对照门槛分级（重复出现的异议、已确认的公开动作、竞争卡片缺口）→ 剔除噪音 → 结构化简报，每条标注负责的 PMM 和更新建议 → 🛑 review (CI 负责人) → 🛑 handoff (负责的 PMM 更新竞争卡片)"
source_hash: c9722b4e43fe
---

# 分发式竞品周报

**与相近工作流的区别：** AWF-0030 议题树研究（Issue-tree research）产出一次性的战略答案。本工作流是对内部商机信号的周期性扫描，并分派给竞争卡片（battlecard）的负责人。
**工具变体：** `claude-cowork-skill-slack-notion`

## 步骤

1. 每周从内部 Slack 频道（竞品新闻、商机协作、活跃的商机作战室）和 Notion 产品发布中心拉取内容，限定在最近 7 天 [[1]](#sources)。
2. 对照书面的门槛分级：某个异议出现在 2+ 个商机中、竞争对手有已确认的公开动作，或现有竞争卡片存在缺口。过滤掉一次性的提及 [[1]](#sources)。
3. 起草结构化简报。把每一条标注给负责该产品领域的 PMM，并附上更新什么、在哪里更新的建议 [[1]](#sources)。
4. 🛑 **审阅**：竞争情报（CI）负责人持续参与，审阅发布到 PMM 频道的简报草稿 [[1]](#sources)。
5. 🛑 **接手**：负责的 PMM 作为领域专家，处理该条目并更新竞争卡片 [[1]](#sources)。

**产出：** 每周发布到 PMM 频道的简报，带有标注了负责人的竞争卡片更新项。
**失败模式 → 防护：** 噪音淹没频道 → 明确的分级门槛 [[1]](#sources)。单人成为瓶颈 → 把条目分派给各自负责的 PMM，而不是集中交给一位分析师 [[1]](#sources)。大范围拉取来源时的上下文限制（评论者提出）→ 限制每次运行的来源数量。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Andy McCotter-Bicknell, Apollo competitive intel skill](https://www.linkedin.com/posts/andrewmccotterbicknell_i-used-to-be-apollos-competitive-intel-bottleneck-activity-7447707923620724736-e1t7) (2026-04-08)。每周用 Claude Cowork 扫描 Slack/Notion；简报分派给各自负责的 PMM。"if an objection is showing up in 2+ deals"。*第一手：是；可信度：中。*
