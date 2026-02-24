---
type: insight-synthesis
topic_id: thinking-block-design
topic_name: "사고 과정 블록 설계"
category: agent-ui
document_level: specific
parent_broad:
  - agent-reasoning-visualization
catalog_components:
  - agent_thinking
tags:
  - insight
  - agent-ui
  - pattern
  - thinking
  - reasoning
  - transparency
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

# 사고 과정 블록 설계

## TL;DR

- Claude의 Extended Thinking은 축소 가능한 블록으로 사고 요약을 기본 표시, 전체 사고는 확대 시 표시 [^1]
- OpenAI o3/o4-mini는 "Reasoning..." 상태 레이블과 함께 체인 오브 쏘트(chain of thought) 단계 표시 [^2]
- Manus AI는 유리 박스 실행 미러(glass box execution mirror) 방식으로 실시간 브라우저 미러링 + 실행 트리 표시 [^3]
- Salesforce Agentforce는 주제→행동→레코드→그라운딩 단계별 시각화로 구조화된 접근 [^4]
- KonaI-Agent는 현재 사고 시각화가 없으므로, Claude 스타일의 축소 가능 사고 블록이 가장 실용적 [^5]

## Overview

사고 과정 블록은 LLM의 내부 추론(reasoning) 또는 사고(thinking) 단계를 사용자에게 시각화하는 UI 패턴이다. 최신 LLM들(Claude 4.5, OpenAI o3 등)은 "확장된 사고"(extended thinking)를 활용하여 복잡한 문제를 더 정확하게 해결한다. 이 사고 과정을 시각화하면 사용자가 AI의 의사결정 과정을 이해하고, 신뢰도를 높일 수 있다.

다양한 제품들이 사고 과정을 다르게 표현한다. Claude는 간단한 축소 가능 블록, OpenAI는 단계적 추론 텍스트, Manus AI는 실시간 브라우저 미러링 조합으로 접근한다. 각 접근법은 사용자 신뢰도, 구현 복잡도, 성능 영향 측면에서 트레이드오프가 있다.

## 경쟁사 구현 분석

### Claude (Extended Thinking) [^1]

**구현 방식**: 축소 가능한 블록(collapsible block)으로 사고 요약 기본 표시, 전체 사고 내용은 클릭 시 확대

**왜 이 방식인가?**
- 사용자는 기본적으로 최종 답변만 보고, 필요하면 사고 과정을 깊이 있게 확인 가능
- 메시지 길이가 과도하게 길어지지 않음(사용자 UX 최적화)
- Extended Thinking을 활용한 복잡한 문제 해결 과정을 투명하게 드러냄
- 모바일 친화적

**사고 표시 형식**:
- 제목: "Thinking" 또는 "Claude is thinking..."
- 요약: 2-3문장으로 사고의 핵심 내용 요약
- 확대: 전체 사고 텍스트 표시(마크다운 포맷)

**시각적 표시**: 라벨 + 드롭다운 화살표 아이콘

**Reference**: [Claude Extended Thinking Documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), [Claude Help - Using Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

### OpenAI o3/o4-mini [^2]

**구현 방식**: "Reasoning with..." 또는 "Thinking..." 상태 레이블 + 체인 오브 쏘트 단계 표시

**왜 이 방식인가?**
- 사용자에게 AI가 복잡한 추론 중임을 명확히 알림(투명성)
- o3-mini의 "high reasoning" 모드 사용 시, 단계적 사고 구조를 사용자에게 공개
- 최근 업데이트에서 "더 많은 사고 단계"를 표시하는 방향으로 진화 중
- 단계별로 AI가 올바른 방향으로 가는지 사용자가 검증 가능

**사고 표시 형식**:
- 각 단계를 번호 매김(1. 문제 이해 → 2. 접근 방식 → 3. 실행 → 4. 검증)
- 각 단계는 1-2문장 요약으로 표시
- 이전/다음 버튼으로 단계별 이동 가능

**시각적 표시**: 진행 바 또는 단계 인디케이터

**Reference**: [OpenAI o3 Announcement](https://openai.com/index/introducing-o3-and-o4-mini/), [TechCrunch - o3-mini Reasoning](https://techcrunch.com/2025/02/06/openai-now-reveals-more-of-its-o3-mini-models-thought-process/), [OpenAI o3 Models Doc](https://platform.openai.com/docs/models/o3)

### Manus AI (Glass Box Execution Mirror) [^3]

**구현 방식**: 실시간 브라우저 미러링 + 실행 트리 시각화로 사고와 행동을 동시에 표시

**왜 이 방식인가?**
- 사용자가 AI의 사고 과정과 실제 행동(마우스 클릭, 타이핑 등)을 동시에 볼 수 있음
- "자체 수정"(self-correction) 루프가 명확히 시각화됨: 에러 감지 → 원인 분석 → 대안 시도 → 재실행
- 데스크톱 자동화 작업의 경우, 사용자가 "AI가 정말로 내가 원하는 것을 하고 있는지" 실시간 검증 가능
- 신뢰도 극대화

**사고 표시 형식**:
- 실행 트리: 최상위 목표 → 중간 단계 → 세부 행동으로 계층화
- 각 노드에 상태 표시(pending → running → completed/failed)
- 브라우저 미러 옆에 트리를 배치
- 실패 지점 자동 하이라이트

**시각적 표시**: 색상 코딩(진행 중: 파란색, 완료: 초록색, 실패: 빨간색)

**Reference**: [Manus AI Medium - Early Users and Insights](https://medium.com/manus-im/manus-ais-early-users-iterations-and-strategic-insights-11a063eb0ccd), [Manus AI Self-Correction Review](https://crepal.ai/blog/agent/manus-1-5-in-depth-review-the-ai-agent-that-actually-builds/), [Manus.im Official](https://manus.im/)

### Salesforce Agentforce [^4]

**구현 방식**: 주제(Topic) → 행동(Action) → 레코드(Record) → 그라운딩(Grounding) 단계별 구조화된 시각화

**왜 이 방식인가?**
- 비즈니스 논리(예: 고객 환불 처리)를 명확한 단계로 분해
- 각 단계가 CRM 데이터와 연결되므로, 사용자가 AI의 행동이 실제 데이터에 미치는 영향을 이해
- 멀티스텝 에이전트 워크플로우에 최적화
- 엔터프라이즈 사용자에게 감사(audit) 흔적 제공

**사고 표시 형식**:
- 각 단계를 카드로 표시
- 카드 내용: 단계명 + 수행할 행동 + 영향받을 레코드
- 완료된 단계는 체크마크, 진행 중인 단계는 로더 표시

**시각적 표시**: 수직 타임라인 또는 스텝퍼 UI

**Reference**: [Salesforce Agentforce 360 Announcements](https://www.salesforce.com/agentforce/what-is-new/?bc=OTH), [Salesforce Developers - New Agentforce Features](https://developer.salesforce.com/blogs/2025/10/build-and-optimize-agents-with-new-agentforce-360-features), [Salesforce Guide 2025-26](https://admin.salesforce.com/blog/2026/2026-roadmap-for-salesforce-admins-ai-agentforce-and-emerging-trends-podcast)

### 비교 매트릭스

| 제품 | 기본 표시 | 상세 정보 | 사고 형식 | 신뢰도 | 구현 난이도 |
|------|---------|---------|---------|-------|-----------|
| Claude | 요약 축소형 | 확대 시 전체 | 텍스트 일문체 | 높음 | 낮음 |
| OpenAI o3 | 단계별 진행 | 각 단계 설명 | 구조화됨 | 높음 | 중간 |
| Manus AI | 트리 + 미러 | 실시간 행동 | 실행 트리 | 극높음 | 높음 |
| Salesforce | 타임라인 | 각 단계 카드 | 구조화됨 | 높음 | 중간 |

## 패턴 분류 및 트레이드오프

### 패턴 A: 축소 가능 텍스트 블록 (Claude)

**특징**: 사고 내용을 단순 텍스트로 축소/확대 가능하게 표시

**장점**:
- 구현이 매우 간단함
- 메시지 흐름에 자연스럽게 통합
- 모바일 친화적
- 로딩 성능 우수

**단점**:
- 사고 과정의 구조화 불가
- 사용자가 텍스트를 일일이 읽어야 함
- 복잡한 사고는 이해하기 어려움

### 패턴 B: 단계별 진행 표시 (OpenAI o3)

**특징**: 사고를 구조화된 단계로 분해, 각 단계를 순차적으로 표시

**장점**:
- 복잡한 사고를 체계적으로 이해 가능
- 사용자가 각 단계를 검증 가능
- 애니메이션으로 진행 상황 표시 가능

**단점**:
- 수동으로 단계를 정의해야 함(LLM이 자동 생성해야 함)
- UI 복잡도 증가
- 단계 수가 많으면 스크롤 필요

### 패턴 C: 실시간 실행 미러 (Manus AI)

**특징**: 브라우저 미러링과 함께 실행 트리를 실시간으로 표시

**장점**:
- 가장 높은 신뢰도(사용자가 직접 행동을 봄)
- 자체 수정 루프가 명확히 표시됨
- 에러가 발생한 정확한 순간을 파악 가능

**단점**:
- 구현 복잡도 극대
- 성능 오버헤드 큼(브라우저 미러링 + 트리 렌더링)
- 웹 기반 작업에만 적용 가능
- 모바일에서 사용 불가

### 패턴 D: 구조화된 카드 타임라인 (Salesforce)

**특징**: 각 단계를 카드로 표시, 타임라인 형태로 구성

**장점**:
- 복잡한 워크플로우를 시각적으로 명확히 표시
- 각 단계의 영향(예: 어떤 레코드 수정)을 함께 표시 가능
- 감사(audit) 용도로 유용

**단점**:
- 디자인 및 구현이 복잡함
- 모바일에서 가로 스크롤 필요 가능성
- 단계당 많은 정보 필요(자동 추출 어려움)

### 트레이드오프 요약 테이블

| 고려사항 | 패턴 A | 패턴 B | 패턴 C | 패턴 D |
|---------|--------|--------|--------|--------|
| 신뢰도 | 중간 | 중상 | 극높음 | 높음 |
| 구현 난이도 | 낮음 | 중간 | 높음 | 높음 |
| UI 복잡도 | 낮음 | 중간 | 높음 | 중간-높음 |
| 모바일 친화성 | 높음 | 높음 | 낮음 | 중간 |
| 성능 영향 | 무시할 수준 | 낮음 | 높음 | 중간 |
| 이해 용이성 | 중간 | 높음 | 극높음 | 높음 |
| 웹 기반만 가능 | 아니오 | 아니오 | 예 | 아니오 |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 컴포넌트 | 상태 | 사고 시각화와의 관련성 |
|---------|------|----------------------|
| useScenarioOrchestration.ts | 멀티스텝 상태 머신 | 단계 표시 로직 활용 가능 |
| usePPTScenario.ts | PPT 생성 + 단계 추적 | 구조 일부 재사용 가능 |
| NotificationContext | 전역 알림 시스템 | 사고 완료/에러 알림용 |
| Radix UI Components | 아코디언, 콜랩스 | 축소/확대 UI 기본 제공 |
| Chat Message Component | 기본 메시지 렌더링 | 사고 블록 통합점 |

### 추천 전략: "단기 패턴 A + B 하이브리드, 장기 패턴 D로 진화"

**선택 이유**:

**단기 (Phase 1-2)**:
- Claude 스타일의 축소 가능 블록(패턴 A)이 구현 비용 대비 효과가 좋음
- useScenarioOrchestration.ts의 단계 정보를 활용하여 기본 단계 표시 가능(패턴 B 일부)
- 현재 사용자들이 "사고 과정" 개념에 생소하므로, 간단한 구현으로 시작하여 점진적 개선

**장기 (Phase 3+)**:
- Salesforce 스타일의 구조화된 카드(패턴 D)로 진화 가능
- 에이전트 행동(예: 파일 수정)과 사고를 연계하여 "이 행동을 왜 했는가"를 사용자가 이해

### 세부 설계 방안

**Phase 1: 기본 사고 블록 (축소 가능)**
- 메시지 내 "💭 Thinking" 라벨 + 드롭다운 화살표
- 사고 요약: 모델이 자동 생성(최대 200자)
- 클릭 시 전체 사고 내용 확대(마크다운 포맷)
- 색상: 검은색 텍스트 + 밝은 배경(예: #F0F0F0)

**Phase 2: 단계별 시각화 추가**
- useScenarioOrchestration.ts에서 `steps` 정보 추출
- 각 단계를 축소 블록 내에 번호 매김(1. 분석 2. 계획 3. 실행)
- 현재 진행 중인 단계 하이라이트

**Phase 3: 도구 호출과의 연계**
- 각 단계 하에 그 단계에서 호출된 도구 표시
- 예: "단계 2: 계획" → [도구: 파일 읽기] → [도구: 검색]

**Phase 4: 구조화된 카드 레이아웃 (향후)**
- 단계를 카드로 변환
- 각 카드: 제목 + 설명 + 관련 도구 + 완료/실패 상태

### 구현 아키텍처

```
Chat Message
├── Message Content
├── Thinking Block (새로 추가)
│   ├── Header
│   │   ├── "💭 Thinking" Label
│   │   └── Toggle Icon (expanded/collapsed)
│   ├── Summary (항상 표시)
│   │   └── "Claude is analyzing..."
│   └── Detailed Thinking (클릭 시 확대)
│       ├── Step 1: Analysis
│       ├── Step 2: Planning
│       ├── Step 3: Execution
│       └── Step 4: Verification
└── Tool Calls Section
```

### Acceptance Criteria

사고 과정 블록이 완성되려면 다음을 충족해야 함:

1. **기본 표시**: 에이전트가 사고 단계를 거칠 때, "💭 Thinking" 레이블 아래에 간단한 요약(최대 200자)이 항상 표시될 것

2. **상세 정보 접근**: 사용자가 드롭다운 화살표를 클릭하면, 전체 사고 과정을 마크다운 형식으로 확인할 수 있을 것

3. **단계별 분해**: 사고 과정이 명확한 단계(예: 이해 → 계획 → 실행)로 분해되어 표시될 것

4. **진행 상황 표시**: 사고가 진행 중일 때는 "분석 중..." 같은 상태 레이블이 표시되고, 완료되면 체크마크가 표시될 것

5. **메시지 흐름 통합**: 사고 블록이 메시지의 자연스러운 부분으로 통합되어, 별도 패널이나 팝업을 열지 않아도 볼 수 있을 것

6. **모바일 친화성**: 모바일 환경에서도 사고 블록이 깔끔하게 렌더링되고, 축소 상태에서 메시지를 주고받는 데 방해가 없을 것

7. **성능**: 사고 내용이 10,000자 이상이어도 초기 로딩이 1초 이내일 것(전체 내용은 지연 로딩)

8. **도구 호출과의 연계**: 각 사고 단계 아래에 그 단계에서 호출된 도구 목록이 표시될 것(향후)

## Key Considerations

### 사고 내용의 명확성
- LLM이 생성하는 사고 내용이 종종 읽기 어려운 형식일 수 있으므로, 자동으로 마크다운 포맷팅 또는 섹션 분리 고려
- 사고 내용에서 "중요한 결정 지점"을 자동 추출하여 볼드 처리

### 유저 인터페이스 일관성
- 사고 블록의 배경색을 메시지 배경과 구분 가능하게 선택
- 축소 아이콘의 방향(∨/∧)을 명확히 하여 상태 즉시 파악 가능하게

### 성능 및 접근성
- 매우 긴 사고 내용은 처음 500자만 로딩하고, "더 보기" 버튼으로 나머지 로드
- 스크린 리더를 위해 사고 블록을 `<summary>` + `<details>` HTML 요소 또는 role="region" 속성 사용

### 브라우저 호환성
- Radix UI의 Collapsible 컴포넌트 사용으로 IE11 미지원(최신 브라우저만 지원)

### 브랜드 일관성
- 로딩 애니메이션: #FF3C42 (Pretendard 폰트)
- 축소 블록 배경: 흰색 또는 #F9F9F9

## Recent Updates

| 날짜 | 업데이트 | 참고 |
|------|---------|------|
| 2025-02-15 | 문서 최초 작성 | Claude Haiku 4.5 |
| 2025-02-15 | Claude/OpenAI o3 패턴 비교 완료 | Manus Glass Box 패턴 추가 |
| 2025-02-15 | 하이브리드 전략 수립 (단기: 패턴 A+B, 장기: 패턴 D) | Salesforce Agentforce 참고 |

## References

### Vault References
- `/mnt/리서치/Insights/agent-ui/patterns/tool-call-visualization.md` - 도구 호출과 사고 블록의 통합
- `/mnt/리서치/Insights/agent-ui/patterns/multi-step-progress-patterns.md` - 멀티스텝과의 UX 연계
- `/mnt/리서치/Insights/agent-ui/patterns/error-recovery-patterns.md` - 에러 시 사고 과정 추적

### External References

[^1]: [Claude Extended Thinking - Official Documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), [Claude Help - Using Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking), [Medium - Thinking Mode in Claude 4.5](https://medium.com/@mkteam/thinking-mode-in-claude-4-5-all-you-need-to-know-353235942182)

[^2]: [OpenAI o3 and o4-mini Announcement](https://openai.com/index/introducing-o3-and-o4-mini/), [TechCrunch - o3-mini Reasoning Texts](https://techcrunch.com/2025/02/06/openai-now-reveals-more-of-its-o3-mini-models-thought-process/), [OpenAI Models Documentation](https://platform.openai.com/docs/models/o3), [GitHub - Thinking Model Client](https://github.com/tao12345666333/thinking-model-client)

[^3]: [Manus AI Medium - Early Users Iterations](https://medium.com/manus-im/manus-ais-early-users-iterations-and-strategic-insights-11a063eb0ccd), [Manus AI 1.5 In-Depth Review](https://crepal.ai/blog/agent/manus-1-5-in-depth-review-the-ai-agent-that-actually-builds/), [Manus AI - Hands On AI](https://manus.im/), [Manus AI Review 2025](https://smartbottips.com/manus-ai-review/)

[^4]: [Salesforce Agentforce 360 Announcements](https://www.salesforce.com/agentforce/what-is-new/?bc=OTH), [Salesforce Developers - New Agentforce Features](https://developer.salesforce.com/blogs/2025/10/build-and-optimize-agents-with-new-agentforce-360-features), [Salesforce News - Agentic Enterprise 2025](https://www.salesforce.com/news/stories/2025-recap/?bc=OTH)

[^5]: useScenarioOrchestration.ts - 현재 KonaI-Agent 코드베이스의 멀티스텝 상태 관리 훅
