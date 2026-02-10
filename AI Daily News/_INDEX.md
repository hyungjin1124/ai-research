# AI Daily News 인덱스

> AI 관련 일일 뉴스 수집 및 요약 현황. 구조 및 규칙은 [[_CONTEXT]] 참조.

---

## 최근 일일 다이제스트

```dataview
TABLE date AS "날짜", article_count AS "기사 수", join(product_mentions, ", ") AS "제품 언급", status AS "상태"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE")
SORT date DESC
LIMIT 14
```

## 주간 요약

```dataview
TABLE week AS "주차", date_range AS "기간", total_articles AS "총 기사 수", join(top_products, ", ") AS "주요 제품", status AS "상태"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "weekly-summary" AND !contains(file.name, "_TEMPLATE")
SORT week DESC
LIMIT 8
```

---

## 제품별 뉴스 언급 빈도

```dataview
TABLE length(rows) AS "언급 횟수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE") AND length(product_mentions) > 0
FLATTEN product_mentions AS product
GROUP BY product
SORT length(rows) DESC
```

---

## 수집 통계

### 최근 7일 기사 수 추이

```dataview
TABLE date AS "날짜", article_count AS "기사 수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE")
SORT date DESC
LIMIT 7
```

### 월별 누적

```dataview
TABLE length(rows) AS "다이제스트 수", sum(rows.article_count) AS "총 기사 수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE")
GROUP BY dateformat(date, "yyyy-MM") AS "월"
SORT key DESC
LIMIT 6
```
