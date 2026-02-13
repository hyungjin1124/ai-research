---
type: insight-synthesis
topic_id: feature-gap-analysis
topic_name: 기능 격차 분석 & 우선순위 제안
category: strategy
tags:
- insight
- strategy
- feature-gap
- prioritization
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- openai
- claude
- google-gemini
- salesforce-agentforce
- microsoft-copilot
- sap-joule
- servicenow-now-assist
- workday-assistant
- oracle-digital-assistant
- snowflake-intelligence
- databricks-mosaic-ai
- thoughtspot-spotter
- glean
- vercel-v0
- manus-ai
- samsung-sds-fabrix
- lgcns-agenticworks
- douzone-one-ai
- younglimwon-ksystem
source_files:
- AI Agent Products/openai/openai.md
- AI Agent Products/claude/claude.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/oracle-digital-assistant/oracle-digital-assistant.md
- AI Agent Products/snowflake-intelligence/snowflake-intelligence.md
- AI Agent Products/databricks-mosaic-ai/databricks-mosaic-ai.md
- AI Agent Products/thoughtspot-spotter/thoughtspot-spotter.md
- AI Agent Products/glean/glean.md
- AI Agent Products/vercel-v0/vercel-v0.md
- AI Agent Products/manus-ai/manus-ai.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
- AI Agent Products/douzone-one-ai/douzone-one-ai.md
- AI Agent Products/younglimwon-ksystem/younglimwon-ksystem.md
relevant_roles:
- planning_agent
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI agent feature gap analysis
  - enterprise AI agent table stakes features
  - agent marketplace ASOR semantic layer
  - Korea ERP AI agent capability gap
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 기능 격차 분석 & 우선순위 제안

## TL;DR

- **6대 기능 카테고리 x 19개 제품 다차원 매트릭스 분석 결과**, Agent Core(오케스트레이션, 계획, 메모리), Data(RAG, 커넥터, 지식 그래프), UI(대화형, HITL, 대시보드), Platform(마켓플레이스, 노코드 빌더, API), Security(가드레일, 권한, 감사), Protocol(MCP, A2A)의 성숙도 격차가 세그먼트별로 극명하게 갈린다.
- **"Table Stakes" 기능 7가지 확인**: 자연어 대화 인터페이스, RAG 기반 응답, 노코드 에이전트 빌더, RBAC 권한 관리, Human-in-the-Loop 패턴, 소비 기반 가격 모델, MCP 프로토콜 지원 -- 이 7가지는 2026년 하반기까지 모든 주요 제품의 기본 요건이 된다.
- **차별화 기능 3가지**: (1) 에이전트 시스템 오브 레코드(ASOR, [[workday-assistant/workday-assistant|Workday]] 선도), (2) 에이전트 마켓플레이스([[douzone-one-ai/douzone-one-ai|더존 ONE AI]] 한국 최초, [[salesforce-agentforce/salesforce-agentforce|Salesforce]] AppExchange), (3) Semantic Layer 자동 생성([[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot]] SpotterModel).
- **Blue Ocean 기회 3가지**: (1) 한국 세법/노동법 특화 규정 에이전트 + MCP 프로토콜 브릿지, (2) 한국어 Semantic Model 자동 생성(한국 ERP 스키마), (3) 중소기업 대상 Agent Evaluation 경량화 프레임워크.

---

## Overview

[[competitive-landscape-executive-summary|경쟁 환경 Executive Summary]]가 전략적 포지셔닝을, [[product-roadmap-comparison|경쟁사 제품 로드맵 비교 분석]]이 시간축 진화를 다루었다면, 이 문서는 **기능 단위의 수평적 비교**를 통해 "무엇을 만들어야 하는가"에 직접 답한다. 6대 카테고리(Agent Core, Data, UI, Platform, Security, Protocol)에서 19개 제품을 평가하고, Table Stakes(필수)/Differentiator(차별화)/Blue Ocean(미개척)으로 분류한다.

---

## Cross-Product Analysis

### 1. Agent Core: 오케스트레이션 / 계획 / 메모리

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **멀티 에이전트 오케스트레이션** | [[claude/claude\|Claude]] Cowork(팀), [[openai/openai\|OpenAI]] 미지원, [[google-gemini/google-gemini\|Gemini]] Mariner 10병렬 | [[microsoft-copilot/microsoft-copilot\|MS Copilot]] GA, [[servicenow-now-assist/servicenow-now-assist\|ServiceNow]] Orchestrator, [[sap-joule/sap-joule\|SAP]] Collaborative Agents | [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks]] LangGraph 연동, [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot]] 4 에이전트 팀 | [[samsung-sds-fabrix/samsung-sds-fabrix\|삼성SDS]] MCP/A2A 기반, [[lgcns-agenticworks/lgcns-agenticworks\|LG CNS]] 멀티에이전트 협업 | [^2] [^8] [^10] [^9] [^14] [^15] [^4] [^6] |
| **자율 계획 수립 (Planning)** | Atlas(Salesforce), Extended Thinking(Claude), CUA 루프(OpenAI) | [[workday-assistant/workday-assistant\|Workday]] Agent Gateway, SAP Agentic Orchestration | [[snowflake-intelligence/snowflake-intelligence\|Snowflake]] Cortex Agent 에이전틱 루프 | [[douzone-one-ai/douzone-one-ai\|더존]] 4단계 에이전트 모델 | [^7] [^2] [^1] [^11] [^9] [^13] [^5] |
| **지속 메모리 (Persistent Memory)** | OpenAI Memory(대화 간), Claude Memory, Gemini 대화 기억 | Salesforce Data Cloud 고객 프로필, Workday Agent Registry 상태 추적 | 미성숙 (세션 기반) | 미확인 [출처 필요] | [^1] [^2] [^3] [^7] [^11] |
| **추론 엔진** | Claude Extended Thinking, OpenAI o3/o4-mini, Gemini Deep Think | Salesforce Atlas, SAP Knowledge Graph + RAGe | Snowflake Cortex AI, Databricks 멀티 LLM | 삼성SDS 멀티 LLM, LG CNS 코히어+엑사원 | [^2] [^1] [^3] [^7] [^9] [^13] [^14] [^4] [^6] |

**핵심 격차**: 멀티 에이전트 오케스트레이션은 Enterprise SaaS(MS Copilot GA, ServiceNow 3계층, SAP Collaborative Agents)에서 가장 성숙. 지속 메모리는 B2C(OpenAI, Claude)에서만 본격 구현되어 Enterprise에서 구조적 공백. 한국은 삼성SDS/LG CNS만 멀티에이전트 지원, 더존/영림원은 단일 에이전트 수준.

### 2. Data: RAG / 커넥터 / 지식 그래프 / Semantic Layer

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **RAG 아키텍처** | 모든 제품 기본 지원 | Salesforce Data Cloud Vector DB, SAP Knowledge Graph, ServiceNow Genius Results | Snowflake Cortex Search, Databricks Vector Search | 삼성SDS 기업 내부 RAG, LG CNS Knowledge Lake | [^7] [^9] [^10] [^13] [^14] [^4] [^6] |
| **커넥터 수** | MCP 기반 무제한 확장 | MS 1,000+, Salesforce MuleSoft, SAP BTP | Snowflake Zero-Copy, Databricks Unity Catalog | 삼성SDS 멀티클라우드, 더존 WEHAGO 내부 한정 | [^8] [^7] [^9] [^13] [^14] [^4] [^5] |
| **지식 그래프** | [[glean/glean\|Glean]] Enterprise Graph(100+ 앱) | Salesforce Data 360, SAP Knowledge Graph, Workday Data Cloud | 미성숙 | 미확인 [출처 필요] | [^16] [^7] [^9] [^11] |
| **Semantic Layer** | N/A | 제한적 | [[snowflake-intelligence/snowflake-intelligence\|Snowflake]] Semantic View(YAML), [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot]] SpotterModel(자동 생성) | 미존재 | [^13] [^15] |
| **한국 ERP 데이터 접근** | 직접 접근 불가 | SAP S/4HANA(대기업 한정) | 데이터 마이그레이션 필요 | **더존 위하고 5,800+ 기업, 영림원 K-System 제조기업** | [^5] [^19] [^9] |

**핵심 격차**: Semantic Layer는 Snowflake(YAML 수동 정의, 정확도)와 ThoughtSpot(SpotterModel AI 자동 생성, 속도)이 대조적 접근.[^13] [^15] 커넥터에서 Glean 100+, MS 1,000+가 압도적이나, MCP 채택이 커넥터 수 우위를 평준화할 기회. 한국 ERP 데이터는 더존/영림원만 네이티브 보유하나 MCP 서버 부재로 외부 접근 불가 -- 핵심 기회.[^5] [^19]

### 3. UI: 대화형 / HITL / 대시보드 / Generative UI

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **대화형 인터페이스** | 모든 제품 기본 | 모든 제품 기본 | 모든 제품 기본 | 모든 제품 기본 | -- |
| **Human-in-the-Loop** | Claude pause&ask, OpenAI CUA 확인, Gemini 승인 | Salesforce Omni Supervisor, ServiceNow Chat Summarization, Workday Manager 검토 | Databricks SME Review App, ThoughtSpot Expert Labeling | 삼성SDS Brity Copilot 승인 | [^2] [^1] [^3] [^7] [^10] [^11] [^14] [^15] [^4] |
| **실시간 모니터링 대시보드** | 제한적 | Salesforce Command Center, ServiceNow Orchestrator Dashboard, Workday Agent Registry | Databricks MLflow 3.0, Snowflake 비용 모니터링 | 제한적 [출처 필요] | [^7] [^10] [^11] [^14] [^13] |
| **Generative UI** | [[google-gemini/google-gemini\|Gemini]] Dynamic View, [[vercel-v0/vercel-v0\|Vercel v0]] 코드 생성 | SAP Fiori 컴플라이언트 렌더링 | ThoughtSpot SpotterViz 자동 시각화 | 미존재 | [^3] [^17] [^9] [^15] |
| **음성 에이전트** | OpenAI gpt-realtime(S2S), Gemini Live | ServiceNow AI Voice Agents (2025) | 미지원 | 삼성SDS Brity Meeting 95% 음성인식, LG CNS 데일리 브리핑 | [^1] [^10] [^4] [^6] |
| **추론 과정 투명화** | Claude Extended Thinking 시각화, OpenAI Thinking 블록 | Salesforce Atlas Step-by-Step, MS Multi-Agent 경로 시각화 | Snowflake Cortex Agent 단계 표시, Databricks 트레이스 디버깅 | 삼성SDS Glass Box 부분 지원 | [^2] [^1] [^7] [^8] [^13] [^14] [^4] |

**핵심 격차**: Generative UI는 Gemini Dynamic View와 Vercel v0가 선도, Enterprise는 SAP Fiori만 부분 지원. 음성 에이전트는 OpenAI gpt-realtime이 프로덕션 선도, ServiceNow Enterprise ITSM 음성 2025 출시. 에이전트 모니터링 대시보드는 Enterprise SaaS(Salesforce Command Center, ServiceNow Orchestrator, Workday Registry)에서 가장 성숙.

### 4. Platform: 마켓플레이스 / 노코드 빌더 / API / 개발자 도구

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **에이전트 마켓플레이스** | OpenAI GPT Store, Claude Projects(개인 수준) | Salesforce AppExchange, SAP Store, ServiceNow Store, Workday Marketplace | 미존재 | **더존 AI 에이전트 마켓플레이스(한국 최초)** | [^1] [^2] [^7] [^9] [^10] [^11] [^5] |
| **노코드 에이전트 빌더** | OpenAI GPT Builder, Gemini Gems | Salesforce Agent Builder, MS Copilot Studio, SAP Joule Studio, ServiceNow AI Agent Studio, Workday Flowise | Databricks AI Playground | 더존 ONE AI 큐브, LG CNS Studio, 삼성SDS FabriX | [^1] [^3] [^7] [^8] [^9] [^10] [^11] [^14] [^5] [^6] [^4] |
| **프로코드 API/SDK** | OpenAI Responses API, Claude API/MCP SDK, Gemini API | Salesforce APEX/MuleSoft, MS Power Platform, SAP ABAP AI SDK | Databricks Python SDK, Snowflake REST API | LG CNS Builder(코딩 기반) | [^1] [^2] [^3] [^7] [^8] [^9] [^14] [^13] [^6] |
| **에이전트 테스트 도구** | Claude Code 내장, OpenAI Codex 샌드박스 | Salesforce Testing Center, ServiceNow Testing Center | **Databricks Agent Evaluation(AI Judge+규칙+사람 피드백)** | 미확인 [출처 필요] | [^2] [^1] [^7] [^10] [^14] |
| **에이전트 평가 프레임워크** | 기본 벤치마크(SWE-bench 등) | 제한적(Salesforce 시뮬레이션) | **Databricks Agent Evaluation(다차원), ThoughtSpot 피드백 루프** | 미존재 | [^14] [^15] [^7] |

**핵심 격차**: 노코드 빌더는 Table Stakes화(19개 중 16개 보유), 차별화는 사용성과 확장성으로 이동. Agent Evaluation은 Databricks만 체계적 프레임워크 보유(AI Judge+규칙+사람), 모든 Enterprise에 필수이나 공급 극히 부족.[^14] 에이전트 마켓플레이스는 한국에서 더존만 구축(WEHAGO 한정), 개방형 마켓플레이스는 Blue Ocean.[^5]

### 5. Security: 가드레일 / 권한 관리 / 감사 / 샌드박스

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **LLM 가드레일** | Claude Constitutional AI, OpenAI Safety, Gemini 안전장치 | Salesforce Guardrails(토픽 범위), ServiceNow 정책 평가, Workday ASOR 역할 정의 | Databricks LLM Guardrails | 삼성SDS 보안 필터 | [^2] [^1] [^3] [^7] [^10] [^11] [^14] [^4] |
| **RBAC 권한 관리** | 기본 API 키 기반 | Salesforce ABAC(속성 기반), ServiceNow RBAC, Workday RBAC+국가별 | Snowflake 행/열 RBAC, Databricks Unity Catalog ACL | 삼성SDS 기업 보안, 더존 WEHAGO 권한 | [^7] [^10] [^11] [^13] [^14] [^4] [^5] |
| **감사 로깅** | 제한적 | Salesforce Command Center, ServiceNow Orchestrator 감사, Workday Agent 실행 로그 | Databricks MLflow 트레이스, Snowflake 쿼리 로그 | 미확인 [출처 필요] | [^7] [^10] [^11] [^14] [^13] |
| **에이전트 샌드박스** | Claude Cowork VM 격리, OpenAI Codex 클라우드 샌드박스 | Salesforce Agentforce Gateway(Envoy 기반) | **Databricks Lakeguard** | 더존 ONE AI PE(폐쇄망) | [^2] [^1] [^7] [^14] [^5] |
| **ASOR(Agent System of Record)** | 미존재 | **Workday ASOR(업계 최초)** | 미존재 | 미존재 | [^11] |
| **폐쇄망/온프레미스** | Claude 없음, OpenAI 없음 | SAP Private Cloud, Oracle 온프레미스 | Databricks 온프레미스 가능 | **더존 ONE AI PE(LG 엑사원 기반), 영림원 온프레미스** | [^9] [^12] [^14] [^5] [^19] |

**핵심 격차**: ASOR는 Workday 업계 최초 도입, 에이전트 수 증가 시 필수 -- 2026~2027년 경쟁사 유사 기능 도입 예상.[^11] 에이전트 샌드박스는 Databricks Lakeguard, Claude VM 격리, OpenAI Codex 샌드박스가 대표.[^14] [^2] [^1] 한국 공공/금융 시장은 폐쇄망 필수이며 더존 ONE AI PE가 유일하게 충족.[^5]

### 6. Protocol: MCP / A2A / A2UI

| 기능 | 글로벌 AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------------|-----------------|--------------|-------------|--------|
| **MCP 지원** | **Claude(창안)**, OpenAI(채택), Gemini(채택) | Salesforce(3.0), MS Copilot Studio(네이티브), Workday Agent Gateway | **Snowflake Managed MCP Server**, Glean MCP 호스팅 | **삼성SDS, LG CNS** 지원 / 더존, 영림원 **미확인** | [^2] [^1] [^3] [^7] [^8] [^11] [^13] [^16] [^4] [^6] |
| **A2A 지원** | Gemini(주도) | Workday Agent Gateway, SAP Joule | 미지원 | 삼성SDS, LG CNS 지원 | [^3] [^11] [^9] [^4] [^6] |
| **A2UI 지원** | **Gemini(주도)** | 미지원 | 미지원 | 미지원 | [^3] |
| **독자 프로토콜** | OpenAI Function Calling | Salesforce MuleSoft API Fabric, ServiceNow REST API + 전용 커넥터, Oracle Visual Flow Designer | Databricks Unity Catalog 함수 | 더존 자체 API, 영림원 내부 연동 | [^1] [^7] [^10] [^12] [^14] [^5] [^19] |

**핵심 격차**: MCP는 2026년 사실상 업계 표준(AAIF 기증으로 거버넌스 중립화). 한국 시장 프로토콜 격차가 가장 심각 -- 삼성SDS/LG CNS는 MCP/A2A 지원하나 더존/영림원 미확인으로, 한국 중소기업 ERP 데이터의 외부 AI 에이전트 접근이 구조적으로 차단.[^4] [^6] [^5] [^19] A2A는 Google 주도로 MCP 대비 채택 느림, A2UI는 초기 단계.

---

## Key Findings

### Finding 1: Table Stakes 기능 7가지 -- "없으면 경쟁 탈락"

2026년 하반기 기준으로, 다음 7가지 기능은 모든 엔터프라이즈 AI 에이전트 제품의 기본 요건이 된다:

| # | Table Stakes 기능 | 보유 제품 수 (19개 중) | 미보유 시 결과 |
|---|------------------|---------------------|-------------|
| 1 | 자연어 대화 인터페이스 | 19/19 (100%) | 제품 자격 미달 |
| 2 | RAG 기반 문맥 응답 | 17/19 (89%) | 정확도 신뢰 불가 |
| 3 | 노코드 에이전트 빌더 | 16/19 (84%) | 도입 장벽 과다 |
| 4 | RBAC 권한 관리 | 15/19 (79%) | 엔터프라이즈 계약 불가 |
| 5 | Human-in-the-Loop 패턴 | 15/19 (79%) | 자동화 신뢰 부족 |
| 6 | 소비 기반 가격 모델 | 14/19 (74%) | 도입 저항 증가 |
| 7 | MCP 프로토콜 지원 | 12/19 (63%) → 예상 16/19 (84%) by 2026 H2 | 에이전트 상호운용 불가 |

### Finding 2: 차별화 기능의 세그먼트별 분포

세그먼트별로 차별화 기능의 분포가 상이하며, 경쟁 우위를 확보하기 위해서는 세그먼트 교차 기능 조합이 필요하다:

| 차별화 기능 | 선도 제품 | 세그먼트 | 관련성 |
|------------|---------|---------|--------|
| ASOR(에이전트 시스템 오브 레코드) | Workday | Enterprise SaaS | ★★★ 높음 -- 에이전트 관리의 표준이 될 가능성[^11] |
| 에이전트 마켓플레이스 | Salesforce, 더존 | Enterprise SaaS, Korea | ★★★ 높음 -- 생태계 lock-in 핵심[^7] [^5] |
| Semantic Layer 자동 생성 | ThoughtSpot SpotterModel | Data Platform | ★★★ 높음 -- ERP NL-to-SQL 핵심[^15] |
| Agent Evaluation 프레임워크 | Databricks | Data Platform | ★★☆ 중간 -- 품질 보증에 필수적[^14] |
| Generative UI | Google Gemini, Vercel v0 | AI-Native | ★★☆ 중간 -- UX 차별화 가능[^3] [^17] |
| 멀티 에이전트 오케스트레이션 | MS Copilot, ServiceNow | Enterprise SaaS | ★★☆ 중간 -- Phase 3 목표[^8] [^10] |
| Enterprise Graph | Glean | Knowledge | ★☆☆ 낮음 -- 초기 단계에서 불필요[^16] |
| 음성 에이전트(S2S) | OpenAI gpt-realtime | AI-Native | ★☆☆ 낮음 -- 장기 과제[^1] |

### Finding 3: Blue Ocean 기회 -- 아무도 하지 않는 것

19개 제품 분석에서 식별된 명확한 공백 3가지:

**Blue Ocean 1: 한국 규정 특화 에이전트 + MCP 브릿지** -- 한국 세법/K-IFRS/4대 보험/노동법 에이전트는 더존만 부분 제공(WEHAGO 종속, MCP 미지원).[^5] MCP 서버로 구현 시 Claude/ChatGPT/Gemini 등 모든 AI-Native에서 호출 가능한 유일한 브릿지.

**Blue Ocean 2: 한국어 Semantic Model 자동 생성** -- Snowflake YAML은 수동, ThoughtSpot SpotterModel은 영문 중심.[^13] [^15] 한국 ERP의 한국어 테이블/컬럼/비즈니스 용어를 자동 Semantic Model화하는 도구 전무. NL-to-SQL 접근성 혁신 기회.

**Blue Ocean 3: 중소기업 Agent Evaluation 경량화** -- Databricks의 고급 프레임워크는 ML 엔지니어 대상.[^14] 비기술 사용자가 에이전트 정확도/비용/응답시간을 간편하게 모니터링하는 경량 대시보드 부재.

### Finding 4: 기능 성숙도 히트맵 -- 세그먼트 x 카테고리

| 카테고리 | AI-Native | Enterprise SaaS | Data Platform | Korea (대기업IT) | Korea (ERP네이티브) |
|---------|----------|-----------------|--------------|-----------------|-------------------|
| Agent Core | ★★★★ | ★★★★★ | ★★★ | ★★★ | ★★ |
| Data | ★★★ | ★★★★ | ★★★★★ | ★★★ | ★★★★ (자사 ERP) |
| UI | ★★★★★ | ★★★★ | ★★★ | ★★★ | ★★ |
| Platform | ★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★ |
| Security | ★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★ (PE 제외) |
| Protocol | ★★★★★ | ★★★★ | ★★★ | ★★★★ | ★ |

(★ = 초기, ★★★★★ = 완전 성숙)

한국 ERP 네이티브 벤더(더존, 영림원)는 자사 ERP 데이터 접근에서 ★★★★이나, 프로토콜(★), 플랫폼(★★), 보안 거버넌스(★★)에서 글로벌 대비 2~3단계 격차가 존재한다.[^5] [^19] 이 비대칭 격차가 핵심 기회이다.

### Finding 5: 가격 모델 시사점

시장 가격 모델은 6가지로 분류된다: 대화당 과금(Salesforce $2), 사용자당 번들(MS $30/월, ThoughtSpot $25~50/월), 소비 기반 크레딧(Snowflake, Databricks, SAP AI Unit), Assist 토큰(ServiceNow), 모듈별 구독(더존, 영림원), 비공개 협의(Workday, 삼성SDS).[^7] [^8] [^15] [^13] [^14] [^9] [^10] [^5] [^19] [^11] [^4]

### Finding 6: 기능 구현 난이도 vs 경쟁 영향도

19개 제품의 기능을 구현 난이도(기술 복잡성 + 데이터 요구 + 시간)와 경쟁 영향도(시장 차별화 + 고객 가치)로 평가하면:

| 사분면 | 기능 | 전략 |
|--------|------|------|
| **Quick Wins** (낮은 난이도, 높은 영향도) | MCP 서버 구축, 자연어 대화 UI, 노코드 빌더 기초, RBAC | **즉시 구현** |
| **Strategic Bets** (높은 난이도, 높은 영향도) | 한국 ERP Semantic Layer, 에이전트 마켓플레이스, ASOR 경량 버전 | **Phase 2 핵심 투자** |
| **Fill Gaps** (낮은 난이도, 낮은 영향도) | 기본 RAG, 소비 기반 과금, HITL 기본 패턴 | **기본 구현** |
| **Long-term** (높은 난이도, 낮은 즉시 영향도) | 멀티 에이전트 오케스트레이션, 음성 에이전트, Generative UI | **Phase 3 이후** |

---

## Recent Updates

<!-- auto-append: 새로운 업데이트는 이 테이블 하단에 자동 추가됩니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-11 | [AI agents aren't eating SaaS — they're using it](https://fortune.com/2026/02/10/ai-agents-anthropic-openai-arent-killing-saas-salesforce-servicenow-microsoft-workday-cant-sleep-easy/) · [[2026/02/2026-02-11\|다이제스트]] | $2조 SaaS 시가총액 증발. 좌석 기반 과금 → 소비/에이전트 모델 전환 가속 | #strategy |

---

## References

### Vault

[^1]: [[openai/openai|OpenAI]] -- GPT-5.2, ChatGPT Agent, Codex, GPT Store
[^2]: [[claude/claude|Anthropic Claude]] -- MCP 창안, Claude Code, Cowork, Constitutional AI
[^3]: [[google-gemini/google-gemini|Google Gemini]] -- Gemini Dynamic View, A2A/A2UI, Project Mariner
[^4]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- AI 풀스택, MCP/A2A, 20만 사용자, Brity Copilot
[^5]: [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] -- ERP 네이티브, 에이전트 마켓플레이스, 5,800+ 기업, PE 폐쇄망
[^6]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 6종 모듈, 코히어 협력, SecureXper AI, Studio
[^7]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- Atlas Engine, Agent Builder, $2/대화, AppExchange
[^8]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] -- 멀티 에이전트 오케스트레이션, Copilot Studio, $30/월
[^9]: [[sap-joule/sap-joule|SAP Joule]] -- 2,400+ 스킬, Knowledge Graph, Joule Studio, AI Unit
[^10]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- 3계층 아키텍처, Orchestrator, Testing Center
[^11]: [[workday-assistant/workday-assistant|Workday Assistant]] -- ASOR(업계 최초), Agent Gateway, Marketplace, Flex Credits
[^12]: [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] -- Skills 기반, Visual Flow Designer, 온프레미스
[^13]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- Semantic View, Managed MCP Server, Cortex Agent
[^14]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- Agent Evaluation, Lakeguard, MLflow 3.0, Unity Catalog
[^15]: [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] -- SpotterModel, 4 에이전트 팀, SpotterViz
[^16]: [[glean/glean|Glean]] -- Enterprise Graph, 100+ 앱 커넥터, Agentic Engine 2
[^17]: [[vercel-v0/vercel-v0|Vercel v0]] -- AI 풀스택 빌더, 복합 모델 아키텍처
[^18]: [[manus-ai/manus-ai|Manus AI]] -- 범용 자율 에이전트, Glass Box, Meta 인수
[^19]: [[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]] -- 제조 특화, ERP+MES 통합, 온프레미스

### External

- 각 제품의 상세 기능은 해당 프로필 문서를 참조.

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
