---
name: event
description: 关键事件快评 —— 自动调 event-quick-comment Skill
---

# /event <title> <summary> <timestamp> [--source-docs ...]

Command 层只做 3 件事：

1. **参数解析**：title / summary / timestamp 必填
2. **调用 Skill**：`event-quick-comment` 接管业务逻辑（30 分钟内出第一稿）
3. **输出整理**：按 urgency 返回不同字数 MD

## 用法

```bash
/event "FOMC Sept Statement" "Fed 暂停加息，点阵图下调 50bp" 2026-09-20T18:00
/event "巴以局势升级" "..." 2026-05-18T09:30 --source-docs ./raw/news.txt
```

## 反模式

- 在 Command 里写"先调 classifier" —— 是 Skill 的事
- 输出 HTML —— 事件快评是内部时效产物，无 HTML
