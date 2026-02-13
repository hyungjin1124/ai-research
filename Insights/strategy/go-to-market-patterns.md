---
type: insight-synthesis
topic_id: go-to-market-patterns
topic_name: GTM 전략 패턴 비교 분석
category: strategy
tags:
- insight
- strategy
- go-to-market
- sales-strategy
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
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI agent go-to-market strategy 2026
  - enterprise AI agent sales pricing model
  - developer-led growth AI agent
  - Korea enterprise AI GTM channel partner
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# GTM 전략 패턴 비교 분석

## TL;DR

- AI 에이전트 시장의 GTM 전략은 5가지 뚜렷한 패턴으로 분류된다: **(1) Enterprise Sales-Led**, **(2) Product-Led Growth**, **(3) Developer-Led**, **(4) Channel/Partner-Led**, **(5) Platform/Ecosystem-Led**.
- **가장 빠른 매출 성장**을 보인 모델은 PLG(Product-Led Growth)이다. [[manus-ai/manus-ai|Manus AI]]의 출시 8개월 ARR $100M, [[openai/openai|OpenAI]]의 B2C 시장 지배력이 이를 증명한다. 반면 **가장 높은 LTV**는 Enterprise Sales-Led([[salesforce-agentforce/salesforce-agentforce|Salesforce]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow]])에서 나온다.
- **무료 티어 전략**이 AI 에이전트 시장의 핵심 경쟁 무기로 부상했으며, OpenAI, Google, Anthropic 모두 관대한 무료 티어를 제공한다. 이는 유료 전환(conversion)보다 **시장 교육과 습관 형성**에 목적이 있다.
- 한국 시장의 GTM은 **대기업 계열사 내부 배포**(삼성SDS, LG CNS)와 **기존 ERP 고객 기반 활용**(더존)이라는 고유한 패턴을 형성하며, 이는 글로벌 시장과 근본적으로 다르다.

---

## Overview

Go-to-Market 전략은 기술적 우위 못지않게 AI 에이전트 시장에서의 성패를 결정짓는 요인이다. [^1] [^4] 동일한 기술력을 가진 제품이라도 GTM 전략에 따라 시장 점유율, 수익성, 성장 속도가 크게 달라진다. 특히 AI 에이전트 시장은 기존 SaaS 시장과 다른 특성을 가진다: (1) 기술 진입 장벽이 빠르게 변화하고, (2) 사용자 교육 비용이 높으며, (3) 신뢰(Trust)가 구매 결정의 핵심 요소이다.

---

## Cross-Product Analysis

### GTM 패턴 분류 매트릭스

| GTM 패턴 | 제품 | 초기 진입 전략 | 확장 전략 | 가격 전략 | 주요 성과 지표 | Source |
|----------|------|-------------|----------|----------|-------------|--------|
| **Enterprise Sales-Led** | Salesforce Agentforce, SAP Joule, ServiceNow Now Assist, Workday Assistant | C-level 세일즈, 컨설팅 파트너 | Cross-sell/Upsell | 시트 기반 + 소비 기반 | ACV, NRR, 도입 기업 수 | [^1] [^6] [^8] [^7] |
| **Product-Led Growth (PLG)** | OpenAI, Manus AI | 무료/저가 B2C 제품 | 엔터프라이즈 업셀 | 프리미엄, 크레딧 기반 | WAU, 유료 전환율, ARR | [^3] [^12] |
| **Developer-Led** | Claude (Anthropic), Vercel v0, Databricks Mosaic AI | 개발자 도구/SDK/API | 팀 → 기업 확산 | API 종량 과금, 개발자 무료 | API 호출 수, GitHub Stars | [^4] [^13] [^10] |
| **Platform/Ecosystem-Led** | Microsoft Copilot, Google Gemini | 기존 플랫폼 번들 | 생태계 잠금 | 번들 구독 | 플랫폼 MAU, AI 활성화율 | [^2] [^5] |
| **그룹사/Channel-Led** | 삼성SDS FabriX, LG CNS AgenticWorks, Glean | 모기업/채널 파트너 | 레퍼런스 기반 외부 확대 | 엔터프라이즈 구독 | 그룹사 도입률, 파트너 수 | [^14] [^15] [^11] |

### 패턴 A: Enterprise Sales-Led

#### 대표 제품

**[[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]** [^1]
- **진입 전략**: 기존 Salesforce CRM 고객 기반(전 세계 15만+ 기업)에 Agentforce를 Cross-sell. Dreamforce 등 대규모 이벤트로 인지도 확보
- **가격**: $2/대화(소비 기반) + 산업별 애드온 $125-$650/사용자/월. 초기 진입은 낮지만 TCO는 높아질 수 있음
- **채널**: 직접 세일즈 + Salesforce 파트너 생태계(SI, ISV). MuleSoft를 통한 외부 시스템 통합 컨설팅
- **핵심 전략**: 6개월 간격 메이저 버전 출시(1.0->2.0->3.0)로 혁신 속도를 강조하여 기존 고객의 AI 전환을 가속

**[[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]]** [^6]
- **진입 전략**: ITSM 도메인 독보적 시장 지배력(Gartner MQ 리더 10년 연속) 활용. 기존 Now Platform 고객에 AI 애드온 판매
- **가격**: Pro Plus/Enterprise Plus 시트 기반 + Assist 토큰 소비 모델. AI Starter Pack(25 ITSM Pro 시트 + 150K Assists)으로 진입 장벽 낮춤
- **채널**: 직접 세일즈 + ServiceNow Store + Knowledge 컨퍼런스
- **핵심 전략**: ITSM -> CSM -> HRSD -> ITOM으로 도메인 확장. Skills -> Agents -> Orchestrator 3계층으로 점진적 AI 성숙도 업셀

**[[sap-joule/sap-joule|SAP Joule]]** [^8]
- **진입 전략**: RISE with SAP 마이그레이션과 연계한 자연스러운 AI 도입. 기존 SAP 고객(포춘 500 중 87%)에 Joule 번들 제공
- **가격**: AI Unit 소비 기반(~7EUR/단위), RISE with SAP Public Cloud에 기본 포함
- **채널**: SAP 직접 세일즈 + SAP 파트너 에코시스템 + SAP Store
- **핵심 전략**: S/4HANA Cloud 마이그레이션 트리거와 AI 도입을 결합. 2,400+ Skills로 즉시 가치 제공

**[[workday-assistant/workday-assistant|Workday Assistant]]** [^7]
- **진입 전략**: HR/Finance 도메인 기존 고객에 Illuminate 브랜드로 AI 확장
- **가격**: Flex Credits 소비 모델(구체적 단가 비공개)
- **채널**: 직접 세일즈 + Agent Partner Network(50+ 파트너) + Workday Marketplace
- **핵심 전략**: ASOR 개념으로 "AI 에이전트 관리 = HR 관리"라는 새로운 카테고리 창출. Sana Labs 인수로 AI 검색/학습 역량 강화

#### Enterprise Sales-Led 패턴의 특징

- **장점**: 높은 ACV(연간 계약 가치), 강한 고객 잠금 효과, 예측 가능한 매출
- **단점**: 긴 세일즈 사이클(6-18개월), 높은 CAC(고객 획득 비용), 기존 플랫폼 종속
- **핵심 성공 요인**: 기존 고객 기반의 크기와 깊이, 도메인 전문성, 컨설팅 파트너 생태계

### 패턴 B: Product-Led Growth (PLG)

#### 대표 제품

**[[openai/openai|OpenAI (ChatGPT)]]** [^3]
- **진입 전략**: 무료 ChatGPT로 역사상 가장 빠른 사용자 확보. "ChatGPT"를 AI의 대명사로 만들어 시장 자체를 교육
- **가격**: 무료 / Plus $20/월 / Pro $200/월 / Team $25-30/월/인
- **무료 티어 전략**: GPT-5.2 접근, 제한된 메시지 수, 기본 도구 사용 가능. 사용량 한도로 유료 전환 유도
- **확장 전략**: 개인 사용 -> Team -> Enterprise 업셀. Custom GPTs + GPT Store로 생태계 확장
- **핵심 전략**: B2C 점유율 1위를 기반으로 엔터프라이즈 시장 진입. Microsoft 파트너십을 통한 Azure OpenAI Service로 기업 채널 확보

**[[manus-ai/manus-ai|Manus AI]]** [^12]
- **진입 전략**: 초대 기반 베타 → 바이럴 성장 → 일반 공개. 출시 직후 소셜 미디어 바이럴로 폭발적 인지도 확보
- **가격**: Standard $20/월(4,000 크레딧) / Customizable $40/월 / Extended $200/월
- **핵심 전략**: "Chat-to-Execution" 패러다임으로 새로운 카테고리 창출. Glass Box 투명성이 입소문의 핵심 동인. 출시 8개월 ARR $100M 달성 후 Meta $2B 인수

#### PLG 패턴의 특징

- **장점**: 빠른 사용자 확보, 낮은 초기 CAC, 제품 자체가 세일즈 도구, 바이럴 성장
- **단점**: 낮은 초기 ARPU, 높은 인프라 비용(무료 사용자), 엔터프라이즈 전환의 어려움
- **핵심 성공 요인**: 제품의 즉각적 가치 체감(Aha moment), 강력한 무료 티어, 유료 전환 트리거 설계

### 패턴 C: Developer-Led

#### 대표 제품

**[[claude/claude|Claude (Anthropic)]]** [^4]
- **진입 전략**: API 먼저 공개(개발자 대상) → Claude.ai 웹 앱(일반 사용자) → Claude Code CLI(개발자 에이전트) 순차 출시
- **가격**: API 종량 과금($1-$25/MTok 모델별) + 구독 플랜($20-$200/월)
- **개발자 채널**: MCP 프로토콜 오픈소스 공개로 개발자 커뮤니티 형성. GitHub에서 MCP 서버 생태계 자발적 확산
- **핵심 전략**: MCP를 업계 표준으로 만들어 에이전트 도구 연결의 "중력 중심"이 됨. Claude Code 매출 5.5배 성장이 이 전략의 성공을 증명. Linux Foundation에 MCP 기증으로 중립성 확보

**[[vercel-v0/vercel-v0|Vercel v0]]** [^13]
- **진입 전략**: Next.js 개발자 커뮤니티(전 세계 수백만)를 기반으로 v0 자연스럽게 도입
- **가격**: Free(월 $5 크레딧) / Premium $20/월 / Team $30/유저/월
- **개발자 채널**: Vercel 플랫폼(배포 인프라) + Next.js(프레임워크) + v0(AI 코드 생성)의 풀스택 개발자 경험
- **핵심 전략**: "Vibe Coding" 트렌드 선도. 개발자가 v0로 코드 생성 -> Vercel로 배포하는 자연스러운 워크플로우로 락인

**[[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]]** [^10]
- **진입 전략**: 데이터 엔지니어/ML 엔지니어 대상. AI Playground로 진입 장벽 낮춤
- **가격**: DBU 기반 소비 모델
- **개발자 채널**: MLflow(오픈소스) 3.0, LangChain 통합, Python SDK
- **핵심 전략**: 오픈소스(MLflow, Delta Lake)로 개발자 커뮤니티 구축 → 유료 플랫폼(Databricks)으로 전환

#### Developer-Led 패턴의 특징

- **장점**: 강한 기술적 credibility, 낮은 CAC, 자발적 커뮤니티 형성, 바텀업 기업 침투
- **단점**: 비기술 의사결정자에 대한 접근 제한, 매출 전환까지 긴 시간, 커뮤니티 관리 비용
- **핵심 성공 요인**: 오픈소스/표준 프로토콜 기여, 개발자 경험(DX) 품질, 기술 문서 수준

### 패턴 D: Platform/Ecosystem-Led

#### 대표 제품

**[[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]]** [^5]
- **진입 전략**: Microsoft 365 + Dynamics 365 기존 사용자에 Copilot 자동 노출. Teams, Outlook에서 자연스럽게 AI 경험
- **가격**: $30/사용자/월 번들(Sales, Service, Finance 모두 포함). 기존 M365 라이선스에 추가
- **생태계**: Microsoft 365 (Teams, Outlook, Word, Excel) + Azure + Power Platform + GitHub Copilot
- **핵심 전략**: "이미 사용하는 도구에 AI를 추가"하는 최소 마찰 전략. 번들 가격으로 개별 모듈 구매 대비 TCO 경쟁력

**[[google-gemini/google-gemini|Google Gemini]]** [^2]
- **진입 전략**: Google 검색 + Android + Gmail/Docs에 Gemini 통합. 전 세계 30억+ 사용자에 자동 노출
- **가격**: 무료(관대한 무료 티어) / AI Pro $19.99/월 / AI Ultra ~$250/월
- **생태계**: Google Workspace + Android + Google Cloud + YouTube
- **핵심 전략**: 가장 큰 도달 범위(reach)를 활용한 시장 침투. 무료 티어에서 API 일일 1,000건 허용으로 개발자 채택도 동시 추구. A2A/A2UI 프로토콜로 에이전트 생태계 표준 주도

#### Platform/Ecosystem-Led 패턴의 특징

- **장점**: 즉각적인 대규모 도달, 낮은 마찰, 기존 워크플로우 통합, 교차 판매 시너지
- **단점**: 기존 플랫폼 성능/한계에 종속, 독립 브랜드 구축 어려움, 혁신 속도 제한
- **핵심 성공 요인**: 기존 사용자 기반 규모, 번들 가격 경쟁력, 생태계 잠금 효과

### 패턴 E: 그룹사/Channel-Led (한국 특수)

#### 대표 제품

**[[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]]** [^14]
- **진입 전략**: 삼성 계열사 전체(약 20만 명)에 우선 배포 → 외부 대기업/공공기관으로 확장
- **가격**: 비공개 (엔터프라이즈 구독)
- **채널**: 삼성 그룹사 내부 → KB금융, S-OIL 등 외부 대기업 → 300+ 공공기관
- **핵심 전략**: 모기업 실전 검증(일일 5시간 20분 절감)을 레퍼런스로 활용. OpenAI 리셀러 지위로 AI 모델 접근 차별화

**[[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]]** [^15]
- **진입 전략**: LG 계열사(LG디스플레이 등)에 우선 적용 → 외부 기업으로 확장
- **가격**: 비공개 (엔터프라이즈 구독 추정)
- **채널**: LG 계열사 → 500+ AX 프로젝트 외부 고객 → 코히어/클라인 파트너 채널
- **핵심 전략**: LG디스플레이 연간 100억 원+ 절감 실증으로 외부 세일즈. 코히어와의 글로벌 협력으로 기술 credibility 확보

**[[glean/glean|Glean]]** [^11]
- **진입 전략**: 엔터프라이즈 검색이라는 명확한 pain point로 진입 → AI 에이전트 플랫폼으로 확장
- **가격**: ~$50/유저/월 (추정), 중앙값 계약 ~$65K/년
- **채널**: 직접 세일즈 + 기술 파트너(100+ SaaS 커넥터)
- **핵심 전략**: "검색"이라는 보편적 pain point로 초기 도입 장벽 낮춤 → Agentic Engine으로 AI 에이전트 가치 확대. 벤더 중립 포지셔닝으로 이종 SaaS 환경 기업에 어필

#### 그룹사/Channel-Led 패턴의 특징

- **장점**: 초기 고객 보장, 레퍼런스 확보 용이, 빠른 실증 데이터 축적
- **단점**: 모기업 의존도, 외부 시장 확대의 어려움, 독립적 브랜드 구축 제한
- **핵심 성공 요인**: 모기업/채널의 규모, 실증 데이터의 구체성, 외부 확대를 위한 독립적 가치 제안

### 가격 전략 비교

| 가격 모델 | 제품 | 장점 | 단점 | Source |
|-----------|------|------|------|--------|
| **소비 기반 (대화당/토큰)** | Salesforce ($2/대화), ServiceNow (Assist 토큰), SAP (AI Unit ~7EUR) | 초기 진입 장벽 낮음, 사용량에 비례한 가치 | TCO 예측 어려움, 비용 폭증 리스크 | [^1] [^6] [^8] |
| **시트 기반 구독** | Microsoft ($30/사용자/월) | 예측 가능한 매출, 높은 NRR | 미사용 시트 낭비, 활성 사용률 과제 | [^5] |
| **크레딧 기반** | Manus (4,000-40,000 크레딧/월), Vercel ($5-$20 크레딧), Snowflake (크레딧) | 유연한 사용, 다양한 가격 포인트 | 크레딧 가치 불투명, 미사용 소멸 | [^12] [^13] [^9] |
| **프리미엄 (무료+유료)** | OpenAI (Free/Plus $20/Pro $200), Claude (Free/Pro $20/Max $200), Google (Free/Pro $20/Ultra $250) | 대규모 사용자 확보, 바이럴 | 무료 사용자 인프라 비용, 유료 전환율 | [^3] [^4] [^2] |
| **API 종량 과금** | OpenAI (토큰당), Anthropic (토큰당), Google (토큰당), Databricks (DBU) | 개발자 친화적, 사용량 비례 | B2C 매출 예측 어려움 | [^3] [^4] [^2] [^10] |
| **번들** | Microsoft ($30 번들), SAP (RISE 포함) | 빠른 침투, TCO 경쟁력 | AI 매출 독립 추적 어려움 | [^5] [^8] |
| **비공개** | Glean, 삼성SDS, LG CNS, Workday | 고객별 맞춤 가격 | 가격 비교 어려움, 초기 영업 마찰 | [^11] [^14] [^15] [^7] |

### 무료 티어 전략 비교

| 제품 | 무료 티어 범위 | 유료 전환 트리거 | 유료 시작가 | Source |
|------|-------------|---------------|-----------|--------|
| [[openai/openai\|OpenAI]] | GPT-5.2 접근, 제한된 메시지 | 메시지 한도 초과, 고급 모델 접근 | $20/월 | [^3] |
| [[claude/claude\|Claude]] | 기본 모델 접근, 5시간 세션 제한 | 사용량 한도, Extended Thinking | $20/월 | [^4] |
| [[google-gemini/google-gemini\|Google]] | Gemini 2.5 Flash, 관대한 사용량 | 고급 모델(Gemini 3 Pro), Deep Research | $19.99/월 | [^2] |
| [[vercel-v0/vercel-v0\|Vercel v0]] | 월 $5 크레딧 | 크레딧 소진, 팀 기능 | $20/월 | [^13] |
| [[manus-ai/manus-ai\|Manus AI]] | 없음 (유료만) | - | $20/월 | [^12] |
| [[snowflake-intelligence/snowflake-intelligence\|Snowflake]] | 기존 Snowflake 고객 기본 크레딧 | 크레딧 소진 | 소비 기반 | [^9] |

### 지역별 GTM 전략

| 전략 | 글로벌 우선 | 한국 특화 | 하이브리드 | Source |
|------|-----------|----------|-----------|--------|
| 제품 | OpenAI, Claude, Google, Salesforce, Microsoft, SAP, ServiceNow, Workday, Manus, Vercel, Databricks | 삼성SDS, LG CNS | Glean, Snowflake | [^3] [^4] [^2] [^14] [^15] |
| 한국어 지원 | 다국어 중 하나 | 한국어 최적화 | 영문 중심 (한국 진출 시 현지화) | - |
| 한국 채널 | 글로벌 파트너/리셀러 | 그룹사 + 대기업 직접 영업 | 파트너 발굴 중 | - |
| 한국 규정 대응 | 제한적 | 네이티브 (세법, K-IFRS 등) | 미지원 | - |

---

## Key Findings

### 1. PLG에서 Enterprise로의 "이중 전환" 전략이 가장 높은 밸류에이션 성장을 달성

OpenAI와 Anthropic의 사례가 보여주듯, B2C PLG로 시작하여 Enterprise 세일즈로 확장하는 이중 전환 전략이 가장 높은 밸류에이션 성장을 달성했다. [^3] [^4] OpenAI는 무료 ChatGPT로 시장을 교육한 뒤 Team/Enterprise 플랜과 Azure OpenAI Service로 기업 시장에 진입했고, Anthropic은 Claude API(개발자) -> Claude.ai(일반 사용자) -> Claude Code(개발자 에이전트) -> Claude Cowork(비개발자 에이전트)로 확장하며 $60B 밸류에이션을 달성했다. 핵심은 **B2C에서 확보한 브랜드 인지도와 사용자 경험이 엔터프라이즈 세일즈의 전환 비용을 대폭 낮춘다**는 것이다.

### 2. 프로토콜/표준 주도가 가장 효과적인 Developer-Led GTM

Anthropic이 MCP를 오픈소스로 공개하고 업계 표준으로 만든 전략은, 전통적인 Developer-Led GTM(SDK 공개, 문서화, 커뮤니티 운영)을 넘어서는 새로운 차원의 접근이다. [^4] [^2] MCP가 OpenAI, Google, Microsoft에 의해 채택되면서, Anthropic은 **에이전트 도구 연결의 "인프라 제공자"** 위치를 확보했다. 이는 단순히 API 사용자를 확보하는 것보다 훨씬 깊은 시장 침투를 가능하게 한다. 유사하게 Google의 A2A/A2UI 프로토콜 주도도 같은 맥락이다.

### 3. "번들 가격"이 Enterprise AI 침투의 가장 빠른 경로

Microsoft의 $30/사용자/월 번들 전략(Sales, Service, Finance Copilot 모두 포함)과 SAP의 RISE with SAP 번들(Joule 기본 포함)은, 기업이 AI를 별도 예산으로 구매하지 않고 기존 플랫폼 비용에 포함시키는 심리적 장벽을 낮추는 전략이다. [^5] [^8] [^1] 반면 Salesforce의 대화당 $2 독립 과금은 AI 매출을 명확히 추적할 수 있지만, 초기 채택 속도에서는 번들 대비 불리할 수 있다.

### 4. 한국 시장의 "그룹사 내부 배포" 모델의 이중성

삼성SDS의 20만 명 사용자와 LG CNS의 LG디스플레이 100억 원+ 절감 실증은 그룹사 내부 배포 모델의 강력한 장점을 보여준다. [^14] [^15] 그러나 이 모델은 외부 시장 확대에 구조적 한계가 있다: (1) 외부 기업은 삼성/LG와 동일한 환경이 아니므로 레퍼런스 적용성이 제한적이고, (2) 독립적 제품 브랜드보다 그룹사 IT 서비스 이미지가 강하며, (3) 가격이 비공개이므로 외부 고객의 TCO 비교가 어렵다. 삼성SDS/LG CNS가 커버하지 못하는 **중견기업 시장**에서 투명한 가격과 독립적 브랜드로 차별화할 수 있는 기회가 존재한다.

### 5. "Pain Point 진입 -> 플랫폼 확장" 패턴의 유효성

Glean이 "엔터프라이즈 검색"이라는 보편적 pain point로 진입한 뒤 AI 에이전트 플랫폼으로 확장한 전략, Snowflake가 "데이터 분석"으로 진입한 뒤 AI Intelligence로 확장한 전략은, 명확한 pain point로 초기 도입을 확보한 뒤 플랫폼으로 확장하는 "Wedge Strategy"의 전형이다. [^11] [^9] Glean의 ARR $100M+ 달성과 $7.2B 밸류에이션은 이 전략의 유효성을 증명한다.

### 6. 에이전트 마켓플레이스가 GTM의 차세대 채널

Workday의 Agent Partner Network(50+ 파트너), OpenAI의 GPT Store, 더존 ONE AI의 에이전트 마켓플레이스는, 에이전트 자체를 서드파티가 개발하고 배포하는 마켓플레이스 모델이 새로운 GTM 채널로 부상하고 있음을 보여준다. [^7] [^3] 이 모델은 (1) 자사 개발 리소스 없이 에이전트 공급을 확대하고, (2) 파트너 생태계를 통한 간접 세일즈 채널을 확보하며, (3) 네트워크 효과로 플랫폼 가치를 증가시킨다. 더존 ONE AI 마켓플레이스의 실제 활성 사용률은 아직 확인이 필요하다. [출처 필요]

---

## Recent Updates

<!-- auto-append: 새로운 GTM 전략 변화를 아래 테이블에 추가 -->
| Date | Source | Summary | Tags |
|------|--------|---------|------|
|  |  |  |  |

---

## References

### Vault

[^1]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- $2/대화 소비 기반 과금, Agent Builder, 6개월 메이저 버전 주기
[^2]: [[google-gemini/google-gemini|Google Gemini]] -- 관대한 무료 티어, Google Workspace 통합, A2A/A2UI
[^3]: [[openai/openai|OpenAI]] -- Free/Plus/Pro 프리미엄 모델, Custom GPTs + GPT Store
[^4]: [[claude/claude|Claude (Anthropic)]] -- MCP 표준화, Claude Code 5.5x 성장, Developer-Led
[^5]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] -- $30/사용자/월 번들, M365 네이티브 통합
[^6]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- Assist 토큰, AI Starter Pack, ITSM 지배력
[^7]: [[workday-assistant/workday-assistant|Workday Assistant]] -- Flex Credits, Agent Partner Network 50+
[^8]: [[sap-joule/sap-joule|SAP Joule]] -- AI Unit ~7EUR, RISE 번들, 2400+ Skills
[^9]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- 크레딧 소비 기반, Semantic Model
[^10]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- DBU 과금, MLflow 오픈소스 전략
[^11]: [[glean/glean|Glean]] -- ~$50/유저/월, Pain point 진입 -> 플랫폼 확장
[^12]: [[manus-ai/manus-ai|Manus AI]] -- 크레딧 $20-200/월, 출시 8개월 ARR $100M
[^13]: [[vercel-v0/vercel-v0|Vercel v0]] -- Free $5 크레딧, Developer-Led, Next.js 생태계
[^14]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- 비공개 가격, 20만 명 사용자, 그룹사 GTM
[^15]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 비공개 가격, 500+ AX 프로젝트, 코히어 협력

### External

[^16]: [Anthropic Blog: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
[^17]: [Workday Newsroom: Agent Partner Network 발표](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
[^18]: [Salesforce Agentforce Pricing](https://www.winfomi.com/blog/salesforce-agentforce-pricing-service-sales)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
