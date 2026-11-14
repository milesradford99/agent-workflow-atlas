---
id: AWF-0151
name: 施工提交件初审
summary: "将施工提交件与规格书及既往批复比对并给出处理建议；项目经理或工程师复核，最终由审批责任人批准。"
deliverable: 提交件审查回复
shape: "收到提交件 → 匹配适用的规格章节 + RFI + 既往批复 → 逐项核对要求 → 标出不合规 / 缺失项 → 结构化建议 → 🛑 review (PM/PE 确认并修改) → 回复分包商 | 转交建筑师 → 🛑 sign-off (建筑师/责任工程师作出处置)"
source_hash: aba04f36e902
---

# 施工提交件初审

**工具变体：** `trunk-tools` · `procore-datagrid` · `buildsync`

## 背景

在施工项目上，承包商不能想装什么就装什么：每种产品、每个做法、每张加工详图，都必须在订货或施工之前向设计方证明，自己打算用的东西符合规格书。这份材料叫提交件——产品样本、数据表、检测证书、加工图——中型商业项目往往有几百到两千份，每份都带合同约定的审查时限。承包商的项目工程师拿它对照对应的规格章节、对照此前 RFI 里已经给出的答复、对照项目上早先批准过的产品，然后要么退回分包商整改，要么转给建筑师盖章：批准、有条件批准，或退回修改再报。时间都花在"读"上，而漏掉的一处偏差，之后会在现场变成拆了重装。在这里，一份提交件到达就立刻跑一次检查：找到适用的规格章节，把提交文件逐条对着要求检验，再把建议放进项目工程师的队列。工程师确认或改写建议，而带有合同效力的处置，仍然由建筑师或责任工程师在自己的系统里做出。

**术语：**
- **提交件（submittal）**：承包商在采购或施工之前提交、用于证明产品或做法符合规格书的文件。
- **规格章节（specification section）**：项目规格书中管某一专业或产品的编号章节，按标准的分类编号编排。
- **加工详图（shop drawing）**：加工厂画出的、说明构件实际如何制作与安装的图纸。
- **RFI**（request for information，信息请求）：承包商提出的正式问题，其答复可能改变提交件必须证明的内容。
- **处置（disposition）**：审阅人盖的章：批准、有条件批准，或退回修改再报。
- **退回修改再报（revise and resubmit）**：把整份材料打回整改的答复，代价是完整的一轮周期。
- **PM / PE**：承包商的项目经理与项目工程师，日常跑提交件的人。
- **责任工程师（engineer of record）**：以执业印章对设计负责的工程师；只有他或建筑师才能对提交件作出处置。

## 用智能体搭建

**形态：** `service`。材料按各自的节奏从许多分包商那里到达，检查必须在没人按下开始的情况下跑；项目工程师从队列里逐份看到建议并作答。

**需要：** 对项目管理平台的读权限——提交件台账、现行规格书与补充文件、RFI 台账、既往批准记录，通过 MCP 连接器取得；每个规格章节的要求文本，形式要能被引用；按"材料编号 + 版本"存放每次结果的地方；项目工程师的队列。智能体不能有把材料退回分包商的工具，也不能有盖章处置的工具：这两个都是合同行为。

| 步骤 | 搭建方式 |
|---|---|
| 收到提交件 | 监视平台提交件模块，或用一个 webhook，每份材料每个版本启动一次运行；重新报审是新的一次运行，同时读取上一版。 |
| 匹配适用的规格章节 + RFI + 既往批复 | 从材料自带的规格引用出发；检索步骤取出该章节、所有答复涉及该章节的 RFI，以及同一章节早先批准过的产品。 |
| 逐项核对要求 → 标出不合规 / 缺失项 | 按要求分组，每组一个 Subagent，只给它该组的条款和提交页面，返回合规、部分合规或不合规，并注明条款与所读页码。 |
| 结构化建议 | Skill 汇总合规对照表、建议和未决问题，写在工程师会去找的位置。 |
| 🛑 review（PM/PE 确认并修改）→ 回复分包商 | 运行以"表格进入工程师队列"结束；退回分包商是工程师在平台上持有的权限，本次运行没有。 |
| 转交建筑师 → 🛑 sign-off（建筑师/责任工程师作出处置） | 由工程师带着自己的修改和合规对照表转交；处置章由建筑师或责任工程师在平台上盖，落在智能体所有工具之外。 |

**检查点：** `review`：运行不能对外发出任何东西。它的产出只是工程师队列里的一张表，而真正要紧的两个平台动作——把材料退回分包商、带着建议转交建筑师——都是它没有的权限。`sign-off`：处置是执业行为，所以本搭建方式不给智能体盖章、批准或归档的工具；它同时把合规对照表附着在材料上，让建筑师看得到查了什么、什么没查。

**与来源相比：** 来源出自 2025-09 到 2026-11-02：厂商案例研究、两篇行业媒体访谈，以及一份平台案例研究。厂商在 2026 年对这类软件做的横向比较本月已打开；各份案例研究本轮没有重新打开。此后有这些变化：触发方式。那份比较指出，[有一款产品在材料上传时自动开始审查，而其他产品要等人手动触发](https://trunktools.com/blog/best-construction-submittal-software)，并且各产品覆盖的提交件类型差别很大——这一点在这里很要紧，因为只有当触发是自动的、覆盖的类型又包含项目实际会提交的东西时，无人值守的服务形态才值得跑。所有人提到的两个人工动作都没有变：最终判断仍由人做，处置仍由建筑师盖章。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 提交件到达时，将其与项目规格书、相关的 RFI 回复和此前已批准的提交件比对 [[1]](#sources)。
2. 标出不合规的条目，并 'in minutes' 生成结构化建议 [[1]](#sources)。
3. 🛑 **审阅**：助理项目经理或项目工程师依据分析采取行动，并回复分包商 [[1]](#sources)。
4. 🛑 **签发**：批准权仍在责任审批人手中；Procore 的智能体 'require human consent before actions are finalized' [[2]](#sources)。

**产出：** 经过修正的提交件送交建筑师，避免被退回要求修改并重新提交（Revise and Resubmit）。
**失败模式 → 防护：** 漏检的不合规问题到现场才暴露 → 逐项要求核对。规格书已被取代 → 从项目管理系统读取当前的项目文件集。

**与相近工作流的区别：** AWF-0058 带引用的预审检查（Cited pre-screen checks）是对许可申请人的图纸集做规范合规预审。本工作流则是承包商对照项目规格书，检查分包商的产品资料和施工详图。产出不同（提交件审查回复），审批人也不同（先是 PM，再是责任建筑师）。
**近期实践（2026）：**
- 逐项核对要求：把每一项标为合规、部分合规或不合规，让审阅人集中处理例外项（ENR 2026-06-17）。
- 回复分包商：返还 AI 报告和自动标注，并附上审阅人的指示；转交建筑师时，附上合规对照表（BuildSync；ENR 2026-06-17）。[[5]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Trunk Tools, Cleveland Construction](https://trunktools.com/content/customers/pdfs/cleveland.pdf) (n.d.)。电气提交件当天完成；引述助理 PM 的话。"estimated savings of 790+ hours and $60K+ across four projects"。*第一手：厂商；可信度：中。*
- [ENGtechnica, Procore/Datagrid](https://engtechnica.com/procore-embeds-datagrid-ai-agents-in-construction-workflows/) (2026-05-22)。Level 10 Construction 自建了提交件智能体。"We ran 10 submittal reviews in an hour using our agent, easily saving 12 hours of work"。*第一手：访谈；可信度：中。*
- [Bryan Gottlieb, ENR, Trunk Tools Launches Cortex AI Platform](https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings) (2026-06-17)。Cleveland Construction 的高级副总裁：提交件先经 AI 处理再由员工审阅；合规对照表发送给建筑师。"reducing average submittal cycle times from 55 days to 13 days"；"from roughly two hours to less than 10 minutes"。*第一手：访谈；可信度：中。*
- [Jeff Yoders, ENR, Gilbane Rolls Out Trunk Tools AI Agents Across Its Jobsites](https://www.enr.com/articles/61435-gilbane-rolls-out-trunk-tools-ai-agents-across-its-jobsites) (2025-09-26)。30 个 Gilbane 项目；多数收到的提交件在送交建筑师前就被标为不合规。"review more than 2,000 submittals"；"72% of submittals received ... were non-compliant, 25% partially compliant, and only 3% fully compliant"。*第一手：否；可信度：中。*
- [Trunk Tools, Torcon case study](https://trunktools.com/customers/case-study-how-torcon-project-team-save-time-reduce-risk/) (2026-03-12)。两个项目的试点；为项目工程师做提交件合规审查。"64 submittal reviews completed with ~43.5 minutes saved per review (~46 hours)"。*第一手：厂商；可信度：中。*
- [BuildSync, Monteith Construction: Blueprints to Bedside](https://buildsync.ai/case-studies/blueprints-to-bedside) (n.d.)。PM 在每份产品资料提交件提交后，立即在 Procore 内运行 AI 审查。"I spend 70% less time reviewing submittals"；"Our failure rate has dropped by around 50%"。*第一手：厂商；可信度：中。*
