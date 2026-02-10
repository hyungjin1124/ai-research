---
type: product-profile
product_id: servicenow-now-assist
product_name: ServiceNow Now Assist
vendor: ServiceNow
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
url: https://www.servicenow.com/products/now-assist.html
launched: 2023-09
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# ServiceNow Now Assist

## 개요

ServiceNow가 개발한 엔터프라이즈 생성형 AI 플랫폼. Now Platform 위에 구축되어 ITSM, CSM, HRSD, Creator 등 전 워크플로우 모듈에 GenAI 역량을 네이티브로 임베딩한다. 개별 AI 기능 단위인 "Skills"와, 이를 조합하여 엔드투엔드 업무를 자율 수행하는 "AI Agents", 그리고 여러 에이전트의 협업을 관리하는 "AI Agent Orchestrator"로 구성된 3계층 아키텍처가 핵심이다. 2023년 9월 Washington DC 릴리스에서 첫 출시된 이후, 2025년 3월 AI Agent Orchestrator와 AI Agent Studio를 공개하며 Agentic AI 전략을 본격화했다. 엔터프라이즈 워크플로우 자동화 시장에서 Salesforce Agentforce, SAP Joule와 직접 경쟁하며, ITSM 도메인에서는 압도적 시장 점유율을 보유하고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | ServiceNow |
| 출시일 | 2023-09 (Washington DC), 2025-03 (Agent Orchestrator) |
| 가격 | Pro Plus / Enterprise Plus 시트 기반 애드온 + Assist 토큰 소비 모델 (AI Starter Pack: 25 ITSM Pro 시트, 150K Assists 포함) |
| 플랫폼 | Web (Now Platform), Mobile (Now Mobile), Virtual Agent (채팅/음성), Microsoft Teams, Slack |
| 공식 사이트 | https://www.servicenow.com/products/now-assist.html |

## 핵심 기능

- **Now Assist Skills**: Now Assist의 핵심 단위. 각 Skill은 특정 GenAI 작업(티켓 요약, 해결 노트 초안, 지식 문서 생성, 코드 스니펫 생성 등)을 수행하도록 패키징되어, 관리자가 LLM을 직접 학습시키지 않고도 활성화·구성·거버넌스를 수행할 수 있다. Xanadu 릴리스부터 Now Assist Skill Kit(NASK)을 통해 커스텀 Skill 개발도 가능
- **AI Agents**: 다수의 Skill을 조합하여 단순~복잡한 워크플로우를 엔드투엔드로 자율 수행하는 지능형 유닛. 인시던트 자동 분류 -> 관련 지식 문서 검색 -> 해결책 제안 -> 사용자 확인 -> 해결 완료까지의 전체 흐름을 자동화
- **AI Agent Orchestrator**: 여러 AI Agent 팀의 협업을 조율하는 중앙 컨트롤 타워. 태스크 시퀀싱, Assist 토큰 예산 관리, 역할 기반 접근 제어, 감사 로깅, 서비스 윈도우 정책을 실시간으로 적용. 에이전트가 수행하는 모든 단계를 정책 대비 실시간 평가
- **Now Assist Panel**: 인간 에이전트와 AI 에이전트 사이의 인터페이스 역할. AI Search를 통해 Agentic Workflow와 AI Agent를 동적으로 발견하여 사용자에게 제시. ITSM, CSM, HRSD 등 모든 모듈에 임베딩
- **AI Agent Studio**: 자연어 인터페이스로 전문 AI 에이전트를 빌드·커스터마이즈하는 개발 도구. 가드레일 설정, 태스크 자동화 정의, 테스트·배포까지 로코드 환경에서 수행
- **Virtual Agent + AI Voice Agents**: 사전 구축된 대화 템플릿(ITSM, HR, CSM용)을 기반으로 텍스트 및 음성 채널에서 자연어 대화를 수행. 2025년부터 AI Voice Agents가 추가되어 음성 기반 자율 서비스 제공
- **Dynamic Translation & Genius Results**: 다국어 실시간 번역으로 글로벌 서비스 제공. Genius Results는 여러 지식 문서를 합성하여 단일 카드로 최적 답변을 생성

## 아키텍처

### 3계층 AI 아키텍처
| 계층 | 구성 요소 | 역할 |
|------|-----------|------|
| Skills | Now Assist Skills, NASK 커스텀 Skills | 개별 GenAI 태스크 수행 (요약, 분류, 생성 등) |
| Agents | AI Agents (ITSM/CSM/HRSD/Creator) | 복수 Skill 조합, 엔드투엔드 워크플로우 자율 실행 |
| Orchestrator | AI Agent Orchestrator | 멀티 에이전트 팀 협업 조율, 거버넌스, 정책 적용 |

### LLM 지원
- 기본 LLM: ServiceNow 자체 도메인 특화 모델
- 외부 LLM 연동: Gemini, Azure OpenAI, Claude 등 (Yokohama Patch 6+ 기준, 2025년 7월)
- Generic LLM Connector: 서드파티 LLM 서비스 범용 연결
- Watsonx LLM Connector: IBM Watsonx 전용 연결

### 에이전트 라이프사이클
1. **빌드**: AI Agent Studio에서 자연어 기반 에이전트 정의 및 가드레일 설정
2. **테스트**: Testing Center에서 시나리오 기반 검증
3. **배포**: Now Assist Panel을 통해 대상 모듈에 활성화
4. **모니터링**: Orchestrator 대시보드에서 실시간 성능·정책 준수 추적
5. **최적화**: 사용량 집계 및 Assist 토큰 소비 분석 기반 튜닝

### 도메인별 통합
- **ITSM**: 인시던트 자동 분류, 변경 관리, 문제 분석, SLA 추적
- **CSM**: 고객 케이스 요약, 멀티채널 대응 자동화, 해결 노트 생성
- **HRSD**: 온보딩 가이드, 직원 문의 자동 응답, 복리후생 안내
- **Creator**: 코드 생성, Flow Designer 자동화, 앱 개발 지원
- **ITOM**: 시스템 모니터링, 사전 장애 탐지, 자동 수정 권장

### 외부 시스템 연동
- Microsoft 365 Copilot 양방향 통합 (예정)
- SharePoint, Teams, Slack 네이티브 커넥터
- REST API 기반 서드파티 시스템 연결
- ServiceNow Store를 통한 앱·플러그인 배포

## UI·UX 분석

### 메인 인터페이스 구성
- **Now Assist Panel (Embedded Sidecar)**: 기존 Now Platform 워크스페이스 우측에 임베딩되는 사이드 패널. 사용자가 업무 컨텍스트를 유지하면서 AI와 상호작용. 레코드(인시던트, 케이스, HR 요청) 화면에서 직접 접근 가능
- **MyNow (개인화 포탈)**: 사용자별 역할·권한에 맞춘 개인화된 AI 서비스 허브. 자주 사용하는 Skill과 에이전트를 즐겨찾기로 구성
- **Admin Console (중앙 관리)**: Skills/Plugins 활성화, LLM 연결 관리, 사용량 모니터링, Dynamic Translation 설정 등 관리자 전용 대시보드

### 대화형 UI 패턴
- **LLM 기반 의도 인식**: 사용자 자연어 입력에서 의도(Intent)를 LLM으로 분석하여 적절한 Skill/Agent로 라우팅
- **멀티턴 컨텍스트 유지**: 대화 이력을 기반으로 문맥을 유지하며 복잡한 요청을 단계적으로 처리
- **Carousel 형식 결과**: 복수의 지식 문서, 해결책, 관련 인시던트를 카드 캐러셀로 시각 제시
- **Slash Commands**: `/now-assist` 등 명령어 기반 빠른 Skill 호출 패턴

### Human-in-the-Loop 패턴
- **Chat Summarization 전환**: 라이브 채팅에서 AI 에이전트 전환 시 대화 내용을 자동 요약하여 인간 에이전트에게 전달
- **Resolution Notes Review**: AI가 생성한 해결 노트를 인간 에이전트가 검토·수정 후 확정
- **Knowledge Article Approval**: AI가 초안한 지식 문서를 관리자가 승인하는 워크플로우
- **Proactive Triggers/Notifications**: AI가 이상 징후를 탐지하면 인간 에이전트에게 사전 알림 발송

### 데이터 시각화
- **Genius Result Card**: 복수 지식 문서의 핵심 내용을 합성하여 단일 결과 카드로 표시. 출처 문서 링크 포함
- **Theme Builder Branding**: 서비스 포탈의 브랜딩·테마를 커스터마이즈하여 기업 아이덴티티에 맞춤
- **Multiple Assistant Profiles**: 도메인별(IT, HR, CS) 서로 다른 어시스턴트 프로필을 구성하여 사용자 혼란 최소화

## 경쟁 포지셔닝

### 강점
- **ITSM 도메인 독보적 시장 지배력**: Gartner Magic Quadrant ITSM 부문 리더 10년 연속. Now Platform 기반의 깊은 워크플로우 통합으로, AI가 단순 챗봇이 아닌 실제 업무 프로세스를 자동화
- **3계층 Agentic AI 아키텍처**: Skills -> Agents -> Orchestrator의 체계적 구조로, 단순 기능부터 복잡한 크로스 도메인 자동화까지 확장 가능
- **엔터프라이즈 거버넌스**: Assist 토큰 예산 관리, 역할 기반 접근 제어, 감사 로깅 등 대기업이 요구하는 거버넌스 기능이 Orchestrator에 내장
- **크로스 도메인 통합**: 단일 플랫폼에서 IT, HR, CS, 보안, 운영 등 모든 엔터프라이즈 워크플로우를 AI로 연결. 사일로 해소에 강점
- **Virtual Agent 성숙도**: 텍스트·음성 채널을 아우르는 Virtual Agent 인프라가 이미 성숙하여, GenAI 기능 추가가 자연스러움

### 약점
- **가격 장벽**: Pro Plus/Enterprise Plus 애드온 + Assist 토큰 소비 모델이 중소기업에게 부담. 공개 가격표 없이 커스텀 견적 필요
- **LLM 유연성 제한**: 외부 LLM 지원이 2025년 중반부터 확대되었으나, Salesforce(자체 Einstein LLM + 다중 LLM)나 SAP Joule(다중 파운데이션 모델) 대비 선택지가 제한적이었음
- **MCP/A2A 프로토콜 미지원**: Workday(MCP+A2A), Salesforce(MuleSoft API)와 달리 개방형 에이전트 간 통신 프로토콜 채택이 아직 공식화되지 않음
- **Generative UI 부재**: Google Gemini의 Dynamic View나 SAP Joule의 Rich UI Elements 대비, 응답 포맷이 텍스트·카드 중심으로 제한적

### 주요 경쟁사 비교
| 항목 | ServiceNow Now Assist | Salesforce Agentforce | SAP Joule |
|------|----------------------|----------------------|-----------|
| 핵심 도메인 | ITSM, CSM, HRSD, ITOM | CRM, Sales, Service, Commerce | ERP, HCM, SCM, Procurement |
| 에이전트 아키텍처 | Skills -> Agents -> Orchestrator | Topics -> Actions -> Atlas Engine | Scenario Catalog -> Knowledge Catalog -> RAGe |
| LLM 전략 | 자체 모델 + 외부 LLM (Gemini, Azure OpenAI, Claude) | Einstein LLM + 다중 LLM Gateway | SAP 자체 + 다중 파운데이션 모델 |
| 빌더 도구 | AI Agent Studio (로코드) | Agentforce Builder (3-Panel) | Joule Studio |
| 가격 모델 | 시트 기반 + Assist 토큰 소비 | 대화당 $2 (Agentforce) | SAP 라이선스 번들 포함 |
| HITL 패턴 | Chat Summarization 전환, Resolution Notes Review | Omni Supervisor 실시간 모니터링 | SuccessFactors Goals 승인, Ariba 검토 |
| 음성 에이전트 | AI Voice Agents (2025) | 음성 미지원 | 음성 미지원 |
| 프로토콜 | REST API, 전용 커넥터 | MuleSoft API | Microsoft 365 Copilot 양방향 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 UI/UX 비교 테이블에서 ServiceNow Now Assist 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] -- 엔터프라이즈 AI 에이전트 벤치마크 대상 목록

## 참고 자료

- [ServiceNow Now Assist 공식 사이트](https://www.servicenow.com/platform/now-assist.html)
- [ServiceNow AI Agents 공식 페이지](https://www.servicenow.com/products/ai-agents.html)
- [ServiceNow Newsroom: AI Agent Orchestrator 발표 (2025-01)](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-announces-new-agentic-AI-innovations-to-autonomously-solve-the-most-complex-enterprise-challenges-01-29-2025-traffic/default.aspx)
- [ServiceNow Newsroom: Microsoft 통합 발표 (2025)](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-Advances-Enterprise-AI-through-Seamless-Integrations-with-Microsoft-Enabling-Collaboration-Orchestration-and-Governance/default.aspx)
- [Now Assist Skill Kit (NASK) FAQ](https://www.servicenow.com/community/now-assist-articles/now-assist-skill-kit-nask-faq/ta-p/3007953)
- [AI Voice Agents 발표](https://www.servicenow.com/community/now-assist-articles/ai-voice-agents-are-here-autonomous-service-that-delights/ta-p/3448126)
- [Knowledge 2025: Now Assist Panel 실습 가이드](https://servicenow-events-or-lab-guidebo.gitbook.io/knowledge-2025/ccl2500-k25/exercise-7-invoke-from-now-assist-panel-15-min)
- [ServiceNow ITSM Pricing](https://www.servicenow.com/products/itsm/pricing.html)
- [ServiceNow Pricing 2026 가이드 (Desk365)](https://www.desk365.io/blog/servicenow-pricing/)
- [Now Assist 2025 개요 (eesel.ai)](https://www.eesel.ai/blog/what-is-now-assist-in-service-now)
