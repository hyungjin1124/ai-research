# AI Agent Products 리서치 인덱스

> AI Agent 서비스별 종합 리서치 현황. 구조 및 규칙은 [[_CONTEXT]] 참조.

---

## 전체 제품 목록

```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류", status AS "상태", last_updated AS "최종 수정"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND !contains(file.name, "_TEMPLATE")
SORT category ASC, product_name ASC
```

## 최근 업데이트된 제품

```dataview
TABLE product_name AS "제품", last_updated AS "최종 수정"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND status != "draft"
SORT last_updated DESC
LIMIT 5
```

---

## 카테고리별 보기

### B2C
```dataview
LIST
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND category = "B2C"
SORT product_name ASC
```

### Enterprise
```dataview
LIST
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND category = "Enterprise"
SORT product_name ASC
```

### Analytics
```dataview
LIST
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND category = "Analytics"
SORT product_name ASC
```

### Knowledge
```dataview
LIST
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND category = "Knowledge"
SORT product_name ASC
```

---

## 태그별 보기

> 제품 frontmatter의 `tags` 필드 기준 분류. 하나의 제품이 여러 태그에 중복 표시될 수 있습니다.

#### ERP-Integrated
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "ERP-Integrated")
SORT product_name ASC
```

#### MCP-Support
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "MCP-Support")
SORT product_name ASC
```

#### A2A-Support
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "A2A-Support")
SORT product_name ASC
```

#### Agent-Builder
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Agent-Builder")
SORT product_name ASC
```

#### LLM-Native
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "LLM-Native")
SORT product_name ASC
```

#### NL-to-SQL
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "NL-to-SQL")
SORT product_name ASC
```

#### Full-Stack-AI
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Full-Stack-AI")
SORT product_name ASC
```

#### Enterprise-Search
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Enterprise-Search")
SORT product_name ASC
```

#### Agent-Marketplace
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Agent-Marketplace")
SORT product_name ASC
```

#### Korea-ERP
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Korea-ERP")
SORT product_name ASC
```

#### Manufacturing-ERP
```dataview
TABLE product_name AS "제품", vendor AS "회사", category AS "분류"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND contains(tags, "Manufacturing-ERP")
SORT product_name ASC
```

### 📊 태그 전체 매트릭스

```dataview
TABLE product_name AS "제품", join(filter(tags, (t) => t != "AI-Agent"), ", ") AS "태그"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-profile" AND !contains(file.name, "_TEMPLATE")
SORT category ASC, product_name ASC
```

---

## 업데이트 활성도

```dataview
TABLE product_id AS "제품", last_appended AS "마지막 업데이트"
FROM "KonaChain/리서치/AI Agent Products"
WHERE type = "product-updates" AND !contains(file.name, "_TEMPLATE")
SORT last_appended DESC
```
