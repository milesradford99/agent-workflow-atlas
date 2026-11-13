---
id: AWF-0159
name: 样本调优的合同要素提取
summary: "将存量合同提取为带原文链接的 CLM 字段；律师先在样本上调优提示词，再校验并抽检结果。"
deliverable: 可导入 CLM 的合同元数据
shape: "律师定义字段和风险要求 → 盘点并去重存量合同 → 为每个 CLM 字段编写提示词 → (在代表性样本上提取 ⟲ 🛑 review (律师优化提示词)) → 每个合同：条款原文 + 通俗摘要 + 标准编码，并链接到原文 → 🛑 review (律师监督的团队校验) → 🛑 sample (准确率指标 + 一致性检查) → 导入 CLM"
source_hash: 1f0d5c6b7dcf
---

# 样本调优的合同要素提取

**与相近工作流的区别：** AWF-0024 手册式合同审阅是针对一份来件合同做修订以供谈判；AWF-0092 是起草新的低风险文件。本工作流的交付物是覆盖整个存量合同组合的结构化元数据，带样本校准循环和组合层面的质控；交付物和检查点都不同。
**工具变体：** `hebbia` · `elevate-elm` · `ironclad` · `contractpodai-leah`

## 步骤

1. 企业律师确定哪些条款和属性重要（当事方、所在地、期限、续约选项、转让、其他关键条款） [[1]](#sources)。
2. 盘点合同库，剔除草稿、重复件和未签署版本，缩小到范围内的文件（例如约 98,000 个文件缩减到 60,000） [[2]](#sources)。
3. 配置与具体 CLM 字段对应的 AI 提示词，输出符合 CLM 平台导入格式的结果 [[1]](#sources)。
4. 🛑 **审阅**：先在有代表性的合同样本上测试，并在规模化之前优化提示词和输出 [[1]](#sources)；即「基于样本的手册验证」和领域专家校准 [[2]](#sources)。
5. 对每份合同，AI 提取条款原文，写出通俗易懂的摘要，并套用标准化编码 [[1]](#sources)。
6. 🛑 **审阅**：在律师监督下，审阅人从每个数据点点击跳转到原文来校验；律师理顺合同族中的主从关系 [[1]](#sources)[[2]](#sources)。
7. 🛑 **抽检**：迁移前依据质量框架，使用明确的准确率指标、反馈循环和自动一致性检查 [[2]](#sources)。

**产出：** 经校验、带原文链接、已导入客户 CLM 系统的合同元数据。
**失败模式 → 防护：** 提示词漏掉字段细微差别 → 规模化之前先做样本试点。主从层级出错（修订协议与主服务协议） → 由律师主导的合同族核对。提取错误悄无声息 → 提供原文链接和准确率指标。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Troutman Pepper Locke, Accelerating CLM Implementation](https://www.troutman.com/insights/accelerating-clm-implementation/) (2026-04-20)。律所自己的实例：1,000 多份燃气公用事业存量合同，样本测试提示词，律师监督下校验。"roughly half of what a traditional manual review would have taken"。*第一手：是；可信度：高。*
- [Elevate, CLM-ready contract repository](https://elevate.law/case-studies/how-ai-enabled-review-delivered-a-clm-ready-contract-repository/) (2026-05-27)。法律服务提供商自己的项目：分流 98K 个文件，提取 60K 个，迁移到 Ironclad。">99% accuracy across extracted metadata"。*第一手：厂商；可信度：中。*
