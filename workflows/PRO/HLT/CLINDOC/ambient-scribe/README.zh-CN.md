---
id: AWF-0026
name: 诊室环境语音病历助手
summary: "经患者同意后录制就诊，生成关联转写稿的病历、编码和患者小结；医生审核签署。"
deliverable: 临床病历
shape: "🛑 plan (患者同意) → 录制就诊 → 区分说话人的转写稿 → 加载电子病历上下文 → 病历 + 编码 + 患者小结 → 每句话链接到转写稿 → 🛑 review → 🛑 sign-off → 归档到电子病历"
source_hash: ce4f78794515
---

# 诊室环境语音病历助手

## 步骤

1. 🛑 **计划**：取得患者对录音的同意。
2. 在诊室或用手机进行环境录音。
3. 区分说话人的转写，然后按专科模板生成结构化病历。
4. 病历中的每个短语都链接到其来源录音或转写稿。Abridge 把这称为“Linked Evidence”，位于 Epic Haiku → Hyperdrive 之内 [[26]](#sources)。
5. 🛑 **审阅**：医生编辑病历。
6. 🛑 **签发**：医生签署，并作为法律意义上的作者。

**工具变体：** `abridge-epic` [[26]](#sources) · `dragon-copilot`（2025 年 3 月发布；把 Dragon Medical One 听写与 DAX 环境录音结合 [[25]](#sources)） · `nabla` · `ambience`
**标签：** 风险 `high`，HIPAA，需要签署 BAA。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Taylor … Adams, UC Davis Health, JMIR Med Inform 2026;14:e86474](https://escholarship.org/content/qt9r89g3sp/qt9r89g3sp.pdf) (pilot Jul–Aug 2024)。31 位医生，7,545 份病历；其中 356 份被评估有无遗漏和幻觉；每份病历都由医生批准。"94.7% (337/356) free from significant errors"；"hallucinations (n=41, 11.5%)"。*第一手：是；可信度：高。*
