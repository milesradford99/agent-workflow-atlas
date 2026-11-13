---
id: AWF-0109
name: 入站线索资格审核与约会
summary: "实时对话筛选入站销售线索并预约会议；人工每天复核所有对话，会议由销售负责。"
deliverable: 已预约的合格会议
shape: "联系销售表单 → 读取提交内容 + 补全公司信息 → 实时语音/文字对话 → 按固定标准判定资格 → 通话中未达标：先做网站分析 + 补贴资格检查，再取消资格 → 分流：预约会议 | 自助服务 | 支持 → 将决定及理由写入 CRM + 通知团队 → 🛑 review (每天对照人工评分复核每一场对话) → 🛑 handoff (销售代表主持已预约的会议) → 调整提示词/标准"
source_hash: c2d222d76cb6
---

# 入站线索资格审核与约会

**与相近工作流的区别：** AWF-0020 先调研再个性化的外呼：它在计划和抽检关卡之后建立外呼名单并启动触达序列。本工作流则实时回应入站线索，并自行预约会议（抽检式自主），事后再做复核。产出是已预约的会议，而不是已启动的触达序列。
**工具变体：** `elevenlabs-agents` · `salesforce` · `qualified-piper`

## 步骤

1. 每次通话开始时，智能体先查看线索提交的联系表单。它依据包含 100 多条 FAQ 和文档的知识库回答产品问题 [[1]](#sources)。
2. 在对话中按既定标准（使用场景、预期用量、时间表）判定资格。把智能体调成宁可误报也不漏报 [[1]](#sources)。
3. 如果通话没有定论，在取消资格之前先运行后端的瀑布式流程：对线索公司网站做 AI 分析，并行检查初创公司补贴资格 [[2]](#sources)。
4. 为线索分流：跨时区查看日历并当场预约会议，引导其自助服务，或交给支持团队。并按线索的要求发送一封跟进邮件 [[1]](#sources)[[2]](#sources)。
5. 把使用场景、资格判定和补全的数据写入 CRM 并通知团队，使判定结果及其理由都可见 [[2]](#sources)。
6. 🛑 **审阅**：团队每天复核每一场对话，无论合格与否，检查判定是否准确、是否有帮助。先阅读 CSAT 低和高的通话 [[1]](#sources)[[2]](#sources)。
7. 🛑 **接手**：由人工销售主持已预约的会议，以智能体记录的内容开场 [[3]](#sources)。
8. 把复核发现反馈为提示词规则或工作流节点，并在工具调用失败时切换模型 [[1]](#sources)。

**产出：** 已排进销售代表日历的会议及 CRM 中的资格记录；不合格的线索被分流到自助服务或支持。
**失败模式 → 防护：** 边缘情况规则不断堆积使提示词膨胀 → 拆分为工作流节点 [[1]](#sources)。线索要求转人工来绕过资格审核 → 设置明确的护栏 [[1]](#sources)。工具调用期间的沉默让来电者困惑 → 口头播报状态 [[1]](#sources)。被中途挂断的通话被误判为不合格 → 网站分析的瀑布式流程 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [ElevenLabs, How our AI SDR qualifies leads in minutes](https://elevenlabs.io/blog/how-our-ai-sdr-qualifies-leads-in-minutes) (2026-09-15)。通过瀑布式流程把准确率从 78% 提高到 92%；每天复核每一通电话。"4 min median speed to qualification"。*第一手：是；可信度：高。*
- [SaaStr, inbound AI agent guide](https://www.saastr.com/the-saastr-ai-guide-to-building-a-top-tier-inbound-ai-agent-17000-conversations-600-meetings-booked-and-60-more-new-business/) (2026-09-23)。入站智能体筛选并预约赞助会议；由三个人运营。"17,000 conversations with prospects in the last 12 months and booked about 600 meetings"。*第一手：是；可信度：中。*
