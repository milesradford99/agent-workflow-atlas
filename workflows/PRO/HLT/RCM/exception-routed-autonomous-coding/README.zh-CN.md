---
id: AWF-0090
name: 按例外分流的自动编码
summary: "为每份病历自动分配 ICD/CPT 编码并附理由；低置信或冲突病历转编码员，其余定期抽审。"
deliverable: 已编码的理赔单
shape: "记录编码理念与机构指南 → 🛑 plan (配置并验证引擎) → 每个病历：引擎分配 ICD/CPT/E&M 编码，并为每个编码附理由 → 覆盖检查 → 已覆盖：编码送计费 | 被剔除 (理解缺口、文档冲突、编码置信度低、文档缺失)：🛑 handoff (编码员) → 🛑 sample (定期编码审计) → 审计反馈给引擎"
source_hash: ad0f1aeeffd4
---

# 按例外分流的自动编码

**与相近工作流的区别：** AWF-0032 依据标准把关的预授权（Criteria-gated prior auth）是最接近的一个，它是辅助级的：工作人员审阅每封信函并提交每项申请。这里，已覆盖病历的编码不经人工审阅直接进入计费，人只处理例外情况和审计抽样。
**工具变体：** `nym-autonomous-coding`

## 步骤

1. 记录机构的编码理念和指南，并用它们配置引擎 [[1]](#sources)。
2. 🛑 **计划**：在依赖引擎的结果之前先验证。培训人工编码员验证其输出并给出反馈 [[1]](#sources)。
3. EHR 把病历发给引擎。引擎在数秒内完成编码，并为每个编码给出理由 [[1]](#sources)。
4. 已覆盖病历的编码直接送往计费，不逐份审阅 [[1]](#sources)。
5. 🛑 **接手**：被剔除的病历交给人工编码员。剔除的原因有四种：引擎理解缺口、文档冲突、某个编码置信度低，以及文档缺失（例如缺少急诊记录或医师签名）[[1]](#sources)。
6. 🛑 **抽检**：对自动编码的病历定期做审计和质量检查。审计发现会补充到引擎的知识库中 [[1]](#sources)。

**产出：** 送往计费的已编码理赔单，外加一个供编码员处理的例外病历队列。
**失败模式 → 防护：** 有缺口或冲突的病历被错误编码 → 每一类都作为被剔除的病历分流出去。覆盖范围有限（主要是门诊专科）→ 为被剔除的那部分保留编码员人手。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Geretz/Nym Health, Autonomous Medical Coding (OHIMA)](https://ohima.memberclicks.net/assets/docs/blog/RevCycle_AutonomousMedicalCoding_KacieGeretz.pdf) (n.d.)。厂商演示文稿，介绍被剔除病历转给编码员的分流以及审计闭环。"~ 5 - 10% of charts cannot be coded due to engine understanding gaps"。*第一手：厂商；可信度：中。*
