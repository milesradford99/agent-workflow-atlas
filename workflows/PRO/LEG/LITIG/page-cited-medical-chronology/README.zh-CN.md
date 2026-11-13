---
id: AWF-0161
name: 逐页引注的病历时间线
summary: "生成每个事件都标注页码的病历时间线；律师助理或律师逐条核对后使用。"
deliverable: 病历时间线
shape: "把病历和证词上传到案件（案件管理系统链接） → 设定案件背景（案件类型、律所摘要格式） → 对病历分类并提取带页码引注的带日期事件 → 起草时间线/证词摘要 → 🛑 review (律师助理或律师对照所引页码核对每一条) → 🛑 sign-off (律师用于索赔函、证词准备或庭前备忘录)"
source_hash: ee4eec2bf35f
---

# 逐页引注的病历时间线

**与相近工作流的区别：** AWF-0035 和 AWF-0093 是对大批文档分类或登记以供提交。本工作流的交付物是律所自己备案用的单案事实时间线，并对照所引页码逐条审阅；交付物和检查点都不同。
**工具变体：** `squary` · `supio`

## 步骤

1. 把病历、证词和案件文件上传到案件工作区，并连接案件管理系统（例如 Filevine） [[1]](#sources)。
2. 选择任务（病历时间线、证词摘要、庭前备忘录）；律所可以提供自己的摘要格式，使输出符合合伙人的写法 [[1]](#sources)[[2]](#sources)。
3. 工具提取带日期的临床事件和证词，起草结构化的时间线或摘要，每一项论断都带页码级引注 [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：律师和律师助理点击进入所引的行或页，确认上下文；「如果无法把一句陈述追溯到记录，它就不能用」 [[1]](#sources)。
5. 🛑 **签发**：律师把核实过的时间线用于索赔函、证词准备或庭审 [[1]](#sources)[[2]](#sources)。

**产出：** 案件档案中带原文链接的病历时间线或证词摘要，供索赔函起草和证词准备使用。
**失败模式 → 防护：** 事实无依据或日期有误 → 每条都带页码引注，并对照原文核对。与律所风格不符 → 上传律所自己的摘要模板。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或记者转述的说法。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Squary, Quatrini Law Group](https://www.squary.ai/blog/how-quatrini-law-group-modernized-legal-workflows-with-squary-ai) (2025-11-10)。人身伤害/残疾案律所：带页码引注的病历摘要和证词准备；引述了创始合伙人的话。注：该律所合伙人在厂商董事会任职。"up to 70% faster document reviews and 10-15 hours saved per case"。*第一手：厂商；可信度：中。*
- [Supio, GLP Attorneys](https://www.supio.com/customers/how-glp-personal-injury-attorneys-levels-the-playing-field-with-supio) (2026-09-02)。律师助理生成时间线和索赔函草稿；合伙人上传自己的摘要格式。"Catastrophic-injury medical record review, compressed from 40 hours"。*第一手：厂商；可信度：中。*
