---
id: AWF-0178
name: 带护栏的一对一决策
summary: "智能体在营销人员设定的护栏和对照组内，为每位客户选择消息、渠道和时机；营销人员审阅洞察。"
deliverable: 个性化消息流
shape: "盘点消息素材 → 设定目标 + 目标权重 + 护栏（发给谁、多频繁、哪些创意、哪几天）+ 对照组 → 🛑 plan → 每个客户：智能体选择消息、渠道、时机，或不发送 → 发送 → 从结果中学习 → 与对照组比较 → 🛑 review (营销人员阅读洞察，更新内容)"
source_hash: b00a2edd75ef
---

# 带护栏的一对一决策

**与相近工作流的区别：** 最接近的是 AWF-0054 带护栏的活动搭建（Guardrailed campaign build）：那里每个活动在导出前都要搭建、QA 并获批。这里不审批任何单次发送；人们只一次性批准护栏，并审阅汇总结果。自主程度是抽检，而不是分段。
**工具变体：** `hightouch-ai-decisioning` · `moengage-campaign-decisioning` · `monocle`

## 步骤

1. 盘点智能体可能用到的所有现有和新增消息素材 [[1]](#sources)。
2. 定义护栏：谁可以收到哪些消息、多频繁、哪些创意、哪几天；设定带权重的短期和长期目标（例如点击与订单及订单金额）[[1]](#sources)[[2]](#sources)。设置对照组 [[2]](#sources)[[3]](#sources)。
3. 🛑 **计划**：营销团队在上线前批准目标、权重和护栏 [[1]](#sources)[[2]](#sources)。
4. 智能体为每位客户选择消息、渠道、时机和频率，包括是否发送，并从每次响应中学习（强化学习 / 多臂老虎机）[[2]](#sources)[[4]](#sources)。
5. 相对对照组衡量提升效果 [[2]](#sources)[[3]](#sources)。
6. 🛑 **审阅**：营销人员阅读智能体给出的洞察（哪些消息、地区、主题表现好），并新增、更新或下线内容 [[1]](#sources)[[2]](#sources)。

**产出：** 持续运行的个性化消息流，附相对对照组的实测提升，以及供团队参考的内容洞察。
**失败模式 → 防护：** 智能体优化了错误的结果 → 使用包含长期价值的加权目标 [1]。过度发送或不符合品牌的优惠 → 频率上限、成本上限，以及“Exclude VIPs from discounts”这类白话规则 [3][4]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名的、与厂商相关的或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Hightouch, Fundrise customer story](https://hightouch.com/customers/fundrise) (2025-07-16)。决策智能体在经审计的素材和护栏下进行的沉睡用户召回。"AI Decisioning delivered a 4x higher amount invested on roughly the same number of orders placed"。*第一手：厂商；可信度：中。*
