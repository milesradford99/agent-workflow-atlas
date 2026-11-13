---
id: AWF-0061
name: 原话核验的研究综合
summary: "基于检索到的原话和主题起草研究洞察报告；研究员对照原始记录核验每条引用并签批。"
deliverable: 研究洞察报告
shape: "转录稿集中存放 → 每个 研究问题：检索带受访者编号的原话 → 反复出现的主题 → 🛑 review (对照原始记录核验每个主题和原话) → 人工综合并排定优先级 → 报告草稿 → 🛑 sign-off (研究员) → 发布并附给干系人的 TL;DR"
source_hash: d7eec03e1d46
---

# 原话核验的研究综合

**与相近工作流的区别：** AWF-0007 反馈到原型：那个工作流把反馈变成原型。本工作流止于经过核验的洞察报告，不做构建。
**工具变体：** [`claude-code` kit](variants/claude-code.md) · `claude-code-skill` · `notebooklm` · `dovetail` · `otter-ai`

## 步骤

1. 把所有录音和转录稿放进同一个证据库，例如 Dovetail，或每项研究一个 notebook [[2]](#sources)[[3]](#sources)。
2. 针对每个研究问题，让智能体给出匹配的原话，并附受访者编号和时间戳或来源链接。一次只问一个问题，一直问到结果穷尽为止 [[2]](#sources)[[3]](#sources)。
3. 要求给出 3 位及以上受访者提到的主题，附直接引语，并明确告诉它不要解读情绪 [[1]](#sources)。
4. 🛑 **审阅**：研究员对照原始录音或转录稿核验每个主题和每条原话。在一次实践中，这一步发现“每天查看仪表盘”其实是在绕开失灵的告警，而不是用户活跃的表现 [[1]](#sources)。
5. 由人对洞察进行聚类并排定优先级（在 Miro 中做亲和图）。AI 只用作唱反调的角色，检查是否有遗漏或偏见 [[2]](#sources)。
6. 智能体根据已核验的洞察起草报告 [[3]](#sources)。
7. 🛑 **签发**：研究员批准报告，随后发布到 Confluence，并把 TL;DR 发到 Slack 频道 [[3]](#sources)。

**产出：** 一份引用可追溯、经过核验的洞察报告，发布到 Confluence 或做成幻灯片，用于支撑设计和产品决策。
**失败模式 → 防护：** 编造原话（ChatGPT 即使在温度 0.1 下也出现过）→ 基于来源的检索加 100% 原话核对 [[3]](#sources)。仅凭字面词语误判情绪 → 提示词禁止解读情绪，并由人重新听录音 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Tanya Donska, Using AI for UX Research](https://dnsk.work/blog/using-ai-for-ux-research-workflow) (2025-10-08)。Deutsche Telekom 的研究：8 场访谈；AI 提炼的主题对照音频核验。"45-minute interview uploaded. 5 minutes later, transcript ready. 90% accurate."。*第一手：是；可信度：高。*
- [Lana Hung, How we transformed qualitative synthesis](https://medium.com/@LanaHung/how-we-transformed-qualitative-synthesize-with-ai-chatgpt-notebooklm-claude-code-0b4df664a15f) (2026-06-14)。ShopBack 的用户研究团队改用 Claude Code 综合技能，并发布到 Confluence/Slack。"The entire process typically took 3 — 5 days." → "we were able to complete most reports within a single day"。*第一手：是；可信度：高。*
