---
id: AWF-0162
name: 代位追偿线索分诊
summary: "为每宗理赔评估代位追偿可能并给出理由；追偿专员逐条接受或驳回后跟进追偿。"
deliverable: 代位追偿转介单
shape: "每个未结/已结理赔：读取结构化数据 + 理赔员备注 → 套用各州过失与 PIP 法律、召回及外部数据 → 估算责任 + 可追偿金额 → 给线索打分并说明理由 → 🛑 review (追偿专员接受或驳回线索) → 🛑 action (经办人推进索赔/追偿)"
source_hash: d3a0dc5b4d90
---

# 代位追偿线索分诊

**与相近工作流的区别：** AWF-0094、AWF-0095 和 AWF-0096 是决定或沟通保险公司向自家客户赔付多少。本工作流是赔付之后向第三方追回款项；智能体无人值守地筛查全部理赔，人只看线索。交付物和自主程度都不同。
**工具变体：** `shift-subrogation` · `megaputer-subrocheck`

## 步骤

1. 扫描每份理赔档案，包括结构化字段和理赔员的自由文本备注（用 GenAI 归纳），弄清发生了什么、涉及哪些人、其他方是否可能有过错 [[1]](#sources)[[2]](#sources)。
2. 套用外部数据：各州比较过失和 PIP/MedPay 规则、诉讼时效、产品召回清单、车辆登记数据（例如确认某辆车是网约车/出租车辆，以适用纽约 PIP） [[1]](#sources)[[3]](#sources)。
3. 估算责任和潜在追偿金额；生成带评分的线索，并附上驱动评分的理由和细节摘要 [[1]](#sources)。
4. 🛑 **审阅**：追偿人员审阅线索，而不是逐宗理赔：「我们不再需要审阅每一宗理赔」 [[2]](#sources)。
5. 🛑 **操作**：理赔经办人推进追偿；经办人仍会手动转介理赔，由工具兜住遗漏 [[2]](#sources)。

**产出：** 带责任估算和支撑理由的、按优先级排序的代位追偿转介单，由追偿团队跟进。
**失败模式 → 防护：** 经办人忘记转介导致漏追 → 后台扫描全部理赔，包括已结案的。诉讼时效已过 → 在线索中套用各州规则。理赔员不信任 → 定位为辅助并培训团队 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Shift Technology, Top US P&C insurer streamlines subrogation](https://www.shift-technology.com/resources/case-studies/top-25-us-auto-and-property-insurer-streamlines-subrogation) (2026-07-09)。先是车险后是财产险；GenAI 读取备注，在经办人转介之前给出带评分的线索。"recurring average recovery of over $1 million per month"。*第一手：厂商；可信度：中。*
- [Shift Technology, Central Insurance](https://www.shift-technology.com/resources/reports-and-insights/subrogation-central-insurance) (2024-07-09)。追偿主管：团队审阅线索而非每宗已结理赔；马萨诸塞州 PIP 示例。没有数字。"It is saving my team hours every week.".。*第一手：访谈；可信度：中。*
