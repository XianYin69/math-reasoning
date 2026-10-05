#!/usr/bin/env python3
"""dimension_check：量纲一致性校验与 Buckingham π 无量纲乘子计数。

用法：
  python scripts/dimension_check.py --equation "m*a = F - k*x" --dims dims.json
  python scripts/dimension_check.py --pi --dims dims.json --bases M,L,T
dims.json 形如 {"m": [1,0,0], "a": [1,0,-2]}，向量顺序与 --bases 对应。
限制：不支持括号嵌套；除号之后的因子整体取负幂（脚手架用途，非代数系统）。
"""
import argparse
import json
import re
import sys
from fractions import Fraction


def load_dims(path):
    with open(path, encoding="utf-8") as handle:
        raw = json.load(handle)
    return {k: [int(x) for x in v] for k, v in raw.items()}


def term_dim(term, dims, size):
    vector = [Fraction(0)] * size
    sign = 1
    for token in re.split(r"([*/])", term.strip()):
        token = token.strip()
        if token == "/":
            sign = -1
            continue
        if token in ("*", ""):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^(-?\d+))?$", token)
        if not match:
            raise ValueError("无法解析因子：%s" % token)
        name = match.group(1)
        if name not in dims:
            raise ValueError("未知量：%s" % name)
        power = int(match.group(2) or 1) * sign
        for index, exp in enumerate(dims[name]):
            vector[index] += Fraction(exp) * power
    return vector


def split_sides(equation):
    parts = re.split(r"[=＝]", equation)
    if len(parts) != 2:
        raise ValueError("等式须恰含一个等号：%s" % equation)
    return parts[0], parts[1]


def check_equation(equation, dims, bases):
    size = len(bases)
    problems = []
    sides = {}
    for label, side in (("左", split_sides(equation)[0]), ("右", split_sides(equation)[1])):
        terms = [t for t in re.split(r"[+\-]", side) if t.strip()]
        vectors = []
        for term in terms:
            try:
                vectors.append(term_dim(term, dims, size))
            except ValueError as error:
                problems.append("%s侧：%s" % (label, error))
        sides[label] = vectors
        if vectors:
            first = vectors[0]
            for term, vector in zip(terms, vectors):
                if vector != first:
                    problems.append("%s侧项 %s 量纲 %s ≠ %s" % (
                        label, term.strip(), fmt(vector, bases), fmt(first, bases)))
    if sides.get("左") and sides.get("右") and sides["左"][0] != sides["右"][0]:
        problems.append("等式两侧量纲不一致")
    for func in re.findall(r"\b(exp|log|sin|cos|tan)\s*\(", equation):
        problems.append("超越函数 %s 的参数须核验是否无量纲" % func)
    return problems


def fmt(vector, bases):
    return "·".join("%s^%s" % (b, str(v)) for b, v in zip(bases, vector) if v != 0) or "无量纲"


def pi_count(dims, bases):
    matrix = [list(map(Fraction, v)) for v in dims.values()]
    rank = 0
    rows = [row[:] for row in matrix]
    for col in range(len(bases)):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]
        for r, row in enumerate(rows):
            if r != rank and row[col] != 0:
                factor = row[col]
                rows[r] = [a - factor * b for a, b in zip(row, rows[rank])]
        rank += 1
    return len(dims) - rank, rank


def main():
    parser = argparse.ArgumentParser(description="量纲一致性 / Buckingham π 校验")
    parser.add_argument("--equation", help="待校验等式")
    parser.add_argument("--dims", required=True, help="量纲表 JSON")
    parser.add_argument("--bases", default="M,L,T", help="基本量顺序")
    parser.add_argument("--pi", action="store_true", help="输出独立 π 乘子个数")
    args = parser.parse_args()
    bases = [b.strip() for b in args.bases.split(",")]
    dims = load_dims(args.dims)
    report = {"bases": bases, "quantities": len(dims), "problems": []}
    if args.equation:
        report["equation"] = args.equation
        report["problems"].extend(check_equation(args.equation, dims, bases))
    if args.pi:
        count, rank = pi_count(dims, bases)
        report["pi_group"] = {"rank": rank, "independent_pi": count}
    report["ok"] = not report["problems"]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
