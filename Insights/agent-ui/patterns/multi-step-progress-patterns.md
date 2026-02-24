---
type: insight-synthesis
topic_id: multi-step-progress-patterns
topic_name: "멀티스텝 진행 표시 패턴"
category: agent-ui
document_level: specific
parent_broad:
  - agent-reasoning-visualization
catalog_components:
  - multi_step_progress
tags:
  - insight
  - agent-ui
  - pattern
  - progress
  - stepper
  - multi-step
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

# 멀티스텝 진행 표시 패턴

## TL;DR

- Claude Cowork는 체크박스 형태의 비주얼 To-Do 리스트로 실시간 상태 업데이트 제공 [^1]
- GitHub Copilot Workspace는 Understanding → Planning → Coding → Execution 5단계 스텝 바로 진행 상황 표시 [^2]
- Bolt.new는 Plan Mode로 제안된 모든 단계를 리스트 형태로 보여주고 사용자 승인 후 실행 [^3]
- Cursor IDE는 실시간 에이전트 상태("searching codebase", "editing files") + 사이드바 에이전트 모니터링 패널 [^4]
- KonaI-Agent는 useScenarioOrchestration.ts의 단계 상태를 일반화하여, 3-panel 레이아웃의 우측 사이드바에 진행률 표시 가능 [^5]

## Overview

멀티스텝 진행 표시는 에이전트가 여러 단계를 거쳐 작업을 완료할 때, 현재 어느 단계에 있는지, 얼마나 진행되었는지를 시각적으로 사용자에게 알려주는 UI 패턴이다. 장시간 실행되는 작업(예: 코드 생성, PPT 작성)의 경우, 명확한 진행 표시가 사용자의 불안감을 감소시키고, 작업 예상 시간을 파악하게 한다.

최신 개발 도구들(Claude Cowork, GitHub Copilot Workspace, Bolt.new)은 선형 스텝퍼(linear stepper), 체크리스트(checklist), 실시간 상태 레이블(real-time status labels) 등 다양한 패턴을 채택하고 있다. 각 패턴은 단계 유형(결정적 vs. 동적), 사용자 상호작용(수동 vs. 자동), 시각적 복잡도에 따라 장단점이 다르다.

## 경쟁사 구현 분석

### Claude Cowork (To-Do 리스트) [^1]

**구현 방식**: 체크박스 형태의 비주얼 To-Do 리스트, 각 항목의 상태를 실시간으로 업데이트(pending → active → completed)

**왜 이 방식인가?**
- 사용자가 작업 진행 상황을 직관적으로 이해 가능(체크박스 = 완료 직관성 최고)
- 수직 레이아웃으로 긴 작업 목록도 깔끔하게 표시
- 각 항목을 클릭하면 상세 정보(도구 호출, 결과) 표시 가능
- 모바일 친화적

**단계 표시 형식**:
- 각 행: [체크박스] [단계명] [상태 레이블: "진행 중", "완료"]
- 진행 중인 단계: 체크박스 대신 스피너 표시
- 완료된 단계: 초록색 체크마크

**시각적 특징**: 수직 선(vertical line)으로 단계 연결

**Reference**: Claude Cowork official documentation (internal Anthropic resource)

### GitHub Copilot Workspace (5단계 스텝 바) [^2]

**구현 방식**: Understanding → Planning → Coding → Execution → Review 5가지 고정 단계를 수평 스텝 바로 표시

**왜 이 방식인가?**
- 개발 워크플로우의 본질적 단계를 일반화하여 모든 작업에 적용 가능
- 수평 레이아웃으로 전체 진행 상황을 한눈에 파악
- 각 단계를 클릭하면 해당 단계의 내용(understanding text, code diff) 표시
- 데스크톱 환경에 최적화

**단계 표시 형식**:
- 각 단계: 원형 노드 + 단계명 + 연결선
- 현재 단계: 파란색으로 강조
- 완료된 단계: 초록색 체크마크
- 미진행 단계: 회색

**진행 세부 정보**: 각 단계 아래에 진행률(예: "Generating plan... 60% complete")

**Reference**: [GitHub Copilot Workspace User Manual](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/overview.md), [GitHub Next Copilot Workspace](https://githubnext.com/projects/copilot-workspace)

### Bolt.new (Plan Mode 리스트) [^3]

**구현 방식**: Plan Mode에서 제안된 모든 단계를 리스트 형태로 표시, 사용자가 승인 후 단계별 실행 시각화

**왜 이 방식인가?**
- 사용자가 실행 전에 계획을 완전히 검토 가능(HITL 패턴)
- 각 단계를 수정하거나 스킵할 수 있는 유연성
- Plan Mode와 Build Mode의 명확한 분리로 사용자 혼동 최소화
- 토큰 절약: 사용자가 사전에 계획을 검증하므로 불필요한 생성 방지

**단계 표시 형식**:
- 리스트 형태 (번호 매김: 1. 2. 3. ...)
- 각 항목: 단계명 + 간단한 설명(1-2문장)
- "Implement Plan" 버튼으로 승인

**실행 중 시각화**:
- 실행 시작 후, 각 단계별 파일 생성/수정 상황을 진행률로 표시
- Diff 뷰에서 변경 사항 자동 스크롤

**Reference**: [Bolt.new Support - Plan and Discussion Modes](https://support.bolt.new/best-practices/discussion-mode), [Bolt.new Inside V2](https://bolt.new/blog/inside-bolt-v2-hidden-power-features)

### Cursor IDE (실시간 상태 + 사이드바) [^4]

**구현 방식**: 실시간 에이전트 상태 레이블("searching codebase", "editing files") + 우측 사이드바의 에이전트 모니터링 패널

**왜 이 방식인가?**
- 메인 에디터 영역을 방해하지 않으면서도 에이전트 진행 상황 추적 가능
- 여러 에이전트를 동시에 실행할 때, 각 에이전트의 상태를 독립적으로 모니터링 가능
- "Mission Control" 그리드 뷰로 평면도 같이 모든 에이전트의 상태를 한눈에 확인

**단계 표시 형식**:
- 상태 레이블: "정보 검색 중...", "파일 편집 중...", "검증 중..."
- 각 에이전트별 사이드바 카드:
  - 에이전트명
  - 현재 상태 (running/paused/completed)
  - 진행 로그 (마지막 5줄)
  - 관련 파일 목록

**시각적 특징**: 색상 코딩 (파란색: 진행 중, 초록색: 완료, 빨간색: 에러)

**Reference**: [Cursor IDE Agent Documentation](https://docs.ag-ui.com/tutorials/cursor), [Cursor Agent Mode Guide](https://apidog.com/blog/how-to-use-cursor-agent-mode-for-ai-powered-coding-and-api-workflows/), [Analytics Vidhya - Cursor Agent Tutorial](https://www.analyticsvidhya.com/blog/2025/07/cursor-agent-guide/)

### 비교 매트릭스

| 제품 | 패턴 | 단계 수 | 상호작용 | 데스크톱 | 모바일 | 실시간 |
|------|------|--------|---------|---------|--------|--------|
| Claude Cowork | 체크리스트 | 동적 | 자동 | 우수 | 우수 | 예 |
| GitHub Copilot | 스텝 바 | 5 고정 | 클릭 | 우수 | 불가 | 예 |
| Bolt.new | 리스트 + 승인 | 동적 | 승인 후 자동 | 우수 | 중간 | 예 |
| Cursor | 상태 + 사이드바 | 동적 | 자동 | 우수 | 불가 | 예 |

## 패턴 분류 및 트레이드오프

### 패턴 A: 체크리스트 형 (Claude Cowork)

**특징**: 수직 리스트로 각 단계를 체크박스 형태로 표시, 완료 상태를 직관적으로 표현

**장점**:
- 극도로 직관적(체크박스 = 완료 상징)
- 수직 레이아웃으로 공간 활용 효율적
- 모바일에서도 가독성 우수
- 각 단계를 클릭하여 상세 정보 확인 가능

**단점**:
- 단계가 50개 이상이면 스크롤 과다
- 단계 간 시각적 연결이 약함
- 사용자가 "남은 진행 %"를 한눈에 파악하기 어려움

### 패턴 B: 수평 스텝 바 (GitHub Copilot)

**특징**: 수평 진행 바로 5단계의 고정 워크플로우를 표시, 선형적 진행을 강조

**장점**:
- 전체 워크플로우 "흐름"을 명확히 표시
- 진행 상황(%) 직관적 이해
- 데스크톱 환경에서 상단 고정 가능
- 단계 간 "다음" 순서가 명확함

**단점**:
- 모바일에서 좌우 스크롤 필요 가능
- 고정 5단계 모델이 모든 워크플로우에 맞지 않을 수 있음
- 단계가 더 필요하면 확장 어려움

### 패턴 C: 리스트 + 사용자 승인 (Bolt.new)

**특징**: Plan Mode에서 리스트로 단계 제시, 사용자 승인 후 실행 중 진행률 표시

**장점**:
- HITL(Human In The Loop) 패턴으로 사용자 신뢰도 극대화
- 계획과 실행이 명확히 분리되어 사용자가 제어권 유지
- 동적 단계 수 대응 가능
- 토큰 효율적

**단점**:
- 사용자 승인이 필요하므로 완전 자동화 불가
- 승인 단계 추가로 UX 복잡도 증가
- 사용자가 리스트를 일일이 읽어야 함

### 패턴 D: 상태 레이블 + 사이드바 (Cursor)

**특징**: 에디터 우측 사이드바에 에이전트 모니터링 패널, 실시간 상태 레이블 표시

**장점**:
- 메인 작업 영역(에디터) 방해 최소화
- 여러 에이전트 동시 모니터링 가능
- Mission Control 그리드로 평면도 스타일 전체 상태 파악
- 개발자 도구로 최적화

**단점**:
- 사이드바 공간 필요(화면 좁으면 불편)
- 모바일/태블릿 구현 어려움
- UI 복잡도 높음

### 트레이드오프 요약 테이블

| 고려사항 | 패턴 A | 패턴 B | 패턴 C | 패턴 D |
|---------|--------|--------|--------|--------|
| 직관성 | 극높음 | 높음 | 중간 | 중간 |
| 공간 효율성 | 높음 | 중간 | 높음 | 낮음 |
| 모바일 친화성 | 높음 | 낮음 | 중간 | 낮음 |
| 사용자 제어 | 낮음 | 중간 | 높음 | 낮음 |
| 구현 복잡도 | 낮음 | 중간 | 중간 | 높음 |
| 다중 에이전트 | 어려움 | 불가 | 불가 | 가능 |
| 동적 단계 수 | 가능 | 불가 | 가능 | 가능 |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 컴포넌트 | 상태 | 멀티스텝과의 관련성 |
|---------|------|--------------------|
| useScenarioOrchestration.ts | 멀티스텝 상태 머신 구현됨 | 핵심: 단계 상태, 타이밍 관리 |
| usePPTScenario.ts | PPT 시나리오 특화된 단계 추적 | 중간: 단계 구조 일부 재사용 |
| useSlideOutlineHITL.ts | HITL 사용자 승인 플로우 | 중간: 승인 로직 활용 가능 |
| 3-Panel Layout | 우측 사이드바 공간 있음 | 높음: 진행률 표시 영역 |
| Radix UI | 아코디언, 슬라이더 기본 제공 | 높음: UI 컴포넌트 기본 |
| NotificationContext | 전역 상태 및 알림 | 높음: 단계 완료/에러 알림 |

### 추천 전략: "패턴 A (체크리스트) + 패턴 B (스텝 바) 하이브리드"

**선택 이유**:

1. **현재 아키텍처 활용**: useScenarioOrchestration.ts의 단계 상태를 그대로 활용 가능
2. **모바일 친화성**: 체크리스트(수직) + 스텝 바(수평) 조합으로 반응형 대응 가능
   - 데스크톱: 우측 사이드바에 체크리스트 (패턴 A)
   - 모바일: 상단 스텝 바 (패턴 B)
3. **PPT 생성 프로세스와 맞음**: PPT는 현재 여러 단계(분석 → 계획 → 생성 → 다운로드)를 거침
4. **확장 가능성**: 향후 다른 에이전트 시나리오 추가 시, 동일 컴포넌트 재사용

### 세부 설계 방안

**Phase 1: 기본 체크리스트 구현 (데스크톱)**

우측 사이드바에 다음 구조:
```
Progress: [====-->  ] 60%

단계 진행:
☐ 요구사항 분석
✓ 콘텐츠 계획
⟳ PPT 생성 중... (스피너)
○ 검수 대기
○ 다운로드
```

**Phase 2: 반응형 스텝 바 추가 (모바일)**

모바일에서는 상단에 수평 스텝 바:
```
[1. 분석]--[2. 계획]--[3. 생성(진행중)]--[4. 검수]--[5. 다운로드]
```

**Phase 3: 단계별 상세 정보 표시**

각 단계 클릭 시:
- 해당 단계의 도구 호출 목록 표시
- 진행 로그 (실시간 업데이트)
- 예상 소요 시간

**Phase 4: 동적 단계 추가 (향후)**

Bolt.new처럼 "Plan 단계"에서 사용자가 단계 승인:
- "다음 단계 미리보기" 섹션
- 각 단계 수정/삭제 버튼

### 구현 아키텍처

```
Layout (3-panel)
├── Left: Chat Messages
├── Center: Content/Preview
└── Right Sidebar: Progress Panel (새로 추가)
    ├── Header: "진행 상황"
    ├── Progress Bar: Visual %
    ├── Step List
    │   ├── Step 1
    │   │   ├── Status Icon (✓/⟳/○)
    │   │   ├── Step Name
    │   │   └── Collapse (show details)
    │   │       ├── Tool Calls
    │   │       └── Logs
    │   ├── Step 2
    │   └── ...
    └── Footer: Estimated Time
```

### Acceptance Criteria

멀티스텝 진행 표시가 완성되려면 다음을 충족해야 함:

1. **진행률 표시**: 데스크톱에서는 우측 사이드바에 진행률 바(0-100%)와 함께 "X/Y 단계 완료" 텍스트 표시

2. **단계 목록**: 각 단계를 리스트로 표시하되, 상태를 아이콘으로 구분(○ 대기 / ⟳ 진행 중 / ✓ 완료 / ✗ 에러)

3. **실시간 업데이트**: 에이전트가 단계를 진행할 때마다, UI가 지연 없이 즉시 업데이트될 것

4. **단계별 상세 정보**: 사용자가 각 단계를 클릭하면, 그 단계의 도구 호출, 생성된 콘텐츠, 실시간 로그를 볼 수 있을 것

5. **모바일 대응**: 모바일 환경에서는 상단 수평 스텝 바로 표시되고, 탭 시 상세 정보 모달 또는 슬라이드업 패널이 표시될 것

6. **예상 시간 표시**: 각 단계별 예상 소요 시간을 표시하고, 진행됨에 따라 업데이트할 것(선택사항)

7. **에러 상태 명확화**: 단계 실패 시, 빨간색 경고와 함께 에러 메시지 및 재시도 버튼이 표시될 것

8. **성능**: 50개 이상의 단계를 표시할 때도 스크롤 성능이 부드러워야 하며, 가상화(virtualization) 고려

## Key Considerations

### 단계 정의의 유연성
- 현재는 PPT 시나리오에 맞게 단계가 고정되어 있으나, 향후 다른 에이전트 시나리오 추가 시 단계를 동적으로 정의할 수 있는 구조 필요
- 예: `steps: [{ name: string, type: "thinking" | "tool" | "validation", ... }]`

### 시간 표시의 정확성
- 예상 시간은 첫 실행 후 학습된 데이터로 점진적 개선
- 초기에는 고정값(예: "약 2분") 표시, 정확도 향상 후 동적 계산

### 사용자 피드백
- 단계가 오래 진행 중일 때 ("5분 이상"), ETA 또는 "작업 중..." 메시지로 사용자 불안감 해소

### 접근성
- 진행 상황을 아이콘뿐 아니라 텍스트로도 표시 (스크린 리더 지원)
- 키보드 네비게이션으로 각 단계 선택 가능

### 브랜드 일관성
- 진행률 바: #FF3C42 (Pretendard 폰트)
- 배경: 흰색 또는 #FAFAFA

## Recent Updates

| 날짜 | 업데이트 | 참고 |
|------|---------|------|
| 2025-02-15 | 문서 최초 작성 | Claude Haiku 4.5 |
| 2025-02-15 | Claude Cowork/GitHub Copilot 패턴 분석 완료 | 체크리스트 vs 스텝 바 |
| 2025-02-15 | KonaI-Agent 하이브리드 전략 수립 | 데스크톱(패턴 A) + 모바일(패턴 B) |
| 2025-02-15 | 3-panel 레이아웃과의 통합 계획 | 우측 사이드바 활용 |

## References

### Vault References
- `/mnt/리서치/Insights/agent-ui/patterns/tool-call-visualization.md` - 각 단계의 도구 호출 표시
- `/mnt/리서치/Insights/agent-ui/patterns/thinking-block-design.md` - 사고 단계와의 연계
- `/mnt/리서치/Insights/agent-ui/patterns/error-recovery-patterns.md` - 에러 단계 처리

### External References

[^1]: Claude Cowork official documentation (internal Anthropic resource)

[^2]: [GitHub Copilot Workspace User Manual](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/overview.md), [GitHub Next - Copilot Workspace](https://githubnext.com/projects/copilot-workspace), [Visual Studio Magazine - Copilot Planning Feature](https://visualstudiomagazine.com/articles/2025/10/23/hands-on-with-new-visual-studio-copilot-planning-feature-preview.aspx)

[^3]: [Bolt.new Support - Plan and Discussion Modes](https://support.bolt.new/best-practices/discussion-mode), [Bolt.new Blog - Inside V2](https://bolt.new/blog/inside-bolt-v2-hidden-power-features), [Bolt.new Official](https://bolt.new)

[^4]: [Cursor IDE - Developing with Cursor and Agent Protocol](https://docs.ag-ui.com/tutorials/cursor), [APIdog - Cursor Agent Mode Guide](https://apidog.com/blog/how-to-use-cursor-agent-mode-for-ai-powered-coding-and-api-workflows/), [Analytics Vidhya - Cursor Agent Tutorial](https://www.analyticsvidhya.com/blog/2025/07/cursor-agent-guide/), [Cursor.fan - Cursor AI Agents Introduction](https://www.cursor.fan/tutorial/HowTo/introduction-to-cursor-ai-agents/)

[^5]: useScenarioOrchestration.ts - KonaI-Agent 현재 코드베이스의 멀티스텝 상태 머신 구현
