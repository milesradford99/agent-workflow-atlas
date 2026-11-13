---
id: AWF-0031
name: 每日收件箱分流
summary: "每天早晨整理邮件、日程和私信，生成回复草稿、时段建议和重点简报；所有消息由本人发送。"
deliverable: 已分流的收件箱
shape: "07:00 定时：邮件、日程、私信 → 分类 (处理 / 知悉 / 转派 / 归档) → 每个邮件线程：回复存为草稿 → 会议时段建议 → 前 5 项简报 → 🛑 action (每条消息由本人发送，每个邀请由本人接受)"
source_hash: 5a206fb917ad
---

# 每日收件箱分流

**智能体套件：** [在 Claude Code 中运行](variants/claude-code.md)
**防护：** 收到的邮件是不可信输入（提示词注入的攻击面）。智能体绝不能自行发送。

## 步骤

1. 按计划运行分流，用桌面端的定时任务，因为它会接触本地数据 [[2]](#sources)。通过 MCP 连接 Gmail、日历和通讯录 [[1]](#sources) [[2]](#sources)，如有需要再加入 Slack、WhatsApp 或 iMessage 来处理私信 [[3]](#sources)。
2. 把每一项归入某个层级：立即回复、今天处理，或知悉/归档 [[3]](#sources)。按领域分类也可行，比如审稿邀请、合作者邮件、各类邀请和行政截止日期 [[2]](#sources)。一份需要回复的简单清单（未读优先）同样可行 [[1]](#sources)。
3. 每个邮件线程：起草回复。找到原始线程及其邮件 ID，明确写出 `To:` 地址，搜索上下文，把回复存为草稿，绝不发送 [[1]](#sources)。语气规则来自机主已发送的几百封邮件，提炼后写入 CLAUDE.md [[1]](#sources) [[3]](#sources)。
4. 建议会议时段：当某个线程需要约时间时，把日历占位作为待批准的操作提出，而不是直接订下事件 [[2]](#sources)。
5. 撰写早间简报，涵盖日程、任务、紧急消息和会议准备 [[3]](#sources)，另附摘要和待办事项追踪表 [[2]](#sources)。
6. 🛑 **操作**：机主在自己的邮件客户端中查看草稿，然后编辑并发送，或者拒绝 [[1]](#sources)。每个提议的操作（包括日历占位）都要等待批准，不会自动发送任何内容 [[2]](#sources)。

**产出：** 一个已分流的收件箱、放在邮件客户端草稿箱中的回复草稿、建议的日历占位，以及一份简短的早间简报。机主逐项发送、接受或丢弃。
**失败模式 → 防护：** 未经批准就发送（一个原型接受了作者不想要的写书邀约）→ 只给智能体草稿权限，不提供发送工具 [[1]](#sources)。有发送能力却没有说明审批步骤的方案 [[3]](#sources) → 直接移除发送权限，而不是依赖提示词。来自收件邮件的提示词注入，因为私有数据、不可信内容和对外消息凑在一起就构成“致命三要素”（lethal trifecta）→ 让发送动作不在智能体的能力范围内 [[4]](#sources)。回复发错地址，因为工具不会从线程里取收件人 → 在提示词中明确写出 `To:` [[1]](#sources)。邮件会经过第三方服务 → 连接私人收件箱之前先权衡这一点 [[1]](#sources)。MCP 连接中断 → 该技能会优雅降级，而不是直接失败 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Harper Reed, *Getting Claude Code to do my emails*](https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/) (2025-12-03)。通过 MCP 接入邮件、日历和通讯录 → 只生成草稿；每条消息由他本人发送，此前发生过一次未经批准的发送。"the past couple hundred emails I have sent"（用于训练语气）。*第一手：是；可信度：高。*
- [Pedro Sant'Anna, `/triage-inbox`](https://github.com/pedrohcgs/claude-code-my-workflow)。定时的早晨分流 → 分类 → 草稿 → 建议的日历占位；每个对外操作都需要确认。triage-inbox v2.0（配置，没有运行记述）。*第一手：是；可信度：高。*
- [Mike Murchison, claude-chief-of-staff](https://github.com/mimurchison/claude-chief-of-staff)。`/gm` 简报 + 三级分流并附草稿；**允许发送**，且没有说明审批步骤。"from 90 minutes of morning inbox processing to about 5"。*第一手：是；可信度：中。*
