---
id: AWF-0029
name: 寻访筛选排期招聘
summary: "寻访候选人、整理个人证据摘要、安排面试并准备面试材料；智能体不做淘汰决定，由人定夺。"
deliverable: 候选人管线
shape: "职位描述 → 🛑 plan → 每个 渠道：寻访 → 按评分项给出匹配理由 → 🛑 action → 外联 → 每位 候选人：证据摘要 (不做淘汰决定) → 排期 → 面试材料包 → 🛑 sign-off (由人决定)"
source_hash: f7bc2afaa629
---

# 寻访筛选排期招聘

**工具变体：** `linkedin-hiring-assistant`（2025 年 9 月底前推出全球英文版；寻访候选人，通过 InMail 问答筛选，安排面试 [[29]](#sources)） · `paradox` · `juicebox`

**为什么“给证据，不下结论”很重要（合规）：**
- **纽约 LL144。** 要求在使用自动化招聘工具之前每年做一次独立的偏见审计，公开审计结果摘要，并提前 10 个工作日通知候选人。责任在雇主，而不在供应商 [[27]](#sources)。
- **欧盟 AI 法案。** 把招聘类 AI 归为高风险。其义务原定于 2026 年 8 月 2 日生效，Digital Omnibus 暂定将其推迟到 2027 年 12 月 2 日。请确认法律上实际生效的是哪个日期 [[28]](#sources)。

让智能体只提供*证据*、不下*结论*，可以降低这两方面的风险。

## 步骤

1. 从职位描述和用人经理的标准出发。Hiring Assistant 会把招聘人员的标准转成搜索查询 [[32]](#sources)。在 YC 的做法中，用一个 playbook 文件记录每个职位的评分依据 [[30]](#sources)。
2. 🛑 **计划**：招聘人员选定职位，并定义给候选人打分所依据的资质要求 [[31]](#sources) [[32]](#sources)。用人经理调整标准时，招聘人员更新标准，几分钟内就能得到新的一批候选人 [[31]](#sources)。
3. 每个渠道：寻访。从 LinkedIn 拉取候选人，并“in a click”导出到 ATS 的候选短名单 [[31]](#sources)。在 YC 的做法中，每天开始时的 `/triage` 会扫描收件箱、Work at a Startup (WAAS) 的申请人、Ashby ATS 和日历 [[30]](#sources)。
4. 按评分项写出匹配理由：依据招聘人员的资质要求给每位候选人打分 [[31]](#sources)，并显示个人资料中符合哪些资质、缺少哪些 [[32]](#sources)。`/review-applicants` 依据 playbook 给新申请人评级 [[30]](#sources)。
5. 🛑 **操作**：招聘人员在外联信息发出前阅读并编辑草稿。LinkedIn 起草的消息可以编辑 [[32]](#sources)。在 YC 的做法中，`/outreach` 依据职位模板起草个性化邮件，经理审阅一封结束沟通的邮件并修改，然后才说“send it” [[30]](#sources)。
6. 每位候选人：证据摘要，而不是结论。`/candidate-brief` 写一段背景简介，`/candidate-status` 在 WAAS、Ashby、Gmail 和日历中核对候选人的情况 [[30]](#sources)。供应商声明 Hiring Assistant “does not make autonomous or automatic decisions” [[32]](#sources)。
7. 排期：`/schedule` 查找空闲时段，创建 Zoom 或线下面试事件，发送邀请，并推进候选人在 ATS 中的阶段。改期后再检查 ATS 事件是否已同步 [[30]](#sources)。YC 仓库里的面试准备就是第 6 步的候选人简介 [[30]](#sources)。
8. 🛑 **签发**：由人决定谁进入下一轮、谁被淘汰。按纽约 LL144，自动化工具的偏见审计和候选人通知义务由雇主而非供应商承担 [[27]](#sources)，而欧盟 AI 法案把招聘类 AI 视为高风险 [[28]](#sources)。

**产出：** ATS 中的候选人管线：已寻访并打分的短名单（附按评分项的理由）、已发出的外联、已约定的面试和候选人简介。晋级与淘汰的决定交给用人经理。
**失败模式 → 防护：** 一条指令批量淘汰（“reject all of these” 在约 2 分钟内发出了 8 封拒信）→ 逐个候选人签发，而不是按批次 [[30]](#sources)。日历、ATS 和邮件不同步 → 每次排期变更后检查同步情况 [[30]](#sources)。骚扰候选人 → README 对此提出警告，并说明该工具不是用来取代判断的 [[30]](#sources)。模型偏见 → LinkedIn 对每个模型做公平性审查 [[32]](#sources)，而雇主按 LL144 仍需自己的独立审计 [[27]](#sources)。配置文件中的 API 密钥和令牌 → 放在被 git 忽略的文件里 [[30]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [YC software team, yc-software/recruiting](https://github.com/yc-software/recruiting)。用于分流、外联、排期和候选人简介的 Claude Code 命令；经理批准每一步，**包括淘汰**。"27 inbox emails, 38 active candidates"；评级 8 位申请人，"about 2 minutes"。*第一手：是；可信度：中。*
- [LinkedIn, Infinite Resource Solutions story](https://business.linkedin.com/hire/customer-stories/infinite-resource-solutions) (undated)。寻访 → 导出到 ATS → 依据招聘人员的标准打分。"2–3 hours per day"；"48 hours to less than a day"。*第一手：厂商；可信度：低。*
