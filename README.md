# 数理推理（Math-Physics Reasoning）

面向数学与物理的**精准分析、新定理洞察与独立证明**技能；含数学推理、物理推理两个能力子技能。

## 入口与结构

- [SKILL.md](SKILL.md)：入口（YAML frontmatter，可直接注入 agent）。
- [agent/](agent/CLAUDE.md)：四格式提示词（CLAUDE.md / .cursorrules / instructions.md / agent_prompt.md）。
- [branch/流程/](branch/流程/流程.md)：主干七步流程；[branch](branch/branch.md) 为分支库索引。
- [scripts/](scripts/scripts.md)：五个纯标准库校验脚本（英文名）。
- [references/](references/references.md)：知识库（[知识树](references/知识树.md) + 方法目录 + 当轮来源）。
- [resistance/](resistance/resistance.md)：约束库（[红线](resistance/红线/红线.md)、[审查约束](resistance/审查约束/审查约束.md)、[双仓与可见性](resistance/双仓与可见性/双仓与可见性.md)、[降级策略](resistance/降级策略/降级策略.md)）。
- [asset/](asset/asset.md)：形式化/证明链/猜想/量纲表四份模板。
- [dependence/](dependence/dependence.md)：依赖清单（[deps.json](dependence/deps.json)）。
- [planned_tasks/](planned_tasks/README.md)：计划任务声明（到期由 SMS 调度器执行）。
- 子技能：[数学推理](数学推理/SKILL.md) · [物理推理](物理推理/SKILL.md)。

## 快速上手

1. 复制 [asset/形式化模板.md](asset/形式化模板.md) 写规格 → `formalize_check.py`。
2. 复制 [asset/证明链模板.md](asset/证明链模板.md) 写证明 → `proof_chain_check.py`。
3. 物理题加 `dimension_check.py`，数值加 `numeric_verify.py`，交付前跑 `counterexample_search.py`。
4. 按 [交付分级](branch/流程/交付分级/交付分级.md) 打 `已证 / 猜想 / 待验` 标签。

## 版本与许可

[CHANGELOG.md](CHANGELOG.md) · [CONTRIBUTORS.md](CONTRIBUTORS.md) · [LICENSE](LICENSE)（MIT）
