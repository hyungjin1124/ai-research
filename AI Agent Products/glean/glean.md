---
type: product-profile
product_id: glean
product_name: Glean
vendor: Glean
category: Knowledge
tags:
  - AI-Agent
  - Knowledge
  - Agent-Builder
  - MCP-Support
  - Enterprise-Search
url: https://www.glean.com
launched: 2019-01
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
---

# Glean

## 개요

Glean은 기업 내부의 모든 앱·문서·대화를 통합 검색·이해하는 Work AI 플랫폼이다. 100개 이상의 SaaS 커넥터와 독자적인 Enterprise Graph(지식 그래프 + 개인 그래프)를 기반으로, AI 기반 엔터프라이즈 검색·AI 어시스턴트·커스텀 에이전트 빌더를 제공한다. 2025년 ARR $100M을 돌파하고 기업 가치 $7.2B에 도달하며, 엔터프라이즈 AI 검색 시장의 선두 주자로 자리잡았다. 기존 데이터 소스의 권한 체계를 그대로 상속하는 보안 모델이 핵심 차별점이다.

| 항목 | 내용 |
|------|------|
| 회사 | Glean |
| 출시일 | 2019-01 (설립), 2022 (GA), 2025-09 (3세대 어시스턴트) |
| 가격 | 비공개 (사용자당 ~$50/월 추정, 중앙값 계약 ~$65K/년) |
| 플랫폼 | Web, Chrome 확장, Slack/Teams 통합, API |
| 공식 사이트 | https://www.glean.com |

## 핵심 기능

- **AI 기반 엔터프라이즈 검색**: 시맨틱 검색 + 어휘 검색을 결합하여 기업 고유의 약어·도메인 용어를 이해. Enterprise Graph가 사용자의 역할·팀·프로젝트에 맞춰 검색 결과를 개인화하여 제공
- **3세대 AI 어시스턴트 (Agentic Engine 2)**: 멀티스텝 전략을 자율 수립하고 서브 에이전트를 병렬 조율하여 복잡한 업무를 수행. 누락된 컨텍스트를 자동 탐색하고 진행 상황을 단계별 평가하여 최종 결과물을 생성. 94% 태스크 완성도 달성
- **커스텀 AI 에이전트 빌더**: 자연어로 전문 에이전트를 정의·구축하는 노코드 에이전트 빌더. Agents API(LangChain Agent Protocol 기반)를 통해 프로그래밍 방식의 에이전트 개발도 지원. 20개 이상의 프리빌트 에이전트 제공
- **Enterprise Graph**: 기업 내 사람·콘텐츠·워크플로우·앱 간의 관계를 동적으로 모델링하는 지능 레이어. 기존 지식 그래프에 개인별 Personal Graph를 추가하여 각 직원의 프로젝트·협업자·업무 스타일까지 반영
- **오픈 에이전트 플랫폼 & MCP**: 원격 MCP 서버를 통해 Glean Search·Assistant·Agents에 대한 크로스 플랫폼 에이전트 상호운용성 제공. 20개 이상의 검증된 MCP 서버 디렉터리 제공, 자체 MCP 호스트 연결도 지원

## 아키텍처

### 핵심 엔진
| 구성 요소 | 설명 |
|-----------|------|
| Enterprise Graph | 지식 그래프 + Personal Graph로 구성된 기업 지능 레이어. 권한·활동·메타데이터를 포함한 동적 관계 모델링 |
| Agentic Engine 2 | 적응형 계획 수립 → 스마트 도구 사용 → 크로스 시스템 실행의 에이전트 워크플로우 엔진 |
| 검색 엔진 | 시맨틱 + 어휘 하이브리드 검색. 실시간 인덱싱으로 원본 앱의 변경 사항을 즉시 반영 |

### 커넥터 & 통합
- **100개 이상 SaaS 커넥터**: Google Workspace, Microsoft 365, Slack, Salesforce, Jira, Confluence, GitHub, Notion 등 주요 업무 앱 네이티브 지원
- **커넥터 프레임워크 & Indexing API**: 커스텀 데이터 소스를 프로그래밍 방식으로 연결. 콘텐츠뿐 아니라 메타데이터·신원 정보·권한 정보·활동 데이터까지 수집
- **커스텀 데이터 소스**: 조직 고유의 내부 시스템이나 데이터베이스를 Glean에 통합

### 프로토콜 지원
- **MCP (Model Context Protocol)**: 호스팅 MCP 서버로 Glean 검색·어시스턴트·에이전트에 대한 보안 에이전트 상호운용성 제공. 20개 이상의 검증된 인기 MCP 서버 디렉터리를 큐레이션하여 제공
- **LangChain Agent Protocol (AP)**: Agents API가 LangChain AP를 따르며, 개발자가 선호하는 프레임워크 내에서 에이전트를 프로그래밍 방식으로 생성

### 보안 아키텍처
- **권한 상속 모델**: 원본 앱의 접근 권한을 그대로 상속·적용하여 사용자는 자신이 접근 가능한 데이터만 검색·열람 가능
- **실시간 권한 동기화**: 원본 앱의 권한 변경이 즉시 Glean 검색 결과에 반영
- **규제 준수**: SOC 2 Type II, GDPR, HIPAA, ISO 27001 인증. 싱글 테넌시 아키텍처

## UI·UX 분석

### 메인 인터페이스 구성
- **통합 검색 바**: Google 스타일의 단일 검색 입력으로 전사 앱·문서·대화를 즉시 검색. 검색 결과에 출처·권한·최근 활동 정보를 인라인 표시
- **AI 어시스턴트 채팅**: 검색과 대화형 AI를 통합한 인터페이스. 멀티턴 대화를 통해 복잡한 질문에 대한 종합적 답변 생성
- **에이전트 워크스페이스**: 커스텀 에이전트를 탐색·생성·관리하는 전용 공간

### 대화형 UI 패턴
- **출처 인라인 표시**: 모든 답변에 근거가 된 문서·메시지·페이지를 인라인으로 표시하여 검증 가능
- **개인화된 응답**: Personal Graph 기반으로 사용자의 역할·프로젝트·협업 맥락에 맞춘 답변 제공
- **멀티스텝 진행 표시**: Agentic Engine이 복잡한 질문을 처리할 때 계획 수립 → 정보 수집 → 분석 → 결과 도출 과정을 단계별 시각화

### 에이전트 UI 패턴
- **에이전트 빌더**: 자연어 프롬프트로 에이전트의 목적·지식·도구·행동을 정의하는 노코드 인터페이스
- **에이전트 디렉터리**: 프리빌트 에이전트를 카테고리별로 탐색·활성화하는 카탈로그 UI

### 배포 채널
- 웹 앱 (독립 인터페이스)
- Chrome 확장 프로그램 (브라우저 내 검색 오버레이)
- Slack/Teams 통합 (메시징 플랫폼 내 AI 어시스턴트)
- API (커스텀 앱·워크플로우 임베딩)

## 경쟁 포지셔닝

### 강점
- **엔터프라이즈 검색 선구자**: 100개 이상 SaaS 앱을 네이티브로 연결하는 가장 넓은 커넥터 생태계. 경쟁사 대비 깊은 통합 수준(메타데이터, 권한, 활동 데이터까지 수집)
- **Enterprise Graph**: 지식 그래프 + Personal Graph의 이중 구조로 기업 전체의 업무 맥락과 개인별 업무 패턴을 동시에 모델링. 경쟁 솔루션 대비 높은 개인화 수준
- **보안 모델**: 원본 앱의 권한을 실시간 상속하는 제로 트러스트 접근 방식. 엔터프라이즈 보안 요구사항에 가장 적합
- **벤더 중립성**: 특정 에코시스템(Microsoft, Google)에 종속되지 않는 독립 플랫폼. 이종 SaaS 환경을 운영하는 기업에 최적
- **MCP 오픈 플랫폼**: 호스팅 MCP 서버와 Agent Protocol로 외부 에이전트와의 상호운용성 선도

### 약점
- **가격 비투명성**: 공개 가격표 없이 영업팀 협의 필요. 예상 비용(~$50/유저/월)은 Microsoft Copilot($30/유저/월) 대비 높음
- **자체 LLM 부재**: 서드파티 LLM(GPT-4, Claude 등)에 의존. 모델 성능·비용에 대한 직접적 통제 제한
- **B2C 부재**: 순수 엔터프라이즈 솔루션으로 소비자 시장 접점 없음. 브랜드 인지도에서 OpenAI·Google 대비 열세
- **구현 복잡성**: 100개 이상 커넥터 설정·권한 매핑·Enterprise Graph 학습에 초기 구축 시간 소요

### 주요 경쟁사 비교
| 항목 | Glean | Microsoft Copilot | Google Gemini (Workspace) |
|------|-------|-------------------|--------------------------|
| 포지셔닝 | 벤더 중립 엔터프라이즈 AI 검색 | Microsoft 365 네이티브 AI | Google Workspace 네이티브 AI |
| 커넥터 | 100개+ SaaS 앱 | Microsoft 365 중심 | Google Workspace 중심 |
| 에이전트 빌더 | 노코드 + API (Agent Protocol) | Copilot Studio | Gems + Agent Builder |
| 보안 모델 | 원본 권한 실시간 상속 | Microsoft Entra 기반 | Google Workspace 권한 |
| 가격 | ~$50/유저/월 (추정) | $30/유저/월 | $30/유저/월 |
| MCP 지원 | 호스팅 MCP 서버 + 디렉터리 | 제한적 | MCP + A2A + A2UI |
| 기업 가치 | $7.2B (2025-06) | Microsoft 자회사 | Google 자회사 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — 크로스 제품 비교에서 Glean의 엔터프라이즈 검색 포지셔닝 분석

## 참고 자료

- [Glean 공식 사이트](https://www.glean.com)
- [Glean Work AI Platform 개요](https://www.glean.com/product/overview)
- [Glean AI Agents](https://www.glean.com/product/ai-agents)
- [Glean 커넥터 목록](https://www.glean.com/connectors)
- [Glean Developer Platform](https://developers.glean.com/)
- [Glean Blog: 3세대 AI 어시스턴트 & Enterprise Graph 발표](https://www.glean.com/blog/live-fall-25-main)
- [Glean Blog: Agentic Engine 2 성능](https://www.glean.com/blog/live-fall-25-agentic-engine2-performance)
- [Glean Blog: 오픈 에이전트 플랫폼](https://www.glean.com/blog/open-agent-platform)
- [Glean Press: 에이전트 플랫폼 확장 발표](https://www.glean.com/press/glean-expands-horizontal-agent-platform-delivers-dozens-of-agents-and-open-interoperability-across-the-enterprise)
- [CNBC: Glean $7.2B 기업가치 도달](https://www.cnbc.com/2025/06/10/glean-gen-ai-search-startup-raises-150-million-at-7-billion-value.html)
