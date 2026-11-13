---
id: AWF-0144
name: 经理批准的招聘流程操作
summary: "对应聘者分级并给出处理建议；经理批准整批操作后，再发送消息并归档候选人。"
deliverable: 已执行的招聘流程操作
shape: "分流：收件箱 + WAAS + Ashby + 日历 → 每个应聘者：对照岗位手册分级 (归档 | 索要作品示例 | 推进) → 向经理给出建议 (终端或 Slack) → 🛑 action (经理批准整批操作，例如 \"reject all of these\") → 按阶段定制每位候选人的消息 → 在 Gmail、WAAS、Ashby 中发送并归档 → 重新查询各系统以核实"
source_hash: bcda23f07979
---

# 经理批准的招聘流程操作

**与相近工作流的区别：** AWF-0029 寻访-筛选-排期式招聘（Source-screen-schedule hiring）中，智能体撰写证据摘要，且“no reject decision”，由人在最后做决定。本工作流中，智能体对候选人分级，建议归档和拒绝，并在经理下令后自己发送拒信、归档候选人。检查点是按批次的操作审批，产出是已发出的消息和 ATS 变更，而不是面试材料包。
**工具变体：** `claude-code` · `waas-mcp` · `ashby-mcp` · `gmail` · `slack`

## 步骤

1. 配置：复制用户、Ashby 和各岗位的岗位手册模板。手册包含硬性要求、强信号、自动归档规则和邮件模板 [[1]](#sources)。
2. 分流：智能体扫描收件箱、Work at a Startup (WAAS) 的应聘者、Ashby 候选人、日历、已发邮件和草稿，然后把事项分组（排期、流程决定、新申请、噪音）[[1]](#sources)。
3. 审阅应聘者：智能体拉取完整资料，对照手册为每人分级。如果工作许可或所在地不明确，就标记该候选人待审，而不是自动归档 [[2]](#sources)。
4. 可选的后台模式：`/loop 10m /recruit-watch` 会把每个新事项的建议发到 Slack。经理在帖子下回复 👎、'skip' 或 'ask' [[3]](#sources)。
5. 🛑 **操作**：招聘经理批准每个写操作，可逐个也可批量。技能先展示起草好的拒信和归档方案，然后等待（'Present for approval — DO NOT CREATE YET'）。其规则包括 'NEVER send or archive without explicit approval' [[2]](#sources)。
6. 执行：智能体通过 Gmail 或 WAAS 消息发送每封个性化拒信（标准模板加每人一句定制内容），并在 Gmail、WAAS 和 Ashby 中带原因代码归档候选人 [[1]](#sources)[[2]](#sources)。
7. 核实：智能体重新查询 Gmail、Ashby 和 WAAS，每个操作确认生效之前不报告成功 [[2]](#sources)。

**产出：** 候选人在 ATS、WAAS 和 Gmail 中得到一致的通知与归档，反馈备注记录在 ATS 中。经理的招聘流程中已决定的事项被清空。
**失败模式 → 防护：** 因数据缺失（所在地或签证）而拒绝 → 手册规则强制标记，而不是自动归档。某个系统中写入静默失败 → 汇报前必须重新查询。骚扰式群发 → README 明确声明不做批量垃圾邮件。因为智能体对候选人分级，所以会涉及招聘相关法规风险（纽约 LL144、欧盟 AI 法案的高风险类别）。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [YC software team, Recruiting Co-Pilot 'See it work'](https://github.com/yc-software/recruiting) (2026-03-31)。真实会话：评定 8 位应聘者；经理说全部拒绝；智能体发出 8 封个性化拒信并逐一归档。"Claude pulled full profiles for 8 applicants" … "Took about 2 minutes."。*第一手：是；可信度：高。*
