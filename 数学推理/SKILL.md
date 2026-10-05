---
name: 数学推理
version: 0.1.0
description: >
  数理推理的数学侧子技能：结构/代数/分析/组合/数论的猜想生成与独立证明，
  遵循本体七步流程，输出区分「已证/猜想/待验」。
license: MIT
metadata:
  category: science
  parent: 数理推理
  role: capability-sub-skill
---

# 数学推理

使用 `数学推理` skill 来完成用户请求。

## 定位

本体 [数理推理](../SKILL.md) 的**能力子技能**（非 `*_only-*` 私有附属），
随本体进入同一 PUBLIC 主仓，判定见 [双仓与可见性](../resistance/双仓与可见性/双仓与可见性.md)。

## 流程

复用主干七步：[形式化](../branch/流程/形式化/形式化.md) →
[建模求解](../branch/流程/建模求解/建模求解.md) →
[猜想生成](../branch/流程/猜想生成/猜想生成.md) →
[证明策略](../branch/流程/证明策略/证明策略.md) →
[证明链](../branch/流程/证明链/证明链.md) →
[自检回炉](../branch/流程/自检回炉/自检回炉.md) →
[交付分级](../branch/流程/交付分级/交付分级.md)

## 分支细则

[数学分支/](branch/数学分支/数学分支.md)：按领域给出对象表、常用引理与失效边界。

## 约束

[resistance/](resistance/resistance.md)：数学侧红线（存在性须构造或指定公理体系等）。

## 工具

复用本体脚本：[scripts](../scripts/scripts.md)
（`proof_chain_check.py`、`counterexample_search.py`、`formalize_check.py`、`numeric_verify.py`）。
