---
id: AWF-0086
name: 模板驱动的会议纪要
summary: "转写带说话人标记的会议录音，按所选模板生成纪要；经负责人修改后再分发。"
deliverable: 已核准的会议纪要
shape: "录制或上传会议音频 → 转写并标记说话人 → 选择会议模板 → 生成纪要 → (AI 对话修改 ⟲ 🛑 review (负责人修改)) → 导出 Word → 分发"
source_hash: 4505d4b39845
---

# 模板驱动的会议纪要

**与相近工作流的区别：** AWF-0026 环境记录员（Ambient scribe）在临床签发的前提下产出临床记录。本工作流产出的是一般性的政府会议纪要，由负责人审阅，风险较低。
**工具变体：** `iai-minute` · `justice-transcribe`

## 步骤

1. 上传会议录音。音频经转换后存放在有时限的上传链接之后 [[2]](#sources)。
2. 用语音转文字进行转写，按时长和质量选择服务商 [[2]](#sources)。
3. 选择模板：内阁会议、规划委员会、护理评估、一般会议，或自定义模板 [[2]](#sources)。
4. LLM 把对话整理成纪要，并套用政府公文的时态、语法和格式规则 [[2]](#sources)。
5. 🛑 **审阅**：负责人在使用前微调并修正摘要 [[1]](#sources)。
6. 分发最终纪要，并跟进后续工作。在地方议会中，这样做是为了加快规划会议之后的跟进行动，以及督导会谈的记录 [[1]](#sources)。

**产出：** 经修正、作为会议记录导出并分发的纪要。负责人据此跟进后续行动。
**失败模式 → 防护：** 陈述有误或说话人归属错误 → 负责人在分发前更正。敏感会议 → 按相应的密级处理数据，且不保留音频。行动事项跟踪并没有记载为工具功能，所以应把行动事项提取视为手工操作或依赖模板。节省时间的结论来自中央政府的早期测试，而非独立评估 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [GOV.UK, Humphrey helps townhalls](https://www.gov.uk/government/news/ai-experiments-see-humphrey-help-townhalls-cut-costs-and-improve-services) (2025-05-23)。25 个地方议会试用了 Minute，包括 West Berkshire 和 Stockton-on-Tees，用于规划和社会照护会议。"officials are saved from 60-minutes of admin for each hour-long meeting"。*第一手：是；可信度：低。*
