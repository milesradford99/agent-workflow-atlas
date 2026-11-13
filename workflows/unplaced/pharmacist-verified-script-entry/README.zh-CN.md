---
id: AWF-0215
name: 药师核验的处方录入
summary: "机器人把收到的处方录入药房系统，无法匹配的跳过；药师两次核验后才发药。"
deliverable: 已录入的处方
shape: "收到处方 (电子处方 | 传真 | 队列) → 机器人操作 PMS 界面：匹配患者、开方医生、药品、数量、SIG → 不确定 / 无法识别：机器人跳过 (记录原因) → 🛑 review (QV1 药师核验；驳回到错误队列) → 🛑 sign-off (QV2 发药前最终核验) → 每日复查跳过项和错误 → 新一轮训练"
source_hash: 76ddae18fb78
---

# 药师核验的处方录入

**与相近工作流的区别：** PRO/HLT（CLINDOC、RCM、CLINTRIAL、DRUGDISC）中没有特别接近的。按流程最接近的是 AWF-0148 的报关单准备（提取 → 持证审阅人 → 提交），但这里的智能体是通过计算机操作来操作 PMS，并且每个条目在发药前都要经过两次药师核验。
**工具变体：** `tjm-labs`

## 步骤

1. 训练过程仿照新技术员入职：记录员工如何录入新患者、查询保险和录入处方；每周复盘，持续 4-5 周；然后每天用 5 或 10 份处方测试约六周，再在一个站点上线 [[1]](#sources)。
2. 机器人读取电子处方和传真，并通过技术员使用的同一批界面把它们录入药房管理系统：按姓名、出生日期和地址匹配患者，按 NPI 匹配开方医生，然后录入药品、数量、供应天数和用法 [[1]](#sources)[[2]](#sources)。
3. 遇到不认识的内容时，它会停下来并标记为“bot skip”（机器人跳过），把原因记在一张持续更新的表里；管制药品默认留给药师处理 [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：机器人录入的每张处方在数据录入后立即由药师做 QV1 核验；有错误的驳回到错误处理队列交给技术员，并且机器人以一名具名技术员的身份登记，以便追踪它的错误 [[1]](#sources)。
5. 🛑 **签发**：药品出药房之前，由药师做 QV2 最终核验 [[1]](#sources)。
6. 团队每天复查跳过项和错误，与厂商分享以便修复，大约每 90 天增加一项新技能 [[1]](#sources)。

**产出：** 录入 PMS 且发药前经药师两次核验的处方；以及驱动再训练的跳过/错误日志。
**失败模式 → 防护：** 机器人对不常见的处方瞎猜 → 设计上就是跳过，绝不临场发挥 [1][2]。录入错误 → QV1 发现并驳回到错误队列；记录该错误并与厂商一起修复 [1]。早期跳过率高 → 从 20% 出头降到 10% 以下 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [TJM Labs, Inside Horizon Pharmacy webinar](https://tjmlabs.com/blog/horizon-pharmacy-redesigning-ltc-operations-with-ai-webinar/) (2026-09-16)。长期护理药房的 CEO 和药师介绍机器人“Hal”、两次药师核验和跳过率追踪。"Megan has managed the bot-skip rate down from the mid-20s at the start to under 10% in the last 60 days. That is about 2,700 scripts a month the team does not have to touch directly."。*第一手：是；可信度：高。*
