---
id: AWF-0187
name: 紫队式检测规则构建
summary: "蓝队和红队智能体把威胁报告转化为经实验室验证的检测规则；分析师逐条批准后合并。"
deliverable: 检测规则包
shape: "威胁文章或 PoC 仓库 → 蓝队智能体: 候选检测 + 狩猎查询 → 红队智能体: 攻击计划 (若无 PoC 则自行编写) → 实验室以生产安全栈自动部署 → 每个 变体: 引爆 → (对照实验室 + 运营遥测验证 ⟲ 优化逻辑) → Sigma 或 Python 分析规则 + 证据包 → 🛑 review (分析师验证、批准或修改) → 合并到检测仓库"
source_hash: 949a4b0e8bcf
---

# 紫队式检测规则构建

**与相近工作流的区别：** AWF-0128 引爆并确认检测（Detonate-and-confirm detections）从已有规则出发，用攻击模拟和定期健康检查来验证它。这里的输入是威胁情报，产出是由蓝队/红队智能体循环构建的新检测逻辑，最后只有一次分析师批准。AWF-0005 是对告警分诊，不创建规则。
**工具变体：** `claude-opus` · `claude-mythos` · `sigma` · `proxmox` · `ansible`

## 步骤

1. 摄入一个威胁来源：文章、博客、事件报告、分析师描述或 PoC 仓库 [[1]](#sources)。
2. 蓝队智能体：提出一个或多个候选检测，每个都附有用白话写的逻辑描述和一条狩猎查询 [[1]](#sources)。
3. 红队智能体：编写攻击计划，涵盖要引爆的基础设施、软件和 PoC。如果没有公开的 PoC，它会尝试自行创建 [[1]](#sources)。
4. 实验室根据计划自动部署（例如 Proxmox 靶场加 Ansible），并配备与生产环境相同的安全栈。可能会创建多个环境变体 [[1]](#sources)。
5. 用该技术的多个变体执行攻击。对照实验室模拟和真实运营数据验证检测逻辑，反复进行，直到该活动能被可靠检出且误报降到最低 [[1]](#sources)。
6. 把结果转换为 Sigma（简单情形）或 Python 分析规则（复杂情形），附带过滤条件、调优逻辑和文档，并与支撑证据和验证结果一起打包 [[1]](#sources)。
7. 🛑 **审阅**：分析师在检测规则合并进仓库之前验证、批准或修改它们 [[1]](#sources)。

**产出：** 带验证证据、可用于生产的检测规则，经分析师批准后合并到检测仓库。
**失败模式 → 防护：** 检测只能抓到原样的 PoC → 每条规则测试 5 个以上的技术变体，包括进程内规避，以找到持久的行为指标。误报泛滥 → 在评审前用真实运营遥测验证。AI 自作主张 → 运营决策由分析师掌握。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Canadian Centre for Cyber Security, used frontier AI to accelerate detection engineering](https://www.cyber.gc.ca/en/guidance/canadian-centre-cyber-security-used-frontier-ai-accelerate-detection-engineering) (n.d., 2026)。Exploitarium PoC 测试用例经蓝队/红队智能体循环，产出经分析师审阅的规则。"In total, 8 new production detection rules were created from the above test case, with more than 5 variants of each technique tested"。*第一手：是；可信度：高。*
