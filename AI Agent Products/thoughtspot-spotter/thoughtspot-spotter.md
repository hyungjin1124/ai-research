---
type: product-profile
product_id: thoughtspot-spotter
product_name: ThoughtSpot Spotter
vendor: ThoughtSpot
category: Analytics
tags:
  - AI-Agent
  - Analytics
  - NL-to-SQL
url: https://www.thoughtspot.com/product/spotter
launched: 2025-01
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# ThoughtSpot Spotter

## 개요

ThoughtSpot가 개발한 에이전틱 애널리틱스(Agentic Analytics) 플랫폼. 자연어 검색 기반 BI를 넘어, 4개의 AI 에이전트(Spotter 3, SpotterModel, SpotterViz, SpotterCode)가 팀으로 협업하여 데이터 모델링부터 시각화·코드 생성까지 분석 라이프사이클 전체를 자동화한다. 특허 출원 중인 피드백 루프를 통해 사용자의 단어·구문 수준 교정을 학습하여 지속적으로 정확도를 개선하며, Drill-Anywhere 기능으로 사전 정의된 드릴 경로 없이도 어떤 시각화에서든 즉시 상세 분석으로 진입할 수 있다. 2025년 1월 Spotter 최초 발표 이후, 2025년 12월에 4개 에이전트 체계를 갖추며 풀 에이전틱 분석 플랫폼으로 진화했다.

| 항목 | 내용 |
|------|------|
| 회사 | ThoughtSpot |
| 출시일 | 2025-01 (Spotter), 2025-12 (4 BI Agents 발표) |
| 가격 | Essentials $25/사용자/월, Pro $50/사용자/월, Enterprise 커스텀 |
| 플랫폼 | Web (SaaS), 임베디드 분석, Mobile SDK, REST API |
| 공식 사이트 | https://www.thoughtspot.com/product/spotter |

## 핵심 기능

- **Spotter 3 (핵심 AI 분석 에이전트)**: 최신 버전의 핵심 에이전트로, 정형 데이터뿐 아니라 Slack, Salesforce 등 비정형 앱 데이터도 통합하여 분석한다. 질문에 대한 답변을 생성한 후 자체적으로 답변 품질을 평가하고, 정확한 결과에 도달할 때까지 추가 분석을 자동으로 반복하는 자기 검증(self-validation) 기능을 갖추었다. Python 코딩, 예측 분석(forecasting) 기능도 내장되어 있다
- **SpotterModel (시맨틱 모델 에이전트)**: 원시 데이터를 거버넌스가 적용된 시맨틱 모델로 자동 변환한다. 비즈니스 로직에 따라 관계, 디멘션, 메저를 자동으로 매핑하며, Human-in-the-Loop 검증을 통해 정의의 일관성을 유지한다. 모델 유지보수도 자동화하여 스키마 변경 시 자동 업데이트를 수행한다
- **SpotterViz (대시보드 에이전트)**: 데이터를 스토리로 변환하는 대시보드 생성 에이전트. 데이터의 특성에 맞는 최적의 시각화 유형을 자동으로 선택(best-fit visualization)하고, Liveboards를 통해 실시간 협업 대시보드를 생성한다
- **SpotterCode (개발자 에이전트)**: 임베디드 분석 개발을 가속화하는 AI 페어 프로그래머. Cursor, Claude Code, GitHub Copilot, VS Code 등 주요 IDE와 통합되며, ThoughtSpot API를 활용한 코드를 자동 생성한다
- **Patent-Pending Feedback Loop**: 특허 출원 중인 피드백 메커니즘으로, 사용자가 단어·구문 단위로 교정한 내용을 학습하여 도메인 특화 용어와 비즈니스 맥락에 대한 이해를 지속적으로 개선한다. Human Expert Labeling UI를 제공한다
- **Drill-Anywhere**: 사전 정의된 드릴 경로 없이 어떤 Liveboard 시각화에서든 즉시 세부 데이터로 진입할 수 있는 기능. 최상위 요약에서 가장 세분화된 레코드까지 자유롭게 탐색 가능하다
- **Liveboards (실시간 대시보드)**: 실시간 데이터에 연결된 협업 대시보드. Note tiles, Cross Filters, In-app Commenting, Verified Liveboards(검증된 대시보드) 기능을 지원한다

## 아키텍처

### 에이전트 팀 아키텍처
```
사용자 자연어 질문
    ↓
Spotter 3 (핵심 에이전트)
├── 질문 파싱 · 의도 분석
├── 자기 검증 루프 (답변 품질 자동 평가 → 추가 분석 반복)
├── Python 코딩 · 예측 분석
└── 최종 답변 + 시각화 생성
    ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ SpotterModel  │  │ SpotterViz    │  │ SpotterCode   │
│ 시맨틱 모델    │  │ 대시보드 생성   │  │ 임베디드 코드   │
│ 자동 생성/관리  │  │ 최적 차트 선택  │  │ IDE 통합       │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Search Token 아키텍처
- ThoughtSpot의 고유한 검색 토큰(Search Token) 기반 아키텍처로, GPT/Gemini 등 외부 LLM과 결합하여 자연어를 분석 쿼리로 변환한다
- 데이터 모델에서 쿼리로의 변환(Data Model → Query Translation) 과정이 투명하게 표시된다
- SQL 생성 과정을 사용자에게 시각화하여 분석 결과의 신뢰도를 높인다

### 데이터 연결
- 주요 클라우드 데이터 웨어하우스(Snowflake, BigQuery, Redshift, Databricks 등)에 직접 연결
- 라이브 쿼리 방식으로 데이터 이동 없이 실시간 분석 수행
- Spotter 3부터 Slack, Salesforce 등 비정형 앱 데이터와도 통합

### 프로토콜 지원
- **MCP Server**: 외부 AI 플랫폼과의 연결을 위한 MCP 서버를 제공한다 (2025년 9월 발표)
- **REST API**: 임베디드 분석 및 외부 통합을 위한 다양한 REST API 제공
- **Mobile SDK**: 모바일 앱에 ThoughtSpot 분석을 임베딩할 수 있는 SDK 제공

## UI/UX 분석

### 메인 인터페이스 구성
- **Spotter 대화형 인터페이스**: 자연어로 질문을 입력하면 즉시 차트·테이블 형태로 결과를 반환하는 대화형 분석 환경
- **Liveboards**: 복수의 시각화를 배치한 실시간 대시보드. Note tiles, Cross Filters로 인터랙티브한 데이터 탐색 지원
- **Integrated Developer Playground**: SpotterCode와 연동된 개발자 전용 실험 환경

### 대화형 UI 패턴
- GPT/Gemini + Search Token 기반 자연어 처리로 높은 정확도의 Conversational BI(Ask Sage) 구현
- Starter questions 제안으로 분석 시작점을 안내하여 사용자 진입 장벽을 낮춤
- 멀티스텝 분석 진행 상태를 실시간으로 표시
- 어떤 차트에서든 Follow-up 질문이 가능하여 끊김 없는 분석 흐름을 유지

### Human-in-the-Loop 패턴
- **특허 출원 피드백 루프**: 단어·구문 단위의 세밀한 교정 인터페이스 제공
- **Human Expert Labeling UI**: 도메인 전문가가 모델의 용어 매핑과 비즈니스 규칙을 검증·수정할 수 있는 전용 UI
- **SpotterModel 검증**: AI가 자동 생성한 시맨틱 모델을 사람이 검토·승인하는 워크플로우

### 데이터 시각화
- **Best-fit Visualization 자동 선택**: 데이터 특성에 맞는 최적 차트 유형을 AI가 자동으로 결정
- **Drill-Anywhere**: 사전 정의 없이 어떤 시각화에서든 즉시 상세 데이터로 진입 가능
- **Liveboards 협업**: Verified Liveboards로 검증된 데이터 뷰를 조직 전체에 공유
- **예측 분석 시각화**: Spotter 3의 내장 Forecasting 기능으로 미래 예측 차트를 생성

## 경쟁 포지셔닝

### 강점
- **에이전틱 분석의 선도적 구현**: 4개 에이전트가 팀으로 협업하여 데이터 모델링부터 시각화·코드 생성까지 분석 라이프사이클 전체를 커버한다. 단순 NL-to-SQL을 넘어 완전한 에이전틱 분석 워크플로우를 구현했다
- **자기 검증 루프**: Spotter 3가 자체적으로 답변 품질을 평가하고 개선하는 메커니즘으로, 다른 NL-to-SQL 솔루션 대비 높은 응답 신뢰도를 제공한다
- **Drill-Anywhere의 자유도**: 사전 정의된 드릴 경로 없이 자유로운 데이터 탐색이 가능하여, 예상치 못한 분석 경로를 추구하는 비즈니스 사용자에게 강점이다
- **SpotterModel의 자동화**: Snowflake Intelligence의 수동 YAML 작성과 달리, AI가 시맨틱 모델을 자동 생성하여 초기 구축 비용을 대폭 줄인다
- **임베디드 분석 생태계**: SpotterCode, REST API, Mobile SDK를 통해 자사 제품에 분석을 쉽게 내장할 수 있다

### 약점
- **데이터 플랫폼 비종속**: 자체 데이터 저장소가 없어 외부 데이터 웨어하우스에 의존한다. 데이터 거버넌스는 원본 데이터 플랫폼에서 관리해야 한다
- **높은 가격 진입 장벽**: Enterprise 플랜 기준 연간 $100K-$500K+ 비용으로, 중소기업에게는 부담이 될 수 있다
- **Spotter 에이전트 GA 시기**: 4개 BI 에이전트(SpotterModel, SpotterViz, SpotterCode)의 GA가 2026년 초로 예정되어 아직 완전히 프로덕션 레디가 아니다
- **비정형 데이터 통합 초기 단계**: Spotter 3에서 Slack, Salesforce 등 비정형 소스를 지원하기 시작했으나, Glean 등 전용 지식 검색 플랫폼 대비 깊이가 부족하다

### 주요 경쟁사 비교
| 항목 | ThoughtSpot Spotter | Snowflake Intelligence | Tableau/Power BI |
|------|-------------------|----------------------|-----------------|
| 핵심 접근법 | 에이전틱 분석 (4 에이전트 팀) | 데이터 플랫폼 네이티브 NL-to-SQL | 전통적 BI + AI 보조 |
| 자연어 분석 | Search Token + LLM 하이브리드 | Semantic Model 기반 SQL 생성 | 자연어 질의 보조 기능 |
| 시맨틱 모델 | SpotterModel (AI 자동 생성) | YAML Semantic Model (수동 정의) | 데이터 모델 수동 구축 |
| 셀프서비스 수준 | 높음 (비기술 사용자 최적화) | 중간 (일부 SQL 지식 필요) | 중간 (대시보드 중심) |
| 드릴다운 | Drill-Anywhere (무제한) | 기본 Follow-up 질문 | 사전 정의 드릴 경로 |
| 가격 | $25-$50+/사용자/월 | 소비 기반 크레딧 | $15-$70/사용자/월 |
| 주요 대상 | 비즈니스 분석가, 셀프서비스 BI | Snowflake 기존 고객 | 전통적 BI 사용자 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — 크로스 제품 UI/UX 비교 테이블에서 ThoughtSpot Spotter 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] — Analytics 카테고리 벤치마크 대상

## 참고 자료

- [ThoughtSpot 공식 사이트](https://www.thoughtspot.com/)
- [ThoughtSpot Spotter 제품 페이지](https://www.thoughtspot.com/product/spotter)
- [ThoughtSpot BI Agents (Spotter, SpotterModel, SpotterViz, SpotterCode)](https://www.thoughtspot.com/product/agents)
- [ThoughtSpot Pricing](https://www.thoughtspot.com/pricing)
- [ThoughtSpot Blog: Introducing Spotter AI Analyst](https://www.thoughtspot.com/blog/introducing-spotter-ai-analyst)
- [ThoughtSpot Press: Four BI Agents Launch (2025-12)](https://www.thoughtspot.com/press-releases/thoughtspot-launches-four-bi-agents-that-work-as-a-team-to-deliver-modern-analytics)
- [ThoughtSpot Liveboards & Visualizations](https://www.thoughtspot.com/product/visualize)
- [ThoughtSpot Spotter Agents 분석 (TechTarget)](https://www.techtarget.com/searchbusinessanalytics/news/366636078/ThoughtSpot-automates-full-platform-with-new-Spotter-agents)
- [ThoughtSpot Agents 분석 (SiliconANGLE)](https://siliconangle.com/2025/12/10/thoughtspot-agents-aimed-automating-analytics-lifecycle/)
- [ThoughtSpot Pricing 분석 2026 (Luzmo)](https://www.luzmo.com/blog/thoughtspot-pricing)
- [ThoughtSpot Pricing 분석 (Upsolve AI)](https://upsolve.ai/blog/thoughtspot-pricing)
