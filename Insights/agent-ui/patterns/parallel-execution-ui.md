---
type: insight-synthesis
topic_id: parallel-execution-ui
topic_name: 병렬 실행 UI 패턴
category: agent-ui
document_level: specific
parent_broad:
  - agent-reasoning-visualization
  - dashboard-composition
catalog_components:
  - parallel_execution_view
tags:
  - insight
  - agent-ui
  - pattern
  - parallel-execution
  - multi-agent
  - task-management
status: draft
confidence: high
last_updated: '2026-02-15'
source_products:
  - cursor
  - windsurf
  - claude-code
  - openai-codex
  - devin
  - github-copilot-workspace
  - manus-ai
source_files:
  - '[[cursor]]'
  - '[[manus-ai]]'
  - '[[엔터프라이즈 AI 서비스 비교 분석]]'
  - '[[Manus AI UX 분석]]'
auto_update:
  enabled: true
  keywords:
    - parallel execution
    - multi-agent
    - concurrent tasks
    - background agents
    - task queue
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 병렬 실행 UI 패턴

## TL;DR

- 병렬 실행 UI는 크게 **3가지 레이아웃 패턴**으로 분류된다: Sidebar Task List(Cursor, Devin), Multi-Pane Dashboard(Windsurf), Sequential Queue(GitHub Copilot Workspace). 제품마다 선택한 패턴은 "사용자가 병렬 작업에 얼마나 깊이 개입하느냐"에 따라 결정된다. [^1][^2]
- **작업 격리(Isolation) 방식**이 UI 설계를 근본적으로 결정한다. Git Worktree 기반(Cursor, Windsurf, Claude Code)은 로컬 멀티패인 UI를, Cloud Sandbox 기반(Codex, Devin)은 비동기 대시보드 UI를 자연스럽게 유도한다. [^3]
- **결과 통합(Aggregation) 패턴**이 병렬 실행 UI의 핵심 차별화 포인트이다. Cursor의 Unified Diff View(모든 파일 변경을 하나의 뷰로 통합), Devin의 Multi-Panel 비교, GitHub Copilot Workspace의 File-by-File Diff가 각각 다른 사용자 경험을 제공한다. [^1][^4]
- 현재 KonaI-Agent 프로젝트는 단일 시나리오 순차 실행(`useScenarioOrchestration`) 패턴만 보유하고 있으며, 병렬 실행 UI의 기반이 될 수 있는 **react-grid-layout**(위젯 그리드)과 **ReactFlow**(DAG 시각화) 인프라는 이미 갖추고 있다. [^5]

---

## Overview

AI 에이전트가 단일 작업 수행에서 복수 작업 동시 처리로 진화하면서, "여러 에이전트/태스크가 동시에 실행되는 상태를 사용자에게 어떻게 보여줄 것인가"는 2025~2026년 에이전트 UI의 핵심 설계 과제로 부상하고 있다. Cursor 2.0이 최대 8개 에이전트 병렬 실행을, Windsurf Wave 13이 Multi-Pane Cascade를, OpenAI Codex가 클라우드 기반 비동기 병렬 태스크를 도입하면서, 이 영역은 AI 코딩 도구뿐 아니라 범용 에이전트 서비스 전반으로 확산되고 있다.

KonaI-Agent 프로젝트에서 병렬 실행 UI는 두 가지 시나리오에서 필요하다: (1) 에이전트가 여러 데이터 소스를 동시에 조회·분석하는 과정을 보여주는 경우, (2) 복수의 에이전트/시나리오가 병렬로 작업하는 상태를 모니터링하는 경우. 특히 데모 목적에서 "AI가 여러 일을 동시에 처리하고 있다"는 것을 시각적으로 보여주는 것이 핵심이다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| Product | 레이아웃 패턴 | 최대 동시 실행 | 격리 방식 | 태스크 상태 표시 | 결과 통합 방식 | 사용자 개입 수준 |
|---------|-------------|-------------|----------|---------------|-------------|--------------|
| **Cursor 2.0** | 우측 Sidebar Task List | 8 에이전트 | Git Worktree | Sidebar 아이템별 상태 아이콘 + Context Pills | Unified Diff View (전체 변경 통합) | 낮음 (자동 실행) |
| **Windsurf Wave 13** | Multi-Pane Dashboard | 제한 없음 (수동 생성) | Git Worktree | 패인별 독립 상태 | Side-by-Side 비교 | 중간 (수동 패인 관리) |
| **Claude Code** | Terminal Subagent Output | 제한 없음 (서브에이전트) | Git Worktree | `Task(...)` 출력 로그 | Lead Agent 종합 | 낮음 (자동 위임) |
| **OpenAI Codex** | Cloud Task Dashboard | 제한 없음 | Cloud Sandbox (각 태스크별) | 프로젝트별 스레드 상태 | Traces 대시보드 (타임라인) | 낮음 (비동기) |
| **Devin 2.0** | Multi-Session Panel | 제한 없음 | Cloud IDE (각 세션별) | 좌측 세션 목록 + 우측 IDE 탭 | Multi-Panel 비교 | 중간 (세션 전환) |
| **GitHub Copilot Workspace** | Sequential File Queue | 1 (순차) | 단일 워크스페이스 | 파일별 Pending→In Progress→Done | File-by-File Diff | 높음 (파일별 검토) |
| **Manus AI** | Execution Tree | 1 (순차 반복) | 단일 에이전트 | 실행 트리 + 단계별 상태 아이콘 | 실시간 브라우저 미러링 | 관찰 위주 |

### 경쟁사별 상세 분석

#### Cursor 2.0 — Sidebar Agent List + Unified Diff

Cursor 2.0은 Agent 모드에서 기존 파일 트리를 대체하여 **에이전트/플랜/실행을 1급 객체**로 취급하는 우측 사이드바를 도입했다. 각 에이전트는 독립 항목으로 표시되며, 실행 중인 작업("searching codebase", "editing files")이 실시간으로 업데이트된다. 파일은 더 이상 트리 구조가 아니라 대화 내 **Context Pills**로 인라인 참조된다.

핵심 설계 결정은 **Unified Diff View**이다. 8개 에이전트가 병렬로 수정한 모든 파일의 변경사항을 하나의 통합 diff 화면에서 검토할 수 있다. 이는 "파일별로 뛰어다니며 변경 확인"하는 대신 "전체 변경의 흐름을 한눈에 파악"하게 한다.

**왜 이 방식인가**: 코딩 도구에서 최종 산출물은 코드 변경이므로, 실행 과정보다 결과 통합이 중요하다. Sidebar는 실행 상태의 빠른 스캔을, Unified Diff는 결과 검토의 효율을 각각 최적화한다.

*참고 URL*: https://www.cursor.com/blog/cursor-2 — Cursor 2.0 런칭 블로그, Background Agents + Sidebar 리디자인

#### Windsurf Wave 13 — Multi-Pane Cascade Dashboard

Windsurf는 여러 Cascade(에이전트 대화) 세션을 **별도의 패인/탭**으로 열어 Side-by-Side로 비교하는 방식을 채택했다. 각 Cascade는 독립 Git Worktree로 격리되어 동일 리포지토리에서 충돌 없이 병렬 작업이 가능하다.

**왜 이 방식인가**: 개발자가 직접 비교하며 판단하는 것을 중시한다. 자동 통합보다는 "사용자가 양쪽을 보고 어떤 접근이 나은지 결정"하는 워크플로우를 지원한다. 전체 화면을 "대형 Cascade 대시보드"로 전환할 수 있어, 대시보드 중심의 모니터링에 적합하다.

*참고 URL*: https://docs.windsurf.com/windsurf/cascade/worktrees — Worktrees 공식 문서

#### Devin 2.0 — Multi-Session IDE Panel

Devin은 각 인스턴스가 독립 **Cloud IDE**를 갖는 방식으로, 좌측 패널에 활성 세션 목록, 우측에 선택된 세션의 IDE(Shell, Browser, Editor, Progress 탭)를 표시한다. 세션별 Fork/Rollback이 가능하며, 비동기 핸드오프(작업 시작 후 오프라인, 복귀 후 결과 검토)를 지원한다.

**왜 이 방식인가**: 엔지니어가 동시에 여러 기능 개발을 위임하고, 각 세션을 독립적으로 관리할 수 있어야 한다. Cloud IDE 격리로 완전한 환경 분리를 보장하면서, 세션 전환으로 빠른 컨텍스트 스위칭을 지원한다.

*참고 URL*: https://cognition.ai/blog/devin-2 — Devin 2.0 제품 소개

#### OpenAI Codex — Cloud Background Tasks + Traces

Codex는 각 태스크를 **독립 클라우드 샌드박스**에서 실행하는 완전 비동기 모델이다. 프로젝트별 스레드로 조직되며, 완료 후 Review Queue에 결과가 도착한다. **Traces 대시보드**에서 실행 타임라인(프롬프트, 도구 호출, 에이전트 간 핸드오프)을 사후 검사할 수 있다.

**왜 이 방식인가**: "태스크를 던져놓고 다른 일을 하다가 결과를 확인"하는 비동기 워크플로우를 최적화한다. 로컬 리소스 제약 없이 병렬 확장이 가능하고, 스케줄링(Automations)으로 반복 작업을 자동화할 수 있다.

*참고 URL*: https://openai.com/index/introducing-codex/ — Codex 소개 페이지

#### GitHub Copilot Workspace — Sequential File Queue

병렬이 아닌 **순차 파일 큐** 방식이지만, 멀티스텝 계획 실행의 시각화로서 의미 있는 레퍼런스다. 우측 패널에 파일별 업데이트 큐가 표시되고, 각 파일이 Pending → In Progress → Done으로 진행되며 완료 시 자동으로 Diff가 렌더링된다.

**왜 이 방식인가**: 코드 변경의 신뢰성을 중시하여, 사용자가 매 파일마다 검토할 수 있는 granular control을 제공한다. "전체를 한번에 실행"보다 "하나씩 확인하며 진행"이 실수를 줄인다는 철학이다.

*참고 URL*: https://githubnext.com/projects/copilot-workspace — Copilot Workspace 프로젝트 페이지

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Sidebar Task List (태스크 목록 사이드바)

사이드바에 실행 중인 태스크/에이전트를 리스트로 나열하고, 메인 영역에서 선택한 태스크의 상세를 표시하는 패턴.

- **대표**: Cursor 2.0 (우측 사이드바), Devin 2.0 (좌측 세션 목록)
- **장점**: 화면 공간 효율적, 태스크 수가 많아도 스크롤로 관리 가능, 빠른 상태 스캔
- **단점**: 동시에 2개 이상 태스크의 실시간 진행을 비교하기 어려움
- **적합한 상황**: 에이전트/태스크 수가 3개 이상이고, 사용자가 전체 목록을 오버뷰하면서 필요 시 개별 태스크로 진입하는 워크플로우

### 패턴 B: Multi-Pane Dashboard (멀티패인 대시보드)

화면을 여러 패인으로 분할하여 각 태스크의 실시간 상태를 동시에 보여주는 패턴.

- **대표**: Windsurf Wave 13 (Side-by-Side Cascade), Salesforce Command Center (KPI 위젯 그리드)
- **장점**: 병렬 진행 상태의 실시간 비교, 시각적 임팩트가 강함 (데모에 효과적)
- **단점**: 패인 수가 늘어나면 각 패인의 공간이 좁아짐, 4개 이상에서는 가독성 하락
- **적합한 상황**: 태스크 수가 2~4개이고, 사용자가 모든 태스크의 진행을 동시에 모니터링해야 하는 워크플로우

### 패턴 C: Sequential Queue (순차 큐)

태스크가 큐에 나열되고 하나씩 처리되며, 완료된 항목에 결과(diff, 시각화 등)가 표시되는 패턴.

- **대표**: GitHub Copilot Workspace (파일별 큐), Manus AI (실행 트리)
- **장점**: 사용자 제어감 극대화, 각 단계에서 검증 가능, 예측 가능한 진행
- **단점**: 병렬 실행의 속도 이점을 살리지 못함, "동시에 일어나는 느낌"이 부족
- **적합한 상황**: 정확성이 속도보다 중요하고, 사용자가 각 단계를 승인해야 하는 워크플로우

### 패턴 D: Background + Review Queue (비동기 백그라운드)

태스크를 백그라운드로 보내고, 완료 시 Review Queue에 결과가 도착하는 패턴.

- **대표**: OpenAI Codex (Cloud Sandbox + Review Queue), Cursor Background Agents
- **장점**: 사용자가 대기하지 않음, 비동기로 다른 작업 가능, 서버 확장 용이
- **단점**: 실시간 진행 관찰 불가, 실패 시 피드백 지연, "에이전트가 일하고 있다"는 느낌 부족
- **적합한 상황**: 장시간 실행되는 태스크, 사용자가 결과만 확인하면 되는 워크플로우

### 트레이드오프 요약

| | 실시간 가시성 | 화면 효율 | 데모 임팩트 | 구현 복잡도 | 태스크 확장성 |
|---|---|---|---|---|---|
| **Sidebar Task List** | 중간 | 높음 | 중간 | 낮음 | 높음 |
| **Multi-Pane Dashboard** | 높음 | 낮음 | **높음** | 중간 | 낮음 |
| **Sequential Queue** | 낮음 | 높음 | 낮음 | 낮음 | 높음 |
| **Background + Review** | 낮음 | 높음 | 낮음 | 높음 | 높음 |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 |
|----------|-----------|
| `useScenarioOrchestration.ts` — 멀티스텝 시나리오 순차 실행 | 단일 시나리오 상태 머신의 기반을 복수 태스크 트래킹으로 확장 가능 |
| `usePPTScenario.ts` — PPT 생성 시나리오 오케스트레이션 | 단계별 상태 추적 패턴을 병렬 태스크별 상태 추적으로 일반화 가능 |
| `react-grid-layout` (LiveboardView) — 드래그/리사이즈 위젯 그리드 | Multi-Pane 패턴의 기반으로 직접 활용 가능. 각 그리드 셀이 하나의 태스크 패널 역할 |
| `ReactFlow` (DataManagementView) — 노드 기반 그래프 에디터 | 태스크 간 의존성 시각화(DAG)에 활용 가능 |
| `NotificationContext` — 글로벌 알림 시스템 | 태스크 완료/실패 알림의 기반 |
| 3-panel layout (GeneralChatView) — 좌측 사이드바 + 중앙 채팅 + 우측 사이드바 | Sidebar Task List 패턴과 자연스럽게 결합 가능 |

### 권장 접근: Sidebar + Grid 하이브리드

KonaI-Agent는 데모 프로젝트이므로 **시각적 임팩트**가 중요하다. 동시에 기존 3-panel 레이아웃과의 일관성도 유지해야 한다. 따라서:

**기본 모드**: GeneralChatView의 우측 사이드바 영역에 **Task List Sidebar** 배치 (Cursor 패턴 참고). 채팅에서 에이전트에게 복수 작업을 요청하면, 우측에 태스크별 카드가 쌓이며 각 카드에 상태(Pending/Running/Completed/Failed), 현재 작업 설명, 진행률이 실시간으로 업데이트.

**확장 모드**: 태스크 카드를 클릭하면 전체 화면이 `react-grid-layout` 기반 **Multi-Pane Dashboard**로 전환 (Windsurf 패턴 참고). 각 패인에 해당 태스크의 실시간 로그/결과가 표시되며, 패인 리사이즈/드래그로 자유 배치 가능.

**결과 통합 뷰**: 모든 태스크 완료 후, 각 태스크의 산출물을 하나의 통합 아티팩트 패널에 탭으로 정리 (Cursor Unified Diff View의 변형).

### 이 접근을 권장하는 이유

1. **기존 3-panel 레이아웃 활용**: 새로운 레이아웃 패러다임을 도입하지 않고 우측 패널을 확장하여 일관성 유지
2. **react-grid-layout 재사용**: LiveboardView에서 이미 검증된 위젯 그리드를 그대로 활용하므로 구현 비용 절감
3. **데모 임팩트**: Multi-Pane 모드에서 여러 태스크가 동시에 진행되는 화면은 시각적으로 강력함
4. **점진적 복잡도**: 기본 모드(Sidebar)로 시작하고, 확장 모드(Dashboard)로 발전하는 2단계 구현이 가능

### Acceptance Criteria

- [ ] 2개 이상의 에이전트 태스크가 동시에 실행되는 상태를 시각적으로 구분하여 표시
- [ ] 각 태스크별 상태(Pending → Running → Completed/Failed) 실시간 전환
- [ ] 각 태스크별 현재 수행 중인 작업 설명 (예: "데이터 조회 중", "차트 생성 중") 실시간 업데이트
- [ ] 진행률 표시 (전체 단계 수 대비 현재 단계, 또는 퍼센트)
- [ ] 태스크 간 전환 (사이드바에서 클릭 시 상세 보기)
- [ ] 전체 태스크 완료 후 결과 요약 표시
- [ ] 실패한 태스크의 에러 표시 및 재시도 액션
- [ ] Multi-Pane 모드로 전환하여 여러 태스크 동시 모니터링 (선택 기능)

---

## Key Considerations

### 데모 vs. 프로덕션

KonaI-Agent는 데모 프로젝트이므로, 실제 병렬 백엔드 처리가 아닌 **시뮬레이션된 병렬 실행**을 시각적으로 보여주는 것이 핵심이다. 기존 `usePPTScenario`의 시뮬레이션 패턴(setTimeout 기반 단계 진행)을 복수 태스크에 적용하되, 각 태스크의 진행 속도를 다르게 설정하면 병렬 실행의 느낌을 자연스럽게 연출할 수 있다.

### 태스크 상태 표현

경쟁사들의 공통 패턴은 최소 4가지 상태를 시각적으로 구분하는 것이다: Pending(회색), Running(파란 스피너), Completed(녹색 체크), Failed(빨간 X). KonaI-Agent의 브랜드 컬러(#FF3C42)를 Running 상태의 액센트로 활용하면 차별화된 시각적 아이덴티티를 줄 수 있다.

### 태스크 의존성 시각화

Cursor, Codex 등은 독립 태스크의 병렬 실행에 초점을 맞추지만, 에이전트 시나리오에서는 태스크 간 의존성이 있는 경우가 많다 (예: "데이터 수집" 완료 후 "분석" 시작). 현재 DataManagementView에서 사용 중인 ReactFlow로 태스크 DAG를 시각화하면, 의존성이 있는 병렬 실행을 직관적으로 보여줄 수 있다. 이는 경쟁사 대비 차별화 포인트가 될 수 있다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Web Research | Cursor 2.0 Background Agents: 최대 8개 병렬, Sidebar Task List + Unified Diff View. Git Worktree 기반 격리. | parallel, cursor |
| 2026-02-15 | Web Research | Windsurf Wave 13: Multi-Pane Cascade, Git Worktree, Side-by-Side 비교 | parallel, windsurf |
| 2026-02-15 | Web Research | Devin 2.0: Multi-Session Cloud IDE, 좌측 세션 리스트 + 우측 IDE 탭, Fork/Rollback 지원 | parallel, devin |
| 2026-02-15 | Web Research | OpenAI Codex: Cloud Sandbox 기반 비동기 병렬, Traces 대시보드, Automations 스케줄링 | parallel, codex |

---

## References

### Vault
- [^1]: [[cursor]] — Cursor 2.0 Background Agents, Sidebar 리디자인, Unified Diff View
- [^2]: [[Manus AI UX 분석]] — 실행 트리 시각화, 순차 반복 실행 모델
- [^5]: KonaI-Agent 코드베이스 — `useScenarioOrchestration.ts`, `react-grid-layout`, `ReactFlow`

### External
- [^3]: [Cursor 2.0 adds coding model, UI for parallel agents](https://www.infoworld.com/article/4081431/cursor-2-0-adds-coding-model-ui-for-parallel-agents.html) (2026) — Cursor 2.0의 병렬 에이전트 아키텍처 상세
- [^4]: [Cognition: Devin 2.0](https://cognition.ai/blog/devin-2) (2025) — Devin 2.0 Multi-Session IDE, Fork/Rollback
- [^6]: [Windsurf Worktrees Docs](https://docs.windsurf.com/windsurf/cascade/worktrees) — Git Worktree 기반 병렬 격리 공식 문서
- [^7]: [Introducing Codex | OpenAI](https://openai.com/index/introducing-codex/) — Cloud Sandbox 병렬 실행, Traces 대시보드
- [^8]: [GitHub Next: Copilot Workspace](https://githubnext.com/projects/copilot-workspace) — Sequential File Queue 패턴

---

*Last synthesized: 2026-02-15 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
