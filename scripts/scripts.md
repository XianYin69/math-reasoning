# scripts（脚本库）

英文名、可独立运行、纯标准库（无第三方依赖）。每个脚本对应流程中的一道校验关。

| 脚本 | 用途 | 挂载步骤 | 用法 |
|---|---|---|---|
| `formalize_check.py` | 规格四要素齐备 + 符号定义 + 模糊措辞 | 形式化 | `python scripts/formalize_check.py --spec 规格.md` |
| `proof_chain_check.py` | 步骤编号/依据齐备、跳步词、前提闭合、结论对齐 | 证明链、自检 | `python scripts/proof_chain_check.py --proof 证明.md` |
| `dimension_check.py` | 量纲一致性 + Buckingham π 独立乘子计数 | 建模求解、自检 | `python scripts/dimension_check.py --equation "m*a = F - k*x" --dims dims.json --pi` |
| `numeric_verify.py` | 相对误差、一致有效位数、数量级互校 | 建模求解、交付 | `python scripts/numeric_verify.py --exact X --approx Y --estimate E --actual A` |
| `counterexample_search.py` | 参数网格反例搜索（脚手架，非求解器） | 猜想生成、自检 | `python scripts/counterexample_search.py --pred "…" --grid "n=2..40"` |

## 约定

- 退出码：`0` 通过，`1` 存在缺陷（缺陷清单以 JSON 打到 stdout）。
- 输出统一 JSON（`ensure_ascii=False`），无 `print` 调试残留、无裸 `except`。
- 量纲表格式：`{"符号": [基本量幂次…]}`，顺序与 `--bases` 一致。
- 反例搜索的谓词须为纯 Python 布尔表达式，蕴含写成 `not A or B`。

## 边界

脚本只做**形式校验与数值互校**，不代替推导：通过校验≠命题为真，
仍需 [自检回炉](../branch/流程/自检回炉/自检回炉.md) 的人工/模型复核。
