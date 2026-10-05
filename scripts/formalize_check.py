#!/usr/bin/env python3
"""formalize_check：校验问题规格四要素（对象/假设/记号/目标命题）是否齐备。

用法：python scripts/formalize_check.py --spec <规格文件>
判据：四要素各成一段；假设须编号 H1..；目标须编号 G1..；
      目标段出现的符号必须在对象段或记号段定义。
"""
import argparse
import json
import re
import sys

SECTIONS = ("对象", "假设", "记号", "目标")
FORBIDDEN = ("显然", "易见", "同理可得", "略", "大概")


def split_sections(text):
    lines = text.splitlines()
    marks = []
    for index, line in enumerate(lines):
        for name in SECTIONS:
            if name in line[:24]:
                marks.append((index, name))
                break
    buckets = {name: [] for name in SECTIONS}
    for pos, (start, name) in enumerate(marks):
        stop = marks[pos + 1][0] if pos + 1 < len(marks) else len(lines)
        buckets[name].extend(lines[start:stop])
    return buckets


def symbols(lines):
    found = set()
    for line in lines:
        found.update(re.findall(r"`([^`]{1,24})`", line))
        found.update(re.findall(r"([A-Za-z][A-Za-z0-9_]{0,12})\s*[：:]", line))
    return {token.strip() for token in found if token.strip()}


def main():
    parser = argparse.ArgumentParser(description="校验形式化规格四要素")
    parser.add_argument("--spec", required=True, help="规格文件（含 对象/假设/记号/目标 段）")
    args = parser.parse_args()
    with open(args.spec, encoding="utf-8") as handle:
        text = handle.read()
    buckets = split_sections(text)
    problems = []
    for name in SECTIONS:
        if not "".join(buckets[name]).strip():
            problems.append("缺少「%s」段" % name)
    hypothesis = "\n".join(buckets["假设"])
    if not re.search(r"H\d+", hypothesis):
        problems.append("假设未编号（应写 H1、H2…）")
    goal = "\n".join(buckets["目标"])
    if not re.search(r"G\d+", goal):
        problems.append("目标命题未编号（应写 G1…）")
    defined = symbols(buckets["对象"] + buckets["记号"] + buckets["假设"])
    targets = symbols(buckets["目标"])
    undefined = sorted(token for token in targets if token not in defined)
    if undefined:
        problems.append("目标中出现未定义符号：%s" % ", ".join(undefined))
    for line in text.splitlines():
        for word in FORBIDDEN:
            if word in line:
                problems.append("规格段出现模糊措辞「%s」：%s" % (word, line.strip()[:40]))
    report = {"spec": args.spec, "sections": {k: len(v) for k, v in buckets.items()},
              "problems": problems, "ok": not problems}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
