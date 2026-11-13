---
id: AWF-0129
name: AI 模糊测试目标挖掘
summary: "自动编写并运行模糊测试目标，将崩溃分类整理成漏洞报告；分类由人确认，确认的漏洞交维护者修复。"
deliverable: 漏洞报告
shape: "为项目建立索引 (函数、类型、交叉引用、单元测试) → 每个目标函数：(起草模糊测试目标 ⟲ 修复编译错误) → (短时运行 ⟲ 修复运行时错误) → 在模糊测试基础设施上长时间运行 → 每个崩溃：分诊驱动 bug | 项目 bug → 🛑 review (人工确认分诊) → 向维护者报告 → 🛑 handoff (维护者修复)"
source_hash: 0e928c5d337c
---

# AI 模糊测试目标挖掘

**与相近工作流的区别：** AWF-0067 Sanitizer 缺陷自动修补：AWF-0067 从已知的 sanitizer 发现出发，交付由代码负责人签发的补丁。本工作流则是发现新的 bug：产出是模糊测试 harness 和已分诊的漏洞报告，关卡是分诊审阅以及向外部维护者的接手。
**工具变体：** `oss-fuzz-gen` · `clusterfuzz`

## 步骤

1. 自动为每个项目建立索引：函数、类型定义、交叉引用和已有的单元测试。这给提示词提供了项目特有的上下文，减少幻觉。[[1]](#sources)
2. 针对每个目标函数，LLM 起草一个模糊测试目标。编译错误交回给 LLM，直到能编译通过。[[1]](#sources)
3. 短时运行该目标。如果它立即崩溃（是设置错误，而不是项目 bug），由 LLM 修复。[[1]](#sources)
4. 把修正后的目标在 ClusterFuzz 上长时间运行。[[1]](#sources)
5. 对每个崩溃，LLM 拿到堆栈跟踪、目标源码和项目代码，并附上分析，把它标为 'bug in fuzz driver' 或 'bug in project'。[[1]](#sources)
6. 🛑 **审阅**：报告发出前，仍由人审阅分诊结果。去掉这一步被列为未来目标。[[1]](#sources)
7. 🛑 **接手**：确认的漏洞交给项目维护者修复（OpenSSL 的 CVE 于 9 月 16 日报告，10 月 16 日修复）。[[1]](#sources)

**产出：** 加入项目 OSS-Fuzz 配置的新模糊测试目标，以及发给维护者的已确认漏洞报告。
**失败模式 → 防护：** 目标中出现幻觉的 API → 带索引的项目上下文加编译修复循环。把驱动 bug 误当成真漏洞 → LLM 分诊，并在报告前由人审阅。把覆盖率提升误当成安全 → 即使对已做过模糊测试的代码，也持续生成新目标。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Google, Leveling Up Fuzzing](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html) (2024-11-20)。272 个 C/C++ 项目，新增覆盖 370k+ 行代码；其中包括 OpenSSL 中的 CVE-2024-9143。"This led to the discovery of 26 new vulnerabilities"。*第一手：是；可信度：高。*
