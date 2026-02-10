---
type: product-profile
product_id: openai
product_name: OpenAI
vendor: OpenAI
category: B2C
tags:
  - AI-Agent
  - B2C
  - LLM-Native
url: https://chatgpt.com
launched: 2022-11
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
---

# OpenAI

## 개요

OpenAI가 개발한 세계 최대 B2C AI 플랫폼. GPT-5.2(플래그십)와 o3/o4-mini(추론 특화) 모델을 기반으로, 대화형 어시스턴트(ChatGPT)부터 브라우저 에이전트(ChatGPT Agent, 구 Operator), 자율 코딩 에이전트(Codex), 실시간 음성 에이전트(Realtime API)까지 가장 넓은 제품 스펙트럼을 보유하고 있다. 2022년 11월 ChatGPT 출시로 생성형 AI 시장을 개척한 선구자이며, 2026년 현재 주간 활성 사용자 수 기준 B2C AI 시장 점유율 1위를 유지하고 있다. Canvas, Memory, Custom GPTs, Voice Mode 등 풍부한 사용자 경험 기능과 Microsoft와의 전략적 파트너십이 핵심 경쟁력이다.

| 항목 | 내용 |
|------|------|
| 회사 | OpenAI |
| 출시일 | 2022-11 (ChatGPT), 2024-05 (GPT-4o), 2025-08 (GPT-5), 2025-12 (GPT-5.2) |
| 가격 | 무료 / Plus $20/월 / Pro $200/월 / Team $25~30/월/인 |
| 플랫폼 | Web, macOS, Windows, iOS, Android, API |
| 공식 사이트 | https://chatgpt.com |

## 핵심 기능

- **GPT-5.2 (Auto/Instant/Thinking)**: OpenAI의 최신 플래그십 모델. 쿼리 복잡도에 따라 연산량을 자동 할당하는 적응형 컴퓨팅(Adaptive Computation) 내장. Auto 모드에서 자동 판단, Instant 모드에서 즉시 응답, Thinking 모드에서 깊은 추론을 수행. Plus 사용자 기준 주당 3,000건 Thinking 메시지 허용
- **o3/o4-mini (추론 모델)**: 강화학습 기반 깊은 추론 특화 모델. o3-pro는 가장 신뢰성 높은 응답을 위해 장시간 사고하도록 설계. o4-mini는 소형·멀티모달 최적화로 속도와 추론 능력의 균형을 달성. 웹 검색, 파일 분석, 시각 입력 추론, Python 실행, Memory 활용 등 ChatGPT 도구 전체 접근 가능
- **Canvas**: 대화 옆에 별도 편집 영역을 제공하는 협업 인터페이스. 코드 작성·문서 편집을 실시간으로 수행하며, 인라인 수정·하이라이트·버전 관리를 지원. Deep Research 결과를 인터랙티브 형태로 변환하는 용도로도 활용
- **ChatGPT Agent (구 Operator)**: 2025년 1월 Operator로 출시, 8월 ChatGPT Agent로 통합 후 Operator 종료. Computer-Using Agent(CUA) 모델 기반으로 GPT-4o의 비전 능력과 강화학습을 결합. 스크린샷을 통해 웹 페이지를 인식하고 마우스·키보드로 상호작용하여 항공권 검색, 레스토랑 예약, 온라인 쇼핑 등 브라우저 태스크를 자율 수행. WebVoyager 87%, WebArena 58.1%, OSWorld 38.1% 성공률 달성
- **Codex (자율 코딩 에이전트)**: 클라우드 샌드박스 환경에서 리포지토리를 로드하여 기능 구현·버그 수정·대규모 리팩토링·코드 리뷰·PR 생성을 자율 수행하는 비동기 에이전트. GPT-5.3-Codex는 GPT-5.2 대비 25% 빠른 처리 속도를 제공하며, 테스트 중 7시간 이상 독립 작업 수행 사례가 보고됨. 스크린샷·디자인 스펙 첨부, 별도 에이전트의 코드 리뷰 기능을 지원. Codex CLI(오픈소스, Rust 기반)로 로컬 터미널에서도 사용 가능
- **Custom GPTs**: 사용자가 직접 전문가 페르소나·지식·도구를 정의하여 맞춤형 AI를 생성. GPT-4o, o3, o4-mini 등 전체 모델 선택 가능. Voice Mode 연동으로 음성 대화형 커스텀 GPT 구현 가능. GPT Store를 통해 퍼블리싱·검색·공유
- **Voice Mode**: 실시간 음성 대화 인터페이스. gpt-realtime 모델 기반의 Speech-to-Speech 아키텍처로 고객 지원, 개인 비서, 교육 등에 특화. Plus 사용자는 거의 무제한, Free 사용자도 하루 수 시간 이용 가능. 사용자 지시에 따라 말하기 스타일(길이, 속도, 톤) 자동 조절
- **Memory**: 대화 간 사용자 선호·배경 정보를 지속적으로 기억하여 개인화된 응답 제공. 설정에서 켜기/끄기 가능. 기억된 내용을 사용자가 직접 확인·삭제 가능

## 아키텍처

### 모델 라인업
| 모델 | API 가격 (입력/출력, /MTok) | 특징 | 용도 |
|------|---------------------------|------|------|
| GPT-5.2 | 추론 기반 과금 | 적응형 컴퓨팅, 최신 플래그십 | 복잡한 추론, 에이전트, 멀티모달 |
| GPT-5 | $1.25 / $10 | 고성능 범용 | 고급 분석, 코딩, 리서치 |
| GPT-5 Mini | $0.25 / $2 | 비용 효율 | 대량 처리, 일반 업무 |
| GPT-5 Nano | $0.05 / $0.40 | 초저비용 | 분류, 요약, 경량 태스크 |
| o3-pro | 프리미엄 과금 | 최고 신뢰성 추론 | 수학·과학, 복잡한 논리 |
| o4-mini | 경량 과금 | 소형 멀티모달 추론 | 빠른 추론, 비용 효율 태스크 |
| GPT-5.3-Codex | Codex 전용 | GPT-5.2 + 코딩 최적화, 25% 빠름 | 자율 소프트웨어 엔지니어링 |

### 에이전트 아키텍처
- **Computer-Using Agent (CUA)**: GPT-4o 비전 + 강화학습 결합. 스크린샷 기반 웹 페이지 인식 → 마우스·키보드 액션 생성 → 결과 검증의 에이전트 루프. 민감 작업 시 사용자 확인 요청, 막힐 경우 사용자에게 제어권 반환
- **Codex Sandbox**: 각 태스크를 독립 클라우드 샌드박스에서 실행. 리포지토리 프리로드 → 계획 수립 → 코드 작성·테스트 → 결과 제출의 비동기 워크플로우
- **Responses API**: Assistants API를 대체하는 차세대 통합 인터페이스. 도구 호출(Function Calling), 웹 검색, 코드 실행, 파일 분석을 단일 API에서 처리. Assistants API는 Responses API 기능 완전 이전 후 2026년 중 종료 예정
- **Realtime API**: gpt-realtime 모델 기반 Speech-to-Speech 스트리밍. 고객 지원, 교육 등 실시간 음성 에이전트 구축용

### 프로토콜 지원
- **MCP**: 2025년 3월부터 Agents SDK, Responses API, ChatGPT Desktop에서 MCP 지원. 서드파티 도구 연결용 표준 프로토콜로 채택
- **Function Calling**: OpenAI 자체 도구 호출 프로토콜. JSON Schema 기반 함수 정의 → 모델이 파라미터 생성 → 외부 실행 → 결과 반환

### 플랫폼 통합
- **Microsoft 에코시스템**: Azure OpenAI Service를 통한 엔터프라이즈 배포. Microsoft 365 Copilot과의 간접적 연결
- **Google Workspace**: Gmail, Google Calendar, Google Contacts와 ChatGPT 직접 연동 (2025년 추가)
- **서드파티 플러그인/GPT Actions**: Custom GPTs의 Actions 기능을 통해 외부 API 연동. Zapier, Slack 등 다양한 서비스와 통합 가능

## UI/UX 분석

### 메인 인터페이스 구성
- **Chat + Canvas 이중 패널**: 좌측 대화형 채팅 + 우측 Canvas 영역에서 코드 편집·문서 작성. Canvas 내 인라인 수정, 하이라이트, 코멘트, 버전 히스토리 지원
- **사이드바 내비게이션**: 대화 히스토리를 시간순·카테고리별로 구성. GPTs, Projects 등 접근점 제공
- **모델 선택기**: 대화 시작 시 GPT-5.2, o3, o4-mini 등 모델 선택. Composer 영역의 Tools 드롭다운에서 Agent Mode 활성화 가능

### 대화형 UI 패턴
- **멀티모달 입력**: 텍스트, 이미지, 파일 업로드, 음성 입력을 통합 Composer에서 처리
- **Thinking 시각화**: o3/GPT-5.2 Thinking 모드에서 추론 과정을 접이식 블록으로 표시
- **Memory 표시**: 대화 중 기억된 정보를 활용할 때 인라인으로 참조 표시. 사용자가 기억 항목을 직접 관리
- **후속 질문 제안**: 응답 하단에 관련 후속 질문 칩을 표시하여 대화 흐름 유도

### 에이전트 UI 패턴
- **ChatGPT Agent**: Composer의 Tools 드롭다운에서 Agent Mode를 선택하여 활성화. 웹 브라우징, 작업 실행 중 진행 상황을 단계별로 표시. 민감 작업(로그인, CAPTCHA) 시 사용자에게 제어권 반환하는 Human-in-the-Loop 패턴
- **Codex**: 별도 Codex 인터페이스에서 태스크 생성 → 샌드박스 실행 → 결과(diff, PR) 확인의 비동기 워크플로우. 스크린샷/디자인 스펙 첨부 기능으로 시각적 요구사항 전달

### Custom GPTs 경험
- **GPT Builder**: 자연어 대화를 통해 Custom GPT를 구성하는 인터랙티브 빌더. 이름, 설명, 지시문, 지식 파일, Actions(API 연동)를 단계적으로 설정
- **GPT Store**: 커뮤니티가 만든 GPT를 검색·탐색·사용하는 마켓플레이스. 카테고리별 분류, 인기순 정렬, 리뷰 시스템

## 경쟁 포지셔닝

### 강점
- **시장 지배력**: B2C AI 시장 점유율 1위. 가장 큰 사용자 베이스와 브랜드 인지도를 보유하며, "ChatGPT"가 AI 챗봇의 대명사로 자리잡음
- **모델 라인업 다양성**: GPT-5.2(범용), o3(깊은 추론), o4-mini(경량 추론), GPT-5-Codex(코딩 특화) 등 용도별 세분화된 모델 포트폴리오. 가격대도 $0.05~프리미엄까지 폭넓게 커버
- **멀티모달 리더십**: 이미지·오디오 입출력, 실시간 Speech-to-Speech(gpt-realtime), 비전 기반 에이전트(CUA) 등 멀티모달 역량에서 가장 넓은 스펙트럼
- **음성 에이전트**: gpt-realtime 기반의 프로덕션 레벨 음성 에이전트 API. 고객 지원, 교육 등 실시간 음성 대화 유스케이스에서 경쟁사 대비 선점
- **에코시스템**: Custom GPTs + GPT Store로 사용자 생성 에이전트 마켓플레이스 구축. Microsoft/Azure 파트너십으로 엔터프라이즈 채널 확보

### 약점
- **코딩 벤치마크**: SWE-bench Verified 기준 GPT-5.2의 80.0%는 Claude Sonnet 5(82.1%) 대비 소폭 열세
- **안전성 논란**: 빠른 출시 주기에 따른 안전성 검증 우려. 할루시네이션 이슈에서 Claude 대비 약간 높은 비율이라는 평가
- **프로토콜 독자성 부재**: MCP는 Anthropic 주도, A2A/A2UI는 Google 주도. OpenAI 자체 표준 프로토콜 부재로 생태계 표준 주도권에서 후발
- **가격 부담**: Pro $200/월은 Claude Max($200/월)와 동일하나, Gemini AI Pro($19.99/월) 대비 중간 티어(Plus $20/월)에서의 기능 차별화가 약함
- **컨텍스트 윈도우**: 128K 토큰으로 Claude(200K), Gemini(1M) 대비 가장 짧음

### 주요 경쟁사 비교
| 항목 | ChatGPT (OpenAI) | Claude | Google Gemini |
|------|-------------------|--------|---------------|
| 최대 컨텍스트 | 128K 토큰 | 200K (Sonnet 5: 1M) | 1M 토큰 |
| 멀티모달 | 이미지·오디오 입출력, 실시간 음성 | 이미지 입력 | 네이티브 (영상·오디오 포함) |
| 코딩 (SWE-bench) | 80.0% (GPT-5.2) | 82.1% (Sonnet 5) | 76.8% |
| 가격 (중간 티어) | Plus $20/월 | Pro $20/월 | AI Pro $19.99/월 |
| 최상위 플랜 | Pro $200/월 | Max $200/월 | AI Ultra ~$250/월 |
| 브라우저 에이전트 | ChatGPT Agent (CUA) | Claude in Chrome | Project Mariner |
| 코딩 에이전트 | Codex (클라우드 샌드박스) | Claude Code (CLI) | Jules (GitHub 통합) |
| 음성 에이전트 | gpt-realtime (S2S) | - | Gemini Live |
| 커스텀 에이전트 | Custom GPTs + GPT Store | Projects + Styles | Gems |
| 프로토콜 | MCP (채택), Function Calling | MCP (창안·주도) | MCP + A2A + A2UI |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 UI/UX 비교 테이블에서 OpenAI/ChatGPT 관련 분석 참조

## 참고 자료

- [ChatGPT 공식 사이트](https://chatgpt.com)
- [OpenAI API 개발자 문서](https://platform.openai.com/docs)
- [OpenAI: Introducing Operator](https://openai.com/index/introducing-operator/)
- [OpenAI: Introducing ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/)
- [OpenAI: Computer-Using Agent](https://openai.com/index/computer-using-agent/)
- [OpenAI: Introducing Codex](https://openai.com/index/introducing-codex/)
- [OpenAI: Introducing GPT-5.2-Codex](https://openai.com/index/introducing-gpt-5-2-codex/)
- [Codex CLI GitHub Repository](https://github.com/openai/codex)
- [OpenAI: Introducing gpt-realtime](https://openai.com/index/introducing-gpt-realtime/)
- [OpenAI API Pricing](https://openai.com/api/pricing/)
- [ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [OpenAI for Developers in 2025](https://developers.openai.com/blog/openai-for-developers-2025/)
