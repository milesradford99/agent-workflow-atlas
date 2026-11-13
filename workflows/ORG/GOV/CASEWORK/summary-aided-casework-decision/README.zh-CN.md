---
id: AWF-0081
name: 摘要辅助的个案决定
summary: "整理面谈记录摘要并检索政策依据；决策者核对摘要，亲自作出并签署决定。"
deliverable: 个案决定
shape: "面谈记录 → 总结案情 → 🛑 review (决策者核对摘要) → 政策问题 → 检索带出处的国别政策说明 → 决策者阅读完整原文 → 起草决定 → 🛑 sign-off (决策者作出决定) → 🛑 sample (质量抽检)"
source_hash: 442aedaaa04c
---

# 摘要辅助的个案决定

**与相近工作流的区别：** AWF-0021 流程智能体（Procedure agent）按既定流程办理客户请求。这里的智能体只负责准备材料，每一项决定都由法定的决策者作出并签署（辅助级自主度，高风险）。
**工具变体：** `home-office-acs` · `home-office-aps`

## 步骤

1. 把庇护面谈记录（可能长达 50 页甚至更多）交给 LLM，由它写出简明的案情摘要（Asylum Case Summarisation）[[1]](#sources)。
2. 试点之前，技术专家审阅了每一份摘要。其中 9% 被判定为不准确或不完整而剔除，这些案件走常规流程 [[1]](#sources)。
3. 🛑 **审阅**：决策者借助摘要重新熟悉案情，并对照面谈记录核对。摘要没有指向记录的出处标注，所以这一步核对只能手工完成 [[1]](#sources)。
4. 决策者向一个聊天式检索助手提出针对个案的政策问题，该助手覆盖国别政策信息说明（Country Policy Information Notes）和原籍国信息请求（Country of Origin Information Requests）（Asylum Policy Search）。它返回带出处的摘要 [[1]](#sources)。
5. 决策者在依赖其引用的说明或请求之前，必须先打开完整原文 [[1]](#sources)。
6. 🛑 **签发**：只有决策者可以作出决定。这些工具自身不能作出决定，也不能给出决定建议 [[1]](#sources)。
7. 🛑 **抽检**：用常规的质量框架（Calibre）对决定质量做抽检，并与对照组比较 [[1]](#sources)。

**产出：** 由个案办理人撰写并负责的庇护决定，外加一份抽检质量记录。在试点中，AI 摘要和政策检索的回答只是辅助工具。
**失败模式 → 防护：** 摘要不准确或不完整 → 使用前先筛查摘要（试点中剔除了 9%）。用户对摘要没有十足信心（23%）→ 决策者重读面谈记录，而摘要缺少出处标注使这一步更费力。过度依赖政策摘要 → 必须打开完整原文。试点规模小且依赖自报 → 持续监测，并在全面推广前做部署后评估 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [UK Home Office, Evaluation of AI trials in the asylum decision-making process](https://www.gov.uk/government/publications/evaluation-of-ai-trials-in-the-asylum-decision-making-process/evaluation-of-ai-trials-in-the-asylum-decision-making-process) (2025-04-29)。两个试点，2024 年 5 月至 12 月。试验组与对照组决策者对比；摘要和政策检索节省的时间；质量抽检。"reviewed transcripts 23 minutes quicker than the comparison group (a 32% time saving)"；政策检索 "saved on average 37 minutes per case"。*第一手：是；可信度：中。*
