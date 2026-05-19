"""
Ch35 Stop hook —— 会话级收尾检查。

注意：用 decision=warn 而非 block——会话已走到收尾，强制 block 会让研究员工作丢失。
"""
import sys
import json
import pathlib
import subprocess


def main() -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain", "output/"],
        capture_output=True, text=True
    )
    files = []
    for line in result.stdout.splitlines():
        if line[:2] in ("??", " M", "A "):
            files.append(line[3:].strip())

    issues = []
    md_files = [f for f in files if f.endswith(".md")]
    for md in md_files:
        html = md.replace(".md", ".html")
        if html in files:
            md_len = len(pathlib.Path(md).read_text(encoding="utf-8"))
            html_len = len(pathlib.Path(html).read_text(encoding="utf-8"))
            if html_len < md_len * 0.9:
                issues.append(f"{md} vs {html}: html 字数显著少于 md，疑似截断")

    if issues:
        print(json.dumps({
            "decision": "warn",
            "reason": "stop_check 警告：\n  " + "\n  ".join(issues)
        }))

    sys.exit(0)


if __name__ == "__main__":
    main()
