# /creditflow — 信用货币流向分析

触发 `macro-credit-flow` skill，从银行资产负债表三层拆解全社会资金流向，输出月度备忘录 Section 1。

## 用法

```
/creditflow [月份]
```

示例：
```
/creditflow 2026年5月
/creditflow 5月
```

## 运行内容

- 资产端：社融总量 / 信贷结构 / 票据充量判断
- 负债端：M2/M1 / 存款结构（非银单独列出）
- 机构行为层：央行操作 / 同业存单 / 债券净供给 / 官方点评印证

## 说明

单独运行时只输出 Section 1；完整备忘录请用 `/capitalflow`。
