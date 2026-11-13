---
id: AWF-0082
name: 模型分流的记录公开审查
summary: "用训练好的模型对记录判定解密或豁免；存疑记录由人工复核，模型判断经抽检后才公开。"
deliverable: 公开的政府记录
shape: "过往审查人的决定 → 训练模型 → 每个记录：判定解密 | 豁免 | 存疑 → 存疑：🛑 handoff (人工审查人) → 🛑 sample (对模型判断做质检) → 把决定载入审查系统 → 发布到 FOIA 阅览室 → 因主题漂移而重新训练"
source_hash: 36958060dea9
---

# 模型分流的记录公开审查

**与相近工作流的区别：** AWF-0005 告警充实与裁定（Alert enrich and adjudicate，SECOPS）同样按置信度分流，但它裁定的是安全告警。这里的产出是依据解密/FOIA 规定经法律审查后公开的政府记录，并带有质检抽样。没有相近的工作流。
**工具变体：** `state-dept-ips-declass`

## 步骤

1. 选定一种格式统一的记录（eRecords 中的外交电报），其过往的人工解密决定可以充当标注 [[1]](#sources)。
2. 用这些决定训练模型（解密与豁免解密）。试点中的训练数据是 1995–96 年的电报决定，模型则用于处理 1997 年的电报 [[1]](#sources)[[2]](#sources)。
3. 把每份电报判定为可能解密、可能豁免或需要人工审查 [[2]](#sources)。
4. 🛑 **接手**：模型拿不准的电报交给人工审查人 [[1]](#sources)。
5. 🛑 **抽检**：人工对模型输出做质量检查，并按需重新标注训练数据 [[1]](#sources)。
6. 把模型预测载入审查系统，然后在 FOIA 阅览室主动发布已解密的电报（案号 S-2023-00002，每月发布）[[1]](#sources)。
7. 重新训练并监测主题漂移。随着世界局势变化，敏感内容也在变，工作人员要持续审阅训练数据 [[1]](#sources)[[2]](#sources)。

**产出：** 每月发布到国务院 FOIA 阅览室的已解密历史记录。豁免的记录转交 NARA 或进一步审查。
**失败模式 → 防护：** 主题漂移使过往决定不再适合作为依据 → 由人关注漂移并重新训练。判断不透明 → 准备好解释 AI 如何得出结果。FOIA 数据杂乱，分散在 3 个系统中 → 先做好数据准备 [[1]](#sources)。置信度阈值未公开 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [US Department of State, AI Pilot Results](https://transforming-classification.blogs.archives.gov/wp-content/uploads/sites/10/2024/07/State-AI-Pilot-Results-June-24-2024.pdf) (2024-06-24)。电报解密从试点到全面部署，设计上始终让人参与其中；电报发布到 FOIA 阅览室。"Reduced volume for humans to review (by 80%)"；"450,000 cables reviewed by AI"。*第一手：是；可信度：高。*
