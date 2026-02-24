---
type: insight-synthesis
topic_id: approval-gate-component
topic_name: "승인 게이트 컴포넌트 설계"
category: agent-ui
document_level: specific
parent_broad:
  - hitl-approval-patterns
catalog_components:
  - approval_rejection
tags:
  - insight
  - agent-ui
  - pattern
  - approval
  - hitl
  - permission
  - elicitation
  - async-hitl
status: draft
confidence: high
last_updated: "2026-02-21"
source_products:
  - claude-code
  - claude-cowork
  - github-copilot
  - chatgpt
  - salesforce-agentforce
  - cursor
  - mcp-sdk
  - crewai
  - langgraph
  - vercel-ai-sdk
source_files:
  - "src/hooks/useSlideOutlineHITL.ts"
  - "src/hooks/usePPTScenario.ts"
  - "src/hooks/useScenarioOrchestration.ts"
auto_update:
  enabled: true
  keywords:
    - "approval gate"
    - "human-in-the-loop"
    - "HITL"
    - "elicitation"
    - "interrupt"
    - "plan preview"
  feeds:
    - "https://github.com/modelcontextprotocol/typescript-sdk/releases.atom"
    - "https://github.com/vercel/ai/releases.atom"
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 승인 게이트 컴포넌트 설계

## TL;DR

- Claude Code Permission Tiers (Allow Once / Session / Always)는 가장 성숙한 승인 모델이며, Claude Code Security Preview(Feb 2026)에서 다단계 self-adversarial 검증 + 인간 게이팅으로 확장됨 [^1][^7]
- MCP SDK v1.27.0의 **Elicitation**이 프로토콜 레벨 HITL를 표준화 — `elicitation/create` JSON-RPC로 도구 실행 중 JSON Schema 기반 구조화 입력을 요청 가능 [^8]
- CrewAI, LangGraph, Vercel AI SDK가 동시에 async HITL / sequential interrupt / lifecycle callbacks를 출시하여 프레임워크 생태계 전반에서 HITL 인프라 성숙 [^9][^10][^11]
- Claude Code · ChatGPT Deep Research · Cursor CLI가 동시에 "실행 전/중 계획 편집 + 실시간 프리뷰" Live Plan Preview 패턴을 채택 — 승인 게이트가 이진 approve/reject에서 협업적 문서 편집으로 진화 [^12]
- KonaI-Agent는 PPT 시나리오의 HITL 로직을 범용 ApprovalGate로 분리하되, MCP elicitation 호환 스키마와 async 상태 지속을 Phase 1부터 설계에 반영해야 함

---

## Overview

승인 게이트 컴포넌트는 Agent가 잠재적으로 영향력 있는 작업을 수행하기 전에 사용자 의사 결정을 중개하는 UI 패턴이다. HITL 시스템의 핵심 제어점으로, 자동화 수준(autonomy)과 사용자 신뢰도 간의 균형을 결정한다.

2026년 2월 셋째 주에 MCP SDK의 Elicitation 표준화, CrewAI의 async HITL, LangGraph의 sequential interrupt 수정, Vercel AI SDK의 agent lifecycle callbacks, 그리고 3개 이상 경쟁사의 Live Plan Preview 동시 채택이 일어나면서, HITL 생태계에 중대한 전환이 발생했다. 기존의 "Agent가 제안 → 사용자가 yes/no" 이진 모델에서, "Agent가 계획을 초안 → 사용자가 인라인 편집 → Agent가 반영 → 실행 중 개입 가능"한 협업 모델로 패러다임이 이동하고 있다. KonaI-Agent는 현재 `useSlideOutlineHITL.ts`에서 PPT-specific 승인 로직이 결합되어 있으나, 이 새로운 패러다임을 수용하는 범용 ApprovalGate 컴포넌트로 리팩토링이 필요하다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| Product / Framework | 승인 메커니즘 | UI 패턴 | 주요 특징 | Async 지원 | 왜 이 방식인가 (요약) | Source |
|---------------------|-------------|---------|---------|-----------|---------------------|--------|
| Claude Code | Permission Tiers + Security Gating | Modal + Button Set | Once/Session/Always + 다단계 self-adversarial 검증 | - | Session scope으로 "set-and-forget" 회피 + 보안은 항상 인간 게이팅 | [^1][^7] |
| Claude Cowork | Tool-Type Classification | Permit/Deny Buttons | read=auto, write=ask, delete=warning | - | 위험도 차등 처리로 approval fatigue 감소 | [^1] |
| GitHub Copilot Workspace | Multi-Stage Plan Review | Editable Plan View | Spec → Plan → Diff 각 단계 editable | - | early-stage 정정이 downstream 자동 반영 | [^2] |
| ChatGPT Deep Research | Live Plan + Mid-run Pivot | Plan Editor + Progress Tracker | 리서치 계획 편집 + 실행 중 방향 전환 | ✅ | 장시간 리서치에서 중단 없이 방향 수정 | [^12] |
| Salesforce Agentforce | Confidence-Based Escalation | Supervisor Approval Flow | 신뢰도 < threshold → 자동 escalate | ✅ | approval fatigue vs safety 자동 최적화 | [^3] |
| Cursor CLI | Per-Hunk + Plan Mode | Diff Checkboxes + Decision Menu | 변경사항 hunk 단위 accept/reject + 클라우드/로컬 빌드 선택 | - | 세밀한 제어 + 키보드 중심 결정 UI | [^4][^12] |
| **MCP SDK v1.27.0** | Elicitation Protocol | JSON Schema Form / URL Redirect | 도구 실행 중 일시정지 → 구조화 입력 요청 | ✅ | 프로토콜 레벨 HITL 표준화로 모든 MCP 서버가 통일된 방식 사용 | [^8] |
| **CrewAI v1.10.0a1** | Async HITL + Provider Pattern | @human_feedback decorator / Webhook | 비동기 pause/resume, 플러그 가능 provider | ✅ | 장시간 작업에서 human이 즉시 응답 불필요 | [^9] |
| **LangGraph v1.0.9** | Sequential Interrupt | interrupt() + Command(resume=) | 함수형 API에서 다중 순차 interrupt 정상 작동 | ✅ | 다단계 승인 플로우의 정확성 보장 | [^10] |
| **Vercel AI SDK v6.0.97** | ToolLoopAgent Callbacks | 6개 Lifecycle Hooks | onToolCallStart/Finish, onStepStart/Finish 등 | ✅ | agent 루프 내 HITL 삽입 hook point 제공 | [^11] |

### 경쟁사별 상세 분석

#### Claude Code — Permission Tiers + Security Gating [^1][^7]

Claude Code는 3단계 Permission Tier를 기반으로 한 승인 모델을 제공한다:
- **Allow Once**: 현재 action만 허용, 이후 재문의
- **Allow for Session**: 세션 내 동일 도구 재사용 허용, 세션 종료 시 reset
- **Always Allow**: settings.json에 영구 저장

2026년 2월 20일 발표된 **Claude Code Security Preview**에서 이 모델이 보안 검증으로 확장되었다. 5단계 파이프라인(AI Detection → Self-adversarial Re-examination → Severity/Confidence Classification → Human Review Dashboard → Developer Decision)에서 각 단계마다 인간 승인이 필수이며, "developers always make the call" 원칙이 명시되었다. Confidence rating이 finding 단위로 제공되어 사용자가 도구 전체가 아닌 개별 발견에 대해 신뢰를 보정할 수 있다.

**왜 이 방식인가**: Session-scoped permission은 "한 번은 믿지만 계속은 물어본다"는 심리모델을 구현하며, 보안 검증에서는 AI의 self-adversarial 단계로 false positive를 줄여 인간에게 도달하는 항목의 신호 대 잡음 비율을 높인다.

*참고 URL*: [Configure permissions](https://code.claude.com/docs/en/permissions), [Claude Code Security](https://www.anthropic.com/news/claude-code-security)

#### MCP SDK v1.27.0 — Elicitation Protocol [^8]

MCP (Model Context Protocol) TypeScript SDK v1.27.0에서 **Elicitation**이 추가되어 프로토콜 레벨에서 HITL가 표준화되었다. MCP 서버가 도구 실행 중 `elicitation/create` JSON-RPC 메서드로 일시정지하고 사용자에게 구조화된 입력을 요청할 수 있다.

두 가지 모드를 지원한다:
- **Form Mode**: JSON Schema subset(flat object, primitive types)으로 입력 폼 스키마를 정의. 클라이언트가 폼을 생성하고 validation 후 응답. 응답 종류: accept(data 포함) / decline(명시적 거부) / cancel(해제)
- **URL Mode**: 민감한 데이터(OAuth, 결제 등)용. 서버가 URL + elicitationId를 제공하면 클라이언트가 보안 브라우저에서 열기. 데이터가 MCP 클라이언트를 경유하지 않음.

v1.27.0에서는 `createMessageStream()`과 `elicitInputStream()` 스트리밍 메서드가 추가되어 장시간 작업 시나리오에서 실용적으로 사용 가능하다.

**왜 이 방식인가**: 각 MCP 서버가 커스텀 HITL을 구현하면 클라이언트마다 다른 UX가 발생한다. 프로토콜 레벨 표준화로 모든 MCP 서버가 동일한 입력 요청 방식을 사용하고, 클라이언트는 일관된 UI를 제공할 수 있다. JSON Schema 기반이므로 폼 생성이 자동화된다.

*참고 URL*: [MCP Elicitation Spec](https://modelcontextprotocol.io/specification/draft/client/elicitation), [SDK v1.27.0](https://github.com/modelcontextprotocol/typescript-sdk/releases)

#### CrewAI v1.10.0a1 — Async HITL + Provider Pattern [^9]

CrewAI v1.10.0a1(pre-release)에서 비동기 HITL와 플러그 가능 provider 패턴이 도입되었다.

Flow 기반 HITL은 `@human_feedback` 데코레이터로 체크포인트를 설정하고, 승인/거부/수정 중 하나를 받아 분기한다. 엔터프라이즈 환경에서는 Webhook 기반으로 `human_input=True` 태스크가 "Pending Human Input" 상태로 일시정지되고, resume 엔드포인트에서 Bearer/Basic 인증으로 피드백을 수신한다.

핵심 아키텍처 변경은 **provider 패턴 리팩토링**(PR #4361)으로, HITL 메커니즘을 플러그 가능한 추상화로 분리했다. 이를 통해 커스텀 승인 UI, Slack 연동, 외부 티켓 시스템 등을 provider로 교체 가능하다. 상태 직렬화(state persistence)로 비동기 상호작용 간 상태가 완전 보존된다.

**왜 이 방식인가**: 동기 HITL은 인간이 즉시 응답해야 하므로 장시간 작업에 부적합하다. Async HITL로 crew가 pause → 상태 직렬화 → 수 시간/일 후 resume이 가능하며, provider 패턴으로 승인 메커니즘을 교체할 수 있어 엔터프라이즈 배포에 필수적이다.

*참고 URL*: [CrewAI HITL Docs](https://docs.crewai.com/en/learn/human-in-the-loop), [v1.10.0a1](https://github.com/crewAIInc/crewAI/releases/tag/1.10.0a1)

#### LangGraph v1.0.9 — Sequential Interrupt Fix [^10]

LangGraph v1.0.9에서 functional API(`@entrypoint` + `@task`)의 **sequential interrupt 버그**가 수정되었다(PR #6863).

버그: `@task` 함수가 interrupt 전에 실행되면, `Command(resume=value)`로 재개 시 이전 답변이 중복 반환되고 후속 `interrupt()`가 트리거되지 않았다. 원인은 `_scratchpad()`가 `pending_writes` 리스트 참조를 캡처하는데, 자식 task의 `put_writes()`가 리스트 객체를 재할당하여 부모 entrypoint의 클로저에서 소비가 보이지 않게 된 것이다.

수정: root scratchpad만 null resume write를 캡처/소비하도록 변경하여, 자식 task의 리스트 재할당이 영향을 미치지 않도록 했다.

**왜 이 방식인가**: 다단계 승인 플로우("step 1 확인" → "step 2 확인")에서 두 번째 interrupt가 첫 번째 답변을 재사용하면 승인 플로우가 신뢰할 수 없다. 이 수정으로 각 `interrupt()`가 정확히 자신의 인간 입력만 수집하는 것이 보장된다.

*참고 URL*: [LangGraph v1.0.9](https://github.com/langchain-ai/langgraph/releases), [PR #6863](https://github.com/langchain-ai/langgraph/pull/6863)

#### Vercel AI SDK v6.0.97 — ToolLoopAgent Lifecycle Callbacks [^11]

Vercel AI SDK v6.0.97에서 `ToolLoopAgent`에 6개 experimental lifecycle callbacks가 추가되었다:

1. `experimental_onStart` — agent 시작 시 1회
2. `experimental_onStepStart` — 각 LLM 호출 전
3. `experimental_onToolCallStart` — 도구 실행 직전
4. `experimental_onToolCallFinish` — 도구 실행 후 (success/error 구분 + durationMs)
5. `onStepFinish` — 각 step(LLM + 도구) 완료 후
6. `onFinish` — 전체 agent 완료 시

생성자와 메서드 양쪽에서 지정 가능하며, 양쪽 모두 지정 시 생성자 콜백이 먼저 실행된다.

**왜 이 방식인가**: 기존 `ToolLoopAgent`는 불투명(start → result)했다. 이 callbacks로 `onToolCallStart`에서 위험한 도구 실행을 게이팅하고, `onStepStart`에서 단계 간 인간 리뷰를 삽입하며, `onStepFinish`에서 다음 단계 진행 여부를 판단하는 HITL 인프라가 가능하다.

*참고 URL*: [AI SDK v6.0.97](https://github.com/vercel/ai/releases/tag/ai%406.0.97), [ToolLoopAgent Reference](https://ai-sdk.dev/docs/reference/ai-sdk-core/tool-loop-agent)

#### Live Plan Preview — 3개 이상 경쟁사 동시 채택 [^12]

2026년 2월 18-20일에 3개 이상 경쟁사가 동시에 "실행 전/중 계획 편집 + 실시간 프리뷰" 패턴을 채택했다:

- **Claude Code 2.1.47**: VS Code에서 plan preview가 에이전트 반복 수정 시 자동 업데이트. 준비 완료 시에만 코멘트 활성화. `Ctrl+G`로 plan 파일 직접 편집, `Shift+Tab`으로 plan 모드 토글.
- **ChatGPT Deep Research (GPT-5.2)**: 리서치 계획을 사전 편집 가능 + 실행 중 실시간 진행 추적 + 중간 방향 전환(mid-run pivot)으로 재시작 없이 초점 변경.
- **Cursor CLI Plan Mode**: `/plan` 명령으로 결정 메뉴 생성 + 화살표 키 탐색 + Enter 실행. 클라우드/로컬 빌드 선택.

공통 구조 요소: (1) Plan-as-artifact — 계획이 채팅 메시지가 아닌 편집 가능한 문서, (2) Phased gating — 생성 → 편집 → 승인 → 실행(또는 루프백), (3) Live preview — AI 반복 시 실시간 렌더링, (4) Mid-execution intervention — 실행 중 일시정지/방향전환, (5) Keyboard-driven decision UI — 승인/거절 키보드 단축키.

**왜 이 방식인가**: 이진 approve/reject 게이트는 사용자를 의사결정자로만 취급한다. Live Plan Preview는 사용자를 공동 저자로 격상시켜, "AI가 제안, 인간이 yes/no"에서 "AI가 초안, 인간이 편집, AI가 반영, 양쪽이 모니터링"으로 전환한다.

*참고 URL*: [Claude Code Releases](https://releasebot.io/updates/anthropic/claude-code), [ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), [Cursor Releases](https://releasebot.io/updates/cursor)

---

## 패턴 분류 및 트레이드오프

### 패턴 1: Permission Tier System

사용자가 승인 범위를 선택(한 번 / 세션 / 영구)하여 반복 승인을 줄이는 모델.

- **대표**: Claude Code, Claude Cowork
- **장점**: Approval fatigue 최소화, 사용자 의도 명시적 기록, 구현 비용 낮음
- **단점**: Plan visibility 부재, 복잡한 multi-step 작업에 부적합
- **적합한 상황**: 반복적인 도구 호출 (파일 읽기, API 호출 등)

### 패턴 2: Plan-Review-Execute (Live Plan Preview 포함)

다단계 계획을 문서로 시각화하고, 각 단계에서 사용자가 편집/승인한 뒤 실행하는 모델. 2026년 2월 Live Plan Preview로 진화하여 실시간 프리뷰 + 실행 중 개입이 추가됨.

- **대표**: GitHub Copilot Workspace, Claude Code Plan Mode, ChatGPT Deep Research, Cursor CLI
- **장점**: 높은 visibility, 사용자가 공동 저자로 참여, early-stage 정정이 downstream 자동 반영
- **단점**: 구현 비용 높음 (plan 렌더링 + 실시간 동기화), 모바일 부적합
- **적합한 상황**: 복잡한 multi-step 작업 (PPT 시나리오, 데이터 분석 파이프라인)

### 패턴 3: Confidence-Based Escalation

AI의 신뢰도 점수에 따라 승인 UI를 동적으로 조절하는 모델.

- **대표**: Salesforce Agentforce, Claude Code Security (confidence rating)
- **장점**: Approval fatigue와 safety의 자동 최적화, high-confidence는 fast-path
- **단점**: Confidence scoring 인프라 필요, 사용자에게 "왜 이 점수인지" 설명 필요
- **적합한 상황**: 다양한 risk profile의 action이 혼재된 워크플로우

### 패턴 4: Protocol-Level Elicitation (신규)

프레임워크/프로토콜 레벨에서 HITL 일시정지와 구조화 입력을 표준화하는 모델. 2026년 2월 MCP Elicitation으로 본격화.

- **대표**: MCP SDK (Elicitation), CrewAI (Provider Pattern), LangGraph (interrupt), Vercel AI SDK (Callbacks)
- **장점**: 프로토콜 표준으로 상호 운용성 보장, 커스텀 구현 불필요, 스키마 기반 자동 폼 생성
- **단점**: 아직 draft 스펙(MCP), 복잡한 UI에는 스키마 한계(flat object만)
- **적합한 상황**: MCP 서버 기반 도구 실행, 다중 프레임워크 통합

### 트레이드오프 요약

| | Approval Fatigue | User Autonomy | Impl. Cost | Visibility | Async 지원 | 표준화 수준 |
|---|---|---|---|---|---|---|
| **Permission Tier** | 낮음 (허용 저장) | 높음 (once/session) | 낮음 | 낮음 (implicit) | ✗ | 제품별 |
| **Plan-Review (Live)** | 중간 (multi-stage) | 매우 높음 (편집 가능) | 높음 (실시간 동기화) | 매우 높음 (문서) | △ (mid-run pivot) | 제품별 |
| **Confidence-Based** | 낮음 (filtering) | 중간 (auto vs ask) | 높음 (scoring) | 중간 (score 의존) | ✅ | 제품별 |
| **Protocol Elicitation** | 중간 (매번 폼) | 중간 (스키마 제한) | 낮음 (표준 활용) | 높음 (구조화 폼) | ✅ (streaming) | **프로토콜 표준** |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 현재 상태 | 활용 가능성 |
|----------|---------|-----------|
| `useSlideOutlineHITL.ts` | PPT-specific approval hooks (approve/reject/modify) | 범용 ApprovalGate의 참조 구현으로 활용 |
| `usePPTScenario.ts` | `resumeWithHitlSelection()` + `isHitl` step type | Orchestration 레벨 HITL 인프라의 기반 |
| `useScenarioOrchestration.ts` | `ActiveHitl`, `RunStatus`, `InterruptPayload` 타입 | LangGraph interrupt 모델과 이미 정렬됨 |
| `HITLFloatingPanel.tsx` | 채팅 입력 위 floating panel UI | ApprovalGate의 inline 모드 UI 기반 |
| `dialog.tsx` (Radix) | Radix UI Dialog base component | high-risk modal 모드에 직접 활용 |
| `#FF3C42` brand color | 프로젝트 accent color | high-risk 시각적 경고에 사용 |

### 권장 접근: Hybrid Orchestration + Protocol-Ready ApprovalGate

기존 Orchestration 프레임워크를 확장하면서 MCP Elicitation 호환 스키마와 async 상태 지속을 설계에 반영하는 하이브리드 접근.

**Phase 1 (MVP): Generic ApprovalGate Component**

범용 ApprovalGate를 다음 props로 설계:
- `actionType`: 'create' | 'modify' | 'delete' | 'execute' | 'custom'
- `riskLevel`: 'low' | 'medium' | 'high'
- `title`, `description`: 사용자에게 표시할 작업 정보
- `onApprove`, `onReject`, `onModify`: handlers
- `schema?`: MCP Elicitation 호환 JSON Schema (선택적 구조화 입력 폼)
- `items?`: 다중 항목 승인 시 ApprovalItem[] (예: 슬라이드 목록)

렌더링 로직:
- `riskLevel === 'low'`: Toast notification (자동 승인 예정, "취소" 버튼만)
- `riskLevel === 'medium'`: Inline card (approve/reject/modify 버튼, border-left: #FF3C42)
- `riskLevel === 'high'`: Modal dialog (full focus, #FF3C42 accent)
- `schema` 제공 시: JSON Schema → 자동 폼 렌더링 (MCP Elicitation form mode 호환)

Orchestration 통합:
- `ScenarioStep`에 `approvalGate?: ApprovalGateConfig` 필드 추가
- `ToolType`에 `'approval_gate'` 추가
- `resumeWithHitlSelection()`에서 ApprovalGate 응답 처리

**Phase 2 (확장): Async HITL + Session Permissions**

- `ApprovalGateProvider` Context 생성 — 승인 상태를 컴포넌트 트리 전체에서 접근 가능
- CrewAI 패턴 참조: async pause/resume — 시나리오가 승인 대기 중 상태를 직렬화하고, 사용자가 나중에 돌아와 승인 가능
- Session Permission Storage: `sessionPermissions: Map<actionTypeKey, PermissionTier>` — "Allow for Session" 선택 시 동일 actionType은 자동 승인
- Vercel AI SDK 패턴 참조: `onToolCallStart` hook에서 risk 기반 게이팅 판단

**Phase 3 (고급): Live Plan Preview + Confidence Scoring**

- PPT 시나리오 아웃라인 HITL을 Live Plan Preview 패턴으로 강화 — 실시간 프리뷰 + 인라인 코멘트
- Action Risk Classification Engine — actionType × resourceType → riskScore 자동 계산
- AdminView에서 조직 전체 승인 규칙 관리 (Salesforce Supervisor 패턴 참조)
- Audit trail: 모든 approval decision을 로그

### 이 접근을 권장하는 이유

1. **기존 자산 최대 활용**: Orchestration의 `ActiveHitl` + `InterruptPayload`가 이미 LangGraph interrupt 모델과 정렬되어 있어 확장 비용이 낮음
2. **프로토콜 표준 선제 대응**: MCP Elicitation JSON Schema 호환으로 향후 MCP 서버 통합 시 ApprovalGate가 elicitation 클라이언트 역할을 바로 수행 가능
3. **점진적 복잡도 관리**: Phase 1은 기존 HITLFloatingPanel의 확장 수준으로 시작, Phase 2-3에서 async/live preview 점진 추가
4. **경쟁사 3+의 동시 채택 트렌드 반영**: Live Plan Preview가 산업 표준으로 자리잡는 추세에 Phase 3에서 대응

### Acceptance Criteria

- [ ] **AC1**: Generic ApprovalGate component가 actionType, riskLevel, handlers를 수용하고 PPT-specific 로직은 호출자에게 위임
- [ ] **AC2**: riskLevel에 따라 3가지 UI 변형(toast / inline card / modal) 렌더링, #FF3C42 accent
- [ ] **AC3**: `schema` prop 제공 시 JSON Schema → 자동 폼 렌더링 (MCP Elicitation form mode 호환)
- [ ] **AC4**: `items` prop 제공 시 다중 항목 개별 승인/거부 가능 (현재 슬라이드 아웃라인 HITL 대체)
- [ ] **AC5**: Orchestration의 `ScenarioStep.approvalGate`로 시나리오 내 HITL 활성화 가능
- [ ] **AC6**: Session Permission: "Allow for Session" 선택 시 동일 actionType 자동 승인, 세션 종료 시 clear
- [ ] **AC7**: 접근성: Modal은 `role="alertdialog"` + focus trap, Inline은 `role="alert"` + aria-live
- [ ] **AC8**: 키보드: Enter=approve, Escape=reject (modal), Tab=항목 간 이동

---

## Key Considerations

### Approval Fatigue vs Safety

모든 action을 ask하면 사용자가 "approve all" 버튼을 찾게 된다. Risk classification + Permission Tier + Action Granularity를 조합하여 truly risky action만 slow-path로 라우팅하는 것이 essential. Claude Code Security의 self-adversarial 패턴(AI가 자체 발견을 반증 시도)은 인간에게 도달하는 항목의 품질을 높이는 보완 전략이다.

### Protocol-Level HITL 표준화 대응

MCP Elicitation이 draft 스펙이므로 API가 변경될 수 있다. JSON Schema 기반 폼 생성을 ApprovalGate의 선택적 기능으로 설계하되, core approval flow는 MCP에 의존하지 않도록 분리한다. CrewAI의 provider 패턴처럼 승인 메커니즘 자체를 플러그 가능하게 설계하면 향후 프로토콜 변경에 대응 가능하다.

### Async HITL 상태 관리

비동기 승인에서 핵심 과제는 상태 직렬화와 복원이다. CrewAI는 webhook + resume 엔드포인트 패턴을, LangGraph는 checkpoint 기반 interrupt/resume 패턴을 사용한다. KonaI-Agent에서는 React Context의 상태를 localStorage 또는 서버에 직렬화하고, 사용자가 재방문 시 pending approval 목록을 보여주는 방식이 적합하다.

### Sequential Interrupt 정확성

LangGraph v1.0.9 버그가 보여주듯, 다단계 승인에서 각 interrupt가 정확히 자신의 입력만 수집하는 것이 critical하다. KonaI-Agent의 `usePPTScenario`에서 `completedStepIds: Set<string>`으로 완료된 단계를 추적하는 기존 패턴이 이 문제를 회피하지만, 향후 functional API 스타일 시나리오 정의 시 scratchpad 패턴을 주의해야 한다.

### Modify Option과 Revision Loop

"Modify" 버튼을 제공할 때, 수정 후 재검토 로직이 명확해야 한다. ChatGPT Deep Research의 mid-run pivot 패턴(재시작 없이 방향 변경)이 가장 이상적이지만 구현 비용이 높다. Phase 1에서는 modify → 시나리오 특정 단계로 리와인드하는 단순한 모델로 시작하고, Phase 3의 Live Plan Preview에서 인라인 편집으로 전환한다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다. 수동 편집 금지. -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Claude Code docs | Permission Tiers 3단계 모델 분석, GitHub Copilot Plan Review, Salesforce escalation | approval, permission |
| 2026-02-21 | MCP SDK v1.27.0 | Elicitation 프로토콜 추가 — 도구 실행 중 JSON Schema 기반 구조화 입력 요청 가능 | elicitation, mcp, protocol |
| 2026-02-21 | CrewAI v1.10.0a1 | Async HITL + provider 패턴 리팩토링 — 비동기 pause/resume, 플러그 가능 provider | async, hitl, crewai |
| 2026-02-21 | LangGraph v1.0.9 | Sequential interrupt 버그 수정 — 함수형 API 다중 순차 interrupt 정상 작동 | interrupt, langgraph, bugfix |
| 2026-02-21 | Claude Code Security | 다단계 self-adversarial 검증 + 인간 게이팅 — "developers always make the call" | security, verification, gating |
| 2026-02-21 | Vercel AI SDK v6.0.97 | ToolLoopAgent 6개 lifecycle callbacks — agent 루프 내 HITL 삽입 hook point | callbacks, vercel, agent |
| 2026-02-21 | Claude Code/ChatGPT/Cursor | Live Plan Preview 3사 동시 채택 — 실시간 계획 편집 + 실행 중 개입 | plan-preview, collaboration |

---

## References

### Vault

- [[Insights/agent-ui/hitl-approval-patterns|HITL 승인 패턴 (Broad)]] — 5가지 HITL 패턴 분류 및 cross-product 분석
- [[Insights/agent-ui/patterns/risk-based-rendering|위험도 기반 동적 UI 렌더링]] — Risk-based rendering 상세 분석

### External

[^1]: [Configure permissions - Claude Code Docs](https://code.claude.com/docs/en/permissions) — Permission Tiers (Allow Once/Session/Always) 구현 상세
[^2]: [GitHub Copilot Workspace Guide](https://createaiagent.net/tools/github-copilot-workspace/) — Spec → Plan → Diff 3단계 검토 구조
[^3]: [Atlas Reasoning Engine - Salesforce](https://www.salesforce.com/agentforce/what-is-a-reasoning-engine/atlas/) — Confidence-based escalation 메커니즘
[^4]: [Cursor Changelog](https://releasebot.io/updates/cursor) — Per-hunk acceptance, CLI plan mode
[^5]: [Claude Code Internals Part 8: Permission System](https://kotrotsos.medium.com/claude-code-internals-part-8-the-permission-system-624bd7bb66b7) — Permission 내부 구현 분석
[^6]: [Inside Agentforce: Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/) — Confidence scoring 엔지니어링 상세
[^7]: [Claude Code Security Preview](https://www.anthropic.com/news/claude-code-security) (2026-02-20) — 다단계 self-adversarial 검증 + 인간 게이팅
[^8]: [MCP Elicitation Specification](https://modelcontextprotocol.io/specification/draft/client/elicitation) + [SDK v1.27.0](https://github.com/modelcontextprotocol/typescript-sdk/releases) (2026-02-16) — 프로토콜 레벨 HITL 표준화
[^9]: [CrewAI v1.10.0a1](https://github.com/crewAIInc/crewAI/releases/tag/1.10.0a1) (2026-02-19) — Async HITL + provider 패턴 리팩토링
[^10]: [LangGraph v1.0.9 PR #6863](https://github.com/langchain-ai/langgraph/pull/6863) (2026-02-19) — Sequential interrupt 버그 수정
[^11]: [Vercel AI SDK v6.0.97](https://github.com/vercel/ai/releases/tag/ai%406.0.97) (2026-02-20) — ToolLoopAgent lifecycle callbacks
[^12]: Claude Code 2.1.47 / ChatGPT Deep Research / Cursor CLI (2026-02-18~20) — Live Plan Preview 3사 동시 채택

---

*Last synthesized: 2026-02-21 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
