---
id: AWF-0058
name: 带条文引用的预审检查
summary: "对上传的图纸按预设规范逐项检查并引用条文；市政审查员对每项结果判定通过或需整改。"
deliverable: 规范符合性检查结果
shape: "上传图纸集 → 提取为结构化数据 → 每个预设检查：通过/不通过 + 规范条文引用 → 申请人整改 → 提交 → 审查员查看 AI 判定 → 🛑 review (逐项批准 / 需整改) → 结构化反馈 → 重新校准检查项"
source_hash: 5afcb11385b3
---

# 带条文引用的预审检查

**与相近工作流的区别：** 暂无相近者。AWF-0024 按手册审阅合同（playbook contract review）是对照手册检查文档，但其交付物是带修订标记的合同，而不是许可审查结果。
**工具变体：** `civcheck` · `archistar` · `codecomply-ai` · `blitz-ai`

## 步骤

1. 只配置那些能转化为明确逻辑的检查项。西雅图用了 34 项完整性检查和 67 项合规性检查，范围限定在《西雅图住宅规范》下较简单的住宅类“中间住宅”（middle housing）[[1]](#sources)。
2. 申请人上传图纸集。工具把图纸内容提取为结构化数据，运行所有预设检查，返回与规范要求挂钩的通过/不通过结论 [[1]](#sources)[[2]](#sources)。
3. 申请人在提交之前先整改被标记的问题。申请仍然要走市政府的正常审查流程 [[2]](#sources)。
4. 🛑 **审阅**：在图纸审查阶段，市政审查员先做正常审查，然后看到工具对每项检查给出的通过/不通过判定。他们点击“批准”或“需整改”，并在工具出错时提交结构化反馈 [[1]](#sources)。
5. 供应商根据审查员的反馈重新校准检查项。试点期间准确率不断提高 [[1]](#sources)[[2]](#sources)。

**产出：** 给申请人的逐项检查结果报告，附规范条文引用，之后是正常的市政许可审查。审查员保有最终决定权。
**失败模式 → 防护：** 漏掉整改项，即工具放行了审查员退回的条目 → 对每项检查设置审查员关卡，并跟踪误放行率。规范无法转化为逻辑而出现覆盖缺口，申请人把它当作“又一道门槛” → 先把范围限制在简单的建筑类型和完整性检查 [[1]](#sources)[[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [City of Seattle, CivCheck AI Pre-Screening Pilot Report](https://seattle.gov/documents/Departments/Performance/Publications/2026CivCheckEvaluationReport.pdf) (2026)。审查员对 57 份住宅申请中的 1,262 项检查的 AI 通过/不通过判定进行了评判。"Overall Accuracy: 91.7%"。*第一手：是；可信度：高。*
- [Seattle Innovation & Performance, CivCheck pilot insights](https://innovation-hub.seattle.gov/2026/06/17/ai-construction-permitting-seattle-civcheck-study/) (2026-06-17)。市政府对试点的总结：准确率，以及覆盖范围与准确率同样重要。"application completeness checks were 87% accurate and design compliance checks were 92% accurate"。*第一手：是；可信度：高。*
