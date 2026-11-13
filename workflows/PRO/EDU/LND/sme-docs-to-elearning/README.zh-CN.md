---
id: AWF-0043
name: 专家资料转电子课程
summary: "把领域专家的资料转为大纲和在线课程；教学设计师与专家审核后才发布。"
deliverable: 电子课程
shape: "收集领域专家（SME）资料（文档、视频、演示、工作辅助卡）→ AI 生成大纲和学习目标 → 🛑 review (教学设计师调整结构) → 起草课节和测验 → 🛑 review (领域专家 + 同行) → 在制作工具中搭建 → 发布"
source_hash: 5be46971a713
---

# 专家资料转电子课程

**与相近工作流的区别：** AWF-0027 逆向设计课程（Backward-design course，COURSE）与它最接近，但从学习成果出发。本工作流从领域专家（SME）的源文档出发，并以 SME 的准确性审阅为关口，面向企业内训模块。需要确认它是否算作变体。
**工具变体：** `leai` · `articulate-rise-ai`

## 步骤

1. 把 SME 的原始材料（文档、视频、演示、转录稿、工作辅助卡）上传到 AI 课程制作工具 [[1]](#sources)[[2]](#sources)。
2. AI 生成结构化的课程大纲、学习目标和关键概念摘要 [[1]](#sources)[[2]](#sources)。
3. 🛑 **审阅**：教学设计师通过提示词，按受众和呈现形式重塑学习目标与结构 [[1]](#sources)。
4. AI 起草课节文案、知识检测和测验题，并调整技术内容的语气 [[1]](#sources)[[2]](#sources)。
5. 🛑 **审阅**：SME 和同行审阅草稿的准确性。仍然需要有人把输出改得更有人味 [[2]](#sources)。
6. 在制作工具中搭建互动和版面，然后发布 [[1]](#sources)[[2]](#sources)。

**产出：** 一个带测验、经过审阅的电子课程模块，发布到公司的学习平台。
**失败模式 → 防护：** AI 文案平淡 → 人工编辑，并配一份 AI 风格指南 [[2]](#sources)。内容与源文档不符 → SME 审阅关口 [[1]](#sources)[[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [LearnExperts, Paycor](https://learnexperts.ai/blog/how-paycor-accelerated-learning-design-by-75-using-ai-powered-course-development/) (2026-08-11)。AI 在 SME 审阅之前充当初稿教学设计师。"reduced early-stage development time by up to 75%"。*第一手：厂商；可信度：中。*
- [Articulate, Cloud communications company](https://www.articulate.com/resources/case-studies/cloud-communications-company/) (2025-11-03)。技术撰稿人把 SME 文档转成 Rise 课程，再经 SME 和同行审阅。"60% faster course development"。*第一手：厂商；可信度：中。*
