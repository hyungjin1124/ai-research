---
type: weekly-summary
week: "{{year}}-W{{week_number}}"
date_range: "{{start_date}} ~ {{end_date}}"
tags:
  - weekly-summary
  - AI-News
total_articles: 0
top_products: []
status: done
---

# AI 주간 요약 — {{year}}-W{{week_number}}

> **기간**: {{start_date}} ~ {{end_date}}

## 주간 하이라이트

<!-- 이번 주 가장 중요한 3-5개 뉴스 요약 -->

---

## 토픽별 정리

### 신제품/기능 출시
<!-- -->

### 기술 동향
<!-- -->

### 업계 동향 (투자/인수/파트너십)
<!-- -->

### 규제/정책
<!-- -->

---

## 제품별 업데이트 현황

```dataview
TABLE length(rows) AS "언급 횟수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE") AND date >= date("{{start_date}}") AND date <= date("{{end_date}}") AND length(product_mentions) > 0
FLATTEN product_mentions AS product
GROUP BY product
SORT length(rows) DESC
```

## 일일 다이제스트

```dataview
LIST
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE") AND date >= date("{{start_date}}") AND date <= date("{{end_date}}")
SORT date ASC
```

---

## 다음 주 주목 사항

<!-- 예고된 이벤트, 예상 발표, 컨퍼런스 등 -->
