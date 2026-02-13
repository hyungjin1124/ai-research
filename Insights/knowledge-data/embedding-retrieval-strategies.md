---
type: insight-synthesis
topic_id: embedding-retrieval-strategies
topic_name: 임베딩 & 검색 전략
category: knowledge-data
tags:
- insight
- knowledge-data
- embedding
- retrieval
- vector-db
- hybrid-search
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- snowflake-intelligence
- glean
- salesforce-agentforce
- databricks-mosaic-ai
- thoughtspot-spotter
source_files:
- '[[snowflake-intelligence]]'
- '[[glean]]'
- '[[salesforce-agentforce]]'
- '[[databricks-mosaic-ai]]'
- '[[thoughtspot-spotter]]'
relevant_roles:
- backend_agent
- data_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - embedding
  - vector search
  - retrieval strategy
  - dense vector
  - hybrid search
  - semantic search
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 임베딩 & 검색 전략

## TL;DR

- **엔터프라이즈 AI 에이전트의 검색 전략은 4가지 패턴으로 수렴한다**: (1) Dense Vector Search 기반 RAG, (2) Semantic + Lexical 하이브리드 검색, (3) Semantic Model 기반 NL2SQL 구조화 쿼리 생성, (4) Search Token + LLM 결합형 검색. 각 패턴은 데이터 유형(정형/비정형)과 정확도-유연성 트레이드오프에 따라 선택된다
- **시맨틱 모델(Semantic Layer)이 검색 정확도의 결정적 차별 요소로 부상했다**: Snowflake의 YAML Semantic Model, ThoughtSpot의 SpotterModel(AI 자동 생성), Databricks의 Unity Catalog 메타데이터가 각각 다른 방식으로 비즈니스 용어-데이터 스키마 매핑을 구현하며, 이 매핑의 품질이 NL2SQL 및 RAG 정확도를 직접 결정한다
- **하이브리드 검색(Semantic + Lexical)이 엔터프라이즈 비정형 데이터 검색의 사실상 표준이다**: [[glean]]이 시맨틱 검색과 어휘 검색을 결합하여 도메인 특화 약어와 고유 용어를 처리하고, [[snowflake-intelligence]]의 Cortex Search가 임베딩 유사도 매칭과 인덱싱을 결합한 RAG 패턴을 구현한다. 순수 벡터 검색만으로는 엔터프라이즈 도메인 용어의 정밀도를 확보하기 어렵다
- **정형-비정형 데이터 통합 검색이 차세대 에이전트의 핵심 역량이다**: Snowflake Cortex Agent가 Cortex Analyst(정형, NL2SQL)와 Cortex Search(비정형, RAG)를 도구로 결합하고, Salesforce Data Cloud가 벡터 DB에 비구조화 데이터를 인덱싱하여 CRM 정형 데이터와 통합 검색하는 것처럼, 단일 검색 모달리티로는 엔터프라이즈 질문에 완전히 답할 수 없다
- **피드백 루프 기반 검색 품질 지속 개선이 새로운 경쟁 축이다**: [[thoughtspot-spotter]]의 특허 출원 피드백 루프(단어/구문 단위 교정 학습)와 [[databricks-mosaic-ai]]의 Agent Evaluation(AI Judge + 사람 피드백) 등, 검색 결과에 대한 체계적 피드백 수집-학습 메커니즘이 장기적 검색 품질을 결정한다

---

## Context

엔터프라이즈 AI 에이전트가 사용자의 자연어 질문에 정확한 답변을 제공하려면 올바른 데이터를 올바른 방식으로 검색하는 것이 전제 조건이다. 임베딩 전략(어떤 데이터를 어떻게 벡터화하는가), 검색 전략(벡터 검색, 하이브리드 검색, 구조화 쿼리 생성 중 어떤 방식을 언제 선택하는가), 그리고 시맨틱 레이어 설계(비즈니스 용어와 데이터 스키마를 어떻게 매핑하는가)는 에이전트 응답 품질의 80%를 결정하는 인프라 결정이다.

특히 엔터프라이즈 환경에서는 정형 데이터(고객 테이블, 매출 데이터)와 비정형 데이터(고객 문의 이력, 사내 문서, 정책 PDF)가 혼재하므로, 단일 검색 전략으로는 모든 질문에 답할 수 없다. 경쟁사들이 이 문제를 어떤 아키텍처와 패턴으로 해결하고 있는지를 분석하면, 엔터프라이즈 AI 에이전트의 RAG 파이프라인 설계와 시맨틱 레이어 구축에 직접적 설계 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 검색 접근 방식 | 임베딩/벡터 DB | 시맨틱 레이어 | 하이브리드 검색 | 정형+비정형 통합 | 성숙도 |
|---------|-------------|-------------|------------|-------------|--------------|--------|
| [[snowflake-intelligence]] | NL2SQL(Cortex Analyst) + RAG(Cortex Search) | Cortex Search 임베딩 인덱싱 | YAML Semantic Model/View (수동 정의) | 임베딩 유사도 + 인덱싱 결합 | Cortex Agent가 Analyst+Search를 도구로 오케스트레이션 | 높음 (GA) |
| [[glean]] | 시맨틱 + 어휘 하이브리드 검색 | 자체 임베딩 엔진 + Enterprise Graph | Enterprise Graph (지식 그래프 + Personal Graph) | 시맨틱 검색 + 어휘 검색 네이티브 결합 | 100개+ SaaS 커넥터로 정형/비정형 통합 인덱싱 | 높음 (GA) |
| [[salesforce-agentforce]] | Data Cloud 벡터 DB + RAG | Data Cloud 내장 Vector Database | Data Cloud 360 (고객 프로필 + 거래 이력) | 벡터 검색 + CRM 구조화 쿼리 | Zero-Copy Partner Network로 외부 데이터 레이크 직접 연결 | 중간 (3.0 GA) |
| [[databricks-mosaic-ai]] | Vector Search + RAG 파이프라인 | 자체 Vector Search (Unity Catalog 관리 벡터 인덱스) | Unity Catalog (메타데이터 거버넌스 + 데이터 리니지) | 벡터 검색 중심 (하이브리드 미언급) | Agent Framework에서 리트리버+도구 조합으로 구현 | 중간 (GA) |
| [[thoughtspot-spotter]] | Search Token + LLM 하이브리드 NL2SQL | 없음 (외부 데이터 웨어하우스 의존) | SpotterModel (AI 자동 생성 시맨틱 모델) | Search Token(어휘) + LLM(시맨틱) 결합 | Spotter 3에서 Slack/Salesforce 비정형 통합 시작 | 중간 (일부 Preview) |

### 패턴 분류

#### 패턴 A: Dense Vector Search (밀집 벡터 검색)

**대표 제품**: [[databricks-mosaic-ai]], [[salesforce-agentforce]]

비정형 데이터(문서, 이메일, 채팅 로그 등)를 임베딩 모델로 벡터화한 후, 벡터 유사도 검색으로 관련 문서를 검색하여 LLM 컨텍스트에 주입하는 RAG(Retrieval-Augmented Generation) 패턴이다. Databricks는 Unity Catalog에서 관리되는 벡터 인덱스를 기반으로 Vector Search를 제공하며, Salesforce는 Data Cloud에 내장된 Vector Database로 고객 관련 비구조화 데이터를 임베딩하여 의미 기반 검색을 수행한다.

- **장점**: 의미적으로 유사한 문서를 키워드 일치 없이도 검색 가능, 다국어 질의에 자연스럽게 대응, 구현이 상대적으로 단순
- **단점**: 도메인 특화 약어/전문 용어의 정밀도가 낮을 수 있음, 정확한 키워드 매칭이 필요한 경우(코드명, 제품번호 등) 성능 저하, 임베딩 품질에 전적으로 의존

#### 패턴 B: Hybrid Search (시맨틱 + 어휘 결합 검색)

**대표 제품**: [[glean]], [[snowflake-intelligence]] (Cortex Search)

시맨틱 벡터 검색과 전통적 어휘 검색(BM25 등)을 결합하여, 의미적 유사도와 키워드 정확도를 동시에 확보하는 패턴이다. Glean은 이 하이브리드 검색에 Enterprise Graph(지식 그래프 + Personal Graph)를 추가하여 사용자의 역할/팀/프로젝트에 따른 개인화된 검색 결과를 제공한다. Snowflake Cortex Search는 임베딩 기반 유사도 매칭과 인덱싱을 결합한 RAG 패턴으로 비정형 문서에서 인사이트를 추출한다.

- **장점**: 도메인 특화 약어, 고유명사, 제품 코드 등 정확한 매칭이 필요한 케이스와 의미적 유사도가 중요한 케이스를 동시에 처리, 엔터프라이즈 환경의 다양한 질의 유형에 범용적 대응 가능
- **단점**: 시맨틱/어휘 검색 결과의 가중치 조합(fusion) 로직 설계가 복잡, 인덱싱 인프라 이중 관리 필요, 튜닝 파라미터 증가

#### 패턴 C: Structured Query Generation (NL2SQL 기반 구조화 쿼리 생성)

**대표 제품**: [[snowflake-intelligence]] (Cortex Analyst), [[thoughtspot-spotter]]

자연어 질문을 SQL 등 구조화된 쿼리로 변환하여 정형 데이터에서 정확한 답변을 생성하는 패턴이다. 벡터 검색과 근본적으로 다른 접근으로, 비정형 "유사 문서"가 아닌 정확한 수치/집계 결과를 반환한다. Snowflake Cortex Analyst는 YAML Semantic Model을 참조하여 LLM이 정확한 SQL을 생성하고, ThoughtSpot은 고유한 Search Token 아키텍처와 외부 LLM을 결합하여 자연어를 분석 쿼리로 변환한다.

- **장점**: 정형 데이터에 대해 정확한 수치/집계 결과 제공 (벡터 검색으로는 불가능), 결과의 검증 가능성이 높음 (생성된 SQL을 직접 확인 가능), 기존 데이터 웨어하우스 인프라를 그대로 활용
- **단점**: 시맨틱 모델/레이어 구축에 초기 투자 필요 (Snowflake: YAML 수동 작성, ThoughtSpot: AI 자동 생성으로 완화), 비정형 데이터에는 적용 불가, 복잡한 조인/서브쿼리에서 할루시네이션 위험

#### 패턴 D: Semantic Model-Guided Search (시맨틱 모델 가이드 검색)

**대표 제품**: [[snowflake-intelligence]] (Semantic View), [[thoughtspot-spotter]] (SpotterModel), [[databricks-mosaic-ai]] (Unity Catalog)

패턴 A~C를 관통하는 메타 패턴으로, 비즈니스 용어와 데이터 스키마 간의 매핑 레이어(시맨틱 모델)가 검색/쿼리 생성의 정확도를 높이는 가이드 역할을 수행한다. Snowflake의 Semantic View는 Metrics/Dimensions/Facts 구조로 분석 모델을 정의하며, ThoughtSpot의 SpotterModel은 AI가 원시 데이터에서 관계/디멘션/메저를 자동 매핑한다. Databricks의 Unity Catalog는 데이터/모델/도구에 대한 메타데이터 거버넌스를 중앙화하여 에이전트가 올바른 데이터 소스와 도구를 선택하도록 돕는다.

- **장점**: 비즈니스 맥락을 반영한 검색/쿼리 정확도 향상, 할루시네이션 최소화, 거버넌스(접근 제어, 리니지)를 검색 레이어에 통합 가능
- **단점**: 시맨틱 모델 구축/유지보수 비용 (특히 수동 정의 방식), 모델 커버리지 밖의 질문에 대한 폴백 전략 필요, 스키마 변경 시 동기화 부담

---

## Key Findings

1. **정형-비정형 통합 오케스트레이션이 단일 검색 전략보다 중요하다**: Snowflake의 Cortex Agent는 질문 유형에 따라 Cortex Analyst(정형, NL2SQL)와 Cortex Search(비정형, RAG)를 도구로 자동 선택하는 에이전틱 루프를 구현했다. 이는 "매출 트렌드 보여줘"(NL2SQL)와 "지난 분기 전략 보고서 요약해줘"(RAG)를 단일 에이전트가 처리할 수 있게 한다. 단일 검색 전략의 선택보다 복수 전략을 적절히 라우팅하는 오케스트레이션 레이어가 더 결정적이다 -- *Source*: [[snowflake-intelligence]]

2. **시맨틱 모델 자동 생성 vs 수동 정의가 도입 속도와 정확도의 트레이드오프를 결정한다**: Snowflake는 YAML 기반 Semantic Model을 수동으로 정의하여 높은 정확도를 확보하지만 초기 셋업 비용이 크다. 반면 ThoughtSpot의 SpotterModel은 AI가 원시 데이터에서 시맨틱 모델을 자동 생성하여 도입 속도를 크게 단축하되, Human-in-the-Loop 검증으로 품질을 보완한다. Snowflake는 Semantic Model Generator(오픈소스)로 자동 생성도 지원하기 시작했으나, 완전 자동 생성 대비 사람 검증이 포함된 하이브리드 접근이 현실적 최선으로 수렴하고 있다 -- *Source*: [[snowflake-intelligence]], [[thoughtspot-spotter]]

3. **Enterprise Graph가 벡터 검색의 개인화 한계를 극복하는 핵심 레이어다**: Glean의 Enterprise Graph는 단순 벡터 유사도를 넘어, 검색자의 역할/팀/프로젝트/협업 관계를 반영하여 동일한 질의에도 사용자마다 다른 검색 결과를 제공한다. 같은 "Q4 매출 보고서"를 검색해도 영업팀 매니저에게는 파이프라인 보고서를, 재무팀 분석가에게는 재무제표를 우선 반환한다. 순수 벡터 검색은 질의-문서 유사도만 고려하지만, 그래프 기반 개인화는 검색자-문서-조직 관계까지 활용한다 -- *Source*: [[glean]]

4. **벡터 DB를 자사 플랫폼에 내장하는 것이 거버넌스 통합의 전제 조건이다**: Salesforce는 Data Cloud 내장 Vector Database로 벡터 검색에 CRM 수준의 접근 제어를 적용하고, Databricks는 Unity Catalog가 관리하는 벡터 인덱스로 데이터 리니지와 접근 제어를 벡터 검색에 확장한다. Snowflake는 Cortex Search를 보안 경계 내에서 실행하여 행/열 수준 RBAC을 검색 결과에 적용한다. 외부 벡터 DB(Pinecone, Weaviate 등)를 사용하면 거버넌스 레이어가 분리되어 엔터프라이즈 보안 요구사항 충족이 어렵다 -- *Source*: [[salesforce-agentforce]], [[databricks-mosaic-ai]], [[snowflake-intelligence]]

5. **검색 품질의 지속적 개선 메커니즘이 초기 정확도만큼 중요하다**: ThoughtSpot의 특허 출원 피드백 루프는 사용자가 단어/구문 단위로 교정한 내용을 학습하여 도메인 용어 이해도를 지속 개선한다. Databricks의 Agent Evaluation은 AI Judge와 사람 피드백을 결합한 체계적 평가로 검색 품질 회귀를 방지한다. Snowflake는 Semantic Model 편집 후 즉시 테스트 가능한 HITL 패턴으로 모델 품질을 반복 개선한다. 검색 시스템은 "배포 후 완성"이 아니라 "배포 후 시작"이다 -- *Source*: [[thoughtspot-spotter]], [[databricks-mosaic-ai]], [[snowflake-intelligence]]

6. **Zero-Copy 데이터 접근이 벡터 임베딩의 데이터 중복 문제를 해결하는 새로운 접근이다**: Salesforce의 Zero-Copy Partner Network는 Snowflake, Databricks, BigQuery 등 외부 데이터 레이크와 데이터 복제 없이 직접 연결하여, 벡터 임베딩을 위한 별도 데이터 파이프라인 구축 부담을 줄인다. ThoughtSpot 역시 라이브 쿼리 방식으로 데이터 이동 없이 실시간 분석을 수행한다. 이는 데이터 신선도(freshness)와 거버넌스 일관성 측면에서 별도 벡터 DB로의 데이터 복제보다 유리하다 -- *Source*: [[salesforce-agentforce]], [[thoughtspot-spotter]]

---

## Source References

### 제품 프로필
- [[snowflake-intelligence]] -- Cortex Analyst(NL2SQL), Cortex Search(RAG), YAML Semantic Model/View, Cortex Agent 오케스트레이션, 임베딩 기반 유사도 매칭, RBAC 기반 검색 거버넌스
- [[glean]] -- 시맨틱 + 어휘 하이브리드 검색, Enterprise Graph(지식 그래프 + Personal Graph) 기반 개인화, 100개+ SaaS 커넥터 통합 인덱싱, 실시간 권한 동기화
- [[salesforce-agentforce]] -- Data Cloud 내장 Vector Database, RAG 기반 비구조화 데이터 검색, Zero-Copy Partner Network, Atlas Reasoning Engine의 검색 전략 선택
- [[databricks-mosaic-ai]] -- Vector Search(Unity Catalog 관리 벡터 인덱스), Agent Framework의 리트리버 통합, Agent Evaluation의 검색 품질 평가, Lakeguard 샌드박스 실행
- [[thoughtspot-spotter]] -- Search Token + LLM 하이브리드 NL2SQL, SpotterModel AI 자동 생성 시맨틱 모델, 특허 출원 피드백 루프, Drill-Anywhere 탐색

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [Snowflake Cortex Search 문서](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search)
- [Snowflake Cortex Analyst Semantic Model Specification](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec)
- [Databricks Vector Search 문서](https://docs.databricks.com/aws/en/generative-ai/vector-search)
- [Glean 오픈 에이전트 플랫폼](https://www.glean.com/blog/open-agent-platform)
- [ThoughtSpot Spotter Agents](https://www.thoughtspot.com/product/agents)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
