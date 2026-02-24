---
type: insight-synthesis
topic_id: tool-call-visualization
topic_name: "도구 호출 시각화 패턴"
category: agent-ui
document_level: specific
parent_broad:
  - agent-reasoning-visualization
catalog_components:
  - tool_call_display
tags:
  - insight
  - agent-ui
  - pattern
  - tool-call
  - visualization
  - tracing
  - mcp
  - ag-ui
status: current
confidence: high
last_updated: "2026-02-23"
source_products:
  - claude
  - openai
  - cursor
  - windsurf
  - copilot-cli
source_files: []
auto_update:
  enabled: true
  keywords:
    - tool call visualization
    - tool invocation
    - function calling UI
    - MCP tool display
    - AG-UI protocol
    - toolInvocation rendering
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 도구 호출 시각화 패턴

## TL;DR

- 도구 호출 UI의 업계 표준은 **인라인 확장형(Inline Expandable)** 패턴으로 수렴 중: Claude Code는 도구명+시제 기반 상태+결과 축소, ChatGPT는 상태 레이블("Searching...")+결과 인라인 임베딩, Cursor/Windsurf는 파일 참조 pill+diff 뷰를 조합 [^1][^2][^3]
- **Vercel AI SDK 5.0+의 `message.parts` 배열**이 도구 호출 렌더링의 사실상 React 표준: 4단계 상태(`input-streaming` → `input-available` → `output-available` / `output-error`)로 점진적 UI 업데이트 지원 [^4]
- **AG-UI Protocol**은 `TOOL_CALL_START → ARGS(delta) → END → RESULT` 4-이벤트 라이프사이클로 프레임워크 독립 표준을 제시하며, CopilotKit의 `useRenderToolCall` 훅으로 React 통합 [^5]
- **GitHub Copilot CLI의 permission elevation 다이얼로그**: autopilot 모드에서 위험 도구 실행 전 리스크 레벨(MODERATE/HIGH) 표시 + 범위 지정 승인(once/session/always) — KonaI-Agent의 ApprovalGate risk-based rendering과 직접 연계 가능 [^6]
- KonaI-Agent는 기존 `TOOL_METADATA`(30+ 도구 정의), `usePPTScenario` 단계 추적, `ApprovalGate` 승인 컴포넌트를 재활용하여 **인라인 확장형 + 상태 레이블 + 권한 게이트** 하이브리드 패턴 구현 권장 [^7]

---

## Overview

도구 호출 시각화(Tool Call Display)는 AI 에이전트가 외부 도구(파일 읽기, 코드 실행, 웹 검색, 데이터베이스 질의 등)를 호출할 때 사용자가 이 과정을 실시간으로 추적하고 검증할 수 있도록 하는 UI 패턴이다. 에이전트 시스템의 **투명성(Transparency)**과 **신뢰도(Trustworthiness)**를 좌우하는 핵심 UX 요소다.

2025-2026년 사이에 이 영역은 급격히 성숙했다. Claude Code, ChatGPT, Cursor, Windsurf 등 주요 AI 코딩 도구들이 각자의 방식으로 도구 호출을 시각화하고, Vercel AI SDK와 AG-UI Protocol이 렌더링 표준을 제시하면서 패턴이 수렴하는 추세다. 특히 MCP(Model Context Protocol) 생태계의 확장으로 서드파티 도구 호출이 급증하면서, 도구 자동 감지 → 권한 승인 → 실행 시각화 → 결과 검증의 전체 흐름을 다루는 통합 UI의 중요성이 높아졌다.

KonaI-Agent에서는 PPT 생성, 매출 분석 등 멀티스텝 에이전트 시나리오에서 다수의 도구(ERP 연결, 데이터 조회, 슬라이드 계획 등)를 순차/병렬로 호출하므로, 각 도구 호출의 상태를 실시간 피드백하고 HITL 개입 시점을 명확히 표시하는 UI가 필수적이다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| Product | 표시 위치 | 상태 표현 | 매개변수 공개 | 결과 표시 | 에러/재시도 | 권한 관리 | 프로토콜 |
|---------|----------|----------|-------------|----------|-----------|----------|---------|
| **Claude Code** | 인라인 축소형 | 시제 기반(진행:동명사, 완료:과거형) | 간단 요약(파일경로 등) | 전용 뷰어(구문 강조, 인라인 diff) | 에러 메시지 표시 | 계층적 권한(deny→allow→ask) | 자체 |
| **ChatGPT** | 인라인 상태 레이블 | "Searching...", "Analyzing..." | 숨겨짐(보안) | 인라인 임베딩 + Apps SDK iframe | 상태 레이블만 | 액션별 확인 프롬프트 | Responses API |
| **Cursor** | 컴포저 패널 내 스트리밍 | 실시간 액션 설명 | 파일 pill/chip 참조 | 라인 단위 diff 뷰 | 에이전트 루프 자동 재시도 | 디렉토리 신뢰 경계 | 자체 |
| **Windsurf** | Cascade 패널 | 로딩 인디케이터 + MCP별 상태 | 파일 탐색기 드래그앤드롭 | 청크별 diff + 수락/거절 | 시각적 diff 동결 감지 | MCP별 수동 활성화 | MCP |
| **GitHub Copilot** | 에이전트 모드 단계별 표시 | 도구 선택→실행→완료 단계 | 도구 목록 드롭다운(렌치 아이콘) | 단계별 결과 누적 | 권한 상승 다이얼로그 | 리스크 기반 3-tier(once/session/always) | MCP |
| **Vercel AI SDK** | `message.parts` 배열 | 4단계 상태 머신 | 스트리밍 input delta | `output` 필드 | `output-error` + `errorText` | `approval-requested` 상태 | AI SDK Data Stream |
| **AG-UI/CopilotKit** | `useRenderToolCall` 훅 | pending→executing→complete | ARGS 이벤트 delta 스트리밍 | RESULT 이벤트 | 이벤트 기반 에러 전파 | 도구별 커스텀 | AG-UI SSE |

### 경쟁사별 상세 분석

#### Claude Code — 시제 기반 그룹핑 + 전용 결과 뷰어

Claude Code는 도구 호출을 메시지 흐름 내에 **축소 가능한(collapsible) 그룹**으로 표시한다. 핵심 차별점은 시제(tense) 기반 상태 표현이다: 진행 중에는 현재진행형("Reading", "Searching for"), 완료 시에는 과거형("Read", "Searched for")으로 전환된다. 축소 상태에서도 현재 처리 중인 파일 경로나 검색 패턴이 요약 라인 아래에 표시되어 사용자가 진행 상황을 파악할 수 있다.

결과 표시에서는 도구 유형별 전용 뷰어를 사용한다: Read 호출은 구문 강조된 코드 + 라인 번호, Edit 호출은 인라인 diff(추가/삭제 하이라이팅), Search 패턴은 인용 부호로 감싸서 표시한다. 권한 관리는 `deny → allow → ask` 계층 구조로, 프로젝트 설정이 사용자 설정을 오버라이드할 수 있다.

**왜 이 방식인가**: CLI/IDE 환경에서 개발자는 에이전트가 어떤 파일을 읽고 수정하는지 정확히 알아야 한다. 시제 기반 상태 전환은 스크롤하면서도 진행/완료를 직관적으로 구분할 수 있게 하며, 전용 뷰어는 코드 컨텍스트에서의 변경 사항을 즉시 검증하게 한다.

*참고 URL*: https://code.claude.com/docs/en/overview, https://skywork.ai/blog/permission-model-claude-code-vs-code-jetbrains-cli/

#### ChatGPT — 최소 상태 레이블 + Apps SDK 인터랙티브 결과

ChatGPT는 도구 호출을 **최소한의 상태 레이블**로 표시한다. "Searching...", "Analyzing..." 같은 동작 설명이 로딩 인디케이터와 함께 나타나고, 완료 후 결과가 대화 흐름에 인라인으로 임베딩된다. 2025년 도입된 Apps SDK는 MCP를 확장하여 도구 결과를 **sandboxed iframe** 내 인터랙티브 웹 컴포넌트로 렌더링할 수 있게 했다. Data tool(데이터 조회)과 Render tool(UI 생성)을 분리하여 모델이 데이터에 지능을 적용한 후 시각화를 결정하는 패턴이 권장된다.

ChatGPT Agent 모드(CUA 기반)에서는 가상 컴퓨터에서 작업을 실행하며, 화면 내레이션(on-screen narration)으로 진행 상황을 실시간 표시한다. 위험 작업 전에는 사용자에게 권한을 요청하며, 사용자는 언제든 개입하거나 중단할 수 있다.

**왜 이 방식인가**: B2C 대중 시장에서 도구 내부 매개변수 노출은 혼란을 주므로 숨기고, 대신 "무엇을 하고 있는지"만 자연어로 설명한다. Apps SDK는 서드파티 도구의 결과를 풍부한 인터랙티브 UI로 표현할 수 있게 확장성을 열었다.

*참고 URL*: https://developers.openai.com/apps-sdk/build/chatgpt-ui, https://openai.com/index/introducing-chatgpt-agent/

#### Cursor — 컴포저 패널 스트리밍 + 파일 참조 pill

Cursor는 Composer 모드(Cmd+I)에서 멀티파일 에이전트 작업을 수행하며, 도구 호출을 **실시간 스트리밍 상태 메시지**와 **파일 참조 pill/chip**으로 표시한다. "searching codebase", "editing files" 같은 액션 설명이 실시간으로 스트리밍되고, 관련 파일이 인라인 pill로 표시된다. 변경 결과는 green/red 하이라이팅의 diff 뷰로 보여준다.

Cursor 2.0의 멀티에이전트 구조에서는 각 에이전트가 사이드바에 별도 항목으로 나타나며 running/waiting/completed 상태 아이콘이 표시된다. Planning → Executing → Applying → Verification → Adjustment 루프가 시각적으로 추적 가능하다.

**왜 이 방식인가**: 코딩 워크플로우에서는 "어떤 파일을 수정하는가"가 가장 중요한 정보다. 파일 pill은 파일 트리 탐색 없이도 맥락을 유지하게 하고, 라인 단위 diff는 변경 사항의 정밀한 검증을 가능하게 한다.

*참고 URL*: https://prismic.io/blog/cursor-ai, https://www.infoq.com/news/2025/11/cursor-composer-multiagent/

#### GitHub Copilot — MCP 도구 자동 감지 + 리스크 기반 권한 상승

GitHub Copilot Agent Mode는 MCP 서버를 자동 감지하고, 렌치(wrench) 아이콘 드롭다운으로 사용 가능한 도구 목록을 표시한다. 도구 호출 시에는 단계별 진행 상태를 표시하며, **위험 수준(MODERATE/HIGH)**에 따라 권한 상승 다이얼로그를 노출한다. CLI 버전(v0.0.414+)에서는 `--allow-tool`, `--deny-tool` 플래그로 세밀한 도구 권한 관리가 가능하다.

핵심 패턴은 **2-tier 신뢰 모델**: 내장 도구는 기본 신뢰(경량 승인), MCP/외부 도구는 명시적 활성화 + 호출별 승인이 필요하다. 승인 범위는 once(일회)/session(세션)/always(항상)의 3단계로 구분된다.

**왜 이 방식인가**: 오픈소스 MCP 서버의 보안 위험(CVE-2025-53773 사례)을 고려하여 도구 실행 전 명시적 확인을 요구한다. 리스크 레벨 표시는 사용자가 위험도를 즉시 판단하고 적절한 범위로 승인할 수 있게 한다.

*참고 URL*: https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp, https://deepwiki.com/github/copilot-cli/3.10-autopilot-and-plan-modes

#### Vercel AI SDK — `message.parts` 기반 타입 안전 렌더링

Vercel AI SDK 5.0+는 도구 호출을 `message.parts` 배열의 타입화된 파트(typed part)로 노출한다. 각 도구는 `tool-{toolName}` 타입으로 구분되며, 4단계 상태 머신(`input-streaming` → `input-available` → `output-available` / `output-error`)으로 점진적 UI 업데이트를 지원한다. `approval-requested` 상태는 사용자 확인이 필요한 도구에 대한 명시적 지원을 제공한다.

도구 입력(arguments)은 기본적으로 스트리밍되어, UI가 매개변수 생성 과정을 실시간으로 표시할 수 있다. React 렌더링에서는 `parts.map()` → `switch(part.type)` → `switch(part.state)` 패턴으로 도구별 맞춤 UI를 구현한다.

**왜 이 방식인가**: React/Next.js 생태계에서 가장 자연스러운 통합 방식이다. 타입 안전 상태 머신은 누락된 상태 처리 없이 모든 도구 호출 라이프사이클을 커버하며, 입력 스트리밍은 사용자의 대기 불안(Waiting Anxiety)을 줄인다.

*참고 URL*: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage, https://vercel.com/blog/ai-sdk-5

#### AG-UI Protocol / CopilotKit — 프레임워크 독립 이벤트 기반 표준

AG-UI Protocol은 도구 호출을 4-이벤트 라이프사이클(`TOOL_CALL_START` → `TOOL_CALL_ARGS` → `TOOL_CALL_END` → `TOOL_CALL_RESULT`)로 정의한다. `TOOL_CALL_ARGS`는 delta 청크로 매개변수를 점진적으로 스트리밍하며, 각 이벤트에 `tool_call_id`로 상관관계를 유지한다. CopilotKit의 `useAgent` 훅과 `useRenderToolCall` 훅으로 React 통합을 제공하며, LangGraph, CrewAI, AG2 등 다양한 에이전트 프레임워크와 호환된다.

Vercel AI SDK와의 핵심 차이: AG-UI는 **프로토콜 우선(protocol-first)** 접근으로 프레임워크에 독립적이고, Vercel AI SDK는 **라이브러리 우선(library-first)** 접근으로 React/Next.js에 최적화되어 있다.

**왜 이 방식인가**: 멀티 에이전트 시스템에서 Python 백엔드와 React 프론트엔드가 분리된 환경에서, 프로토콜 수준의 표준화가 필요하다. SSE 기반 이벤트 스트리밍은 WebSocket보다 단순하고 HTTP 인프라와 호환된다.

*참고 URL*: https://docs.ag-ui.com/introduction, https://docs.copilotkit.ai/reference/hooks/useAgent

---

## 패턴 분류 및 트레이드오프

### 패턴 A: 인라인 확장형 (Inline Expandable)

메시지 흐름 내에서 도구 호출을 축소/확대 가능한 섹션으로 표시하는 패턴. 도구명 + 상태 아이콘이 기본 표시되고, 클릭/토글 시 매개변수와 결과를 확인할 수 있다.

- **대표**: Claude Code, Claude.ai 웹 검색
- **장점**: 대화 흐름 유지, 점진적 공개(Progressive Disclosure), 모바일 친화적, 구현 단순
- **단점**: 병렬 도구 호출 시각화 제한, 복잡한 중첩 JSON 매개변수 표시 어려움
- **적합한 상황**: 순차적 도구 호출 중심, 일반 사용자 대상, 채팅 인터페이스 통합

### 패턴 B: 상태 레이블 + 인터랙티브 결과 (Status Label + Interactive Result)

최소한의 상태 텍스트("Searching...", "Analyzing...")로 진행 상황을 표시하고, 결과를 인터랙티브 위젯(iframe, 차트, 데이터 테이블)으로 임베딩하는 패턴.

- **대표**: ChatGPT, OpenAI Apps SDK
- **장점**: 깔끔한 UX, 비기술 사용자 친화적, 결과의 풍부한 인터랙션
- **단점**: 도구 호출 투명성 낮음, 디버깅 어려움, iframe 보안 관리 필요
- **적합한 상황**: B2C 대중 시장, 도구 내부보다 결과에 집중하는 워크플로우

### 패턴 C: 파일 참조 pill + Diff 뷰 (File Reference + Diff View)

도구가 참조/수정하는 파일을 인라인 pill/chip으로 표시하고, 변경 결과를 라인 단위 diff로 보여주는 패턴. 코딩 도구에 특화.

- **대표**: Cursor, Windsurf
- **장점**: 파일 변경 추적에 최적, 라인 단위 수락/거절, 멀티파일 작업 가시성
- **단점**: 코딩 외 도메인에 부적합, 비기술 사용자에게 복잡
- **적합한 상황**: AI 코딩 도구, 파일 기반 작업 중심 워크플로우

### 패턴 D: 리스크 기반 권한 게이트 (Risk-Based Permission Gate)

도구 호출 전에 위험 수준을 평가하여, 저위험은 자동 실행, 고위험은 사용자 승인을 요구하는 패턴. 도구 시각화와 권한 관리를 통합.

- **대표**: GitHub Copilot Agent Mode, Claude Code 권한 모델
- **장점**: 보안과 UX의 균형, 범위 지정 승인(once/session/always), 자동화 가능
- **단점**: 승인 피로(approval fatigue), 리스크 분류 기준 설정 필요
- **적합한 상황**: 외부 도구/MCP 통합, 엔터프라이즈 보안 요구사항

### 트레이드오프 요약

| | 투명성 | UX 단순성 | 모바일 호환 | 구현 난이도 | 병렬 호출 | 보안 통합 |
|---|---|---|---|---|---|---|
| **패턴 A: 인라인 확장형** | 중간 | 높음 | 높음 | 낮음 | 제한적 | 낮음 |
| **패턴 B: 상태 레이블** | 낮음 | 매우 높음 | 높음 | 낮음 | 불가 | 중간 |
| **패턴 C: 파일+Diff** | 높음 | 낮음 | 낮음 | 중간 | 가능 | 낮음 |
| **패턴 D: 권한 게이트** | 높음 | 중간 | 중간 | 중간 | 가능 | 높음 |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 |
|----------|-----------|
| `TOOL_METADATA` (30+ 도구 정의) | **높음** — 도구명, 진행/완료 레이블, 아이콘, subtools 메타데이터 이미 정의됨 |
| `usePPTScenario` / `useScenarioOrchestration` | **높음** — 단계 추적 상태 머신, 완료 콜백 패턴 재사용 가능 |
| `ApprovalGate` (toast/inline/modal) | **높음** — risk-based rendering 3-tier가 이미 구현됨. 도구 호출 전 권한 게이트로 직접 사용 가능 |
| `SCENARIO_TODOS` + `getScenarioTodosWithStatus` | **중간** — 전체 작업 진행률 표시의 상위 레이어로 활용 가능 |
| `NotificationContext` | **중간** — 전역 도구 호출 알림(에러, 완료)에 활용 가능 |
| Radix UI (`Collapsible`, `Accordion`) | **높음** — 인라인 확장형 UI의 기본 프리미티브 |

### 권장 접근: "인라인 확장형 + 상태 레이블 + 권한 게이트" 하이브리드

기존 코드베이스의 강점을 최대한 활용하면서, 업계 표준 패턴을 조합하는 하이브리드 접근을 권장한다.

**Phase 1 (MVP): 기본 도구 호출 표시**

`<ToolCallDisplay>` 컴포넌트를 메시지 흐름에 삽입한다:
- `TOOL_METADATA`의 `icon` + `labelRunning`/`labelComplete`로 상태 표시
- Radix UI `Collapsible`로 축소/확대 토글
- 진행 중: 스피너 + 현재진행형 레이블 (예: "📊 데이터 조회 중...")
- 완료: 체크 아이콘 + 과거형 레이블 (예: "✅ 데이터 조회 완료")
- 실패: 경고 아이콘 + 에러 메시지

**Phase 2 (확장): 매개변수 + 결과 + Sub-tool 표시**

- 확장 시 매개변수 요약 표시 (도구 타입별 포맷팅)
- `subtools` 배열이 있는 도구(예: `financial_data_collection`)는 중첩 진행 표시
- 결과는 도구 유형별 전용 렌더러: 데이터 조회 → 미니 테이블, 웹 검색 → 링크 목록, 분석 → 인사이트 카드

**Phase 3 (고급): 권한 게이트 + 병렬 실행 시각화**

- `ApprovalGate` 통합: 위험 도구 호출 전 risk level에 따라 toast/inline/modal 렌더링
- 병렬 도구 호출(`parallel_data_query`)을 그룹으로 묶어 동시 진행 상태 표시
- 각 병렬 작업의 개별 진행률과 전체 완료율 표시

### 이 접근을 권장하는 이유

1. **기존 자산 극대화**: `TOOL_METADATA`의 30+ 도구 정의와 `ApprovalGate`의 3-tier 승인 UI를 재활용하여 구현 비용 최소화
2. **데모 임팩트**: PPT 시나리오에서 도구 호출이 실시간으로 시각화되면 에이전트의 작업 과정 투명성을 극적으로 보여줄 수 있음
3. **점진적 복잡도**: Phase 1은 단순 상태 표시, Phase 2는 상세 정보, Phase 3은 권한+병렬 — 각 단계가 독립적으로 가치를 제공
4. **경쟁사 대비 차별화**: Claude Code의 확장형 + GitHub Copilot의 권한 게이트 + 기존 ApprovalGate의 risk-based rendering을 통합한 하이브리드는 업계에서 아직 드문 조합

### Acceptance Criteria

- [ ] 에이전트가 도구를 호출할 때마다, 사용자는 (1) 어떤 도구인지, (2) 현재 실행 중/완료/실패 상태를 즉시 구분할 수 있어야 함
- [ ] 도구 호출 영역을 클릭/토글하여 매개변수와 결과를 축소/확대할 수 있어야 함
- [ ] 도구 실행 중에는 명확한 로딩 상태(스피너 또는 애니메이션)와 현재진행형 레이블을 표시할 것
- [ ] 도구 호출 실패 시 에러 메시지를 표시하고, 가능하면 재시도 옵션을 제공할 것
- [ ] 도구 호출 UI가 메시지 흐름과 자연스럽게 통합되어, 대화 흐름을 방해하지 않을 것
- [ ] `subtools`가 있는 도구는 하위 단계의 진행 상태를 중첩 표시할 것
- [ ] 기존 `TOOL_METADATA`의 도구 정의를 그대로 활용하여 새로운 도구 추가 시 메타데이터만 추가하면 되도록 할 것
- [ ] 키보드 내비게이션과 스크린 리더 지원 (Radix UI 접근성 준수)

---

## Key Considerations

### 데이터 모델: Vercel AI SDK `parts` 패턴 채택

KonaI-Agent는 Next.js 15 + React 18 스택이므로, Vercel AI SDK의 `message.parts` 모델을 참조하여 도구 호출 데이터를 구조화하는 것이 자연스럽다. 핵심은 도구 호출을 메시지의 일부(part)로 모델링하되, 각 part가 독립적인 상태(`pending` → `running` → `completed` / `failed`)를 가지는 것이다. 현재 `ToolType`과 `TOOL_METADATA`가 이미 이 역할을 부분적으로 수행하므로, `ToolCallPart` 인터페이스를 추가하여 상태 머신을 명시화하면 된다.

### ApprovalGate 연동: 도구별 위험 수준 매핑

기존 `ApprovalGate`의 `riskLevel` (low/medium/high/critical)을 도구별로 매핑하면 GitHub Copilot의 권한 상승 패턴을 자연스럽게 구현할 수 있다. 예: 데이터 조회 도구는 `low` (자동 실행), ERP 연결은 `medium` (인라인 카드), 데이터 삭제는 `high` (모달 승인). `TOOL_METADATA`에 `riskLevel` 필드를 추가하여 도구 등록 시점에 위험 수준을 선언하는 방식이 유지보수에 유리하다.

### 성능: 가상화와 메모이제이션

PPT 시나리오에서 15+ 도구 호출이 발생하고, 매출 분석 시나리오에서는 30+ 도구 호출이 가능하다. 각 `ToolCallDisplay` 컴포넌트를 `React.memo`로 메모이제이션하고, 긴 대화에서는 뷰포트 밖의 도구 호출을 가상화(virtualization)하여 렌더링 성능을 유지해야 한다. 특히 `subtools` 중첩 표시는 불필요한 리렌더링을 유발할 수 있으므로 상태 관리에 주의가 필요하다.

### 보안: 민감 정보 마스킹

ERP 연결 정보, SPARQL 쿼리, 재무 데이터 등 민감한 매개변수가 도구 호출에 포함될 수 있다. 매개변수 표시 시 API 키, 토큰, 비밀번호 등을 자동 마스킹하는 필터를 적용하고, 파일 경로는 상대 경로로 변환하여 표시해야 한다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다. 수동 편집 금지. -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-23 | 전면 리서치 업데이트 | 6개 제품 비교, Vercel AI SDK/AG-UI Protocol 표준 분석, GitHub Copilot 권한 상승 패턴 추가, KonaI-Agent 적용 전략 전면 개편 | tool-call, mcp, ag-ui, vercel-ai-sdk |

---

## References

### Vault
- [^7]: `src/components/features/agent-chat/components/ToolCall/constants.ts` — TOOL_METADATA, HITL_TOOLS 등 기존 도구 메타데이터 정의
- [[Insights/agent-ui/agent-reasoning-visualization|추론 과정 시각화 패턴]] — 도구 호출 시각화의 상위 맥락 (사고 vs 실행 시각화 분리)
- [[Insights/agent-ui/patterns/approval-gate-component|승인 게이트 컴포넌트]] — ApprovalGate risk-based rendering 패턴 (도구 권한 게이트 연동)

### External
- [^1]: [Claude Code Documentation](https://code.claude.com/docs/en/overview) — 도구 호출 축소형 그룹, 시제 기반 상태 표현, 전용 결과 뷰어
- [^2]: [ChatGPT Agent / Apps SDK](https://developers.openai.com/apps-sdk/build/chatgpt-ui) — 상태 레이블, Apps SDK iframe 렌더링, Data/Render tool 분리
- [^3]: [Cursor 2.0 Multi-Agent](https://www.infoq.com/news/2025/11/cursor-composer-multiagent/) — 파일 pill, diff 뷰, 멀티에이전트 상태 사이드바
- [^4]: [Vercel AI SDK: Chatbot Tool Usage](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage) — `message.parts`, 4단계 상태 머신, input 스트리밍
- [^5]: [AG-UI Protocol: Events](https://docs.ag-ui.com/sdk/python/core/events) — TOOL_CALL_START/ARGS/END/RESULT 이벤트 라이프사이클
- [^6]: [GitHub Copilot: Agent Mode with MCP](https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp) — MCP 도구 자동 감지, 렌치 아이콘 드롭다운, 권한 상승 다이얼로그
- [Windsurf Cascade Documentation](https://docs.windsurf.com/windsurf/cascade/cascade) — MCP별 로딩 상태, 컨텍스트 윈도우 미터, diff 수락/거절
- [Claude Code Permission Model](https://skywork.ai/blog/permission-model-claude-code-vs-code-jetbrains-cli/) — deny→allow→ask 계층 권한
- [CopilotKit useAgent Hook](https://docs.copilotkit.ai/reference/hooks/useAgent) — AG-UI React 통합, useRenderToolCall

---

*Last synthesized: 2026-02-23 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
