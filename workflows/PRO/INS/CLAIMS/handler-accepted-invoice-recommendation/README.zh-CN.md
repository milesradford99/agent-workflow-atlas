---
id: AWF-0095
name: 理赔员确认的发票处理建议
summary: "对宠物医疗发票逐行建议赔付或除外；理赔员接受、修改或转人工处理。"
deliverable: 理赔付款建议
shape: "收到宠物医疗发票 → 智能体逐行建议赔付 / 除外 → 🛑 action (理赔员接受、修改或转人工) → 现有的付款授权 + QA → 理赔员标记缺失的背景信息 → 🛑 review (资深人员核实后才更新背景数据)"
source_hash: 17b9d4d10b37
---

# 理赔员确认的发票处理建议

**与相近工作流的区别：** AWF-0085 按政策审核报销（Policy-checked expense audit）会自动通过合规的条目，只把违规项交给专员。这里理赔员要确认每一条建议（辅助级），并且知识库的更新另有一道资深人员的审阅关口。
**工具变体：** `uipath-action-center`

## 步骤

1. 范围：NFU Mutual 的宠物和马匹理赔，基于 UiPath 智能体构建 [[1]](#sources)。
2. 智能体审阅每张收到的发票，并建议哪些赔付、哪些除外 [[1]](#sources)。
3. 🛑 **操作**：建议在 Action Center 中呈现给理赔员；理赔员接受、修改，或转入人工处理 [[1]](#sources)。
4. 现有的付款授权、质量保证和审计轨迹保持不变 [[1]](#sources)。
5. 理赔员标记智能体背景信息中缺少的内容（例如一种新药）。🛑 **审阅**：资深团队成员核实每一项补充，之后才更新背景信息；不会自动更新 [[1]](#sources)。

**产出：** 经理赔员接受的逐张发票赔付/除外建议，随后进入正常的付款流程。
**失败模式 → 防护：** 理赔员漏掉的多付漏损 → 在试点中，智能体发现了理赔员漏掉的一处除外项。药品/治疗知识过时 → 理赔员标记出来，由资深人员把关更新。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [diginomica, NFU Mutual's agentic AI pilot](https://diginomica.com/uipath-fusion-2026-nfu-mutuals-agentic-ai-pilot-delivers-results-so-why-ai-governance-still-harder) (2026-03-17)。试点从 9 月到 11 月；建议准确；智能体发现了一处被漏掉的多付；计划于 2026 年下半年投入生产。"the equivalent of 30 people's time each year"（指付款工作量的规模，并非实测的节省）。*第一手：访谈；可信度：中。*
