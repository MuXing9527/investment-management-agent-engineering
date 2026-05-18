---
name: policy
description: 央行 / 财政 / 监管政策文件解读 —— 自动调 policy-doc-analyzer Skill
---

# /policy <doc_path>

Command 层只做 3 件事：

1. **参数解析**：政策文件路径必填
2. **调用 Skill**：`policy-doc-analyzer` 接管业务逻辑
3. **输出整理**：返回 MD + HTML

## 用法

```bash
/policy ./raw/pboc_q3_monetary_report.pdf
/policy ./raw/csrc_new_listing_rules.pdf
```

## 反模式

- 在 Command 里写措辞 diff 逻辑 —— 是 Skill / Subagent 的事
- 政策文件 + 数据混用一个 Command —— 应分 /macro 和 /policy
