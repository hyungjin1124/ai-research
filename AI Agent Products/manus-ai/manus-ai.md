---
type: product-profile
product_id: manus-ai
product_name: Manus AI
vendor: Manus
category: B2C
tags:
  - AI-Agent
  - B2C
  - Agent-Builder
url: https://manus.im
launched: 2025-03
last_updated: 2026-02-09
status: in-progress
related:
  - "[[Manus AI UX 분석]]"
  - "[[Manus AI 실습 데모]]"
  - "[[AI 에이전트 서비스 서베이 (2025-2026)]]"
---

# Manus AI

## 개요

Manus(구 Monica.im / Butterfly Effect AI)가 개발한 범용 자율 AI 에이전트 플랫폼. 2025년 3월 출시 이후 기존 대화형 AI의 패러다임을 "Chat-to-Artifact"에서 "Chat-to-Execution"으로 전환한 혁신적 제품으로 주목받았다. 사용자가 목표를 제시하면 에이전트가 자율적으로 계획 수립 → 웹 탐색 → 코드 실행 → 파일 생성까지 엔드투엔드 워크플로우를 수행하며, 클라우드 샌드박스 가상 환경에서 최대 14일까지 작업을 지속할 수 있다. 출시 8개월 만에 연간 매출 런레이트 $1억을 돌파하였고, 2025년 12월 Meta가 약 $20억에 인수하여 Meta의 에이전트 전략 핵심 자산으로 편입되었다. Two-Pane UI와 Glass Box 투명성 패턴은 AI 에이전트 인터페이스의 새로운 표준으로 평가받고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Manus (2025-12 Meta 인수) |
| 출시일 | 2025-03-06 |
| 가격 | Standard $20/월 (4,000 크레딧) / Customizable $40/월 (8,000) / Extended $200/월 (40,000) |
| 플랫폼 | Web, 모바일 브라우저 |
| 공식 사이트 | https://manus.im |

## 핵심 기능

- **자율 태스크 실행 (Autonomous Task Execution)**: 사용자가 자연어로 목표를 제시하면, 에이전트가 스스로 계획을 수립하고 단계별로 실행하여 최종 산출물을 전달한다. 시장 조사, 데이터 분석, 코딩, 콘텐츠 제작 등 다양한 복잡 워크플로우를 사용자 개입 없이 처리. 명확한 태스크 정의가 효율성을 높이며, 불필요한 반복과 크레딧 소모를 줄인다
- **클라우드 샌드박스 가상 환경**: 모든 에이전트 작업이 격리된 클라우드 가상 환경에서 실행된다. 브라우저 자동화, 파일 시스템 조작, Python/Shell 스크립트 실행이 안전한 샌드박스 내에서 이루어지며, 작업을 최대 14일까지 비동기로 지속할 수 있어 장기 프로젝트에 적합. 사용자가 이탈해도 작업이 계속 진행되는 "시키고 잊기(Fire and Forget)" 패턴을 지원
- **실시간 브라우저 미러링 (Glass Box)**: "Manus's Computer"라는 우측 패널에서 에이전트의 브라우저 활동, 코드 실행, 파일 변경을 실시간으로 관찰할 수 있다. 경쟁사의 "작업 중..." 로딩 스피너와 달리, 에이전트가 실제로 무엇을 클릭하고 타이핑하는지 투명하게 공개하여 대기 불안(Waiting Anxiety)을 해소하고 신뢰도를 향상시킨다
- **멀티 에이전트 오케스트레이션**: 중앙의 Planner Agent가 사용자의 복잡한 프롬프트를 수십 개의 서브태스크로 분해하고, 각 서브태스크를 전문화된 에이전트(브라우저, 코드 실행, 파일 생성 등)에 분배하여 병렬 처리한다. 전통적 LLM의 단일 토큰 예측 방식과 차별화된 에이전트 오케스트레이션 구조
- **Code-First 검증**: Python/Shell 스크립트 실행 과정을 사용자에게 직접 노출하여 에이전트가 수행한 작업의 검증 가능성(Verifiability)을 제공한다. 개발자가 에이전트의 코드를 디버깅하거나 학습할 수 있으며, 비개발자도 에이전트의 작업 과정을 코드 수준에서 추적 가능
- **산출물(Artifact) 생성**: 리서치 보고서, 데이터 분석 결과, 웹 애플리케이션, 발표 자료, 스프레드시트 등 실체적 파일 형태의 산출물을 생성한다. Manus의 Artifact는 워크플로우 실행 결과의 "원자적 증거(Atomic Evidence)"로서, 에이전트가 실제로 무엇을 수행했는지를 증명하는 역할을 한다
- **Self-Correction Loop**: 에이전트가 작업 중 오류를 만나면 자동으로 수정을 시도하는 자기교정 루프를 내장한다. 오류 발생 → 원인 분석 → 대안 시도 → 재실행의 사이클이 시각적으로 표시되어, 에이전트의 문제 해결 과정을 투명하게 관찰 가능
- **최대 20개 동시 태스크**: 모든 플랜에서 최대 20개의 태스크를 동시에 실행할 수 있어, 여러 리서치나 분석 작업을 병렬로 처리 가능

## 아키텍처

### 에이전트 아키텍처
- **Planner Agent (중앙 오케스트레이터)**: 사용자 입력을 분석하여 실행 계획을 수립하고, 서브태스크를 전문 에이전트에 분배하는 핵심 컴포넌트. 전체 워크플로우의 진행 상황을 추적하고, 의존성을 관리하며, 필요 시 계획을 동적으로 조정
- **Browser Agent**: 웹 페이지 탐색, 폼 작성, 데이터 스크래핑, 스크린샷 캡처 등 브라우저 기반 작업을 수행하는 전문 에이전트
- **Code Execution Agent**: Python, Shell 스크립트를 샌드박스 내에서 실행하여 데이터 처리, 분석, 파일 변환 등을 수행
- **File Generation Agent**: 보고서, 스프레드시트, 프레젠테이션, 웹 앱 등 최종 산출물을 생성

### 실행 환경
- **클라우드 샌드박스**: 각 태스크가 격리된 가상 환경에서 실행. 브라우저, 파일 시스템, 코드 실행 엔진을 포함하는 독립 컨테이너
- **비동기 실행**: 작업을 큐에 등록하고 백그라운드에서 실행. 사용자가 브라우저를 닫아도 작업 지속 (최대 14일)
- **상태 관리**: 각 태스크의 실행 트리(Execution Tree)를 유지하여 진행 상황, 중간 결과, 오류 이력을 추적

### 모델 기반
- Manus는 특정 단일 LLM에 의존하지 않고, 태스크 유형에 따라 여러 모델을 조합하여 사용하는 멀티모델 오케스트레이션 방식을 채택. 계획 수립에는 고추론 모델, 코드 생성에는 코딩 특화 모델, 일반 텍스트 생성에는 범용 모델을 적용

### 프로토콜/통합
- 외부 API 연동보다는 브라우저 자동화를 통한 범용 웹 접근 방식을 주로 활용. 특정 API 통합 없이도 대부분의 웹 서비스에 브라우저를 통해 접근 가능
- MCP 등 표준 프로토콜 지원에 대한 공식 발표는 제한적이나, Meta 인수 후 에코시스템 확장이 예상

## UI/UX 분석

### Two-Pane 아키텍처 (메인 인터페이스)
- **좌측: 대화 패널 (CLI 역할)**: 사용자 명령 입력, 에이전트 계획 표시, 개입 요청 수신. 전통적 채팅 인터페이스이지만, 단순 Q&A가 아닌 "업무 지시 + 진행 보고" 채널로 기능
- **우측: Manus's Computer (작업 관찰 패널)**: 에이전트의 실시간 브라우저 화면, 코드 실행 결과, 파일 시스템 변경을 직접 관찰하는 1급 시민(First-Class Citizen) 영역. 이 패널이 Manus의 가장 핵심적인 UX 차별화 요소

### Glass Box 투명성 패턴
- **실시간 브라우저 미러링**: 경쟁사(Claude, ChatGPT)의 "작업 중..." 로딩 스피너 대신, 에이전트가 실제로 웹 페이지에서 무엇을 하는지 실시간으로 표시
- **실행 트리 + 코드 노출**: 경쟁사의 "Thinking..." 텍스트 대신, 구체적인 실행 단계와 코드를 시각화하여 에이전트의 사고 과정을 투명하게 공개
- **Self-Correction Loop 시각화**: 경쟁사의 "오류 발생" 메시지 대신, 에이전트가 오류를 감지하고 스스로 교정하는 전체 사이클을 시각적으로 표시

### 에이전트 UI 패턴
- **"보면서 개입" (Watch & Intervene)**: 사용자가 에이전트 작업을 실시간으로 관찰하다가 필요한 시점에 개입하여 방향을 수정하는 Human-in-the-Loop 패턴. 에이전트가 완전 자율 모드로 작동하되, 사용자의 개입 여지를 상시 보장
- **Fire and Forget**: 태스크를 지시하고 브라우저를 닫은 뒤, 나중에 완료된 산출물을 확인하는 비동기 워크플로우. 모바일 브라우저에서도 접근 가능하여 이동 중 결과 확인이 가능
- **태스크 큐**: 여러 태스크를 동시에 실행하고, 각 태스크의 진행 상황을 독립적으로 추적. 대시보드 형태로 전체 작업 현황을 한눈에 파악

### 산출물 경험
- **다양한 포맷**: 리서치 보고서(PDF/문서), 데이터 분석(스프레드시트), 웹 앱(배포 가능한 HTML/JS), 프레젠테이션, 코드 프로젝트 등 실체적 파일 생성
- **다운로드 및 공유**: 생성된 산출물을 직접 다운로드하거나 링크로 공유 가능
- **원자적 증거**: 각 산출물이 에이전트의 실행 과정과 연결되어, 어떤 단계에서 어떤 데이터를 기반으로 생성되었는지 추적 가능

## 경쟁 포지셔닝

### 강점
- **진정한 작업 위임**: 대화형 Q&A를 넘어 실제 업무를 엔드투엔드로 위임할 수 있는 유일한 B2C 제품. 최대 14일 비동기 실행, 20개 동시 태스크로 대규모 병렬 작업 처리 가능
- **Glass Box 투명성**: "Manus's Computer" 패널을 통한 실시간 작업 관찰은 AI 에이전트 업계에서 새로운 UX 표준을 정립. 경쟁사의 블랙박스 방식 대비 압도적인 투명성과 신뢰도
- **범용성**: 리서치, 코딩, 데이터 분석, 콘텐츠 제작, 웹 스크래핑, 파일 생성 등 광범위한 작업 유형을 단일 에이전트로 처리. API 통합 없이도 브라우저 자동화로 대부분의 웹 서비스 접근 가능
- **Meta 인수 시너지**: $20억 Meta 인수로 자원·인프라·사용자 베이스에서 급격한 확장이 예상. Meta의 AI 에이전트 전략(Llama 모델, Meta AI 등)과 통합 시 시너지 효과가 클 것으로 전망
- **폭발적 성장**: 출시 8개월 만에 연간 매출 런레이트 $1억 돌파, $500M 밸류에이션에서 $2B 인수까지 급성장

### 약점
- **크레딧 비용 불투명성**: 크레딧 기반 과금 체계에서 태스크별 크레딧 소모량을 사전에 예측하기 어려움. 사용자가 비용을 통제하기 힘들며, 미사용 월간 크레딧은 소멸
- **신뢰성 한계**: 복잡한 워크플로우에서 에이전트의 실패율이 존재하며, Self-Correction Loop로도 해결되지 않는 경우 크레딧만 소모되는 리스크
- **엔터프라이즈 미성숙**: 거버넌스, SSO, 감사 로그, 팀 관리 등 엔터프라이즈 기능이 부족. Meta 인수 후 개선이 예상되나 현재 시점에서는 개인·소규모 팀 대상
- **자체 LLM 부재**: 특정 자사 모델이 아닌 멀티모델 오케스트레이션 방식으로, 모델 성능 발전에 대한 직접적 통제력이 제한적. Meta 인수 후 Llama 모델 통합이 예상
- **Meta 인수 후 불확실성**: 일부 기존 사용자가 Meta 인수에 반감을 표시. 중국 창업팀 출신에 대한 프라이버시 우려, Meta 정책 하에서의 제품 방향성 변화 불확실성

### 주요 경쟁사 비교
| 항목 | Manus AI | Claude | ChatGPT |
|------|----------|--------|---------|
| 제품 유형 | 자율 에이전트 (작업 위임) | 대화형 AI + 에이전트 도구 | 대화형 AI + 에이전트 모드 |
| 실행 환경 | 클라우드 샌드박스 VM | 로컬(Code/Cowork) + Chrome | 브라우저(Agent) + 클라우드(Codex) |
| 최대 작업 시간 | 14일 비동기 | 세션 기반 | 7시간+(Codex) |
| 동시 태스크 | 20개 | 1개 (Code/Cowork) | 1개 (Agent) / 다수(Codex) |
| 투명성 | Glass Box (실시간 미러링) | Thinking 블록 + CLI 로그 | Thinking 블록 |
| 가격 (중간 티어) | $40/월 (8,000 크레딧) | Pro $20/월 | Plus $20/월 |
| 과금 방식 | 크레딧 (태스크별 소모) | 구독 (사용량 한도) | 구독 (메시지 한도) |
| 에코시스템 | 브라우저 자동화 중심 | MCP 기반 도구 연결 | GPT Actions + Function Calling |
| 소유사 | Meta (2025-12 인수) | Anthropic | OpenAI |

## 관련 리서치

- [[Manus AI UX 분석]] -- Manus의 Two-Pane 아키텍처, Glass Box 투명성, 경쟁사 비교 상세 분석
- [[Manus AI 실습 데모]] -- 실제 사용 시나리오 및 데모 케이스
- [[AI 에이전트 서비스 서베이 (2025-2026)]] -- Manus 포함 주요 에이전트 서비스 크로스 비교

## 참고 자료

- [Manus AI 공식 사이트](https://manus.im)
- [Manus AI 가격 정책](https://manus.im/pricing)
- [Manus AI 문서](https://manus.im/docs/introduction/plans)
- [Manus Blog: Manus Joins Meta for Next Era of Innovation](https://manus.im/blog/manus-joins-meta-for-next-era-of-innovation)
- [Manus Blog: Introducing Manus 1.6 Max](https://manus.im/blog/manus-max-release)
- [TechCrunch: Meta just bought Manus](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)
- [CNBC: Meta acquires intelligent agent firm Manus](https://www.cnbc.com/2025/12/30/meta-acquires-singapore-ai-agent-firm-manus-china-butterfly-effect-monicai.html)
- [Manus AI: An Analytical Guide to the Autonomous AI Agent 2025](https://www.baytechconsulting.com/blog/manus-ai-an-analytical-guide-to-the-autonomous-ai-agent-2025)
- [UX Collective: Cursor, vibe coding, and Manus: the UX revolution that AI needs](https://uxdesign.cc/cursor-vibe-coding-and-manus-the-ux-revolution-that-ai-needs-3d3a0f8ccdfa)
- [Emerge Haus: The New Dominant UI Design for AI Agents](https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents)
- [Cybernews: Manus AI Review 2026](https://cybernews.com/ai-tools/manus-ai-review/)
