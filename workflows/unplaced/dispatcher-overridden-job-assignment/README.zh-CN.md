---
id: AWF-0214
name: 调度员可覆盖的派工
summary: "按技能、位置和绩效把预约工单派给技术员；调度员盯看派工板，随时覆盖并记录原因。"
deliverable: 已派工的调度板
shape: "预约工单 (在线预约 | 电话) → 为技术员打分（空闲时间、技能 / 资质、位置、绩效、潜在收入） → 派到调度板 → 🛑 sample (调度员盯看调度板并覆盖；安装和回访保持人工) → 记录覆盖原因 → 调整设置 / 技能 → 技术员获得路线"
source_hash: bcd04aaff50a
---

# 调度员可覆盖的派工

**与相近工作流的区别：** 没有特别接近的。按检查点风格最接近的是 AWF-0150（邮件转订单）这类抽检式路由工作流，但这里的交付物是技术员排班表，人是通过覆盖实时调度板来审核，而不是处理未解决的条目。
**工具变体：** `servicetitan-dispatch-pro` · `domo-roborouter`

## 步骤

1. 客户通过在线链接预约，链接显示来自产能规划的空闲时段；也可以由办公室通过电话代为预约 [[1]](#sources)。
2. 调度智能体根据技能、位置和潜在收入把每个工单派给一名技术员 [[1]](#sources)。T3 自研的 RoboRouter 会实时按空闲时间、技能（包括各地区专属资质）和按时效加权的绩效分对技术员排序 [[2]](#sources)。
3. 🛑 **抽检**：调度员盯看调度板，修改自己不同意的派工；在 Esser，覆盖比例从早期约占派工的 40% 降到约 10% [[1]](#sources)。T3 让安装和回访预约保持人工，让调度员专注于异常 [[2]](#sources)。
4. 追踪覆盖原因以改进算法；团队调整技术员的技能和设置 [[1]](#sources)[[2]](#sources)。

**产出：** 现场服务管理系统中已填好的调度板 / 技术员排班表。
**失败模式 → 防护：** 早期派错技术员 → 调度员覆盖，并调整技能和设置（40% 降到约 10%）[1]。调度员抵触运行缓慢的工具 → T3 把运行时间从 15-20 分钟缩短到 5 分钟以内 [2]。调度员离职导致经验流失 → 把决策逻辑固化下来 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [ServiceTitan, Esser Air](https://www.servicetitan.com/blog/success-story-esser-air-ai-dispatch-automation) (2026-06-22)。办公室经理讲述随着时间推移，对调度智能体的派工覆盖越来越少。"the team changed the software's assignments about 40% of the time" ... "Today that number is around 10%."。*第一手：厂商；可信度：中。*
- [Domo, T3 Services Group RoboRouter](https://www.domo.com/blog/human-loop-ai-roborouter-dispatch) (2026-06-01)。CIO 自研的调度系统，覆盖七个门店；异常仍由人处理。"they reduced runtime from 15–20 minutes down to under five minutes"。*第一手：厂商；可信度：中。*
