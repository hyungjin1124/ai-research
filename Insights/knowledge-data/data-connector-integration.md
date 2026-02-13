---
type: insight-synthesis
topic_id: data-connector-integration
topic_name: 데이터 커넥터 & 통합 패턴
category: knowledge-data
tags:
- insight
- knowledge-data
- data-connector
- integration
- api-fabric
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- glean
- microsoft-copilot
- salesforce-agentforce
- snowflake-intelligence
- databricks-mosaic-ai
- servicenow-now-assist
source_files:
- '[[glean]]'
- '[[microsoft-copilot]]'
- '[[salesforce-agentforce]]'
- '[[snowflake-intelligence]]'
- '[[databricks-mosaic-ai]]'
- '[[servicenow-now-assist]]'
relevant_roles:
- backend_agent
- data_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - data connector
  - API integration
  - zero-copy
  - data federation
  - ETL pipeline
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 데이터 커넥터 & 통합 패턴

## TL;DR

- **엔터프라이즈 AI 에이전트의 데이터 통합은 5가지 패턴으로 수렴한다**: (1) Native SaaS Connectors -- 사전 구축된 SaaS 앱 커넥터로 빠른 연결, (2) API Fabric/Gateway -- 중앙화된 API 관리 레이어를 통한 외부 시스템 연결, (3) Zero-Copy Federation -- 데이터 이동 없이 원본 위치에서 직접 쿼리, (4) MCP-Based Integration -- 표준 프로토콜 기반의 양방향 도구/데이터 노출, (5) Custom Connector SDK -- 개발자가 직접 구축하는 프로그래밍 방식 커넥터
- **데이터 통합 전략은 "커넥터 수(breadth)"에서 "거버넌스 깊이(depth)"로 경쟁축이 이동하고 있다**: [[glean]]의 100개 이상 SaaS 커넥터, [[microsoft-copilot]]의 1,000개 이상 Power Platform 커넥터 등 커넥터 수 확보는 이미 포화 상태에 진입했으며, [[snowflake-intelligence]]의 행/열 수준 RBAC 적용이나 [[salesforce-agentforce]]의 Agentforce Gateway(Envoy 기반 ABAC) 등 거버넌스 품질이 새로운 차별화 요소로 부상
- **Zero-Copy Federation이 데이터 중복 문제의 해결책으로 급부상한다**: [[salesforce-agentforce]]의 Zero-Copy Partner Network(Snowflake, Databricks, BigQuery 연결)가 대표 사례이며, 데이터 복제 비용과 일관성 문제를 근본적으로 해소. [[snowflake-intelligence]]는 자사 보안 경계 내 처리를 통해 유사한 효과를 달성
- **MCP 기반 통합이 기존 커넥터 패러다임을 보완하되 대체하지는 못한다**: [[snowflake-intelligence]]의 Managed MCP Server와 [[glean]]의 호스팅 MCP 서버가 외부 에이전트와의 표준 연결을 제공하지만, [[microsoft-copilot]]과 [[salesforce-agentforce]]는 자사 독자 커넥터 체계(Power Platform, MuleSoft)를 MCP와 병행 유지하여 완전한 대체는 아직 발생하지 않음
- **커넥터 프레임워크의 메타데이터 수집 범위가 AI 에이전트의 응답 품질을 직접 결정한다**: [[glean]]의 커넥터가 콘텐츠뿐 아니라 권한 정보, 활동 데이터, 신원 정보까지 수집하여 Enterprise Graph를 구축하는 반면, 단순 데이터 동기화만 수행하는 커넥터는 에이전트의 개인화와 권한 준수에 한계를 보인다

---

## Context

엔터프라이즈 AI 에이전트 제품을 개발할 때, 고객의 기존 데이터 소스(ERP, CRM, 데이터 웨어하우스, SaaS 앱 등)와 어떻게 연결하느냐는 제품의 실질적 가치와 도입 가능성을 결정짓는 최우선 아키텍처 결정이다. 에이전트가 아무리 뛰어난 추론 능력을 갖추더라도, 관련 데이터에 접근하지 못하면 비즈니스 가치를 생성할 수 없다.

특히 엔터프라이즈 환경에서는 단순 "연결" 이상의 요구사항이 존재한다. 원본 시스템의 권한 체계를 상속해야 하고, 데이터 복제 비용을 최소화해야 하며, 감사 추적이 가능해야 하고, 커넥터 장애가 에이전트 전체 서비스에 영향을 주지 않아야 한다. 경쟁사들이 이러한 요구사항을 어떤 패턴으로 해결하고 있는지를 분석하면, 엔터프라이즈 AI 에이전트 데이터 통합 아키텍처 설계에 직접적 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 통합 접근 방식 | 커넥터 규모 | 거버넌스 수준 | MCP 통합 | Zero-Copy | 성숙도 |
|---------|--------------|-----------|-------------|---------|-----------|--------|
| [[glean]] | Native SaaS Connectors + Indexing API + MCP Server | 100개+ SaaS 앱 | 원본 권한 실시간 상속, 싱글 테넌시 | 호스팅 MCP 서버 (양방향) | 미지원 (인덱싱 기반) | 높음 (GA) |
| [[microsoft-copilot]] | Power Platform 커넥터 + Microsoft Graph + MCP | 1,000개+ 커넥터 | Microsoft Entra 기반 인증, Copilot Orchestrator | F&O MCP Server + Copilot Studio 네이티브 | 비동기 Dual-Write | 높음 (GA) |
| [[salesforce-agentforce]] | MuleSoft Agent Fabric + Data Cloud + Zero-Copy | MuleSoft API Catalog (광범위) | Agentforce Gateway (Envoy ABAC), 토픽 범위 제한 | 3.0부터 내장 | Zero-Copy Partner Network (Snowflake, Databricks, BigQuery) | 중간 (3.0 GA) |
| [[snowflake-intelligence]] | Managed MCP Server + REST API + 보안 경계 내 처리 | 자사 데이터 플랫폼 내 테이블/뷰 | 행/열 RBAC, MCP Server RBAC, 보안 경계 | Managed MCP Server (양방향) | 자체 보안 경계 내 처리 (이동 불필요) | 중간 (GA) |
| [[databricks-mosaic-ai]] | Unity Catalog 함수 + LangChain 통합 + AI Gateway | Unity Catalog 등록 도구/함수 | Unity Catalog + Lakeguard 샌드박스 | 미지원 | Delta Sharing (외부 데이터 공유) | 중간 (GA) |
| [[servicenow-now-assist]] | Now Platform 네이티브 + REST API + 전용 커넥터 | Now Platform 내장 (ITSM/CSM/HRSD) + Store 앱 | Orchestrator 토큰 예산, 역할 기반 접근 제어, 감사 로깅 | 미지원 | 미지원 | 중간 (GA) |

### 패턴 분류

#### 패턴 A: Native SaaS Connectors (네이티브 SaaS 커넥터)

**대표 제품**: [[glean]], [[microsoft-copilot]]

사전 구축된 커넥터를 통해 주요 SaaS 앱(Google Workspace, Microsoft 365, Slack, Salesforce, Jira 등)에 직접 연결하고, 데이터를 자사 플랫폼으로 인덱싱하여 검색·분석에 활용하는 패턴이다. [[glean]]은 100개 이상의 SaaS 커넥터로 콘텐츠뿐 아니라 메타데이터, 권한 정보, 활동 데이터까지 수집하여 Enterprise Graph를 구축한다. [[microsoft-copilot]]은 1,000개 이상의 Power Platform 커넥터로 SAP, ServiceNow 등 비-Microsoft 시스템까지 광범위하게 연결한다.

- **장점**: 설정이 간단하고 즉시 사용 가능(plug-and-play), 벤더가 커넥터 유지보수를 담당하므로 고객 부담 최소, 광범위한 SaaS 생태계 커버리지
- **단점**: 데이터 복제 비용 발생(인덱싱 기반), 원본 데이터와의 동기화 지연 가능, 커넥터 미지원 시스템에 대한 사각지대 존재, 커스텀 온프레미스 시스템 연결 제한

#### 패턴 B: API Fabric/Gateway (API 패브릭/게이트웨이)

**대표 제품**: [[salesforce-agentforce]], [[microsoft-copilot]]

중앙화된 API 관리 레이어를 두고, 외부 시스템의 API를 에이전트가 직접 호출할 수 있는 도구(Action)로 변환하는 패턴이다. [[salesforce-agentforce]]는 MuleSoft Agent Fabric을 통해 외부 API를 Agentforce의 Topic-Action 모델에 매핑하고, Agentforce Gateway(Envoy 기반)로 ABAC, 할당량 제한, 인증/인가를 중앙 관리한다. [[microsoft-copilot]]은 Copilot Orchestrator가 Power Platform 커넥터와 MCP 도구를 통합 오케스트레이션한다.

- **장점**: 기존 엔터프라이즈 API 자산을 재활용, 실시간 데이터 접근(데이터 복제 불필요), 중앙화된 거버넌스(인증, 할당량, 감사)로 보안 통제 용이
- **단점**: MuleSoft, Power Platform 등 별도 미들웨어 라이선스 필요, API 설계/관리 전문 인력 요구, 게이트웨이 레이어 추가로 레이턴시 증가 가능, 벤더 종속성 잔존

#### 패턴 C: Zero-Copy Federation (제로카피 페더레이션)

**대표 제품**: [[salesforce-agentforce]], [[snowflake-intelligence]]

데이터를 물리적으로 복제하지 않고 원본 위치에서 직접 쿼리하는 패턴이다. [[salesforce-agentforce]]의 Data Cloud는 Zero-Copy Partner Network를 통해 Snowflake, Databricks, Google BigQuery의 데이터를 복제 없이 연결하며, 에이전트가 실시간으로 외부 데이터 레이크에 접근한다. [[snowflake-intelligence]]는 모든 처리를 자사 보안 경계 내에서 수행하여 데이터 이동 자체를 불필요하게 만든다.

- **장점**: 데이터 복제 비용 제거, 원본-복제본 간 일관성 문제 해소, 데이터 거버넌스를 원본 시스템에서 유지 가능, 대용량 데이터 처리에 효율적
- **단점**: 원본 시스템의 가용성/성능에 직접 의존, 네트워크 레이턴시로 인한 응답 지연 가능, Zero-Copy 파트너 네트워크 외 시스템은 커버 불가, 크로스 플랫폼 쿼리 최적화 복잡

#### 패턴 D: MCP-Based Integration (MCP 기반 통합)

**대표 제품**: [[snowflake-intelligence]], [[glean]], [[microsoft-copilot]]

Model Context Protocol을 통해 자사 데이터/기능을 표준화된 MCP 도구로 외부 에이전트에 노출하거나, 외부 MCP 서버의 도구를 자사 에이전트가 소비하는 패턴이다. [[snowflake-intelligence]]는 Managed MCP Server로 Cortex Analyst/Search를 외부에 노출하면서 RBAC를 적용한다. [[glean]]은 호스팅 MCP 서버로 검색/어시스턴트/에이전트를 노출하고, 20개 이상의 검증된 MCP 서버 디렉터리도 큐레이션한다. [[microsoft-copilot]]은 Copilot Studio에서 MCP를 네이티브 지원하고 F&O MCP Server를 통해 ERP 데이터를 MCP 도구로 직접 노출한다.

- **장점**: 업계 표준 프로토콜로 벤더 종속 최소화, 서버/클라이언트 양방향 구현으로 생태계 허브 포지셔닝 가능, 별도 인프라 배포 불필요(Managed MCP Server), 기존 거버넌스(RBAC)를 MCP 레이어에 적용 가능
- **단점**: 아직 초기 단계로 엔터프라이즈급 보안/감사/과금 요구사항을 완전히 충족하지 못함, 독자 커넥터 체계와의 이중 관리 부담, MCP 프로토콜 진화에 대한 주도권 부재 시 종속 위험

#### 패턴 E: Custom Connector SDK (커스텀 커넥터 SDK)

**대표 제품**: [[glean]], [[databricks-mosaic-ai]]

개발자가 프로그래밍 방식으로 커스텀 데이터 소스를 연결할 수 있는 SDK/API를 제공하는 패턴이다. [[glean]]은 Indexing API를 통해 커스텀 데이터 소스의 콘텐츠, 메타데이터, 권한 정보, 활동 데이터를 프로그래밍 방식으로 수집한다. [[databricks-mosaic-ai]]는 Unity Catalog 함수로 외부 API, SQL 쿼리, Python 함수를 에이전트 도구로 등록하며, LangChain/LangGraph와 호환되는 `databricks-langchain` 패키지를 제공한다.

- **장점**: 커넥터 미지원 시스템이나 커스텀 온프레미스 시스템에 대한 유연한 연결, 메타데이터 수집 범위를 개발자가 직접 제어, 기존 코드 자산(Python, LangChain 등) 재활용 가능
- **단점**: 개발/유지보수 비용이 고객에게 전가, 데이터 엔지니어/ML 엔지니어 인력 필요, 커넥터 품질이 구현자 역량에 의존, 대규모 커넥터 관리 시 복잡성 증가

---

## Key Findings

1. **커넥터의 "메타데이터 수집 깊이"가 에이전트 품질을 결정짓는 숨은 변수이다**: [[glean]]의 커넥터는 콘텐츠뿐 아니라 권한 정보, 활동 데이터(누가 언제 어떤 문서를 편집했는지), 신원 정보(조직 구조, 역할)까지 수집하여 Enterprise Graph + Personal Graph를 구축한다. 이 깊은 메타데이터가 검색 결과 개인화와 권한 준수의 기반이 된다. 반면 단순 콘텐츠 동기화만 수행하는 커넥터는 "누가 이 데이터를 볼 수 있는가"를 판단할 수 없어 엔터프라이즈 환경에서 보안 사고 위험이 있다 -- *Source*: [[glean]]

2. **API Fabric 패턴과 MCP 패턴은 경쟁이 아닌 보완 관계로 공존하고 있다**: [[salesforce-agentforce]]는 MuleSoft Agent Fabric(API Fabric)과 MCP를 동시에 지원하고, [[microsoft-copilot]]은 1,000개 이상의 Power Platform 커넥터 체계와 MCP 네이티브 지원을 병행한다. 이는 MCP가 "범용 표준 연결"을, API Fabric이 "깊은 비즈니스 로직 통합"을 각각 담당하는 역할 분담 구조가 형성되고 있음을 시사한다. 두 패턴을 양립시키지 않으면 광범위한 커넥터 수요와 고급 거버넌스 요구를 동시에 충족하기 어렵다 -- *Source*: [[salesforce-agentforce]], [[microsoft-copilot]]

3. **Zero-Copy Federation이 대용량 데이터 통합의 게임 체인저로 부상하되, 적용 범위는 제한적이다**: [[salesforce-agentforce]]의 Zero-Copy Partner Network는 Snowflake, Databricks, BigQuery와의 데이터 복제 비용을 제거하고 실시간성을 확보하는 혁신적 접근이다. 그러나 Zero-Copy 연결이 가능한 파트너가 대형 데이터 플랫폼에 한정되어 있으며, 중소규모 SaaS 앱이나 레거시 온프레미스 시스템에는 적용되지 않는다. 이로 인해 Zero-Copy는 "전략적 데이터 소스"에 대한 선택적 패턴으로 자리잡고, "롱테일 데이터 소스"에는 여전히 커넥터/API 패턴이 필요하다 -- *Source*: [[salesforce-agentforce]], [[snowflake-intelligence]]

4. **MCP 미지원 제품([[databricks-mosaic-ai]], [[servicenow-now-assist]])은 에이전트 간 상호운용성에서 불리해지고 있다**: [[databricks-mosaic-ai]]는 Unity Catalog 함수와 LangChain 통합으로 자체 생태계 내 도구 연결은 강력하지만, 외부 AI 에이전트(Claude, GPT 등)가 Databricks 데이터에 표준화된 방식으로 접근하는 경로가 없다. [[servicenow-now-assist]] 역시 REST API와 전용 커넥터에 의존하며 MCP/A2A를 공식 지원하지 않는다. MCP가 업계 표준으로 자리잡아가면서, 이 두 제품은 상호운용성 측면에서 [[snowflake-intelligence]], [[glean]] 대비 열세에 놓인다 -- *Source*: [[databricks-mosaic-ai]], [[servicenow-now-assist]]

5. **거버넌스 레이어의 위치(게이트웨이 vs. 데이터 플랫폼 내장)가 통합 아키텍처의 복잡도를 결정한다**: [[salesforce-agentforce]]는 Agentforce Gateway를 별도 구축하여 MCP/API 호출에 ABAC를 적용하는 "게이트웨이 방식"을, [[snowflake-intelligence]]는 기존 행/열 RBAC를 MCP Server에 그대로 적용하는 "플랫폼 내장 방식"을 택한다. 게이트웨이 방식은 이종 시스템에 일관된 정책을 적용할 수 있지만 관리 복잡도가 높고, 플랫폼 내장 방식은 관리가 단순하지만 자사 플랫폼 외부 데이터에 대한 거버넌스 확장이 어렵다 -- *Source*: [[salesforce-agentforce]], [[snowflake-intelligence]]

6. **Semantic Layer가 데이터 커넥터와 AI 에이전트 사이의 핵심 중간 계층으로 부상한다**: [[snowflake-intelligence]]의 YAML 기반 Semantic Model/Semantic View와 [[glean]]의 Enterprise Graph는 모두 원시 데이터 스키마를 비즈니스 용어로 번역하는 의미론적 중간 계층이다. 이 계층이 없으면 에이전트의 텍스트-to-SQL 정확도가 크게 하락하고 할루시네이션이 증가한다. 커넥터가 "데이터를 가져오는" 역할이라면, Semantic Layer는 "데이터를 이해시키는" 역할로서 동등한 중요도를 갖는다 -- *Source*: [[snowflake-intelligence]], [[glean]]

---

## Source References

### 제품 프로필
- [[glean]] -- 100개+ SaaS 커넥터, Indexing API, Enterprise Graph(지식 그래프 + Personal Graph), 호스팅 MCP 서버, 원본 권한 실시간 상속 모델
- [[microsoft-copilot]] -- 1,000개+ Power Platform 커넥터, Microsoft Graph + Dataverse, Copilot Orchestrator, F&O MCP Server, 비동기 Dual-Write
- [[salesforce-agentforce]] -- MuleSoft Agent Fabric, Agentforce Gateway(Envoy ABAC), Data Cloud Zero-Copy Partner Network, Topic-Action 모델, MCP 3.0 내장
- [[snowflake-intelligence]] -- Managed MCP Server, Cortex Analyst Semantic Model/View, 행/열 RBAC, 보안 경계 내 처리, YAML 기반 메타데이터 정의
- [[databricks-mosaic-ai]] -- Unity Catalog 함수 등록, Lakeguard 샌드박스, AI Gateway, LangChain/LangGraph 통합, MCP 미지원
- [[servicenow-now-assist]] -- Now Platform 네이티브 통합, REST API/전용 커넥터, AI Agent Orchestrator 토큰 예산, Skills -> Agents -> Orchestrator 3계층

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [Snowflake Managed MCP Server 문서](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
- [Salesforce Architects: MuleSoft로 Agentic Enterprise 구축](https://architect.salesforce.com/fundamentals/mulesoft-architecting-agentic-enterprise)
- [Glean 커넥터 목록](https://www.glean.com/connectors)
- [Glean Developer Platform](https://developers.glean.com/)
- [Microsoft Learn: Copilot for Finance and Operations Overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
