"""
Ch27 模式 A 可选 hook —— 中心化审计日志异步上传。

关键：审计日志失败不能阻断研究员工作流。所有异常 swallow 掉。
"""
import os
import sys
import json
import datetime
import urllib.request


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        if payload.get("tool") not in ("Write", "Edit"):
            sys.exit(0)

        audit_entry = {
            "ts": datetime.datetime.utcnow().isoformat(),
            "user": os.environ.get("USER") or os.environ.get("USERNAME"),
            "tool": payload.get("tool"),
            "file": payload.get("tool_input", {}).get("file_path"),
            "skill": payload.get("context", {}).get("skill_name"),
        }

        endpoint = os.environ.get("AUDIT_LOG_ENDPOINT")
        if endpoint:
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(audit_entry).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
