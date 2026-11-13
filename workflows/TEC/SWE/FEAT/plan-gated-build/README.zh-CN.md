---
id: AWF-0001
name: 先审计划再开发
summary: "从议题出发，先出计划和失败测试再实现并提交 PR；计划、提交动作和最终评审都由人把关。"
deliverable: 拉取请求（PR）
shape: "读取议题和代码 → 制定计划 → 🛑 plan → 编写失败测试 → (写代码 ⟲ 测试) → 全新上下文评审 → 🛑 action → 创建 PR → 🛑 review → 更新上下文文件"
source_hash: cfc3885e2a6a
---

# 先审计划再开发

- **输入：** 带验收标准的议题；含 `CLAUDE.md`/`AGENTS.md` 的仓库（构建、测试和 lint 命令，约定，禁区）；可用的测试套件。
- **角色与工具：** 主智能体（读取、编辑、白名单 shell）；只读的探索子智能体；验证器（格式化和 lint 钩子、测试、类型检查，UI 改动用浏览器截图）；全新上下文的评审子智能体。

## 步骤

1. 智能体读取上下文文件、议题（`gh issue view` 或工单系统的 MCP）以及相关代码。探索子智能体并行展开，梳理受影响的模块。
2. 在计划模式（只读）下，智能体写出计划：要改的文件、方案、测试策略、待确认的问题 [[2]](#sources)。🛑 **计划**：这是杠杆最高的纠偏点。
3. 编写体现验收标准的失败测试，并确认它们确实失败。
4. 分小步实现，每一步后运行针对性测试和类型检查。根据失败输出循环修复，并在升级转交前限制迭代次数。
5. 全新上下文的评审者对照规格检查 diff：边界情况、死代码、安全问题。
6. 对于 UI 改动，启动开发服务器、截图并与设计稿对比。
7. 🛑 **操作**：提交、推送并创建 PR，除非这些操作已被预先授权。
8. 🛑 **审阅**：由人评审 PR 和 CI 结果。
9. 把反复出现的纠正意见写回上下文文件。

**产出：** 一个带测试、经过评审的 PR，以及更新后的上下文文件。
**失败模式 → 防护：** 智能体为了让测试通过而改测试 → 测试写完后禁止修改测试。范围蔓延 → 标记计划清单之外被改动的任何文件。上下文饱和 → 任务之间清空上下文，并把计划持久化到文件 [[2]](#sources)。
**相近形态：** 每次编辑都要求批准的版本（`assist`，辅助）按替换测试属于另一个物种。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [HumanLayer, *Advanced Context Engineering for Coding Agents*](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) (无署名和日期；图片标注 Aug 2025)。在 300k 行代码的 Rust 代码库上按研究 → 计划 → 实现推进；由人审阅研究和计划。"shipping 35k LOC to BAML"；"spent 7 hours"。*第一手：是；可信度：高。*
- [Harper Reed, *My LLM codegen workflow atm*](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) (2025-02-16)。规格 → 提示词计划（TDD 变体）→ 逐步实现，每步后都测试。"This entire process will take maybe 15 minutes."（指规划阶段）。*第一手：是；可信度：中。*
