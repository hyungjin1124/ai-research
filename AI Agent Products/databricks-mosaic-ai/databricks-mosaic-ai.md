---
type: product-profile
product_id: databricks-mosaic-ai
product_name: Databricks Mosaic AI
vendor: Databricks
category: Analytics
tags:
  - AI-Agent
  - Analytics
  - Agent-Builder
url: https://www.databricks.com/product/machine-learning
launched: 2024-06
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Databricks Mosaic AI

## 개요

Databricks가 개발한 엔터프라이즈 AI 에이전트 빌드·배포·평가 플랫폼. 단일 LLM이 아닌 복합 AI 시스템(Compound AI Systems) 패러다임을 핵심으로 하여, LLM·리트리버·도구·가드레일을 조합한 프로덕션급 에이전트를 구축할 수 있는 통합 프레임워크를 제공한다. Agent Framework로 에이전트를 구축하고, Agent Evaluation으로 품질·비용·레이턴시를 평가하며, Unity Catalog로 거버넌스를 적용하고, MLflow 3.0으로 관측성(observability)을 확보하는 엔드투엔드 에이전트 라이프사이클을 지원한다. Lakeguard 샌드박스로 에이전트 코드 실행의 안전성을 보장하며, 데이터 엔지니어와 ML 엔지니어를 주요 대상으로 한다. 2024년 6월 첫 발표 후 지속적으로 기능을 확장하여 2025년 GA를 달성했다.

| 항목 | 내용 |
|------|------|
| 회사 | Databricks |
| 출시일 | 2024-06 (Agent Framework 발표), 2025 GA |
| 가격 | DBU(Databricks Unit) 기반 소비 모델 + 토큰당 추론 비용 |
| 플랫폼 | Web (Databricks Workspace), AI Playground, REST API, Python SDK |
| 공식 사이트 | https://www.databricks.com/product/machine-learning |

## 핵심 기능

- **Agent Framework (에이전트 프레임워크)**: 프로덕션급 AI 에이전트를 구축·배포하기 위한 통합 프레임워크. LangChain, LangGraph 등 주요 오케스트레이션 프레임워크와 호환되며, Unity Catalog에 등록된 도구를 에이전트가 직접 호출할 수 있다. RAG 애플리케이션부터 자율 에이전트까지 다양한 유형을 지원한다
- **Agent Evaluation (에이전트 평가)**: AI 에이전트의 품질(정확도, 근거 기반 응답), 비용, 레이턴시를 체계적으로 평가하는 도구. 규칙 기반 검사, LLM 판정자(AI Judge), 사람 피드백을 결합한 하이브리드 평가 방식을 지원한다. 근거 기반 평가(groundedness), 정확도(accuracy), 안전성(safety) 등 다차원 평가 메트릭을 제공한다
- **Agent Evaluation Review App**: 도메인 전문가(SME)가 에이전트 응답을 평가·라벨링·수정할 수 있는 전용 웹 앱. 스프레드시트나 커스텀 도구 없이 GenAI 앱 트레이스를 평가하고, Golden Examples(정답 데이터셋)을 정의할 수 있다. 피드백은 Delta 테이블로 Unity Catalog에 저장된다
- **Unity Catalog (통합 거버넌스)**: 에이전트가 사용하는 모든 도구, 데이터, 모델, 함수에 대한 중앙화된 거버넌스를 제공한다. 데이터 리니지 추적, 접근 제어, 메타데이터 관리를 단일 카탈로그에서 수행한다. 에이전트 도구를 Unity Catalog 함수로 등록하여 재사용 가능하게 한다
- **Lakeguard (샌드박스 실행 환경)**: 에이전트 코드를 격리된 샌드박스에서 실행하여 Unity Catalog 거버넌스와 ACL을 준수하면서도 안전하게 도구를 사용할 수 있게 한다. 악의적이거나 오류가 있는 코드가 프로덕션 데이터에 영향을 주는 것을 방지한다
- **AI Playground (프로토타이핑 환경)**: 에이전트를 코드 없이 빠르게 프로토타이핑하고 테스트할 수 있는 샌드박스 환경. 도구 호출(tool-calling)을 실험하고 에이전트 동작을 검증한 뒤 프로덕션으로 배포할 수 있다
- **MLflow 3.0 통합**: GenAI 시대에 맞춰 재설계된 MLflow 3.0과 긴밀히 통합된다. 에이전트 관측성(observability), 프롬프트 레지스트리(버전 관리·테스트·배포), 크로스 플랫폼 모니터링(Databricks 외부 배포 에이전트도 지원)을 제공한다
- **Vector Search**: 비정형 데이터에 대한 벡터 임베딩 기반 유사도 검색을 제공하여 RAG 파이프라인의 리트리벌 단계를 지원한다

## 아키텍처

### 에이전트 라이프사이클
```
1. 구축 (Build)
   ├── AI Playground에서 프로토타이핑
   ├── Agent Framework로 에이전트 코드 작성
   ├── Unity Catalog에서 도구 등록 및 발견
   └── LangChain/LangGraph 등 오케스트레이션 프레임워크 활용
        ↓
2. 평가 (Evaluate)
   ├── Agent Evaluation으로 품질·비용·레이턴시 측정
   ├── Review App으로 도메인 전문가 피드백 수집
   ├── Golden Examples 정의 및 회귀 테스트
   └── AI Judge (LLM 기반 자동 평가) + 규칙 기반 검사
        ↓
3. 배포 (Deploy)
   ├── Model Serving으로 원클릭 최적화 배포
   ├── Lakeguard 샌드박스에서 안전한 코드 실행
   ├── AI Gateway로 중앙화된 접근·거버넌스·모니터링
   └── LLM Guardrails로 안전성 보장
        ↓
4. 모니터링 (Monitor)
   ├── MLflow 3.0 프로덕션 트레이스
   ├── 비용/레이턴시/품질 실시간 추적
   └── 크로스 플랫폼 관측성 (외부 배포 포함)
```

### 복합 AI 시스템(Compound AI Systems) 구조
- **LLM**: 다양한 파운데이션 모델(Claude, GPT, Llama, DBRX 등) 중 선택 가능. Mosaic AI Model Serving을 통해 제공
- **리트리버(Retriever)**: Vector Search 기반 RAG 리트리벌. Unity Catalog에서 관리되는 벡터 인덱스 활용
- **도구(Tools)**: Unity Catalog 함수로 등록된 외부 API, SQL 쿼리, Python 함수 등을 에이전트가 호출
- **가드레일(Guardrails)**: LLM Guardrails로 유해 콘텐츠, 개인정보 노출, 오프토픽 응답을 차단
- **거버넌스**: Unity Catalog가 모든 컴포넌트에 대한 접근 제어, 리니지, 감사를 제공

### 프레임워크 호환성
- **LangChain/LangGraph**: `databricks-langchain` 패키지로 Databricks LLM과 Unity Catalog 도구를 LangChain/LangGraph에서 직접 사용
- **MLflow 3.0**: 에이전트 로깅, 트레이스, 프롬프트 버전 관리, 크로스 플랫폼 모니터링
- **Python SDK**: 에이전트 정의, 도구 등록, 평가 실행을 코드로 수행

### 배포 아키텍처
- **Mosaic AI Model Serving**: 파운데이션 모델 및 커스텀 모델을 서버리스 엔드포인트로 배포
- **Mosaic AI Gateway**: 에이전트 시스템 프로덕션 환경에서의 중앙화된 거버넌스, 통합 접근, 관측성을 제공. 토큰 사용량 및 스토리지 기반 과금

## UI/UX 분석

### 메인 인터페이스 구성
- **Agent Evaluation Review App**: 도메인 전문가가 에이전트 트레이스를 평가·라벨링하는 전용 웹 앱. 외부 이해관계자도 접근 가능(SME Review App)
- **AI Playground**: 에이전트를 코드 없이 실험할 수 있는 샌드박스 환경. 도구 호출을 시각적으로 테스트하고 결과를 즉시 확인
- **Monitoring UI**: 프로덕션 배포된 에이전트의 성능, 비용, 품질을 실시간으로 모니터링하는 대시보드

### 대화형 UI 패턴
- MLflow 기반 로깅으로 에이전트 대화 이력을 체계적으로 기록
- 트레이스 기반 디버깅으로 에이전트의 추론 과정을 단계별로 추적
- LangChain/LangGraph 통합으로 복잡한 멀티스텝 에이전트 플로우를 시각적으로 구성

### Human-in-the-Loop 패턴
- **SME Review App**: 도메인 전문가가 스프레드시트 없이 웹 인터페이스에서 직접 에이전트 응답을 평가하고 라벨링
- **Golden Examples 정의**: 정답 데이터셋을 정의하여 에이전트 성능의 기준선을 설정하고 회귀를 방지
- **Human Feedback Loops**: 사람의 피드백을 Delta 테이블로 수집하여 평가 데이터셋 구축에 활용. 지속적 품질 개선 사이클을 구현

### 데이터 시각화
- **Evaluation Metrics 시각화**: 정확도, 근거 기반 응답(groundedness), 비용, 레이턴시 등 평가 지표를 시각적으로 비교·분석
- **Cost/Latency/Quality 트레이드오프**: 모델·설정 변경에 따른 비용-성능 균형을 시각적으로 표현
- **Root Cause Analysis**: 에이전트 실패 원인을 트레이스 기반으로 분석하는 시각화 도구
- **MLflow Tracking UI**: 실험 파라미터, 메트릭, 아티팩트를 추적하고 비교하는 대시보드

## 경쟁 포지셔닝

### 강점
- **엔드투엔드 에이전트 라이프사이클**: 구축 → 평가 → 배포 → 모니터링의 전체 과정을 하나의 플랫폼에서 수행한다. 별도 도구를 조합할 필요 없이 통합된 워크플로우를 제공한다
- **체계적 에이전트 평가**: Agent Evaluation의 다차원 평가(AI Judge + 규칙 기반 + 사람 피드백)는 경쟁 제품에서 찾기 어려운 수준의 품질 보증 메커니즘이다
- **Unity Catalog 거버넌스**: 데이터, 모델, 도구, 함수 전체에 걸친 중앙화된 거버넌스로, 대기업의 컴플라이언스 요구사항을 충족한다. 데이터 리니지, 접근 제어, 감사 추적을 단일 지점에서 관리한다
- **Lakeguard 안전성**: 에이전트 코드를 샌드박스에서 실행하여 프로덕션 데이터 안전성을 보장한다. 자율 에이전트의 예측 불가능한 행동으로 인한 위험을 완화한다
- **MLflow 3.0 크로스 플랫폼 관측성**: Databricks 외부(AWS, GCP, 온프레미스)에 배포된 에이전트도 모니터링할 수 있어, 멀티클라우드 환경을 운영하는 기업에 강점이다
- **프레임워크 유연성**: LangChain, LangGraph 등 인기 프레임워크와 호환되어 기존 코드 자산을 재활용할 수 있다

### 약점
- **높은 기술 장벽**: 데이터 엔지니어/ML 엔지니어 대상 플랫폼으로, 비기술 비즈니스 사용자가 직접 활용하기 어렵다. ThoughtSpot이나 Snowflake Intelligence 같은 셀프서비스 NL-to-SQL 경험은 제공하지 않는다
- **복잡한 가격 구조**: DBU, 토큰, 스토리지 등 다중 과금 요소로 비용 예측이 복잡하다. 에이전트 복잡도에 따라 비용이 크게 변동할 수 있다
- **Databricks 생태계 의존**: Unity Catalog, Model Serving, Vector Search 등 Databricks 전용 서비스에 최적화되어 있어, 다른 플랫폼과의 이식성이 제한적이다
- **MCP 미지원**: 현재 MCP(Model Context Protocol) 표준을 지원하지 않아, 외부 AI 에이전트 생태계와의 연결에서 Snowflake나 Glean 대비 불리하다

### 주요 경쟁사 비교
| 항목 | Databricks Mosaic AI | Snowflake Intelligence | AWS Bedrock Agents |
|------|-------------------|----------------------|-------------------|
| 핵심 접근법 | 에이전트 프레임워크 + MLOps | 데이터 플랫폼 네이티브 NL-to-SQL | 클라우드 에이전트 서비스 |
| 주요 대상 | 데이터/ML 엔지니어 | 데이터 팀 + 비즈니스 사용자 | 클라우드 개발자 |
| 에이전트 평가 | Agent Evaluation (AI Judge + 사람 피드백) | 기본 HITL 검증 | 기본 테스트 도구 |
| 거버넌스 | Unity Catalog + Lakeguard | 행/열 RBAC | IAM + Guardrails |
| 샌드박스 실행 | Lakeguard | Snowflake 보안 경계 | Lambda 격리 환경 |
| 관측성 | MLflow 3.0 (크로스 플랫폼) | 기본 사용 통계 | CloudWatch 통합 |
| 가격 모델 | DBU 기반 소비 | 크레딧 기반 소비 | 요청당 과금 |
| MCP 지원 | 미지원 | Managed MCP Server | 미지원 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — 크로스 제품 UI/UX 비교 테이블에서 Databricks Mosaic AI 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] — Analytics 카테고리 벤치마크 대상

## 참고 자료

- [Databricks Mosaic AI 공식 사이트](https://www.databricks.com/product/artificial-intelligence)
- [Mosaic AI Agent Framework 제품 페이지](https://www.databricks.com/product/machine-learning/retrieval-augmented-generation)
- [Databricks Blog: Announcing Mosaic AI Agent Framework and Agent Evaluation](https://www.databricks.com/blog/announcing-mosaic-ai-agent-framework-and-agent-evaluation)
- [Databricks Blog: Mosaic AI Announcements at Data+AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
- [Databricks Blog: Build Autonomous AI Assistant with Mosaic AI Agent Framework](https://www.databricks.com/blog/build-autonomous-ai-assistant-mosaic-ai-agent-framework)
- [Databricks Blog: Introducing Enhanced Agent Evaluation](https://www.databricks.com/blog/introducing-enhanced-agent-evaluation)
- [Databricks Blog: Build and Deploy Production-quality Compound AI Systems](https://www.databricks.com/blog/mosaic-ai-build-and-deploy-production-quality-compound-ai-systems)
- [Mosaic AI GenAI Capabilities 문서 (AWS)](https://docs.databricks.com/aws/en/generative-ai/guide/mosaic-ai-gen-ai-capabilities)
- [AI Agent Tools 문서](https://docs.databricks.com/aws/en/generative-ai/agent-framework/agent-tool)
- [Mosaic AI Gateway 문서](https://www.databricks.com/product/artificial-intelligence/ai-gateway)
- [Databricks AI Agent 비용 가이드 (Community)](https://community.databricks.com/t5/technical-blog/demystifying-databricks-pricing-for-ai-agents/ba-p/122281)
- [Databricks Mosaic AI Gateway Pricing (TrueFoundry)](https://www.truefoundry.com/blog/databricks-mosaic-ai-gateway-pricing-explained-2026)
- [Databricks Mosaic AI 2026 개요 (Kanerika)](https://kanerika.com/blogs/databricks-mosaic-ai/)
