"""
Ch35 PreToolUse hook —— 写文件前的合规检查闸门。

非 0 退出 + decision=block 会阻止本次写入。
本脚本是 demo 示意，生产环境使用前需要：
  - 替换黑名单为机构合规标准
  - 加错误日志 / 监控
  - 性能优化（大文件场景）
"""
import sys
import json
import re
import pathlib

BLACKLIST_CN = [
    "推荐", "买入", "卖出", "加仓", "减仓",
    "强烈推荐", "首选", "建议买入", "建议卖出",
    "龙头", "赛道", "高景气", "硬科技",
    "应该", "必须", "一定会", "肯定",
]

BLACKLIST_EN = [
    "buy", "sell", "strong buy", "outperform", "underperform",
    "recommend", "we recommend", "must", "should",
]

BROKER_NAMES_CN = [
    "中信证券", "中金", "华泰", "海通", "国泰君安",
    "招商证券", "广发证券", "申万", "东方证券",
]

VERIFY_PATTERN = re.compile(r"\[VERIFY[^\]]*\]")


def main() -> None:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})
    fp = tool_input.get("file_path", "")
    content = tool_input.get("content", "")

    p = pathlib.Path(fp)
    if not (p.suffix in {".md", ".html"} and "output" in p.parts):
        sys.exit(0)

    violations = []

    for w in BLACKLIST_CN:
        if w in content:
            violations.append(f"BLACKLIST_CN hit: {w}")

    if "us" in p.parts or "美股" in fp:
        for w in BLACKLIST_EN:
            if re.search(rf"\b{re.escape(w)}\b", content, re.IGNORECASE):
                violations.append(f"BLACKLIST_EN hit: {w}")

    if "research_digest" in fp or "industry_deep" in fp:
        for b in BROKER_NAMES_CN:
            if b in content:
                violations.append(f"BROKER_NAME hit: {b}")

    if "event_quick_comment" in fp:
        n = len(VERIFY_PATTERN.findall(content))
        if n < 3:
            violations.append(f"event_quick_comment requires >=3 [VERIFY], found {n}")

    if "ipo_quick_read" in fp:
        if re.search(r"客户[^\u4e00-\u9fa5]?[\u4e00-\u9fa5]{2,}(公司|集团|股份)", content):
            violations.append("ipo_quick_read: customer name not anonymized")

    if violations:
        print(json.dumps({
            "decision": "block",
            "reason": "check.py 拦截：\n  " + "\n  ".join(violations)
        }))
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
