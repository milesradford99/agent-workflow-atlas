---
id: AWF-0153
name: 漏提货电话处置
summary: "就零担漏提货致电承运商并决定后续动作；无法解决的移交零担团队处理。"
deliverable: 已解决的提货异常
shape: "零担漏提货通知 → 每个 货件：呼叫智能体联系承运商 → 决策智能体选择后续动作 (改期 | 重新委托 | 确认已提货) → 更新系统 + 通知客户 → 未解决：🛑 handoff (零担团队) → 日常：向承运商共享漏提货数据"
source_hash: 58d82bb0193f
---

# 漏提货电话处置

**与相近工作流的区别：** AWF-0005 告警补充与裁定（Alert enrich and adjudicate）会自动关闭无害告警。本工作流中，智能体在现实世界中行动（对承运商外呼、重新委托），产出是已解决的货件，而不是一个判定。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `FREIGHT`（TAXONOMY.md 规则 2）之前，先归在这里。

## 步骤

1. 当提货没有按计划发生时，智能体会自动收到通知 [[1]](#sources)[[2]](#sources)。
2. 一个智能体给承运商打电话或联系承运商；第二个智能体决定后续动作；两者合力能 '100 calls and 100 decisions simultaneously' [[1]](#sources)。
3. 系统随之更新，客户收到通知；此前是由人去查承运商网站、打电话、记录进展并重新委托 [[1]](#sources)[[2]](#sources)。
4. 🛑 **接手**：未能自动化的那部分（95% 的核查已自动化）仍由团队处理；资料来源没有详细描述这一分流 [[1]](#sources)。
5. 漏提货数据每天与承运商共享 [[2]](#sources)。

**产出：** 每个漏提货都得到解决或升级，外加每日的承运商数据推送。
**失败模式 → 防护：** 错误的重新委托把卡车派到尚未备好的货物处 → 智能体先与承运商确认状态。注：移交路径只是由资料来源暗示的。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../research/2026-11-second-pass.md)。

- [C.H. Robinson, missed LTL pickups](https://www.chrobinson.com/en-us/about-us/newsroom/press-releases/2026/chrobinson-lean-ai-agents-for-ltl-pickup-efficiency/) (2026-01-26)。已推广到各零担客户；每天数百个货件。"95% of checks on missed LTL pickups have been automated, saving over 350 hours of manual work per day."。*第一手：是；可信度：高。*
