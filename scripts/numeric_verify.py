#!/usr/bin/env python3
"""numeric_verify：误差界、有效位数与数量级校验。

用法：
  python scripts/numeric_verify.py --exact 0.6931471805599453 --approx 0.69315
  python scripts/numeric_verify.py --estimate 6.3e-3 --actual 6.93e-3
判据：相对误差 = |approx-exact|/|exact|；一致有效位数 = floor(-log10(相对误差))；
      数量级差 = |floor(log10(estimate)) - floor(log10(actual))|，>1 即告警。
"""
import argparse
import json
import math
import sys


def sig_digits(exact, approx):
    if exact == 0:
        return 0 if approx != 0 else None
    rel = abs(approx - exact) / abs(exact)
    if rel == 0:
        return None
    return max(0, int(math.floor(-math.log10(rel))))


def magnitude(value):
    if value == 0:
        return None
    return int(math.floor(math.log10(abs(value))))


def main():
    parser = argparse.ArgumentParser(description="数值可信度校验")
    parser.add_argument("--exact", type=float, help="参考值（解析/高精度）")
    parser.add_argument("--approx", type=float, help="计算值")
    parser.add_argument("--tol", type=float, default=1e-6, help="容许相对误差")
    parser.add_argument("--estimate", type=float, help="数量级估算值")
    parser.add_argument("--actual", type=float, help="实际值")
    args = parser.parse_args()
    report = {"problems": []}
    if args.exact is not None and args.approx is not None:
        rel = abs(args.approx - args.exact) / abs(args.exact) if args.exact else abs(args.approx)
        digits = sig_digits(args.exact, args.approx)
        report["relative_error"] = rel
        report["consistent_digits"] = digits
        report["tolerance"] = args.tol
        if rel > args.tol:
            report["problems"].append("相对误差 %.3e 超出容许 %.3e" % (rel, args.tol))
    if args.estimate is not None and args.actual is not None:
        low, high = magnitude(args.estimate), magnitude(args.actual)
        gap = abs(low - high) if low is not None and high is not None else None
        report["order_gap"] = gap
        if gap is not None and gap > 1:
            report["problems"].append("估算与精确解相差 %d 个数量级，须重查单位与截断" % gap)
    if not report.get("relative_error") and report.get("order_gap") is None:
        report["problems"].append("未提供任何比较对（--exact/--approx 或 --estimate/--actual）")
    report["ok"] = not report["problems"]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
