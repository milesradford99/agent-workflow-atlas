---
id: AWF-0075
name: 代码 PR 文档草稿
summary: "根据代码 PR 起草文档 PR；代码作者核对准确性，文档团队审查文风后合并。"
deliverable: 文档 PR
shape: "代码 PR 已打开 → 智能体起草对用户文档、开发者文档及各版本分支的更新 → 以草稿形式打开文档 PR → (代码 PR 有改动 ⟲ 智能体更新草稿) → 代码 PR 已合并 → 将文档 PR 标为就绪 → 🛑 review (代码作者：准确性) → 🛑 review (文档团队：文风) → 合并"
source_hash: 4386448747fe
---

# 代码 PR 文档草稿

**与相近工作流的区别：** AWF-0003 委派式 PR 是让智能体根据工单修改代码。这里的输入是代码 PR，输出是文档 PR，两位审阅人各把关不同的方面。
**工具变体：** `promptless` · `github-agentic-workflows` · `ona-automations` · `biel-nova` · `claude-code-doc-check-skill`

## 步骤

1. 触发：开发者在代码仓库上打开一个 pull request。智能体（Promptless）起草对用户文档和开发者文档的相应更新，并覆盖两者各自的版本分支 [[1]](#sources)。
2. 代码 PR 尚未合并时，文档 PR 保持为草稿。如果代码 PR 在评审期间有改动，智能体会同步更新文档草稿 [[1]](#sources)。
3. 代码 PR 合并后，文档 PR 自动标为可供评审 [[1]](#sources)。
4. 🛑 **审阅**：编写该代码变更的开发者检查草稿是否与自己构建的内容一致。有人就发现过草稿描述了一个已不存在的按钮 [[1]](#sources)。
5. 🛑 **审阅**：教育团队（Education Team）像对待任何文档贡献一样检查语法、措辞和文风，然后合并 [[1]](#sources)。
6. 推广关卡：项目起初只是在仪表盘上给出建议，由团队手动转成 PR；直到草稿持续符合风格指南之后，才切换为自动生成 PR [[1]](#sources)。

**产出：** 已合并到文档仓库的文档 PR，与代码发布保持同步。
**失败模式 → 防护：** 文档描述了过时的界面或行为 → 合并前由代码作者审阅。文风漂移 → 由文档团队审阅，并且只在经过有人监督的试运行之后才启动自动化。

**近期实践（2026）：**
- 步骤 1（触发）：一些团队把合并后的改动攒成每天一个文档 PR，而不是为每个代码 PR 配一个，因为按每次提交运行太嘈杂（Ona）。另一些团队先由撰写人触发一份分诊报告，只为被标记的 PR 起草文档（NetFoundry doc-check）。[[3]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例补充于 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Mautic, How we keep docs up to date automatically with AI](https://mautic.org/?p=26025) (2026-09-03)。这个开源项目借助智能体起草的文档 PR，缩小了文档相对发布的滞后。约 4 个月内合并了 129 个 Promptless 文档 PR；从代码合并到文档合并的间隔为 27 天，此前是 98 天。*第一手：是；可信度：高。*
- [Ona (Siddhant Khare), How we automated writing docs with an Ona Automation](https://ona.com/stories/docs-automation) (2026-02-12)。每天早上 8 点，智能体读取代码仓库和文档仓库过去 24 小时的 diff，打开一个文档草稿 PR。"Reviewing a draft takes about 30 seconds. Writing that same page from scratch would have been 30 minutes."。*第一手：是；可信度：中。*
- [Biel.ai (David Garcia), Our AI teammate keeps our docs up to date](https://blog.techdocs.studio/p/our-ai-teammate-keeps-our-docs-up) (2026-10-08)。智能体检查 main 上已合并的 PR/提交，打开后续的文档 PR（附截图）；撰写人在 PR 中审阅。没有数量统计；一个示例 PR 补上了两处缺失的 React 组件章节。*第一手：是；可信度：中。*
- [NetFoundry, Inside NetFoundry docs: Streamline doc freshness with AI](https://blog.openziti.io/streamline-doc-freshness-with-ai) (2026-03)。由撰写人运行的 doc-check 技能，把跨仓库已合并的 PR 分诊为需要处理/已覆盖/已跳过，并按指令起草。"5 PRs analyzed · 2 need doc work · 1 already covered · 2 skipped (internal)"; "a 20-to-1 engineer-to-writer ratio"。*第一手：是；可信度：高。*
