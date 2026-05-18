---
name: announcement
description: A 股公告快速点评 —— 自动调 announcement-comment-cn Skill
---

# /announcement <announcement_pdf_path>

Command 层只做 3 件事：

1. **参数解析**：公告 PDF 路径必填
2. **调用 Skill**：`announcement-comment-cn` 接管业务逻辑
3. **输出整理**：根据公告 importance 分流，返回 MD 或"不点评"标记

## 用法

```bash
/announcement ./raw/600519_equity_incentive.pdf
/announcement ./raw/000858_m_and_a.pdf
```

## 反模式

- Command 里硬编码"先分类再点评"流程 —— 是 Skill 的事
- Command 里挑公告类型 —— 应由 classifier Subagent 决定
