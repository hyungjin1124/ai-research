---
type: insight-synthesis
topic_id: enterprise-vs-b2c-strategies
topic_name: Enterprise vs B2C AI 에이전트 전략 비교
category: market
tags:
- insight
- market
- go-to-market
- enterprise
- B2C
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
  - enterprise AI agent
  - B2C AI agent
  - enterprise strategy
  - consumer AI
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# Enterprise vs B2C AI 에이전트 전략 비교

## TL;DR

- AI 에이전트 시장의 GTM 전략은 **Enterprise-First**(Salesforce, SAP, ServiceNow, Workday, Oracle), **B2C-First**(OpenAI, Claude, Google Gemini), **개발자 플랫폼**(Vercel v0, Databricks, Manus AI), **지식 플랫폼**(Glean, ThoughtSpot, Snowflake)의 4개 축으로 분화되어 있으며, 각각 근본적으로 다른 제품 설계 철학과 판매 모션을 채택한다.
- **Enterprise-First** 벤더들은 기존 ERP/CRM 고객 기반에 AI를 임베딩하는 "Inside-Out" 전략을 택하여 높은 도입률을 달성하지만, **자사 에코시스템 종속성**이 성장의 천장으로 작용한다(비-Salesforce 고객의 Agentforce 진입 장벽, 비-SAP 환경에서의 Joule 활용 한계).
- **B2C-First** 벤더들은 수억 명의 사용자 베이스를 활용한 "Outside-In" 전략으로 엔터프라이즈 시장에 진입하고 있으며, OpenAI의 Microsoft 파트너십, Claude의 Claude Code/Cowork, Google의 Workspace 통합이 핵심 채널이다. B2C에서 검증된 UX가 엔터프라이즈 기대치를 높이는 **"소비자화(consumerization)"** 효과가 관찰된다.
- **개발자 플랫폼** 접근(Vercel v0, Databricks Mosaic AI)은 기술 의사결정자를 바텀업으로 획득하여 조직 전체 도입으로 확장하는 PLG 전략을 구사하며, AI 에이전트 시장의 **제3의 진입 경로**로 부상하고 있다.
- 2026년 현재 가장 주목할 추세는 **B2C-Enterprise 융합**이다. Claude는 B2C 어시스턴트에서 출발하여 Claude Code(개발자) → Claude Cowork(비개발자 업무) → Claude in Chrome(브라우저 자동화)으로 에이전트 풀스택을 구축하고 있으며, Google은 Gemini를 소비자 앱에서 Workspace 엔터프라이즈 통합까지 확장하고 있다.

---

## Context

AI 에이전트 제품의 GTM(Go-To-Market) 전략은 크게 "누구를 먼저 고객으로 삼을 것인가"에 따라 결정된다. Enterprise-First 벤더들은 기존 대기업 고객 관계를 활용하여 높은 ACV(연간 계약 가치)를 빠르게 확보하지만, 시장 범위가 자사 에코시스템에 제한된다. B2C-First 벤더들은 대규모 사용자 베이스와 브랜드 인지도를 무기로 바텀업 엔터프라이즈 침투를 시도하지만, 거버넌스/보안/통합 깊이에서 엔터프라이즈 요구를 충족시키는 데 시간이 필요하다.

엔터프라이즈 AI 에이전트 전략 수립에 있어, 이 두 접근법의 강점과 한계를 정확히 이해하는 것은 GTM 포지셔닝을 결정하는 기반이 된다. 한국 시장은 대기업 중심의 기업 구조와 빠른 기술 트렌드 수용이 공존하는 독특한 환경이므로, 글로벌 벤더들의 전략을 그대로 복제하기보다 한국 시장에 최적화된 하이브리드 접근이 필요하다.

---

## Cross-Product Analysis

### 비교 매트릭스

| 항목 | Enterprise-First | B2C-First | 개발자 플랫폼 | 지식/분석 플랫폼 |
|------|-----------------|-----------|------------|--------------|
| **대표 제품** | Salesforce, SAP, ServiceNow, Workday, Oracle | OpenAI, Claude, Google Gemini | Vercel v0, Databricks, Manus AI | Glean, ThoughtSpot, Snowflake |
| **1차 고객** | CIO/CTO, 구매팀 | 개인 소비자 | 개발자, 데이터 엔지니어 | 비즈니스 분석가, IT 관리자 |
| **판매 모션** | 탑다운 필드 세일즈 | 셀프서비스 구독 | PLG(Product-Led Growth) | 미드마켓 세일즈 + PLG |
| **핵심 가치** | 기존 시스템 네이티브 통합 | 범용 AI 능력 + 사용 경험 | 개발 생산성 10x | 기업 데이터 활용 민주화 |
| **도입 장벽** | 높음 (플랫폼 의존) | 낮음 (무료 시작) | 중간 (기술 스킬 필요) | 중간 (데이터 연결 필요) |
| **ACV** | $100K~$1M+ | $240~$3,000/인 | $240~$3,600/인 | $50K~$500K+ |
| **에이전트 유형** | 업무 프로세스 자동화 | 범용 어시스턴트+태스크 에이전트 | 코딩/빌드 에이전트 | 검색/분석 에이전트 |
| **거버넌스** | 내장 (RBAC, 감사, 정책) | 기본적 (Pro/Team 플랜) | 개발자 자율 | 데이터 거버넌스 중심 |
| **확장 방향** | AI 기능 추가 → 기존 고객 깊이 | 엔터프라이즈 → 조직 확대 | 팀/조직 → 엔터프라이즈 | 분석 → 에이전틱 자동화 |

### 패턴 분류

#### 패턴 A: Enterprise-First — "Inside-Out" 전략

**설명**: 기존 ERP/CRM/ITSM 플랫폼에 AI 에이전트를 네이티브로 임베딩하여, 현재 고객 기반에서 AI 매출을 창출하는 전략. 에이전트가 기존 비즈니스 데이터와 프로세스에 직접 접근할 수 있어 즉각적인 비즈니스 가치를 제공하지만, 플랫폼 외부 확장이 제한적이다.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[sap-joule/sap-joule|SAP Joule]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[workday-assistant/workday-assistant|Workday Assistant]], [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]], [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

**제품 설계 특징**:
- 에이전트가 ERP/CRM 트랜잭션을 직접 실행 (단순 조회가 아닌 실제 업무 처리)
- 도메인 특화 에이전트 (Salesforce: Sales/Service/Marketing/Commerce 에이전트, SAP: 14+ Joule Agent, Workday: HR 6종 + Finance 5종)
- 기존 UI/UX에 임베딩 (Sidecar 패턴, Embedded Panel)
- 엔터프라이즈급 거버넌스 내장 (RBAC, 감사 로그, 정책 엔진)

**판매 모션 특징**:
- 기존 ERP/CRM 계약의 업셀/크로스셀로 AI 도입
- SAP: RISE with SAP 마이그레이션과 연계한 Joule 번들
- Salesforce: Agentforce를 신규 성장 엔진으로 포지셔닝 ($2/대화로 진입 장벽 하향)
- ServiceNow: Pro Plus/Enterprise Plus 티어 업그레이드로 Now Assist 활성화

**장점**:
- 기존 고객 관계와 데이터 접근 권한을 즉시 활용하여 빠른 가치 실현
- 엔터프라이즈 보안/거버넌스 요구사항을 기본 충족
- 도메인 특화(금융, HR, ITSM 등)로 높은 업무 정확도

**단점**:
- 플랫폼 종속성이 성장의 천장 (비-Salesforce 고객은 Agentforce 사용 불가)
- 범용 AI 능력에서 B2C AI(ChatGPT, Claude, Gemini) 대비 열세
- 혁신 속도가 B2C 경쟁사 대비 느린 경향 (엔터프라이즈 릴리스 주기)

#### 패턴 B: B2C-First — "Outside-In" 전략

**설명**: 대규모 소비자 사용자 베이스에서 축적한 모델 성능, UX 인사이트, 브랜드 인지도를 활용하여 엔터프라이즈 시장에 진입하는 전략. 개인 사용자의 업무 활용 → 팀 도입 → 조직 전체 도입의 바텀업 경로를 따른다.

**예시 제품**: [[openai/openai|OpenAI]] (ChatGPT → Team → Enterprise), [[claude/claude|Claude]] (claude.ai → Claude Code → Cowork → Enterprise), [[google-gemini/google-gemini|Google Gemini]] (Gemini App → Workspace 통합)

**제품 설계 특징**:
- 범용 AI 능력을 기반으로 한 "만능 어시스턴트" 경험
- 풍부한 멀티모달 인터랙션 (OpenAI: 이미지/오디오/실시간 음성, Gemini: 네이티브 멀티모달, Claude: Extended Thinking)
- 에이전트 제품 라인업 확장 (OpenAI: ChatGPT Agent + Codex, Claude: Claude Code + Cowork + in Chrome, Google: Project Mariner + Jules)
- 개인화 기능 (OpenAI: Memory + Custom GPTs, Claude: Projects + Styles, Google: Gems)

**엔터프라이즈 진입 채널**:
- OpenAI: Microsoft Azure OpenAI Service를 통한 간접 엔터프라이즈 판매 + ChatGPT Team/Enterprise 직접 판매
- Claude: Claude Code의 개발자 커뮤니티 바텀업 침투 + Anthropic API 엔터프라이즈 계약
- Google: Workspace 네이티브 통합으로 기존 Google 고객에 자연스러운 AI 확장

**장점**:
- 대규모 사용자 베이스에서 축적한 인터랙션 데이터로 지속적 모델 개선
- 높은 브랜드 인지도 ("ChatGPT"가 AI 챗봇의 대명사)
- 빠른 혁신 주기와 다양한 에이전트 실험 (Codex, Claude Cowork, Project Mariner 등)

**단점**:
- 엔터프라이즈 거버넌스(RBAC, 감사, 데이터 레지던시)가 후발적으로 추가되어 성숙도가 부족
- 기업 내부 데이터/시스템과의 통합 깊이가 Enterprise-First 대비 얕음
- 개인 사용자 UX 최적화와 엔터프라이즈 요구사항 간의 긴장 관계

#### 패턴 C: 개발자 플랫폼 — "Build-First" 전략

**설명**: 개발자를 1차 고객으로 삼아 AI 에이전트 구축/배포 도구를 제공하고, 개발자가 조직 내에서 AI 도입을 주도하도록 하는 PLG 전략. 개발자 경험(DX)이 핵심 차별화 요소이며, 커뮤니티/생태계 구축에 투자한다.

**예시 제품**: [[vercel-v0/vercel-v0|Vercel v0]] (AI 코드 생성), [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] (에이전트 프레임워크), [[manus-ai/manus-ai|Manus AI]] (자율 태스크 에이전트)

**제품 설계 특징**:
- 개발자 도구 체인에 네이티브 통합 (Vercel: GitHub + Next.js, Databricks: MLflow + LangChain)
- 프레임워크 유연성 (Databricks: LangChain/LangGraph 호환, Vercel: Next.js 생태계)
- 코드 수준의 제어권 제공 (Manus: Code-First 검증, Databricks: Python SDK)
- 셀프서비스 온보딩 (무료 티어 또는 크레딧 기반 체험)

**장점**:
- 기술 의사결정자를 바텀업으로 획득하여 조직 도입의 내부 챔피언 확보
- 커뮤니티 기반 성장으로 낮은 CAC(고객 획득 비용)
- 빠른 프로토타이핑과 실험이 가능하여 혁신 속도 우위

**단점**:
- 비개발자 비즈니스 사용자에 대한 접근성이 제한적
- 엔터프라이즈 판매 모션(필드 세일즈, 컴플라이언스 대응)이 미성숙
- 프로덕션 규모의 거버넌스/보안 기능이 후순위

#### 패턴 D: 지식/분석 플랫폼 — "Data-First" 전략

**설명**: 기업 내부 데이터와 지식에 대한 AI 기반 접근을 제공하는 전략. 검색(Glean), 분석(ThoughtSpot, Snowflake)을 핵심으로 하되, 에이전트 기능을 점진적으로 확장한다.

**예시 제품**: [[glean/glean|Glean]] (엔터프라이즈 검색), [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] (에이전틱 분석), [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] (데이터 플랫폼 네이티브 분석)

**제품 설계 특징**:
- 벤더 중립적 접근 (Glean: 100+ SaaS 커넥터, ThoughtSpot: 멀티 데이터 웨어하우스 연결)
- 데이터 거버넌스 중심 설계 (Snowflake: RBAC + 보안 경계, Glean: 원본 권한 상속)
- 자연어 인터페이스를 통한 데이터 민주화 (NL-to-SQL, 시맨틱 검색)

**장점**:
- 특정 ERP/CRM 종속 없이 이종 환경의 기업에서 도입 가능
- 데이터 품질과 거버넌스에 집중하여 엔터프라이즈 신뢰도 높음
- 기존 데이터 인프라 투자를 그대로 활용

**단점**:
- "분석"에서 "실행"으로의 확장이 Enterprise-First 벤더 대비 느림
- 에이전트의 액션 범위가 데이터 조회/분석에 제한됨 (트랜잭션 실행 불가)
- ERP/CRM 통합 깊이에서 네이티브 벤더 대비 한계

---

## Key Findings

1. **"소비자화(Consumerization)" 효과가 엔터프라이즈 기대치를 재설정**: ChatGPT, Claude, Gemini에서 경험한 직관적 대화형 UX가 엔터프라이즈 사용자의 기대치를 높이고 있다. SAP Joule이나 Oracle Digital Assistant의 전통적 챗봇 UI는 ChatGPT 경험에 익숙한 사용자에게 실망감을 줄 수 있으며, 이는 Salesforce가 Agentforce에서 실시간 응답 스트리밍과 멀티모달 입력을 강화하는 배경이 된다. Enterprise 제품의 UX 바닥선이 B2C AI에 의해 상향 조정되고 있다. — *Source*: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[sap-joule/sap-joule|SAP Joule]], [[openai/openai|OpenAI]]

2. **Claude의 풀스택 에이전트 전략이 B2C-Enterprise 경계를 재정의**: Anthropic은 claude.ai(B2C 어시스턴트) → Claude Code(개발자 CLI) → Claude Cowork(비개발자 데스크톱 에이전트) → Claude in Chrome(브라우저 자동화)으로 사용자 세그먼트별 에이전트 라인업을 완성했다. 이는 단일 모델 기반에서 B2C와 Enterprise를 동시에 공략하는 전략으로, 기존의 "B2C 또는 Enterprise" 이분법을 넘어선다. Claude Code 매출이 2025년 7월 기준 전년 대비 5.5배 성장한 것은 개발자 채널의 엔터프라이즈 침투력을 입증한다. — *Source*: [[claude/claude|Claude]]

3. **Microsoft의 "에코시스템 번들" 전략이 TCO 경쟁에서 우위**: Microsoft Copilot의 $30/사용자/월 번들에 Sales, Service, Finance Copilot이 모두 포함되는 구조는, Salesforce(에이전트별 과금 + 플랫폼 비용)나 SAP(AI Unit + RISE + 모듈별 라이선스) 대비 단순하고 예측 가능한 TCO를 제공한다. Teams, Outlook, Word 등 전 세계 사용자가 가장 많이 쓰는 업무 도구와의 네이티브 통합은 채택 장벽을 추가로 낮추며, "기존 업무 도구 안에서 ERP 데이터에 접근"하는 경험은 ERP 전용 UI보다 실사용률이 높을 수 있다. — *Source*: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]]

4. **개발자 플랫폼(Vercel v0, Databricks)의 "제3의 경로" 부상**: Vercel v0는 자연어로 웹 애플리케이션을 생성하는 "Vibe Coding" 패러다임으로, 전통적 Enterprise SaaS나 B2C AI와 다른 시장을 개척했다. Databricks Mosaic AI는 에이전트 프레임워크 + 평가 + 배포의 엔드투엔드 MLOps를 제공하여 데이터 엔지니어를 1차 고객으로 확보한다. 이들 제품은 "AI 에이전트를 사용하는 것"이 아니라 "AI 에이전트를 만드는 것"에 초점을 맞추며, Agent Builder 생태계의 핵심 인프라가 되고 있다. — *Source*: [[vercel-v0/vercel-v0|Vercel v0]], [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]]

5. **Workday ASOR 모델이 Enterprise 에이전트 관리의 새 패러다임 제시**: Workday의 Agent System of Record(ASOR)는 AI 에이전트를 "디지털 직원"으로 채용-온보딩-역할배정-성과관리-퇴직까지 관리하는 개념으로, HR 도메인 전문성을 AI 거버넌스에 적용한 독보적 사례이다. 50개 이상 파트너의 에이전트를 단일 레지스트리에서 관리할 수 있는 이 모델은, "에이전트가 수백 개 사용되는 미래"에서 필수적인 인프라가 될 수 있으며, Enterprise-First 전략의 진화된 형태를 보여준다. — *Source*: [[workday-assistant/workday-assistant|Workday Assistant]]

6. **Manus AI의 "Fire and Forget" 모델이 에이전트 자율성의 새 기준 설정**: Manus AI는 태스크를 지시하면 최대 14일까지 비동기로 자율 실행되는 모델로, ChatGPT/Claude의 세션 기반 인터랙션과 근본적으로 다른 패러다임을 제시했다. 20개 동시 태스크 지원과 Glass Box 투명성 패턴은 "에이전트에게 일을 맡기고 잊어도 되는" 경험을 가능하게 하며, 이는 향후 Enterprise 에이전트에서도 기대되는 자율성 수준의 벤치마크가 되고 있다. Meta의 $20억 인수는 이 모델의 시장 가치를 검증한다. — *Source*: [[manus-ai/manus-ai|Manus AI]]

---

## Go-To-Market Strategy Options

### 1. "Enterprise + PLG" 하이브리드 GTM 전략

순수 Enterprise-First(필드 세일즈 중심)는 초기 자원 소모가 크고, 순수 B2C-First(셀프서비스)는 대기업의 탑다운 구매 프로세스와 맞지 않는다. 가장 적합한 접근은 "개발자/기술 리더를 무료 체험으로 획득(PLG) → 파일럿 프로젝트로 가치 검증 → 기업 단위 계약 확대(Enterprise 세일즈)"의 하이브리드 모델이다. 개발자 채널의 바텀업 침투 → 엔터프라이즈 확대 사례를 참고할 수 있다.

### 2. ERP 네이티브 통합 깊이를 핵심 차별화로 설정

Enterprise-First 벤더의 가장 큰 강점은 ERP/CRM 데이터에 대한 직접 접근과 트랜잭션 실행 능력이다. 특정 ERP와의 네이티브 통합을 구축하면, B2C AI(ChatGPT, Claude)나 지식 플랫폼(Glean)이 제공할 수 없는 "실제 업무 실행" 능력을 차별화할 수 있다. 이는 단순 조회/분석이 아닌, 구매주문 생성, 휴가 승인, 경비 보고서 제출 등 트랜잭션 수준의 에이전트 기능을 의미한다.

### 3. B2C 수준의 UX를 엔터프라이즈 제품에 구현

소비자화 효과를 활용하여, 직관적 대화형 UX를 엔터프라이즈 에이전트에 적용해야 한다. 이는 전통적 엔터프라이즈 UI와 차별화되는 지점이다. 실시간 응답 스트리밍, 투명성 패턴, Glass Box 설계 등 최신 UX 패턴을 엔터프라이즈 맥락에 적용하면, "기업용이지만 사용하기 쉬운" 포지셔닝이 가능하다.

### 4. 에이전트 거버넌스 프레임워크를 1일차부터 설계

B2C-First 벤더들의 공통 약점은 거버넌스가 후발적으로 추가된다는 점이다. 제품 설계 1일차부터 엔터프라이즈급 에이전트 관리(역할, 권한, 성과 추적), 정책 엔진(토큰 예산, 실행 범위 제한, 감사 로깅)을 내장해야 한다. 엔터프라이즈의 보안/컴플라이언스 요구를 기본 충족하는 거버넌스는 글로벌 B2C AI와의 핵심 차별화 요소가 된다.

### 5. "시장 전문" 포지셔닝으로 글로벌 벤더와 차별화

글로벌 Enterprise-First 벤더의 지역 시장 대응은 로컬라이제이션 수준에 그치며, 지역 고유 비즈니스 프로세스에 대한 깊이 있는 AI 에이전트는 제공하지 않는다. 특정 지역 시장과 고유 비즈니스 도메인에 특화된 에이전트로 포지셔닝하면, 글로벌 벤더가 따라올 수 없는 도메인 깊이를 확보할 수 있다.

---

## Source References

### 제품 프로필
- [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Enterprise-First 전략, CRM 네이티브 에이전트, Atlas 추론 엔진
- [[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — 에코시스템 번들 전략, Teams/Outlook 네이티브 통합
- [[openai/openai|OpenAI]] — B2C-First 전략, ChatGPT Agent/Codex, Microsoft 파트너십
- [[claude/claude|Claude]] — B2C-Enterprise 풀스택 에이전트 전략, MCP 프로토콜 주도
- [[google-gemini/google-gemini|Google Gemini]] — Workspace 통합 B2C-Enterprise 하이브리드
- [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — ITSM 도메인 독점, 3계층 에이전트 아키텍처
- [[workday-assistant/workday-assistant|Workday Assistant]] — ASOR 에이전트 관리 패러다임, HR/Finance 특화
- [[sap-joule/sap-joule|SAP Joule]] — SAP ERP 네이티브 임베딩, 2,400+ Joule 스킬
- [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] — 데이터 플랫폼 네이티브 분석
- [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] — 에이전트 프레임워크 + MLOps 개발자 플랫폼
- [[glean/glean|Glean]] — 벤더 중립 엔터프라이즈 검색, 100+ SaaS 커넥터
- [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] — Oracle Cloud 네이티브, Skills 기반 모듈형
- [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] — 에이전틱 분석, 4 BI 에이전트 팀
- [[manus-ai/manus-ai|Manus AI]] — 자율 태스크 에이전트, Fire and Forget 패러다임
- [[vercel-v0/vercel-v0|Vercel v0]] — AI 코드 생성 플랫폼, Vibe Coding 선도

### UI 리서치
- (GTM 전략 관련 UI/UX 비교 문서 추가 예정)

### 외부 참고 자료
- [Salesforce Agentforce 공식 사이트](https://www.salesforce.com/agentforce/)
- [Microsoft Build 2025: Multi-Agent Orchestration](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/)
- [Anthropic Blog: Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [TechCrunch: Meta acquires Manus AI](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
