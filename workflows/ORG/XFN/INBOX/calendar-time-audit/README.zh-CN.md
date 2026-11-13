---
id: AWF-0145
name: 日历时间审计
summary: "审查近两周日历，提出可取消或转交的会议；本人逐项取舍，由助理执行日历变更。"
deliverable: 带转交计划的日历审计
shape: "周度：只读方式读取最近两周日历 → 对会议分类 (可写成文档、可转交、可跳过、重复预订、频繁切换上下文) → 对照岗位期望比较时间分配 → 下周：可取消或转交的会议 → 🛑 review (本人逐项接受或拒绝) → 🛑 handoff (助理执行日历变更)"
source_hash: dad44fc8166a
---

# 日历时间审计

**与相近工作流的区别：** AWF-0031 每日收件箱分流（Daily inbox triage）每天处理邮件、日历和私信，产出回复草稿和前 5 项简报，每条消息都由人发送。本工作流的产出是对时间使用情况的回顾性审计，加上向前的取消与转交计划。它每周运行一次，检查点是先审阅、再移交给助理（EA），而不是逐条消息发送。
**工具变体：** `claude-code` · `cursor` · `google-calendar-api`

## 步骤

1. 通过官方 API，以只读方式连接 Google Calendar，并连接不带发送权限的 Gmail。令牌放在被 git 忽略的 .env 文件中。上下文文件描述负责人的角色和风格 [[1]](#sources)[[2]](#sources)。
2. 提示智能体分析过去两周的时间是怎么花的 [[2]](#sources)。
3. 智能体标出这些情况：可以改成文档或 Slack 更新的会议、总监或同事可以代为参加的会议、来自陌生组织者或议程不清的会议、重复预订，以及频繁的上下文切换 [[1]](#sources)[[2]](#sources)。
4. 一个 'Brutal Truth' 模块把时间分布与该岗位的期望做对比，指出低于该岗位层级的工作 [[1]](#sources)。
5. 智能体查看下周，建议可以取消的会议 [[2]](#sources)。
6. 🛑 **审阅**：负责人把输出当作初稿，逐项接受或拒绝每条建议 [[2]](#sources)。
7. 🛑 **接手**：负责人把结论交给她的助理（EA），由助理修改日历。智能体对日历没有写权限 [[1]](#sources)[[2]](#sources)。

**产出：** 一份时间分配审计和下周的取消与转交清单，交给助理，由助理修改日历。
**失败模式 → 防护：** 建议忽略背景（有些会议有政治上的重要性）→ 负责人逐项接受或拒绝。智能体擅自操作他人日历 → 只读的日历范围，且无发送权限。会议所需的数据缺失（如链接）→ 负责人修正并优化提示词；她建议在调校到位之前先运行智能体 '3 or 4 times'。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Aakash Gupta interview with Rachel Wolan](https://www.aakashg.com/ai-product-leadership-rachel-wolan-claude-code-cursor/) (2025-11-24)。Webflow 的 CPO 大约每周做一次日历分析，并把结果分享给她的助理。"I asked to look at the last two weeks and I said, can you analyze my calendar, like how I spent my time?"。*第一手：访谈；可信度：中。*
- [How I AI, Rachel Wolan](https://chatprd.ai/how-i-ai/webflow-cpo-ai-chief-of-staff-adoption-playbook) (2025-12-29)。同一套系统，日历只读、无发送权限；标出适合异步处理、转交和拒绝的会议。"Her agent helps manage a 500+ email backlog"。*第一手：访谈；可信度：中。*
