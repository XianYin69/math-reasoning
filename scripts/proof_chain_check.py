#!/usr/bin/env python3
"""proof_chain_check：校验证明链步骤编号、依据齐备、跳步词、前提闭合与结论对齐。

用法：python scripts/proof_chain_check.py --proof <证明文件>
判据：步骤以 P1、P2… 起始且编号连续；每步须含「依据：」且非空；
      禁止「显然/易见/同理可得/易证/略去/不难验证」；前提清单与使用集互相覆盖；
      结论段须引用目标命题 G1。
"""
import argparse
import json
import re
import sys

FORBID = ("显然", "易见", "同理可得", "易证", "略去", "不难验证")


def parse_steps(text):
    steps = []
    current = None
    for line in text.splitlines():
        match = re.match(r"^\s*P(\d+)[\s:：、]+(.*)$", line)
        if match:
            current = {"id": int(match.group(1)), "body": [line]}
            steps.append(current)
        elif current is not None:
            current["body"].append(line)
    return steps


def premise_block(text):
    match = re.search(r"前提[^\n]*\n(.*?)(?=\n#|\Z)", text, re.S)
    return match.group(1) if match else ""


def used_premises(steps):
    used = set()
    for step in steps:
        body = "\n".join(step["body"])
        match = re.search(r"依据[：:](.+)", body)
        if match:
            used.update(re.findall(r"H\d+", match.group(1)))
    return used


def main():
    parser = argparse.ArgumentParser(description="校验证明链完整性")
    parser.add_argument("--proof", required=True, help="证明链文件")
    args = parser.parse_args()
    with open(args.proof, encoding="utf-8") as handle:
        text = handle.read()
    steps = parse_steps(text)
    problems = []
    if not steps:
        problems.append("未找到任何 P<n> 步骤")
    ids = [step["id"] for step in steps]
    if ids and ids != list(range(1, len(ids) + 1)):
        problems.append("步骤编号不连续：%s" % ids)
    for step in steps:
        body = "\n".join(step["body"])
        if not re.search(r"依据[：:]\s*\S", body):
            problems.append("P%d 缺少依据" % step["id"])
        for word in FORBID:
            if word in body:
                problems.append("P%d 出现跳步词「%s」" % (step["id"], word))
    declared = set(re.findall(r"H\d+", premise_block(text)))
    used = used_premises(steps)
    for name in sorted(declared - used):
        problems.append("前提 %s 声明但未被使用（须说明可否去掉）" % name)
    for name in sorted(used - declared):
        problems.append("使用了未声明的前提 %s" % name)
    conclusion = re.search(r"结论[^\n]*\n(.*?)(?=\n#|\Z)", text, re.S)
    if not conclusion or "G1" not in conclusion.group(1):
        problems.append("结论段未对齐目标命题 G1")
    report = {"proof": args.proof, "steps": len(steps),
              "premises_used": sorted(used), "problems": problems,
              "ok": not problems}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
