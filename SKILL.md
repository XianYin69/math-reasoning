---
name: 数理推理
version: 0.1.0
description: >
  面向数学与物理的精准分析、新定理洞察与独立证明：先形式化（对象/假设/记号/目标命题）
  再建模求解，显式选择证明策略，写出严格证明链并自检；输出区分「已证/猜想/待验」。
  含数学推理、物理推理两个子技能。
license: MIT
metadata:
  category: science
---

# 数理推理

使用 `数理推理` skill 来完成用户请求。

## 工作原则

1. **先形式化后求解**：明确对象、假设、记号、目标命题，再建模；每步推导可追溯。
2. **禁止跳步**：不得写「显然」「易见」「同理可得」替代推导；每步须给依据（公理/引理/定理/前提编号）。
3. **数值可校**：数值结果必附误差界、有效位数与数量级校验。
4. **分级交付**：结论标注 `已证 / 猜想 / 待验`；自检不过则回炉，不交付。

## 执行路径

[形式化](branch/流程/形式化/形式化.md) → [建模求解](branch/流程/建模求解/建模求解.md) →
[猜想生成](branch/流程/猜想生成/猜想生成.md) → [证明策略](branch/流程/证明策略/证明策略.md) →
[证明链](branch/流程/证明链/证明链.md) → [自检回炉](branch/流程/自检回炉/自检回炉.md) →
[交付分级](branch/流程/交付分级/交付分级.md)

主干索引：[branch/流程/](branch/流程/流程.md)；兜底约束：[resistance/](resistance/resistance.md)

## 子技能

- [数学推理](数学推理/SKILL.md)：结构/代数/分析/组合的猜想与证明。
- [物理推理](物理推理/SKILL.md)：量纲、对称与守恒、估算与精确解互校。

## 可用工具（scripts/）

`formalize_check.py`、`proof_chain_check.py`、`dimension_check.py`、`numeric_verify.py`、
`counterexample_search.py`——清单见 [scripts](scripts/scripts.md)。

## 知识·依赖·计划任务

[references/](references/references.md) · [dependence/deps.json](dependence/deps.json) ·
[planned_tasks/](planned_tasks/README.md) · [asset/](asset/asset.md)

## 红线摘要

不得空口声称「已证明」；不得用记忆旧结论替代当轮推导；不得伪造引用；
所有 .md ≤ 50 行、悬空链接 = 0；缓存文件不得写入 skill 目录。
