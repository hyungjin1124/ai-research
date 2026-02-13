---
type: insight-synthesis
topic_id: agent-memory-context
topic_name: 에이전트 메모리 & 컨텍스트 관리
category: agent-runtime
tags:
- insight
- agent-runtime
- memory
- context-management
- session
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- salesforce-agentforce
- glean
- microsoft-copilot
- manus-ai
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[salesforce-agentforce]]'
- '[[glean]]'
- '[[microsoft-copilot]]'
- '[[manus-ai]]'
relevant_roles:
- backend_agent
- data_agent
- qa_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - agent memory
  - context window
  - context management
  - sliding window
  - persistent memory
  - conversation history
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 메모리 & 컨텍스트 관리

## TL;DR

- **에이전트 메모리 시스템은 크게 4가지 패턴으로 분류된다**: (1) 대화 내 슬라이딩 윈도우 기반의 단기 컨텍스트, (2) RAG(Retrieval-Augmented Generation) 기반의 지식 검색 증강 메모리, (3) 세션 간 사용자 선호를 유지하는 Persistent Memory Store, (4) 프로젝트/토픽 단위로 컨텍스트를 고정하는 Project-Scoped Context
- **B2C 제품(Claude, OpenAI)은 "개인화 메모리"에 집중하고, 엔터프라이즈 제품(Salesforce, Microsoft, Glean)은 "조직 지식 그래프"에 집중한다**: Claude Memory와 ChatGPT Memory가 개별 사용자의 선호/배경을 세션 간 기억하는 반면, Glean Enterprise Graph와 Salesforce Data Cloud는 조직 전체의 구조화/비구조화 데이터를 벡터 DB에 인덱싱하여 에이전트의 RAG 컨텍스트로 활용한다
- **컨텍스트 윈도우 크기 경쟁은 "양"에서 "질"로 전환되고 있다**: Claude Sonnet 5(1M 토큰)와 Gemini(1M)가 대용량 컨텍스트를 제공하지만, Glean의 Enterprise Graph나 Salesforce Data Cloud처럼 "필요한 정보만 정확히 검색하여 주입하는" RAG 기반 접근이 엔터프라이즈에서 더 실용적이라는 합의가 형성되고 있다
- **Manus AI의 "14일 비동기 상태 관리"는 장기 실행 에이전트의 새로운 메모리 패러다임을 제시한다**: 세션 기반 대화를 넘어, 태스크별 실행 트리(Execution Tree)를 최대 14일간 유지하며 중간 결과/오류 이력/상태를 추적하는 방식은, 기존의 대화 히스토리 중심 메모리 모델과 근본적으로 다르다
- **엔터프라이즈 컨텍스트 관리의 핵심 차별점은 "권한 인지(Permission-Aware) 메모리"이다**: Glean의 권한 상속 모델과 Salesforce Data Cloud의 RBAC 기반 데이터 접근은, 에이전트가 검색한 정보가 해당 사용자에게 허용된 범위 내인지를 실시간 검증한다. 권한 없는 메모리/컨텍스트는 엔터프라이즈에서 보안 리스크가 된다

---

## Context

엔터프라이즈 AI 에이전트를 개발함에 있어, 에이전트가 "무엇을 기억하고, 어떤 맥락에서 추론하는가"는 응답 품질과 사용자 경험을 결정짓는 핵심 아키텍처 결정이다. 단일 대화 세션 내의 컨텍스트 관리를 넘어, 세션 간 사용자 선호 유지(Persistent Memory), 조직 지식 기반 검색(RAG), 장기 실행 태스크의 상태 관리(Stateful Agent)까지, 메모리와 컨텍스트의 범위가 급격히 확장되고 있다.

특히 엔터프라이즈 환경에서는 "에이전트가 접근할 수 있는 데이터의 범위"가 곧 보안 경계와 직결되기 때문에, 권한 인지(Permission-Aware) 메모리 설계가 기술적 요구사항을 넘어 컴플라이언스 요구사항이 된다. 산업의 경쟁 제품들이 이 문제를 어떤 깊이와 방식으로 해결하고 있는지를 비교 분석하면, 효과적인 메모리 아키텍처 설계에 직접적 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 컨텍스트 윈도우 | 세션 간 메모리 | RAG/지식 검색 | 장기 상태 관리 | 권한 인지 | 성숙도 |
|---------|--------------|-------------|------------|-------------|---------|--------|
| [[claude]] | 200K (Sonnet 5: 1M) | Memory (사용자 선호 기억) | Projects (200K 토큰 상시 컨텍스트) | 세션 기반 (Cowork: 작업 큐) | 제한적 (MCP 서버별 인증) | 중간 |
| [[openai]] | 128K | Memory (선호/배경 기억, 확인/삭제 가능) | Custom GPTs 지식 파일 + Function Calling | Codex: 비동기 샌드박스 (7시간+) | 제한적 | 중간 |
| [[salesforce-agentforce]] | Atlas 엔진 기반 (비공개) | Topic 기반 대화 상태 | Data Cloud RAG (벡터 DB + Zero-Copy) | 없음 (세션 기반) | RBAC + ABAC (Agentforce Gateway) | 높음 |
| [[glean]] | 비공개 (서드파티 LLM 의존) | Personal Graph (업무 패턴 학습) | Enterprise Graph + 100개+ 커넥터 RAG | 없음 (세션 기반) | 원본 권한 실시간 상속 | 높음 |
| [[microsoft-copilot]] | Azure OpenAI 기반 (128K 추정) | Copilot Tuning (조직별 미세 조정) | Microsoft Graph + Dataverse RAG | 자율 에이전트 (long-running) | Microsoft Entra 기반 | 높음 |
| [[manus-ai]] | 멀티모델 (비공개) | 태스크 히스토리 보존 | 브라우저 자동화 기반 실시간 수집 | 실행 트리 14일 유지 | 없음 (B2C 단일 사용자) | 초기 |

### 패턴 분류

#### 패턴 A: Sliding Window + Persistent Memory (슬라이딩 윈도우 + 영속 메모리)

**대표 제품**: [[claude]], [[openai]]

B2C AI 어시스턴트의 기본 패턴으로, 현재 대화 세션 내에서는 컨텍스트 윈도우(128K~1M 토큰)를 슬라이딩 윈도우로 관리하면서, 세션 간에는 별도의 Persistent Memory Store에 사용자 선호/배경 정보를 저장한다. Claude는 Memory 기능으로 대화 간 선호를 기억하고, OpenAI는 Memory를 통해 사용자가 기억된 내용을 직접 확인/삭제할 수 있다.

- **장점**: 구현 복잡성이 낮고, 개인화 경험을 즉시 제공. 사용자가 메모리를 직접 통제(확인/삭제)할 수 있어 투명성 확보
- **단점**: 조직 수준의 지식 공유가 불가능. 컨텍스트 윈도우 크기에 의존하므로 대규모 코드베이스나 문서 분석 시 한계. 메모리 품질(무엇을 기억할지)에 대한 정교한 판단 로직 필요

#### 패턴 B: RAG-Augmented Organizational Memory (RAG 기반 조직 메모리)

**대표 제품**: [[salesforce-agentforce]], [[glean]], [[microsoft-copilot]]

에이전트의 컨텍스트를 조직 전체의 구조화/비구조화 데이터에서 실시간 검색(RAG)하여 증강하는 엔터프라이즈 패턴. Salesforce는 Data Cloud의 벡터 DB에 고객 프로필/거래 이력/외부 데이터를 인덱싱하여 Atlas 추론 엔진에 주입한다. Glean은 100개 이상 SaaS 앱의 데이터를 Enterprise Graph로 통합하여 시맨틱+어휘 하이브리드 검색을 수행한다. Microsoft는 Microsoft Graph와 Dataverse를 통해 Microsoft 365 전반의 데이터를 Copilot Orchestrator에 실시간 제공한다.

- **장점**: 컨텍스트 윈도우 크기에 제약받지 않고 조직 전체 지식에 접근 가능. 기존 업무 시스템의 데이터를 별도 마이그레이션 없이 활용. 권한 체계를 RAG 레이어에 통합하여 보안 준수
- **단점**: 검색 품질(Retrieval Quality)이 응답 품질을 직접 좌우하므로, 인덱싱 정확도/시맨틱 모델 품질에 대한 지속적 투자 필요. 초기 구축(커넥터 설정, 권한 매핑, 인덱싱)에 상당한 시간 소요

#### 패턴 C: Project-Scoped Context (프로젝트 범위 고정 컨텍스트)

**대표 제품**: [[claude]] (Projects), [[openai]] (Custom GPTs)

특정 업무/주제에 맞는 문서, 코드, 지식을 프로젝트 단위로 사전 로드하여 상시 컨텍스트로 유지하는 패턴. Claude Projects는 프로젝트당 최대 200K 토큰의 문서/코드/지식을 고정 컨텍스트로 유지하면서, 프로젝트별 커스텀 지시(Custom Instructions)로 응답 톤/역할/포맷을 제어한다. OpenAI Custom GPTs도 지식 파일을 첨부하여 전문가 페르소나별 컨텍스트를 구성한다.

- **장점**: RAG 대비 검색 지연이 없고, 관련 문서가 항상 컨텍스트에 포함되어 누락 리스크가 낮음. 사용자가 컨텍스트 범위를 명시적으로 통제 가능
- **단점**: 컨텍스트 윈도우 크기에 의존(Claude 200K, Custom GPTs 제한적). 프로젝트가 많아지면 관리 부담 증가. 프로젝트 간 지식 공유가 제한적

#### 패턴 D: Stateful Execution Tree (상태 보존 실행 트리)

**대표 제품**: [[manus-ai]], [[openai]] (Codex), [[microsoft-copilot]] (Autonomous Agents)

대화 히스토리가 아닌, 태스크의 실행 상태(계획, 중간 결과, 오류 이력, 파일 시스템 스냅샷)를 장기간 유지하는 패턴. Manus AI는 클라우드 샌드박스에서 실행 트리를 최대 14일간 보존하며, 사용자가 이탈해도 작업이 지속되는 "Fire and Forget" 모델을 구현한다. OpenAI Codex는 클라우드 샌드박스에서 리포지토리를 프리로드하고 7시간 이상 독립 작업을 수행한다. Microsoft의 자율 에이전트(Autonomous Agents)도 장기 실행 작업에서 동적 계획 수립 능력을 보유한다.

- **장점**: 복잡한 멀티스텝 워크플로우에서 중간 상태를 안정적으로 유지. 비동기 실행으로 사용자 대기 시간 제거. 오류 복구 시 전체 재실행 불필요
- **단점**: 인프라 비용(샌드박스 유지)이 높음. 장기 상태의 일관성 보장이 기술적으로 도전적. 사용자가 상태를 파악하고 개입하는 UX 설계가 복잡

---

## Key Findings

1. **"컨텍스트 윈도우 크기 경쟁"은 실질적 한계에 도달하고 있다**: Claude Sonnet 5(1M 토큰)와 Gemini(1M)가 대용량 컨텍스트를 제공하지만, 실제 엔터프라이즈 시나리오에서는 조직 전체 데이터가 수백만~수십억 토큰에 달하므로 컨텍스트 윈도우만으로는 커버할 수 없다. Glean, Salesforce, Microsoft 모두 RAG 기반 검색 증강을 핵심 전략으로 채택한 것은, 컨텍스트 윈도우의 "양적 확장"보다 "필요한 정보의 정밀 검색"이 엔터프라이즈에서 더 중요하다는 산업적 합의를 반영한다 -- *Source*: [[glean]], [[salesforce-agentforce]], [[microsoft-copilot]]

2. **B2C Memory와 Enterprise Knowledge Graph는 기술적으로 수렴하고 있다**: Claude Memory와 ChatGPT Memory는 "개인 선호/배경"을 기억하고, Glean Personal Graph는 "개인 업무 패턴/협업자/프로젝트"를 학습한다. 표면적으로는 개인화 수준의 차이이지만, 궁극적으로 두 접근 모두 "사용자별 컨텍스트 프로파일"을 구축하는 것이다. B2C 메모리가 조직 수준으로 확장되거나, 엔터프라이즈 그래프가 개인 선호 수준으로 세분화되는 방향으로 수렴할 것으로 예상된다 -- *Source*: [[claude]], [[openai]], [[glean]]

3. **Manus의 "실행 트리 기반 메모리"는 에이전트 메모리의 새로운 차원을 열었다**: 기존 에이전트의 메모리가 "대화 히스토리"(무엇을 말했는가)에 집중한 반면, Manus는 "실행 히스토리"(무엇을 했는가, 어떤 파일을 만들었는가, 어떤 오류를 만났는가)를 메모리의 핵심 단위로 삼는다. 이 패턴은 장기 실행 에이전트에서 대화 기록보다 실행 상태가 더 중요한 컨텍스트임을 입증한다. Self-Correction Loop의 오류 이력이 실행 트리에 누적되어, 동일 오류의 반복을 방지하는 "경험 학습" 효과까지 관찰된다 -- *Source*: [[manus-ai]]

4. **권한 인지(Permission-Aware) 메모리는 엔터프라이즈 채택의 비타협적 요구사항이다**: Glean의 원본 권한 실시간 상속 모델은, 에이전트가 RAG로 검색한 모든 정보가 해당 사용자의 접근 권한 범위 내인지를 보장한다. Salesforce는 Agentforce Gateway에서 ABAC(속성 기반 접근 제어)를 적용하고, Microsoft는 Entra 기반 인증을 Copilot 도구 호출에 연계한다. B2C 제품(Claude, OpenAI, Manus)에서는 이 요구사항이 부재하나, 엔터프라이즈 확장 시 반드시 해결해야 하는 아키텍처적 갭이다 -- *Source*: [[glean]], [[salesforce-agentforce]], [[microsoft-copilot]]

5. **"프로젝트 범위 컨텍스트"는 RAG의 보완재이지 대체재가 아니다**: Claude Projects(200K 토큰 고정 컨텍스트)는 특정 업무 맥락을 안정적으로 유지하는 데 효과적이지만, 조직 전체 지식에 접근할 수 없는 한계가 있다. 반면 RAG는 넓은 범위를 커버하지만 검색 누락(Recall Gap) 리스크가 존재한다. Salesforce의 Data Cloud RAG + Topic 기반 대화 상태, Glean의 Enterprise Graph + Personal Graph 조합처럼, "고정 컨텍스트 + 동적 검색"의 하이브리드가 최적 구성으로 수렴하고 있다 -- *Source*: [[claude]], [[salesforce-agentforce]], [[glean]]

6. **멀티모델 오케스트레이션에서 컨텍스트 전달(Context Handoff)은 미해결 과제이다**: Manus AI가 Planner Agent → Browser Agent → Code Execution Agent로 태스크를 분배할 때, 각 서브 에이전트 간 컨텍스트 전달의 효율성과 정확성이 전체 워크플로우 품질을 결정한다. Microsoft의 멀티 에이전트 오케스트레이션에서도 에이전트 간 실행 경로/핵심 단계/관련 시스템을 추적하는 시각화가 필요한 것은, 컨텍스트 손실(Context Loss)이 멀티 에이전트 시스템의 주요 실패 원인임을 시사한다 -- *Source*: [[manus-ai]], [[microsoft-copilot]]

---

## Recommended Implementation Approach

1. **하이브리드 메모리 아키텍처를 설계해야 한다**: "Project-Scoped Context(고정) + RAG(동적) + Persistent Memory(개인화)"의 3계층 메모리 아키텍처를 구현해야 한다. 1계층은 업무/프로젝트별 핵심 문서를 상시 컨텍스트로 유지하고, 2계층은 조직 전체 데이터에서 필요 시 검색하여 주입하며, 3계층은 사용자별 선호/업무 패턴을 세션 간 유지한다. Claude Projects + Glean Enterprise Graph + ChatGPT Memory의 장점을 결합한 설계가 최적이다.

2. **권한 인지(Permission-Aware) RAG를 1일 차부터 설계해야 한다**: Glean의 원본 권한 상속 모델을 참고하여, 에이전트가 검색하는 모든 데이터에 사용자별 접근 권한 검증을 내장해야 한다. 이는 나중에 추가하기 어려운 기반 아키텍처 결정이므로, RAG 파이프라인 설계 초기부터 RBAC/ABAC 레이어를 통합해야 한다. Salesforce의 Data Cloud RBAC와 Microsoft Entra 연동 패턴이 구체적 참고 모델이다.

3. **장기 실행 에이전트를 위한 Stateful Execution 메모리를 로드맵에 포함해야 한다**: Manus AI의 실행 트리 패턴을 참고하여, 에이전트가 복잡한 멀티스텝 비즈니스 워크플로우(예: 월말 정산, 다단계 승인, 장기 리서치)를 처리할 때 중간 상태를 안정적으로 보존하는 메커니즘이 필요하다. 대화 히스토리 기반 메모리만으로는 이러한 시나리오를 커버할 수 없다.

4. **컨텍스트 윈도우 전략은 "크기 극대화"보다 "효율적 활용"에 집중해야 한다**: 1M 토큰 컨텍스트 윈도우를 제공하는 것보다, 200K 토큰 내에서 가장 관련성 높은 정보를 정밀하게 배치하는 것이 비용 대비 효과가 높다. Semantic Layer를 활용하여 비즈니스 용어-데이터 스키마 매핑을 정의하고, 이를 기반으로 RAG 검색 정확도를 높이는 전략이 필요하다.

5. **멀티 에이전트 간 컨텍스트 공유 프로토콜을 표준화해야 한다**: 멀티 에이전트 아키텍처를 도입할 경우, 에이전트 간 컨텍스트 전달(Context Handoff)의 표준 포맷과 프로토콜을 정의해야 한다. Microsoft의 멀티 에이전트 오케스트레이션에서 각 에이전트의 실행 경로를 시각화하는 패턴과, Manus의 Planner Agent가 서브태스크 간 의존성을 관리하는 패턴을 참고하여, 컨텍스트 손실을 최소화하는 핸드오프 메커니즘을 설계해야 한다.

---

## Source References

### 제품 프로필
- [[claude]] -- Projects(200K 토큰 상시 컨텍스트), Memory(세션 간 선호 기억), Styles(개인화), 컨텍스트 윈도우 200K~1M, Extended Thinking 추론 파이프라인
- [[openai]] -- Memory(선호/배경 기억, 확인/삭제 가능), Custom GPTs(지식 파일 컨텍스트), Codex(7시간+ 비동기 샌드박스 실행), 128K 컨텍스트 윈도우
- [[salesforce-agentforce]] -- Atlas Reasoning Engine(계획-행동-관찰 루프), Data Cloud RAG(벡터 DB + Zero-Copy), Topic 기반 대화 상태 관리, ABAC 기반 거버넌스
- [[glean]] -- Enterprise Graph(지식 그래프 + Personal Graph), 100개+ 커넥터 RAG, 원본 권한 실시간 상속, Agentic Engine 2(멀티스텝 자율 추론)
- [[microsoft-copilot]] -- Microsoft Graph + Dataverse RAG, Copilot Tuning(조직별 미세 조정), 멀티 에이전트 오케스트레이션, Entra 기반 권한 관리, 자율 에이전트 장기 실행
- [[manus-ai]] -- 실행 트리(14일 상태 보존), Fire and Forget 비동기 패턴, Self-Correction Loop 오류 이력 추적, Planner Agent 멀티 에이전트 컨텍스트 분배

### UI 리서치
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 컨텍스트 관리 방식 비교 참조

### 외부 참고 자료
- [Anthropic Blog: Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)
- [OpenAI: ChatGPT Memory](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [Glean Blog: Enterprise Graph & Personal Graph](https://www.glean.com/blog/live-fall-25-main)
- [Salesforce Engineering: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)
- [Microsoft Learn: Copilot for Finance and Operations Overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
