---
type: insight-synthesis
topic_id: agent-planning-reasoning
topic_name: 에이전트 플래닝 & 리즈닝 패턴
category: agent-runtime
tags:
- insight
- agent-runtime
- planning
- reasoning
- chain-of-thought
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- salesforce-agentforce
- manus-ai
- workday-assistant
- microsoft-copilot
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[salesforce-agentforce]]'
- '[[manus-ai]]'
- '[[workday-assistant]]'
- '[[microsoft-copilot]]'
- '[[agent-orchestration-loops]]'
relevant_roles:
- architecture_agent
- backend_agent
- planning_agent
- qa_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - planning
  - reasoning
  - chain-of-thought
  - self-reflection
  - extended thinking
  - ReAct
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 플래닝 & 리즈닝 패턴

## TL;DR

- **에이전트의 추론 방식은 크게 3가지 세대로 분류된다**: (1) 단순 프롬프트 체이닝(1세대), (2) 내부 Chain-of-Thought/Extended Thinking 기반 심층 추론(2세대), (3) 계획-실행-반성의 자기교정형 추론(3세대). 현재 시장 선도 제품은 모두 3세대로 수렴하고 있으나, 구현 깊이와 반성(Reflection) 메커니즘에서 의미 있는 차별화가 발생한다
- **"계획 수립" 전략이 에이전트 성공률을 결정짓는 핵심 변수이다**: Manus AI의 Planner Agent가 복잡한 목표를 수십 개 서브태스크로 사전 분해하는 "계획 선행(Plan-First)" 접근은 병렬 실행과 오류 격리를 가능하게 하며, Salesforce Atlas의 Topic Classification은 계획 진입 전 도메인을 사전 분류하여 잘못된 추론 경로 진입을 차단한다
- **Extended Thinking(Claude)과 Adaptive Computation(OpenAI)은 "추론 연산 할당"이라는 동일한 문제를 반대 방향에서 해결한다**: Claude는 사용자 또는 시스템이 명시적으로 심층 추론 모드를 활성화하는 "Opt-in 확장" 방식이고, OpenAI GPT-5.2는 쿼리 복잡도에 따라 연산량을 자동 할당하는 "적응형 자동 조절" 방식이다
- **Self-Reflection의 깊이가 에이전트 품질의 결정적 차이를 만든다**: Salesforce Atlas의 self-reflection은 정확도 33% 개선이라는 수치적 효과를 입증했고, Manus의 Self-Correction Loop는 오류 원인 분석까지 수행하는 가장 심층적 반성 메커니즘을 구현한다. 반면 Microsoft Copilot과 Workday Assistant는 명시적 self-reflection 계층이 부재하여 추론 품질 개선의 여지가 크다
- **본 문서는 [[agent-orchestration-loops]]와 상호보완적이다**: 오케스트레이션 루프 문서가 루프의 "구조"(Plan-Act-Observe, 계층적, 분산 등)를 다루는 반면, 본 문서는 루프 내부에서 에이전트가 "어떻게 생각하고 계획하는가"에 집중한다

---

## Context

에이전트 플래닝과 리즈닝은 AI 에이전트의 "두뇌" 역할을 하는 핵심 능력이다. 오케스트레이션 루프([[agent-orchestration-loops]] 참조)가 에이전트의 실행 골격(skeleton)을 정의한다면, 플래닝과 리즈닝은 그 골격 내에서 에이전트가 무엇을 어떤 순서로, 왜 수행할지를 결정하는 인지 엔진이다. 동일한 Plan-Act-Observe 루프를 사용하더라도, 계획 수립의 세분도(granularity), 추론의 깊이(depth), 반성의 빈도(frequency)에 따라 에이전트의 성공률과 신뢰성이 근본적으로 달라진다.

엔터프라이즈 AI 에이전트를 개발함에 있어, 플래닝과 리즈닝 전략은 제품의 핵심 경쟁력을 좌우하는 아키텍처 결정이다. 특히 엔터프라이즈 환경에서는 단순한 작업 완수를 넘어, 왜 그 결정을 내렸는지를 설명할 수 있는 추론 투명성(Reasoning Transparency)과, 잘못된 경로를 스스로 감지하고 교정하는 자기교정 능력(Self-Correction)이 고객 신뢰와 규제 준수의 핵심 요건이 된다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 추론 방식 | 계획 수립 전략 | 태스크 분해 | 반성/교정 메커니즘 | 추론 투명성 | 성숙도 |
|---------|----------|-------------|-----------|-----------------|-----------|--------|
| Claude (Anthropic) | Extended Thinking (내부 CoT 블록) | 목표 기반 계획 수립 후 도구 호출 | 단일 에이전트 순차 분해 | 결과 검증 실패 시 계획 재수립 | Thinking 블록 요약 공개 | 높음 |
| OpenAI (GPT-5.2/o3) | Adaptive Computation + RL 기반 추론 | 복잡도 자동 판별 후 연산량 할당 | Codex: 계획 → 코드 → 테스트 순차 | CUA: 막힘 시 사용자 반환 / Codex: 테스트 기반 재시도 | Thinking 블록 (o3/GPT-5.2 Thinking) | 높음 |
| Salesforce Agentforce | Atlas Reasoning Engine (숙고형) | Topic Classification → Action 매핑 | Topic-Action 단위 분해 | Self-Reflection 내장 (정확도 33% 개선) | Step-by-Step Reasoning 시각화 | 중간 |
| Manus AI | 멀티모델 오케스트레이션 | Planner Agent 사전 계획 + 동적 조정 | 수십 개 서브태스크 병렬 분해 | Self-Correction Loop (원인 분석 포함) | Glass Box 실시간 미러링 + 실행 트리 | 중간 |
| Workday Assistant | 서드파티 LLM 기반 (자체 추론 엔진 없음) | ASOR 역할 기반 태스크 범위 제한 | 비즈니스 프로세스 단계별 안내 | Agent Gateway 통한 폴백 | 제한적 (텍스트 응답 중심) | 초기 |
| Microsoft Copilot | Azure OpenAI 기반 (자체 추론 엔진 없음) | Copilot Orchestrator 의도 분류 | 멀티 에이전트 위임 기반 분해 | Plugin 선택 과정 투명 노출 | 경로 시각화 (멀티 에이전트) | 중간 |

### 패턴 분류

#### 패턴 A: Extended Thinking / Deep Reasoning (심층 내부 추론)

**대표 제품**: [[claude]] (Extended Thinking), [[openai]] (o3/GPT-5.2 Thinking Mode)

에이전트가 최종 응답이나 액션을 생성하기 전에 내부적으로 긴 추론 체인(Chain-of-Thought)을 생성하여 복잡한 문제를 단계적으로 분석하는 패턴이다. 사용자에게는 추론 과정의 요약본을 투명하게 공개한다.

**구현 비교**:
- **Claude Extended Thinking**: 사용자 입력 -> 내부 추론 블록 생성(숨김) -> 추론 요약 표시 -> 최종 응답 출력의 단계적 파이프라인으로 구현된다. Extended Thinking은 명시적 토글(Opt-in)로 활성화되며, 활성화 시 내부 추론 블록의 길이에 비례하여 응답 품질이 향상된다. Claude Code/Cowork의 에이전틱 루프에서는 계획 수립 단계에 Extended Thinking이 통합되어, 도구 호출 전 심층 추론을 수행한다
- **OpenAI Adaptive Computation**: GPT-5.2는 쿼리 복잡도에 따라 연산량을 자동 할당하는 적응형 컴퓨팅을 내장한다. Auto 모드에서 자동 판단, Instant 모드에서 즉시 응답, Thinking 모드에서 깊은 추론을 수행한다. o3/o4-mini는 강화학습 기반 깊은 추론 특화 모델로, 추론 과정에 더 많은 연산을 할당하여 수학/과학/복잡한 논리 문제에서 최고 성능을 달성한다

**핵심 차이**: Claude는 "사용자/시스템이 추론 깊이를 결정"하는 명시적 모드 전환 방식이고, OpenAI는 "모델이 자동으로 추론 깊이를 결정"하는 적응형 방식이다. 전자는 비용 통제와 예측 가능성에서 유리하고, 후자는 사용자 편의성에서 유리하다.

- **장점**: 복잡한 멀티스텝 문제에서 정확도 대폭 향상, 추론 과정의 투명성으로 사용자 신뢰 구축, 할루시네이션 감소
- **단점**: 추론 깊이에 비례하는 레이턴시 및 비용 증가, 단순 쿼리에 불필요한 오버헤드 발생 가능

#### 패턴 B: Plan-First Task Decomposition (계획 선행형 태스크 분해)

**대표 제품**: [[manus-ai]] (Planner Agent), [[salesforce-agentforce]] (Atlas Topic Classification)

에이전트가 실행에 앞서 목표를 분석하고, 태스크를 구조화된 서브태스크로 분해한 뒤, 실행 순서와 의존성을 정의하는 계획을 먼저 수립하는 패턴이다.

**구현 비교**:
- **Manus AI Planner Agent**: 중앙 Planner Agent가 사용자의 복잡한 프롬프트를 수십 개 서브태스크로 분해하고, 각 서브태스크를 전문화된 에이전트(Browser, Code, File)에 분배한다. 서브태스크 간 의존성을 관리하며, 실행 중 필요 시 계획을 동적으로 조정한다. 최대 20개 동시 태스크 병렬 처리가 가능하며, 실행 트리(Execution Tree)를 유지하여 진행 상황과 의존성을 추적한다
- **Salesforce Atlas Topic Classification**: 사용자 입력을 먼저 비즈니스 토픽(Sales, Service, Marketing 등)으로 자동 분류한 뒤, 해당 토픽에 매핑된 액션(Flow, Apex, API)을 실행한다. 토픽 분류가 계획 수립의 첫 단계로 기능하여, 잘못된 도메인 진입을 사전에 차단한다. 이후 Atlas가 Plan-Act-Observe 루프 내에서 세부 실행 계획을 수립한다

**핵심 차이**: Manus는 "목표를 서브태스크로 분해하여 병렬 분배"하는 수평적 분해 방식이고, Salesforce는 "도메인을 먼저 분류한 뒤 도메인 내에서 순차 계획"하는 수직적 분류 후 계획 방식이다. 전자는 복잡한 범용 태스크에, 후자는 도메인 특화 엔터프라이즈 시나리오에 적합하다.

- **장점**: 복잡한 태스크의 체계적 처리, 서브태스크 수준의 오류 격리, 병렬 실행을 통한 처리 속도 향상
- **단점**: 계획 수립 자체의 비용(시간/토큰), 사전 계획과 실제 실행 간 괴리(Plan Drift) 발생 가능, 계획 재수립 시 오버헤드

#### 패턴 C: Self-Reflection & Correction (자기 반성형 추론)

**대표 제품**: [[salesforce-agentforce]] (Atlas Self-Reflection), [[manus-ai]] (Self-Correction Loop)

에이전트가 행동의 결과를 단순히 관찰하는 것을 넘어, 결과의 충분성과 정확성을 자체 평가하고, 부족할 경우 추론 전략 자체를 수정하는 반성(Reflection) 메커니즘을 내장한 패턴이다.

**구현 비교**:
- **Salesforce Atlas Self-Reflection**: Plan-Act-Observe 루프의 각 관찰 단계 후 "이 결과가 충분한가?"를 자체 평가하는 self-reflection 단계를 추가한다. 불충분하다고 판단되면 동일한 액션을 재시도하는 것이 아니라, 추론 전략 자체를 재구성하여 다른 접근 방식으로 재시도한다. 이 메커니즘은 초기 파일럿에서 응답 관련성 2배 향상, 엔드투엔드 정확도 33% 개선이라는 수치적 효과를 입증했다
- **Manus AI Self-Correction Loop**: 에이전트가 작업 중 오류를 만나면 (1) 오류 감지 -> (2) 원인 분석 -> (3) 대안 전략 수립 -> (4) 재실행의 4단계 자기교정 사이클을 수행한다. 단순 재시도가 아닌 원인 분석(Root Cause Analysis)을 포함하는 점이 차별적이며, 전체 사이클이 Glass Box UI를 통해 시각적으로 표시되어 사용자가 교정 과정을 실시간으로 관찰할 수 있다
- **Claude 결과 검증**: Claude Code/Cowork의 에이전틱 루프에서 결과 검증 단계를 통해, 도구 호출 결과가 목표와 일치하는지 확인한다. 불일치 시 계획을 재수립하여 재시도한다. Atlas나 Manus 수준의 명시적 self-reflection 레이블링은 없으나, Extended Thinking 내에서 암묵적으로 유사한 자기 검증이 수행된다

- **장점**: 추론 품질의 지속적 개선, 잘못된 경로의 조기 탈출, 수치적으로 입증된 정확도 향상
- **단점**: 반성 단계 추가로 인한 레이턴시 증가, 무한 반성 루프 방지를 위한 상한 설정 필요, 반성의 품질이 기반 모델 능력에 의존

#### 패턴 D: Domain-Constrained Reasoning (도메인 제약형 추론)

**대표 제품**: [[workday-assistant]] (ASOR 역할 기반), [[microsoft-copilot]] (Copilot Orchestrator)

에이전트의 추론 범위를 사전 정의된 도메인, 역할, 권한으로 제약하여, 추론의 자유도를 줄이는 대신 안전성과 예측 가능성을 높이는 패턴이다. 자체적인 깊은 추론 엔진을 구축하기보다, 서드파티 LLM의 추론 능력에 의존하되 그 범위를 거버넌스 레이어로 통제한다.

**구현 비교**:
- **Workday ASOR**: 에이전트의 역할(Role), 데이터 접근 범위(Data Access), 실행 가능한 액션(Actions)을 ASOR에서 명시적으로 정의한다. 에이전트는 할당된 역할의 범위 내에서만 추론하고 행동할 수 있으며, 범위를 벗어나는 요청은 Agent Gateway를 통해 적절한 다른 에이전트로 라우팅된다. 추론 자체는 서드파티 LLM에 의존하나, 추론의 "경계"를 엄격하게 통제한다
- **Microsoft Copilot Orchestrator**: 자연어 요청의 의도를 식별하고, 적절한 데이터 소스(Microsoft Graph, Dataverse, Power Platform 커넥터)를 선택하여 액션을 실행한다. 멀티 에이전트 오케스트레이션 시 각 에이전트의 역할과 접근 가능한 시스템을 사전 정의하여, 추론이 허용된 시스템 범위 내에서만 이루어지도록 한다. Azure OpenAI Service에 추론을 의존하되, Microsoft Entra 기반 인증으로 데이터 접근을 통제한다

- **장점**: 높은 안전성과 예측 가능성, 엔터프라이즈 거버넌스 요구사항 충족, 감사 용이성
- **단점**: 추론의 창의성과 유연성 제한, 사전 정의되지 않은 시나리오에 대한 대응력 부족, LLM 성능 변동에 따른 품질 관리 부담

---

## Key Findings

1. **추론 연산 할당 전략의 이원화가 시장을 분리하고 있다**: Claude의 Extended Thinking(명시적 Opt-in)과 OpenAI GPT-5.2의 Adaptive Computation(자동 할당)은 "누가 추론 깊이를 결정하는가"라는 근본적 설계 철학의 차이를 반영한다. Claude 방식은 API 사용자에게 비용 통제권을 제공하여 엔터프라이즈 환경에서 선호되고, OpenAI 방식은 비기술 사용자의 편의성을 극대화하여 B2C에서 유리하다. 엔터프라이즈 타겟의 경우, 명시적 추론 깊이 제어가 더 적합한 선택이다 -- *Source*: [[claude]], [[openai]]

2. **Self-Reflection은 "있으면 좋은" 기능이 아니라 정확도의 결정적 차이를 만드는 핵심 메커니즘이다**: Salesforce Atlas의 self-reflection이 정확도 33% 개선이라는 수치적 효과를 입증한 것은, 단순 Plan-Act-Observe 루프와 Self-Reflection을 내장한 루프 간의 품질 격차가 상당함을 의미한다. 그럼에도 Microsoft Copilot과 Workday Assistant는 명시적 self-reflection 계층을 두고 있지 않아, 이 영역이 엔터프라이즈 에이전트 시장에서의 차별화 기회임을 시사한다 -- *Source*: [[salesforce-agentforce]], [[microsoft-copilot]], [[workday-assistant]]

3. **태스크 분해의 "세분도(Granularity)"가 에이전트의 병렬성과 오류 격리를 동시에 결정한다**: Manus AI의 Planner Agent가 목표를 수십 개 서브태스크로 세분화하는 접근은, 개별 서브태스크의 실패가 전체 워크플로우를 중단시키지 않는 오류 격리(Fault Isolation)를 가능하게 한다. 반면 Claude Code의 순차적 계획-실행은 단일 실패 지점이 전체 워크플로우에 영향을 줄 수 있다. 단, 세분도가 높을수록 서브태스크 간 상태 동기화와 결과 통합의 복잡성이 증가하는 트레이드오프가 존재한다 -- *Source*: [[manus-ai]], [[claude]]

4. **추론 투명성(Reasoning Transparency) 구현 방식이 사용자 신뢰에 직접적 영향을 준다**: 6개 제품의 추론 투명성 접근법이 명확히 3단계로 분류된다. (1) Glass Box 완전 투명(Manus: 실시간 브라우저 미러링 + 실행 트리 + 코드 노출), (2) 요약 투명(Claude: Thinking 블록 요약, Salesforce: Step-by-Step Reasoning 시각화), (3) 제한적 투명(Microsoft: Plugin 선택 과정 표시, Workday: 텍스트 응답). 투명성이 높을수록 사용자의 대기 불안(Waiting Anxiety)이 감소하고 에이전트에 대한 신뢰도가 향상된다 -- *Source*: [[manus-ai]], [[claude]], [[salesforce-agentforce]], [[microsoft-copilot]]

5. **엔터프라이즈 에이전트에서는 "추론의 자유도"보다 "추론의 경계"가 더 중요하다**: Workday ASOR의 역할 기반 추론 범위 제한과 Salesforce Atlas의 Topic 기반 도메인 제약은, 에이전트가 "무엇이든 할 수 있는" 범용 추론보다 "허용된 범위 내에서 정확하게 추론하는" 제약형 추론이 엔터프라이즈에서 더 가치 있음을 보여준다. 이는 Claude Code/Manus AI 같은 B2C 에이전트의 "최대한 자율적으로 해결" 전략과 명확히 다른 설계 방향이다 -- *Source*: [[workday-assistant]], [[salesforce-agentforce]], [[claude]], [[manus-ai]]

6. **오케스트레이션 루프와 추론 패턴은 독립적으로 조합 가능하며, 최적 조합이 제품마다 다르다**: [[agent-orchestration-loops]]에서 분류한 4가지 오케스트레이션 패턴(Plan-Act-Observe, 계층적, 분산, 평가주도형)과 본 문서의 4가지 추론 패턴(심층 내부 추론, 계획 선행형, 자기 반성형, 도메인 제약형)은 독립적 차원이다. Salesforce는 "Plan-Act-Observe 루프 + Self-Reflection 추론"을, Manus는 "분산 오케스트레이션 + Plan-First 분해 + Self-Correction 추론"을, Microsoft는 "멀티 에이전트 오케스트레이션 + 도메인 제약형 추론"을 조합한다. 최적 조합은 제품의 대상 시장과 도메인에 의존한다 -- *Source*: [[agent-orchestration-loops]]

---

## Recommended Implementation Approach

### 1. Extended Thinking 수준의 심층 추론 계층을 핵심 아키텍처에 내장해야 한다

에이전트의 계획 수립 단계에 Claude Extended Thinking에 준하는 내부 Chain-of-Thought 추론 계층을 설계해야 한다. 단순 프롬프트 전달이 아니라, 복잡한 엔터프라이즈 요청(예: "지난 분기 MVNO 매출이 감소한 원인을 분석하고 개선 방안을 제안해줘")에 대해 에이전트가 내부적으로 다단계 추론을 수행한 뒤 행동으로 옮기는 구조가 필요하다. 비용 통제를 위해 Claude 방식의 명시적 추론 깊이 제어(Opt-in)를 채택하되, 태스크 복잡도에 따라 시스템이 자동으로 추론 모드를 권장하는 하이브리드 접근을 권장한다.

### 2. Self-Reflection을 Plan-Act-Observe 루프에 필수 내장해야 한다

[[agent-orchestration-loops]]에서 권장한 Plan-Act-Observe 기본 루프에, Salesforce Atlas의 self-reflection 메커니즘을 참조하여 매 관찰 단계 후 "결과 충분성 자체 평가" 단계를 추가해야 한다. 구체적으로: (1) 관찰된 결과가 원래 계획의 기대치를 충족하는가? (2) 추가 데이터나 다른 접근 방식이 필요한가? (3) 현재 경로를 계속할 것인가, 계획을 재수립할 것인가?를 매 단계 평가하는 반성 프롬프트를 루프에 내장한다. 무한 반성 루프 방지를 위해 최대 반성 횟수와 비용 상한을 설정해야 한다.

### 3. 도메인 제약형 추론을 거버넌스 계층과 통합 설계해야 한다

엔터프라이즈 환경에서 에이전트의 추론 범위를 사전 정의된 비즈니스 도메인으로 제약하는 Topic Classification 메커니즘을 Salesforce Atlas를 참조하여 구현해야 한다. Workday ASOR의 역할 기반 접근 범위 제한을 참고하여, 에이전트별로 추론이 허용되는 데이터 범위와 액션 범위를 명시적으로 정의하는 거버넌스 레이어를 설계한다. 이를 통해 에이전트가 허용되지 않은 도메인으로 추론이 발산하는 것을 구조적으로 방지한다.

### 4. 추론 투명성을 3단계로 설계하여 사용자 역할에 따라 차별화해야 한다

Manus의 Glass Box, Claude의 Thinking 요약, Salesforce의 Step-by-Step 시각화를 참조하여, 에이전트의 추론 투명성을 사용자 역할별로 차별화한다: (1) 관리자/개발자: Glass Box 수준의 전체 추론 과정 공개(실행 트리, 도구 호출 로그, 중간 결과), (2) 비즈니스 사용자: 요약 수준의 추론 단계 표시(무엇을 왜 결정했는지), (3) 최종 사용자: 결과 중심 응답 + 필요 시 추론 과정 열람 옵션. 특히 엔터프라이즈 감사 요구사항을 충족하기 위해, 모든 추론 단계의 로그가 내부적으로 기록되어야 한다.

### 5. 태스크 분해 세분도를 도메인별로 최적화해야 한다

Manus의 수십 개 서브태스크 병렬 분해와 Claude의 순차 계획 사이에서, 도메인 특성에 맞는 최적 세분도를 결정해야 한다. 정형화된 비즈니스 워크플로우에서는 Salesforce 방식의 도메인 기반 분류 후 순차 실행이 적합하고, 크로스 도메인 분석에서는 Manus 방식의 병렬 분해가 적합하다. 태스크 복잡도를 자동 판별하여 분해 전략을 동적으로 선택하는 메타 계획 레이어를 설계할 것을 권장한다.

---

## Source References

### 제품 프로필
- [[claude]] -- Extended Thinking Pipeline, Agentic Loop (Goal -> Plan -> Tool Call -> Verify -> Iterate), Constitutional AI 기반 안전성 가드레일
- [[openai]] -- GPT-5.2 Adaptive Computation (Auto/Instant/Thinking), o3/o4-mini 강화학습 기반 추론, CUA Screenshot-Action-Verify 루프, Codex 비동기 계획-코드-테스트 워크플로우
- [[salesforce-agentforce]] -- Atlas Reasoning Engine의 숙고형 추론, Topic Classification, Self-Reflection 메커니즘 (정확도 33% 개선), Plan-Act-Observe 루프
- [[manus-ai]] -- Planner Agent 기반 태스크 분해, Self-Correction Loop (오류 감지-원인 분석-대안 시도-재실행), Glass Box 추론 투명성, 멀티모델 오케스트레이션
- [[workday-assistant]] -- ASOR 역할 기반 에이전트 추론 범위 제한, Agent Gateway 폴백, 서드파티 LLM 의존 추론 구조
- [[microsoft-copilot]] -- Copilot Orchestrator 의도 분류, Azure OpenAI 기반 추론, 멀티 에이전트 경로 시각화, Dynamic Planning 기반 자율 에이전트

### 관련 인사이트
- [[agent-orchestration-loops]] -- 오케스트레이션 루프 구조(Plan-Act-Observe, 계층적, 분산, 평가주도형)와의 상호보완 관계. 본 문서는 루프 "내부"의 추론/계획 메커니즘에 집중

### 외부 참고 자료
- [Salesforce Engineering: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)
- [Anthropic Blog: Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [OpenAI: Computer-Using Agent](https://openai.com/index/computer-using-agent/)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
