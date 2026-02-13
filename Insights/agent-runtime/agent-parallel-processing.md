---
type: insight-synthesis
topic_id: agent-parallel-processing
topic_name: 에이전트 병렬 처리 패턴
category: agent-runtime
tags:
- insight
- agent-runtime
- parallel-processing
- multi-agent
- orchestration
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- salesforce-agentforce
- microsoft-copilot
- manus-ai
- workday-assistant
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[salesforce-agentforce]]'
- '[[microsoft-copilot]]'
- '[[manus-ai]]'
- '[[workday-assistant]]'
relevant_roles:
- backend_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - parallel processing
  - concurrent agents
  - fan-out fan-in
  - async execution
  - multi-agent parallel
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 병렬 처리 패턴

## TL;DR

- **병렬 처리 구현 수준은 제품별로 극명하게 갈린다**: Manus AI는 Planner Agent가 서브태스크를 최대 20개까지 동시 분배하는 Fan-Out/Fan-In 패턴을 프로덕션 수준으로 구현한 유일한 B2C 제품이며, Microsoft Copilot은 멀티 에이전트 오케스트레이션으로 이종 에이전트 간 작업 위임과 결과 공유를 GA로 제공한다
- **대부분의 제품은 "Sequential Chain + 도구 병렬 호출" 수준에 머물러 있다**: Claude(Code/Cowork), OpenAI(Codex/Agent), Salesforce(Atlas Engine)는 단일 에이전트 루프 내에서 도구를 순차 호출하는 구조이며, 진정한 멀티 에이전트 병렬 실행은 아직 제한적이다
- **엔터프라이즈 제품은 병렬 처리보다 "에이전트 간 협업 거버넌스"에 초점을 맞춘다**: Workday의 ASOR + Agent Gateway, Salesforce의 Agentforce Gateway는 병렬 에이전트의 권한/감사/라이프사이클 관리를 우선시하며, 이는 엔터프라이즈 환경에서 병렬 처리의 선결 조건이 거버넌스임을 시사한다
- **Supervisor-Worker 패턴이 멀티 에이전트 병렬 처리의 지배적 아키텍처로 수렴 중이다**: Manus의 Planner Agent, Microsoft의 Copilot Orchestrator, Workday의 Agent Gateway 모두 중앙 Supervisor가 전문화된 Worker 에이전트에 태스크를 분배하고 결과를 수집하는 동일한 패턴을 따른다
- **비동기 실행(Async Execution)은 병렬 처리의 전제 조건이자 UX 차별화 요소이다**: Manus(14일 비동기), OpenAI Codex(7시간+ 비동기), Claude Cowork(작업 큐)가 비동기 실행을 지원하며, 이는 사용자가 여러 태스크를 동시에 위임하고 결과를 나중에 확인하는 "Fire and Forget" 패턴의 기반이 된다

---

## Context

엔터프라이즈 AI 에이전트를 개발함에 있어, 단일 에이전트의 순차 실행만으로는 복잡한 비즈니스 워크플로우(예: 다수 시스템의 데이터를 동시 조회하여 통합 보고서를 생성하거나, 여러 부서의 승인을 병렬로 처리)를 효율적으로 수행할 수 없다. 병렬 처리 패턴은 에이전트의 처리량(throughput)과 응답 시간(latency)을 결정짓는 핵심 아키텍처 결정이며, 특히 멀티 에이전트 오케스트레이션이 2025년 하반기부터 산업의 주요 차별화 포인트로 부상하고 있다.

산업 분석 결과, 병렬 처리의 구현 깊이는 (1) 단일 에이전트 내 도구 병렬 호출, (2) 복수 에이전트의 동시 실행(Fan-Out/Fan-In), (3) 이종 에이전트 간 비동기 협업의 3단계로 분류되며, 각 단계마다 필요한 오케스트레이션 인프라와 거버넌스 요구사항이 크게 달라진다. 이 분석은 6개 경쟁 제품의 병렬 처리 접근 방식을 비교하여, 효과적인 멀티 에이전트 아키텍처 설계에 실질적 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 병렬 처리 접근 방식 | 핵심 특징 | 동시 태스크 수 | 비동기 지원 | 성숙도 |
|---------|-------------------|----------|-------------|-----------|--------|
| [[claude]] | 단일 에이전트 루프 + Cowork 작업 큐 | Agentic Loop 순차 실행, Cowork에서 작업 큐 병렬 처리 도입 | 1개 (Code/Chrome), 큐 기반 (Cowork) | 제한적 (Cowork 작업 큐) | 초기 (병렬은 Cowork Preview) |
| [[openai]] | 독립 샌드박스 병렬 실행 | Codex 각 태스크를 독립 클라우드 샌드박스에서 실행, CUA는 순차 | 다수 (Codex), 1개 (Agent) | 지원 (Codex 7시간+) | 중간 (Codex GA) |
| [[salesforce-agentforce]] | Topic-Action 순차 오케스트레이션 | Atlas Engine의 Plan-Act-Observe 루프, 단일 에이전트 중심 | 1개 (에이전트당) | 미지원 (실시간 대화 중심) | 중간 (3.0 GA) |
| [[microsoft-copilot]] | 멀티 에이전트 오케스트레이션 | Copilot Orchestrator가 이종 에이전트 간 작업 위임/결과 공유 | 복수 에이전트 협업 | 지원 (Autonomous Agents) | 높음 (GA, Build 2025) |
| [[manus-ai]] | Planner Agent Fan-Out/Fan-In | 중앙 Planner가 서브태스크를 전문 에이전트에 병렬 분배 | 최대 20개 동시 태스크 | 지원 (최대 14일) | 높음 (프로덕션 GA) |
| [[workday-assistant]] | Agent Gateway 기반 에이전트 간 협업 | ASOR + MCP/A2A로 자사+파트너 에이전트 통합 관리 및 연결 | 복수 에이전트 (Gateway 경유) | 지원 (Agent Gateway) | 초기 (Early Adopter) |

### 패턴 분류

#### 패턴 A: Fan-Out/Fan-In (분산 수집형)

**대표 제품**: [[manus-ai]]

중앙 Planner Agent가 사용자의 복잡한 요청을 수십 개의 서브태스크로 분해한 후, 각 서브태스크를 전문화된 Worker 에이전트(Browser Agent, Code Execution Agent, File Generation Agent)에 병렬 분배한다. 각 Worker가 독립 샌드박스에서 작업을 완료하면, Planner가 결과를 수집(Fan-In)하여 최종 산출물로 통합한다. Manus는 최대 20개 태스크를 동시 실행하며, 각 태스크가 최대 14일까지 비동기로 지속될 수 있어 대규모 리서치, 데이터 수집 등 장기 병렬 작업에 최적화되어 있다.

- **장점**: 처리량(throughput) 극대화, 장기 태스크 지원, 서브태스크 간 독립성으로 장애 격리 용이
- **단점**: 서브태스크 간 의존성이 있는 워크플로우에서 Planner의 조율 복잡성 증가, 크레딧 소모량 예측 어려움, 태스크 실패 시 부분 결과만 남는 리스크

#### 패턴 B: Supervisor-Worker Orchestration (감독자-작업자형)

**대표 제품**: [[microsoft-copilot]], [[workday-assistant]]

중앙 Orchestrator(Copilot Orchestrator / Agent Gateway)가 요청을 분석하여 적절한 에이전트에 작업을 위임하고, 각 에이전트의 실행 경로와 결과를 추적한다. Fan-Out/Fan-In과 유사하나, Worker가 반드시 동시에 실행되는 것이 아니라 Supervisor의 판단에 따라 순차 또는 병렬로 실행되는 점이 다르다. Microsoft는 Microsoft 365, Azure AI, Fabric에서 구축된 이종 에이전트를 오케스트레이션하며, Workday는 ASOR에 등록된 자사+파트너 에이전트를 Agent Gateway를 통해 연결한다.

- **장점**: 이종 에이전트(서로 다른 벤더, 서로 다른 도메인) 간 협업 가능, 중앙 거버넌스 적용 용이, 동적 계획 수립(dynamic planning)으로 런타임에 실행 전략 조정
- **단점**: Orchestrator가 병목(bottleneck)이 될 수 있음, 이종 에이전트 간 데이터 포맷/프로토콜 호환성 관리 부담, 에이전트 수 증가 시 조율 오버헤드 증가

#### 패턴 C: Independent Sandbox Parallelism (독립 샌드박스 병렬형)

**대표 제품**: [[openai]] (Codex)

각 태스크를 완전히 독립된 클라우드 샌드박스에서 실행하여, 태스크 간 간섭 없이 병렬 처리한다. OpenAI Codex는 태스크마다 리포지토리를 프리로드한 독립 컨테이너를 생성하고, 계획 수립 → 코드 작성 → 테스트 → 결과 제출을 자율적으로 수행한다. 태스크 간 조율이나 결과 통합은 사용자의 몫이며, 에이전트 레벨에서의 Fan-In은 없다.

- **장점**: 태스크 간 완전한 격리로 안정성 극대화, 샌드박스 단위 리소스 관리 용이, 태스크별 독립적 롤백 가능
- **단점**: 태스크 간 컨텍스트 공유 불가, 결과 통합은 사용자 수동 작업, 에이전트 간 협업 시나리오 미지원

#### 패턴 D: Sequential Chain with Tool Parallelism (순차 체인 + 도구 병렬형)

**대표 제품**: [[claude]] (Code/Chrome), [[salesforce-agentforce]]

단일 에이전트가 Plan → Act → Observe 루프를 순차적으로 반복하되, 개별 Act 단계에서 여러 도구를 병렬로 호출할 수 있다. Claude Code의 Agentic Loop는 목표 설정 → 계획 수립 → 도구 호출 → 결과 검증을 반복하는 순차 구조이며, Salesforce Atlas Engine도 Plan-Act-Observe 순환을 단일 에이전트 내에서 수행한다. 멀티 에이전트 수준의 병렬 처리는 아직 지원하지 않는다.

- **장점**: 구현 복잡성이 낮음, 단일 에이전트의 일관된 컨텍스트 유지, 디버깅 용이, Human-in-the-Loop 승인 포인트 명확
- **단점**: 처리량이 에이전트의 순차 실행 속도에 종속, 복잡한 멀티스텝 워크플로우에서 지연 시간 증가, 에이전트 간 분업 불가

#### 패턴 E: Registry-Governed Agent Mesh (레지스트리 기반 에이전트 메시형)

**대표 제품**: [[workday-assistant]]

ASOR(Agent System of Record)가 에이전트의 라이프사이클(등록-온보딩-역할배정-성과추적)을 통합 관리하고, Agent Gateway가 MCP/A2A 프로토콜로 에이전트 간 통신을 중계한다. 50개 이상 파트너의 에이전트를 동일 레지스트리에서 관리하며, 각 에이전트의 데이터 접근 범위, 국가별 가용성, 실행 권한을 명시적으로 정의한다. 병렬 처리 자체보다 "누가 무엇에 접근하여 무엇을 실행할 수 있는가"의 거버넌스에 초점을 맞춘 모델이다.

- **장점**: 멀티벤더 에이전트 환경에서 유일하게 통합 거버넌스 제공, 감사(audit) 추적 용이, 에이전트 성과 기반 최적화 가능, A2A 프로토콜로 이종 시스템 간 상호운용성 확보
- **단점**: 오케스트레이션 런타임 최적화보다 관리/거버넌스에 집중하여 실행 성능 최적화는 미흡, Agent Gateway 아직 Early Adopter 단계

---

## Key Findings

1. **병렬 처리의 "실행 단위"가 제품의 아키텍처 철학을 결정한다**: Manus는 "태스크"를, Microsoft는 "에이전트"를, OpenAI Codex는 "샌드박스"를 병렬 실행의 기본 단위로 삼는다. 이 선택에 따라 격리 수준, 컨텍스트 공유 방식, 장애 대응 전략이 근본적으로 달라진다. Manus의 태스크 단위 병렬은 처리량에, Microsoft의 에이전트 단위 병렬은 협업 유연성에, Codex의 샌드박스 단위 병렬은 안정성에 각각 최적화되어 있다 -- *Source*: [[manus-ai]], [[microsoft-copilot]], [[openai]]

2. **B2C 제품(Manus)이 엔터프라이즈 제품(Salesforce, Workday)보다 병렬 실행 성숙도가 높다**: Manus는 최대 20개 동시 태스크를 프로덕션에서 지원하지만, Salesforce Agentforce는 아직 단일 에이전트 순차 처리 중심이고 Workday Agent Gateway는 Early Adopter 단계이다. 이는 B2C 환경에서의 빠른 실험-검증 사이클과 엔터프라이즈 환경에서의 거버넌스 우선 접근의 차이를 반영한다 -- *Source*: [[manus-ai]], [[salesforce-agentforce]], [[workday-assistant]]

3. **비동기 실행 지원 여부가 병렬 처리의 실질적 가치를 좌우한다**: Manus(14일), OpenAI Codex(7시간+), Claude Cowork(작업 큐)가 비동기 실행을 지원하면서 사용자가 여러 태스크를 동시에 위임하는 것이 가능해졌다. 반면 Salesforce Atlas Engine과 Claude Code는 실시간 세션 기반으로, 사용자가 에이전트 옆에 있어야 하는 동기 모델이다. 비동기 실행은 병렬 처리를 "기술적 가능성"에서 "실용적 워크플로우"로 전환하는 핵심 요인이다 -- *Source*: [[manus-ai]], [[openai]], [[claude]]

4. **멀티 에이전트 오케스트레이션의 거버넌스 레이어가 엔터프라이즈 도입의 게이트키퍼이다**: Microsoft Copilot Orchestrator는 각 에이전트의 실행 경로를 사용자에게 시각적으로 표시하고, Workday ASOR는 에이전트별 RBAC과 국가별 가용성을 명시적으로 관리한다. 병렬 에이전트가 서로 다른 데이터에 접근하고 서로 다른 액션을 실행할 때, 누가 무엇을 했는지 추적할 수 없으면 엔터프라이즈에서 채택되지 않는다 -- *Source*: [[microsoft-copilot]], [[workday-assistant]]

5. **Claude Cowork의 "작업 큐 병렬 처리"는 Anthropic의 멀티 에이전트 전략 전환 신호이다**: Claude Code가 단일 에이전트 순차 루프인 반면, 2026년 1월 출시된 Claude Cowork는 VM 샌드박스 내에서 작업 큐 기반 병렬 처리를 도입했다. 이는 Anthropic이 순차 에이전트에서 병렬 에이전트로의 아키텍처 전환을 시작했음을 시사하며, Opus 4.6의 "에이전트 팀 지원" 특성과 맞물려 멀티 에이전트 Fan-Out 패턴이 가까운 미래에 등장할 가능성이 있다 -- *Source*: [[claude]]

---

## Recommended Implementation Approach

1. **Supervisor-Worker 패턴을 기본 아키텍처로 채택하되, Fan-Out/Fan-In 확장을 설계해야 한다**: 6개 제품 중 멀티 에이전트 병렬 처리를 가장 성공적으로 구현한 Manus와 Microsoft 모두 중앙 Supervisor가 Worker에 태스크를 분배하는 패턴을 따른다. 중앙 Orchestrator가 비즈니스 프로세스를 분해하여 전문 에이전트(데이터 조회, 보고서 생성, 승인 처리 등)에 분배하는 구조를 채택하되, 서브태스크 간 의존성 그래프를 관리하여 독립 태스크는 병렬로, 의존 태스크는 순차로 실행하는 동적 스케줄링을 구현해야 한다.

2. **비동기 실행 인프라를 병렬 처리의 기반으로 우선 구축해야 한다**: Manus의 14일 비동기 실행, Codex의 장기 샌드박스 실행이 보여주듯, 진정한 병렬 처리는 비동기 태스크 큐 위에서만 실현된다. 에이전트 런타임에 비동기 태스크 큐(task queue), 태스크 상태 머신(state machine), 결과 수집기(result aggregator)를 핵심 인프라로 설계해야 하며, 이는 MCP의 2025년 11월 비동기 연산 스펙과도 연계된다.

3. **병렬 에이전트 거버넌스를 Day 1부터 설계에 포함해야 한다**: Workday의 ASOR 모델과 Microsoft의 Multi-Agent 경로 시각화가 보여주듯, 엔터프라이즈 고객은 "어떤 에이전트가 어떤 데이터에 접근하여 어떤 액션을 수행했는가"의 완전한 감사 추적을 요구한다. 병렬 에이전트 각각의 실행 로그, 데이터 접근 기록, 결과 산출물을 에이전트 레지스트리에서 통합 추적하는 거버넌스 레이어를 병렬 처리 아키텍처와 동시에 설계해야 한다.

4. **태스크 분해(Task Decomposition) 엔진의 품질이 병렬 처리 효과를 결정한다**: Manus의 Planner Agent가 복잡한 요청을 수십 개 서브태스크로 분해하는 능력이 전체 시스템의 효율성을 좌우하듯, 비즈니스 프로세스를 병렬화 가능한 단위로 분해하는 Task Decomposition 엔진을 핵심 컴포넌트로 개발해야 한다. 이때 Salesforce의 Topic-Action 모델처럼 비즈니스 도메인별 분해 규칙을 사전 정의하면 분해 정확도를 높일 수 있다.

5. **실행 경로 시각화를 멀티 에이전트 UX의 필수 요소로 포함해야 한다**: Microsoft Copilot의 Multi-Agent 경로 시각화와 Manus의 Glass Box 투명성 패턴이 보여주듯, 여러 에이전트가 동시에 작업할 때 사용자는 "지금 무슨 일이 벌어지고 있는지" 파악하지 못하면 불안감을 느낀다. 각 에이전트의 실행 상태, 진행률, 의존 관계를 실시간으로 시각화하는 오케스트레이션 대시보드를 설계해야 한다.

---

## Source References

### 제품 프로필
- [[claude]] -- Agentic Loop 순차 구조, Claude Cowork 작업 큐 병렬 처리, Opus 4.6 에이전트 팀 지원
- [[openai]] -- Codex 독립 샌드박스 병렬 실행, CUA 순차 에이전트 루프, Responses API 통합 인터페이스
- [[salesforce-agentforce]] -- Atlas Reasoning Engine Plan-Act-Observe 루프, Topic-Action 오케스트레이션, 단일 에이전트 중심 구조
- [[microsoft-copilot]] -- 멀티 에이전트 오케스트레이션 GA, Copilot Orchestrator, Multi-Agent 경로 시각화, Autonomous Agents 장기 실행
- [[manus-ai]] -- Planner Agent Fan-Out/Fan-In, 최대 20개 동시 태스크, 14일 비동기 실행, Glass Box 투명성
- [[workday-assistant]] -- ASOR 에이전트 레지스트리, Agent Gateway MCP/A2A, Agent Partner Network 50+ 파트너, 에이전트 라이프사이클 관리

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [Microsoft Build 2025: Multi-Agent Orchestration](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/)
- [Workday: Agent Gateway & Agent Partner Network](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
- [Manus AI 공식 사이트](https://manus.im)
- [OpenAI: Introducing Codex](https://openai.com/index/introducing-codex/)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
