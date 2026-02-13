---
type: insight-synthesis
topic_id: partnership-ecosystem-map
topic_name: AI 에이전트 파트너십·생태계 관계 맵
category: market
tags:
- insight
- market
- partnership
- ecosystem
- LLM
- protocol
status: draft
confidence: medium
last_updated: '2026-02-10'
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
- oracle-digital-assistant
- thoughtspot-spotter
- manus-ai
- vercel-v0
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
- AI Agent Products/oracle-digital-assistant/oracle-digital-assistant.md
- AI Agent Products/thoughtspot-spotter/thoughtspot-spotter.md
- AI Agent Products/manus-ai/manus-ai.md
- AI Agent Products/vercel-v0/vercel-v0.md
relevant_roles:
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI partnership
  - ecosystem
  - SI consulting
  - platform integration
  - strategic alliance
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 파트너십·생태계 관계 맵

## TL;DR

- AI 에이전트 생태계는 **LLM 공급(모델 제공)**, **플랫폼 통합(채널/데이터)**, **프로토콜 표준(MCP/A2A)**, **SI/컨설팅 파트너** 4개 차원의 파트너십으로 구성되며, 단일 벤더가 모든 차원을 자체 충당하는 경우는 없다.
- **LLM 공급 관계**에서 가장 강력한 축은 OpenAI-Microsoft(Azure OpenAI Service)이며, Anthropic Claude는 Salesforce(Amazon Bedrock 기반), ServiceNow, SAP AI Core를 통해 엔터프라이즈 벤더에 광범위하게 침투하고 있다. Google Gemini는 자사 Workspace/Cloud 생태계 내에서 수직 통합에 집중한다.
- **MCP 프로토콜**은 Anthropic이 창안하고 OpenAI(2025-03), Google(2025-04)이 채택하며 사실상 업계 표준으로 정착되었고, 2025-12 Linux Foundation 산하 AAIF에 기증되어 거버넌스가 중립화되었다. **A2A(Agent-to-Agent)**는 Google이 주도하며 Workday, SAP가 지원한다.
- **"경쟁적 공생(Co-opetition)"** 관계가 보편화되어 있다: SAP Joule은 Microsoft Copilot과 양방향 통합하면서도 AI Core에서 OpenAI, Claude, Gemini를 모두 사용하고, Salesforce Agentforce는 Anthropic Claude를 Amazon Bedrock에서 호스팅하면서 자체 Atlas 추론 엔진을 운영한다.
- 시장의 주요 플레이어들은 다양한 LLM 파트너십 전략을 구축하고 있으며, 이는 각 시장의 **LLM 선택지 다양화**를 야기한다.

---

## Context

AI 에이전트 시장에서 파트너십은 단순한 기술 제휴를 넘어, 제품의 역량 범위, 고객 접근 채널, 데이터 연결 깊이를 결정하는 전략적 요소이다. 특히 "누구의 LLM을 사용하는가"는 제품의 AI 성능 상한을 결정하고, "누구의 데이터/채널과 통합하는가"는 시장 도달 범위를 결정하며, "어떤 프로토콜을 지원하는가"는 생태계 참여 자격을 결정한다.

파트너십 전략 수립에 있어, 경쟁 제품들의 생태계 관계를 정밀하게 매핑하는 것은 기술적 의사결정(어떤 LLM을 사용할 것인가, 어떤 프로토콜을 지원할 것인가)과 사업적 의사결정(어떤 채널 파트너와 협력할 것인가)의 기반이 된다. 특히 지역 시장의 파트너십 지형은 글로벌 시장과 다른 독자적 구조를 형성하고 있어 별도의 분석이 필요하다.

---

## Cross-Product Analysis

### LLM 공급 관계 매트릭스

| 제품 | 주력 LLM | 서드파티 LLM 지원 | LLM 전략 |
|------|---------|----------------|---------|
| [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | 자체 xGen | Anthropic Claude(Bedrock), OpenAI | 멀티 LLM + 자체 Atlas 추론 엔진 |
| [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | Azure OpenAI(GPT 시리즈) | - | 단일 LLM 파트너(OpenAI) |
| [[openai/openai\|OpenAI]] | 자체 GPT-5.2, o3 시리즈 | - | 자체 모델 전용 |
| [[claude/claude\|Claude]] | 자체 Opus/Sonnet/Haiku | - | 자체 모델 전용 |
| [[google-gemini/google-gemini\|Google Gemini]] | 자체 Gemini 3 Pro, 2.5 Flash | - | 자체 모델 전용 |
| [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | 자체 도메인 모델 | Gemini, Azure OpenAI, Claude | 자체 모델 + 외부 LLM 범용 연결 |
| [[workday-assistant/workday-assistant\|Workday Assistant]] | 서드파티 의존 | 미공개 | 자체 LLM 미보유, Sana 인수로 내재화 중 |
| [[sap-joule/sap-joule\|SAP Joule]] | SAP AI Core 관리 | OpenAI, Google Gemini, Claude, Mistral | 멀티 LLM 허브(AI Core) |
| [[snowflake-intelligence/snowflake-intelligence\|Snowflake Intelligence]] | Cortex AI 관리 | OpenAI GPT-5.2, Claude, Llama | 멀티 LLM (Cortex AI) |
| [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks Mosaic AI]] | Mosaic AI Serving | Claude, GPT, Llama, DBRX | 멀티 LLM + 자체 DBRX |
| [[glean/glean\|Glean]] | 서드파티 의존 | GPT-4, Claude 등 | 자체 LLM 미보유 |
| [[oracle-digital-assistant/oracle-digital-assistant\|Oracle Digital Assistant]] | Oracle GenAI | Cohere, Meta Llama | 자체 GenAI + 서드파티 LLM Block |
| [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot Spotter]] | 서드파티 의존 | GPT, Gemini | Search Token + 외부 LLM 조합 |
| [[manus-ai/manus-ai\|Manus AI]] | 멀티모델 오케스트레이션 | 태스크별 최적 모델 자동 선택 | 특정 LLM 비종속, Meta 인수 후 Llama 통합 예상 |
| [[vercel-v0/vercel-v0\|Vercel v0]] | Anthropic Sonnet 기반 | - | 복합 모델(RAG + Base LLM + AutoFix) |

### 프로토콜 생태계 맵

| 제품 | MCP 지원 | A2A 지원 | 자체 프로토콜 | 프로토콜 역할 |
|------|---------|---------|------------|-----------|
| [[claude/claude\|Claude]] | **창안·주도** | - | - | MCP 프로토콜 설계자 |
| [[openai/openai\|OpenAI]] | O (2025-03 채택) | - | Function Calling | MCP 추종자 + 자체 프로토콜 병행 |
| [[google-gemini/google-gemini\|Google Gemini]] | O (2025-04 채택) | **A2A 주도** | A2UI (오픈 프로젝트) | MCP + A2A + A2UI 멀티 프로토콜 |
| [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | O (Copilot Studio 네이티브) | - | Power Platform 커넥터 | MCP 적극 채택 |
| [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | O (3.0부터) | - | MuleSoft API Fabric | MCP 후발 채택 + 자체 통합 |
| [[workday-assistant/workday-assistant\|Workday Assistant]] | O (Agent Gateway) | O (Agent Gateway) | - | MCP + A2A 네이티브 |
| [[sap-joule/sap-joule\|SAP Joule]] | - | O | SAP BTP Integration Suite | A2A 지원, MCP 미공식 |
| [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | - | - | REST API, 전용 커넥터 | 개방형 프로토콜 미채택 |
| [[snowflake-intelligence/snowflake-intelligence\|Snowflake Intelligence]] | O (Managed MCP Server) | - | REST API | MCP 적극 채택 |
| [[glean/glean\|Glean]] | O (호스팅 MCP 서버) | - | LangChain Agent Protocol | MCP + Agent Protocol 이중 지원 |
| [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks Mosaic AI]] | - | - | MLflow, LangChain 통합 | 개방형 프로토콜 미채택 |
| [[oracle-digital-assistant/oracle-digital-assistant\|Oracle Digital Assistant]] | - | - | Oracle Integration Cloud | 개방형 프로토콜 미채택 |
| [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot Spotter]] | O (2025-09) | - | REST API | MCP 후발 채택 |
| [[manus-ai/manus-ai\|Manus AI]] | 미공식 | - | 브라우저 자동화 중심 | 프로토콜보다 범용 웹 접근 |
| [[vercel-v0/vercel-v0\|Vercel v0]] | - | - | Vercel AI SDK | 자체 SDK 중심 |

### 패턴 분류

#### 패턴 A: LLM 수직 통합 (Vertical Integration)

**설명**: 자체 LLM을 보유하고, 이를 자사 제품 생태계에서 독점적으로 사용하는 모델. 모델 성능에 대한 완전한 통제권을 보유하지만, 생태계가 폐쇄적이다.

**예시 제품**: [[openai/openai|OpenAI]], [[claude/claude|Claude]], [[google-gemini/google-gemini|Google Gemini]]

**장점**:
- 모델 로드맵에 대한 완전한 통제 (성능 향상, 비용 최적화, 안전성 강화)
- 모델-제품 간 최적화로 최상의 사용자 경험 제공 가능
- 경쟁사에 모델 역량이 노출되지 않아 기술적 moat 확보

**단점**:
- 모델 개발에 대규모 R&D 투자 필요 (수억~수십억 달러)
- 특정 도메인에서 외부 특화 모델이 더 우수할 수 있음
- 고객의 모델 선택 자유도 제한으로 벤더 종속 우려 야기

#### 패턴 B: 멀티 LLM 허브 (Multi-LLM Hub)

**설명**: 자사 플랫폼에서 복수의 LLM을 통합 관리하고, 태스크/도메인에 따라 최적 모델을 선택적으로 활용하는 모델. 모델 유연성과 벤더 중립성을 강조한다.

**예시 제품**: [[sap-joule/sap-joule|SAP Joule]] (AI Core에서 OpenAI, Gemini, Claude, Mistral 지원), [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] (Cortex AI에서 GPT-5.2, Claude, Llama 지원), [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] (Claude, GPT, Llama, DBRX 지원), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] (자체 + Gemini, Azure OpenAI, Claude)

**장점**:
- 고객이 규제/비용/성능 요구에 맞는 모델을 선택 가능
- 특정 LLM 벤더의 가격/정책 변경에 대한 리스크 분산
- "베스트 오브 브리드" 접근으로 태스크별 최적 성능 달성

**단점**:
- 복수 모델 통합/관리의 기술적 복잡성
- 모델 간 일관성 유지와 품질 보증의 어려움
- 각 LLM 벤더와의 라이선스 협상 복잡성

#### 패턴 C: 전략적 단일 파트너십 (Strategic Single Partnership)

**설명**: 특정 LLM 벤더와 깊은 전략적 파트너십을 형성하여, 기술적·사업적 시너지를 극대화하는 모델.

**예시 제품**: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] (OpenAI 독점), [[vercel-v0/vercel-v0|Vercel v0]] (Anthropic Sonnet 기반), LG CNS AgenticWorks (Cohere 파트너십)

**장점**:
- 파트너와의 깊은 기술 협업으로 최적화된 통합
- 공동 마케팅, 공동 세일즈 등 사업적 시너지
- 명확한 기술 로드맵 정렬

**단점**:
- 파트너 종속 리스크 (모델 성능 정체, 가격 인상, 정책 변경)
- 경쟁사가 더 나은 모델을 출시해도 전환이 어려움
- 고객의 모델 선택 자유도 제한

#### 패턴 D: 프로토콜 기반 개방형 연결 (Protocol-Based Open Connectivity)

**설명**: MCP, A2A 등 표준 프로토콜을 채택하여 외부 에이전트/도구/데이터와 개방적으로 연결하는 모델. 자체 생태계의 폐쇄성을 극복하고, 멀티벤더 환경에서의 상호운용성을 확보한다.

**예시 제품**: [[workday-assistant/workday-assistant|Workday Assistant]] (MCP + A2A 네이티브), [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] (Managed MCP Server), [[glean/glean|Glean]] (호스팅 MCP 서버 + Agent Protocol)

**장점**:
- 이종 시스템 간 에이전트 상호운용성 확보
- 파트너 생태계 확장이 용이 (Workday: 50+ Agent Partner Network)
- 고객의 기존 AI 투자를 재활용 가능

**단점**:
- 프로토콜 표준의 성숙도와 안정성에 의존
- 개방형 연결에 따른 보안/거버넌스 복잡성 증가
- 프로토콜 미채택 벤더(ServiceNow, Oracle, Databricks)와의 연결 제한

---

## Key Findings

1. **Anthropic Claude가 엔터프라이즈 LLM 시장의 "스위스 군용 칼"로 부상**: Claude 모델은 Salesforce(Amazon Bedrock 기반), ServiceNow(외부 LLM), SAP(AI Core), Snowflake(Cortex AI), Databricks(Mosaic AI Serving)에서 모두 사용 가능하다. OpenAI GPT가 Microsoft 독점에 가까운 전략적 파트너십을 형성한 반면, Anthropic은 모든 엔터프라이즈 벤더에 개방적으로 모델을 공급하며, 특히 Salesforce의 주력 외부 LLM으로 선택된 것은 CRM 시장 전체에 대한 간접 침투를 의미한다. 동시에 Anthropic이 MCP 프로토콜을 창안하여 업계 표준화를 주도한 것은 "모델 + 프로토콜" 이중 전략으로 생태계 영향력을 극대화하는 사례이다. — *Source*: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[sap-joule/sap-joule|SAP Joule]], [[claude/claude|Claude]]

2. **SAP의 "멀티 LLM + Microsoft Copilot 양방향" 전략이 가장 복잡한 파트너십 매트릭스**: SAP Joule은 AI Core를 통해 OpenAI, Google Gemini, Claude, Mistral 등 프론티어 모델을 모두 지원하는 동시에, Microsoft Copilot과 양방향 통합을 구축하여 SAP Work Zone에서 Microsoft 365 도구에 접근하고, Microsoft 365에서 SAP 데이터에 접근할 수 있게 했다. 이는 "모델 레이어에서는 멀티벤더, 채널 레이어에서는 Microsoft 전략적 제휴"라는 복합적 파트너십 구조이며, 가장 많은 외부 접점을 가진 엔터프라이즈 AI 제품이다. — *Source*: [[sap-joule/sap-joule|SAP Joule]], [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

3. **MCP 프로토콜의 거버넌스 중립화(AAIF 기증)가 채택 가속화의 전환점**: MCP가 2025년 12월 Linux Foundation 산하 Agentic AI Foundation(AAIF)에 기증된 것은, Anthropic의 독자 표준이라는 우려를 해소하고 OpenAI, Google, Microsoft, Salesforce 등이 안심하고 채택할 수 있는 환경을 만들었다. 현재 MCP 지원 제품(Claude, OpenAI, Google, Microsoft Copilot, Salesforce, Workday, Snowflake, Glean, ThoughtSpot)과 미지원 제품(ServiceNow, Oracle, Databricks)의 분화가 뚜렷하며, MCP 미지원은 에이전트 상호운용성에서 불리한 포지션을 초래한다. — *Source*: [[claude/claude|Claude]], [[workday-assistant/workday-assistant|Workday Assistant]], [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]]

4. **Workday의 Agent Partner Network(50+ 파트너)가 엔터프라이즈 에이전트 생태계의 모델 케이스**: Workday는 Accenture, Adobe, AWS, Deloitte, Glean, Google Cloud, IBM, Microsoft, PwC 등 50개 이상 글로벌 파트너의 에이전트를 ASOR에 등록하고 Agent Gateway(MCP+A2A)를 통해 연결하는 개방형 생태계를 구축했다. 이는 단일 벤더 에이전트가 아닌 "멀티벤더 에이전트 오케스트레이션"의 가장 진전된 사례이며, Salesforce의 MuleSoft API 중심 연동이나 ServiceNow의 전용 커넥터 방식보다 개방적이다. — *Source*: [[workday-assistant/workday-assistant|Workday Assistant]]

5. **한국 AI 에이전트 시장의 LLM 생태계 분화**: 한국 시장에서는 삼성SDS가 OpenAI 공식 리셀러(GPT-4o + 자체 LLM + Upstage 협력), LG CNS가 Cohere 전략적 파트너(Cohere + LG 엑사원), 더존이 실용적 조합(GPT-4o + LG 엑사원)을 채택하여, 글로벌 시장의 LLM 경쟁이 한국 시장에서는 SI/ERP 벤더를 통해 간접적으로 진행되고 있다. 이는 한국 기업이 AI 에이전트를 도입할 때 "LLM 선택"이 아니라 "SI/ERP 벤더 선택"에 의해 LLM이 결정되는 구조를 만든다. — *Source*: 한국 ERP AI 생태계 분석 참조

6. **Meta-Manus AI 인수가 B2C 에이전트 생태계에 지각변동 예고**: Meta가 Manus AI를 약 $20억에 인수하면서, Manus의 멀티모델 오케스트레이션 아키텍처가 Meta의 Llama 모델 및 Meta AI 에코시스템과 통합될 전망이다. 이는 OpenAI-Microsoft, Google-DeepMind, Anthropic(독립)에 이어 Meta가 에이전트 시장의 네 번째 축으로 부상할 가능성을 보여주며, 특히 Facebook/Instagram/WhatsApp의 수십억 사용자 기반은 Manus의 "자율 태스크 에이전트"에 전례 없는 배포 채널을 제공한다. — *Source*: [[manus-ai/manus-ai|Manus AI]]

---

## Partnership Strategy Options

### 1. 멀티 LLM 허브 전략 + 모델 선택 유연성

SAP AI Core나 Snowflake Cortex AI처럼, 복수의 LLM을 통합 관리하는 멀티 LLM 허브를 구축해야 한다. 글로벌 모델과 함께 지역 특화 모델을 병행 지원하는 것이 차별화 포인트가 된다. 고객이 규제 요구(데이터 레지던시), 비용, 성능에 따라 모델을 선택할 수 있는 유연성을 제공해야 한다.

### 2. MCP + A2A 네이티브 지원 1일차 구현

프로토콜 미지원은 에이전트 상호운용성에서 불리한 포지션을 초래한다. MCP와 A2A를 모두 네이티브로 지원하여, 기존 AI 에이전트와 즉시 연결할 수 있는 환경을 만들어야 한다. Snowflake Managed MCP Server처럼, 데이터와 기능을 MCP 도구로 노출하면 외부 AI 에코시스템에서 자연스럽게 발견·활용되는 효과를 얻을 수 있다.

### 3. ERP/SI 벤더와의 전략적 파트너십

주요 ERP 및 시스템 통합 벤더와의 기술 파트너십(프로토콜 연동, 마켓플레이스 등록)을 구축하면, 자체 직접 판매보다 빠르게 시장에 침투할 수 있다. 이를 통해 주요 벤더의 기존 고객 기반에 접근할 수 있다.

### 4. "벤더 중립 통합" 접근

특정 ERP/CRM에 종속되지 않으면서, 이종 시스템의 데이터를 통합 검색·분석·활용할 수 있는 중립적 접근 계층을 제공하면, 다양한 시스템 환경의 고객을 확보할 수 있다.

### 5. 컨설팅/SI 파트너 생태계 구축

Workday의 Agent Partner Network에서 보듯, 컨설팅 펌과의 파트너십은 엔터프라이즈 도입의 핵심 채널이다. 주요 컨설팅 펌 및 클라우드 벤더와의 인프라 파트너십을 조기에 구축하면, 엔터프라이즈 시장 진입을 가속할 수 있다.

---

## Source References

### 제품 프로필
- [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Anthropic Claude(Bedrock), MuleSoft API Fabric, MCP 3.0
- [[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — Azure OpenAI 독점, MCP Copilot Studio 네이티브
- [[openai/openai|OpenAI]] — 자체 모델 전용, MCP 채택(2025-03), Microsoft 전략적 파트너십
- [[claude/claude|Claude]] — MCP 창안·주도, AAIF 기증, 멀티 엔터프라이즈 공급
- [[google-gemini/google-gemini|Google Gemini]] — A2A/A2UI 주도, Workspace 수직 통합
- [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — 멀티 LLM(자체+외부), MCP/A2A 미채택
- [[workday-assistant/workday-assistant|Workday Assistant]] — MCP+A2A 네이티브, Agent Partner Network 50+
- [[sap-joule/sap-joule|SAP Joule]] — AI Core 멀티 LLM, A2A 지원, Microsoft Copilot 양방향
- [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] — Managed MCP Server, Cortex AI 멀티 LLM
- [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] — MLflow/LangChain 통합, MCP 미지원
- [[glean/glean|Glean]] — 호스팅 MCP 서버, 100+ SaaS 커넥터
- [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] — Oracle GenAI + LLM Block, 프로토콜 미채택
- [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] — MCP Server(2025-09), 멀티 데이터 웨어하우스
- [[manus-ai/manus-ai|Manus AI]] — 멀티모델 오케스트레이션, Meta 인수
- [[vercel-v0/vercel-v0|Vercel v0]] — Anthropic Sonnet 기반, 복합 모델 아키텍처

### UI 리서치
- (파트너십/통합 UI 비교 문서 추가 예정)

### 외부 참고 자료
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)
- [Anthropic Blog: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)
- [Workday Newsroom: Agent Partner Network & Agent Gateway](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
- [SAP News: Joule Agent Architecture](https://community.sap.com/t5/technology-blog-posts-by-sap/how-sap-s-joule-agent-architecture-enables-companies-to-move-to-an-ai/ba-p/14158296)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
