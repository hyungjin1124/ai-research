---
type: product-profile
product_id: workday-assistant
product_name: Workday Assistant
vendor: Workday
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
  - MCP-Support
url: https://www.workday.com/en-us/artificial-intelligence.html
launched: 2024-01
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Workday Assistant

## 개요

Workday가 개발한 HR·Finance 특화 엔터프라이즈 AI 에이전트 플랫폼. Workday Illuminate 브랜드 하에 AI 에이전트를 제공하며, 업계 최초로 AI 에이전트를 인간 직원과 동일한 방식으로 관리하는 Agent System of Record(ASOR) 개념을 도입했다. ASOR를 통해 AI 에이전트의 채용(등록), 온보딩(권한 설정), 역할 배정, 데이터 접근 범위 정의, 성과 추적을 단일 레지스트리에서 수행한다. 2025년 6월에는 MCP(Model Context Protocol)와 A2A(Agent-to-Agent Protocol)를 지원하는 Agent Gateway를 발표하여, Workday 내외부 AI 에이전트의 상호운용성을 확보했다. 2025년 9월 Sana Labs를 11억 달러에 인수하여 AI 검색·학습·에이전트 역량을 강화했으며, Workday Rising 2025에서 Workday Build 플랫폼과 Flowise Agent Builder를 공개하며 개발자 생태계를 본격 확장하고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Workday |
| 출시일 | 2024-01 (Illuminate), 2025-02 (ASOR), 2025-06 (Agent Gateway) |
| 가격 | Flex Credits 기반 소비 모델 (구체적 단가 비공개, 커스텀 견적) |
| 플랫폼 | Web (Workday), Mobile (Workday App), Slack 연동, Microsoft Copilot 통합 |
| 공식 사이트 | https://www.workday.com/en-us/artificial-intelligence.html |

## 핵심 기능

- **Agent System of Record (ASOR)**: AI 에이전트를 디지털 직원으로 관리하는 중앙 레지스트리. Agent Registry 대시보드에서 모든 에이전트의 목록, 설명, 접근 권한 보안 그룹, 국가별 가용성, 활성/비활성 상태를 통합 관리. 에이전트의 역할(Role), 데이터 접근 범위(Data Access), 실행 가능한 액션(Actions)을 명시적으로 정의
- **Illuminate Agents**: Workday Marketplace에서 제공되는 사전 구축된 AI 에이전트 라인업. HR 영역에서는 Business Process Copilot Agent, Employee Sentiment Agent, Job Architecture Agent, Performance Agent, Recruiting Agent, Talent Mobility Agent를, Finance 영역에서는 Financial Close Agent, Cost and Profitability Agent, Financial Audit Agent, Financial Test Agent, Payroll Agent를 제공
- **Agent Gateway (MCP/A2A)**: MCP와 A2A 프로토콜을 기반으로 Workday 내부 에이전트와 외부 파트너 에이전트를 원활하게 연결하는 게이트웨이. Workday Agent Partner Network 소속 50개 이상 파트너(Accenture, Adobe, AWS, Deloitte, Glean, Google Cloud, IBM, Microsoft, PwC 등)의 에이전트를 ASOR에 등록하고 통합 관리 가능
- **Workday Build + Flowise Agent Builder**: 개발자가 커스텀 AI 에이전트 및 앱을 구축하는 플랫폼. Developer Copilot, Agent Gateway API, Data Cloud 접근을 통합 제공. Flowise 기반 비주얼 에이전트 빌더로 로코드/노코드 에이전트 개발 지원
- **Sana Labs 통합**: 2025년 11월 인수 완료. Sana의 AI 기반 검색, 에이전트, 학습 관리 플랫폼을 Workday 데이터·컨텍스트와 결합하여 지식 관리 및 직원 학습 경험을 혁신. Workday를 "업무의 프런트 도어(Front Door for Work)"로 포지셔닝
- **Unified Experience**: 단일 뷰에서 HR, Finance, 운영 전반의 AI 에이전트 결과를 통합 표시. 복잡한 비즈니스 프로세스를 자연어 대화로 안내하고 크로스 앱 정보를 실시간으로 집계

## 아키텍처

### ASOR 중심 에이전트 관리 모델
| 구성 요소 | 역할 |
|-----------|------|
| Agent Registry | 모든 AI 에이전트의 메타데이터(역할, 권한, 상태, 성과) 중앙 저장소 |
| Agent Gateway | MCP/A2A 프로토콜 기반 에이전트 간 통신 및 외부 에이전트 연결 허브 |
| Agent Partner Network | 50+ 글로벌 파트너가 개발한 에이전트를 Marketplace에 배포·관리 |
| Workday Build | 커스텀 에이전트·앱 개발 플랫폼 (Developer Copilot, Flowise Agent Builder) |

### 프로토콜 지원
- **MCP (Model Context Protocol)**: AI 에이전트에 필요한 비즈니스 데이터와 도구 접근을 표준화된 방식으로 제공. 에이전트가 Workday의 HR·Finance 데이터에 컨텍스트 기반으로 접근 가능
- **A2A (Agent-to-Agent Protocol)**: 에이전트 간 통신·협업 프로토콜. Workday 자체 에이전트와 파트너 에이전트가 실시간으로 정보를 교환하며 복합 태스크를 수행

### 에이전트 라이프사이클 관리
1. **등록(Hire)**: ASOR에 에이전트를 등록하고 기본 메타데이터(이름, 설명, 유형) 정의
2. **온보딩(Onboard)**: 보안 그룹 할당, 데이터 접근 범위 설정, 국가별 가용성 구성
3. **역할 배정(Assign Role)**: 수행할 비즈니스 프로세스와 액션 범위 정의
4. **운영(Operate)**: 프로덕션 환경에서 에이전트 활성화 및 태스크 수행
5. **성과 추적(Track Performance)**: 에이전트별 실행 로그, 완료율, 비용, 사용자 피드백 집계
6. **최적화/퇴직(Optimize/Retire)**: 성과 데이터 기반 튜닝 또는 비활성화

### Illuminate Agent 유형별 분류

**HR Agents**
| 에이전트 | 기능 |
|---------|------|
| Business Process Copilot | 복잡한 HR 프로세스 단계별 안내 및 자동화 |
| Employee Sentiment Agent | 직원 감정 분석 및 조직 분위기 인사이트 제공 |
| Job Architecture Agent | 직무 구조 설계·검토·최적화 지원 |
| Performance Agent | 성과 평가 프로세스 자동화 및 관리자 의사결정 지원 |
| Recruiting Agent | 채용 프로세스 자동화 (후보자 스크리닝, 일정 조율) |
| Talent Mobility Agent | 내부 인재 이동 기회 매칭 및 경력 개발 안내 |

**Finance Agents**
| 에이전트 | 기능 |
|---------|------|
| Financial Close Agent | 결산 프로세스 자동화 및 이상 항목 탐지 |
| Cost and Profitability Agent | 비용 분석 및 수익성 인사이트 제공 |
| Financial Audit Agent | 감사 준비 자동화 및 컴플라이언스 점검 |
| Financial Test Agent | 재무 데이터 무결성 테스트 자동화 |
| Payroll Agent | 급여 처리 자동화 및 오류 사전 탐지 |

### 데이터 아키텍처
- Workday Data Cloud: 전사 HR·Finance 데이터를 단일 데이터 레이어로 통합
- 크로스 앱 컨텍스트 유지: 에이전트가 여러 Workday 모듈의 데이터를 동시에 참조하여 통합 인사이트 생성
- 보안: 역할 기반 접근 제어(RBAC), 국가별 데이터 거주지(Residency) 정책 적용

## UI·UX 분석

### 메인 인터페이스 구성
- **Unified Experience (Single View)**: HR, Finance, 운영 데이터를 단일 화면에서 통합 표시. 사용자가 앱 간 전환 없이 크로스 도메인 정보에 접근
- **Workday Marketplace**: Illuminate Agent를 포함한 서드파티 앱·에이전트를 탐색·설치하는 앱 스토어 인터페이스
- **Agent Registry Dashboard**: 관리자가 모든 AI 에이전트의 상태, 권한, 성과를 한눈에 파악하는 대시보드. 에이전트를 인간 직원처럼 리스트·필터·검색 가능

### 대화형 UI 패턴
- **Natural Language HR/Finance**: HR 질의(휴가 잔여일, 급여 명세, 복리후생 옵션)와 Finance 질의(예산 현황, 비용 보고서, 결산 상태)를 자연어로 처리
- **Complex Process Guidance**: 복잡한 비즈니스 프로세스(채용 워크플로우, 보상 결정, 예산 편성)를 단계별로 안내하는 가이디드 대화
- **Copilot/Slack 스타일 접근**: Slack 연동 및 Microsoft Copilot 통합을 통해 사용자 친숙한 메시징 인터페이스에서 Workday 기능 접근

### Human-in-the-Loop 패턴
- **Manager Bonus 결정 지원**: AI가 성과 데이터 기반 보너스 권장안을 생성하면, 매니저가 검토·조정 후 확정
- **Job Architecture Agent 검토**: AI가 제안한 직무 구조 변경사항을 HR 담당자가 검토·승인
- **Task Workflow Confirmation**: AI가 자동 수행한 프로세스 결과를 사용자에게 확인 요청하는 단계별 승인 패턴

### 데이터 시각화
- **Real-time Cross-App Info**: 여러 Workday 모듈의 데이터를 실시간으로 집계하여 통합 대시보드에 표시
- **Expense/Logistics Dashboards**: 비용 현황, 예산 대비 실적, 물류 추적 등 운영 데이터를 시각적 대시보드로 제공
- **Budget Overrun Alerts**: 예산 초과 시 실시간 알림과 함께 원인 분석 시각화 제공

## 경쟁 포지셔닝

### 강점
- **ASOR: 업계 최초 에이전트 관리 패러다임**: AI 에이전트를 디지털 직원으로 관리하는 개념을 선도. 에이전트 채용-온보딩-역할배정-성과관리-퇴직의 전체 라이프사이클을 인사 관리 방식으로 표준화. 멀티벤더 에이전트(자사+파트너)를 단일 레지스트리에서 통합 관리
- **MCP + A2A 프로토콜 네이티브 지원**: 엔터프라이즈 ERP 벤더 중 가장 적극적으로 개방형 에이전트 프로토콜을 채택. 이종 시스템 에이전트 간 상호운용성에서 차별화
- **강력한 파트너 생태계**: Agent Partner Network에 50개 이상 글로벌 파트너(Accenture, AWS, Deloitte, Google Cloud, IBM, Microsoft, PwC 등) 참여. 빠르게 4배 이상 성장하며 에코시스템 확장 가속
- **HR·Finance 도메인 전문성**: 20년 이상의 HR·Finance 데이터 축적과 도메인 지식을 기반으로, 에이전트가 비즈니스 컨텍스트를 깊이 이해. 단순 챗봇이 아닌 도메인 전문가 수준의 의사결정 지원
- **Sana Labs 인수를 통한 학습·검색 역량 강화**: AI 기반 엔터프라이즈 검색과 학습 관리를 통합하여, 지식 관리까지 아우르는 풀스택 AI 경험 제공

### 약점
- **도메인 범위 제한**: HR과 Finance에 강하지만, ITSM(ServiceNow), CRM(Salesforce), SCM(SAP) 등 타 도메인에서는 존재감이 약함. 크로스 도메인 자동화에 한계
- **Agent Gateway 초기 단계**: 2025년 말 Early Adopter 공개 예정으로, 아직 대규모 프로덕션 배포 사례가 제한적. 안정성과 확장성 검증이 진행 중
- **가격 투명성 부족**: Flex Credits 모델을 도입했으나, 구체적 단가와 크레딧 소비 기준이 공개되지 않아 TCO 예측이 어려움
- **자체 LLM 전략 미비**: 자체 파운데이션 모델을 보유하지 않고 서드파티 LLM에 의존. Sana 인수를 통해 AI 역량을 내재화하고 있으나, ServiceNow(자체 모델)나 Salesforce(Einstein LLM)와 달리 모델 수준의 차별화가 부족
- **Generative UI 미비**: 응답 포맷이 텍스트·리스트 중심이며, Salesforce Agentforce의 3-Panel Builder나 Google Gemini의 Dynamic View 같은 동적 UI 생성 기능은 부재

### 주요 경쟁사 비교
| 항목       | Workday Assistant                     | ServiceNow Now Assist   | SAP Joule                  |
| -------- | ------------------------------------- | ----------------------- | -------------------------- |
| 핵심 도메인   | HR, Finance                           | ITSM, CSM, HRSD         | ERP, HCM, SCM, Procurement |
| 에이전트 관리  | ASOR (에이전트를 직원처럼 관리)                  | AI Agent Orchestrator   | SAP AI Core                |
| 프로토콜 지원  | MCP + A2A (네이티브)                      | REST API, 전용 커넥터        | Microsoft 365 Copilot 양방향  |
| 파트너 생태계  | Agent Partner Network (50+ 파트너)       | ServiceNow Store        | SAP Store                  |
| 빌더 도구    | Workday Build + Flowise Agent Builder | AI Agent Studio         | Joule Studio               |
| 가격 모델    | Flex Credits 소비                       | 시트 기반 + Assist 토큰       | SAP 라이선스 번들                |
| 에이전트 라인업 | HR 6종 + Finance 5종 (Illuminate)       | 도메인별 Skills + AI Agents | Cross-product (80% 트랜잭션)   |
| 학습/검색    | Sana Labs 통합 (AI 검색·학습)               | Knowledge Management    | SAP Knowledge Graph        |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 UI/UX 비교 테이블에서 Workday Assistant (ASOR) 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] -- 엔터프라이즈 AI 에이전트 벤치마크 대상 목록

## 참고 자료

- [Workday AI 공식 사이트](https://www.workday.com/en-us/artificial-intelligence.html)
- [Workday ASOR 공식 페이지](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html)
- [Workday Newsroom: ASOR 발표 (2025-02)](https://investor.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record)
- [Workday Newsroom: Agent Partner Network & Agent Gateway 발표 (2025-06)](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
- [Workday Newsroom: AI Developer Toolset 발표 (2025-06)](https://investor.workday.com/2025-06-03-Workday-Unveils-AI-Developer-Toolset,-Empowering-Developers-to-Customize-and-Connect-AI-Apps-and-Agents-on-the-Workday-Platform)
- [Workday Newsroom: Illuminate 확장 -- HR, Finance, Industry 에이전트 (2025-09)](https://newsroom.workday.com/2025-09-16-Workday-Illuminate-TM-Expands-with-New-AI-Agents-for-HR,-Finance,-and-Industry)
- [Workday Newsroom: Sana Labs 인수 완료 (2025-11)](https://newsroom.workday.com/2025-11-04-Workday-Completes-Acquisition-of-Sana)
- [GitHub: ASOR API 문서](https://github.com/Workday/asor)
- [Workday Blog: AI Agent Protocols 가이드](https://blog.workday.com/en-us/building-enterprise-intelligence-a-guide-to-ai-agent-protocols-for-multi-agent-systems.html)
- [Workday Blog: Agentic Wave -- 차세대 Workforce Management](https://blog.workday.com/en-us/the-agentic-wave-new-era-workforce-management.html)
- [Workday Rising 2025 리뷰 (ERP Advisors Group)](https://www.erpadvisorsgroup.com/blog/independent-review-of-workday-rising-2025-releases)
- [Workday Rising 2025: AI Agents, Data Cloud, Flex Credits (Futurum)](https://futurumgroup.com/insights/workday-rising-2025-ai-agents-data-cloud-and-flex-credits-unveiled/)
