---
id: AWF-0054
name: 带护栏的营销活动搭建
summary: "生成邮件旅程、人群规格、UTM 登记和模板 HTML；方案由人工批准，导出到 ESP 前需人工复核。"
deliverable: 可直接用于 ESP 的营销活动
shape: "需求简报 → 命名 + UTM 登记 → 旅程设计 → 人群规格 → 🛑 plan → 文案（当前产品上下文 + URL 白名单）→ 模块化模板 HTML → (搭建 ⟲ QA 清单) → 🛑 action (复核并导出到 ESP) → A/B 测试 → 胜出版本回流到下一份简报"
source_hash: e3254ffc6c39
---

# 带护栏的营销活动搭建

**与相近工作流的区别：** AWF-0019 广告变体矩阵（Ad variant matrix）产出付费广告素材变体。本工作流在 ESP 中搭建自有渠道的旅程，带人群规格、UTM 登记和渲染 QA，之后再手动导出。
**工具变体：** `claude-code-skills` · `claude-codex-stripo-braze`

## 步骤

1. 在搭建任何内容之前，先生成活动名称、登记 slug 和完整的 UTM 参数，让活动从第一天起就可衡量 [[1]](#sources)。
2. 把简报（Notion 中的 PRD，或一个目标）转成旅程或活动设计，以及人群定义 [[1]](#sources)[[2]](#sources)。
3. 🛑 **计划**：由人审阅简报和人群。每一步都产出可以做 diff 和审阅的文件，之后才会碰到发送工具 [[1]](#sources)。
4. 依据当前的产品上下文撰写文案，配合 URL 白名单和产品名称词典。用模块化模板（Stripo）搭建邮件，生成的图片托管在 ESP 中 [[1]](#sources)[[2]](#sources)。
5. 运行 QA 清单：链接和 UTM 与登记表做 diff、渲染效果、人群合理性、护栏。修复并重复，直到通过 [[1]](#sources)。
6. 🛑 **操作**：营销人员在正式上线前，于手动导出到 Braze 时复核、调整并批准最终素材 [[2]](#sources)。随后做 A/B 测试，在一个项目中每两周一次 [[1]](#sources)。

**产出：** ESP 中可直接投产的邮件和旅程，以登记 slug 追踪，便于归因。
**失败模式 → 防护：** 编造 URL 和产品名称 → 第一版在 QA 中出现 10.5% 的渲染错误；先上线白名单和词典护栏 [[1]](#sources)。旧活动重复一年前的说法 → 把当前的产品上下文作为输入拉取进来 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [sara-beh8, lifecycle-campaign-skills](https://github.com/sara-beh8/lifecycle-campaign-skills) (2026-07-08)。用技能流水线重建了一个同时运行 15 个以上活动的项目；仓库使用虚构数据，架构是真实的。"shipped an A/B test every two weeks"。*第一手：是（仓库使用虚构数据，结果无法核验）；可信度：低。*
- [Justin Williames, lifecycle workflow](https://www.linkedin.com/posts/justinwilliames_one-of-the-most-interesting-workflows-ive-activity-7466001243753054209-Bmng) (2026-05-29)。在 Sophiie AI，Claude 搭建旅程、文案、图片和 Stripo 邮件；由人在导出到 Braze 时批准。*第一手：是；可信度：中。*
