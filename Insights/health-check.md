---
title: 인사이트 Health Check 가이드
tags:
  - automation
  - maintenance
---

# 인사이트 월간 Health Check

> 매월 1일에 실행하여 모든 인사이트 문서의 건강 상태를 점검하는 자동화 가이드입니다.
> AI 에이전트가 이 문서를 읽고 Health Check를 수행합니다.

---

## 실행 프로세스

### Step 1: 전체 인사이트 문서 스캔

`Insights/` 하위의 모든 `.md` 파일(템플릿, _CONTEXT, _INDEX 제외)의 frontmatter를 파싱합니다.

수집할 필드: `topic_id`, `topic_name`, `category`, `status`, `confidence`, `last_updated`, `auto_update.review_trigger`, `auto_update.enabled`

### Step 2: Confidence Decay 적용

`Insights/_CONTEXT.md`의 "Confidence Decay" 규칙에 따라 각 문서의 `confidence`를 검사합니다.

```
today = 현재 날짜
days_since_update = today - last_updated

카테고리 그룹 판별:
  고빈도 = market, maintenance, strategy
  중빈도 = agent-skills, agent-runtime, knowledge-data, agent-ui, open-source
  저빈도 = protocols, security-evaluation, use-cases, decisions

감소 규칙 적용:
  if days_since_update > decay_threshold[category_group][current_confidence]:
    confidence = downgrade(confidence)
    if confidence == "expired":
      status = "needs-update"
```

### Step 3: Recent Updates 미반영 건수 체크

각 문서의 `## Recent Updates` 테이블 행 수를 카운트합니다.

- 5건 이상 미반영: `confidence` 추가 1단계 감소
- 10건 이상 미반영: `status`를 `needs-update`로 변경

### Step 4: 카테고리 커버리지 체크

각 카테고리별 문서 수와 상태를 집계합니다.

```
카테고리별:
  total_docs: 전체 문서 수
  current_docs: status == "current" 문서 수
  needs_update_docs: status == "needs-update" 문서 수
  draft_docs: status == "draft" 문서 수
  avg_confidence: 평균 신뢰도 (high=3, medium=2, low=1)
  coverage_score: current_docs / total_docs * 100
```

### Step 5: 보고서 생성

아래 형식의 보고서를 `Insights/maintenance/` 디렉터리에 `YYYY-MM-health-check.md`로 생성합니다.

---

## 보고서 템플릿

```markdown
# YYYY년 MM월 인사이트 Health Check 보고서

> 생성일: YYYY-MM-DD | 총 점검 문서: N개

## 종합 건강도

| 지표 | 값 | 상태 |
|------|-----|------|
| 전체 문서 수 | N | — |
| Current 문서 | N (XX%) | 🟢/🟡/🔴 |
| Needs-Update 문서 | N (XX%) | 🟢/🟡/🔴 |
| Draft 문서 | N (XX%) | — |
| 평균 Confidence | X.X / 3.0 | 🟢/🟡/🔴 |
| 미반영 Recent Updates | N건 | 🟢/🟡/🔴 |

> 기준: 🟢 Current 80%+ / 🟡 60-80% / 🔴 60% 미만

## Confidence 변경 내역

| 문서 | 이전 | 이후 | 경과일 | 사유 |
|------|------|------|--------|------|
| ... | high | medium | 21일 | Decay 규칙 적용 |

## 즉시 리뷰 필요 (🔴 Critical)

> status: needs-update 이거나 confidence: low인 문서

| 문서 | 카테고리 | 상태 | 미반영 건수 | 마지막 업데이트 |
|------|---------|------|-----------|-------------|
| ... | ... | needs-update | 8건 | 2026-01-15 |

## 카테고리별 건강도

| 카테고리 | 문서 수 | Current | Needs-Update | Draft | 평균 Confidence | 커버리지 |
|---------|---------|---------|-------------|-------|----------------|---------|
| ... | ... | ... | ... | ... | ... | XX% |

## 권장 조치

1. **즉시**: [문서명] 리뷰 (미반영 N건, 경과 N일)
2. **이번 주**: [문서명] Confidence 회복을 위한 업데이트
3. **이번 달**: [카테고리] 신규 문서 작성 필요 (커버리지 부족)
```

---

## 상태 판정 기준

| 지표 | 🟢 양호 | 🟡 주의 | 🔴 위험 |
|------|---------|---------|---------|
| Current 비율 | 80%+ | 60-80% | 60% 미만 |
| Needs-Update 비율 | 10% 미만 | 10-20% | 20% 초과 |
| 평균 Confidence | 2.5+ | 2.0-2.5 | 2.0 미만 |
| 미반영 Updates (문서당) | 0-2건 | 3-5건 | 5건+ |

---

## 자동화 연동

| 트리거 | 산출물 | 알림 |
|--------|--------|------|
| 매월 1일 09:00 KST | `Insights/maintenance/YYYY-MM-health-check.md` | Teams 채널 알림 |
| Confidence 변경 시 | 해당 문서 frontmatter 자동 업데이트 | — |
| 🔴 Critical 발견 시 | 보고서 + Teams 멘션 알림 | PM, 아키텍처 팀 |

---

*이 가이드 최종 수정: 2026-02-11*
