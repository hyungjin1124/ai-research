---
type: insight-synthesis
topic_id: competitive-positioning-matrix
topic_name: AI 에이전트 경쟁 포지셔닝 매트릭스
category: market
tags:
- insight
- market
- competitive-analysis
- positioning
- segmentation
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
  - competitive analysis
  - market positioning
  - competitive landscape
  - market share
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 경쟁 포지셔닝 매트릭스

## TL;DR

- 19개 AI 에이전트 제품을 **타겟 시장(Enterprise vs B2C)**, **AI 성숙도(챗봇 vs 자율 에이전트)**, **에코시스템 개방성(폐쇄적 vs 개방적)**, **도메인 깊이(범용 vs 특화)**, **과금 모델**, **지역 초점** 6개 차원으로 비교하면, 시장은 **4개의 경쟁 세그먼트**로 명확히 분화되어 있다.
- **"도메인 깊이 x 에코시스템 개방성" 2x2 매트릭스**에서, 대부분의 Enterprise 벤더(Salesforce, SAP, Oracle)는 "깊은 도메인 + 폐쇄적 에코시스템" 사분면에 위치하며, "깊은 도메인 + 개방적 에코시스템" 사분면에 포지셔닝하면 **비어 있는 전략적 공백**을 차지할 수 있다.
- **AI 성숙도 측면**에서 Oracle Digital Assistant(전통적 챗봇)와 Manus AI(14일 자율 실행)는 성숙도 스펙트럼의 양 극단에 위치하며, 대부분의 엔터프라이즈 제품은 "가이디드 에이전트(Guided Agent)" 단계에 있다. 진정한 자율 에이전트(Autonomous Agent)를 제공하는 엔터프라이즈 제품은 아직 없어, 이 영역이 차세대 경쟁의 전장이 될 것이다.
- **글로벌 시장 커버리지**에서 Microsoft Copilot(Azure 글로벌 리전)과 Google Gemini(글로벌 + Android)가 가장 넓은 지역 도달 범위를 가지며, 한국 시장에 특화된 글로벌 제품은 **사실상 존재하지 않는** 공백 상태이다.
- **종합 경쟁력 순위**에서 Microsoft Copilot(에코시스템 통합 + 가격 경쟁력), Salesforce Agentforce(CRM 깊이 + 혁신 속도), Claude(코딩 벤치마크 + MCP 주도 + 에이전트 풀스택)가 3강 구도를 형성하고 있으나, 각각의 약점(Microsoft: 자체 추론 엔진 부재, Salesforce: 플랫폼 종속성, Claude: 엔터프라이즈 통합 깊이 부족)이 명확하다.

---

## Context

AI 에이전트 시장은 2024-2026년 사이에 급격한 팽창과 분화를 겪었으며, 2026년 2월 현재 19개 이상의 주요 제품이 서로 다른 전략과 포지셔닝으로 시장을 형성하고 있다. 단순한 "누가 더 좋은가"의 일차원적 비교를 넘어, 다차원적 포지셔닝 분석을 통해 각 제품이 차지하는 전략적 위치, 경쟁이 집중되는 영역, 그리고 아직 점유되지 않은 시장 공백을 파악해야 한다.

이 경쟁 포지셔닝 매트릭스는 "어디에서 싸울 것인가(Where to Play)"와 "어떻게 이길 것인가(How to Win)"의 전략적 질문에 답하는 기반이 된다. 특히 19개 제품 모두가 각각 1~2개 차원에서는 강점을 보이지만 모든 차원에서 지배적인 제품은 없다는 점은, 후발 진입자들에게도 포지셔닝 기회가 존재함을 시사한다.

---

## Cross-Product Analysis

### 다차원 비교 매트릭스

| 제품 | 카테고리 | 타겟 시장 | AI 성숙도 | 에코시스템 개방성 | 도메인 깊이 | 가격 접근성 | 지역 초점 |
|------|---------|----------|----------|--------------|----------|----------|---------|
| [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | Enterprise | 대기업 CRM | 가이디드 에이전트 | 중간 (MuleSoft + MCP) | 깊음 (CRM) | 중간 ($2/대화~) | 글로벌 |
| [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | Enterprise | 대기업 전체 | 가이디드 에이전트 | 중간 (1,000+ 커넥터) | 넓음 (Office+ERP) | 높음 ($30/사용자) | 글로벌 |
| [[openai/openai\|OpenAI]] | B2C | 개인~팀 | 자율 에이전트 (Codex) | 중간 (MCP, GPT Actions) | 범용 | 높음 (무료~$200) | 글로벌 |
| [[claude/claude\|Claude]] | B2C | 개인~Enterprise | 자율 에이전트 (Code/Cowork) | 높음 (MCP 주도) | 범용+코딩 특화 | 높음 (무료~$200) | 글로벌 |
| [[google-gemini/google-gemini\|Google Gemini]] | B2C | 개인~Enterprise | 가이디드 에이전트 | 높음 (MCP+A2A+A2UI) | 범용+멀티모달 | 높음 (무료~$250) | 글로벌+모바일 |
| [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | Enterprise | 대기업 ITSM | 가이디드 에이전트 | 낮음 (전용 커넥터) | 깊음 (ITSM) | 낮음 (비공개) | 글로벌 |
| [[workday-assistant/workday-assistant\|Workday Assistant]] | Enterprise | 대기업 HR/Finance | 가이디드 에이전트 | 높음 (MCP+A2A+ASOR) | 깊음 (HR/Finance) | 낮음 (비공개) | 글로벌 |
| [[sap-joule/sap-joule\|SAP Joule]] | Enterprise | 대기업 ERP | 가이디드 에이전트 | 중간 (A2A+멀티LLM) | 깊음 (ERP 전체) | 중간 (AI Unit) | 글로벌 |
| [[snowflake-intelligence/snowflake-intelligence\|Snowflake Intelligence]] | Analytics | 데이터 팀 | 에이전틱 분석 | 높음 (Managed MCP) | 중간 (데이터 분석) | 중간 (크레딧) | 글로벌 |
| [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks Mosaic AI]] | Analytics | 데이터/ML 엔지니어 | 에이전트 프레임워크 | 중간 (LangChain) | 중간 (ML/데이터) | 중간 (DBU) | 글로벌 |
| [[glean/glean\|Glean]] | Knowledge | Enterprise 전체 | 에이전틱 검색 | 높음 (MCP+100+ 커넥터) | 넓음 (지식 검색) | 낮음 (~$50/사용자) | 글로벌 |
| [[oracle-digital-assistant/oracle-digital-assistant\|Oracle Digital Assistant]] | Enterprise | Oracle Cloud 고객 | 전통적 챗봇+LLM | 낮음 (Oracle 전용) | 깊음 (ERP) | 낮음 (비공개) | 글로벌 |
| [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot Spotter]] | Analytics | 비즈니스 분석가 | 에이전틱 분석 | 중간 (MCP+멀티DW) | 중간 (BI/분석) | 중간 ($25~$50) | 글로벌 |
| [[manus-ai/manus-ai\|Manus AI]] | B2C | 개인~소규모 팀 | 완전 자율 에이전트 | 낮음 (브라우저 중심) | 범용 (태스크) | 중간 ($20~$200) | 글로벌 |
| [[vercel-v0/vercel-v0\|Vercel v0]] | B2C | 개발자~PM | 코드 생성 에이전트 | 중간 (GitHub 통합) | 좁음 (프론트엔드) | 높음 (무료~$30) | 글로벌 |

### 2x2 포지셔닝 매트릭스

#### 매트릭스 1: 도메인 깊이 x 에코시스템 개방성

```
                    에코시스템 개방성
              낮음 ◄─────────────► 높음

    깊음  ┌──────────────┬──────────────┐
    ▲     │ Oracle ODA   │ Workday      │
    │     │ ServiceNow   │ (ASOR+MCP    │
  도│     │ (전용 커넥터) │  +A2A)       │
  메│     │              │              │
  인│     ├──────────────┼──────────────┤
  깊│     │ Salesforce   │ Glean        │
  이│     │ SAP Joule    │ Snowflake    │
    │     │ (자사 생태계  │ (MCP+멀티DW) │
    │     │  +제한적 개방)│              │
    │     ├──────────────┼──────────────┤
    │     │ Vercel v0    │ Claude       │
    │     │ Manus AI     │ Google Gemini│
    ▼     │ (범용+폐쇄)  │ OpenAI       │
    범용  │              │ (MCP+범용)   │
          └──────────────┴──────────────┘
```

**인사이트**: "깊은 도메인 + 높은 개방성" 사분면에는 Workday만 존재하며, 이는 ASOR + MCP + A2A 지원 덕분이다. Salesforce와 SAP는 도메인이 깊지만 에코시스템이 상대적으로 폐쇄적이다. 도메인의 깊이와 MCP/A2A 기반 높은 개방성을 결합하면, 이 사분면에서 전략적 포지션을 확보할 수 있다.

#### 매트릭스 2: AI 성숙도 x 타겟 시장

```
                    타겟 시장
              B2C ◄─────────────► Enterprise

   완전   ┌──────────────┬──────────────┐
   자율   │ Manus AI     │              │
    ▲     │ (14일 비동기  │ [공백 영역]  │
    │     │  자율 실행)   │              │
  A │     ├──────────────┼──────────────┤
  I │     │ Claude       │ Salesforce   │
  성│     │ (Code/Cowork)│ Agentforce   │
  숙│     │ OpenAI       │ ServiceNow   │
  도│     │ (Agent/Codex)│ Now Assist   │
    │     │ Google       │ SAP Joule    │
    │     │ (Mariner/    │ Workday      │
    │     │  Jules)      │ Illuminate   │
    │     ├──────────────┼──────────────┤
    │     │ Vercel v0    │ Oracle ODA   │
    ▼     │ (코드 생성)  │ (챗봇+LLM)  │
   기본   │              │              │
          └──────────────┴──────────────┘
```

**인사이트**: "완전 자율 + Enterprise" 사분면은 **비어 있다**. Manus AI 수준의 자율성(14일 비동기, 20개 동시 태스크, 자기교정)을 엔터프라이즈 거버넌스(RBAC, 감사, 정책)와 결합한 제품은 아직 존재하지 않는다. 이 공백은 차세대 경쟁의 핵심 전장이 될 가능성이 높다.

### 세그먼트 분류

#### 세그먼트 1: ERP/CRM 네이티브 에이전트 (Domain-Embedded Agents)

**포지션**: 기존 엔터프라이즈 소프트웨어에 AI를 임베딩하여 비즈니스 프로세스를 자동화하는 에이전트.

**소속 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[sap-joule/sap-joule|SAP Joule]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[workday-assistant/workday-assistant|Workday Assistant]], [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]], [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

**공통 특징**:
- 기존 고객 기반에 AI 업셀
- 도메인 특화 에이전트 (Sales, HR, ITSM, Finance 등)
- 엔터프라이즈급 거버넌스 내장
- 트랜잭션 수준의 업무 실행 능력

**경쟁 역학**:
- Salesforce vs SAP: CRM vs ERP 도메인 주도권 경쟁
- ServiceNow: ITSM 독점 + 크로스 도메인 확장
- Workday: HR/Finance 특화 + ASOR 혁신으로 차별화
- Oracle: 긴 역사에도 AI 브랜딩 약세, Agentic AI 후발
- Microsoft: 에코시스템 범위로 모든 경쟁사와 동시 경쟁

**핵심 경쟁 지표**: 에이전트 수, 트랜잭션 커버리지(SAP: 80%), 도입 고객 수, TCO

#### 세그먼트 2: 범용 AI 어시스턴트 + 에이전트 (General-Purpose AI + Agents)

**포지션**: 강력한 LLM 성능을 기반으로 범용 대화형 AI와 특화 에이전트(코딩, 브라우저, 리서치)를 제공하는 플랫폼.

**소속 제품**: [[openai/openai|OpenAI]] (ChatGPT + Agent + Codex), [[claude/claude|Claude]] (claude.ai + Code + Cowork + in Chrome), [[google-gemini/google-gemini|Google Gemini]] (Gemini + Mariner + Jules)

**공통 특징**:
- 자체 LLM 보유 (최고 수준의 AI 모델)
- B2C → Enterprise 확장 경로
- 에이전트 제품 라인업 급속 확장 (코딩, 브라우저, 리서치)
- 무료 티어 + 프리미엄 구독 과금

**경쟁 역학**:
- OpenAI: 시장 점유율 1위 + 가장 넓은 모델 라인업 + Microsoft 채널
- Claude: 코딩 벤치마크 최상위 + MCP 프로토콜 주도 + 에이전트 풀스택
- Google: 멀티모달 네이티브 + 1M 컨텍스트 + Workspace 통합 + A2A/A2UI

**핵심 경쟁 지표**: 모델 성능(벤치마크), 사용자 수, 에이전트 제품 스펙트럼, 프로토콜 영향력

#### 세그먼트 3: 데이터/분석 에이전트 (Data & Analytics Agents)

**포지션**: 기업 데이터에 대한 자연어 기반 분석 및 인사이트 제공에 특화된 에이전트.

**소속 제품**: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]], [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]], [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]]

**공통 특징**:
- NL-to-SQL / 시맨틱 모델 기반 데이터 분석
- 데이터 플랫폼에 네이티브 통합(또는 멀티 데이터 소스 연결)
- 데이터 거버넌스(RBAC, 리니지) 중심 설계
- 소비 기반 과금 모델

**경쟁 역학**:
- Snowflake: 데이터 플랫폼 네이티브 + Managed MCP + 거버넌스
- Databricks: 에이전트 프레임워크(빌더) + Agent Evaluation + MLOps
- ThoughtSpot: 셀프서비스 BI + 4 에이전트 팀 + Drill-Anywhere

**핵심 경쟁 지표**: NL-to-SQL 정확도, 데이터 거버넌스, 시맨틱 모델 품질, 셀프서비스 수준

#### 세그먼트 4: 지식/검색 + 특화 에이전트 (Knowledge & Specialized Agents)

**포지션**: 엔터프라이즈 지식 검색, 자율 태스크 실행, 코드 생성 등 특정 영역에 특화된 에이전트.

**소속 제품**: [[glean/glean|Glean]], [[manus-ai/manus-ai|Manus AI]], [[vercel-v0/vercel-v0|Vercel v0]]

**공통 특징**:
- 특정 유스케이스에 최적화된 제품 설계
- 벤더 중립적 접근(특정 ERP/CRM에 비종속)
- 상대적으로 신생 기업(Glean 2019, Manus 2025, Vercel 2023)
- 높은 성장률과 투자자 관심

**경쟁 역학**:
- Glean: 엔터프라이즈 검색 + MCP 개방 플랫폼 + $7.2B 밸류에이션
- Manus AI: 자율 태스크 에이전트 + Glass Box UX + Meta 인수($2B)
- Vercel v0: AI 코드 생성 + Next.js 생태계 + 복합 모델 아키텍처

**핵심 경쟁 지표**: 태스크 완성도(Glean: 94%), 사용자 성장률, UX 혁신도, 생태계 확장성

---

## Key Findings

1. **"완전 자율 에이전트 + 엔터프라이즈 거버넌스" 조합이 미점유 공백**: 2x2 매트릭스 분석에서 "AI 성숙도 높음(완전 자율) + Enterprise 타겟" 사분면이 비어 있다. Manus AI 수준의 자율성(14일 비동기, 자기교정, 20개 동시 태스크)을 엔터프라이즈 거버넌스(Workday ASOR, ServiceNow Orchestrator 수준)와 결합한 제품은 아직 없다. Salesforce, SAP 등의 에이전트는 "가이디드" 수준에 머물러 있으며, 이 공백을 먼저 채우는 벤더가 차세대 시장을 선점할 가능성이 높다. — *Source*: [[manus-ai/manus-ai|Manus AI]], [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[workday-assistant/workday-assistant|Workday Assistant]]

2. **Microsoft Copilot의 "에코시스템 범위" 우위 — 하지만 깊이 부족**: Microsoft Copilot은 Dynamics 365 + Microsoft 365 + Teams + Outlook + Power Platform의 결합으로 가장 넓은 에코시스템 범위를 가진다. $30/사용자/월 번들 가격은 TCO 경쟁력을 제공하고, MCP 네이티브 지원과 멀티 에이전트 오케스트레이션은 기술적 선진성을 보여준다. 그러나 Salesforce의 Atlas 추론 엔진이나 SAP의 Knowledge Graph 같은 **독자적 추론 엔진이 없이 Azure OpenAI에 의존**하는 것은 LLM 성능 변동에 대한 품질 관리 리스크를 내포한다. — *Source*: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

3. **SAP Joule의 "2,400+ 스킬"이 도메인 깊이의 정량적 벤치마크 설정**: SAP Joule이 2,400개 이상의 Joule 스킬과 350개 이상의 AI 기능을 보유한 것은, 엔터프라이즈 AI 에이전트의 도메인 커버리지를 정량적으로 비교할 수 있는 기준점을 만들었다. Salesforce의 Agentforce Actions, ServiceNow의 Now Assist Skills, Oracle의 35+ 사전 구축 Skills 모두 이 스킬 수 경쟁에서 SAP에 뒤처지며, 이는 "에이전트 수"보다 "스킬 수(=실행 가능한 비즈니스 태스크 수)"가 진정한 경쟁 지표임을 보여준다. — *Source*: [[sap-joule/sap-joule|SAP Joule]], [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]]

4. **Claude의 "모델 + 프로토콜 + 에이전트 풀스택" 3중 전략이 가장 독보적 포지셔닝**: 19개 제품 중 Claude만이 (1) 최상위 성능 모델(SWE-bench 82.1%, Sonnet 5), (2) 업계 표준 프로토콜 주도(MCP), (3) 사용자 세그먼트별 에이전트 풀스택(Code/Cowork/Chrome)을 동시에 보유한다. OpenAI는 모델 + 에이전트는 보유하지만 프로토콜을 주도하지 않고, Google은 프로토콜(A2A/A2UI)을 주도하지만 에이전트 풀스택이 아직 미완성이다. 이 3중 전략은 "모델 공급자 + 플랫폼 표준 제정자 + 최종 사용자 제품"의 수직적 가치 사슬을 형성한다. — *Source*: [[claude/claude|Claude]], [[openai/openai|OpenAI]], [[google-gemini/google-gemini|Google Gemini]]

5. **ThoughtSpot의 "4 에이전트 팀" 모델이 분석 분야 에이전틱 AI의 새 기준**: ThoughtSpot Spotter(핵심 분석) + SpotterModel(시맨틱 모델 자동 생성) + SpotterViz(대시보드 생성) + SpotterCode(개발자 지원)의 4 에이전트 팀 구조는, 단일 에이전트가 아닌 "전문화된 에이전트 팀이 협업하는" 패러다임을 분석 분야에서 최초로 구현했다. 특히 SpotterModel이 Snowflake Intelligence의 수동 YAML 작성을 AI 자동 생성으로 대체한 것은, 시맨틱 레이어 구축의 진입 장벽을 근본적으로 낮춘다. — *Source*: [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]], [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]]

6. **Oracle Digital Assistant의 전략적 딜레마 — "가장 긴 역사, 가장 느린 혁신"**: 2018년 출시로 분석 대상 중 가장 긴 역사를 가진 Oracle Digital Assistant는 Skills 기반 모듈형 아키텍처, 35+ 사전 구축 Skills, Visual Flow Designer 등 성숙한 기반을 갖추었으나, MCP/A2A 미지원, Generative UI 부재, AI 브랜딩 약세로 Agentic AI 경쟁에서 후발 주자로 전락했다. ServiceNow(AI Agent Orchestrator), Salesforce(Atlas Engine), Workday(ASOR) 모두 2024-2025년에 차세대 아키텍처를 발표한 반면, Oracle은 기존 ODA에 LLM Block을 추가하는 점진적 접근을 택하여 혁신 속도에서 차이가 벌어지고 있다. — *Source*: [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]]

---

## Strategic Positioning Options

### 1. "도메인 깊이 + 개방적 에코시스템" 포지셔닝

2x2 매트릭스에서 "깊은 도메인 + 높은 개방성" 사분면에 Workday만 존재한다. 비즈니스 도메인에 깊은 특화와 MCP/A2A 기반의 높은 에코시스템 개방성을 결합하면, 이 사분면에서 전략적 포지션을 차지할 수 있다. 이는 Salesforce/SAP의 폐쇄적 생태계와도, Claude/ChatGPT의 범용 접근과도 차별화되는 포지셔닝이다.

### 2. "가이디드 에이전트 → 자율 에이전트" 진화 로드맵

현재 엔터프라이즈 AI 에이전트는 대부분 "가이디드" 수준에 머물러 있다. 초기 제품은 가이디드 에이전트(사용자 확인 기반)로 출시하되, 로드맵에 Manus AI 수준의 자율성(비동기 장기 실행, 자기교정, 병렬 태스크)을 엔터프라이즈 거버넌스와 결합한 자율 에이전트를 포함해야 한다. "완전 자율 + Enterprise" 공백을 채우는 것이 장기적 경쟁 우위의 핵심이다.

### 3. "스킬 수" 경쟁에서의 선택과 집중

SAP의 2,400+ 스킬은 범위 경쟁의 기준점을 설정했지만, 이를 추격하는 것은 비현실적이다. 대신 특정 도메인의 필수 핵심 스킬에 집중하여 "좁지만 깊은" 스킬셋을 구축하고, MCP를 통해 외부 에이전트의 스킬을 연결함으로써 범위를 보완하는 전략이 효과적이다.

### 4. 경쟁 세그먼트 간 크로스오버 기회

4개 세그먼트 간의 경계가 점차 흐려지고 있다. Claude가 B2C에서 Enterprise로 확장하고, ThoughtSpot이 분석에서 에이전틱 자동화로 확장하며, Glean이 검색에서 에이전트 플랫폼으로 확장하는 추세에서, 도메인 에이전트를 출발점으로 하되 데이터 분석, 지식 검색, 개발자 도구 영역으로 점진적 확장하는 로드맵을 수립할 수 있다.

### 5. UX 벤치마크 설정

경쟁 포지셔닝에서 UX는 점점 중요한 차별화 요소가 되고 있다. Oracle Digital Assistant의 전통적 챗봇 UI vs Manus AI의 Glass Box 투명성 패턴, Salesforce의 3-Panel Agent Builder vs Vercel v0의 실시간 프리뷰 등에서 보듯, UX 혁신이 제품의 인지된 가치를 크게 좌우한다. 최고 수준의 에이전트 UX 벤치마크를 달성하는 것이 중요하다.

---

## Source References

### 제품 프로필
- [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — CRM 네이티브 에이전트, Atlas Engine, $2/대화
- [[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — 에코시스템 범위 최대, $30/사용자 번들
- [[openai/openai|OpenAI]] — B2C 시장 점유율 1위, GPT-5.2, ChatGPT Agent + Codex
- [[claude/claude|Claude]] — 코딩 벤치마크 최상위, MCP 주도, 에이전트 풀스택
- [[google-gemini/google-gemini|Google Gemini]] — 멀티모달 네이티브, 1M 컨텍스트, A2A/A2UI
- [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — ITSM 도메인 독점, 3계층 아키텍처
- [[workday-assistant/workday-assistant|Workday Assistant]] — ASOR 혁신, MCP+A2A, Agent Partner Network
- [[sap-joule/sap-joule|SAP Joule]] — 2,400+ 스킬, 멀티 LLM AI Core, Collaborative Agent
- [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] — 데이터 네이티브 분석, Managed MCP, Semantic View
- [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] — 에이전트 프레임워크, Agent Evaluation, Lakeguard
- [[glean/glean|Glean]] — 엔터프라이즈 검색, Enterprise Graph, $7.2B 밸류에이션
- [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] — 최장 역사(2018), Skills 기반, LLM Block 추가
- [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] — 4 BI 에이전트 팀, Drill-Anywhere, 피드백 루프
- [[manus-ai/manus-ai|Manus AI]] — 완전 자율 에이전트, Glass Box, Meta $2B 인수
- [[vercel-v0/vercel-v0|Vercel v0]] — AI 코드 생성, 복합 모델, Vibe Coding

### UI 리서치
- (포지셔닝 관련 UI/UX 비교 문서 추가 예정)

### 외부 참고 자료
- [Salesforce Agentforce 3.0 Announcement (2025-06)](https://www.salesforce.com/news/press-releases/2025/06/23/agentforce-3-announcement/)
- [SAP News: 14 New Joule Agents at SAP Connect 2025](https://news.sap.com/2025/10/sap-connect-business-ai-new-joule-agents-embedded-intelligence/)
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)
- [ThoughtSpot Press: Four BI Agents Launch (2025-12)](https://www.thoughtspot.com/press-releases/thoughtspot-launches-four-bi-agents-that-work-as-a-team-to-deliver-modern-analytics)
- [CNBC: Glean $7.2B 기업가치](https://www.cnbc.com/2025/06/10/glean-gen-ai-search-startup-raises-150-million-at-7-billion-value.html)
- [TechCrunch: Meta acquires Manus AI](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
