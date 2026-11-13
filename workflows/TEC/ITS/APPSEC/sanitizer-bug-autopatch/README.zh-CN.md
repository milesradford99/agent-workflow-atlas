---
id: AWF-0067
name: Sanitizer 漏洞自动修复
summary: "为 Sanitizer 发现的缺陷生成并测试修复提交；安全工程师筛选，代码所有者验证后提交。"
deliverable: 安全修复提交
shape: "单元测试中发现 sanitizer 问题 → 复现并隔离（堆栈跟踪、目标文件）→ 每个 模型：生成修复 → 构建 + 重跑测试 + 重跑 sanitizer → 选出最佳修复 → 🛑 review (安全工程师筛选) → 🛑 sign-off (代码所有者) → 提交"
source_hash: 7bb4ea6a9a03
---

# Sanitizer 漏洞自动修复

**与相近工作流的区别：** AWF-0005 告警增强与裁定止于对安全告警的结论，本工作流止于代码补丁。AWF-0003 委派式 PR 没有复现和 sanitizer 关卡，也没有两级人工筛选。
**工具变体：** `gemini-internal-pipeline` · `github-copilot-autofix` · `snyk-agent-fix`

## 步骤

1. 收集在运行单元测试时发现的 sanitizer 缺陷（内存安全等问题），涵盖 C/C++、Java 和 Go。保留测试运行中的全部信息，尤其是堆栈跟踪 [[1]](#sources)。
2. 复现并隔离每个缺陷，使测试可以重跑。根据堆栈跟踪选定要修改的文件；团队也尝试过让 LLM 来选 [[1]](#sources)。
3. 提示 LLM（Gemini）给出修复。模型依次尝试，因为不同的模型擅长修复不同类型的缺陷 [[1]](#sources)。
4. 自动测试每个候选修复：构建、重跑测试，并在修改后的代码上重跑 sanitizer。这样能挡住删除失败测试之类的假修复 [[1]](#sources)。
5. 把最佳修复交给人审阅 [[1]](#sources)。
6. 🛑 **审阅**：在第一轮人工审阅中，团队拒绝了“约 10-20%”的生成提交，原因是误报或损害代码质量 [[1]](#sources)。
7. 🛑 **签发**：剩下的提交交给代码所有者做最终验证并提交 [[1]](#sources)。

**产出：** 每个漏洞对应一个经过审阅的修复提交，由代码所有者合入。
**失败模式 → 防护：** 模型靠删除失败的测试，或把代码串行化再配一句误导性的注释来“修复”缺陷 → 在打过补丁的代码上重跑测试和 sanitizer，并在代码所有者看到之前保留一道人工筛选。审阅人可能过于信任机器给出的修复 → 告知开发者该修复由 AI 生成，并保留双重人工筛选 [[1]](#sources)。

**近期实践（2026）：**
- 验证步骤：基于 LLM 的批评工具会标出原始代码与修改后代码之间的差异，用来检查是否引入回归。智能体自行纠错，只有修复了根因、功能正确、没有回归且符合风格规范的补丁，才会交给人审阅（CodeMender）。[[2]](#sources)
- 审阅步骤：在开源变体中，人类研究员会审阅每个生成的补丁，之后才提交给上游维护者（CodeMender）。[[2]](#sources)

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。更新见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Google, AI-powered patching](https://storage.googleapis.com/gweb-research2023-media/pubtools/7563.pdf) (2024-01-05)。Gemini 流水线修复单元测试中发现的 sanitizer 缺陷；先经两道人工筛选，再由代码所有者接受。"Approximately 95% of the commits sent to code owners were accepted without discussion"; fixed "15% of sanitizer bugs"。*第一手：是；可信度：中。*
- [Google DeepMind, Introducing CodeMender: an AI agent for code security](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) (2025-10-06)。带程序分析工具和批评智能体的响应式修复智能体；人在上游提交前审阅每个补丁。"we have already upstreamed 72 security fixes to open source projects, including some as large as 4.5 million lines of code"。*第一手：是；可信度：高。*
