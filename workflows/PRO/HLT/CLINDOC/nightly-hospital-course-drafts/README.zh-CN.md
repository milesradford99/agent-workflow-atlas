---
id: AWF-0157
name: 夜间住院经过草稿
summary: "每晚为住院患者起草带来源引用的住院经过摘要；主治医师决定采用、修改或弃用。"
deliverable: 住院经过摘要
shape: "夜间：通过 FHIR 拉取入院记录 (H&P、病程记录、多学科记录) → 3 阶段智能体式摘要 + 核验，附行内来源引用 → 每位患者一封加密邮件草稿，上午 9 点前送达 → 🛑 review (主治医师采用、修改或弃用) → 粘贴进 EHR 中的出院小结 → 🛑 sample (医师反馈危害与错误)"
source_hash: a00eaf0f2092
---

# 夜间住院经过草稿

**与相近工作流的区别：** AWF-0088 预先起草的影像报告（Pre-drafted radiograph reports）是在听写模板内起草单次检查的报告；AWF-0026 医患对话环境记录员（Ambient scribe）是根据录音起草就诊记录。本工作流的产出是整个住院期间的住院经过，由多位作者的记录综合而成，每晚批量生成，供医师选择性使用，且每句话都有来源引用。产出和输入都不同，互换测试不通过。
**工具变体：** `gemini-2-5-pro` · `epic-fhir` · `gpt-4-1-ehr-template`

## 步骤

1. 每晚，流水线通过 FHIR 从 EHR 中取回该次住院的临床文档，包括医师、药学、护理、治疗、营养、个案管理和灵性关怀的记录 [[1]](#sources)。
2. 一个 3 阶段的智能体式工作流（Gemini 2.5 Pro）迭代地构建并核验摘要，而不是单次提示，每个阶段都保持以原始记录为依据 [[1]](#sources)。
3. 输出格式与住院医师共同设计：患者一句话概述、叙述式住院经过、按问题组织的摘要，每条陈述都带指向来源记录的行内引用 [[1]](#sources)。
4. 上午 9:00 前，每位主治医师会收到每位患者一封的加密邮件，草稿为交互式 HTML 文件，附一个复制按钮，会去掉引用以便粘贴进 Epic [[1]](#sources)。
5. 🛑 **审阅**：医师可以 'free to use, edit, or discard summaries at their discretion'；出院小结由医师签署 [[1]](#sources)[[2]](#sources)。
6. 🛑 **抽检**：对一部分摘要，通过反馈表对潜在危害程度（AHRQ Common Format Harm Scale）和错误类型（遗漏、不准确、幻觉、引用错误）打分 [[1]](#sources)[[2]](#sources)。

**产出：** 出院小结中的住院经过部分，由医师在 EHR 中修改并签署。
**失败模式 → 防护：** 遗漏（占已评分摘要的 25%）和不准确（20%）→ 使用前由医师对照所引来源审阅；长时间住院超出上下文长度 → 分阶段拆解；采用了却没有节省时间 → 跟踪 EHR 时间日志和职业倦怠，而不只看使用率。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Grolleau et al., Stanford, JAMA Netw Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2848785) (2026-05-08)。为期 10 周的前瞻性试点，384 例出院，医师可选择是否使用草稿；其中 100 份评定了危害。"Physicians used artificial intelligence (AI) content in 219 cases (57.0%)"；"Physicians rated 88 unedited summaries (88.0%) as having no harm potential"。*第一手：是；可信度：高。*
- [Suarez et al., ACI](https://doi.org/10.1055/a-2962-8004) (2026-08-01)。GPT-4.1 在强制使用的出院小结模板内起草住院经过；8,298 名成人；测量了编辑时间。"the AI tool was associated with a 32% increase in edit time"。*第一手：是；可信度：高。*
