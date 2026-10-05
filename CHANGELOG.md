# CHANGELOG

本项目遵循 Keep a Changelog 与语义化版本。

## [0.1.0] - 2026-10-05

### 新增

- 初始化：工作空间、MIT [LICENSE](LICENSE)、[planned_tasks/](planned_tasks/README.md)
  （README + template）、[agent/](agent/CLAUDE.md) 四格式提示词。
- 主干流程七步：[形式化](branch/流程/形式化/形式化.md) →
  [建模求解](branch/流程/建模求解/建模求解.md) →
  [猜想生成](branch/流程/猜想生成/猜想生成.md) →
  [证明策略](branch/流程/证明策略/证明策略.md) →
  [证明链](branch/流程/证明链/证明链.md) →
  [自检回炉](branch/流程/自检回炉/自检回炉.md) →
  [交付分级](branch/流程/交付分级/交付分级.md)。
- 能力子技能：[数学推理](数学推理/SKILL.md)、[物理推理](物理推理/SKILL.md)
  （归属判定见 [双仓与可见性](resistance/双仓与可见性/双仓与可见性.md)）。
- 脚本：`formalize_check.py`、`proof_chain_check.py`、`dimension_check.py`、
  `numeric_verify.py`、`counterexample_search.py`（正/负例均已实测）。
- 知识库：[知识树](references/知识树.md)、[证明方法目录](references/证明方法目录.md)、
  [量纲分析与π定理](references/量纲分析与π定理.md)、
  [猜想生成与反例排查](references/猜想生成与反例排查.md)、
  [经验查询记录](references/经验查询记录.md)。
- 约束：[红线](resistance/红线/红线.md)、[审查约束](resistance/审查约束/审查约束.md)、
  [降级策略](resistance/降级策略/降级策略.md)。
- 依赖：[deps.json](dependence/deps.json)（4 条，均附 `source_url`）。
- 计划任务：`pt-数理推理-anchor-refresh`（季度锚点复核，由 SMS 调度器执行）。

### 已知限制

- 百科类联网来源本轮不可达（详见 [经验查询记录](references/经验查询记录.md)）。
- 反例搜索为网格脚手架，非定理证明器。
