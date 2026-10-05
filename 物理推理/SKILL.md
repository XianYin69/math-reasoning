---
name: 物理推理
version: 0.1.0
description: >
  数理推理的物理侧子技能：量纲分析、极限与特例验证、对称性与守恒律检查、
  数量级估算与精确解互校、模型假设与适用域声明。
license: MIT
metadata:
  category: science
  parent: 数理推理
  role: capability-sub-skill
---

# 物理推理

使用 `物理推理` skill 来完成用户请求。

## 定位

本体 [数理推理](../SKILL.md) 的**能力子技能**，随本体入同一 PUBLIC 主仓，
判定见 [双仓与可见性](../resistance/双仓与可见性/双仓与可见性.md)。

## 流程

复用主干七步：[形式化](../branch/流程/形式化/形式化.md) →
[建模求解](../branch/流程/建模求解/建模求解.md) →
[猜想生成](../branch/流程/猜想生成/猜想生成.md) →
[证明策略](../branch/流程/证明策略/证明策略.md) →
[证明链](../branch/流程/证明链/证明链.md) →
[自检回炉](../branch/流程/自检回炉/自检回炉.md) →
[交付分级](../branch/流程/交付分级/交付分级.md)

## 分支细则

[物理分支/](branch/物理分支/物理分支.md)：量纲、对称守恒、估算互校、适用域四关。

## 约束

[resistance/](resistance/resistance.md)：单位制统一、量纲一致性、守恒律核验。

## 工具

复用本体脚本：[scripts](../scripts/scripts.md)
（`dimension_check.py`、`numeric_verify.py`、`proof_chain_check.py`）。
