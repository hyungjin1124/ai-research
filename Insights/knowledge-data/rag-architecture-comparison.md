---
type: insight-synthesis
topic_id: rag-architecture-comparison
topic_name: 경쟁사 RAG 아키텍처 비교 분석
category: knowledge-data
tags:
- insight
- knowledge-data
- RAG
- data-architecture
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- snowflake-intelligence
- glean
- salesforce-agentforce
- sap-joule
- databricks-mosaic-ai
- servicenow-now-assist
source_files:
- '[[snowflake-intelligence]]'
- '[[glean]]'
- '[[salesforce-agentforce]]'
- '[[sap-joule]]'
- '[[databricks-mosaic-ai]]'
- '[[servicenow-now-assist]]'
- '[[Research_v4.1_Context Graphs]]'
relevant_roles:
- backend_agent
- data_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - RAG architecture
  - retrieval augmented generation
  - semantic layer enterprise AI
  - knowledge graph RAG
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 경쟁사 RAG 아키텍처 비교 분석

## TL;DR

- 경쟁사 RAG 아키텍처는 **Semantic Layer 중심**(Snowflake, Databricks), **Knowledge Graph 중심**(Glean), **CRM/ERP 네이티브 데이터 통합 중심**(Salesforce, SAP, ServiceNow)의 3가지 패턴으로 분류된다
- Semantic Layer 접근은 정형 데이터 정확도에서 강점을 보이지만 비정형 데이터 통합에 한계가 있고, Knowledge Graph 접근은 관계 기반 검색에서 탁월하지만 구축 복잡성이 높으며, 네이티브 통합 접근은 도메인 특화 Grounding에 유리하지만 플랫폼 종속성이 강하다
- Vector DB는 모든 경쟁사가 채택한 공통 인프라이나, 이를 **어떤 Semantic/Knowledge Layer 위에 배치하느냐**가 RAG 품질의 핵심 차별화 요소이다
- Grounding 전략은 YAML Semantic Model(Snowflake), Enterprise Graph(Glean), Data Cloud + Zero-Copy(Salesforce), Knowledge Catalog(SAP), Unity Catalog(Databricks), Now Platform CMDB(ServiceNow) 등 각사의 기존 데이터 자산을 최대한 활용하는 방향으로 설계되어 있다

---

## Overview

RAG(Retrieval-Augmented Generation)는 엔터프라이즈 AI 에이전트의 핵심 아키텍처 패턴으로, LLM의 hallucination을 줄이고 기업 고유 데이터에 기반한 정확한 응답을 생성하기 위해 필수적이다 [^1]. 경쟁사들이 RAG를 어떻게 구현하는지 -- 데이터 레이어 설계, 의미론적/지식 레이어 구조, 검색 전략, Vector DB 활용, Grounding 방식, 엔터프라이즈 데이터 통합 -- 를 체계적으로 비교 분석하는 것은 아키텍처 의사결정의 핵심 근거가 된다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 데이터 레이어 | Semantic/Knowledge Layer | 검색 전략 | Vector DB | Grounding 방식 | 엔터프라이즈 데이터 통합 | 성숙도 | Source |
|---------|-------------|------------------------|----------|-----------|---------------|---------------------|--------|--------|
| **Snowflake Intelligence** | Snowflake Data Cloud (정형+비정형) | YAML Semantic Model + Semantic View (Metrics/Dimensions/Facts) | Cortex Analyst(NL-to-SQL) + Cortex Search(임베딩 유사도) 이중 경로 | Cortex Search 내장 임베딩 인덱스 | Semantic Model이 비즈니스 용어-스키마 매핑으로 SQL 정확도 보장 | 플랫폼 네이티브 (Snowflake 내 데이터만 대상) | GA (2025-11) | [^1] |
| **Glean** | 100+ SaaS 커넥터 기반 분산 데이터 수집 | Enterprise Graph (Knowledge Graph + Personal Graph) | 시맨틱 + 어휘 하이브리드 검색, 개인화 랭킹 | 자체 임베딩 인덱스 (실시간 인덱싱) | Enterprise Graph가 사용자 역할/팀/프로젝트 맥락으로 결과 개인화 | 벤더 중립 크로스 SaaS 통합 (메타데이터+권한+활동 수집) | GA (2022~) | [^2] |
| **Salesforce Agentforce** | Data Cloud (구조화+비구조화 통합) | Data Cloud 프로필 + Zero-Copy Partner Network | Atlas Engine이 Data Cloud에서 실시간 RAG 검색 수행 | Data Cloud 내장 Vector Database | CRM 객체(고객/기회/케이스) 기반 비즈니스 컨텍스트 Grounding | CRM 네이티브 + MuleSoft API Fabric + Zero-Copy (Snowflake, Databricks, BigQuery) | GA (2024-10~) | [^3] |
| **SAP Joule** | SAP BTP + S/4HANA Cloud 비즈니스 데이터 | Knowledge Catalog + 도메인 특화 비즈니스 로직 | Agentic Orchestration 기반 멀티스텝 검색 | SAP AI Core 내 벡터 검색 | 2,400+ Joule Skills이 SAP 도메인 지식으로 직접 Grounding | SAP 에코시스템 네이티브 (S/4HANA, SuccessFactors, Ariba, Concur) | GA (2024~) | [^4] |
| **Databricks Mosaic AI** | Lakehouse (Delta Lake 기반 정형+비정형) | Unity Catalog (메타데이터 거버넌스 + 도구/함수 레지스트리) | Vector Search 기반 RAG + Unity Catalog 함수 호출 | Mosaic AI Vector Search (벡터 인덱스) | Unity Catalog에 등록된 도구/데이터/모델에 대한 거버넌스 기반 Grounding | Lakehouse 네이티브 + LangChain/LangGraph 프레임워크 호환 | GA (2025) | [^5] |
| **ServiceNow Now Assist** | Now Platform CMDB + 지식 베이스 | Now Platform 워크플로우 데이터 모델 + 도메인별 지식 문서 | AI Search 기반 Skill/Agent 동적 발견 + Genius Results (다문서 합성) | 플랫폼 내장 검색 인덱스 | ITSM/CSM/HRSD 도메인 워크플로우 데이터에 직접 Grounding | Now Platform 네이티브 + REST API 외부 연동 | GA (2023-09~) | [^6] |

### 패턴 분류

#### 패턴 A: Semantic Layer 중심 RAG

**대표 제품**: Snowflake Intelligence, Databricks Mosaic AI

이 패턴은 데이터 플랫폼 위에 명시적인 Semantic Layer를 구축하여 LLM이 비즈니스 맥락을 이해하도록 하는 접근이다. Snowflake는 YAML 기반 Semantic Model로 테이블/컬럼/관계/비즈니스 설명을 정의하고, Databricks는 Unity Catalog로 데이터/모델/도구/함수의 메타데이터를 중앙 관리한다 [^1] [^5].

- **장점**: 정형 데이터에 대한 높은 쿼리 정확도, 비즈니스 용어와 데이터 스키마 간 명확한 매핑으로 hallucination 최소화, 데이터 거버넌스(RBAC, 리니지)가 자연스럽게 적용됨
- **단점**: Semantic Model/Catalog 초기 구축 부담이 큼(Snowflake의 YAML 수동 정의, Databricks의 Unity Catalog 설정), 비정형 데이터 통합은 별도 파이프라인(Cortex Search, Vector Search)으로 분리되어 정형-비정형 간 통합 검색 경험이 제한적
- **RAG 흐름**: `자연어 질문 → Semantic Layer 참조 → SQL 생성(정형) 또는 벡터 검색(비정형) → 결과 합성`

#### 패턴 B: Knowledge Graph 중심 RAG

**대표 제품**: Glean

이 패턴은 기업 내 사람/콘텐츠/워크플로우/앱 간의 관계를 동적으로 모델링하는 Knowledge Graph를 RAG의 핵심 인프라로 활용한다. Glean의 Enterprise Graph는 조직 수준의 Knowledge Graph에 개인별 Personal Graph를 추가하여 이중 구조를 형성한다 [^2].

- **장점**: 관계 기반 검색으로 단순 키워드/벡터 매칭을 넘어선 맥락적 검색 가능, Personal Graph 기반 개인화로 동일 질문에도 사용자 역할/프로젝트에 맞춘 차별화된 결과 제공, 100+ SaaS 앱의 크로스 소스 통합
- **단점**: Knowledge Graph 구축 및 실시간 업데이트에 높은 인프라 비용, 100개+ 커넥터 설정/권한 매핑/Graph 학습에 초기 구축 시간 소요, 정형 데이터(SQL 쿼리)에 대한 정밀 분석에서 Semantic Layer 대비 약함
- **RAG 흐름**: `자연어 질문 → Enterprise Graph에서 관계 탐색 + 벡터 유사도 검색 → 개인화 랭킹 → 출처 포함 응답 합성`

#### 패턴 C: 플랫폼 네이티브 데이터 통합 RAG

**대표 제품**: Salesforce Agentforce, SAP Joule, ServiceNow Now Assist

이 패턴은 기존 비즈니스 플랫폼(CRM, ERP, ITSM)의 데이터 모델과 비즈니스 로직을 RAG의 Grounding 소스로 직접 활용한다. 별도의 Semantic Layer나 Knowledge Graph를 구축하는 대신, 플랫폼에 이미 존재하는 구조화된 비즈니스 객체(고객 프로필, 거래 이력, 인시던트, 구매 주문 등)를 검색 대상으로 삼는다 [^3] [^4] [^6].

- **장점**: 초기 셋업 비용 최소화(기존 데이터 구조를 그대로 활용), 도메인 특화 Grounding으로 비즈니스 프로세스에 대한 높은 정확도, 플랫폼 내 거버넌스/워크플로우와 자연스러운 통합
- **단점**: 강한 플랫폼 종속성(Salesforce, SAP, ServiceNow 에코시스템 외부 데이터 접근 제한), 크로스 플랫폼 검색이 어려움, 범용 지식 검색에서 Knowledge Graph 대비 약함
- **RAG 흐름**: `자연어 질문 → 플랫폼 추론 엔진(Atlas/Agentic Orchestration)이 비즈니스 객체 검색 + 벡터 DB 검색 → 도메인 비즈니스 로직 적용 → 응답 합성`

---

## Key Findings

1. **Semantic Layer와 Knowledge Graph의 수렴 추세**: Snowflake의 Semantic View가 비즈니스 용어-스키마 매핑에서 점차 관계 모델링으로 확장하고, Glean의 Enterprise Graph가 Personal Graph로 개인화를 추가하는 등, 두 패턴이 서로의 약점을 보완하며 수렴하고 있다. 장기적으로 Semantic Layer + Knowledge Graph의 하이브리드가 표준이 될 가능성이 높다 [^1] [^2]

2. **Vector DB는 commodity화, 차별화는 그 위의 레이어에서 발생**: 6개 경쟁사 모두 벡터 임베딩 기반 유사도 검색을 사용하고 있으나, RAG 품질의 차이는 Vector DB 자체가 아니라 그 위의 Semantic/Knowledge/Business Logic Layer에서 결정된다. Snowflake의 Semantic Model이 SQL 정확도를 높이고, Glean의 Enterprise Graph가 개인화 랭킹을 가능하게 하며, Salesforce의 CRM 객체가 비즈니스 컨텍스트를 제공하는 것이 그 예다 [^1] [^2] [^3]

3. **Zero-Copy/권한 상속 패턴의 부상**: Salesforce의 Zero-Copy Partner Network(Snowflake, Databricks, BigQuery 데이터를 복제 없이 직접 연결)와 Glean의 원본 앱 권한 실시간 상속 모델은, 데이터를 이동시키지 않고 제자리에서 RAG를 수행하는 트렌드를 보여준다. 이는 데이터 거버넌스와 비용 효율 양면에서 중요한 아키텍처 결정이다 [^3] [^2]

4. **Grounding 전략의 양극화: 정형 우선 vs 비정형 우선**: Snowflake/Databricks는 정형 데이터(SQL)에서 출발하여 비정형(문서 검색)을 보조적으로 추가하는 반면, Glean/ServiceNow는 비정형 데이터(문서, 메시지, 지식 베이스)에서 출발하여 구조화된 메타데이터를 보조적으로 활용한다. Salesforce와 SAP는 CRM/ERP 비즈니스 객체를 중심으로 정형-비정형을 균형 있게 통합한다 [^1] [^5] [^2] [^6]

5. **에이전트 오케스트레이션이 RAG 검색 전략을 결정**: 단순한 단일 검색이 아니라, 에이전트가 질문을 분석하고 검색 계획을 수립하여 복수의 데이터 소스와 검색 방법을 동적으로 조합하는 "Agentic RAG" 패턴이 표준으로 자리잡고 있다. Snowflake의 Cortex Agent, Salesforce의 Atlas Engine, SAP의 Agentic Orchestration, ServiceNow의 AI Agent Orchestrator 모두 이 패턴을 구현한다 [^1] [^3] [^4] [^6]

6. **"왜(Why)" 설명 능력이 다음 경쟁 전선**: 현재 경쟁사 RAG는 대부분 "무엇(What)"에 답하는 수준이다(매출 수치, 인시던트 현황, 고객 프로필). 인과관계와 의사결정 근거를 추적하여 "왜(Why)"에 답하는 RAG는 아직 경쟁사 중 본격적으로 구현한 사례가 없다 [^7]

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|

---

## References

### Vault
- [^1]: [[AI Agent Products/product/snowflake-intelligence|Snowflake Intelligence]] — Semantic View, Cortex Analyst/Search/Agent, YAML Semantic Model
- [^2]: [[AI Agent Products/product/glean|Glean]] — Enterprise Graph, Personal Graph, 시맨틱+어휘 하이브리드 검색
- [^3]: [[AI Agent Products/product/salesforce-agentforce|Salesforce Agentforce]] — Data Cloud, Atlas Reasoning Engine, Zero-Copy Partner Network, Vector Database
- [^4]: [[AI Agent Products/product/sap-joule|SAP Joule]] — SAP AI Core, Knowledge Catalog, Agentic Orchestration, 2400+ Joule Skills
- [^5]: [[AI Agent Products/product/databricks-mosaic-ai|Databricks Mosaic AI]] — Unity Catalog, Vector Search, Agent Framework, Compound AI Systems
- [^6]: [[AI Agent Products/product/servicenow-now-assist|ServiceNow Now Assist]] — Now Platform, AI Search, Genius Results, 3계층 AI 아키텍처
- [^7]: [[Research_v4.1_Context Graphs]] — Context Graph 정의, Triple 확장 구조, Decision Traces 개념

### External
- 각 제품 프로필 내 참고 자료 목록 참조

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
