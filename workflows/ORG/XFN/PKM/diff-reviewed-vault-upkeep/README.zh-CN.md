---
id: AWF-0087
name: 差异审阅式笔记库维护
summary: "智能体按口述指令整理笔记库、同步转写稿；每次提交前由本人审阅 git 差异。"
deliverable: 更新后的笔记库
shape: "口述指令 → 智能体通过技能编辑笔记库 (同步转写稿、归档笔记) → (智能体处理行内批注 ⟲ 🛑 review (git diff)) → 提交 → 从会话日志中挖掘摩擦点 → 更新智能体指令"
source_hash: 42a2d37fc4d1
---

# 差异审阅式笔记库维护

**与相近工作流的区别：** AWF-0030 议题树研究（Issue-tree research）产出研究简报，AWF-0031 处理收件箱。本工作流维护的是个人笔记库，智能体的每一处改动都以 diff 形式审阅。
**工具变体：** `claude-code-obsidian`

## 步骤

1. 通过口述（Wispr Flow）把内容采集进智能体会话 [[1]](#sources)。
2. Claude Code 通过技能处理 Obsidian 笔记库，例如把 Granola 的会议转写稿连同时间戳和元数据同步成笔记 [[1]](#sources)。
3. 🛑 **审阅**：在 git 中打开智能体的改动并阅读 diff，因为“智能体并不会完全照我说的去做”[[1]](#sources)。
4. 在 diff 上留下行内 `<!-- USER-COMMENT: -->` 批注，让智能体逐条处理。重复这一过程，直到 diff 通过 [[1]](#sources)。
5. 做好备份（git、外置硬盘、Time Machine），并开启详细输出，以便看到智能体读取了哪些文件 [[1]](#sources)。
6. 定期分析会话消息中的摩擦点（编造日期、跳过步骤），把发现转成对 CLAUDE.md 的修改 [[1]](#sources)。

**产出：** 一个更新后、有版本记录的笔记库，以及供下一次运行使用的修订后的智能体指令。
**失败模式 → 防护：** 智能体无视指令或编造日期 → 用行内批注做 diff 审阅，并把摩擦点分析的结果反馈到 CLAUDE.md。笔记丢失或被覆盖 → git 加离线备份。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Artem Zhutov, Building My Personal AI](https://artemxtech.substack.com/p/what-changed-in-2-weeks-claude-code) (2026-01-12)。Claude Code 处理 Obsidian 笔记库；用行内批注审阅 git diff；对自己的会话做摩擦点分析。"1679 user messages across 12 sessions"。*第一手：是；可信度：中。*
