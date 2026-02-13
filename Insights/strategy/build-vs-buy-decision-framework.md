---
type: insight-synthesis
topic_id: build-vs-buy-decision-framework
topic_name: Build vs Buy 의사결정 프레임워크
category: strategy
tags:
- insight
- strategy
- build-vs-buy
- decision-framework
status: current
confidence: medium
last_updated: '2026-02-11'
source_products:
- salesforce-agentforce
- microsoft-copilot
- openai
- claude
- google-gemini
- servicenow-now-assist
- workday-assistant
- sap-joule
- snowflake-intelligence
- databricks-mosaic-ai
- glean
- manus-ai
- vercel-v0
- samsung-sds-fabrix
- lgcns-agenticworks
source_files:
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/openai/openai.md
- AI Agent Products/claude/claude.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/snowflake-intelligence/snowflake-intelligence.md
- AI Agent Products/databricks-mosaic-ai/databricks-mosaic-ai.md
- AI Agent Products/glean/glean.md
- AI Agent Products/manus-ai/manus-ai.md
- AI Agent Products/vercel-v0/vercel-v0.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
relevant_roles:
- architecture_agent
- backend_agent
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI agent build vs buy
  - agent orchestration framework
  - enterprise AI tech stack
  - LLM abstraction layer
  - AI 에이전트 기술스택
  - 에이전트 자체개발 외부도입
  - AI 플랫폼 아키텍처 전략
  review_trigger:
    mode: auto
    priority_override: true
    threshold: 3
  update_zones:
  - id: llm
    match_keywords:
    - LLM
    - 기반 모델
    - GPT
    - Claude
    - Gemini
    - 멀티 LLM
    section: '#### 1. LLM (기반 모델) 계층'
  - id: agent-framework
    match_keywords:
    - 오케스트레이션
    - 에이전트 프레임워크
    - Atlas
    - ASOR
    section: '#### 2. 에이전트 프레임워크/오케스트레이션 계층'
  - id: rag
    match_keywords:
    - RAG
    - 벡터 DB
    - Semantic Model
    - 지식 그래프
    - Enterprise Graph
    section: '#### 3. RAG / 지식 관리 계층'
  - id: ui
    match_keywords:
    - 에이전트 UI
    - Generative UI
    - 에이전트 빌더
    - Glass Box
    section: '#### 4. UI 컴포넌트 계층'
  - id: evaluation
    match_keywords:
    - 에이전트 평가
    - Agent Evaluation
    - MLflow
    - 모니터링
    section: '#### 5. 평가/모니터링 도구 계층'
  - id: security
    match_keywords:
    - 보안
    - 가드레일
    - Lakeguard
    - SecureXper
    - 샌드박스
    section: '#### 6. 보안/가드레일 계층'
---

# Build vs Buy 의사결정 프레임워크

## TL;DR

- AI 에이전트 제품의 기술 스택은 6개 핵심 계층(LLM, 에이전트 프레임워크, RAG, UI 컴포넌트, 평가 도구, 보안/가드레일)으로 구성되며, 각 계층별로 Build vs Buy 의사결정이 독립적으로 필요하다.
- 15개 경쟁 제품 분석 결과, **LLM은 API 활용(Buy)이 압도적 다수**이며 자체 LLM을 핵심 경쟁력으로 보유한 벤더는 OpenAI와 Anthropic, Google 3사에 불과하다.[^1] [^2] [^3] 엔터프라이즈 벤더(Salesforce, SAP, ServiceNow)는 멀티 LLM 전략을 채택한다.[^4] [^6] [^7]
- **에이전트 프레임워크와 오케스트레이션은 대부분 자체 구축(Build)**하며, 이는 제품 차별화의 핵심 계층이다.[^4] [^7] [^8] 반면 RAG, 벡터 DB, 평가 도구는 오픈소스 또는 서드파티 도구를 적극 활용한다.
- 최적 전략은 **"Core Build + Edge Buy"** 모델로, 차별화 핵심(에이전트 오케스트레이션, 도메인 로직, UI/UX)은 자체 구축하고, 범용 인프라(LLM, 벡터 DB, 모니터링)는 외부 서비스를 활용하는 것이다.

---

## Overview

AI 에이전트 제품을 개발하는 모든 기업은 기술 스택의 각 계층에서 "직접 만들 것인가(Build) vs 외부 것을 사용할 것인가(Buy)"라는 근본적 의사결정에 직면한다. 이 결정은 단순히 기술적 역량의 문제가 아니라, **전략적 차별화**, **시장 진입 속도**, **장기 유지보수 비용**, **벤더 종속 리스크**가 복합적으로 작용하는 경영 의사결정이다.

2026년 현재 AI 에이전트 시장은 급속도로 성숙하고 있으며, 기술 구성 요소의 상품화(commoditization)가 빠르게 진행되고 있다. LLM API는 이미 완전한 상품이 되었고, RAG 파이프라인과 벡터 DB도 표준화가 진행 중이다. 반면 에이전트 오케스트레이션, 도메인 특화 로직, 사용자 경험(UX)은 여전히 차별화의 핵심 영역으로 남아 있다.

---

## Cross-Product Analysis

### Build vs Buy 결정 매트릭스

| 기술 계층           | Build (자체 구축)                                                                        | Buy/Adopt (외부 활용)                    | 하이브리드                                  | Source                                                    |
| --------------- | ------------------------------------------------------------------------------------ | ------------------------------------ | -------------------------------------- | --------------------------------------------------------- |
| **LLM (기반 모델)** | OpenAI, Anthropic, Google                                                            | SAP Joule, Workday, Glean, Vercel v0 | Salesforce, ServiceNow, 삼성SDS, LG CNS  | [^1] [^2] [^3] [^6] [^8] [^9] [^11] [^4] [^7] [^13] [^14] |
| **에이전트 프레임워크**  | Salesforce (Atlas), ServiceNow (Orchestrator), Workday (ASOR), Manus (Planner Agent) | -                                    | Databricks (LangChain 호환 자체 프레임워크)     | [^4] [^7] [^8] [^12] [^10]                                |
| **RAG 파이프라인**   | Snowflake (Cortex Search), Glean (Enterprise Graph)                                  | Vercel v0 (자체 RAG 레이어)               | Databricks (Vector Search + 오픈소스)      | [^9] [^11] [^15] [^10]                                    |
| **UI 컴포넌트**     | Salesforce (3-Panel), Manus (Glass Box), Google (Dynamic View)                       | -                                    | Vercel v0 (shadcn/ui 기반 생성)            | [^4] [^12] [^3] [^15]                                     |
| **평가/모니터링 도구**  | Databricks (Agent Evaluation), Salesforce (Testing Center)                           | 대부분의 벤더 (자체 기본 도구만)                  | -                                      | [^10] [^4]                                                |
| **보안/가드레일**     | ServiceNow, Salesforce, Databricks (Lakeguard)                                       | Glean (원본 권한 상속)                     | LG CNS (SecureXper AI), 삼성SDS (SCP 보안) | [^7] [^4] [^10] [^11] [^14] [^13]                         |

### 계층별 Build vs Buy 패턴 분석

<!-- auto-update-zone: llm -->
#### 1. LLM (기반 모델) 계층

**패턴**: 압도적 Buy 우세

15개 제품 중 자체 LLM을 핵심 경쟁력으로 개발한 벤더는 [[openai/openai|OpenAI]] (GPT-5.2), [[claude/claude|Anthropic]] (Opus 4.6/Sonnet 5), [[google-gemini/google-gemini|Google]] (Gemini 3 Pro) 3사에 불과하다.[^1] [^2] [^3] 나머지 12개 제품은 모두 외부 LLM API를 활용하며, 멀티 LLM 전략이 주류이다.

| 전략 유형 | 벤더 | 상세 | Source |
|-----------|------|------|--------|
| 자체 LLM 전용 | OpenAI, Anthropic, Google | 자사 모델이 유일하거나 주력 | [^1] [^2] [^3] |
| 멀티 LLM (자사+외부) | Salesforce, ServiceNow, 삼성SDS | 자체 모델 + GPT/Claude 등 혼용 | [^4] [^7] [^13] |
| 순수 외부 LLM | SAP, Workday, Glean, Snowflake, Databricks, Vercel, Manus | 외부 모델만 사용, 멀티 모델 오케스트레이션 | [^6] [^8] [^11] [^9] [^10] [^15] [^12] |
| 한국 특수 | 삼성SDS, LG CNS | 삼성 자체 LLM/엑사원 + GPT-4o + 코히어 | [^13] [^14] |

**시사점**: LLM 자체 개발은 수십억 달러 규모의 투자가 필요하다. 멀티 LLM API 전략이 최적이며, [[sap-joule/sap-joule|SAP Joule]]의 AI Core 모델이나 [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks]]의 Model Serving처럼 모델 교체가 용이한 추상화 계층 설계가 핵심이다.[^6] [^10]

<!-- auto-update-zone: agent-framework -->
#### 2. 에이전트 프레임워크/오케스트레이션 계층

**패턴**: 압도적 Build 우세

거의 모든 제품이 에이전트 오케스트레이션을 자체 구축했다. 이는 이 계층이 **제품 정체성과 차별화의 핵심**이기 때문이다.

| 제품 | 자체 프레임워크 | 핵심 차별점 | Source |
|------|---------------|-----------|--------|
| [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | Atlas Reasoning Engine | 숙고형 추론(Plan-Act-Observe 루프) | [^4] |
| [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | Copilot Orchestrator | 멀티 에이전트 오케스트레이션 | [^5] |
| [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | Skills-Agents-Orchestrator 3계층 | 체계적 거버넌스 내장 | [^7] |
| [[workday-assistant/workday-assistant\|Workday Assistant]] | ASOR (Agent System of Record) | 에이전트를 디지털 직원으로 관리 | [^8] |
| [[sap-joule/sap-joule\|SAP Joule]] | Agentic Orchestration | Role-Based AI 어시스턴트 | [^6] |
| [[manus-ai/manus-ai\|Manus AI]] | Planner Agent + 멀티 에이전트 | 중앙 Planner가 서브태스크 분배 | [^12] |
| [[glean/glean\|Glean]] | Agentic Engine 2 | 적응형 계획 + 서브 에이전트 병렬 조율 | [^11] |

**주목할 예외**: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]]는 자체 Agent Framework를 제공하면서도 LangChain/LangGraph와의 호환성을 보장하는 **하이브리드 접근**을 취한다.[^10]

**시사점**: 에이전트 오케스트레이션은 반드시 자체 구축해야 하며, 핵심 기술 투자 영역이다. 단, Databricks처럼 LangChain/LangGraph 등 인기 프레임워크와의 호환성을 유지하면 개발자 채택을 가속할 수 있다.

<!-- auto-update-zone: rag -->
#### 3. RAG / 지식 관리 계층

**패턴**: 하이브리드 우세

| 접근법 | 벤더 | 상세 | Source |
|--------|------|------|--------|
| 완전 자체 구축 | Salesforce (Data Cloud + Zero-Copy), Glean (Enterprise Graph), Snowflake (Cortex Search + Semantic Model) | 데이터 플랫폼 자체가 핵심 자산 | [^4] [^11] [^9] |
| 프레임워크 활용 + 자사 데이터 레이어 | Databricks (Vector Search + Unity Catalog) | 오픈소스 기반 + 거버넌스 자체 구축 | [^10] |
| 외부 활용 | Vercel v0 (RAG 레이어로 문서 검색), Manus (브라우저 자동화로 대체) | RAG 자체보다 활용 방식에 집중 | [^15] [^12] |

**시사점**: RAG 파이프라인의 기본 인프라(벡터 DB, 임베딩 모델)는 상품화가 진행 중이므로 Buy 가능하다. 그러나 Semantic Model([[snowflake-intelligence/snowflake-intelligence|Snowflake]])이나 Enterprise Graph([[glean/glean|Glean]])처럼 **비즈니스 컨텍스트를 모델링하는 계층**은 차별화 요소이므로 자체 구축이 필요하다.[^9] [^11]

<!-- auto-update-zone: ui -->
#### 4. UI 컴포넌트 계층

**패턴**: 전원 Build

모든 제품이 UI/UX를 자체 설계했다. 이는 사용자 경험이 제품 경쟁력의 직접적 요소이기 때문이다. 특히 주목할 UI 혁신 패턴:

- **Two-Pane / Glass Box**: [[manus-ai/manus-ai|Manus AI]]의 실시간 작업 관찰 패널[^12]
- **3-Panel Layout**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]의 에이전트 빌더[^4]
- **Sidecar 패턴**: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]]의 사이드 패널[^5] [^7]
- **Dynamic View (Generative UI)**: [[google-gemini/google-gemini|Google Gemini]]의 프롬프트 기반 동적 UI 생성[^3]
- **Chat + Artifacts**: [[claude/claude|Claude]], [[openai/openai|OpenAI]]의 대화 + 산출물 이중 패널[^2] [^1]

**시사점**: UI/UX는 100% 자체 구축이 필수이며, shadcn/ui 같은 오픈소스 컴포넌트 라이브러리를 기반으로 하되 에이전트 특화 UX 패턴(투명성, Human-in-the-Loop, 진행 상황 시각화)은 독자 설계해야 한다.

<!-- auto-update-zone: evaluation -->
#### 5. 평가/모니터링 도구 계층

**패턴**: 대부분 기본 수준, 선도 기업만 심화 Build

| 수준 | 벤더 | 상세 | Source |
|------|------|------|--------|
| 심화 자체 구축 | Databricks (Agent Evaluation + Review App + MLflow 3.0), Salesforce (Testing Center + Command Center) | 다차원 평가(AI Judge + 규칙 + 사람), 크로스 플랫폼 관측성 | [^10] [^4] |
| 중간 수준 | ServiceNow (Orchestrator 대시보드), Workday (Agent Registry 성과 추적) | 기본 모니터링 + 거버넌스 | [^7] [^8] |
| 기본 수준 | 대부분의 다른 벤더 | 사용량 통계, 기본 로그 | -- |

**시사점**: 에이전트 평가/모니터링은 현재 차별화 기회가 큰 영역이다. [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks]]의 Agent Evaluation처럼 AI Judge + 사람 피드백 + 규칙 기반 검사를 결합한 체계적 평가 프레임워크는 엔터프라이즈 고객의 핵심 요구사항이다.[^10]

<!-- auto-update-zone: security -->
#### 6. 보안/가드레일 계층

**패턴**: 핵심 보안은 Build, 인프라 보안은 Buy

| 접근법 | 벤더 | 상세 | Source |
|--------|------|------|--------|
| 에이전트 레벨 보안 자체 구축 | LG CNS (SecureXper AI), Databricks (Lakeguard), Salesforce (Agentforce Gateway) | 에이전트-시스템 연결점, 코드 실행 샌드박스 | [^14] [^10] [^4] |
| 인프라 레벨 보안 | 삼성SDS (SCP), ServiceNow (Now Platform) | 클라우드 인프라 보안 | [^13] [^7] |
| 권한 상속 모델 | Glean, Workday (ASOR RBAC) | 원본 시스템 권한 그대로 활용 | [^11] [^8] |

**시사점**: 에이전틱 AI 시대에는 에이전트 행동의 안전성 보장이 핵심이다. [[lgcns-agenticworks/lgcns-agenticworks|LG CNS]]의 SecureXper AI(에이전트-시스템 연결점 보안)와 [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks]]의 Lakeguard(샌드박스 코드 실행)가 보여주는 **에이전트 레벨 보안**은 자체 구축이 필수이다.[^14] [^10]

---

<!-- auto-update-zone: key-findings -->
## Key Findings

### 1. LLM 계층의 완전한 상품화와 "추상화 계층" 전쟁

15개 제품 중 12개가 외부 LLM API를 사용하며, 자체 LLM 개발은 OpenAI/Anthropic/Google 3사의 영역으로 고착되었다. 주목할 점은 LLM 자체가 아니라 **LLM 위의 추상화 계층**(모델 선택, 라우팅, 비용 최적화)이 새로운 경쟁 영역으로 부상하고 있다는 것이다.[^14] [^6] [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]]의 Router 모듈(요청에 최적인 AI 모델 자동 선택)과 [[sap-joule/sap-joule|SAP Joule]]의 SAP AI Core(멀티 LLM 관리 런타임)가 이 패턴을 선도한다.

### 2. "에이전트 오케스트레이션"이 새로운 OS 계층

모든 성공적인 AI 에이전트 제품이 에이전트 오케스트레이션을 자체 구축한 것은, 이 계층이 운영체제(OS)와 유사한 플랫폼 레이어로 기능하기 때문이다.[^4] [^7] [^8] Salesforce의 Atlas Engine, ServiceNow의 Skills-Agents-Orchestrator 3계층, Workday의 ASOR은 각각 다른 철학을 가지지만, 공통적으로 **"사용자 의도 해석 -> 계획 수립 -> 도구 선택 -> 실행 -> 검증"**의 에이전틱 루프를 자체 구현한다.

### 3. Semantic Layer가 RAG의 차세대 전쟁터

단순 벡터 검색 기반 RAG는 이미 상품화되었으나, **비즈니스 의미론(Semantics)을 모델링하는 계층**에서 새로운 차별화가 발생하고 있다.[^9] [^11] [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]]의 YAML 기반 Semantic Model(비즈니스 용어와 DB 스키마 매핑)과 [[glean/glean|Glean]]의 Enterprise Graph(지식 그래프 + Personal Graph)는 단순 RAG를 넘어 비즈니스 컨텍스트를 구조화한다.

### 4. 평가 도구의 "자체 구축 프리미엄"

대부분의 벤더가 에이전트 평가를 기본 수준에서만 제공하는 반면, [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks]]는 Agent Evaluation(AI Judge + 규칙 기반 + 사람 피드백)을 심도 있게 자체 구축하여 엔터프라이즈 시장에서 차별화에 성공했다.[^10] Review App을 통한 도메인 전문가(SME) 피드백 수집, Golden Examples 정의, MLflow 3.0 크로스 플랫폼 관측성은 경쟁사에서 찾기 어려운 수준이다.

### 5. 한국 시장에서 "도메인 지식"은 Buy가 현실적

한국 세무(부가세 신고, 원천징수, e-Tax), K-IFRS, 4대 보험, 퇴직연금, 노동법 등의 도메인 특화 AI 에이전트는 수년간의 데이터 축적과 전문 지식이 필요하다. [[douzone-one-ai/douzone-one-ai|더존]]은 30년 이상의 한국 기업 ERP 경험을 기반으로 회계·세무·인사 특화 에이전트를 자체 개발한 유일한 사례이며[^19], 삼성SDS와 LG CNS조차 이 도메인에서는 더존 대비 약점을 보인다.[^13] [^14]

### 6. 프로토콜 지원은 Build가 아닌 "Adopt & Extend"

MCP(Anthropic 주도), A2A(Google 주도)는 이미 업계 표준으로 자리잡았다.[^8] [^9] [[workday-assistant/workday-assistant|Workday]]가 MCP+A2A를 네이티브 지원하고 50+ 파트너를 확보한 사례, [[snowflake-intelligence/snowflake-intelligence|Snowflake]]가 Managed MCP Server를 제공하는 사례가 보여주듯, 프로토콜 자체를 만드는 것이 아니라 **표준 프로토콜을 가장 빠르게 채택하고 자사 데이터에 최적화**하는 전략이 유효하다.

---

## Recent Updates

<!-- auto-append: 새로운 업데이트는 이 테이블 상단에 자동 추가됩니다 -->
<!-- affected_zone: update_zones.id 값 사용 (llm, agent-framework, rag, ui, evaluation, security) -->
<!-- review_trigger: threshold(3)개 이상 누적 시 또는 priority_override(high-importance) 시 본문 반영 트리거 -->

| Date | Source | Summary | Affected | Tags |
|------|--------|---------|----------|------|
| 2026-02-11 | [AI agents aren't eating SaaS — they're using it](https://fortune.com/2026/02/10/ai-agents-anthropic-openai-arent-killing-saas-salesforce-servicenow-microsoft-workday-cant-sleep-easy/) · [[2026/02/2026-02-11\|다이제스트]] | $2조 SaaS 시가총액 증발. 좌석→소비/에이전트 기반 과금 전환 가속 | — | #strategy |

---

## References

### Vault

[^1]: [[openai/openai|OpenAI]] -- GPT-5.2, Codex, Responses API
[^2]: [[claude/claude|Anthropic Claude]] -- MCP, Extended Thinking, Claude Code
[^3]: [[google-gemini/google-gemini|Google Gemini]] -- Gemini 3 Pro, Dynamic View, A2A/A2UI
[^4]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- Atlas Reasoning Engine, Agent Builder, Testing Center
[^5]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] -- Copilot Orchestrator, 멀티 에이전트 오케스트레이션
[^6]: [[sap-joule/sap-joule|SAP Joule]] -- SAP AI Core, 멀티 LLM, ABAP AI SDK
[^7]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- Skills-Agents-Orchestrator 3계층
[^8]: [[workday-assistant/workday-assistant|Workday Assistant]] -- ASOR, Agent Gateway, MCP+A2A
[^9]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- Semantic Model, Managed MCP Server
[^10]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- Agent Evaluation, Lakeguard, MLflow 3.0
[^11]: [[glean/glean|Glean]] -- Enterprise Graph, Agentic Engine 2
[^12]: [[manus-ai/manus-ai|Manus AI]] -- Planner Agent, Glass Box 투명성
[^13]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- AI 풀스택, MCP/A2A
[^14]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 6종 모듈, Router, SecureXper AI
[^15]: [[vercel-v0/vercel-v0|Vercel v0]] -- 복합 모델 아키텍처, RAG + AutoFix
[^19]: [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] -- 30년+ 한국 도메인 전문성, 회계·세무·인사 특화 에이전트

### External

[^16]: [Databricks Blog: Announcing Mosaic AI Agent Framework and Agent Evaluation](https://www.databricks.com/blog/announcing-mosaic-ai-agent-framework-and-agent-evaluation)
[^17]: [Snowflake Blog: Managed MCP Servers for Secure Data Agents](https://www.snowflake.com/en/blog/managed-mcp-servers-secure-data-agents/)
[^18]: [Workday Blog: Building Enterprise Intelligence -- A Guide to AI Agent Protocols](https://blog.workday.com/en-us/building-enterprise-intelligence-a-guide-to-ai-agent-protocols-for-multi-agent-systems.html)

---

*Last synthesized: 2026-02-11 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
