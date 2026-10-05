# dependence（依赖声明）

本技能为**纯方法学 + 标准库脚本**，无第三方运行时依赖。

| 名称 | 类型 | 来源 |
|---|---|---|
| Python 标准库 | software | https://www.python.org/ |
| arXiv API（知识锚点检索） | repo | http://export.arxiv.org/api/query |
| Skill_Generator | skill | local://Skill_Generator |
| skill_manage_system | skill | local://skill_manage_system |

机器可读清单：[deps.json](deps.json)
（字段 `name / source_url / license / version / install / checked_at`，缺 `source_url` 即不合格）。

## 校验

```
python scripts/lint-deps.py --root <本技能目录>
```

## 规则

1. 每条依赖必须附**原始链接**（GitHub/GitLab/官方仓库或发布页）；本地技能写 `local://<skill-id>`。
2. `checked_at` 为当轮核实日期；来源不可达即按 [降级策略](../resistance/降级策略/降级策略.md) 处理。
3. 新增依赖须同步更新本表与 [deps.json](deps.json)，并记入 [CHANGELOG.md](../CHANGELOG.md)。

## 相关

- [scripts](../scripts/scripts.md) · [references](../references/references.md)
