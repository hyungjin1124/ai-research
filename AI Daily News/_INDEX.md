# AI Daily News 인덱스

> AI 관련 일일 뉴스 수집 및 요약 현황. 구조 및 규칙은 [[_CONTEXT]] 참조.

---

## 최근 일일 다이제스트

```dataview
TABLE date AS "날짜", article_count AS "기사 수", community_count AS "커뮤니티", deep_dive_count AS "Deep Dive", join(product_mentions, ", ") AS "제품 언급", status AS "상태"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE")
SORT date DESC
LIMIT 14
```

## 주간 요약

```dataview
TABLE week AS "주차", date_range AS "기간", total_articles AS "총 기사 수", total_community AS "커뮤니티", deep_dive_resolved AS "Deep Dive 처리", deep_dive_pending AS "Deep Dive 미처리", join(top_products, ", ") AS "주요 제품", status AS "상태"
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

## 주제별 뉴스 분포

```dataview
TABLE length(rows) AS "언급 횟수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE") AND length(topic_tags) > 0
FLATTEN topic_tags AS topic
GROUP BY topic
SORT length(rows) DESC
```

---

## Deep Dive Queue 현황

```dataview
TABLE date AS "날짜", deep_dive_count AS "Deep Dive 건수"
FROM "KonaChain/리서치/AI Daily News"
WHERE type = "daily-digest" AND !contains(file.name, "_TEMPLATE") AND deep_dive_count > 0
SORT date DESC
LIMIT 10
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
