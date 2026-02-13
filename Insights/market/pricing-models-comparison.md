---
type: insight-synthesis
topic_id: pricing-models-comparison
topic_name: AI 에이전트 과금 모델 비교 분석
category: market
tags:
- insight
- market
- pricing
- business-model
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
- planning_agent
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI pricing
  - subscription model
  - usage-based pricing
  - per-conversation pricing
  - credit-based
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 과금 모델 비교 분석

## TL;DR

- AI 에이전트 시장의 과금 모델은 **대화 기반(Salesforce $2/대화)**, **시트 기반(Microsoft $30/사용자/월)**, **소비 기반(Snowflake 크레딧, SAP AI Unit)**, **프리미엄 구독(OpenAI/Claude $20~$200/월)**, **번들/임베디드(SAP RISE 포함, Oracle Cloud 포함)** 5가지 패턴으로 분화되어 있으며, 시장이 성숙함에 따라 하이브리드 모델로 수렴하는 추세이다.
- **대화 기반 과금(Salesforce)**은 도입 장벽을 낮추지만, 산업별 애드온($125~$650/사용자/월)과 Data Cloud/MuleSoft 라이선스를 합산하면 실질 TCO가 시트 기반보다 높아질 수 있어 **"미끼 가격"** 리스크가 존재한다.
- **소비 기반 모델**(Snowflake 크레딧, Databricks DBU, SAP AI Unit, Workday Flex Credits)은 사용량 비례 과금이라는 공정성을 제공하나, 복잡한 쿼리/워크플로우에서 **비용 폭발(cost explosion)** 사례가 보고되어 예측 가능성이 핵심 과제이다.
- B2C AI 제품(OpenAI, Claude, Google Gemini)은 **무료 티어 + $20/월 중간 티어 + $200~$250/월 최상위 티어**의 3단계 구조가 사실상 업계 표준으로 정착되었으며, 최상위 티어 경쟁이 심화되고 있다.
- 엔터프라이즈 벤더(ServiceNow, Oracle)의 **비공개 가격 정책**은 TCO 비교를 어렵게 만들어 구매 의사결정에서 불리하게 작용하며, 투명한 가격 공개가 경쟁 우위로 부상하고 있다.

---

## Context

AI 에이전트 시장이 급속히 확대되면서, 과금 모델의 선택은 단순한 매출 구조를 넘어 제품 포지셔닝, 고객 획득 전략, 장기 수익성을 결정하는 핵심 전략적 의사결정이 되었다. 전통적 SaaS의 시트 기반 라이선스 모델은 AI 에이전트의 "사용량 예측 불가능성"과 충돌하며, 이에 따라 Salesforce는 대화 기반, Snowflake는 크레딧 기반, SAP는 AI Unit 기반 등 다양한 실험이 진행 중이다.

엔터프라이즈 AI 에이전트 프로덕트의 가격 전략을 수립함에 있어, 경쟁 제품들의 과금 모델을 정밀하게 분석하는 것은 필수적이다. 특히 엔터프라이즈 시장의 구매 패턴(연간 라이선스 계약 선호, 사전 예산 배정 필수)을 고려하면, 소비 기반 모델의 채택 여부와 그 구조 설계가 시장 진입 성패를 좌우할 수 있다. 본 분석은 19개 경쟁 제품의 과금 구조를 체계적으로 비교하여, 가격 전략 수립에 필요한 인사이트를 도출한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| 제품 | 과금 모델 유형 | 기본 가격 | 상위 티어/애드온 | 무료 티어 | 가격 투명성 |
|------|-------------|----------|----------------|---------|----------|
| [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | 대화 기반 | $2/대화 | 산업별 애드온 $125~$650/사용자/월 | X | 중간 |
| [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | 시트 기반 번들 | $30/사용자/월 | Dynamics 365 라이선스 별도 | X | 높음 |
| [[openai/openai\|OpenAI]] | 프리미엄 구독 | 무료 / Plus $20/월 | Pro $200/월, Team $25~30/월/인 | O | 높음 |
| [[claude/claude\|Claude]] | 프리미엄 구독 | 무료 / Pro $20/월 | Max 5x $100/월, Max 20x $200/월 | O | 높음 |
| [[google-gemini/google-gemini\|Google Gemini]] | 프리미엄 구독 | 무료 / AI Pro $19.99/월 | AI Ultra ~$250/월 | O | 높음 |
| [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | 시트+토큰 하이브리드 | Pro Plus/Enterprise Plus 애드온 | AI Starter Pack(25시트+150K Assists) | X | 낮음 |
| [[workday-assistant/workday-assistant\|Workday Assistant]] | 크레딧 소비 | Flex Credits (단가 비공개) | 커스텀 견적 | X | 낮음 |
| [[sap-joule/sap-joule\|SAP Joule]] | AI Unit 소비 | ~7유로/AI Unit, 최소 100단위 | RISE with SAP 번들 포함 | X | 중간 |
| [[snowflake-intelligence/snowflake-intelligence\|Snowflake Intelligence]] | 크레딧 소비 | 100메시지당 6.7크레딧 | LLM 함수별 토큰 과금 | X | 높음 |
| [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks Mosaic AI]] | DBU 소비 | DBU 기반 + 토큰당 추론 비용 | AI Gateway 별도 과금 | X | 중간 |
| [[glean/glean\|Glean]] | 시트 기반 | ~$50/사용자/월 (추정) | 중앙값 계약 ~$65K/년 | X | 낮음 |
| [[oracle-digital-assistant/oracle-digital-assistant\|Oracle Digital Assistant]] | 세션 기반 | 1,000 Sessions 단위 | 최소 시간당 250 Requests | X | 낮음 |
| [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot Spotter]] | 시트 기반 | Essentials $25/사용자/월 | Pro $50/사용자/월, Enterprise 커스텀 | X | 높음 |
| [[manus-ai/manus-ai\|Manus AI]] | 크레딧 소비 | Standard $20/월(4,000 크레딧) | Extended $200/월(40,000 크레딧) | X | 높음 |
| [[vercel-v0/vercel-v0\|Vercel v0]] | 크레딧 구독 | Free $0(월 $5 크레딧) | Premium $20/월, Team $30/유저/월 | O | 높음 |

### 패턴 분류

#### 패턴 A: 대화/세션 기반 과금 (Conversation/Session-Based)

**설명**: AI 에이전트와의 개별 대화 또는 세션을 단위로 과금하는 모델. 사용자가 에이전트와 상호작용한 만큼만 비용이 발생하는 구조로, 초기 도입 비용을 최소화할 수 있다.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] ($2/대화), [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] (1,000 Sessions 단위)

**장점**:
- 사용량이 적은 초기 도입 단계에서 비용 부담이 낮아 PoC/파일럿에 유리
- "사용한 만큼 지불" 원칙으로 고객 심리적 저항이 낮음
- 에이전트 채택률이 낮은 조직에서도 비용 효율적

**단점**:
- 대규모 사용 시 시트 기반 대비 비용이 급증할 수 있음 (Salesforce: 1,000대화/월 = $2,000 vs Microsoft: $30/사용자)
- 산업별 애드온, 플랫폼 라이선스(Data Cloud, MuleSoft) 등 숨겨진 비용이 실질 TCO를 높임
- 대화 단위 정의가 불명확하면 비용 예측이 어려움

#### 패턴 B: 시트 기반/구독형 (Seat-Based/Subscription)

**설명**: 사용자 수 기반의 월정액 구독 모델. 전통적 SaaS 라이선스와 동일한 구조로, 예산 계획과 비용 예측이 용이하다.

**예시 제품**: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] ($30/사용자/월 번들), [[glean/glean|Glean]] (~$50/사용자/월), [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] ($25~$50/사용자/월)

**장점**:
- 비용 예측이 용이하여 기업 예산 계획에 적합
- 무제한 사용이 가능하여 높은 활용도를 유도
- Microsoft Copilot의 경우 Sales/Service/Finance Copilot 번들 포함으로 기능 대비 가격 경쟁력 확보

**단점**:
- AI 에이전트를 적극 활용하지 않는 사용자에게도 동일 비용이 발생하여 낭비 가능
- 대규모 조직에서는 총 비용이 높아질 수 있음 (1,000명 x $30 = $30,000/월)
- 사용량 기반 모델 대비 도입 초기 비용 부담이 큼

#### 패턴 C: 소비/크레딧 기반 (Consumption/Credit-Based)

**설명**: 사용량에 비례하여 크레딧, 토큰, 유닛 등의 단위로 과금하는 모델. 클라우드 인프라(AWS, Azure) 과금 방식과 유사하며, 데이터/AI 플랫폼에서 주로 채택한다.

**예시 제품**: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] (크레딧), [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] (DBU), [[sap-joule/sap-joule|SAP Joule]] (AI Unit ~7유로/단위), [[workday-assistant/workday-assistant|Workday Assistant]] (Flex Credits), [[manus-ai/manus-ai|Manus AI]] (크레딧)

**장점**:
- 사용량에 정비례하는 공정한 과금으로 작은 팀도 접근 가능
- 초기 도입 비용이 없거나 매우 낮아 실험적 사용이 용이
- 워크로드 변동이 큰 환경(계절성 비즈니스 등)에 적합

**단점**:
- 복잡한 쿼리/워크플로우에서 예상 외 비용 폭발 가능 (Snowflake: 대규모 테이블 조인에서 단일 쿼리 수천 달러 사례)
- 비용 예측이 어려워 한국 기업의 연간 예산 사전 배정 방식과 충돌
- 다중 과금 요소(DBU + 토큰 + 스토리지)가 혼재하면 TCO 산정이 복잡

#### 패턴 D: 프리미엄 구독 + 무료 티어 (Freemium)

**설명**: 무료 기본 티어에서 핵심 기능을 제공하고, 프리미엄 구독으로 고급 기능/사용량 한도를 확장하는 모델. B2C AI 제품에서 지배적인 패턴이다.

**예시 제품**: [[openai/openai|OpenAI]] (무료/Plus $20/Pro $200), [[claude/claude|Claude]] (무료/Pro $20/Max $200), [[google-gemini/google-gemini|Google Gemini]] (무료/AI Pro $19.99/AI Ultra ~$250), [[vercel-v0/vercel-v0|Vercel v0]] (Free/Premium $20)

**장점**:
- 무료 티어가 사용자 획득의 강력한 퍼널 역할
- $20/월 중간 티어에서 시장 가격 합의가 형성되어 소비자 인지도 높음
- $200+/월 최상위 티어로 파워 유저 수익화 달성

**단점**:
- 무료 사용자의 전환율(conversion rate)이 수익성에 직결되어 경영 리스크 존재
- 무료 티어 유지를 위한 인프라 비용 부담
- 엔터프라이즈 판매에는 별도의 Team/Enterprise 플랜이 필요

#### 패턴 E: 번들/임베디드 (Bundled/Embedded)

**설명**: AI 기능을 기존 제품 라이선스에 포함시키거나, 기존 구독의 추가 기능으로 제공하는 모델. AI의 독립 가치보다 기존 플랫폼의 부가가치 향상에 초점을 둔다.

**예시 제품**: [[sap-joule/sap-joule|SAP Joule]] (RISE with SAP 번들 기본 포함), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] (Pro Plus/Enterprise Plus 애드온)

**장점**:
- 기존 고객에게 추가 비용 부담 없이(또는 최소 비용으로) AI 도입을 유도
- 플랫폼 전환 비용(switching cost)을 높여 고객 이탈 방지
- AI 기능이 기존 워크플로우에 자연스럽게 녹아들어 채택률 향상

**단점**:
- AI 기능의 독립 수익화가 어려움
- 기존 라이선스 비용이 이미 높은 경우 추가 과금에 대한 저항 발생
- 비번들 고객(기본 플랜)에 대한 AI 접근이 제한되어 시장 확대에 불리

---

## Key Findings

1. **B2C AI 가격 표준의 정착 — $20/월 중간 티어 컨센서스**: OpenAI Plus($20/월), Claude Pro($20/월), Google AI Pro($19.99/월), Manus Standard($20/월), Vercel v0 Premium($20/월) 모두 중간 티어를 $20 전후로 설정했다. 이는 시장이 "AI 어시스턴트의 적정 가격"에 대한 소비자 합의에 도달했음을 시사하며, 이 가격대를 벗어나는 신규 B2C 진입자는 가치 정당화에 더 큰 노력이 필요하다. — *Source*: [[openai/openai|OpenAI]], [[claude/claude|Claude]], [[google-gemini/google-gemini|Google Gemini]]

2. **Salesforce "대화당 $2"의 전략적 이중성**: Salesforce의 대화당 $2 가격은 마케팅적으로 매력적이지만, 실제 TCO 계산 시 Data Cloud, MuleSoft 라이선스, 산업별 애드온($125~$650/사용자/월)이 추가되어 경쟁사 대비 높아질 수 있다. 이 모델은 "에이전트 비용은 낮지만 플랫폼 비용은 높은" 구조로, Salesforce 기존 고객에게는 매력적이지만 신규 고객 획득에는 높은 플랫폼 진입 비용이 장벽으로 작용한다. 반면 Microsoft의 $30/사용자/월 번들은 Sales/Service/Finance Copilot을 모두 포함하여 총 소유 비용 예측이 용이하다. — *Source*: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

3. **소비 기반 모델의 "비용 폭발" 리스크 — Snowflake 사례**: Snowflake Intelligence의 크레딧 기반 모델에서 대규모 테이블 조인 쿼리에 단일 쿼리로 수천 달러의 크레딧이 소비된 사례가 보고되었다. Databricks도 DBU + 토큰 + 스토리지의 다중 과금 요소로 비용 예측이 복잡하다. 이는 소비 기반 모델이 "소규모 실험에는 저렴하지만 프로덕션 규모에서는 위험할 수 있음"을 보여주며, 비용 경고/상한 설정(cost cap) 기능의 중요성을 부각시킨다. — *Source*: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]], [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]]

4. **가격 비투명성이 시장 포지셔닝에 미치는 영향**: ServiceNow, Workday, Glean, Oracle은 공개 가격표 없이 영업팀 협의 방식을 유지한다. 반면 Microsoft($30/사용자/월), ThoughtSpot($25~$50/사용자/월), OpenAI/Claude/Gemini는 웹사이트에서 투명하게 가격을 공개한다. 가격 투명성은 셀프서비스 구매 경험이 중요해지는 PLG(Product-Led Growth) 시대에 경쟁 우위로 작용하며, 특히 중소/중견기업 시장에서 비공개 가격은 진입 장벽으로 인식된다. — *Source*: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[workday-assistant/workday-assistant|Workday Assistant]], [[glean/glean|Glean]]

5. **최상위 티어($200+/월) 경쟁의 심화**: OpenAI Pro($200/월), Claude Max 20x($200/월), Google AI Ultra(~$250/월), Manus Extended($200/월)가 모두 $200 이상의 최상위 티어를 제공한다. 이 티어의 핵심 차별화는 사용량 한도 확장(Claude Max 20x), 최고 성능 모델 독점 접근(OpenAI Pro), 멀티모달 확장(Google Ultra) 등이며, 파워 유저 수익화(ARPU 극대화) 전장이 되고 있다. — *Source*: [[openai/openai|OpenAI]], [[claude/claude|Claude]], [[google-gemini/google-gemini|Google Gemini]], [[manus-ai/manus-ai|Manus AI]]

6. **SAP의 AI Unit 모델 — 엔터프라이즈 소비 기반의 선례**: SAP Joule의 AI Unit(~7유로/단위, 최소 100단위 = 700유로/년)은 엔터프라이즈 ERP 벤더가 소비 기반 모델을 채택한 드문 사례이다. RISE with SAP 번들에 기본 포함되어 기존 고객의 추가 도입 장벽을 낮추면서도, 대규모 사용에는 AI Unit 추가 구매가 필요한 하이브리드 구조이다. 그러나 2025년 중반 번들링 정책 변경이 시장에 혼란을 일으킨 사례는, 가격 정책 변경의 소통 방식이 중요함을 보여준다. — *Source*: [[sap-joule/sap-joule|SAP Joule]]

---

## Pricing Strategy Options

### 1. 하이브리드 과금 모델: 기본 시트 + 소비 초과분

엔터프라이즈 시장의 연간 예산 사전 배정 관행을 고려하면, 순수 소비 기반 모델은 채택 저항이 클 수 있다. 기본 시트 라이선스(예측 가능한 기본 비용)에 일정 사용량을 포함하고, 초과 사용분에 대해서만 소비 기반으로 과금하는 하이브리드 모델이 엔터프라이즈 시장에 최적화된 접근이다. Microsoft의 $30/사용자/월 번들과 SAP의 RISE 번들+AI Unit 초과 과금 구조를 참고할 수 있다.

### 2. TCO 투명성을 경쟁 우위로 활용

ServiceNow, Workday, Oracle 등 경쟁사의 비공개 가격 정책은 중소/중견기업 고객에게 진입 장벽으로 인식된다. 웹사이트에 명확한 가격표를 공개하고, TCO 계산기를 제공하며, 숨겨진 플랫폼 비용이 없는 올인원 가격을 제시하면, 가격 투명성 자체가 차별화 요소가 될 수 있다. 중견기업 시장에서는 "영업팀 협의 없이 가격을 확인할 수 있는" 경험이 중요하다.

### 3. "비용 폭발" 방지 메커니즘 내장

Snowflake의 비용 폭발 사례에서 보듯, 소비 기반 요소를 포함하는 경우 반드시 비용 경고 알림, 월간/일간 비용 상한(cost cap), 실시간 사용량 대시보드, 비용 예측 도구를 프로덕트에 내장해야 한다. 이는 고객 신뢰 확보와 이탈 방지에 직결되며, Databricks의 비용 모니터링 기능이나 SAP의 AI Unit 예산 관리를 참고할 수 있다.

### 4. 무료 티어 전략 — 개발자/기술 리더 획득

엔터프라이즈 시장에서도, 기술 의사결정자(개발자, IT 리더)를 확보하기 위한 제한적 무료 티어 또는 30일 무료 체험이 효과적일 수 있다. Google Gemini의 API 무료 티어(일일 1,000건 요청)나 Vercel v0의 무료 티어(월 $5 크레딧 포함)처럼, 개발자가 자율적으로 제품을 평가할 수 있는 셀프서비스 진입점을 제공하는 것이 바텀업(bottom-up) 엔터프라이즈 도입의 출발점이다.

### 5. 지역 시장 맞춤 가격 전략: 현지화 + 계약 할인 구조

해외 경쟁 제품들의 달러 기반 과금은 환율 변동 리스크와 결제 불편을 야기한다. 현지화 기반 정찰제를 제공하고, 엔터프라이즈 시장이 선호하는 연간 계약 + 선결제 할인(10~20%) 구조를 적용하면, 지역 시장 특화 가격 경쟁력을 확보할 수 있다. 현지 ERP 벤더의 가격 전략을 벤치마크할 수 있다.

---

## Source References

### 제품 프로필
- [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — $2/대화 소비 기반 과금, 산업별 애드온 구조
- [[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — $30/사용자/월 번들 가격 전략
- [[openai/openai|OpenAI]] — 무료/Plus $20/Pro $200 3단계 구독 모델
- [[claude/claude|Claude]] — 무료/Pro $20/Max $100~$200 구독 모델
- [[google-gemini/google-gemini|Google Gemini]] — 무료/AI Pro $19.99/AI Ultra ~$250 구독 모델
- [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — 시트 기반 + Assist 토큰 하이브리드
- [[workday-assistant/workday-assistant|Workday Assistant]] — Flex Credits 소비 모델
- [[sap-joule/sap-joule|SAP Joule]] — AI Unit 소비 기반 + RISE 번들
- [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] — 크레딧 기반 소비 모델
- [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] — DBU 기반 소비 모델
- [[glean/glean|Glean]] — 비공개 시트 기반 (~$50/사용자/월 추정)
- [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] — 세션 기반 과금
- [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] — 시트 기반 $25~$50/사용자/월
- [[manus-ai/manus-ai|Manus AI]] — 크레딧 구독 $20~$200/월
- [[vercel-v0/vercel-v0|Vercel v0]] — 크레딧 구독 + 무료 티어

### UI 리서치
- (가격 UI/구매 경험 분석 문서 추가 예정)

### 외부 참고 자료
- [Agentforce Pricing Overview (Winfomi)](https://www.winfomi.com/blog/salesforce-agentforce-pricing-service-sales)
- [Microsoft 365 Copilot Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)
- [Snowflake Intelligence Pricing (Select)](https://select.dev/posts/snowflake-intelligence-overview-pricing-and-cost-monitoring)
- [Databricks AI Agent Pricing (Community)](https://community.databricks.com/t5/technical-blog/demystifying-databricks-pricing-for-ai-agents/ba-p/122281)
- [ThoughtSpot Pricing](https://www.thoughtspot.com/pricing)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
