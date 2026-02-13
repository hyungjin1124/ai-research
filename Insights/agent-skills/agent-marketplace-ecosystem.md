---
type: insight-synthesis
topic_id: agent-marketplace-ecosystem
topic_name: 에이전트/스킬 마켓플레이스 생태계
category: agent-skills
tags:
- insight
- agent-skills
- marketplace
- ecosystem
- partner
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- salesforce-agentforce
- claude
- microsoft-copilot
- workday-assistant
- glean
- servicenow-now-assist
source_files:
- '[[salesforce-agentforce]]'
- '[[claude]]'
- '[[microsoft-copilot]]'
- '[[workday-assistant]]'
- '[[glean]]'
- '[[servicenow-now-assist]]'
relevant_roles:
- planning_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - agent marketplace
  - skill marketplace
  - plugin store
  - AppExchange
  - agent registry
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트/스킬 마켓플레이스 생태계

## TL;DR

- **AI 에이전트 마켓플레이스는 4가지 뚜렷한 패턴으로 분화되고 있다**: (1) 기존 앱 마켓플레이스를 에이전트/스킬로 확장하는 Platform-Curated형(Salesforce AppExchange, ServiceNow Store), (2) 오픈소스 프로토콜 기반 커뮤니티 레지스트리인 Open Registry형(Claude MCP Server Registry), (3) SI/벤더 파트너십 기반의 Partner-Certified형(Workday Agent Partner Network), (4) 검증된 서드파티 도구를 큐레이션하는 Curated Directory형(Glean MCP Directory)
- **마켓플레이스의 성공을 결정짓는 핵심 요소는 "거버넌스 레이어의 깊이"이다**: 단순 목록 제공을 넘어, 에이전트별 RBAC, 실행 감사 로그, 비용 할당, 성과 추적까지 제공하는 벤더(Workday ASOR, ServiceNow AI Agent Orchestrator)가 엔터프라이즈 채택에서 유리한 고지를 점한다
- **기존 앱 에코시스템의 규모가 에이전트 마켓플레이스의 초기 경쟁력을 좌우한다**: Salesforce AppExchange(7,000+ 앱), Microsoft Power Platform(1,000+ 커넥터), ServiceNow Store(수천 개 앱)처럼 기존 통합 자산이 풍부한 벤더가 에이전트 마켓플레이스로의 전환에서 압도적 선점 효과를 누린다
- **MCP의 AAIF 기증 이후 "프로토콜 기반 마켓플레이스"가 벤더 중립 대안으로 부상 중이다**: Claude의 MCP Server Registry와 Glean의 MCP Directory는 특정 플랫폼 종속 없이 에이전트 도구를 발견-연결하는 새로운 유통 채널을 형성하고 있으며, 이는 기존 플랫폼 벤더의 마켓플레이스 독점에 대한 구조적 도전이 된다
- **"스킬 마켓플레이스"와 "에이전트 마켓플레이스"는 다른 시장이다**: ServiceNow의 Skills(단위 기능)와 Agents(복합 워크플로우) 구분, Salesforce의 Topics/Actions 체계가 보여주듯, 세분화된 기능 단위와 완성된 에이전트 단위는 다른 소비 패턴과 과금 모델을 요구한다

---

## Context

엔터프라이즈 AI 에이전트 프로덕트를 개발함에 있어, 에이전트와 스킬을 외부 개발자 및 파트너가 배포-발견-소비할 수 있는 마켓플레이스/에코시스템 전략은 프로덕트의 장기 경쟁력과 네트워크 효과를 결정짓는 핵심 요소이다. 단순히 에이전트를 잘 만드는 것을 넘어, 파트너와 커뮤니티가 에이전트/스킬을 자발적으로 생산-유통-소비하는 생태계를 구축해야 플랫폼으로서의 해자(moat)가 형성된다.

현재 경쟁사들은 각자의 강점과 기존 생태계 자산에 기반하여 매우 다른 마켓플레이스 전략을 취하고 있다. 기존 앱 스토어를 에이전트로 확장하는 Salesforce, 오픈 프로토콜로 커뮤니티 생태계를 육성하는 Anthropic, 대형 SI 파트너십으로 에이전트 네트워크를 구축하는 Workday, 검증된 도구를 큐레이션하는 Glean까지 -- 이 다양한 접근의 장단점을 분석하면 자사 상황에 맞는 마켓플레이스 전략을 수립하는 데 직접적 근거가 된다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 마켓플레이스 유형 | 핵심 매커니즘 | 생태계 규모 | 거버넌스 수준 | 개방성 | 성숙도 |
|---------|---------------|-------------|-----------|------------|--------|--------|
| Salesforce Agentforce | AppExchange + Agentforce Studio | 기존 7,000+ 앱 생태계를 에이전트 액션으로 확장, MuleSoft API Catalog | 매우 큼 (AppExchange 7,000+) | 높음 (Agentforce Gateway ABAC, Topic Center) | 중간 (자사 플랫폼 중심) | 높음 |
| Claude (Anthropic) | MCP Server Registry + 커뮤니티 | 오픈소스 MCP 프로토콜 기반 커뮤니티 레지스트리, AAIF 중립 거버넌스 | 큼 (수백 개 MCP 서버) | 낮음 (커뮤니티 자율) | 매우 높음 (오픈소스, 벤더 중립) | 중간 |
| Microsoft Copilot | Copilot Studio + Power Platform | 1,000+ Power Platform 커넥터를 에이전트 도구로 활용, Microsoft 365 통합 | 매우 큼 (1,000+ 커넥터) | 높음 (Copilot Orchestrator, Entra 인증) | 중간 (Microsoft 생태계 중심) | 높음 |
| Workday Assistant | Workday Marketplace + Agent Partner Network | ASOR 기반 파트너 에이전트 등록-관리, 50+ 글로벌 SI/벤더 파트너 | 중간 (50+ 파트너, 성장 중) | 매우 높음 (ASOR 라이프사이클 관리) | 중간 (파트너 인증 필요) | 초기 |
| Glean | MCP Directory + Agent Catalog | 호스팅 MCP 서버 + 20+ 검증 MCP 서버 디렉터리, 프리빌트 에이전트 카탈로그 | 작음~중간 (20+ MCP 서버, 20+ 프리빌트 에이전트) | 중간 (권한 상속 모델) | 높음 (MCP 기반 상호운용) | 중간 |
| ServiceNow Now Assist | ServiceNow Store + NASK | Skills 기반 마켓플레이스, Now Assist Skill Kit으로 커스텀 스킬 개발, AI Agent Studio | 큼 (ServiceNow Store 수천 앱) | 매우 높음 (Orchestrator 정책 엔진, Assist 토큰 예산) | 낮음 (자사 플랫폼 전용) | 높음 |

### 패턴 분류

#### 패턴 A: Platform-Curated (플랫폼 큐레이션형)

**대표 제품**: Salesforce Agentforce (AppExchange), ServiceNow Now Assist (ServiceNow Store), Microsoft Copilot (Power Platform Connector Gallery)

기존에 성숙한 앱 마켓플레이스를 보유한 플랫폼 벤더가, 해당 생태계를 에이전트/스킬 마켓플레이스로 자연스럽게 확장하는 패턴이다. Salesforce는 AppExchange의 7,000개 이상 앱과 MuleSoft API Catalog를 Agentforce Studio에서 에이전트 액션으로 직접 연결한다. ServiceNow는 기존 Store의 앱/플러그인 생태계에 Now Assist Skills와 AI Agents를 추가하며, NASK(Now Assist Skill Kit)을 통해 ISV가 커스텀 스킬을 개발-배포할 수 있게 한다. Microsoft는 1,000개 이상의 Power Platform 커넥터를 Copilot Studio에서 에이전트 도구로 바로 활용한다.

- **장점**: 기존 생태계의 네트워크 효과를 즉시 활용하여 에이전트 마켓플레이스의 초기 콘텐츠 부족(cold start) 문제를 해결. 이미 구축된 벤더 심사/인증/과금 인프라를 재활용. 기존 고객 기반에 자연스러운 업셀 경로 제공
- **단점**: 플랫폼 종속성이 강하여 크로스 플랫폼 에이전트 유통이 제한적. 기존 앱의 에이전트화 전환에 시간이 소요되며, 레거시 통합 방식과 MCP 기반 신규 방식 간 이중 관리 부담 발생. 마켓플레이스 참여를 위해 해당 플랫폼 라이선스가 전제

#### 패턴 B: Open Registry (오픈 레지스트리형)

**대표 제품**: Claude (MCP Server Registry)

프로토콜 창안자로서 오픈소스 커뮤니티 기반의 레지스트리를 운영하며, 누구나 MCP 서버를 등록-발견-연결할 수 있는 개방형 생태계를 구축하는 패턴이다. Anthropic은 2024년 11월 MCP를 오픈소스로 공개하고, 2025년 12월 AAIF에 기증하여 거버넌스를 완전히 중립화했다. Claude Code에서 수백 개의 커뮤니티 MCP 서버에 직접 연결할 수 있으며, 2025년 11월 스펙 업데이트에서 커뮤니티 레지스트리와 서버 아이덴티티를 공식 프리미티브로 추가했다.

- **장점**: 벤더 종속 없이 모든 AI 에이전트 플랫폼에서 활용 가능한 범용 생태계. 커뮤니티 자발 참여로 빠른 도구 확장. 프로토콜 표준화를 통해 에이전트 간 상호운용성 극대화. 진입 장벽이 낮아 개인 개발자부터 대형 벤더까지 참여 가능
- **단점**: 커뮤니티 자율 운영으로 품질 관리(QA), 보안 검증, SLA 보장이 어려움. 엔터프라이즈급 거버넌스(RBAC, 감사 로그, 비용 할당) 기능이 프로토콜 자체에는 부재. 디스커버리(발견)와 신뢰도 평가 메커니즘이 아직 초기 단계

#### 패턴 C: Partner-Certified (파트너 인증형)

**대표 제품**: Workday Assistant (Agent Partner Network)

대형 SI(System Integrator)와 소프트웨어 벤더를 선별적으로 파트너로 등록하고, 파트너가 개발한 에이전트를 자사 플랫폼의 레지스트리(ASOR)에서 인증-등록-관리하는 패턴이다. Workday는 Agent Partner Network에 Accenture, Adobe, AWS, Deloitte, Glean, Google Cloud, IBM, Microsoft, PwC 등 50개 이상 글로벌 파트너를 확보하고, 이들의 에이전트를 ASOR에 "디지털 직원"으로 등록하여 자사 에이전트와 동일한 라이프사이클(채용-온보딩-역할배정-성과추적)로 관리한다.

- **장점**: 파트너 에이전트의 품질과 보안을 사전 인증하여 엔터프라이즈 신뢰도 확보. ASOR을 통한 통합 라이프사이클 관리로 멀티벤더 에이전트의 거버넌스 문제를 구조적으로 해결. 대형 SI 파트너의 컨설팅/구현 역량이 에이전트 채택을 가속화
- **단점**: 파트너 인증 프로세스가 진입 장벽으로 작용하여 생태계 확장 속도가 제한적. 개인 개발자나 소규모 ISV의 참여가 어려워 롱테일(long-tail) 에이전트가 부족. 파트너 네트워크 구축에 상당한 BD(사업 개발) 리소스 필요

#### 패턴 D: Curated Directory (큐레이션 디렉터리형)

**대표 제품**: Glean (MCP Directory + Agent Catalog)

벤더 중립적 플랫폼이 검증된 서드파티 MCP 서버와 프리빌트 에이전트를 선별-큐레이션하여 디렉터리로 제공하는 패턴이다. Glean은 호스팅 MCP 서버로 자사 검색/어시스턴트/에이전트 기능을 외부에 노출하면서, 동시에 20개 이상의 검증된 인기 MCP 서버를 큐레이션하여 자사 에이전트에서 바로 사용할 수 있게 한다. 프리빌트 에이전트 카탈로그도 20개 이상 제공한다.

- **장점**: 품질 검증을 거친 도구만 디렉터리에 포함하여 엔터프라이즈 신뢰도와 사용 편의성 확보. MCP 기반 상호운용성으로 특정 벤더에 종속되지 않는 유연성. 100개 이상 SaaS 커넥터의 기존 데이터 통합 역량과 시너지
- **단점**: 큐레이션 범위가 제한적이어서 롱테일 도구 커버리지 부족. 자체 마켓플레이스 인프라(결제, 리뷰, 버전 관리)가 아직 미비. Glean 플랫폼 외부에서의 디렉터리 활용이 제한적

---

## Key Findings

1. **기존 앱 에코시스템의 "에이전트화 전환율"이 마켓플레이스 경쟁의 핵심 지표가 될 것이다**: Salesforce AppExchange의 7,000개 앱, Microsoft Power Platform의 1,000개 커넥터, ServiceNow Store의 수천 개 앱 중 실제로 에이전트 액션/스킬로 전환된 비율은 아직 초기 단계이다. 그러나 전환이 가속화되면 이 기존 자산이 신규 진입자에 대한 압도적 진입 장벽이 된다. 기존 생태계가 없는 플랫폼은 에이전트 마켓플레이스의 cold start 문제를 다른 방식으로 해결해야 한다 -- *Source*: [[salesforce-agentforce]], [[microsoft-copilot]], [[servicenow-now-assist]]

2. **"스킬 단위"와 "에이전트 단위"의 이중 마켓플레이스 구조가 부상하고 있다**: ServiceNow가 Skills(개별 GenAI 태스크)와 AI Agents(복합 워크플로우)를 명시적으로 분리하고, Salesforce가 Actions(단위 액션)과 Topics(에이전트 역할 범위)를 구분하듯, 마켓플레이스에서 거래되는 단위가 세분화되고 있다. 단위 스킬은 조합의 유연성이 높지만 품질 보증이 어렵고, 완성된 에이전트는 즉시 가치를 제공하지만 커스터마이징이 제한적이다. 성공적인 마켓플레이스는 두 단위를 모두 지원하면서 조합(composition)을 용이하게 하는 설계가 필요하다 -- *Source*: [[servicenow-now-assist]], [[salesforce-agentforce]]

3. **ASOR 모델은 마켓플레이스의 "거버넌스 프리미엄"을 증명하는 최초 사례이다**: Workday의 ASOR는 파트너 에이전트를 자사 에이전트와 동일한 인사 관리 프레임워크(채용-온보딩-역할배정-성과추적-퇴직)로 관리한다. 이는 단순한 앱 스토어를 넘어, 에이전트의 전체 라이프사이클을 통제하는 "관리형 마켓플레이스"의 프로토타입이다. 엔터프라이즈 고객은 에이전트를 "설치"하는 것이 아니라 "고용"하는 멘탈 모델을 가지게 되며, 이 패러다임 전환이 거버넌스 요구사항을 구조적으로 해결한다 -- *Source*: [[workday-assistant]]

4. **MCP의 중립화(AAIF 기증)가 "프로토콜 기반 마켓플레이스"라는 새로운 유통 채널을 열었다**: 기존 마켓플레이스는 플랫폼 벤더가 소유-운영하는 폐쇄형 모델이었으나, MCP가 Linux Foundation 산하 AAIF에 기증되면서 벤더 중립적인 에이전트 도구 유통 채널이 형성되고 있다. Claude의 MCP Server Registry, Glean의 MCP Directory, Copilot Studio의 MCP 네이티브 지원이 이를 증명한다. 이는 기존 플랫폼 벤더의 마켓플레이스 독점에 대한 구조적 도전이며, 에이전트 도구 유통의 "HTTP 모멘트"(웹이 등장하면서 독점 온라인 서비스가 해체된 것과 유사)가 될 수 있다 -- *Source*: [[claude]], [[glean]], [[microsoft-copilot]]

5. **마켓플레이스 과금 모델이 에이전트 시대에 근본적으로 재편되고 있다**: 전통적 앱 마켓플레이스의 시트 기반 과금이 에이전트 소비 기반으로 전환 중이다. Salesforce는 대화당 $2, ServiceNow는 Assist 토큰 소비, Workday는 Flex Credits 모델을 도입했다. 이 소비 기반 과금은 마켓플레이스의 생태계 인센티브 구조를 바꾼다 -- ISV는 "설치 수"가 아닌 "호출 수"에 따라 수익을 얻게 되며, 이는 에이전트/스킬의 실질 사용 품질에 대한 시장 압력을 강화한다 -- *Source*: [[salesforce-agentforce]], [[servicenow-now-assist]], [[workday-assistant]]

6. **ServiceNow의 3계층 구조(Skills -> Agents -> Orchestrator)는 마켓플레이스 조직 원리의 모범 사례이다**: 개별 Skill을 패키징하여 활성화-구성-거버넌스하는 단위(NASK), 이를 조합하여 워크플로우를 자율 수행하는 Agent 단위, 그리고 여러 Agent 팀의 협업을 조율하는 Orchestrator 단위의 3계층은, 마켓플레이스에서 "무엇을 거래할 것인가"에 대한 가장 체계적인 답을 제공한다. 특히 Assist 토큰 예산 관리와 감사 로깅이 Orchestrator에 내장된 점은 마켓플레이스 거버넌스의 벤치마크가 된다 -- *Source*: [[servicenow-now-assist]]

---

## Source References

### 제품 프로필
- [[salesforce-agentforce]] -- AppExchange 생태계, MuleSoft Agent Fabric/API Catalog, Agentforce Studio, Topic-Action 모델, Agentforce Gateway ABAC, 대화당 $2 과금
- [[claude]] -- MCP Server Registry, 커뮤니티 MCP 생태계, AAIF 기증(2025-12), MCP 3가지 프리미티브, 커뮤니티 레지스트리 스펙
- [[microsoft-copilot]] -- 1,000+ Power Platform 커넥터, Copilot Studio MCP 네이티브 지원, Copilot Orchestrator, $30/사용자/월 번들
- [[workday-assistant]] -- ASOR(Agent System of Record), Agent Partner Network(50+ 파트너), Agent Gateway(MCP/A2A), Workday Marketplace, Flowise Agent Builder, Flex Credits 소비 모델
- [[glean]] -- 호스팅 MCP 서버, 20+ 검증 MCP 서버 디렉터리, 프리빌트 에이전트 카탈로그, LangChain Agent Protocol, 100+ SaaS 커넥터
- [[servicenow-now-assist]] -- ServiceNow Store, Now Assist Skills/NASK, AI Agents, AI Agent Orchestrator, Assist 토큰 소비 모델, 3계층 Agentic AI 아키텍처

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [Salesforce AppExchange](https://appexchange.salesforce.com/)
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)
- [Workday Newsroom: Agent Partner Network & Agent Gateway 발표](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
- [Glean Blog: 오픈 에이전트 플랫폼](https://www.glean.com/blog/open-agent-platform)
- [ServiceNow AI Agents 공식 페이지](https://www.servicenow.com/products/ai-agents.html)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
