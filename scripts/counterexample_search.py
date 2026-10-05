#!/usr/bin/env python3
"""counterexample_search：在参数网格上搜索命题谓词的反例（脚手架，非求解器）。

用法：
  python scripts/counterexample_search.py \
      --pred "not (n > 1 and is_prime(n)) or n % 2 == 1 or n == 2" \
      --grid "n=2..40"
说明：谓词为纯 Python 布尔表达式（蕴含须写成 not A or B），变量取自网格；表达式须来自当轮形式化（本脚本不校验表达式来源）。
输出：首个反例赋值 + 失败点计数；无失败即「网格内未找到反例」（不等于已证明）。
"""
import argparse
import itertools
import json
import math
import re
import sys

SAFE = {name: getattr(math, name) for name in
        ("sqrt", "log", "log2", "exp", "sin", "cos", "tan", "pi", "floor", "ceil", "fabs")}
SAFE["is_prime"] = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
SAFE["divisors"] = lambda n: [d for d in range(1, n + 1) if n % d == 0]


def parse_grid(spec):
    name, _, span = spec.partition("=")
    low, _, high = span.partition("..")
    step = 1
    if "x" in high:
        high, _, step = high.partition("x")
    return name.strip(), [low and float(low), high and float(high), float(step or 1)]


def values(bounds):
    low, high, step = bounds
    if low is None or high is None:
        raise ValueError("网格格式应为 name=low..high[ xstep]")
    count = int((high - low) // step) + 1
    return [low + i * step for i in range(count)]


def main():
    parser = argparse.ArgumentParser(description="反例搜索脚手架")
    parser.add_argument("--pred", required=True, help="命题谓词布尔表达式")
    parser.add_argument("--grid", action="append", required=True,
                        help="变量网格 name=low..high[xstep]")
    parser.add_argument("--limit", type=int, default=20, help="最多报告反例条数")
    args = parser.parse_args()
    names = []
    axes = []
    for spec in args.grid:
        name, bounds = parse_grid(spec)
        names.append(name)
        axes.append(values(bounds))
    env = dict(SAFE)
    counterexamples = []
    failures = 0
    evaluated = 0
    for combo in itertools.product(*axes):
        evaluated += 1
        env.update(dict(zip(names, combo)))
        try:
            holds = bool(eval(args.pred, {"__builtins__": {}}, env))  # noqa: S307 本地可信表达式
        except Exception as error:  # 记录求值失败而非静默吞掉
            failures += 1
            if len(counterexamples) < args.limit:
                counterexamples.append({"assign": dict(zip(names, combo)),
                                        "error": type(error).__name__})
            continue
        if not holds:
            failures += 1
            if len(counterexamples) < args.limit:
                counterexamples.append({"assign": dict(zip(names, combo)), "holds": False})
    report = {"predicate": args.pred, "grid": args.grid, "evaluated": evaluated,
              "failures": failures, "counterexamples": counterexamples,
              "verdict": "网格内未找到反例（非证明）" if failures == 0 else "找到反例，命题降级为待验"}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
