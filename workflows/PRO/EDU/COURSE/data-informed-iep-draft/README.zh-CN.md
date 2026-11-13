---
id: AWF-0099
name: 数据支持的 IEP 草案
summary: "提取学生数据填入 IEP 模板，未知内容留空；由特教教师确定目标，IEP 团队签核。"
deliverable: IEP 草案
shape: "从学区系统提取学生数据 (出勤、吃力的科目) → 找出优势与不足 → 填写 IEP 模板，标记空白字段 (不编造内容) → 🛑 review (特教教师确定目标与服务) → 🛑 sign-off (IEP 团队)"
source_hash: 2ba367a1a98e
---

# 数据支持的 IEP 草案

**与相近工作流的区别：** 最接近的是 AWF-0027 逆向设计课程（Backward-design course，COURSE），它为整个班级设计课程。本工作流则是依据单个学生的记录起草具有法律约束力的个别化计划，由特教教师和 IEP 团队把关，风险较高。分类说明：IEP 也涉及评估，但它的产出是一份教学计划。
**工具变体：** `panorama-education`

## 步骤

1. 工具从学区的多个平台提取每名学生的记录，例如出勤趋势和学生吃力的科目 [[1]](#sources)。
2. AI 寻找规律、优势和不足，为撰写目标提供参考。它并不用于作出 IEP 决定，也不用于指定干预措施 [[1]](#sources)。
3. 工具依据学区的 IEP 模板起草文件，对不知道的字段标记为空白，而不是编造内容 [[1]](#sources)。
4. 🛑 **审阅**：特教教师对目标和干预措施作最终决定 [[1]](#sources)。
5. 🛑 **签发**：草案交给 IEP 团队。文章没有描述这一阶段；它就是现有的法定 IEP 流程，学区表示该工具不会改变这一流程 [[1]](#sources)。
6. 上线之前，该平台经过学区的审查，确认符合州和联邦的合规要求以及学生数据隐私要求 [[1]](#sources)。

**产出：** 经教师审阅、带到 IEP 团队会议上的 IEP 草案。
**失败模式 → 防护：** 数据分散在多个系统、AI 偏见以及推理过程不透明，这些都是一位隐私倡导者提出的 → 使用经学区审核的平台，而不是通用聊天机器人，并做合规与隐私审查；这位倡导者还呼吁告知家长并提供退出选项，学区尚未这样做 [[1]](#sources)。编造内容 → 工具标记空白，而不是填充内容 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Education Week, How AI tools halved this district's IEP prep time](https://www.edweek.org/teaching-learning/how-ai-tools-halved-this-districts-iep-prep-time/2026/10) (2026-10-28)。Mesquite ISD（得克萨斯州）已使用经学区审核的 IEP 起草工具 11 个月。每名学生 "about 45 minutes"（此前最多三小时）。*第一手：访谈；可信度：中。*
