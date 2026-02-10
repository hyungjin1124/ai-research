---
type: product-profile
product_id: snowflake-intelligence
product_name: Snowflake Intelligence
vendor: Snowflake
category: Analytics
tags:
  - AI-Agent
  - Analytics
  - NL-to-SQL
  - MCP-Support
url: https://www.snowflake.com/en/data-cloud/cortex/
launched: 2025-11
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Snowflake Intelligence

## 개요

Snowflake가 개발한 AI 기반 엔터프라이즈 데이터 분석 플랫폼. Cortex AI 엔진 위에 Cortex Analyst(정형 데이터 텍스트-to-SQL)와 Cortex Search(비정형 데이터 검색)를 통합하여, 비즈니스 사용자가 자연어로 데이터를 질의하고 거버넌스가 적용된 인사이트를 즉시 받을 수 있도록 설계되었다. Semantic View를 통해 비즈니스 용어와 데이터베이스 스키마를 매핑하며, Managed MCP Server를 통해 외부 AI 에이전트가 Snowflake 데이터에 안전하게 접근할 수 있는 개방형 아키텍처를 제공한다. 2025년 11월 GA로 출시되었으며, Snowflake 보안 경계 내에서 엔터프라이즈급 데이터 거버넌스를 유지하면서 셀프서비스 분석을 실현하는 것이 핵심 가치이다.

| 항목 | 내용 |
|------|------|
| 회사 | Snowflake |
| 출시일 | 2025-11 (Intelligence GA), Cortex Analyst 2024 Preview |
| 가격 | 소비 기반 크레딧 모델 (Cortex Analyst: 100메시지당 6.7크레딧, LLM 함수: 토큰당 과금) |
| 플랫폼 | Web (Snowsight), ai.snowflake.com, REST API, MCP Server |
| 공식 사이트 | https://www.snowflake.com/en/data-cloud/cortex/ |

## 핵심 기능

- **Cortex Analyst (텍스트-to-SQL)**: 자연어 질문을 SQL로 변환하여 정형 데이터에서 답변을 생성한다. YAML 기반 Semantic Model을 통해 테이블명, 컬럼명, 데이터 타입, 비즈니스 설명 등 메타데이터를 정의하면, LLM이 이 정보를 참조하여 정확한 SQL을 생성한다. 일반 텍스트-to-SQL 솔루션 대비 비즈니스 맥락을 반영한 높은 정확도가 강점이다
- **Cortex Search (비정형 데이터 검색)**: 문서, PDF, 이메일 등 비정형 소스에서 임베딩 기반 유사도 매칭과 인덱싱을 통해 인사이트를 추출한다. RAG(Retrieval-Augmented Generation) 패턴으로 정형+비정형 데이터를 결합한 종합 답변을 제공한다
- **Cortex Agent (에이전트 오케스트레이션)**: Cortex Analyst와 Cortex Search를 도구(tool)로 활용하는 자율 에이전트. 요청 파싱 → 계획 수립 → 도구 선택 및 실행 → 결과 평가 → 후속 조치(추가 질의 또는 최종 응답)를 반복하는 에이전틱 루프를 구현한다. 복잡한 멀티스텝 질문도 자동으로 서브태스크로 분할하여 처리한다. 2025년 11월 GA
- **Semantic View (의미론적 뷰)**: 비즈니스 용어(예: "매출", "고객 이탈률")를 실제 데이터베이스 스키마에 매핑하는 데이터베이스 객체. Snowsight UI에서 시각적으로 생성·관리 가능하며, Metrics/Dimensions/Facts 구조로 분석 모델을 정의한다. 2025년 10월 GA
- **Cortex Analyst Routing Mode**: 복수의 Semantic Model 간 자동 라우팅 기능. 질문의 의도에 따라 적절한 Semantic Model로 자동 분기하여 대규모 멀티도메인 환경에서도 정확한 응답을 생성한다. 2025년 11월 Preview
- **Custom Instructions**: Cortex Analyst에 사용자 정의 지침을 추가하여 응답 스타일, 용어 사용, 비즈니스 규칙 등을 커스터마이즈할 수 있다. 2025년 1월 Preview
- **Snowflake Managed MCP Server**: Cortex Analyst, Cortex Search, Cortex Agent를 MCP 도구로 노출하여 외부 AI 에이전트(Claude, GPT 등)가 Snowflake 데이터에 안전하게 접근할 수 있게 한다. RBAC 기반 도구 발견 및 호출 권한 제어를 지원하며, 별도 인프라 배포가 불필요하다. 2025년 10월 Preview

## 아키텍처

### 데이터 처리 파이프라인
```
사용자 자연어 질문
    ↓
Cortex Agent (계획 수립 · 태스크 분할)
    ↓
┌─────────────────────┐     ┌──────────────────────┐
│  Cortex Analyst      │     │  Cortex Search        │
│  (정형 데이터)        │     │  (비정형 데이터)       │
│  Semantic Model/View │     │  임베딩 인덱싱         │
│  → SQL 생성 · 실행    │     │  → 유사도 검색         │
└─────────────────────┘     └──────────────────────┘
    ↓                            ↓
결과 평가 및 반복 (Agentic Loop)
    ↓
최종 응답 (텍스트 + 시각화 + 참조 출처)
```

### Semantic Model 구조
- **YAML 기반 정의**: 테이블, 컬럼, 관계, 비즈니스 설명, 파생 메트릭을 경량 YAML 파일로 기술. 데이터베이스 스키마와 유사하지만 더 풍부한 의미론적 정보를 포함한다
- **Metrics**: SUM, AVG, COUNT 등 집계 로직이 포함된 비즈니스 지표 정의
- **Dimensions**: 분석 축(시간, 지역, 카테고리, 제품 라인 등) 정의
- **Facts**: 실제 데이터 테이블과의 물리적 매핑 정의
- **Semantic Model Generator**: Snowflake Labs가 제공하는 오픈소스 도구로, 기존 데이터베이스 스키마에서 Semantic Model YAML을 자동 생성한다

### 거버넌스 아키텍처
- **RBAC (역할 기반 접근 제어)**: Snowflake 네이티브 역할 시스템을 그대로 활용하여 행/열 수준의 세밀한 데이터 거버넌스를 적용한다
- **Snowflake 보안 경계**: 모든 데이터 처리가 Snowflake 플랫폼 내에서 수행되어 외부 데이터 유출 위험을 최소화한다
- **MCP Server RBAC**: MCP 도구 발견(discovery)과 호출(invocation)에 대한 세분화된 권한 관리를 지원한다
- **비용 및 지연 시간 모니터링**: 사용 통계, 쿼리 실행 비용, 레이턴시 메트릭을 추적할 수 있다

### 프로토콜 지원
- **MCP (Model Context Protocol)**: Snowflake Managed MCP Server를 통해 외부 AI 시스템과 표준화된 연결을 제공한다. Cortex Analyst와 Cortex Search를 MCP 도구로 자동 노출하며, 커스텀 도구 및 SQL 실행도 지원한다
- **REST API**: Cortex Agent, Cortex Analyst를 REST API로 직접 호출할 수 있다

### LLM 지원
- Snowflake Cortex AI를 통해 다양한 외부 모델을 선택할 수 있다
- OpenAI GPT-5.2가 Snowflake Cortex AI에서 직접 사용 가능 (2025년 발표)
- Claude, Llama 등 주요 모델도 지원하며, 모델별로 크레딧 단가가 상이하다

## UI/UX 분석

### 메인 인터페이스 구성
- **Snowsight 통합**: Snowflake의 웹 기반 UI인 Snowsight 내에 Intelligence 기능이 내장되어, 기존 Snowflake 사용자에게 익숙한 환경에서 AI 분석을 수행할 수 있다
- **ai.snowflake.com (독립 인터페이스)**: 비기술 사용자를 위한 전용 자연어 인터페이스로, 대화형 데이터 탐색에 최적화되어 있다
- **Dual-Pane 구조**: 좌측 채팅 패널에서 자연어 질의를 입력하고, 우측 캔버스에서 차트·테이블·분석 결과를 넓게 표시한다
- **Snowsight Wizard**: 데이터 에이전트를 선택하고 복수의 Semantic Layer를 탐색할 수 있는 가이드 방식 인터페이스

### 대화형 UI 패턴
- 자연어 입력 → SQL 생성 → 결과 시각화의 연속적 흐름
- Follow-up 질문을 통한 드릴다운 데이터 탐색 지원
- Semantic View 기반으로 비즈니스 용어를 사용한 직관적 대화 가능
- Starter questions 제안으로 초기 탐색을 안내

### 에이전트 UI 패턴
- **Cortex Agent 실행 단계 표시**: 에이전트가 선택한 도구, 실행한 쿼리, 검색 결과 등을 투명하게 시각화한다
- **Semantic View 논리 레이어**: LLM과 규칙 기반 처리를 분리하여 RAG 검색 과정을 투명하게 보여준다
- **Human-in-the-Loop**: YAML Semantic Model 편집 후 즉시 테스트 가능. 결과가 의도와 다를 경우 모델을 수정하여 즉각 반영한다
- **RBAC 기반 데이터 접근 제어**: 사용자 역할에 따라 접근 가능한 데이터와 기능이 자동으로 제한된다

### 데이터 시각화
- Metrics/Dimensions/Facts 구조에 기반한 자동 차트·테이블 생성
- Data indexing progress, Query execution plan 등 실행 과정 모니터링
- Derived Metrics(파생 지표)를 활용한 계산된 시각화 지원
- Cortex Search 통합으로 비정형 문서 내용과 정형 데이터를 결합한 복합 시각화

## 경쟁 포지셔닝

### 강점
- **데이터 플랫폼 네이티브 통합**: Snowflake 데이터 클라우드에 내장되어 별도 데이터 이동 없이 즉시 분석이 가능하다. 기존 Snowflake 고객에게 가장 낮은 도입 장벽을 제공한다
- **엔터프라이즈급 거버넌스**: 행/열 수준 RBAC, 데이터 리니지 추적, 보안 경계 내 처리로 금융·의료 등 규제 산업의 엄격한 요구사항을 충족한다
- **Semantic Model의 정확도**: YAML 기반 비즈니스 메타데이터가 일반 텍스트-to-SQL 대비 높은 쿼리 정확도를 제공한다. 비즈니스 용어와 데이터 스키마 간 명확한 매핑으로 할루시네이션을 최소화한다
- **MCP 표준 지원**: 오픈 프로토콜 기반으로 외부 AI 에이전트 생태계와 호환된다. Claude, GPT 등에서 Snowflake 데이터에 직접 접근 가능하여 벤더 종속을 최소화한다
- **소비 기반 가격**: 사용한 만큼만 과금하는 크레딧 모델로 초기 비용 부담이 없으며, 소규모 팀도 즉시 시작할 수 있다

### 약점
- **Snowflake 종속성**: Snowflake 플랫폼에 데이터가 있어야만 사용 가능하다. BigQuery, Redshift 등 타 데이터 웨어하우스 사용자는 데이터 마이그레이션이 필요하다
- **Semantic Model 구축 부담**: YAML 기반 Semantic Model을 수동으로 정의해야 하는 초기 셋업 비용이 존재한다. 대규모 스키마의 경우 상당한 노력과 도메인 전문 지식이 요구된다
- **비용 예측 어려움**: 소비 기반 모델 특성상 복잡한 쿼리가 예상보다 높은 비용을 발생시킬 수 있다. 대규모 테이블 조인 쿼리에서 단일 쿼리에 수천 달러의 크레딧이 소비된 사례가 보고되었다
- **셀프서비스 BI 성숙도**: ThoughtSpot 등 전용 셀프서비스 BI 도구 대비 최종 사용자 경험(시각화, 드릴다운, 대시보드)의 깊이가 아직 부족하다

### 주요 경쟁사 비교
| 항목 | Snowflake Intelligence | ThoughtSpot Spotter | Databricks Mosaic AI |
|------|----------------------|-------------------|-------------------|
| 핵심 접근법 | 데이터 플랫폼 네이티브 NL-to-SQL | 검색 기반 에이전틱 분석 | 에이전트 프레임워크 + MLOps |
| 가격 모델 | 소비 기반 크레딧 | 사용자당 월 과금 ($25-$50+) | DBU 기반 소비 모델 |
| Semantic Layer | YAML Semantic Model (수동 정의) | SpotterModel (AI 자동 생성) | Unity Catalog (메타데이터 거버넌스) |
| MCP 지원 | Managed MCP Server (Preview) | MCP Server 연결 (2025-09) | 미지원 |
| 거버넌스 | 행/열 RBAC, 보안 경계 | 역할 기반 접근 제어 | Unity Catalog + Lakeguard |
| 주요 대상 | Snowflake 기존 고객, 데이터 팀 | 비즈니스 분석가, 셀프서비스 BI | 데이터 엔지니어, ML 엔지니어 |
| 비정형 데이터 | Cortex Search (기본 RAG) | Spotter 3 (Slack, Salesforce 등) | Vector Search + 고급 RAG |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — 크로스 제품 UI/UX 비교 테이블에서 Snowflake Intelligence 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] — Analytics 카테고리 벤치마크 대상

## 참고 자료

- [Snowflake Cortex AI 공식 사이트](https://www.snowflake.com/en/data-cloud/cortex/)
- [Snowflake Intelligence GA 릴리스 노트](https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-snowflake-intelligence)
- [Cortex Agents 문서](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)
- [Cortex Analyst 문서](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
- [Cortex Analyst Semantic Model Specification](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec)
- [Snowflake Managed MCP Server 문서](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
- [Snowflake Labs MCP GitHub](https://github.com/Snowflake-Labs/mcp)
- [Snowflake Blog: Managed MCP Servers for Secure Data Agents](https://www.snowflake.com/en/blog/managed-mcp-servers-secure-data-agents/)
- [Snowflake Blog: Agentic AI Ready Enterprise Data](https://www.snowflake.com/en/blog/agentic-ai-ready-enterprise-data/)
- [Snowflake Blog: OpenAI GPT-5.2 on Cortex AI](https://www.snowflake.com/en/blog/announcing-openai-snowflake-cortex-ai/)
- [Snowflake Intelligence 가격 및 비용 모니터링 (Select)](https://select.dev/posts/snowflake-intelligence-overview-pricing-and-cost-monitoring)
- [Cortex Analyst 비용 모니터링 (Select)](https://select.dev/posts/snowflake-cortex-analyst-overview-pricing-and-cost-monitoring)
- [Snowflake Cortex AI 비용 분석 (Seemore Data)](https://seemoredata.io/blog/snowflake-cortex-ai/)
- [Semantic Model Generator (GitHub)](https://github.com/Snowflake-Labs/semantic-model-generator)
- [Developer's Guide to Snowflake Cortex Agent (Medium)](https://medium.com/snowflake/developers-guide-to-snowflake-cortex-agent-46b52ea4aceb)
