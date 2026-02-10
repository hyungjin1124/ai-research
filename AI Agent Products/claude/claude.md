---
type: product-profile
product_id: claude
product_name: Claude
vendor: Anthropic
category: B2C
tags:
  - AI-Agent
  - B2C
  - LLM-Native
  - MCP-Support
url: https://claude.ai
launched: 2024-03
last_updated: 2026-02-09
status: in-progress
related:
  - "[[Claude Cowork 개요]]"
  - "[[Claude Cowork UI 분석]]"
  - "[[Claude Cowork 플랜 아키텍처]]"
  - "[[Claude Cowork 데모 시나리오]]"
  - "[[AI 에이전트 서비스 서베이 (2025-2026)]]"
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
---

# Claude

## 개요

Anthropic이 개발한 안전성 중심(Constitutional AI) LLM 플랫폼. 텍스트 추론, 코딩, 분석에 특화된 모델 라인업(Opus 4.5/4.6, Sonnet 4.5/5, Haiku 4.5)을 기반으로, B2C 어시스턴트(claude.ai)부터 CLI 코딩 에이전트(Claude Code), 데스크톱 에이전트(Claude Cowork), 브라우저 자동화(Claude in Chrome)까지 풀스택 에이전트 생태계를 구축하고 있다. Anthropic이 직접 창안한 MCP(Model Context Protocol)가 2025년 업계 표준으로 부상하면서, 도구 연결 생태계의 사실상 표준 제정자(de facto standard setter)로 자리잡았다. 2026년 2월 현재, SWE-bench Verified 80.9%(Opus 4.5)로 코딩 벤치마크 최상위권을 유지하며, Claude Code 매출이 2025년 7월 기준 전년 대비 5.5배 성장하는 등 개발자 시장에서 강력한 입지를 확보하고 있다.

| 항목     | 내용                                                             |
| ------ | -------------------------------------------------------------- |
| 회사     | Anthropic                                                      |
| 출시일    | 2024-03 (Claude 3), 2025-06 (Claude 4), 2025-11 (Claude 4.5)   |
| 가격     | 무료 / Pro $20/월 / Max 5x $100/월 / Max 20x $200/월                |
| 플랫폼    | Web, macOS, Windows, iOS, Android, Chrome 확장, CLI(Claude Code) |
| 공식 사이트 | https://claude.ai                                              |

## 핵심 기능

- **Extended Thinking (확장 사고)**: Claude 4.5 시리즈에 도입된 핵심 기능으로, 최종 응답 전에 내부 추론 블록을 생성하여 복잡한 문제 해결, 멀티스텝 코딩, 심층 분석 작업에서 정확도를 크게 향상시킨다. 사용자에게 사고 과정의 요약본을 투명하게 표시하여 신뢰도를 높인다
- **Artifacts (아티팩트)**: 대화 중 생성되는 코드, 문서, 시각화, 인터랙티브 앱 등을 별도 패널에 실시간 렌더링하는 기능. 15줄 이상의 실질적 콘텐츠를 독립 윈도우에서 편집·수정·재사용할 수 있으며, 2025년 6월 업데이트로 원클릭 웹 임베딩 기능이 추가되었다. 모든 사용자(무료 포함)가 이용 가능
- **Projects (프로젝트)**: 특정 업무·주제별 맞춤형 워크스페이스. 프로젝트당 최대 200K 토큰(약 500페이지 분량)의 문서·코드·지식을 상시 컨텍스트로 유지하며, 프로젝트별 커스텀 지시(Custom Instructions)를 설정하여 응답 톤·역할·포맷을 제어할 수 있다
- **Claude Code (CLI 코딩 에이전트)**: 2025년 2월 출시, 5월 GA. 터미널에서 직접 코딩 작업을 위임하는 에이전틱 CLI 도구. 코드 읽기·수정·실행, 파일 시스템 탐색, Git 워크플로우(커밋·PR 생성), MCP 서버 연결을 통한 외부 도구 통합을 지원한다. 2025년 7월 기준 매출 5.5배 성장으로 엔터프라이즈 개발자 채택이 급증
- **Claude Cowork (데스크톱 에이전트)**: 2026년 1월 Research Preview로 출시. Claude Code와 동일한 에이전틱 기반을 공유하되, 비개발자/일반 업무 사용자 대상의 GUI 에이전트. VM 샌드박스 내에서 로컬 파일 접근(허용 폴더 한정), 커넥터 연동, Skills 기반 산출물 생성(문서·프레젠테이션), 작업 큐 병렬 처리를 지원한다
- **Claude in Chrome (브라우저 에이전트)**: 2025년 8월 Research Preview(Max 플랜 1,000명), 12월 전체 유료 플랜 확대. Chrome 사이드 패널에서 자연어로 브라우저 작업을 지시하면, 버튼 클릭·폼 작성·이메일 관리·웹 탐색을 자율 수행한다. Prompt injection 공격 성공률을 23.6%에서 11.2%로 저감하는 안전장치를 적용
- **Styles (스타일)**: 응답의 포맷·톤·길이·속도를 맞춤 설정하는 개인화 기능. 간결(Concise), 설명적(Explanatory), 형식적(Formal) 등 프리셋 스타일 간 전환이 가능하며, 프로필 설정과 독립적으로 동작

## 아키텍처

### 모델 라인업
| 모델 | API 가격 (입력/출력, /MTok) | 특징 | 용도 |
|------|---------------------------|------|------|
| Opus 4.6 | $5 / $25 | 최신 플래그십, 에이전트 팀 지원 | 복잡한 아키텍처 결정, 대규모 코드베이스 분석, 에이전트 팀 |
| Opus 4.5 | $5 / $25 | 고추론, SWE-bench 80.9% | 엔터프라이즈 리서치, 고급 코딩, 에이전트 체인 |
| Sonnet 5 (Fennec) | $3 / $15 | SWE-bench 82.1%, 1M 컨텍스트, Antigravity TPU 최적화 | 에이전틱 자율 코딩, 대규모 프로젝트 |
| Sonnet 4.5 | $3 / $15 | 균형형, Extended Thinking 토글 | 구조화 분석, 코딩, 장시간 대화 |
| Haiku 4.5 | $1 / $5 | 초저지연, 저비용 | 일상 채팅, 문서 요약, 분류 태스크 |

### 에이전트 아키텍처
- **Constitutional AI (CAI)**: Anthropic의 핵심 안전성 프레임워크. 인간 피드백(RLHF)과 헌법적 원칙 기반 자기감독(RLAIF)을 결합하여 모델의 안전성을 보장
- **Extended Thinking Pipeline**: 사용자 입력 → 내부 추론 블록 생성(숨김) → 추론 요약 표시 → 최종 응답 출력의 단계적 파이프라인. 복잡한 태스크에서 Chain-of-Thought 품질을 극대화
- **Agentic Loop (Claude Code/Cowork)**: 목표 설정 → 계획 수립 → 도구 호출(파일 I/O, 터미널, 브라우저, MCP) → 결과 검증 → 반복 실행의 자율적 에이전트 루프. Human-in-the-Loop 승인 포인트를 내장

### MCP (Model Context Protocol)
- Anthropic이 2024년 11월 오픈소스로 공개한 AI-도구 연결 표준 프로토콜
- **3가지 핵심 프리미티브**: Tools(도구 호출), Resources(데이터 소스 접근), Prompts(템플릿 프롬프트)
- 2025년 3월 OpenAI 채택, 4월 Google DeepMind 지원 확인으로 사실상 업계 표준화
- 2025년 11월 주요 스펙 업데이트: 비동기 연산, 무상태성, 서버 아이덴티티, 커뮤니티 레지스트리
- 2025년 12월 Linux Foundation 산하 Agentic AI Foundation(AAIF)에 기증하여 거버넌스 중립화
- Claude Code에서 MCP 서버를 통해 수백 개의 외부 도구·데이터베이스·API에 연결 가능

### 플랫폼 통합
- **Google Workspace**: Gmail, Google Docs 등과의 네이티브 연동 (Pro 플랜 이상)
- **GitHub**: Claude Code를 통한 Git 워크플로우 통합 (커밋, PR, 코드 리뷰)
- **MCP 에코시스템**: Figma, Slack, 데이터베이스, 커스텀 API 등 서드파티 도구 확장

## UI/UX 분석

### 메인 인터페이스 구성
- **Chat + Artifacts 이중 패널**: 좌측 대화형 채팅 영역 + 우측 Artifacts 패널에서 코드·문서·시각화·인터랙티브 앱을 실시간 렌더링. Artifacts는 독립적으로 편집·복사·공유 가능
- **사이드바 내비게이션**: 대화 히스토리, Projects, Starred 대화 등을 계층적으로 구성. 검색 및 필터링 지원
- **모델 선택기**: 대화 시작 시 또는 진행 중 모델 전환 가능 (Haiku/Sonnet/Opus). 사용량 상황에 따라 자동 안내

### 대화형 UI 패턴
- **Extended Thinking 시각화**: 사고 모드 활성 시 접이식(collapsible) 블록으로 추론 과정 요약을 표시. 사용자가 펼쳐서 단계별 사고 흐름을 확인 가능
- **멀티턴 대화**: 이전 대화 맥락을 유지하며 후속 질문 제안 표시
- **인라인 코드 실행**: Artifacts 패널 내에서 코드 실행 결과를 실시간 렌더링 (HTML/CSS/JS, React, Mermaid 등)
- **출처 인용**: 웹 검색 결과 활용 시 인라인 출처 표기

### 에이전트 UI 패턴
- **Claude Code (터미널)**: CLI 인터페이스에서 작업 계획 표시 → 단계별 실행 → 결과 요약. 파일 변경 시 diff 표시, 위험 작업 시 사용자 승인 요청
- **Claude Cowork (데스크톱)**: 에이전트가 계획을 세우고 단계적으로 수행하면서 진행 상황을 공유하는 패턴. 작업 완료 시까지 계속 실행하는 흐름을 지향. VM 샌드박스 내 파일 시스템 접근
- **Claude in Chrome**: 사이드 패널에서 작업 진행 상황을 실시간 표시. 민감한 작업(결제, 로그인 등) 시 pause & ask 패턴으로 사용자 확인 요청

### 개인화 및 컨텍스트 관리
- **Styles**: 응답 스타일(간결/설명적/형식적)을 프리셋으로 전환하거나 커스텀 정의
- **Projects**: 프로젝트별 200K 토큰 상시 컨텍스트 + 커스텀 지시
- **Memory**: 대화 간 사용자 선호·배경 정보를 기억하여 개인화된 응답 제공

## 경쟁 포지셔닝

### 강점
- **코딩 벤치마크 최상위**: SWE-bench Verified에서 Opus 4.5(80.9%), Sonnet 5(82.1%)로 업계 최고 수준. 실제 소프트웨어 엔지니어링 태스크에서 검증된 성능
- **MCP 생태계 주도권**: Anthropic이 창안한 MCP가 업계 표준으로 자리잡으면서, 도구 연결 생태계의 중심에 위치. OpenAI, Google 모두 MCP를 채택
- **안전성 리더십**: Constitutional AI 기반의 체계적 안전성 프레임워크. Prompt injection 방어, 유해 콘텐츠 거부 등에서 업계 최고 수준의 안전장치 보유
- **에이전트 풀스택**: Claude Code(개발자) → Claude Cowork(비개발자) → Claude in Chrome(브라우저)으로 사용자 세그먼트별 에이전트 제품 라인업을 완성
- **글쓰기 품질**: 자연스럽고 뉘앙스 있는 텍스트 생성에서 경쟁사 대비 높은 평가. 문학적 글쓰기, 기술 문서 등에서 선호도 높음

### 약점
- **멀티모달 제한**: 이미지 입력은 지원하나, 이미지·비디오·오디오 네이티브 생성에서 Google Gemini 대비 약세. TTS, 음성 모드는 후발 주자
- **컨텍스트 윈도우**: Sonnet 5의 1M 토큰 제외 시 기본 200K 토큰으로, Gemini(1M 토큰) 대비 제한적
- **에코시스템 규모**: Google Workspace, Microsoft 365 같은 대규모 자사 서비스 생태계가 없어 통합 깊이에서 한계
- **무료 티어 제한**: 5시간 세션 기반 사용량 제한으로, ChatGPT 무료 티어 대비 제약이 큼

### 주요 경쟁사 비교
| 항목 | Claude | ChatGPT | Google Gemini |
|------|--------|---------|---------------|
| 최대 컨텍스트 | 200K (Sonnet 5: 1M) | 128K | 1M 토큰 |
| 멀티모달 | 이미지 입력 | 이미지·오디오 입출력 | 네이티브 (영상·오디오 포함) |
| 코딩 (SWE-bench) | 82.1% (Sonnet 5) | 80.0% (GPT-5.2) | 76.8% |
| 가격 (중간 티어) | Pro $20/월 | Plus $20/월 | AI Pro $19.99/월 |
| 최상위 플랜 | Max $200/월 | Pro $200/월 | AI Ultra ~$250/월 |
| 브라우저 에이전트 | Claude in Chrome | ChatGPT Agent (구 Operator) | Project Mariner |
| 코딩 에이전트 | Claude Code | Codex | Jules |
| 데스크톱 에이전트 | Claude Cowork | - | - |
| 프로토콜 | MCP (창안·주도) | MCP (채택) | MCP + A2A + A2UI |

## 관련 리서치

- [[Claude Cowork 개요]] -- Claude Cowork의 핵심 컨셉, 주요 기능, 활용 시나리오 분석
- [[Claude Cowork UI 분석]] -- Cowork 인터페이스의 UI/UX 패턴 상세 분석
- [[Claude Cowork 플랜 아키텍처]] -- Cowork 아키텍처 및 기술 스택 분석
- [[Claude Cowork 데모 시나리오]] -- 실제 사용 시나리오 및 데모 케이스
- [[AI 에이전트 서비스 서베이 (2025-2026)]] -- Claude Cowork 포함 주요 에이전트 서비스 크로스 비교
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 UI/UX 비교 테이블에서 Claude 관련 분석 참조

## 참고 자료

- [Claude 공식 사이트](https://claude.ai)
- [Claude API 개발자 문서](https://platform.claude.com/docs)
- [Claude Code 문서](https://code.claude.com/docs)
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)
- [Anthropic Blog: Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [Anthropic Blog: Claude SWE-Bench Performance](https://www.anthropic.com/research/swe-bench-sonnet)
- [Anthropic Blog: Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome)
- [Anthropic Blog: Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)
- [Claude Pricing](https://claude.com/pricing)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Anthropic Blog: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
