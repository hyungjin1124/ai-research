---
type: insight-synthesis
topic_id: dashboard-composition
topic_name: 대시보드 구성 및 멀티 에이전트   UI 레이아웃 패턴
category: agent-ui
tags:
- insight
- agent-ui
- dashboard
- layout-patterns
- monitoring
- widget
status: draft
confidence: high
last_updated: '2026-02-10'
source_products:
- salesforce-agentforce
- microsoft-copilot
- databricks-mosaic-ai
- servicenow-now-assist
- workday-assistant
- thoughtspot-spotter
- snowflake-intelligence
- glean
source_files:
- '[[엔터프라이즈 AI 서비스 비교 분  석]]'
- '[[salesforce-agentforce]]'
- '[[microsoft-copilot]]'
- '[[databricks-mosaic-ai]]'
- '[[servicenow-now-assist]]'
- '[[workday-assistant]]'
relevant_roles:
- frontend_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - dashboard
  - multi-agent UI
  - layout pattern
  - widget
  - command center
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 대시보드 구성 및 멀티 에이전트 UI 레이아웃 패턴

## TL;DR

- 엔터프라이즈 AI 에이전트 대시보드는 크게 **4가지 레이아웃 패턴**으로 분류된다: Sidecar Embedded, Supervisor Command Center, Agent Registry Grid, Dual-Pane Analytics. 대부분의 제품은 역할(관리자/일반 사용자/개발자)에 따라 2~3개 레이아웃을 병행 제공한다.
- **멀티 에이전트 상태 모니터링 UI**는 "에이전트를 직원처럼 관리하는 패러다임"(Workday ASOR)과 "에이전트를 서비스 인스턴스로 관리하는 패러다임"(Salesforce Omni Supervisor, ServiceNow Orchestrator)으로 양분되며, ERP 맥락상 ASOR 방식이 더 자연스럽다.
- **위젯 기반 모듈형 대시보드**(Microsoft Copilot Home, ThoughtSpot Liveboards)가 커스터마이징 측면에서 가장 유연하며, PIN/드래그/필터 기반의 개인화 기능이 사용자 채택률을 결정하는 핵심 요소이다.
- **에이전트 활동 오버뷰**는 단순 로그 나열이 아닌, "Morning Briefing" 카드 뉴스 패턴(ThoughtSpot/Dynamics 365)과 Proactive Trigger 알림 피드(ServiceNow)를 결합해야 실질적인 의사결정 가속 효과를 얻는다.
- 엔터프라이즈 환경에서 ERP 에이전트 대시보드를 구축할 경우, **Role-Adaptive Layout(역할별 레이아웃 자동 전환) + Agent Registry + 위젯 커스터마이징 + Morning Briefing 피드**의 4요소 조합이 최적의 대시보드 전략이다.

---

## Context

엔터프라이즈 AI 에이전트가 단일 챗봇 인터페이스를 넘어 조직 전반에 걸친 다수의 자율 에이전트로 확장되면서, "여러 에이전트의 활동과 상태를 어떻게 통합적으로 보여줄 것인가"가 핵심 UX 설계 과제로 부상하고 있다. 대시보드는 단순한 데이터 시각화 도구가 아니라, 관리자의 에이전트 감독(Supervision), 일반 사용자의 업무 컨텍스트 유지(Context Continuity), 경영진의 성과 추적(Performance Tracking)이 교차하는 정보 허브이다.

엔터프라이즈 AI 에이전트 프로덕트가 ERP 데이터(재무, 인사, 운영)를 기반으로 복수의 에이전트가 동시에 활동하는 환경을 지원해야 한다면, 경쟁사들이 채택한 대시보드 구성 패턴과 멀티 에이전트 모니터링 UI를 체계적으로 분석하고, 역할별 최적 레이아웃, 위젯 구성 전략, 알림/이벤트 피드 설계를 수립할 필요가 있다. 특히 ERP 도메인에서는 Morning Briefing(일일 핵심 지표 브리핑), 이상징후 알림, 에이전트 실행 결과 요약이 사용자 의사결정 속도에 직접적인 영향을 미치므로, 대시보드가 단순 모니터링을 넘어 "행동 유도(Action-Oriented)" 인터페이스로 설계되어야 한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 대시보드 레이아웃 | 위젯/커스터마이징 | 에이전트 모니터링 | 활동 오버뷰/브리핑 | 알림/이벤트 피드 | 비고 |
|---------|----------------|-----------------|-----------------|-------------------|----------------|------|
| **Salesforce Agentforce** | 3-Panel Builder + Omni Supervisor + Command Center | Agent Actions Library 기반 모듈 구성 | Omni Supervisor: AI+인간 에이전트 통합 실시간 테이블, Listen-in | Command Center KPI 대시보드 (헬스, 대화량, 해결률) | 에스컬레이션 건 추적, 인터랙션 테이블 요약 컬럼 | 서비스 감독자 중심 설계 |
| **Microsoft Copilot (D365)** | Sidecar + Copilot Home (역할별) + Embedded Banner | Widget 기반 모듈형, Role-specific views, Real-time 업데이트 | Manager Insights Dashboard, Multi-Agent 경로 시각화 | Copilot Home 역할별 추천 액션/인사이트 요약 | Timeline Highlights, Follow-up Suggestions | Sidecar에서 full-screen 폐지 결정 주목 |
| **Databricks Mosaic AI** | Agent Evaluation Review App + AI Playground + Monitoring UI | Tools Catalog (Unity Catalog), Vector Search 통합 | MLflow 3.0 프로덕션 트레이스, 비용/레이턴시/품질 실시간 | Evaluation Metrics 시각화, Root Cause Analysis | 배포 파이프라인 상태, Cost/Latency 트레이드오프 알림 | 개발자/ML 엔지니어 대상 |
| **ServiceNow Now Assist** | Now Assist Panel (Embedded) + MyNow (개인화) + Admin Console | Theme Builder 브랜딩, Multiple Assistant Profiles, Service Portal config | AI Agent Orchestrator: 멀티 에이전트 팀 조율, 정책 대비 실시간 평가 | Skills/Plugins 관리 대시보드, Usage aggregation | Proactive Triggers/Notifications, Genius Result Card | ITSM 워크플로우 깊은 통합 |
| **Workday Assistant** | Unified Experience (Single View) + Agent Registry Dashboard | Illuminate Agents 통합, Business Process Orchestration | ASOR: 에이전트를 직원처럼 리스트/필터/검색, 성과 추적 | Cross-app 실시간 집계, Budget Overrun Alerts | Expense/Logistics 알림, Rule-based Alerts | ASOR 패러다임 차별화 |
| **ThoughtSpot Spotter** | SpotterViz Liveboards + Chat-Canvas 이중 패널 | Note tiles, Cross filters, Verified Liveboards, PIN 기반 개인화 | Usage Analytics Dashboard, SpotterCode IDE | Starter Questions, 대시보드 특정 지표 질의 | In-app commenting, 드릴다운 후속 질문 | 셀프서비스 BI 최강 |
| **Snowflake Intelligence** | 독립 인터페이스 (ai.snowflake.com) + Cortex Analyst UI | Data Agent selector, Multiple semantic layers | Usage statistics, Cost/Latency metrics | SQL 생성 및 실행 시각화, Semantic View 탐색 | Row/column governance tracking | 데이터 분석 특화 |

### 패턴 분류

#### 패턴 A: Sidecar Embedded (사이드카 임베디드)

기존 업무 애플리케이션의 우측(또는 하단)에 AI 패널을 배치하여, 사용자가 업무 컨텍스트를 벗어나지 않은 채 에이전트와 상호작용하는 패턴. 레코드 상단에 요약/인사이트 배너를 배치하고, 사이드 패널에서 후속 질의를 처리하는 이중 구조가 일반적이다.

- **대표 제품**: Microsoft Copilot for Dynamics 365 (Sidecar + Embedded Banner), ServiceNow Now Assist (Now Assist Panel), SAP Joule (SAP Start/Work Zone Embedded)
- **장점**: 업무 흐름의 연속성 보장, 맥락 전환(context switching) 최소화, 기존 UI에 친숙한 사용자에게 낮은 학습 곡선
- **단점**: 사이드 패널의 공간 제약으로 복잡한 데이터 시각화나 멀티 에이전트 상태 표시에 한계. Microsoft가 full-screen 뷰를 2025년 9월부터 단계적 폐지한 것은 Sidecar 중심 전략의 강화이지만, 일부 사용자에게는 제약으로 작용
- **적용**: ERP 트랜잭션 화면(전표 입력, 결재, 재고 조회 등)에서 컨텍스트 내 에이전트 지원에 최적. 단, 대시보드 메인 화면에는 Sidecar만으로 부족하며 별도의 대시보드 레이아웃이 필요

*Source*: [[microsoft-copilot]], [[servicenow-now-assist]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 B: Supervisor Command Center (감독자 통합 관제)

관리자/감독자가 다수의 에이전트(AI + 인간)의 활동을 실시간으로 모니터링하고, KPI를 추적하며, 필요 시 개입하는 전용 대시보드. 인터랙션 테이블, 성과 지표 차트, 에스컬레이션 큐를 단일 화면에 통합 배치한다.

- **대표 제품**: Salesforce Agentforce (Omni Supervisor + Command Center -- AI 에이전트와 인간 에이전트를 동일 인터페이스에서 모니터링, Listen-in 기능, 대화 요약 컬럼이 포함된 인터랙션 테이블, 에이전트 헬스/대화량/해결률/평균 응답 시간 KPI), ServiceNow (AI Agent Orchestrator -- 멀티 에이전트 팀 협업 조율, 정책 대비 실시간 평가, Assist 토큰 예산 관리), Microsoft Copilot (Manager Insights Dashboard -- 대화 분석, 에이전트 성과, 사용량 추적)
- **장점**: 조직 규모의 에이전트 운영에 필수, 실시간 성과 가시성 확보, 컴플라이언스 감사 추적에 유리
- **단점**: 일반 사용자에게는 과도한 정보 노출, 구축 비용과 복잡성이 높음
- **적용**: IT 관리자/운영팀을 위한 에이전트 관제 대시보드의 핵심 패턴. Salesforce Command Center의 KPI 구성을 참고하되, ERP 도메인 KPI(트랜잭션 처리량, 오류율, 결산 진행률 등)로 대체 가능

*Source*: [[salesforce-agentforce]], [[servicenow-now-assist]], [[microsoft-copilot]]

#### 패턴 C: Agent Registry Grid (에이전트 레지스트리 그리드)

모든 AI 에이전트를 카드 또는 리스트 형태로 나열하고, 각 에이전트의 상태/권한/성과를 필터/검색/정렬하여 관리하는 패턴. 에이전트를 "디지털 직원"으로 다루는 ASOR(Agent System of Record) 개념에서 비롯되었다.

- **대표 제품**: Workday Assistant (Agent Registry Dashboard -- 에이전트를 인간 직원처럼 리스트/필터/검색, 역할/데이터 접근/액션 정의, 활성/비활성 상태, 국가별 가용성, 보안 그룹 표시), Salesforce (Agentforce Studio -- Agent Actions Library, 학습 리소스, 게이트웨이 구성 통합 허브), Glean (Agent Orchestration Dashboard -- Agent 추천 시스템, AI Apps Gallery)
- **장점**: 다수의 에이전트를 체계적으로 탐색/관리, 에이전트 라이프사이클(등록-온보딩-운영-퇴직) 가시화, 거버넌스 관점에서 감사 편의성 높음
- **단점**: 실시간 활동 모니터링보다는 정적 관리에 초점, 에이전트 수가 적을 때는 오버 엔지니어링
- **적용**: 에이전트가 10개 이상으로 확장될 때 반드시 필요한 패턴. ASOR의 라이프사이클 관리를 참고하여, 에이전트 등록/권한 설정/성과 추적을 단일 그리드에서 관리할 수 있음

*Source*: [[workday-assistant]], [[salesforce-agentforce]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 D: Dual-Pane Analytics (이중 패널 분석형)

좌측/하단의 대화(Chat) 패널과 우측/중앙의 캔버스(Canvas) 패널로 구성된 이중 구조. 대화에서 질의하면 캔버스에 심층 리포트, 차트, 비교 분석 테이블이 생성되는 방식이다.

- **대표 제품**: ThoughtSpot Spotter (SpotterViz Liveboards -- Chat 입력 + Analytics Canvas, Best-fit 시각화 자동 선택, Drill-anywhere, Note tiles/Cross filters 기반 커스터마이징, PIN을 통한 대시보드 개인화), Snowflake Intelligence (Cortex Analyst UI -- 독립 인터페이스에서 NL-to-SQL + 시각화 캔버스)
- **장점**: 대화형 탐색과 깊이 있는 데이터 시각화를 동시에 제공, 셀프서비스 분석에 최적, 사용자가 필요한 차트를 대화로 생성하여 대시보드에 PIN하는 점진적 대시보드 구성이 가능
- **단점**: 에이전트 모니터링/관리보다는 데이터 분석에 초점, 사전 구성된 운영 대시보드가 필요한 상황에서는 부족
- **적용**: ERP 데이터 분석 화면(재무 분석, 비용 분석, 인력 분석)에 적합. PIN/드릴다운/Cross filter 패턴을 참고하여, 사용자가 대화로 원하는 시각화를 생성하고 개인 대시보드에 고정하는 기능을 구현할 수 있음

*Source*: [[엔터프라이즈 AI 서비스 비교 분석]], ThoughtSpot Spotter, Snowflake Intelligence

---

## Key Findings

1. **"역할별 레이아웃 자동 전환(Role-Adaptive Layout)"이 엔터프라이즈 대시보드의 필수 요소이다**: Microsoft Copilot Home은 사용자 직무에 따라 관련 인사이트, 추천 액션, 최근 활동 요약을 자동으로 다르게 구성한다. ServiceNow의 MyNow는 사용자별 역할/권한에 맞춘 개인화 AI 서비스 허브를 제공한다. 관리자는 Supervisor Command Center를, 일반 사용자는 Sidecar + 개인화 홈을, 경영진은 KPI 오버뷰를 기본 화면으로 각각 다르게 배치해야 하며, 하나의 고정 레이아웃으로는 다양한 역할의 니즈를 충족할 수 없다. -- *Source*: [[microsoft-copilot]], [[servicenow-now-assist]]

2. **Sidecar 패턴과 독립 대시보드의 이원 구조가 업계 표준으로 수렴하고 있다**: Microsoft는 full-screen Copilot 뷰를 폐지하고 Sidecar 중심으로 전환하면서도 별도의 Copilot Home 대시보드를 유지한다. ServiceNow는 Now Assist Panel(Sidecar)과 Admin Console(독립 대시보드)을 병행한다. 이는 "업무 중 컨텍스트 내 AI 지원"과 "에이전트 종합 관리/분석"이 근본적으로 다른 사용 시나리오이며, 하나의 인터페이스로 통합하려는 시도는 양쪽 모두를 저해한다는 것을 의미한다. -- *Source*: [[microsoft-copilot]], [[servicenow-now-assist]], [[엔터프라이즈 AI 서비스 비교 분석]]

3. **ASOR(Agent System of Record) 패러다임이 대시보드 설계 자체를 변화시킨다**: Workday가 에이전트를 "디지털 직원"으로 관리하는 ASOR를 도입하면서, 대시보드의 최상위 탐색 객체가 "기능"이나 "워크플로우"가 아닌 "에이전트 엔티티"가 되었다. Agent Registry에서 에이전트를 선택하면 해당 에이전트의 역할, 권한, 성과, 실행 이력이 펼쳐지는 구조는, 전통적인 기능 중심 대시보드와 근본적으로 다른 정보 아키텍처를 요구한다. -- *Source*: [[workday-assistant]]

4. **위젯 PIN/드래그 기반 점진적 대시보드 구성이 사용자 채택을 높인다**: ThoughtSpot의 Liveboards에서 사용자가 대화형 분석 결과를 PIN하여 자신만의 대시보드를 점진적으로 구축하는 패턴은, 사전 구성된 고정 대시보드보다 사용자 참여도가 높다. [[엔터프라이즈 AI 서비스 비교 분석]]에서도 "PIN 기능"이 좋은 서비스의 핵심 요소로 평가되었다. 이는 "개발자가 사전 정의한 대시보드"와 "사용자가 AI와 대화하며 점진적으로 구축하는 대시보드"를 병행해야 함을 시사한다. -- *Source*: [[엔터프라이즈 AI 서비스 비교 분석]], ThoughtSpot Spotter

5. **"Morning Briefing" 패턴이 ERP 대시보드의 킬러 기능으로 부상한다**: [[엔터프라이즈 AI 서비스 비교 분석]]에서 제안된 Morning Briefing 모드는 -- 앱 실행 시 전야 변동된 주요 ERP 지표를 카드 뉴스 형태로 브리핑하고, 핵심 KPI/이상징후/원인 Top 3/추천 액션 Top 3를 각 카드에 "왜?" 버튼(드릴다운 질문 템플릿)과 함께 제공하는 것이다. 이는 ThoughtSpot의 Starter Questions 패턴과 ServiceNow의 Proactive Triggers를 결합한 것으로, 사용자가 대시보드를 수동으로 탐색하는 대신 AI가 선제적으로 주목해야 할 사항을 제시하는 "Push형 대시보드"이다. -- *Source*: [[엔터프라이즈 AI 서비스 비교 분석]]

6. **멀티 에이전트 경로 시각화의 깊이가 제품 성숙도를 반영한다**: Microsoft Copilot의 Multi-Agent 오케스트레이션 경로 시각화(각 에이전트의 실행 경로/단계/관련 시스템 표시), Salesforce Atlas의 Step-by-Step Reasoning 시각화(Topic -> Action -> Record -> Grounding), Databricks의 프로덕션 트레이스(MLflow 3.0 기반 단계별 추적)는 각각 다른 수준의 에이전트 활동 투명성을 제공한다. 가장 투명한 대시보드는 "에이전트가 무엇을 했는지"뿐 아니라 "왜 그렇게 했는지"까지 추론 과정을 시각화한다. -- *Source*: [[microsoft-copilot]], [[salesforce-agentforce]], [[databricks-mosaic-ai]]

---

## 소스 제품 매핑

| 인사이트 주제 | 관련 제품 프로필 |
|-------------|----------------|
| Sidecar 임베디드 레이아웃 | [[microsoft-copilot]], [[servicenow-now-assist]] |
| Supervisor Command Center | [[salesforce-agentforce]], [[servicenow-now-assist]], [[microsoft-copilot]] |
| ASOR 에이전트 레지스트리 | [[workday-assistant]] |
| Dual-Pane 분석형 대시보드 | [[엔터프라이즈 AI 서비스 비교 분석]] (ThoughtSpot, Snowflake) |
| 위젯 커스터마이징/PIN | [[엔터프라이즈 AI 서비스 비교 분석]] (ThoughtSpot Liveboards) |
| Morning Briefing 패턴 | [[엔터프라이즈 AI 서비스 비교 분석]] |
| 에이전트 평가/모니터링 UI | [[databricks-mosaic-ai]] |
| Proactive 알림/이벤트 피드 | [[servicenow-now-assist]], [[workday-assistant]] |
| 멀티 에이전트 경로 시각화 | [[microsoft-copilot]], [[salesforce-agentforce]] |

---

---

## Source References

### 제품 프로필
- [[salesforce-agentforce]] -- Omni Supervisor, Command Center, 3-Panel Builder Layout, Atlas Step-by-Step Reasoning 시각화, Agentforce Studio
- [[microsoft-copilot]] -- Sidecar 패턴, Copilot Home 역할별 대시보드, Manager Insights Dashboard, Multi-Agent 경로 시각화, Embedded Banner
- [[databricks-mosaic-ai]] -- Agent Evaluation Review App, AI Playground, Monitoring UI, MLflow 3.0 프로덕션 트레이스, Unity Catalog 거버넌스
- [[servicenow-now-assist]] -- Now Assist Panel (Embedded Sidecar), MyNow 개인화, Admin Console, AI Agent Orchestrator, Proactive Triggers, Genius Result Card, Theme Builder
- [[workday-assistant]] -- ASOR Agent Registry Dashboard, Unified Experience (Single View), Budget Overrun Alerts, Cross-app 실시간 집계, Agent Lifecycle 관리

### UI 리서치
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 10개 엔터프라이즈 AI 서비스의 대시보드 구성 비교, Sidecar/독립화면 장단점, Dual-Pane Architecture, Morning Briefing 모드 제안, PIN 기능, 드릴다운 패턴, ThoughtSpot Liveboards, Snowflake Intelligence UI

### 외부 참고 자료
- [Salesforce Agentforce 3.0: Command Center, MCP, and Apps](https://www.salesforceben.com/salesforce-announces-agentforce-3-0-command-center-mcp-and-apps/)
- [Salesforce Omni Supervisor Documentation](https://help.salesforce.com/s/articleView?id=service.omnichannel_supervisor_intro.htm)
- [Microsoft Copilot for Dynamics 365 공식 사이트](https://www.microsoft.com/en-us/dynamics-365/copilot)
- [Microsoft Ignite 2025: Copilot and Agents](https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-ignite-2025-copilot-and-agents-built-to-power-the-frontier-firm/)
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)
- [ServiceNow AI Agent Orchestrator 발표](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-announces-new-agentic-AI-innovations)
- [ThoughtSpot Spotter Documentation](https://docs.thoughtspot.com/cloud/10.10.0.cl/spotter)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
