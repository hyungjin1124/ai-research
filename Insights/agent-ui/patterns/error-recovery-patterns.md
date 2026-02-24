---
type: insight-synthesis
topic_id: error-recovery-patterns
topic_name: "에러 및 복구 UI 패턴"
category: agent-ui
document_level: specific
parent_broad:
  - agent-reasoning-visualization
catalog_components:
  - error_retry_ui
tags:
  - insight
  - agent-ui
  - pattern
  - error
  - recovery
  - retry
status: draft
confidence: high
last_updated: "2026-02-15"
source_products: []
source_files: []
auto_update:
  enabled: true
  keywords: []
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 에러 및 복구 UI 패턴

## TL;DR

- Claude Code는 에러 메시지 + 제안된 수정 + 재시도 버튼으로 명시적 에러 표시와 자동 수정의 하이브리드 [^1]
- ChatGPT는 빨간색 에러 메시지와 "다시 시도" 버튼으로 최소한의 UI, 네트워크 에러 복구 자동화 [^2]
- Cursor IDE는 코드 생성 실패 시 AutoFix 기능으로 자동 수정, 사용자에게는 "고쳐지고 있습니다" 표시 [^3]
- Manus AI는 자체 수정 루프(self-correction loop) 시각화로 에러 감지 → 원인 분석 → 대안 시도 → 재실행 과정을 명확히 표시 [^4]
- Vercel v0는 AutoFix 모델로 실시간 에러 감지(코드 생성 중 스트림 후처리), 사용자에게는 투명성 최소화 [^5]

## Overview

에러 및 복구 UI 패턴은 에이전트 시스템이 작업 중 실패했을 때, 사용자에게 문제를 알리고 복구 방안을 제시하는 방식을 다룬다. 에러 처리는 단순히 "뭔가 잘못됨"을 보여주는 것이 아니라, (1) 사용자 신뢰도, (2) 문제 디버깅 능력, (3) 자동 복구 여부 등을 종합적으로 고려해야 한다.

최신 AI 개발 도구들은 크게 두 가지 철학으로 나뉜다: (A) 명시적(explicit) - 에러를 사용자에게 명확히 표시하고 선택지 제공, (B) 암묵적(implicit) - 사용자 모르게 에러 감지 및 자동 수정. Manus AI와 v0는 (B) 방식으로 "magical experience" 추구, Claude Code와 ChatGPT는 (A)로 사용자 신뢰도 강조한다.

## 경쟁사 구현 분석

### Claude Code (명시적 + 자동 수정 하이브리드) [^1]

**구현 방식**: 에러 발생 시 (1) 에러 메시지 표시 (2) 에러 원인에 대한 Claude의 해석 (3) 제안된 수정 사항 (4) 재시도 버튼

**왜 이 방식인가?**
- 사용자가 "왜 실패했는가"를 명확히 이해 가능
- Claude의 자동 분석으로 즉시 다음 단계 제시(기다릴 필요 없음)
- `/rewind` 명령으로 특정 지점까지 되감기 가능(심각한 에러 시 복구)
- 신뢰도 + 빠른 복구의 균형

**에러 표시 형식**:
- 빨간색 배경 또는 빨간색 테두리 에러 박스
- 에러 메시지 (예: "File not found: /app.tsx")
- 제안된 수정 (예: "Claude는 파일 경로 수정을 제안합니다")
- 버튼: "수정 적용" 또는 "재시도"

**자체 수정 표시**: "Claude made a mistake, fixing..." 상태 레이블 + 스피너

**Reference**: [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices), [Claude Code Internals - Recovery](https://www.letanure.dev/blog/2025-08-09--claude-code-part-11-troubleshooting-recovery), [Medium - Claude Code Rewind Patterns](https://alirezarezvani.medium.com/claude-code-rewind-5-patterns-for-disaster-recovery-a9de9bce0372)

### ChatGPT (최소 UI) [^2]

**구현 방식**: 빨간색 에러 메시지 + 간단한 설명 + "다시 시도" 버튼. 네트워크 에러는 자동 재시도(사용자 모름)

**왜 이 방식인가?**
- 사용자 혼동 최소화: 에러 메시지만 명확히 표시하고 나머지는 간단하게
- 네트워크 에러(transient errors)는 자동 재시도로 사용자 개입 최소화
- 모바일 친화적: 최소한의 UI로 화면 공간 절약

**에러 표시 형식**:
- 빨간색 배경 박스 또는 톱니바퀴 아이콘 + 빨간색
- "Something went wrong. Please try again."
- 버튼: "Retry" 또는 "Cancel"

**네트워크 에러 처리**: 자동 재시도(exponential backoff 적용), 최대 3회 후 사용자에게 알림

**Reference**: ChatGPT official UI (public interface)

### Cursor IDE (AutoFix 자동 수정) [^3]

**구현 방식**: 코드 생성 실패 감지 → 자동 AutoFix 모델 적용 → 사용자에게는 "고쳐지고 있습니다" 표시

**왜 이 방식인가?**
- "매직" 경험: 사용자가 에러를 인식하기 전에 이미 수정됨
- 개발 속도 극대화: 재시도 버튼 클릭 불필요
- 신뢰도 유지: 에러 메시지로 사용자 불안감 최소화

**에러 표시 형식**:
- 초기: "AutoFix 적용 중..." 상태 레이블
- 성공: 수정된 코드 표시(사용자는 "코드가 개선됨"으로 인식)
- 실패 후 사용자에게만 알림

**자동 수정 프로세스**: 생성 중 에러 감지 → 자동 수정 모델 호출 → 다시 생성 → 최종 결과 표시

**Reference**: [Cursor IDE Agent Documentation](https://docs.ag-ui.com/tutorials/cursor), [Cursor Tips - Builder.io](https://www.builder.io/blog/cursor-tips)

### Manus AI (자체 수정 루프 시각화) [^4]

**구현 방식**: 에러 감지 → 원인 분석 → 대안 시도 → 재실행 의 전체 루프를 실시간으로 시각화

**왜 이 방식인가?**
- 가장 높은 투명성: 사용자가 "AI가 무엇을 시도하는가" 명확히 확인
- 신뢰도 극대화: 에러 발생했으나 자동으로 극복하는 과정을 직접 봄
- 자율성(autonomy) 강조: 사용자 개입 없이 자체 문제 해결

**에러 표시 형식**:
- 실행 트리에서 에러 노드 빨간색 강조
- 다음 노드: "원인 분석 중..." (verification agent)
- 그 다음: "대안 시도..." (alternative approach)
- 마지막: "재실행..." (retry with fix)
- 각 단계 상태를 실시간 업데이트(실행 미러 옆에 트리 표시)

**자체 수정 통계**: "성공률 66% (에러 없음), 복구율 80% (자동 수정됨)"

**Reference**: [Manus AI - Early Users and Iterations](https://medium.com/manus-im/manus-ais-early-users-iterations-and-strategic-insights-11a063eb0ccd), [Manus AI 1.5 Review](https://crepal.ai/blog/agent/manus-1-5-in-depth-review-the-ai-agent-that-actually-builds/), [Skywork - Prompt Engineering for Manus](https://skywork.ai/blog/ai-agent/prompt-engineering-manus-1-5-structure-guardrails-evaluation/)

### Vercel v0 (스트림 후처리 AutoFix) [^5]

**구현 방식**: 코드 생성 중 실시간으로 에러 감지, AutoFix 모델로 동시 수정(스트림 후처리), 최종 결과는 에러 없음

**왜 이 방식인가?**
- 극도의 투명성 최소화: 사용자는 "완성된 코드"만 봄(에러 과정 숨겨짐)
- 성능: 93% 에러 없음, 코드 품질 극대화
- 속도: 40배 빠른 엔드-투-엔드 지연(AutoFix로 재생성 회수 감소)

**에러 처리 프로세스**:
1. 기본 모델이 코드 스트리밍 시작
2. AutoFix 모델(vercel-autofixer-01)이 실시간으로 에러 감지
3. 실시간 수정 제안 또는 재생성 트리거
4. 최종 결과만 사용자에게 표시

**사용자 인터페이스**: "코드 생성 중..." → 완성된 코드 표시. 에러 프로세스 완전히 숨겨짐

**Reference**: [Vercel v0 - How We Made v0 an Effective Agent](https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent), [Fireworks AI - Vercel v0 40X Faster](https://fireworks.ai/blog/vercel), [Vercel v0 Composite Model](https://vercel.com/blog/v0-composite-model-family)

### 비교 매트릭스

| 제품 | 에러 표시 | 자동 복구 | 사용자 개입 | 신뢰도 | 속도 |
|------|---------|---------|-----------|-------|------|
| Claude Code | 명시적 | 부분(재시도) | 높음 | 극높음 | 중간 |
| ChatGPT | 명시적(최소) | 자동(네트워크만) | 중간 | 중간 | 중간 |
| Cursor | 최소 | 자동(AutoFix) | 낮음 | 높음 | 높음 |
| Manus AI | 시각화됨 | 자동 | 낮음 | 극높음 | 중간 |
| v0 | 최소(숨겨짐) | 자동 | 낮음 | 중간 | 극높음 |

## 패턴 분류 및 트레이드오프

### 패턴 A: 명시적 에러 + 수동 재시도 (ChatGPT)

**특징**: 에러 메시지를 명확히 표시, 사용자가 "다시 시도" 클릭

**장점**:
- 구현 간단
- 사용자가 문제를 인식하고 결정 가능
- 신뢰도(transparency) 높음

**단점**:
- 사용자 개입 필수(번거로움)
- 에러 해결 속도 느림
- transient error도 사용자 개입 필요

### 패턴 B: 명시적 에러 + 자동 수정 제안 (Claude Code)

**특징**: 에러 표시 + Claude가 원인과 해결책 제시

**장점**:
- 신뢰도 매우 높음(사용자가 문제와 해결책을 모두 이해)
- 사용자 개입 적음(수정 제시 후 클릭만 필요)
- 디버깅 능력 우수(사용자가 원인을 학습 가능)

**단점**:
- 구현 복잡도 중상
- 자동 수정이 항상 맞다는 보장 없음
- 시간 소비(분석 + 수정 제시 과정)

### 패턴 C: 암묵적 자동 수정 (Cursor, Manus)

**특징**: 사용자 모르게 에러 감지 → 자동 수정, 또는 시각화된 자체 수정 루프

**장점**:
- 사용자 경험 뛰어남("매직" 느낌)
- 개발 속도 극대화(재시도 없음)
- Manus는 시각화로 신뢰도도 높음

**단점**:
- 구현 극도로 복잡함
- 자동 수정이 실패하면 사용자가 원인을 모름
- Cursor 스타일은 투명성 낮음(신뢰도 하락 가능)

### 패턴 D: 실시간 스트림 후처리 (v0)

**특징**: 기본 모델 스트리밍 중 실시간으로 AutoFix 모델이 에러 수정

**장점**:
- 가장 빠른 최종 결과(재생성/재시도 최소)
- 93% 에러 없음 달성 가능
- 사용자는 "품질 높은 코드"만 봄

**단점**:
- 구현 극도로 복잡함(두 모델 병렬 실행)
- 비용 높음(두 모델 사용)
- 실패 시 디버깅 어려움(과정 숨겨짐)

### 트레이드오프 요약 테이블

| 고려사항 | 패턴 A | 패턴 B | 패턴 C | 패턴 D |
|---------|--------|--------|--------|--------|
| 구현 난이도 | 낮음 | 중간 | 높음 | 극높음 |
| 신뢰도 | 중간 | 극높음 | 높음(Manus) | 낮음 |
| 속도 | 느림 | 중간 | 빠름 | 극빠름 |
| 사용자 개입 | 높음 | 중간 | 낮음 | 낮음 |
| 디버깅 용이성 | 높음 | 높음 | 중간(Manus) | 낮음 |
| 비용 | 낮음 | 중간 | 높음 | 극높음 |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 컴포넌트 | 상태 | 에러 처리와의 관련성 |
|---------|------|--------------------|
| useScenarioOrchestration.ts | 기본 상태 머신 | 에러 상태 추가 가능 |
| usePPTScenario.ts | PPT 생성 특화 | 에러 로깅 기본 구현 |
| useSlideOutlineHITL.ts | HITL 승인 플로우 | 사용자 개입 메커니즘 |
| NotificationContext | 전역 알림 시스템 | 에러 알림 기본 제공 |
| Chat Message Component | 기본 메시지 | 에러 메시지 영역 |
| 현재 에러 처리 | alert() 사용 | 기초적(개선 필요) |

### 추천 전략: "패턴 B (명시적 + 제안) + 패턴 C 일부 (비주얼 루프)"

**선택 이유**:

1. **신뢰도 중시**: KonaI-Agent는 PPT 생성 같은 중요한 작업을 수행하므로, 사용자가 원인과 해결책을 이해하는 것이 중요
2. **현실적 구현**: 패턴 D(v0 방식)는 비용과 복잡도가 높으므로 초기에는 비현실적
3. **점진적 개선**: 패턴 B로 시작하여, 향후 자동 복구 데이터 쌓인 후 패턴 C로 진화
4. **PPT 특성**: PPT 생성 실패는 대부분 구조적(예: 슬라이드 개수, 콘텐츠 포맷) 이므로, Claude의 제안이 효과적

### 세부 설계 방안

**Phase 1: 기본 에러 표시**

메시지 내에 `<ErrorBlock>` 컴포넌트:
```
⚠️ PPT 생성 실패

오류: "슬라이드 제목이 비어있음"

Claude의 제안:
- 각 슬라이드에 제목 추가
- 요약 슬라이드 포함

[수정 적용] [상세 보기] [재시도]
```

**Phase 2: 자동 수정 제안**
- Claude가 에러 원인을 분석하고 수정 사항 자동 제시
- 사용자가 "수정 적용" 클릭하면 자동 재시도

**Phase 3: 자체 수정 루프 시각화 (선택)**
- 에러 → 분석 → 수정 → 재시도 각 단계를 진행률로 표시
- Manus처럼 "자동 복구 중..." 상태 표시

**Phase 4: 자동 자체 수정 (향후)**
- 사용자 동의 후, 에러 감지 시 자동으로 수정 → 재시도
- "자동 복구 완료. 다시 시도했습니다." 알림

### 구현 아키텍처

```
Chat Message
├── Message Content
├── Error Block (new)
│   ├── Header
│   │   ├── "⚠️ Error" Label
│   │   └── Error Code
│   ├── Error Message
│   │   └── "Slide title is empty at slide 3"
│   ├── Detailed Error (collapsible)
│   │   └── Stack trace / logs
│   ├── Claude's Suggestion
│   │   ├── Problem Analysis
│   │   └── Proposed Fix (bullet points)
│   └── Action Buttons
│       ├── "Apply Fix"
│       ├── "Retry"
│       └── "Dismiss"
└── Recovery Status (during fix)
    ├── "Applying fix..." (spinner)
    └── "Retrying..." (spinner)
```

### Acceptance Criteria

에러 및 복구 UI 패턴이 완성되려면 다음을 충족해야 함:

1. **명확한 에러 표시**: 에이전트 작업 중 에러 발생 시, 메시지 내에 명확한 에러 블록(배경색 또는 테두리로 구분)이 표시될 것

2. **에러 원인 설명**: 에러 메시지는 사용자가 이해할 수 있는 언어로 "무엇이 잘못되었는가"를 설명할 것

3. **해결책 제시**: Claude가 자동으로 에러 원인을 분석하고, 2-3개의 구체적인 해결책(bullet points)을 제시할 것

4. **사용자 선택지 제공**: "수정 적용", "재시도", "취소" 등의 버튼으로 사용자가 다음 행동을 명확히 선택 가능할 것

5. **자동 복구 진행 상황**: 수정을 적용하거나 재시도할 때, "수정 중...", "재시도 중..." 같은 상태 레이블과 스피너로 진행 상황을 표시할 것

6. **복구 결과 피드백**: 수정이 성공하면 "복구 완료! 재시도합니다." 알림, 실패하면 새로운 에러 블록 표시

7. **상세 정보 접근**: 사용자가 원하면 스택 트레이스, 로그, 기술적 세부 정보를 보기 위해 "상세 보기" 버튼 제공

8. **성능**: 에러 감지 및 제안 생성이 3초 이내에 완료될 것

## Key Considerations

### 에러 분류 및 처리 전략
- **Transient errors** (네트워크, 타임아웃): 자동 재시도 (exponential backoff)
- **Validation errors** (입력 형식, 콘텐츠): Claude 분석 + 제안
- **Fatal errors** (권한, 리소스 부족): 사용자 개입 필수 + 상세 메시지

### 에러 메시지의 명확성
- 기술 용어 최소화
- 한국어 사용자를 위해 자동 번역(또는 처음부터 한글 작성)
- 예시 포함(Bad: "Invalid format", Good: "슬라이드 제목은 50자 이하여야 합니다. 현재: 'Lorem ipsum....' (127자)")

### 사용자 신뢰도
- 에러는 투명하게 표시(숨기지 않기)
- 자동 수정이 실패한 경우, "재시도 횟수: 2/3" 같은 정보 제공

### 브랜드 일관성
- 에러 아이콘: ⚠️ 또는 🔴
- 에러 배경: #FFE5E5 (연한 빨강) 또는 #FFF3CD (연한 주황)
- 액션 버튼: #FF3C42 (Pretendard 폰트)

### 접근성
- 에러 메시지를 아이콘과 텍스트로 동시 표시
- 색상만으로 에러 구분하지 않기(색각 이상 사용자 배려)

## Recent Updates

| 날짜 | 업데이트 | 참고 |
|------|---------|------|
| 2025-02-15 | 문서 최초 작성 | Claude Haiku 4.5 |
| 2025-02-15 | Claude Code/ChatGPT 패턴 분석 완료 | 명시적 vs 암묵적 |
| 2025-02-15 | Manus/v0 자동 수정 패턴 분석 | 스트림 후처리 기술 |
| 2025-02-15 | KonaI-Agent 패턴 B+C 하이브리드 전략 | 신뢰도 중시 |

## References

### Vault References
- `/mnt/리서치/Insights/agent-ui/patterns/tool-call-visualization.md` - 도구 호출 에러 시각화
- `/mnt/리서치/Insights/agent-ui/patterns/thinking-block-design.md` - 사고 과정 중 에러 감지
- `/mnt/리서치/Insights/agent-ui/patterns/multi-step-progress-patterns.md` - 단계별 에러 상태

### External References

[^1]: [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices), [Claude Code Part 11 - Troubleshooting](https://www.letanure.dev/blog/2025-08-09--claude-code-part-11-troubleshooting-recovery), [Medium - Claude Code Rewind Patterns](https://alirezarezvani.medium.com/claude-code-rewind-5-patterns-for-disaster-recovery-a9de9bce0372), [GitHub - Pro-Workflow](https://github.com/rohitg00/pro-workflow), [Medium - Claude Code Checkpoints](https://kotrotsos.medium.com/claude-code-internals-lessons-learned-and-whats-next-551092abeb5d)

[^2]: ChatGPT official public interface

[^3]: [Cursor IDE - Developing with Cursor](https://docs.ag-ui.com/tutorials/cursor), [Builder.io - Cursor Tips](https://www.builder.io/blog/cursor-tips), [APIdog - Cursor Agent Mode](https://apidog.com/blog/how-to-use-cursor-agent-mode-for-ai-powered-coding-and-api-workflows/)

[^4]: [Manus AI Medium - Early Users Iterations](https://medium.com/manus-im/manus-ais-early-users-iterations-and-strategic-insights-11a063eb0ccd), [Manus AI 1.5 Review](https://crepal.ai/blog/agent/manus-1-5-in-depth-review-the-ai-agent-that-actually-builds/), [Skywork - Prompt Engineering for Manus 1.5](https://skywork.ai/blog/ai-agent/prompt-engineering-manus-1-5-structure-guardrails-evaluation/), [Manus.im Official](https://manus.im/)

[^5]: [Vercel v0 - How We Made v0 an Effective Coding Agent](https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent), [Fireworks AI - Vercel 40X Faster](https://fireworks.ai/blog/vercel), [Vercel v0 Composite Model](https://vercel.com/blog/v0-composite-model-family), [Skywork - Vercel v0 Review 2025](https://skywork.ai/blog/vercel-v0-review-2025-ai-ui-code-generation-nextjs/)
