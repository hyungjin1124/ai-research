---
title: Insights Index
---

# 🔍 Insights 인덱스

교차 분석 인사이트 문서를 카테고리별, 상태별로 탐색합니다.

---

## 카테고리별 인사이트

### Agent Skills — Skill 개발

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/agent-skills"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Agent Runtime — Deep Agent 아키텍처

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/agent-runtime"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Knowledge & Data — KG 세팅

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/knowledge-data"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Agent UI — UI 개발

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/agent-ui"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Protocols — 프로토콜

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/protocols"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Open Source — 오픈소스

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/open-source"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Market — 시장·경쟁

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/market"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Strategy — PM·전략

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/strategy"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

### Security & Evaluation — 보안·평가

```dataview
TABLE topic_name AS "주제", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights/security-evaluation"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
```

---

## 전체 인사이트 (최근 수정순)

```dataview
TABLE topic_name AS "주제", category AS "카테고리", status AS "상태", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
SORT last_updated DESC
LIMIT 20
```

---

## ⚠️ 갱신 필요 문서

```dataview
TABLE topic_name AS "주제", category AS "카테고리", status AS "상태", confidence AS "신뢰도", last_updated AS "최종 수정"
FROM "KonaChain/리서치/Insights"
WHERE (type = "insight-synthesis" OR type = "insight-comparison") AND (status = "needs-update" OR confidence = "low")
SORT last_updated ASC
```

---

## 주간 트렌드 & 유지보수

```dataview
TABLE date AS "날짜", status AS "상태"
FROM "KonaChain/리서치/Insights/maintenance"
WHERE type = "insight-synthesis"
SORT date DESC
LIMIT 8
```

---

## 통계

### 카테고리별 문서 수

```dataview
TABLE length(rows) AS "문서 수"
FROM "KonaChain/리서치/Insights"
WHERE type = "insight-synthesis" OR type = "insight-comparison"
GROUP BY category
```
