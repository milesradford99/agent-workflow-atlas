---
id: AWF-0147
name: 分析师核验的租约摘要
summary: "将租约及修订条款提取为带出处的数据字段；分析师对照原文核对并裁定需判断的字段。"
deliverable: 租约摘要
shape: "组合 ZIP → 按租户排序并分组 → 为修订条款排序 → 将租约与修订条款一并提取摘要 (每个值都标注原文出处) → 🛑 review (分析师对照原文核对，裁定需判断的字段) → 载入组合管理系统 → 修订：只对变化的字段重新提取"
source_hash: 7e4b839931df
---

# 分析师核验的租约摘要

**与相近工作流的区别：** AWF-0024 按手册审阅合同（Playbook contract review）是为谈判标注合同。AWF-0037 在数据室中标出风险。本工作流的产出是带修订追踪的结构化记录系统数据集。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `LEASEADMIN`（TAXONOMY.md 规则 2）之前，先归在这里。
**工具变体：** `cremodels-mercury` · `dealsumm` · `kolena` · `legora`

## 步骤

1. 把整个组合作为一个 ZIP 载入；系统对文件排序，并按租户分组 [[1]](#sources)。
2. 按顺序梳理修订历史，让后来的修订取代先前的条款 [[1]](#sources)。
3. 提取带出处的字段；JLL 的平台涵盖 'more than 2,500 data points per lease' [[2]](#sources)。
4. 🛑 **审阅**：分析师对照原文审阅，纠正错误，并裁定回收款和共同租户条款（co-tenancy）这类需要判断的问题 [[1]](#sources)；在 JLL，数据定稿前由人工验证 [[2]](#sources)。
5. 修订条款到达时，只更新有变化的数据点 [[2]](#sources)。

**产出：** 存入组合管理系统的租约摘要，用于承销和租约管理。
**失败模式 → 防护：** 准确率为 80% 时租约数据不可用（'no better than 0%'）→ 分析师签发每一个字段 [[1]](#sources)。

**近期实践（2026）：**
- 为修订条款排序：把租约和所有修订合并为当前有效条款，并把租金表当作表格来读，而不是压平成文本（Kolena，2026-02-26）。[[3]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [CREModels case study](https://www.cremodels.com/ai-lease-abstraction-case-study) (2026-06-24)。为一家购物中心业主处理约 200 家零售租户；分析师签发每个字段。"about 200 retail tenants"（项目范围）。*第一手：是；可信度：高。*
- [Databricks, JLL](https://www.databricks.com/customers/jll/dealsumm) (n.d.)。保留人工审阅；吞吐量翻倍。"Review time per lease dropped from 130 minutes to 85 minutes"。*第一手：厂商；可信度：中。*
- [Kolena, How Real Capital Solutions Cut Lease Review Time by 85%](https://www.kolena.com/blog/how-real-capital-solutions-cut-lease-review-time-by-85/) (2026-02-26)。一家商业地产私募基金管理人（管理规模 $2.8B）提取租约和修订的摘要，输出到 SharePoint/Teams 文件夹供内部审阅。"Internal review time dropped from an average of two hours to roughly 17 minutes"。*第一手：厂商；可信度：中。*
- [Axiom, 2,000 Leases Digitized with Axiom Tech+Talent for Real Estate Manager](https://www.axiomlaw.com/resources/case-studies/real-estate-contracts-digitized-ai-lawyers) (2026-06-03)。93 处物业的组合；Legora 接手审阅 1,400 份租约；由一名领域专家验证数据准确性。"After Legora, the 5-lawyer team turned into one subject matter expert to verify data accuracy"。*第一手：厂商；可信度：低。*
