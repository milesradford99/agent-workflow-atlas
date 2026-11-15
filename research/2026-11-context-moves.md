# 每条工作流的“一招”：全量提炼（2026-11-15）

接续 [试写记录](2026-11-context-moves-trial.md)。范围：最新来源或公开实例在 2025-11 及以后的条目（约 190 条）；更早的 50 条未提炼，列在文末。

方法同试写：只读每条的 summary、shape、“失败模式 → 防护”和“与相近工作流的区别”，没有通读全文；“一招”和分类是我的判断，数字出自条目原文。分类：放入、挡住、外验、回灌、分流、标准（定义见试写记录）。“标准”表示做法就是“AI 起草、人审阅或接手”，保留并标明。

试写的 20 条不在下表重复。

## TEC 技术

| 条目 | 分类 | 一招 |
|---|---|---|
| AWF-0192 Context-tested Slack analyst | 外验 | 不逐条审答案，改为端到端测试“上下文层”并抽看公开线程；只许用认可的数据集，答案附 SQL。 |
| AWF-0006 Governed query | 标准 | 载入指标定义，SQL 自检，分析师审阅后签发。条目没有防护一行。 |
| AWF-0123 Scheduled metric commentary | 外验 | 先用 6 个月标准差和同比判断波动是否有意义，再写评论；指标要在正确粒度上认证过。 |
| AWF-0063 Diff-proven dbt migration | 外验 | 每个模型用与生产数据的逐行 diff 证明；双向比对加不对称行数检查，抓出静默丢掉 NULL 和迟到行的增量水位。 |
| AWF-0124 Summoned dbt debugger | 挡住 | 查询用模板加上下文登记表，把编造路径导致的失败从约 25% 降到约 13%；83% 的诊断无需动作，所以修不修由人定。 |
| AWF-0191 Unprompted pipeline repair | 挡住 | 源数据问题按规则只报告不修，防止智能体用“有创意的过滤”掩盖坏数据；只读角色，沙箱里跑。 |
| AWF-0125 Multi-agent readout review | 放入 | 一行公司术语定义（内部的 DAU 指什么）消掉一整类误报；指标先预筛再交给评审智能体，整包给会把它搞晕。 |
| AWF-0064 Repo-grounded analysis | 挡住 | 只信已验证的表，未验证的表要分析师签字才能临时用；每条 Markdown 规则都配一段代码强制。 |
| AWF-0126 Calibrated-judge quality loop | 外验 | 评审模型先对照留出的人工标注校准，评分标准变了就重校；修复在固定夹具的模拟器上测。 |
| AWF-0065 Overnight experiment ratchet | 挡住 | 评测脚本只读、数据划分冻结，防止刷指标；20–30 轮后上下文会丢，用持久的实验记忆。 |
| AWF-0116 Agent-drafted PCB schematic | 外验 | 模型看不到全局（一个短接的开关引脚把 BOOT0 拉低，没被发现），所以要第二位工程师评审加上电调试；ERC 噪声多，用网表找真问题。 |
| AWF-0056 Phased preview build | 外验 | 每阶段出四视图渲染对照清单自查，再用真实切片器的反馈；布尔运算会静默失败。 |
| AWF-0058 Cited pre-screen checks | 外验 | 每项检查给出通过与否加法规条文引用，审查员逐项批准，并追踪“错放行率”；范围先限于简单建筑类型。 |
| AWF-0117 Pre-submittal plan check | 分流 | 约 4 个标记里只有 1 个是真问题，所以先由事务所分拣再改；用本所以往的审查清单做基准。 |
| AWF-0118 Zoning-rule study crew | 标准 | 逐条规则核对，建筑师签字。 |
| AWF-0059 Drawing-to-route draft | 回灌 | 班组长的修改进变更日志，反哺规则库。 |
| AWF-0057 Engineer-checked CFD run | 外验 | 边界条件错了也照样收敛（旋转壁面被留成 noSlip，叶片根本没转），所以加旋流探针和收敛交叉检查，工程师先审假设文档。 |
| AWF-0193 Unattended simulation campaign | 外验 | 求解器报成功却落在错误的平衡点，所以每次运行都做合理性检查；先用实测数据标定基础模型，再跑上千次。 |
| AWF-0151 First-pass submittal review | 标准 | 逐条要求核对并给出建议，PM 或工程师审阅。 |
| AWF-0235 Rule-set verdict review | 放入 + 外验 | 先由工程师确认通用规范与专用规范的冲突调和结果，再开始检查；每个判定带高亮证据，推翻要写理由。 |
| AWF-0190 Spec-to-submittal register | 标准 | 抽取要求、起草登记表，项目工程师逐行核对。 |
| AWF-0188 Scheduled vuln-fix PRs | 放入 | 每个代码库存自己的依赖模式、文件位置、构建命令和例外；工单、标签、分支和部署状态让重跑无害。 |
| AWF-0068 Slack IT request agent | 挡住 | 谁有权批准写在工作流或策略里，不让模型决定；置信阈值用数周真实流量来调。 |
| AWF-0066 Chat-to-IaC change | 外验 | 评审对象是 plan 输出而不是 HCL diff：看着很小的 diff 可能会替换或销毁资源。 |
| AWF-0186 Plan-verified drift fixes | 放入 | 一张导入 ID 格式表把 ID 错误从 13 个降到 5 个；仍有 12 个弱方案通过了干净的 plan，只被评审人抓到。 |
| AWF-0005 Alert enrich and adjudicate | 标准 | 富化、裁决，良性的自动关闭，其余转二线，每周抽检。条目没有防护一行。 |
