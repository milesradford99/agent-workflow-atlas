---
id: AWF-0067
name: Sanitizer 漏洞自动修复
summary: "为 Sanitizer 发现的缺陷生成并测试修复提交；安全工程师筛选，代码所有者验证后提交。"
deliverable: 安全修复提交
shape: "单元测试中发现 sanitizer 问题 → 复现并隔离（堆栈跟踪、目标文件）→ 每个模型：生成修复 → 构建 + 重跑测试 + 重跑 sanitizer → 选出最佳修复 → 🛑 review (安全工程师筛选) → 🛑 sign-off (代码所有者) → 提交"
source_hash: f6db620f5221
---

# Sanitizer 漏洞自动修复

**工具变体：** `gemini-internal-pipeline` · `github-copilot-autofix` · `snyk-agent-fix`

## 背景

Sanitizer 是在软件运行时发现不安全行为的测试工具，例如访问已经失效的内存。安全工程师需要复现故障、找到原因，再提出不会破坏其他行为的代码修改。大型项目会积累这类发现，难以立即逐一处理。智能体可以根据故障记录准备候选补丁并测试。候选仍由安全工程师筛选，最终提交由代码负责人完成，因为通过某个测试并不能证明修改保留了程序原有意图。

**术语：**
- **Sanitizer / 内存安全**：运行期间的缺陷检测器，以及防止无效访问程序内存的规则。
- **单元测试 / 堆栈跟踪**：针对一小段代码的测试，以及出错时记录的函数调用链。
- **LLM**：大语言模型，这里用来提出代码修改。
- **回归（regression）**：修改破坏了原本正常的行为。
- **误报 / 代码负责人**：不应按所提修复处理的报告，以及负责相关代码的开发者。
- **数据竞争 / 串行化**：并发访问相互冲突，以及强制让工作顺序执行。

## 用智能体搭建

**形态：** `service`。问题进入队列，经过测试的候选交给人工筛选，不要求人逐次启动运行。

**需要：** 获得授权的源码；带复现输入和堆栈跟踪的 sanitizer 报告；隔离的构建与测试脚本；候选存储和私密审阅队列。未披露漏洞及专有代码应留在批准的系统中。保留受保护的测试副本，不提供向上游提交或合并的工具。

| 步骤 | 搭建方式 |
|---|---|
| sanitizer 问题 → 复现并隔离 | `claude -p` (headless) 取出队列中的问题。Skill 复现问题并记录受影响源码与测试命令。 |
| 每个模型：生成修复 | Skill 在独立工作区准备候选 diff；模型比较可选，需要分别配置提供方。 |
| 构建 + 重跑测试 + 重跑 sanitizer → 选出最佳修复 | Skill 运行确定性检查；只读 Subagent 检查 diff 是否删除测试、削弱检查或引入回归。Hook 阻止修改受保护的测试。 |
| 🛑 review → 🛑 sign-off → 提交 | 候选与测试日志进入安全审阅队列；获批候选再交给代码负责人。 |

**检查点：** `review`：安全工程师查看复现、diff、未改动的测试、sanitizer 输出及剩余不确定性。`sign-off`：只有代码负责人能提交最终修改；智能体没有上游写入凭据。构建通过只代表候选可以进入这些审阅环节。

**与来源相比：** 来源出自 2024-01 至 2025-10；报告落地页、PDF 和 CodeMender 文章已于 2026-11 打开。检索发现 [Google Cloud 托管 CodeMender 预览公告](https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender?hl=en)，出自 2026-07，已于 2026-11 打开，其中仍保留开发者对生成补丁的审阅和批准。现在通用智能体可以用 Skill 承载编辑与测试流程，不再必须搭建早期逐次调用模型的定制流水线；真正的 sanitizer 与构建环境仍然必需。本设计不要求访问 Google 内部流水线，也不宣称等同于 CodeMender 的分析工具。PDF 正文所印日期与现有引用采用的创建日期不同，需要另做证据审阅。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 系统收集在运行单元测试时发现的 sanitizer 缺陷（内存安全等问题），涵盖 C/C++、Java 和 Go。保留测试运行中的全部信息，尤其是堆栈跟踪 [[1]](#sources)。
2. 系统复现并隔离每个缺陷，使测试可以重跑。根据堆栈跟踪选定要修改的文件；团队也尝试过让 LLM 来选 [[1]](#sources)。
3. 流水线提示 LLM（Gemini）给出修复。模型依次尝试，因为不同的模型擅长修复不同类型的缺陷 [[1]](#sources)。
4. 流水线自动测试每个候选修复：构建、重跑测试，并在修改后的代码上重跑 sanitizer。这样能挡住删除失败测试之类的假修复 [[1]](#sources)。
5. 流水线把最佳修复交给人审阅 [[1]](#sources)。
6. 🛑 **审阅**：在第一轮人工审阅中，团队拒绝了“约 10-20%”的生成提交，原因是误报或损害代码质量 [[1]](#sources)。
7. 🛑 **签发**：剩下的提交交给代码所有者做最终验证并提交 [[1]](#sources)。

**产出：** 每个漏洞对应一个经过审阅的修复提交，由代码所有者合入。
**失败模式 → 防护：** 模型靠删除失败的测试，或把代码串行化再配一句误导性的注释来“修复”缺陷 → 在打过补丁的代码上重跑测试和 sanitizer，并在代码所有者看到之前保留一道人工筛选。审阅人可能过于信任机器给出的修复 → 告知开发者该修复由 AI 生成，并保留双重人工筛选 [[1]](#sources)。

**近期实践（2026）：**
- 验证步骤：基于 LLM 的批评工具会标出原始代码与修改后代码之间的差异，用来检查是否引入回归。智能体自行纠错，只有修复了根因、功能正确、没有回归且符合风格规范的补丁，才会交给人审阅（CodeMender）。[[2]](#sources)
- 审阅步骤：在开源变体中，人类研究员会审阅每个生成的补丁，之后才提交给上游维护者（CodeMender）。[[2]](#sources)

**与相近工作流的区别：** AWF-0005 告警增强与裁定止于对安全告警的结论，本工作流止于代码补丁。AWF-0003 委派式 PR 没有复现和 sanitizer 关卡，也没有两级人工筛选。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。更新见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Google, AI-powered patching](https://storage.googleapis.com/gweb-research2023-media/pubtools/7563.pdf) (2024-01-05)。Gemini 流水线修复单元测试中发现的 sanitizer 缺陷；先经两道人工筛选，再由代码所有者接受。"Approximately 95% of the commits sent to code owners were accepted without discussion"; fixed "15% of sanitizer bugs"。*第一手：是；可信度：中。*
- [Google DeepMind, Introducing CodeMender: an AI agent for code security](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) (2025-10-06)。带程序分析工具和批评智能体的响应式修复智能体；人在上游提交前审阅每个补丁。"we have already upstreamed 72 security fixes to open source projects, including some as large as 4.5 million lines of code"。*第一手：是；可信度：高。*
