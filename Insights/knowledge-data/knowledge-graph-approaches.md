---
type: insight-synthesis
topic_id: knowledge-graph-approaches
topic_name: Knowledge Graph 활용 패턴
category: knowledge-data
tags:
- insight
- knowledge-data
- knowledge-graph
- semantic-layer
- entity-graph
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- glean
- databricks-mosaic-ai
- sap-joule
- salesforce-agentforce
- snowflake-intelligence
source_files:
- '[[glean]]'
- '[[databricks-mosaic-ai]]'
- '[[sap-joule]]'
- '[[salesforce-agentforce]]'
- '[[snowflake-intelligence]]'
relevant_roles:
- architecture_agent
- backend_agent
- data_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - knowledge graph
  - semantic layer
  - ontology
  - entity graph
  - graph database
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# Knowledge Graph 활용 패턴

## TL;DR

- **엔터프라이즈 AI 에이전트의 정확도와 개인화 수준은 Knowledge Graph/Semantic Layer의 성숙도에 비례한다**: Glean의 Enterprise Graph, Snowflake의 Semantic Model, Salesforce의 Data Cloud, Databricks의 Unity Catalog, SAP의 BTP 비즈니스 지식 레이어 모두 LLM과 데이터 사이를 중재하는 의미론적 계층을 핵심 인프라로 구축하고 있다
- **Knowledge Graph 접근법은 5가지 패턴으로 분류된다**: (1) Enterprise Knowledge Graph (Glean), (2) YAML 기반 Semantic Model (Snowflake), (3) 실시간 데이터 패브릭 + 벡터 DB (Salesforce Data Cloud), (4) 통합 데이터 카탈로그 (Databricks Unity Catalog), (5) ERP 도메인 내장 지식 (SAP BTP/AI Foundation)
- **"Personal Graph"와 "Enterprise Graph"를 결합하는 이중 구조가 차세대 개인화의 핵심이다**: Glean만이 기업 전체의 지식 그래프 위에 개인별 프로젝트, 협업자, 업무 스타일을 반영하는 Personal Graph를 추가하여, 동일한 질문에도 사용자별로 다른 답변을 생성하는 진정한 개인화를 구현한다
- **Semantic Layer는 "LLM의 할루시네이션 방지 인프라"로 진화하고 있다**: Snowflake의 YAML Semantic Model이 비즈니스 용어-스키마 매핑을 명시적으로 정의하여 텍스트-to-SQL 정확도를 크게 향상시킨 것처럼, 의미론적 계층은 단순 메타데이터 관리를 넘어 LLM의 비즈니스 컨텍스트 이해를 구조적으로 보장하는 핵심 인프라가 되었다
- **거버넌스가 내장된 Knowledge Graph만이 엔터프라이즈에서 채택된다**: 5개 제품 모두 자사 Knowledge Graph/Semantic Layer에 RBAC, 권한 상속, 데이터 리니지 등 거버넌스를 네이티브로 통합하며, 이것이 범용 벡터 DB나 오픈소스 Knowledge Graph 대비 핵심 차별점이다

---

## Context

엔터프라이즈 AI 에이전트를 개발할 때, LLM이 기업 데이터를 정확하고 안전하게 이해하도록 만드는 Knowledge Graph/Semantic Layer 설계는 제품의 답변 품질과 신뢰성을 결정짓는 근본 아키텍처 결정이다. LLM 자체의 역량이 평준화되는 상황에서, 기업 고유의 비즈니스 맥락(조직 구조, 업무 용어, 데이터 관계, 권한 체계)을 얼마나 정밀하게 모델링하느냐가 에이전트 제품의 실질적 차별화 요소로 부상하고 있다.

특히 복잡한 비즈니스 도메인은 복잡한 구조, 다층 엔티티 관계, 도메인 특화 용어 등 일반 LLM이 이해하기 어려운 도메인 특화 지식을 포함한다. 경쟁사들이 Knowledge Graph를 어떤 깊이와 구조로 구현하고 있는지를 비교 분석하면, 자체 Semantic Layer와 Context Graph를 설계할 때 실질적 참고 모델과 아키텍처 방향을 확보할 수 있다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 접근 방식 | 핵심 특징 | 거버넌스 통합 | 개인화 수준 | 성숙도 |
|---------|----------|----------|-------------|-----------|--------|
| [[glean]] | Enterprise Graph (지식 그래프 + Personal Graph) | 사람-콘텐츠-워크플로우-앱 간 동적 관계 모델링, 개인별 Personal Graph로 역할/프로젝트/협업자 반영 | 원본 앱 권한 실시간 상속, 제로 트러스트 | 매우 높음 (개인별 맞춤) | 높음 (GA, 3세대) |
| [[snowflake-intelligence]] | YAML 기반 Semantic Model + Semantic View | Metrics/Dimensions/Facts 구조, 비즈니스 용어-스키마 명시적 매핑, Routing Mode로 멀티도메인 자동 분기 | 행/열 수준 RBAC, MCP Server RBAC | 중간 (역할 기반) | 높음 (GA) |
| [[salesforce-agentforce]] | Data Cloud (실시간 데이터 패브릭 + 벡터 DB) | 구조화/비구조화 데이터 통합, Zero-Copy Partner Network, 고객 프로필 360도 뷰 | ABAC (Agentforce Gateway), 토픽 범위 제한 | 높음 (고객 컨텍스트) | 높음 (3.0 GA) |
| [[databricks-mosaic-ai]] | Unity Catalog (통합 데이터 카탈로그) | 데이터-모델-도구-함수 전체에 걸친 메타데이터/리니지 관리, Vector Search 기반 RAG | Unity Catalog ACL + Lakeguard 샌드박스 | 낮음 (개발자 도구) | 높음 (GA) |
| [[sap-joule]] | SAP BTP + AI Foundation (ERP 도메인 내장 지식) | 2,400+ 스킬에 내장된 비즈니스 프로세스 지식, Collaborative Agent 간 도메인 지식 공유 | SAP 역할 기반 접근, BTP 보안 모델 | 중간 (역할 기반) | 중간 (Joule Studio GA 예정) |

### 패턴 분류

#### 패턴 A: Enterprise Knowledge Graph (엔터프라이즈 지식 그래프)

**대표 제품**: [[glean]]

기업 내 모든 앱, 문서, 대화, 사람, 워크플로우 간의 관계를 동적으로 모델링하는 범용 지식 그래프를 구축한다. Glean의 Enterprise Graph는 100개 이상의 SaaS 커넥터에서 콘텐츠뿐 아니라 메타데이터, 신원 정보, 권한 정보, 활동 데이터까지 수집하여 엔티티 간 관계를 자동으로 추론한다. 여기에 개인별 Personal Graph를 추가하여 각 직원의 프로젝트, 협업자, 업무 스타일까지 반영함으로써, 동일한 검색어에 대해서도 사용자 역할과 맥락에 따라 개인화된 결과를 제공한다.

- **장점**: 가장 풍부한 컨텍스트 모델링, 진정한 개인화, 벤더 중립적 크로스 앱 통합, 권한 실시간 상속으로 보안 모델이 강력
- **단점**: 100개 이상 커넥터 설정과 Enterprise Graph 학습에 초기 구축 시간이 상당, 자체 LLM 부재로 서드파티 모델 의존, 높은 비용(~$50/유저/월 추정)

#### 패턴 B: Semantic Model (의미론적 데이터 모델)

**대표 제품**: [[snowflake-intelligence]]

비즈니스 용어와 데이터베이스 스키마 사이의 매핑을 YAML 등 선언적 형식으로 명시적 정의하여, LLM이 정확한 SQL을 생성하도록 구조적으로 안내한다. Snowflake의 Semantic Model은 Metrics(집계 로직), Dimensions(분석 축), Facts(물리 테이블 매핑)의 3계층 구조로 분석 모델을 정의하며, Semantic View를 통해 Snowsight UI에서 시각적으로 생성하고 관리할 수 있다. Routing Mode는 복수의 Semantic Model 간 자동 분기를 지원하여 멀티도메인 환경을 커버한다.

- **장점**: 텍스트-to-SQL 정확도가 크게 향상, 비즈니스 용어의 명확한 정의로 할루시네이션 최소화, 기존 데이터 웨어하우스 거버넌스(RBAC)를 그대로 활용, Semantic Model Generator로 자동 생성 가능
- **단점**: YAML 기반 수동 정의의 초기 셋업 부담, 비정형 데이터(문서, 대화) 커버리지가 상대적으로 약함, 사람-사람/사람-프로젝트 관계 모델링은 범위 밖

#### 패턴 C: Data Catalog (통합 데이터 카탈로그)

**대표 제품**: [[databricks-mosaic-ai]]

데이터, 모델, 도구, 함수 등 AI 시스템의 모든 구성 요소를 단일 카탈로그에서 메타데이터와 리니지를 추적하고 접근 제어를 적용한다. Databricks의 Unity Catalog는 에이전트가 사용하는 도구를 Unity Catalog 함수로 등록하여 발견과 재사용을 가능하게 하며, 데이터 리니지 추적으로 에이전트의 데이터 접근 경로를 감사할 수 있다. Vector Search와 결합하여 비정형 데이터에 대한 RAG 파이프라인도 지원한다.

- **장점**: 데이터-모델-도구 전체에 걸친 가장 포괄적인 거버넌스, Lakeguard 샌드박스로 에이전트 코드 실행 안전성 보장, MLflow 3.0 통합으로 크로스 플랫폼 관측성, LangChain/LangGraph 등 오픈 프레임워크 호환
- **단점**: 비즈니스 용어-스키마 매핑이 Snowflake Semantic Model 수준으로 명시적이지 않음, 최종 사용자(비기술직)를 위한 셀프서비스 경험 부재, MCP 미지원으로 외부 에이전트 생태계 연결 제한

#### 패턴 D: Context Graph (실시간 컨텍스트 그래프)

**대표 제품**: [[salesforce-agentforce]]

고객 중심의 실시간 데이터 통합 플랫폼을 구축하여, 에이전트가 고객 프로필, 거래 이력, 인터랙션 로그, 외부 데이터를 실시간으로 조합한 360도 컨텍스트를 기반으로 추론한다. Salesforce의 Data Cloud는 구조화/비구조화 데이터를 통합하면서 Zero-Copy Partner Network(Snowflake, Databricks, BigQuery)를 통해 외부 데이터 레이크와 데이터 복제 없이 직접 연결한다. 벡터 데이터베이스로 비구조화 데이터를 임베딩하여 RAG 기반 응답을 생성하며, Atlas Reasoning Engine이 이 통합 컨텍스트를 활용해 숙고형 추론을 수행한다.

- **장점**: 고객 컨텍스트의 깊이와 실시간성이 가장 뛰어남, Zero-Copy로 데이터 중복 없이 외부 소스 연결, CRM 데이터와의 네이티브 통합으로 영업/서비스/마케팅 시나리오에 즉시 활용 가능
- **단점**: Salesforce 플랫폼 종속성이 높음, CRM 중심이라 ERP/HR/공급망 등 비-CRM 도메인 커버리지 제한, Data Cloud + MuleSoft 등 추가 라이선스로 TCO 상승

#### 패턴 E: ERP Domain-Embedded Knowledge (ERP 도메인 내장 지식)

**대표 제품**: [[sap-joule]]

범용 Knowledge Graph를 별도로 구축하는 대신, ERP 시스템 자체에 내장된 비즈니스 프로세스 지식(재무, HR, 구매, 공급망)을 AI 에이전트가 직접 활용하도록 설계한다. SAP Joule의 2,400개 이상 스킬은 SAP 비즈니스 로직과 데이터 모델에 대한 도메인 지식을 내장하고 있으며, Collaborative Agent 아키텍처를 통해 부서/시스템 간 도메인 지식을 자동으로 공유한다. SAP AI Foundation의 350+ AI 기능이 이 도메인 지식 위에서 구동된다.

- **장점**: ERP 비즈니스 프로세스에 대한 가장 깊은 도메인 이해, 별도 Knowledge Graph 구축 없이 즉시 활용 가능, 2,400+ 스킬로 커버리지가 넓음, Collaborative Agent로 크로스 도메인 협업 지원
- **단점**: SAP 에코시스템 외부에서의 활용 불가, S/4HANA Cloud 마이그레이션이 전제, 범용 AI 역량(창의적 글쓰기, 일반 지식)에서 열세, 서드파티 앱 통합이 제한적

---

## Key Findings

1. **Knowledge Graph의 "개인화 깊이"가 제품 차별화의 핵심 축으로 부상하고 있다**: 5개 제품 모두 기업 수준의 지식 구조를 갖추고 있지만, Glean만이 Enterprise Graph 위에 Personal Graph를 추가하여 개인별 프로젝트, 협업자, 업무 패턴까지 반영한다. 이 이중 구조가 94% 태스크 완성도라는 성과의 기반이며, 단순 RBAC 기반 역할별 필터링과는 본질적으로 다른 수준의 개인화를 실현한다 -- *Source*: [[glean]]

2. **Semantic Layer는 "선언적 비즈니스 지식 인코딩"이라는 새로운 인프라 카테고리를 형성하고 있다**: Snowflake의 YAML Semantic Model은 LLM이 SQL을 생성할 때 참조하는 구조화된 비즈니스 메타데이터로, 단순 데이터 딕셔너리를 넘어 집계 로직(Metrics), 분석 축(Dimensions), 물리 매핑(Facts)을 포함한다. 이 접근법은 LLM의 할루시네이션을 구조적으로 방지하는 인프라로서, Snowflake의 Semantic Model Generator가 자동 생성을 지원하면서 채택 장벽을 낮추고 있다 -- *Source*: [[snowflake-intelligence]]

3. **"Knowledge Graph 없는 에이전트"와 "Knowledge Graph 기반 에이전트"의 품질 격차가 명확하다**: Databricks Mosaic AI는 Unity Catalog로 강력한 거버넌스와 도구 관리를 제공하지만, 비즈니스 용어-스키마 간 명시적 매핑(Semantic Layer)이 부재하여 최종 사용자 대상 셀프서비스 NL-to-SQL 경험을 제공하지 못한다. 반면 Snowflake는 Semantic Model 덕분에 비기술 사용자도 자연어로 정확한 데이터 분석이 가능하다. 이는 데이터 카탈로그(메타데이터 거버넌스)와 Semantic Layer(비즈니스 의미 인코딩)가 별개의 인프라임을 보여준다 -- *Source*: [[databricks-mosaic-ai]], [[snowflake-intelligence]]

4. **Zero-Copy 연합 데이터 접근이 Knowledge Graph의 범위를 데이터 사일로 너머로 확장한다**: Salesforce의 Data Cloud가 Snowflake, Databricks, BigQuery 등과 Zero-Copy Partner Network로 연결하여 데이터 복제 없이 외부 데이터 레이크를 실시간으로 참조하는 패턴은, Knowledge Graph가 단일 플랫폼 내부의 데이터에만 국한되지 않고 이종 시스템을 아우르는 연합(federated) 컨텍스트로 진화하고 있음을 보여준다 -- *Source*: [[salesforce-agentforce]]

5. **ERP 도메인 내장 지식은 범용 Knowledge Graph와 보완적 관계이며 대체 관계가 아니다**: SAP Joule의 2,400+ 스킬에 내장된 비즈니스 프로세스 지식은 ERP 트랜잭션 실행에는 탁월하지만, 크로스 앱 검색이나 비정형 문서 이해에는 한계가 있다. 반대로 Glean의 Enterprise Graph는 크로스 앱 검색에 강하지만 ERP 비즈니스 로직의 깊이는 SAP에 미치지 못한다. 이는 엔터프라이즈 에이전트가 도메인 특화 지식과 범용 지식 그래프를 모두 필요로 함을 시사한다 -- *Source*: [[sap-joule]], [[glean]]

---

## Source References

### 제품 프로필
- [[glean]] -- Enterprise Graph(지식 그래프 + Personal Graph) 이중 구조, 100+ SaaS 커넥터 기반 동적 관계 모델링, 원본 권한 실시간 상속, Agentic Engine 2의 94% 태스크 완성도
- [[snowflake-intelligence]] -- YAML 기반 Semantic Model(Metrics/Dimensions/Facts), Semantic View, Cortex Analyst 텍스트-to-SQL, Routing Mode 멀티도메인 분기, Managed MCP Server RBAC
- [[salesforce-agentforce]] -- Data Cloud 실시간 데이터 패브릭, Zero-Copy Partner Network, 벡터 DB 기반 RAG, Atlas Reasoning Engine의 숙고형 추론, Agentforce Gateway ABAC
- [[databricks-mosaic-ai]] -- Unity Catalog 통합 데이터 카탈로그, 데이터-모델-도구-함수 메타데이터/리니지 관리, Lakeguard 샌드박스, Vector Search RAG, Agent Evaluation
- [[sap-joule]] -- 2,400+ Joule 스킬 내장 비즈니스 지식, SAP BTP + AI Foundation, Collaborative Agent 크로스 도메인 협업, Role-Based AI Assistants, A2A 프로토콜

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [Snowflake Cortex Analyst Semantic Model Specification](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec)
- [Snowflake Semantic Model Generator (GitHub)](https://github.com/Snowflake-Labs/semantic-model-generator)
- [Glean Blog: Enterprise Graph & Agentic Engine 2](https://www.glean.com/blog/live-fall-25-main)
- [Databricks Blog: Mosaic AI Compound AI Systems](https://www.databricks.com/blog/mosaic-ai-build-and-deploy-production-quality-compound-ai-systems)
- [SAP News: Joule Agent Architecture](https://community.sap.com/t5/technology-blog-posts-by-sap/how-sap-s-joule-agent-architecture-enables-companies-to-move-to-an-ai/ba-p/14158296)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
