---
type: insight-synthesis
topic_id: hitl-approval-patterns
topic_name: Human-in-the-Loop 승인 UI 패턴 비교
category: agent-ui
tags:
- insight
- agent-ui
- HITL
- approval-patterns
status: draft
confidence: high
last_updated: '2026-02-10'
source_products:
- salesforce-agentforce
- claude
- workday-assistant
- servicenow-now-assist
- sap-joule
- manus-ai
source_files:
- '[[엔터프라이즈 AI 서비스 비교 분  석]]'
- '[[salesforce-agentforce]]'
- '[[claude]]'
- '[[workday-assistant]]'
- '[[servicenow-now-assist]]'
- '[[sap-joule]]'
- '[[manus-ai]]'
- '[[Claude Cowork UI 분석]]'
- '[[Claude Cowork 플랜 아키텍처]]'
- '[[Claude Cowork 개요]]'
relevant_roles:
- frontend_agent
- planning_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - HITL
  - human-in-the-loop
  - approval workflow
  - intervention pattern
  - agent oversight
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# Human-in-the-Loop 승인 UI 패턴 비교

## TL;DR

- AI 에이전트의 HITL 승인 UI는 크게 **5가지 패턴**으로 분류된다: Plan-Review-Execute, Inline Contextual Approval, Supervisor Dashboard, Permission Tier System, Mid-Task Steering. 대부분의 제품은 2~3개 패턴을 조합하여 사용한다.
- **Risk-Based Rendering**(액션의 위험도에 따라 완전히 다른 UI를 렌더링하는 방식)이 차세대 HITL의 핵심 차별화 요소로 부상하고 있다. 단순한 "승인하시겠습니까?" 모달은 사용자 피로(Approval Fatigue)를 유발하므로, 액션의 성격에 따라 카드/프리뷰/경고 모달 등을 동적으로 전환해야 한다.
- 엔터프라이즈 제품(Salesforce, ServiceNow, Workday)은 **Supervisor Dashboard** 기반의 조직적 감독 패턴을, B2C 제품(Claude, Manus)은 **개인 사용자의 실시간 개입** 패턴을 우선하여 설계 방향이 명확히 분기된다.
- Claude Cowork의 **Steering Model**(Plan을 마크다운 파일로 영속화하여 사용자와 에이전트 모두 수정 가능)은 현재 시장에서 가장 진보된 Mid-Task Steering 구현이며, Reflect 단계를 포함하는 유일한 아키텍처이다.
- 엔터프라이즈 환경에서 HITL 승인 UI를 구축할 경우, **Permission Tier + Supervisor Dashboard + Risk-Based Rendering**의 3중 조합이 최적의 전략이다.

---

## Context

엔터프라이즈 AI 에이전트가 실질적인 비즈니스 프로세스(결재, 구매, 인사 변경 등)를 자율 수행하게 되면서, "언제, 어떻게, 어떤 형태로 사용자에게 승인을 요청할 것인가"가 제품 설계의 핵심 과제로 부상하고 있다. HITL 승인 UI는 단순히 안전장치가 아니라 사용자 신뢰(Trust), 작업 효율(Efficiency), 컴플라이언스(Compliance)의 교차점에 위치하는 UX 설계 문제이다.

엔터프라이즈 AI 에이전트 프로덕트가 ERP 데이터를 기반으로 재무, 인사, 운영 영역의 의사결정을 지원할 경우, 경쟁사들이 채택한 HITL 패턴을 체계적으로 분석하고 최적화된 승인 UI 전략을 수립할 필요가 있다. 특히 액션의 위험도(reversibility, financial impact, scope of change)에 따라 승인 UI의 강도와 형태를 동적으로 조절하는 Risk-Based Rendering 접근은, 사용자 피로를 최소화하면서도 고위험 작업에 대한 통제력을 유지하는 데 필수적이다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 주요 HITL 패턴 | 승인 UI 형태 | Risk-Based 분류 | Mid-Task 개입 | 감독자 뷰 | 비고 |
|---------|--------------|-------------|----------------|-------------|----------|------|
| **Salesforce Agentforce** | Supervisor Dashboard + Escalation | Omni Supervisor 실시간 모니터링, Listen-in | Atlas Engine이 불확실성 판단 시 자동 에스컬레이션 | 제한적 (에스컬레이션 후 인간이 인수) | Omni Supervisor + Command Center | 서비스 에이전트-인간 에이전트 핸드오프에 최적화 |
| **Claude (Code/Cowork/Chrome)** | Permission Tier + Mid-Task Steering | Allow/Deny/Ask 3단계, Pause & Ask, 인라인 선택지 | 파일 변경(diff), 위험 작업(승인 요청), 민감 작업(pause) | Steering Model - Plan 직접 수정 가능 | 없음 (개인 사용자 대상) | 유일하게 Reflect 단계 포함, Plan 영속화 |
| **Workday Assistant** | Inline Contextual Approval + Workflow Confirmation | AI 권장안 제시 -> 매니저 검토/조정 -> 확정 | 도메인별 정의 (보상 결정, 직무 구조 변경 등) | Task Workflow Confirmation | Agent Registry Dashboard | ASOR로 에이전트를 직원처럼 관리 |
| **ServiceNow Now Assist** | Handoff Summarization + Review-Approve | Chat Summarization 전환, Resolution Notes Review | 지식 문서(승인), 해결 노트(검토), 이상 징후(알림) | Proactive Triggers로 사전 알림 | AI Agent Orchestrator Dashboard | Skills -> Agents -> Orchestrator 3계층 |
| **SAP Joule** | Inline Contextual Approval + Process Confirmation | SuccessFactors 목표 승인, Ariba 검토, Natural Language Instruction | SAP Fiori UI 컨트롤로 응답 렌더링 | 제한적 (지시 -> 실행 -> 확인) | Joule Admin Center | 2,400+ 스킬 기반, Fiori 디자인 시스템 준수 |
| **Manus AI** | Watch & Intervene (Glass Box) | 실시간 브라우저 미러링, 실행 트리 노출 | 분류 없음 (모든 작업을 투명하게 노출) | 실시간 관찰 중 언제든 개입 가능 | 없음 (개인 사용자 대상) | Glass Box 투명성이 사실상 HITL을 대체 |

### 패턴 분류

#### 패턴 A: Plan-Review-Execute (계획 검토형)

에이전트가 실행 계획을 먼저 수립하여 사용자에게 제시하고, 사용자가 검토/승인한 후에 실행하는 패턴. 전체 작업의 로드맵을 사전에 확인할 수 있어 투명성이 높다.

- **대표 제품**: Claude Cowork (Plan을 마크다운 파일로 생성 -> 사용자 검토 -> 실행), Manus AI (Planner Agent가 서브태스크 분해 -> 실행)
- **장점**: 사용자가 전체 워크플로우를 사전에 파악, 잘못된 방향 조기 발견 가능
- **단점**: 계획 수립에 시간 소요, 단순 작업에서도 불필요한 오버헤드 발생 가능
- **적용**: 엔터프라이즈 환경에서 복수 시스템에 걸치는 복합 프로세스(결산, 예산 편성 등)에 적합

*Source*: [[Claude Cowork 플랜 아키텍처]], [[manus-ai]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 B: Inline Contextual Approval (맥락 내 인라인 승인)

대화 흐름 또는 업무 화면 내에서 직접 승인/거부를 수행하는 패턴. 별도의 승인 페이지나 모달로 이동하지 않고 현재 맥락을 유지한 채 결정을 내린다.

- **대표 제품**: SAP Joule (SuccessFactors 목표 승인, Ariba 세그멘테이션 검토), Workday Assistant (매니저 보너스 결정 지원 -> 인라인 조정), Microsoft Copilot (Email Drafts 편집 후 발송, Proposal Summary 검토/승인)
- **장점**: 맥락 전환(context switching) 최소화, 빠른 의사결정
- **단점**: 복잡한 승인 조건(다단계 승인, 조건부 승인)을 표현하기 어려움
- **적용**: 엔터프라이즈 ERP 환경의 트랜잭션 내 단일 승인(구매 주문 확인, 휴가 승인 등)에 최적

*Source*: [[sap-joule]], [[workday-assistant]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 C: Supervisor Dashboard (감독자 대시보드형)

관리자/감독자가 별도의 대시보드에서 다수의 에이전트 활동을 실시간으로 모니터링하고, 필요 시 개입/에스컬레이션하는 패턴. 1:N(한 명의 감독자가 다수의 에이전트를 관리) 구조에 최적화.

- **대표 제품**: Salesforce Agentforce (Omni Supervisor -- 인간 에이전트와 AI 에이전트를 동일 인터페이스에서 모니터링, Listen-in 기능으로 실시간 감청, Command Center에서 KPI 추적), ServiceNow Now Assist (AI Agent Orchestrator -- 멀티 에이전트 팀 협업 조율, 정책 대비 실시간 평가), Workday (Agent Registry Dashboard -- 에이전트를 직원처럼 리스트/필터/검색)
- **장점**: 조직 규모의 에이전트 운영에 필수, 컴플라이언스 감사 추적 용이
- **단점**: 개인 사용자 시나리오에서는 과도한 오버헤드, 구축 비용 높음
- **적용**: 엔터프라이즈 환경의 IT 관리자/운영팀에게 반드시 제공해야 하는 핵심 기능

*Source*: [[salesforce-agentforce]], [[servicenow-now-assist]], [[workday-assistant]]

#### 패턴 D: Permission Tier System (권한 계층형)

액션의 위험도를 사전에 분류하고, 각 등급에 맞는 승인 방식을 적용하는 패턴. 저위험 작업은 자동 실행, 중위험은 사후 알림, 고위험은 사전 승인 요청으로 차등 적용.

- **대표 제품**: Claude Code/Cowork (Allow/Deny/Ask 3단계 -- 파일 읽기는 Allow, 파일 수정은 Ask, 시스템 변경은 Deny), Claude in Chrome (민감 작업인 결제/로그인 시 Pause & Ask, 일반 탐색은 자동 진행), Snowflake Intelligence (RBAC 기반 세밀한 권한 + YAML 편집 후 즉시 테스트)
- **장점**: Approval Fatigue 최소화, 위험도에 비례하는 통제 수준 제공
- **단점**: 위험도 분류 기준 설정이 복잡, 잘못된 분류 시 보안 허점 발생 가능
- **적용**: 엔터프라이즈 ERP 환경에서 액션의 위험도 매트릭스(금액 임계값, 가역성, 영향 범위)를 정의하여 Permission Tier를 구현할 수 있음

*Source*: [[claude]], [[Claude Cowork 개요]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 E: Mid-Task Steering (작업 중 방향 수정형)

에이전트가 작업을 수행하는 도중에 사용자가 실시간으로 방향을 수정할 수 있는 패턴. 단순 승인/거부가 아니라, 에이전트의 실행 계획 자체를 수정하는 깊은 수준의 개입.

- **대표 제품**: Claude Cowork (Steering Model -- Plan을 마크다운 파일로 영속화하여 에이전트와 사용자 모두 수정 가능, Reflect 단계에서 전략 동적 조정), Manus AI (Watch & Intervene -- Glass Box에서 실시간 관찰 중 언제든 대화창으로 방향 수정), ThoughtSpot Spotter (Patent-pending feedback loop -- 단어/구문 단위 correction)
- **장점**: 사용자의 의도 변화에 유연하게 대응, 작업 재시작 불필요
- **단점**: 구현 복잡도 높음, 에이전트 상태 관리가 어려움
- **적용**: 엔터프라이즈 환경의 장기 실행 작업(결산 프로세스, 대량 데이터 분석)에서 중간 방향 수정이 필수

*Source*: [[Claude Cowork 플랜 아키텍처]], [[manus-ai]], [[엔터프라이즈 AI 서비스 비교 분석]]

---

## Key Findings

1. **Risk-Based Rendering이 차세대 HITL의 핵심 차별화 요소이다**: [[엔터프라이즈 AI 서비스 비교 분석]]에서 "승인이 필요한 작업의 성격에 따라 완전히 다른 UI 렌더링"이라는 관찰이 도출되었다. 예를 들어, 주식 구매는 금액/수량이 명확한 카드 UI, 이메일 발송은 전문(full text) 프리뷰, 파일 삭제는 경고 모달로 각각 다른 UI를 렌더링해야 한다. 단순 "승인하시겠습니까?" 텍스트 버튼은 사용자가 무엇을 승인하는지 충분히 이해하지 못한 채 습관적으로 승인하는 Approval Fatigue를 유발한다. — *Source*: [[엔터프라이즈 AI 서비스 비교 분석]]

2. **"왜 이 결정을 했는지" 시각화가 승인 UI의 신뢰도를 결정한다**: 단순히 "승인하시겠습니까?"가 아닌 "왜 이 결정을 했는지"를 시각화하는 것이 HITL UI의 신뢰도를 높이는 핵심이다. Salesforce의 Atlas Engine Step-by-Step Reasoning(Topic -> Action -> Record -> Grounding 단계 시각화), Claude의 Extended Thinking(접이식 추론 과정 요약), Manus의 Glass Box(실시간 브라우저 미러링)가 각각 다른 방식으로 이를 구현한다. — *Source*: [[salesforce-agentforce]], [[claude]], [[manus-ai]]

3. **Reflect 단계를 포함하는 에이전트 루프는 Claude Cowork이 유일하다**: [[Claude Cowork 플랜 아키텍처]]에서 분석된 바와 같이, Claude Cowork만이 Observe-Plan-Act-**Reflect**의 4단계 루프를 구현한다. ChatGPT Agent(Confirmation Model)와 Project Mariner(Takeover Model)는 Reflect 없이 선형 실행한다. Reflect 단계는 에이전트가 자체적으로 실패를 감지하고 전략을 수정하는 데 필수적이며, 이는 사용자의 개입 빈도를 줄여 UX를 크게 개선한다. — *Source*: [[Claude Cowork 플랜 아키텍처]]

4. **엔터프라이즈와 B2C의 HITL 설계 방향이 근본적으로 다르다**: 엔터프라이즈 제품(Salesforce Omni Supervisor, ServiceNow Orchestrator, Workday ASOR)은 1:N 감독(한 명의 관리자가 다수의 에이전트를 모니터링)을 중심으로, B2C 제품(Claude, Manus)은 1:1 개입(사용자가 자신의 에이전트에 직접 개입)을 중심으로 설계한다. 엔터프라이즈 환경의 HITL 아키텍처는 반드시 Supervisor Dashboard를 기본 레이어로 포함해야 하며, 그 위에 개별 사용자의 인라인 승인 레이어를 추가해야 한다. — *Source*: [[salesforce-agentforce]], [[servicenow-now-assist]], [[claude]]

5. **Plan 영속화 방식이 Mid-Task Steering의 품질을 결정한다**: Claude Cowork가 Plan을 마크다운 파일로 저장하여 에이전트와 사용자 모두 수정 가능하게 한 반면, ChatGPT Agent와 Project Mariner는 컨텍스트 메모리에 임시 보관하여 수정이 불가능하다. Plan 영속화는 장기 실행 작업에서 세션 중단/재개, 팀 간 핸드오프, 감사 추적에 필수적이다. — *Source*: [[Claude Cowork 플랜 아키텍처]]

6. **Workday의 ASOR 패러다임은 에이전트 거버넌스의 새로운 표준을 제시한다**: Workday가 AI 에이전트를 "디지털 직원"으로 관리하는 ASOR 개념(채용 -> 온보딩 -> 역할 배정 -> 성과 추적 -> 최적화/퇴직)은 HITL 승인의 상위 레이어로서 "누가 어떤 에이전트에 대해 어떤 수준의 승인 권한을 가지는가"를 정의하는 거버넌스 프레임워크이다. — *Source*: [[workday-assistant]]

---

---

## Source References

### 제품 프로필
- [[salesforce-agentforce]] -- Atlas Reasoning Engine, Omni Supervisor, Command Center, Step-by-Step Reasoning 시각화
- [[claude]] -- Allow/Deny/Ask 3단계 권한 시스템, Agentic Loop, Pause & Ask 패턴, Extended Thinking 시각화
- [[workday-assistant]] -- ASOR 에이전트 관리 패러다임, Manager Bonus 결정 지원, Task Workflow Confirmation
- [[servicenow-now-assist]] -- AI Agent Orchestrator, Chat Summarization 전환, Resolution Notes Review, Proactive Triggers
- [[sap-joule]] -- SuccessFactors 목표 승인, Ariba 검토, Fiori UI 컴플라이언트 응답 렌더링
- [[manus-ai]] -- Glass Box 투명성, Watch & Intervene 패턴, 실시간 브라우저 미러링

### UI 리서치
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 10개 엔터프라이즈 AI 서비스의 HITL 패턴 비교 테이블, Risk-Based Rendering 관찰
- [[Claude Cowork UI 분석]] -- 3패널 레이아웃, Human-In-The-Loop 다이얼로그, PPT/데이터 시각화 Artifacts
- [[Claude Cowork 플랜 아키텍처]] -- Observe-Plan-Act-Reflect 루프, Steering Model vs. Confirmation Model vs. Takeover Model 비교
- [[Claude Cowork 개요]] -- Claude Cowork 강점 분석 (HITL 3단계 권한, Sub-Agent 아키텍처, Visual To-Do List, Mid-Task Steering)

### 외부 참고 자료
- [Salesforce Omni Supervisor Documentation](https://help.salesforce.com/s/articleView?id=service.omnichannel_supervisor_intro.htm)
- [Anthropic Blog: Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) -- Pause & Ask 패턴 안전장치
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)
- [ServiceNow AI Agent Orchestrator 발표](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-announces-new-agentic-AI-innovations)
- [Emerge Haus: The New Dominant UI Design for AI Agents](https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents) -- Two-Pane 아키텍처, Glass Box 패턴

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
