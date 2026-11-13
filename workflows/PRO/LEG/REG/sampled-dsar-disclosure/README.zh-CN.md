---
id: AWF-0160
name: 抽检式数据主体访问披露
summary: "为数据主体访问请求排序文档并遮蔽第三方信息；律师确定范围、抽检排除项并质检遮蔽。"
deliverable: DSAR 披露包
shape: "收到 DSAR（法定期限） → 🛑 plan (与请求人确定保管人、日期、关键词的范围) → 收集 + 去重 + 邮件串合并 → 按请求和司法辖区定制提示词 → AI 对文档按其含数据主体个人数据的程度排序并给出理由 → 🛑 sample (抽样质检“不相关”文档) → 自动检测并遮蔽第三方个人身份信息 → 🛑 review (律师助理/律师质检遮蔽、豁免、特权) → 披露 + 审计记录"
source_hash: c0aeaa1083dd
---

# 抽检式数据主体访问披露

**与相近工作流的区别：** AWF-0035 经验证的 GenAI 初审是在诉讼中判断文档是否相关，并由人签发召回率；AWF-0036 是构建义务登记表。本工作流的交付物是向个人作出的法定披露，带第三方遮蔽质检和一个月的期限；检查点（与请求人确定范围、遮蔽质检）和交付物都不同。
**工具变体：** `relativity-air-for-review` · `cds-vision-ai` · `relativity-redact` · `aiimi`

## 步骤

1. 🛑 **计划**：确定请求范围（保管人、日期范围、针对性关键词），最好与请求人讨论；记录各项参数以备举证 [[1]](#sources)。
2. 从 M365/Google/Slack 收集，去重并合并邮件串以减少数量（例如某案最后剩约 1,500 份文档；另一案从 75,000 份降到 11,671 份） [[1]](#sources)[[2]](#sources)。
3. 用针对 DSAR 的提示词运行 GenAI 审阅，提示词按请求范围和司法辖区定制，对文档排序并给出理由和引用 [[1]](#sources)[[3]](#sources)。
4. 🛑 **抽检**：在规模化之前，对一个有针对性的“不相关”文档样本做质检，以验证 AI 的判断；某个实例用了「两个小型验证样本」 [[1]](#sources)[[2]](#sources)。
5. 自动检测并遮蔽第三方的个人数据（姓名、邮箱、电话号码、地址） [[2]](#sources)。
6. 🛑 **审阅**：律师助理或客户员工对遮蔽后的文档集做质检，并追加保密遮蔽；可能涉及特权的内容单独交给经验丰富的律师质检 [[2]](#sources)[[3]](#sources)。
7. 在一个月的法定期限内完成披露，并保留审计记录 [[1]](#sources)。

**产出：** 经遮蔽的披露文档集和给数据主体的答复，并附范围、质检和遮蔽的审计记录。
**失败模式 → 防护：** 请求过宽（姓名首字母匹配常见词） → 收集之前先协商范围。AI 漏掉相关文档 → 对“不相关”文档做漏检式抽样。披露了第三方数据或特权建议 → 自动个人信息检测加人工遮蔽和特权质检。

## 公开实例

覆盖度（截至 2026-11-13）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点位置不同。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Gravity Stack, From Inbox to Disclosure](https://relativity.com/blog/from-inbox-to-disclosure-how-air-reshapes-dsar-compliance/) (2025-11-24)。前员工的 DSAR：确定范围，去重后约 1,500 份文档，抽样质检“不相关”文档，完成披露。"The entire process, from receipt to production, was completed within 48 hours"。*第一手：是；可信度：中。*
- [CDS, GenAI DSAR responses](https://cdslegal.com/insights/how-generative-ai-is-driving-faster-more-accurate-dsar-responses/) (2026-01-07)。两个服务商的实例：过滤、GenAI 审阅、自动遮蔽、律师助理/客户质检。"saved more than £73,000 compared to their traditional method"。*第一手：是；可信度：中。*
- [Relativity, Baker McKenzie aiR](https://www.relativity.com/resources/customers/baker-mckenzie-relativity-air/) (n.d.)。一周内完成两个 DSAR，使用定制提示词；律师校验输出。"One DSAR was completed in just 48 hours"。*第一手：厂商；可信度：中。*
