---
type: weekly-summary
week: "{{year}}-W{{week_number}}"
date_range: "{{start_date}} ~ {{end_date}}"
tags:
  - weekly-summary
  - AI-News
total_articles: 0
total_community: 0
deep_dive_resolved: 0
deep_dive_pending: 0
top_products: []
top_topics: []
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

### 오픈소스 생태계
<!-- OSS 프레임워크, 모델, 도구 동향 -->

### 데이터/지식 인프라
<!-- RAG, 벡터 DB, 시맨틱 레이어 동향 -->

---

## Community Pulse 주간 하이라이트

### 🔥 이번 주 화제

<!-- 일일 Community Pulse에서 가장 높은 engagement를 기록한 스레드 3-5건 -->

### 💡 이번 주 Best Tip

<!-- 일일 실전 Tip 중 팀에 가장 유용한 1-2건을 선별하여 상세 기술 -->

### 📊 주간 커뮤니티 센티먼트 추이

<!-- 주요 제품/기술에 대한 커뮤니티 반응이 주간 어떻게 변화했는지 요약 -->

---

## Deep Dive 처리 현황

### 이번 주 처리 완료

| 뉴스 | 대상 문서 | 갱신 범위 | 처리일 |
|------|---------|----------|-------|
| | | | |

### 미처리 (다음 주 이월)

| 뉴스 | 대상 문서 | 갱신 범위 | 난이도 | 등록일 |
|------|---------|----------|-------|-------|
| | | | | |

> **처리율**: 0/0건 (0%) — 미처리 항목은 다음 주로 이월됩니다.

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
