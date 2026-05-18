"""
Ch26 hook 单测示例。

Hook 是合规闸门，闸门本身必须有测试覆盖。
"""
import subprocess
import json


def run_check(file_path: str, content: str) -> subprocess.CompletedProcess:
    payload = json.dumps({
        "tool": "Write",
        "tool_input": {"file_path": file_path, "content": content},
    })
    return subprocess.run(
        ["python", ".claude/hooks/check.py"],
        input=payload, capture_output=True, text=True,
    )


def test_blacklist_cn_blocks():
    r = run_check("output/test.md", "建议买入 A 股")
    assert r.returncode == 2
    assert "推荐" in r.stdout or "买入" in r.stdout


def test_clean_text_passes():
    r = run_check("output/test.md", "公司毛利率 32%，同比扩张 80bp")
    assert r.returncode == 0


def test_event_quick_comment_verify_count():
    content = "事件点评内容，只有 [VERIFY: 一条] 不够"
    r = run_check("output/event_quick_comment.md", content)
    assert r.returncode == 2
    assert ">=3 [VERIFY]" in r.stdout


def test_ipo_anonymization():
    content = "前 5 大客户：万科股份占比 12%"
    r = run_check("output/ipo_quick_read.md", content)
    assert r.returncode == 2
    assert "not anonymized" in r.stdout


def test_non_output_path_skipped():
    r = run_check("wiki/test.md", "推荐买入")
    assert r.returncode == 0
