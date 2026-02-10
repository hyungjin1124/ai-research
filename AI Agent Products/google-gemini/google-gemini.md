---
type: product-profile
product_id: google-gemini
product_name: Google Gemini
vendor: Google
category: B2C
tags:
  - AI-Agent
  - B2C
  - LLM-Native
  - MCP-Support
  - Agent-Builder
url: https://gemini.google.com
launched: 2023-12
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[A2UI 프로토콜 및 MCP-UI 비교]]"
---

# Google Gemini

## 개요

Google DeepMind이 개발한 멀티모달 네이티브 AI 플랫폼. 텍스트·이미지·비디오·오디오를 통합 처리하도록 설계된 모델(Gemini 3 Pro, 2.5 Flash 등)을 기반으로, B2C 어시스턴트(Gemini App)부터 개발자 API, 에이전트 플랫폼(Project Mariner, Jules)까지 풀스택 AI 에코시스템을 제공한다. Google Workspace 네이티브 통합이 핵심 차별점이며, 2026년 현재 주간 활성 사용자가 급성장하여 B2C AI 시장 점유율 2위(약 18%)를 차지하고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Google (DeepMind) |
| 출시일 | 2023-12 (Gemini 1.0), 2024-12 (2.0), 2025-03 (2.5) |
| 가격 | 무료 / AI Pro $19.99/월 / AI Ultra ~$250/월 |
| 플랫폼 | Web, Android, iOS, Chrome 확장, Google Workspace |
| 공식 사이트 | https://gemini.google.com |

## 핵심 기능

- **멀티모달 네이티브 처리**: 이미지, 비디오, 오디오, 코드를 단일 모델에서 통합 이해·생성. 텍스트 응답에 이미지·TTS 오디오를 네이티브로 혼합 출력 가능
- **Deep Research**: 멀티스텝 강화학습 기반 리서치 에이전트. 자율적으로 쿼리 설계 → 검색 → 지식 갭 분석 → 재검색을 반복하여 종합 보고서 생성. HLE·BrowseComp 벤치마크 SOTA 달성
- **Gems (커스텀 에이전트)**: 사용자가 직접 전문가 페르소나를 정의하여 맞춤형 AI 에이전트를 생성. 코딩 멘토, 글쓰기 코치, 브레인스토밍 파트너 등으로 활용
- **Project Mariner (브라우저 에이전트)**: Chrome 확장 기반으로 웹 페이지의 픽셀·DOM 요소를 이해하여 브라우저 작업 자동화. 최대 10개 병렬 태스크 스트림 지원, Teach & Repeat 워크플로우 학습 기능
- **Jules (코딩 에이전트)**: GitHub 워크플로우에 통합되는 비동기 자율 코딩 에이전트. 이슈 분석 → 계획 수립 → 코드 작성 → PR 생성까지 자동 수행. 테스트 작성, 버그 수정, 의존성 업데이트 등 지원
- **Canvas**: 대화형 코드/문서 편집 공간. Deep Research 결과를 인터랙티브 시각화, 퀴즈 등으로 변환 가능
- **1M 토큰 컨텍스트 윈도우**: Gemini 3 Pro 기준 100만 토큰 컨텍스트로 대규모 문서·코드베이스 분석에 강점

## 아키텍처

### 모델 라인업
| 모델 | 특징 | 용도 |
|------|------|------|
| Gemini 3 Pro | 최상위 성능, 1M 토큰, 멀티모달 | 복잡한 추론, 에이전트 |
| Gemini 2.5 Flash | 고속·저비용, 사고(Thinking) 모드 내장 | 실시간 응답, 대량 처리 |
| Gemini 2.5 Deep Think | 깊은 추론 특화 | 수학·과학 문제 |

### 에이전트 아키텍처
- **네이티브 도구 호출**: Google Search, 코드 실행, 사용자 정의 함수를 모델이 직접 호출 (compositional function-calling)
- **Interactions API**: 모델·에이전트와 상호작용하기 위한 통합 인터페이스
- **A2UI (Agent-to-UI)**: Google이 주도하는 오픈 프로젝트로, 에이전트가 대화 맥락에 최적화된 UI를 동적 생성하는 프로토콜. 크로스 플랫폼 호환 지원

### 프로토콜 지원
- **MCP**: 서드파티 도구/데이터 소스 연결용 프로토콜 지원
- **A2A (Agent-to-Agent)**: Google이 제안한 에이전트 간 통신 프로토콜

### Google 에코시스템 통합
- Google Workspace (Gmail, Docs, Sheets, Slides, Calendar) 네이티브 연동
- Google Search, Maps, YouTube, Finance 등 자사 서비스 실시간 접근
- Android 시스템 레벨 통합 (Gemini Nano 온디바이스)

## UI·UX 분석

### 메인 인터페이스 구성
- **Chat + Canvas 이중 패널**: 좌측 대화형 채팅 + 우측 Canvas 영역에서 코드 편집·문서 작성·시각화 표시
- **Dynamic View (Generative UI)**: 프롬프트에 맞춰 실시간으로 커스텀 인터랙티브 UI를 코딩·렌더링. 탭, 스크롤, 드릴다운 등 정적 텍스트를 넘어서는 동적 응답 제공
- **Visual Layout**: 정보를 카드, 테이블, 비교 뷰 등으로 자동 구조화하여 표시

### 대화형 UI 패턴
- 멀티턴 대화 + 후속 질문 제안
- Deep Research 진행 시 실시간 계획 표시 → 사용자 승인 후 실행 (Human-in-the-Loop)
- 답변 내 출처·근거 인라인 표시

### 에이전트 UI 패턴
- **Gemini Agent**: 멀티스텝 태스크를 Google 앱(Calendar, Gmail, Reminders)과 연결하여 수행. 단계별 진행 상황 시각화
- **Project Mariner**: 브라우저 내 사이드 패널에서 작업 진행 상황 표시, 사용자 확인 필요 시 pause & ask 패턴

### 데이터 시각화
- Canvas에서 차트, 대시보드, 인터랙티브 시각화 생성
- Deep Research 결과를 퀴즈, 타임라인 등 다양한 포맷으로 변환

## 경쟁 포지셔닝

### 강점
- **멀티모달 네이티브**: 이미지·비디오·오디오·텍스트 통합 처리 능력에서 경쟁 우위. 볼트온(bolt-on) 방식이 아닌 처음부터 멀티모달로 설계
- **1M 토큰 컨텍스트**: Claude(200K), ChatGPT(128K) 대비 압도적 컨텍스트 길이
- **Google 에코시스템**: Workspace, Search, Android 등 자사 서비스와의 깊은 통합. 일상 업무 자동화에 유리
- **무료 티어 관대**: API 무료 티어에서 일일 1,000건 요청 허용
- **Generative UI**: 프롬프트에 따라 동적으로 UI를 생성하는 차별화된 응답 방식

### 약점
- **논리적 추론**: 복잡한 논리 문제에서 Claude 대비 약세
- **코딩 정밀도**: SWE-bench 기준 Claude Opus(80.9%)에 뒤처짐(76.8%)
- **할루시네이션**: 장문 생성 시 Claude보다 사실 정확도 낮다는 평가
- **프라이버시 우려**: Google 에코시스템 의존도로 인한 데이터 프라이버시 민감도

### 주요 경쟁사 비교
| 항목 | Google Gemini | Claude | ChatGPT |
|------|-------------|--------|---------|
| 최대 컨텍스트 | 1M 토큰 | 200K 토큰 | 128K 토큰 |
| 멀티모달 | 네이티브 (영상·오디오 포함) | 이미지 입력 | 이미지·오디오 입출력 |
| 코딩 (SWE-bench) | 76.8% | 80.9% | 74.9% |
| 가격 (Pro) | $19.99/월 | $20/월 | $20/월 |
| 최상위 플랜 | AI Ultra ~$250/월 | Max $200/월 | Pro $200/월 |
| 브라우저 에이전트 | Project Mariner | Claude in Chrome | Operator |
| 코딩 에이전트 | Jules | Claude Code | Codex |
| 에코시스템 통합 | Google Workspace 깊은 통합 | MCP 기반 확장 | Microsoft/OpenAI 파트너십 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — 크로스 제품 UI/UX 비교 테이블에서 Google 관련 분석 참조
- [[A2UI 프로토콜 및 MCP-UI 비교]] — Google이 주도하는 A2UI 오픈 프로젝트 분석

## 참고 자료

- [Google Gemini 공식 사이트](https://gemini.google.com)
- [Gemini API 개발자 문서](https://ai.google.dev/gemini-api/docs)
- [Google Blog: Gemini 2.0 — A new AI model for the agentic era](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)
- [Google Blog: Gemini 3 brings upgraded smarts](https://blog.google/products-and-platforms/products/gemini/gemini-3-gemini-app/)
- [Google I/O 2025: Updates to Gemini 2.5](https://blog.google/technology/google-deepmind/google-gemini-updates-io-2025/)
- [Jules — An Autonomous Coding Agent](https://jules.google)
- [Google Blog: Deep Research Agent via Gemini API](https://blog.google/technology/developers-tools/deep-research-agent-gemini-api/)
- [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)
- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Gemini Pricing 2026 비교 (Finout)](https://www.finout.io/blog/gemini-pricing-in-2026)
