---
id: AWF-0141
name: 缺口核查的福利表单填写
summary: "先做缺口分析，再依据机构记录填写福利申请表；个案工作者逐项修正确认后提交。"
deliverable: 已提交的福利申请
shape: "个案工作者打开客户个案 → 智能体检索机构数据库和福利门户 → 对表单做前置缺口分析 → 个案工作者与客户补齐缺失材料 → 智能体填写字段，并标注每项的取数依据 → 🛑 review (个案工作者修正并确认) → 个案工作者提交"
source_hash: 43ad12ad5b70
---

# 缺口核查的福利表单填写

**与相近工作流的区别：** AWF-0081 摘要辅助的个案决定（Summary-aided casework decision）中，决策者借助摘要裁定庇护申请。本工作流中，智能体依据现有记录组装并填写福利申请表，并先做缺口分析。产出是已提交的申请而非决定，检查点是提交前由个案工作者做的字段级审阅。
**工具变体：** `nava-form-filling-assistant`

## 步骤

1. 个案工作者与居民面谈，开始办理福利申请，例如 Medicaid 或 SNAP [[1]](#sources)。
2. 智能体在机构的数据库和福利系统中检索客户已有的数据 [[1]](#sources)[[2]](#sources)。
3. 缺口核查：填写之前，先扫描申请表并列出缺少的内容，让个案工作者和客户可以着手收集病历等材料 [[1]](#sources)。
4. 智能体填写表单字段。每个由 AI 填写的字段都标注数据来源的说明。处理细节收在可折叠面板里，因为工作人员觉得它会在与客户交谈时分散注意力 [[1]](#sources)。
5. 🛑 **审阅**：个案工作者检查带标注的字段，修正错误并补全缺口（“Caseworkers review for accuracy, fill in anything missing, and submit”）[[3]](#sources)。
6. 个案工作者提交申请 [[2]](#sources)[[3]](#sources)。

**产出：** 一份完整的、经个案工作者确认的福利申请，在与客户的面谈中准备好并提交到项目门户。
**失败模式 → 防护：** 从过期记录中取到错误数据 → 逐字段的来源标注加个案工作者修正。智能体界面分散对客户谈话的注意力 → 处理细节默认折叠。个案工作者与客户之间的信任受损 → 第一阶段的发现促成了面向信任与采用度的设计调整。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Route Fifty, Riverside County pilot](https://www.route-fifty.com/artificial-intelligence/2026/03/open-source-ai-assistant-shows-promise-california-caseworkers-service-delivery/412378) (2026-03-25)。在 Riverside County 儿童与家庭委员会面向真实家庭开展的第二阶段试点。"About a dozen staff members"。*第一手：访谈；可信度：中。*
