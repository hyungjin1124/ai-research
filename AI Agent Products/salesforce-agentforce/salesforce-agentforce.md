---
type: product-profile
product_id: salesforce-agentforce
product_name: Salesforce Agentforce
vendor: Salesforce
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - Agent-Builder
  - ERP-Integrated
url: https://www.salesforce.com/agentforce/
launched: 2024-10
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Salesforce Agentforce

## 개요

Salesforce가 개발한 엔터프라이즈 AI 에이전트 플랫폼. CRM 데이터와 비즈니스 프로세스에 깊이 통합된 자율 AI 에이전트를 구축·배포·관리할 수 있도록 설계되었다. 핵심 추론 엔진인 Atlas Reasoning Engine이 "System 2" 방식의 숙고형 추론을 수행하며, Data Cloud를 통한 실시간 데이터 통합과 MuleSoft를 통한 외부 시스템 연결이 주요 차별점이다. 2024년 10월 Agentforce 1.0 출시 이후 2025년 2월 Agentforce 2.0, 2025년 6월 Agentforce 3.0까지 빠르게 진화하며, Sales·Service·Marketing·Commerce 전 영역에 걸친 자율 에이전트 생태계를 확장하고 있다. 대화당 $2의 소비 기반 과금 모델을 도입하여 기존 시트 기반 라이선스와 차별화된 가격 전략을 취하고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Salesforce |
| 출시일 | 2024-10 (1.0), 2025-02 (2.0), 2025-06 (3.0) |
| 가격 | $2/대화 (기본), 산업별 애드온 $125~$650/사용자/월 |
| 플랫폼 | Salesforce Platform, Data Cloud, MuleSoft, Slack |
| 공식 사이트 | https://www.salesforce.com/agentforce/ |

## 핵심 기능

- **Atlas Reasoning Engine**: Agentforce의 핵심 두뇌로, Salesforce AI Research에서 개발된 숙고형(deliberative) 추론 엔진. 계획 수립(Plan) → 행동(Act) → 관찰(Observe) 순환을 반복하며, 구조화·비구조화 데이터를 Data Cloud에서 실시간으로 검색하여 문맥에 맞는 의사결정을 내린다. 초기 파일럿에서 응답 관련성 2배 향상, 엔드투엔드 정확도 33% 개선 성과 확인
- **Agent Builder**: 노코드/로코드 에이전트 구축 도구. 토픽(Topic) 기반으로 에이전트의 역할과 범위를 정의하고, 각 토픽에 액션(Action)을 연결하여 에이전트 행동을 설계한다. 파일 기반 탐색기(file-based explorer)로 구성 요소를 직관적으로 관리하며, 시뮬레이션·테스트·배포를 단일 워크스페이스에서 수행 가능
- **Agentforce for Sales**: 리드 육성, 파이프라인 관리, 딜 인사이트 제공, 미팅 준비 자동화 등 영업 프로세스 전반을 지원하는 자율 에이전트. 기회 레코드 기반으로 실시간 추천 생성
- **Agentforce for Service**: 고객 문의 자동 분류 및 응답, 케이스 요약, 지식 기반 문서 검색, 에스컬레이션 판단을 수행하는 서비스 에이전트. Omni-Channel 라우팅과 통합되어 인간 에이전트와 원활한 핸드오프 지원
- **Agentforce for Marketing**: 캠페인 설계, 세그먼트 생성, 콘텐츠 최적화, A/B 테스트 자동화를 수행하며, Marketing Cloud 데이터를 활용한 개인화 추천 제공
- **Agentforce for Commerce**: 상품 추천, 주문 추적, 반품 처리, 프로모션 관리 등 커머스 영역 자동화 에이전트
- **Testing Center**: 실제 사용자 인터랙션을 시뮬레이션하여 에이전트 응답 품질과 지연 시간을 검증하는 전용 테스트 환경. 배포 전 품질 보증 워크플로우 내장
- **Agentforce Command Center (3.0)**: 에이전트 상태, 성능 지표, 비즈니스 성과를 단일 대시보드에서 모니터링하는 통합 관제 솔루션. 에이전트 헬스 체크, 대화 분석, 사용량 추적 기능 제공

## 아키텍처

### 추론 엔진

| 구성 요소 | 역할 |
|----------|------|
| Atlas Reasoning Engine | 숙고형 추론, 계획-행동-관찰 루프, 자기 반성(self-reflection) |
| Topic Classification | 사용자 입력을 비즈니스 토픽으로 자동 분류 |
| Action Orchestration | 토픽별 정의된 액션(Flow, Apex, API) 실행 |
| Guardrails | 토픽 범위 제한, 안전 필터, 에스컬레이션 규칙 적용 |

### 데이터 아키텍처

- **Data Cloud (Data 360)**: 구조화·비구조화 데이터를 통합하는 실시간 데이터 플랫폼. 고객 프로필, 거래 이력, 외부 웹 데이터를 벡터 DB에 인덱싱하여 RAG(Retrieval-Augmented Generation) 기반 응답 생성
- **Zero-Copy Partner Network**: Snowflake, Databricks, Google BigQuery 등 외부 데이터 레이크와 데이터 복제 없이 직접 연결
- **Vector Database**: 비구조화 데이터(문서, 이메일, 채팅 로그)를 임베딩하여 의미 기반 검색 수행

### 통합 아키텍처

- **MuleSoft Agent Fabric**: 외부 시스템 API를 에이전트 액션으로 직접 노출. API Catalog에서 Salesforce·Heroku·외부 API를 통합 관리
- **Topic Center**: MuleSoft API를 Agentforce 토픽과 액션에 매핑하는 설계 시점(design-time) 도구
- **Agentforce Gateway**: Envoy 기반 정책 엔진으로 에이전트 트래픽에 대한 ABAC(속성 기반 접근 제어), 할당량 제한, 인증·인가를 처리
- **MCP 지원 (3.0)**: Model Context Protocol 내장 지원으로 외부 AI 도구와의 플러그앤플레이 연동 가능

### 모델 유연성

- Salesforce 자체 LLM 외에 Anthropic Claude (Amazon Bedrock 기반), OpenAI 등 외부 모델을 Salesforce 인프라에서 보안 호스팅하여 사용 가능
- 모델 선택은 에이전트별 또는 태스크별로 구성 가능

### 에코시스템 통합

- Slack: 에이전트를 Slack 채널에 배포하여 팀 협업 내 자연어 인터랙션
- Tableau: 데이터 시각화 및 인사이트 대시보드와 에이전트 연동
- Commerce Cloud, Marketing Cloud, Service Cloud 등 Salesforce 전 제품군 네이티브 통합

## UI·UX 분석

### 메인 인터페이스 구성

- **Agent Builder 3-Panel Layout**: 좌측 단계 패널(Steps) + 중앙 구성 패널(Configuration) + 우측 가이드 패널(Guidance)의 3단 레이아웃으로 에이전트 구축 워크플로우를 시각적으로 구조화. 토픽 정의 → 액션 연결 → 테스트의 전체 흐름을 단일 화면에서 관리
- **파일 기반 탐색기**: 플랫 리스트가 아닌 파일 시스템 스타일의 계층 구조로 토픽·액션·인스트럭션을 조직화. 검색 및 탐색 효율 향상
- **Agentforce Studio**: 에이전트 액션 라이브러리, 학습 리소스, 게이트웨이 구성을 통합 제공하는 중앙 허브

### 대화형 UI 패턴

- 자연어 입력 기반 인터랙션
- 토픽 기반 대화 조직화: 사용자 의도를 자동으로 토픽에 매핑하여 적절한 에이전트 액션을 트리거
- 후속 질문(Follow-up questions) 자동 제안
- 응답 스트리밍: Agentforce 3.0부터 실시간 응답 스트리밍 지원(GA), 50% 지연 시간 단축

### 에이전트 UI 패턴

- **Omni Supervisor 대시보드**: 서비스 관리자가 AI 에이전트와 인간 에이전트를 동일한 인터페이스에서 실시간 모니터링. 대화 요약 컬럼이 포함된 인터랙션 테이블, 진행 중인 대화에 대한 "Listen-in" 기능으로 에이전트 행동을 실시간 감독
- **Step-by-Step Reasoning 시각화**: Atlas 추론 엔진의 사고 과정을 Topic → Action → Record → Grounding 단계로 실시간 표시. 의사결정 트리 시각화로 에이전트 행동의 투명성 확보
- **Test Drive**: 배포 전 에이전트와 직접 대화하며 동작을 검증하는 인터랙티브 테스트 모드
- **Human-in-the-Loop**: 에이전트 판단이 불확실한 경우 자동으로 인간 에이전트에게 에스컬레이션. Omni Supervisor에서 에스컬레이션 건을 추적·관리

### 데이터 시각화

- Vector Database 기반 RAG 처리 과정 시각화
- Tableau 연동을 통한 에이전트 성과 대시보드
- Command Center에서 에이전트 헬스, 대화량, 해결률, 평균 응답 시간 등 KPI 실시간 모니터링

## 경쟁 포지셔닝

### 강점

- **CRM 네이티브 통합**: Salesforce CRM 데이터(고객, 기회, 케이스, 캠페인)와 직접 연결되어 별도 데이터 파이프라인 없이 에이전트가 비즈니스 컨텍스트를 즉시 활용
- **Atlas 추론 엔진**: 단순 프롬프트 전달이 아닌 계획-행동-관찰 루프 기반의 숙고형 추론으로 복잡한 비즈니스 시나리오 처리 가능
- **MuleSoft 통합 생태계**: API-led 아키텍처를 통해 SAP, Workday 등 외부 엔터프라이즈 시스템과의 연결이 네이티브로 지원되며, Agentforce Gateway로 거버넌스까지 통합 관리
- **소비 기반 과금**: 대화당 $2로 시작하는 유연한 가격 모델은 사용량 예측이 어려운 초기 도입 단계에서 진입 장벽을 낮춤
- **빠른 혁신 속도**: 6개월 간격으로 메이저 버전(1.0 → 2.0 → 3.0) 출시, 다국어 지원(6개 언어 + 30개 추가 예정)으로 글로벌 확장

### 약점

- **Salesforce 종속성**: Salesforce Platform 외부에서의 독립적 에이전트 운영이 제한적. Data Cloud, MuleSoft 등 자사 생태계 의존도가 높음
- **실질 비용 부담**: 대화당 $2 기본 가격 외에 Data Cloud, MuleSoft 라이선스, 산업별 애드온($125~$650/사용자/월)이 추가되어 총 소유 비용(TCO)이 높아질 수 있음
- **커스터마이징 복잡성**: 단순 에이전트는 노코드로 빠르게 구축 가능하나, 복잡한 다단계 워크플로우 설계 시 Flow, Apex, MuleSoft 지식이 필요하여 학습 곡선 존재
- **비-Salesforce 고객 진입 장벽**: CRM을 Salesforce로 사용하지 않는 기업에는 플랫폼 전체 도입이 선행되어야 하므로 접근성이 낮음

### 주요 경쟁사 비교

| 항목 | Salesforce Agentforce | Microsoft Copilot (D365) | SAP Joule |
|------|----------------------|--------------------------|-----------|
| 추론 방식 | Atlas (숙고형 루프) | Copilot Orchestrator | Knowledge Graph + RAGe |
| 에이전트 빌더 | Agent Builder (노코드/로코드) | Copilot Studio | Joule Studio |
| 데이터 통합 | Data Cloud + Zero-Copy | Microsoft Graph + Dataverse | SAP Business Data Cloud |
| 외부 연결 | MuleSoft API Fabric | Power Platform 커넥터 + MCP | SAP BTP Integration Suite |
| 가격 모델 | $2/대화 + 애드온 | $30/사용자/월 (번들) | AI Units 소비 기반 |
| 모니터링 | Omni Supervisor + Command Center | Manager Insights | Joule Admin Center |
| MCP 지원 | 3.0부터 내장 | Copilot Studio 네이티브 | Microsoft 365 양방향 연동 |
| 다국어 | 6개 언어 + 30개 추가 예정 | 전 Dynamics 365 지원 언어 | SAP 지원 언어 전체 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — Agentforce의 3-Panel Layout, Omni Supervisor, Atlas Engine 관련 크로스 제품 비교 참조
- [[리서치 목표 및 벤치마크 대상]] — 엔터프라이즈 AI Agent 벤치마크 대상 제품 목록

## 참고 자료

- [Salesforce Agentforce 공식 사이트](https://www.salesforce.com/agentforce/)
- [Salesforce Engineering Blog: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)
- [Salesforce Press Release: Agentforce 3 Announcement (2025-06)](https://www.salesforce.com/news/press-releases/2025/06/23/agentforce-3-announcement/)
- [Salesforce Architects: Architecting the Agentic Enterprise with MuleSoft](https://architect.salesforce.com/fundamentals/mulesoft-architecting-agentic-enterprise)
- [Trailhead: Explore the New Agentforce Builder](https://trailhead.salesforce.com/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder)
- [Trailhead: Atlas Reasoning Engine Capabilities](https://trailhead.salesforce.com/content/learn/modules/reasoning-in-artificial-intelligence/discover-the-atlas-reasoning-engine)
- [Salesforce Ben: Everything About MuleSoft for Agentforce](https://www.salesforceben.com/everything-you-need-to-know-about-mulesoft-for-agentforce/)
- [Salesforce Ben: Agentforce 3 -- Command Center, MCP, and Apps](https://www.salesforceben.com/salesforce-announces-agentforce-3-0-command-center-mcp-and-apps/)
- [Salesforce Omni Supervisor Documentation](https://help.salesforce.com/s/articleView?id=service.omnichannel_supervisor_intro.htm&language=en_US&type=5)
- [Agentforce Pricing Overview (Winfomi)](https://www.winfomi.com/blog/salesforce-agentforce-pricing-service-sales)
