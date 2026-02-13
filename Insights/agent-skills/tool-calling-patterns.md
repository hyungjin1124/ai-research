---
type: insight-synthesis
topic_id: tool-calling-patterns
topic_name: Tool Calling & Function Calling 패턴 비교
category: agent-skills
tags:
- insight
- agent-skills
- tool-calling
- function-calling
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- google-gemini
- salesforce-agentforce
- microsoft-copilot
- workday-assistant
- snowflake-intelligence
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[google-gemini]]'
- '[[salesforce-agentforce]]'
- '[[microsoft-copilot]]'
- '[[workday-assistant]]'
- '[[snowflake-intelligence]]'
relevant_roles:
- backend_agent
- qa_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - tool calling
  - function calling
  - JSON schema
  - parallel tool call
  - tool chain
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# Tool Calling & Function Calling 패턴 비교

## TL;DR

- **Tool Calling 패턴은 크게 4가지로 분류된다**: (1) JSON Schema 기반 Function Calling(OpenAI, Claude API), (2) MCP 프로토콜 기반 표준화 도구 호출(Claude, Microsoft, Salesforce, Workday, Snowflake), (3) Topic-Action 매핑 기반 비즈니스 프로세스 호출(Salesforce Agentforce), (4) Compositional Function Calling 기반 네이티브 도구 체이닝(Google Gemini)
- **"Schema-First" vs "Semantic-First"의 분기가 진행 중이다**: OpenAI와 Claude는 개발자가 JSON Schema로 도구를 엄격하게 정의하는 접근을, Salesforce와 Snowflake는 비즈니스 의미론(Topic/Semantic Model)으로 도구를 발견하는 접근을 취한다. 엔터프라이즈에서는 Semantic-First가 비기술 사용자 접근성에서 유리하다
- **Parallel Tool Calling과 Multi-Step Chaining 지원이 에이전트 성능의 핵심 차별점이다**: OpenAI(parallel_tool_calls), Claude(병렬 MCP 호출), Gemini(compositional function-calling)가 단일 턴에서 다중 도구를 병렬/순차 호출하는 반면, 엔터프라이즈 벤더들은 오케스트레이터(Atlas, Copilot Orchestrator, Cortex Agent)를 통해 멀티스텝 체이닝을 관리한다
- **도구 호출의 거버넌스 레이어가 B2C와 엔터프라이즈를 가르는 핵심 차이다**: B2C 제품(Claude, OpenAI, Gemini)은 도구 호출 자체의 파라미터 정확도에 집중하는 반면, 엔터프라이즈 제품(Salesforce, Microsoft, Workday, Snowflake)은 RBAC, ABAC, 감사 로그, 할당량 제한 등 거버넌스를 도구 호출 파이프라인에 필수적으로 내장한다
- **MCP가 Tool Calling의 사실상 표준 인터페이스로 수렴하고 있으나, 각 벤더는 MCP 위에 독자적 오케스트레이션/거버넌스 레이어를 추가한다**: 순수 MCP만으로는 엔터프라이즈 요구사항을 충족하지 못하며, 이 "MCP+" 레이어가 각 벤더의 실질적 차별점이 되고 있다

---

## Context

Tool Calling(또는 Function Calling)은 AI 에이전트가 외부 시스템의 기능을 호출하여 실제 작업을 수행하는 핵심 메커니즘이다. 단순한 텍스트 응답을 넘어 데이터 조회, API 실행, 비즈니스 프로세스 트리거까지 에이전트의 행동 범위를 결정짓는 아키텍처 결정이다.

2025~2026년 현재, Tool Calling 방식은 OpenAI가 선도한 JSON Schema 기반 Function Calling에서 출발하여, Anthropic의 MCP 표준화, Google의 Compositional Function Calling, Salesforce/Workday의 비즈니스 프로세스 매핑 방식까지 다양하게 분화되고 있다. 이 분화 속에서 어떤 패턴을 채택하고 어떤 깊이로 구현할 것인지가 에이전트 프로덕트의 개발자 경험, 엔터프라이즈 통합 용이성, 생태계 확장성을 직접 좌우한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | Tool Calling 방식 | 스키마 정의 | 병렬 호출 | 에러 핸들링 | 거버넌스 | 스트리밍 | 성숙도 |
|---------|------------------|-----------|---------|-----------|---------|---------|--------|
| Claude (Anthropic) | MCP Tools + API Tool Use | JSON Schema (inputSchema) | 병렬 MCP 호출 지원 | 에이전트 루프 내 재시도 | MCP 서버 레벨 | 스트리밍 응답 지원 | 높음 (GA) |
| OpenAI | Function Calling + MCP (Agents SDK) | JSON Schema (parameters) | parallel_tool_calls 옵션 | Responses API 내장 재시도 | API 레벨 (rate limit) | 스트리밍 지원 | 높음 (GA) |
| Google Gemini | Compositional Function Calling + MCP | FunctionDeclaration (OpenAPI 기반) | 네이티브 병렬/순차 체이닝 | 에이전트 루프 내 자동 복구 | API 레벨 | 스트리밍 지원 | 높음 (GA) |
| Salesforce Agentforce | Topic-Action 모델 + MCP (3.0) | Flow/Apex/API Action 정의 | Atlas Engine 오케스트레이션 | Guardrails + 에스컬레이션 | ABAC (Agentforce Gateway) | 3.0부터 GA | 중간 (3.0 GA) |
| Microsoft Copilot | Power Platform 커넥터 + MCP | 커넥터 스키마 + MCP 도구 | Copilot Orchestrator 관리 | 오케스트레이터 재시도/폴백 | Entra ID + Orchestrator | 실시간 스트리밍 | 높음 (GA) |
| Workday Assistant | Agent Gateway (MCP/A2A) + ASOR | MCP 도구 + A2A 태스크 정의 | Agent Gateway 라우팅 | ASOR 기반 에이전트별 폴백 | RBAC + ASOR 라이프사이클 | 미확인 | 초기 (Early Adopter) |
| Snowflake Intelligence | Cortex Agent 도구 + MCP Server | Semantic Model (YAML) + MCP 도구 | Cortex Agent 멀티도구 | Agentic Loop 재시도 | 행/열 RBAC + MCP RBAC | REST API 스트리밍 | 중간 (GA) |

### 패턴 분류

#### 패턴 A: Schema-First Function Calling (스키마 우선 함수 호출)

**대표 제품**: OpenAI, Claude (API 레벨)

개발자가 JSON Schema로 함수의 이름, 설명, 파라미터 타입, 필수 여부를 엄격하게 정의하면, 모델이 사용자 요청을 분석하여 적절한 함수와 파라미터를 선택한다. OpenAI의 Function Calling이 이 패턴을 2023년에 최초로 대중화했으며, Claude API의 Tool Use도 동일한 접근을 채택한다. 모델이 `tool_use` 블록으로 함수명과 JSON 파라미터를 반환하면, 클라이언트가 실행 후 결과를 `tool_result`로 돌려주는 Request-Response 루프 구조다.

- **장점**: 타입 안전성이 높고 예측 가능한 동작, 개발자 친화적인 명시적 인터페이스, 파라미터 검증이 스키마 수준에서 보장됨
- **단점**: 모든 도구를 수동으로 스키마 정의해야 하는 개발 부담, 비기술 사용자가 도구를 추가/수정하기 어려움, 도구 수가 늘어나면 모델의 선택 정확도가 하락할 수 있음

#### 패턴 B: Protocol-Mediated Tool Discovery (프로토콜 기반 도구 발견)

**대표 제품**: Claude (MCP), Microsoft Copilot (MCP + Power Platform), Workday (MCP/A2A), Snowflake (MCP Server)

MCP 프로토콜을 통해 도구가 자기 자신을 "발견 가능한(discoverable)" 형태로 노출하고, 에이전트가 런타임에 사용 가능한 도구 목록을 동적으로 탐색하여 호출한다. MCP 서버가 `tools/list` 엔드포인트로 도구 카탈로그를 제공하고, 클라이언트(에이전트)가 이를 조회하여 필요한 도구를 선택하는 구조다. Claude Code가 수백 개의 MCP 서버를 동적으로 연결하는 것이 대표적이며, Snowflake는 Cortex Analyst/Search를 MCP 도구로 자동 노출하고, Microsoft는 Copilot Studio에서 MCP 도구를 네이티브로 소비한다.

- **장점**: 도구의 동적 발견과 플러그앤플레이 확장이 가능, 벤더 간 상호운용성 표준화, 도구 제공자와 소비자의 분리(decoupling)로 생태계 확장 용이
- **단점**: 동적 발견에 따른 레이턴시 오버헤드, MCP 프로토콜만으로는 엔터프라이즈급 인증/인가/감사 불충분, 도구 품질의 일관성 보장 어려움

#### 패턴 C: Business Process Mapping (비즈니스 프로세스 매핑)

**대표 제품**: Salesforce Agentforce, Workday Assistant

도구 호출을 기술적 함수 인터페이스가 아닌 비즈니스 프로세스의 추상화로 접근한다. Salesforce는 Topic(비즈니스 주제)과 Action(실행 가능한 비즈니스 작업)의 2계층 구조로, 사용자 의도를 먼저 Topic으로 분류한 뒤 해당 Topic에 매핑된 Action(Flow, Apex, API, MuleSoft)을 실행한다. Workday는 ASOR에 등록된 에이전트의 역할(Role)과 데이터 접근 범위(Data Access)에 따라 실행 가능한 액션이 자동 결정된다. 이 패턴에서 "도구"는 기술적 API가 아니라 "리드 육성", "결산 프로세스", "채용 승인" 같은 비즈니스 도메인 단위로 정의된다.

- **장점**: 비기술 사용자(비즈니스 관리자)가 도구를 이해하고 구성 가능, 비즈니스 컨텍스트에 의한 높은 호출 정확도, 거버넌스가 비즈니스 규칙 수준에서 자연스럽게 적용됨
- **단점**: 범용적 도구 호출이 아닌 특정 비즈니스 도메인에 종속, 플랫폼 외부 시스템과의 연결에 추가 통합 레이어(MuleSoft, Agent Gateway) 필요, 유연성 대비 설정 복잡성 증가

#### 패턴 D: Compositional Native Tool Chaining (네이티브 도구 조합 체이닝)

**대표 제품**: Google Gemini

모델 자체에 도구 조합(composition) 능력을 네이티브로 내장하여, 단일 턴에서 여러 도구를 병렬 또는 순차적으로 체이닝한다. Gemini의 Compositional Function Calling은 Google Search, Code Execution, 사용자 정의 함수를 모델이 직접 조합하여 하나의 응답을 구성한다. 별도의 오케스트레이터 없이 모델 자체가 도구 실행 계획을 수립하고 중간 결과를 다음 도구의 입력으로 전달하는 implicit chaining을 수행한다.

- **장점**: 오케스트레이터 없는 저지연 도구 체이닝, 모델이 도구 간 데이터 흐름을 자연스럽게 관리, 개발자가 체이닝 로직을 명시적으로 구현할 필요 없음
- **단점**: 모델 의존도가 극도로 높아 디버깅이 어려움, 체이닝 로직의 투명성/감사 가능성 부족, 외부 오케스트레이터 대비 복잡한 분기/에러 핸들링이 제한적

#### 패턴 E: Semantic Layer-Mediated Invocation (시맨틱 레이어 기반 호출)

**대표 제품**: Snowflake Intelligence

도구 호출 전에 Semantic Layer(의미론적 계층)를 통해 자연어 요청을 구조화된 비즈니스 의미로 변환한 뒤 도구를 호출한다. Snowflake의 YAML 기반 Semantic Model이 "매출"이라는 자연어를 `SUM(revenue)` 메트릭과 정확히 매핑하고, 이 매핑 정보를 Cortex Analyst가 참조하여 SQL을 생성한다. Cortex Agent는 이 Semantic Layer를 기반으로 Analyst(정형)와 Search(비정형) 도구를 자동 라우팅한다.

- **장점**: 비즈니스 용어와 기술적 실행 간의 정확한 매핑으로 할루시네이션 최소화, 도메인 전문가가 Semantic Model을 관리하여 도구 정확도를 지속 개선 가능, RBAC를 Semantic Layer에 자연스럽게 통합
- **단점**: Semantic Model 초기 구축에 상당한 노력 필요, 모델 유지보수 부담(스키마 변경 시 동기화), 데이터 분석 도메인에 특화되어 범용 도구 호출에는 부적합

---

## Key Findings

1. **Function Calling의 "파라미터 정확도"가 에이전트 품질의 병목이며, 이를 해결하는 접근이 세 갈래로 분화 중이다**: OpenAI/Claude는 JSON Schema의 엄격한 타입 정의와 descriptions 최적화로 모델 자체의 파라미터 생성 정확도를 높이는 "모델 중심" 접근을, Salesforce/Workday는 Topic/ASOR 기반 사전 필터링으로 도구 선택 범위를 좁히는 "컨텍스트 제한" 접근을, Snowflake는 Semantic Model로 자연어-스키마 간 매핑을 사전 정의하는 "의미론적 매핑" 접근을 취한다. 세 접근은 상호 배타적이지 않으며, 조합 적용이 가능하다 -- *Source*: [[openai]], [[claude]], [[salesforce-agentforce]], [[snowflake-intelligence]]

2. **Parallel Tool Calling 지원 여부가 에이전트의 실질적 처리 속도를 2~5배 차이나게 한다**: OpenAI는 `parallel_tool_calls` 파라미터로 단일 턴에서 다중 함수 호출을 명시적으로 지원하고, Claude Code는 MCP 서버 다중 연결에서 병렬 도구 실행을 수행하며, Gemini는 compositional function-calling으로 암묵적 병렬 처리를 한다. 반면 Topic-Action 모델(Salesforce)은 Topic 분류 후 순차적 Action 실행이 기본이어서, 복수의 독립적 데이터 조회가 필요한 시나리오에서 레이턴시 차이가 발생한다 -- *Source*: [[openai]], [[claude]], [[google-gemini]], [[salesforce-agentforce]]

3. **엔터프라이즈 벤더의 "오케스트레이터"가 Tool Calling의 실질적 제어 지점이며, MCP/Function Calling은 그 하위 실행 계층이다**: Salesforce의 Atlas Reasoning Engine(Plan-Act-Observe 루프), Microsoft의 Copilot Orchestrator(의도 식별-데이터 소스 검색-액션 실행), Snowflake의 Cortex Agent(태스크 분할-도구 선택-결과 평가) 모두 도구 호출 자체가 아닌 "언제, 어떤 순서로, 어떤 도구를" 호출할지를 결정하는 오케스트레이션 레이어를 핵심으로 삼는다. Tool Calling 프로토콜(MCP, Function Calling)은 이 오케스트레이터의 실행 수단일 뿐이다 -- *Source*: [[salesforce-agentforce]], [[microsoft-copilot]], [[snowflake-intelligence]]

4. **OpenAI의 Responses API가 Function Calling과 에이전트 도구를 단일 인터페이스로 통합하는 새로운 패러다임을 제시한다**: 기존에 분리되어 있던 Function Calling(사용자 정의 함수), 웹 검색, 코드 실행, 파일 분석을 Responses API 하나로 통합하면서, "도구"의 범위가 개발자 정의 함수를 넘어 플랫폼 내장 기능까지 확장되었다. 이는 Assistants API의 한계(상태 관리 복잡성, 도구 호출 비동기 처리)를 해소하면서, Claude의 MCP 기반 확장과는 다른 "플랫폼 내재화" 전략을 보여준다 -- *Source*: [[openai]]

5. **Tool Calling 에러 핸들링 전략이 B2C와 엔터프라이즈에서 근본적으로 다르다**: B2C 에이전트(Claude Code, ChatGPT Agent, Gemini)는 에이전트 루프 내에서 자동 재시도와 대안 도구 선택으로 에러를 자율 복구하는 반면, 엔터프라이즈 에이전트(Agentforce, Copilot, Workday)는 에러 시 Human-in-the-Loop 에스컬레이션을 기본 패턴으로 채택한다. Salesforce의 Guardrails, Microsoft의 Proposal Summary 검토, Workday의 Task Workflow Confirmation은 모두 도구 호출 실패 시 "안전하게 멈추는" 전략이다 -- *Source*: [[claude]], [[openai]], [[salesforce-agentforce]], [[microsoft-copilot]], [[workday-assistant]]

---

## Source References

### 제품 프로필
- [[claude]] -- MCP 3가지 프리미티브(Tools, Resources, Prompts), Claude Code 에이전틱 루프의 도구 호출 패턴, Agentic Loop 아키텍처
- [[openai]] -- Function Calling(JSON Schema), Responses API 도구 통합, parallel_tool_calls, Agents SDK MCP 지원, CUA 도구 체인
- [[google-gemini]] -- Compositional Function Calling, 네이티브 도구 호출(Google Search, Code Execution, 사용자 정의 함수), Interactions API
- [[salesforce-agentforce]] -- Topic-Action 모델, Atlas Reasoning Engine(Plan-Act-Observe), MuleSoft Agent Fabric, Agentforce Gateway(ABAC), MCP 3.0 내장
- [[microsoft-copilot]] -- Copilot Orchestrator, Power Platform 1,000+ 커넥터, MCP 네이티브 지원, Dynamics 365 F&O MCP Server, 멀티 에이전트 오케스트레이션
- [[workday-assistant]] -- Agent Gateway(MCP/A2A), ASOR 에이전트 라이프사이클, Agent Partner Network 50+ 파트너, Flowise Agent Builder, 역할 기반 액션 제어
- [[snowflake-intelligence]] -- Cortex Agent 도구 오케스트레이션, YAML Semantic Model, Managed MCP Server, RBAC 기반 도구 발견/호출, Cortex Analyst/Search 도구 노출

### 외부 참고 자료
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Google Gemini Function Calling Documentation](https://ai.google.dev/gemini-api/docs/function-calling)
- [Salesforce Atlas Reasoning Engine Architecture](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)
- [Snowflake Cortex Agent Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
