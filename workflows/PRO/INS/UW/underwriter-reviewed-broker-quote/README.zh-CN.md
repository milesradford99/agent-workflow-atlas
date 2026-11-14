---
id: AWF-0155
name: 核保员复核的经纪人报价
summary: "为范围内的续保起草含定价的经纪人报价邮件；发送前由核保员审核。"
deliverable: 经纪人报价邮件
shape: "经纪人投保件 (续保，范围内险种) → 范围检查 → Gemini 评估风险 → 将定价 + 数据填入经纪人邮件 → 🛑 review (核保员) → 发送报价"
source_hash: e6ecfc76b343
---

# 核保员复核的经纪人报价

**工具变体：** `gemini-vertex`

## 背景

专业商业保险大多通过经纪人销售：经纪人把某项风险的细节发给保险公司，请对方报价。保单已在生效、即将续保时，核保员（决定承保条件和价格的人）仍要重新审视风险，并给经纪人发一份报价。细节大多与去年相同，但阅读投保件、对照保险公司的规则核查并定价这些工作，占用了本可用来处理更难风险的时间。这里由智能体检查这笔续保是否落在一个很窄的范围内，评估风险，并把价格和其他数据填进发给经纪人的报价邮件。核保员阅读这封邮件，决定是否发出，因为报价意味着保险公司对价格的承诺，而智能体只被允许处理简单的案件。

**术语：**
- **经纪人（broker）**：替客户向保险公司安排风险并请对方报价的中介。
- **核保员（underwriter）**：决定是否承接风险以及价格的人。
- **续保（renewal）**：保单此前已经承保，现在为下一期再次报价。
- **报价（quote）**：保险公司以某一价格提供保障的书面要约。
- **主承保（lead underwriting）**：为同一风险确定条款和价格，其他保险公司在此基础上跟进。
- **破坏与恐怖主义险（sabotage and terrorism insurance）**：为企业承保此类行为造成的财产损失的专业保险。
- **范围检查**：检验该风险是否属于允许智能体处理的类型：这里指险种、续保状态和地域。
- **都会区（metro area）**：这里指纽约和芝加哥城区，被排除在范围之外。

## 用智能体搭建

**形态：** `service`。经纪人的投保件到达时没有人守在键盘前，核保员只看到成品草稿邮件。曾与 `skill` 比较过，因为每份报价都有人审阅；但运行是在投保件到达时启动，不是应核保员的请求启动。

**需要：** 对投保件收件箱和上一年保单记录的读取权限；写成脚本可检查的文件的范围规则（险种、续保状态、地区、排除项）；作为智能体可调用但不能修改的脚本或连接器提供的保险公司定价方法或费率工具；一份邮件模板；让核保员看到邮件的草稿箱或队列。不要给智能体任何向经纪人发邮件的工具。

| 步骤 | 搭建方式 |
|---|---|
| 经纪人投保件 (续保，范围内险种) → 范围检查 | 云端定时任务，或你自己的程序启动 `claude -p` 或 Agent SDK 程序，取走每份新到的投保件。由脚本套用范围规则；范围外的件留给核保员，并附说明原因的备注。 |
| Gemini 评估风险 | 一个 skill 读取投保件和上一年记录，对照保险公司的核保规则写出风险评估，每一点都注明出处。 |
| 将定价 + 数据填入经纪人邮件 | skill 调用定价脚本，把价格和其他数据填进邮件模板，存为草稿。 |
| 🛑 review (核保员) → 发送报价 | 见“检查点”。 |

**检查点：** `review`：运行结束时把草稿邮件和风险评估放进核保员的队列。智能体没有发送工具，并且由 `PreToolUse` 钩子拒绝任何发送邮件的调用，所以由核保员修改草稿后自己发出，或者不发。范围检查是脚本而不是一句指示，所以智能体无法为范围外的风险定价。

**与来源相比：** 来源出自 2024-08 至 2026-11。Hiscox 用的是 Google Cloud 的 Gemini 模型和自家的内部 AI 工具（Hailo），没有报道提示词或定价的细节；这套搭建方式用通用智能体，模型选择与设计无关。2026 年的交易声明报道范围已扩展到中型市场风险，且破坏与恐怖主义工具直接对接经纪人的平台；这套搭建方式没有做到这些。定价方法是保险公司自己的，所以智能体只调用它，不重现它。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. Hiscox 把范围限定为美国和加拿大现有的破坏与恐怖主义险种的续保，不含纽约和芝加哥都会区 [[1]](#sources)。
2. 系统用 Gemini 结合 Hiscox 的内部 AI 工具（Hailo）评估范围内的风险 [[1]](#sources)。
3. 系统生成发给经纪人的邮件，定价和其他数据已预先填好 [[1]](#sources)。
4. 🛑 **审阅**：邮件在发给经纪人之前处于 'ready for underwriter review' 状态 [[1]](#sources)。

**产出：** 经核保员审核后发给经纪人的含定价报价邮件。
**失败模式 → 防护：** 范围外或复杂的风险被自动定价 → 范围按险种、续保状态和地域限定；复杂风险仍由核保员处理。

**近期实践（2026）：**
- 步骤 1：到 2026 年，范围已扩展到中型市场风险，破坏与恐怖主义工具直接对接经纪人的平台（Hiscox 2026 年第一季度交易声明）。[[2]](#sources)
**与相近工作流的区别：** AWF-0051 受管控答案库的回复草稿（Governed-library response draft）是根据已批准的答案库回答问卷。本工作流的产出是针对单个风险的带定价报价，由一次核保员审核把关。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Hiscox, GenAI lead underwriting model goes live](https://www.hiscoxgroup.com/news/press-releases/2024/12-08-24) (2024-08-12)。在伦敦市场上线；与经纪人 WTW 承保了第一单风险。"an insurance quote in a matter of minutes"。*第一手：是；可信度：高。*
- [Reinsurance News, Hiscox CFO Cooper on AI adoption](https://www.reinsurancene.ws/ai-adoption-drives-productivity-growth-and-opens-business-opportunities-hiscox-cfo-cooper/) (2025-11-07)。增强型主承保已在破坏与恐怖主义业务中规模化；正扩展到中型市场财产险。"from a turnaround time of about three days to certainly around three minutes"；"around two-thirds of the sabotage and terrorism business now subject to the augmented underwriting process"。*第一手：访谈；可信度：高。*
- [Hiscox Group, Q3 2026 trading statement](https://www.hiscoxgroup.com/news/press-releases/2026/03-11-26) (2026-11-03)。美国经纪业务线实现 AI 从投保到报价，并在零售业务中推广。"improved our speed to quote by around 75% in terrorism and architects and engineers"。*第一手：是；可信度：高。*
