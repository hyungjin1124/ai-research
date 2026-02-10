---
type: product-profile
product_id: microsoft-copilot
product_name: Microsoft Copilot for Dynamics 365
vendor: Microsoft
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
  - MCP-Support
  - Agent-Builder
url: https://www.microsoft.com/en-us/dynamics-365/copilot
launched: 2023-11
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Microsoft Copilot for Dynamics 365

## 개요

Microsoft가 Dynamics 365 ERP/CRM 제품군에 통합한 AI Copilot 플랫폼. Sales, Service, Finance, Supply Chain 등 비즈니스 애플리케이션 전반에 Sidecar 방식으로 내장되어, 자연어 기반의 업무 지원과 자율 에이전트 기능을 제공한다. Microsoft Graph와 Dataverse를 통한 데이터 통합, Copilot Studio를 통한 커스텀 에이전트 구축, 그리고 Model Context Protocol(MCP) 네이티브 지원이 핵심 차별점이다. 2025년 Build에서 발표된 멀티 에이전트 오케스트레이션(Multi-Agent Orchestration)은 여러 에이전트가 협업하여 복잡한 비즈니스 워크플로우를 처리할 수 있게 하며, Microsoft 365 Copilot과의 원활한 통합으로 Teams, Outlook, Word 등 일상 업무 도구에서 ERP 데이터에 직접 접근할 수 있다. $30/사용자/월 번들 가격에 Sales, Service, Finance용 Copilot이 모두 포함되어 가격 경쟁력을 갖추고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Microsoft |
| 출시일 | 2023-11 (GA), 2025-05 (멀티 에이전트 오케스트레이션), 2025-11 (Ignite 2025 업데이트) |
| 가격 | $30/사용자/월 (Microsoft 365 Copilot 번들, Sales·Service·Finance 포함) |
| 플랫폼 | Dynamics 365, Microsoft 365, Teams, Outlook, Copilot Studio, Power Platform |
| 공식 사이트 | https://www.microsoft.com/en-us/dynamics-365/copilot |

## 핵심 기능

- **Copilot in Dynamics 365 Sales**: 기회 요약, 리드 우선순위 지정, 이메일 초안 생성, 미팅 준비 브리핑 자동 생성. Opportunity Pipeline View에서 AI 기반 인사이트 제공, Timeline Highlights로 고객 인터랙션 이력 자동 요약
- **Copilot in Dynamics 365 Service**: 케이스 요약, 지식 기반 문서 자동 검색 및 응답 초안 생성, 대화 분석(Conversation Analytics), 실시간 감정 분석. 에이전트 핸드오프 시 자동 요약 전달
- **Copilot in Dynamics 365 Finance & Supply Chain**: 자연어 ERP 쿼리, 현금 흐름 예측, 인보이스 매칭 자동화, 공급망 이상 감지. Finance and Operations 앱 전반에 걸친 Copilot Sidecar 지원
- **Copilot Studio (에이전트 빌더)**: 로코드/노코드 에이전트 구축 플랫폼. Agent Builder에서 프로토타입을 빠르게 생성한 뒤 Copilot Studio로 이관하여 엔터프라이즈급 에이전트로 확장 가능. Python Code Interpreter, Computer Use 도구, 고급 NLU 커스터마이징 지원
- **멀티 에이전트 오케스트레이션**: Microsoft 365, Azure AI, Fabric에서 구축된 에이전트들이 작업을 위임하고 결과를 공유하며 협업. 각 에이전트의 실행 경로, 단계, 관련 시스템을 사용자가 추적 가능
- **10개 자율 에이전트**: Sales Qualification Agent, Supplier Communications Agent, Financial Reconciliation Agent 등 Sales, Service, Finance, Supply Chain 분야의 사전 구축된 자율 에이전트 10종 제공
- **Microsoft 365 Copilot Tuning**: 회사 고유 데이터, 워크플로우, 프로세스를 사용하여 AI 모델을 로코드로 미세 조정하는 기능. 데이터 과학자 팀 없이도 조직별 맞춤화 가능

## 아키텍처

### Copilot 오케스트레이션 계층

| 구성 요소 | 역할 |
|----------|------|
| Copilot Orchestrator | 자연어 요청의 의도 식별, 데이터 소스 검색, 액션 실행을 총괄 |
| Microsoft Graph | Microsoft 365 전반(메일, 일정, 파일, 인맥)의 데이터 접근 |
| Dataverse | Dynamics 365 비즈니스 데이터의 중앙 저장소 및 조회 계층 |
| Power Platform 커넥터 | 1,000+ 외부 시스템과의 연결 (SAP, Salesforce, ServiceNow 등) |

### MCP 통합

- **Dynamics 365 F&O MCP Server**: Finance and Operations 앱에 MCP 서버를 활성화하여 Copilot Sidecar가 MCP 도구로서 ERP 데이터에 접근. 자연어 ERP 쿼리, 에이전트 개발에 활용
- **비동기 Dual-Write 연동**: CRM과 ERP 간 데이터 동기화를 비동기로 처리하여 성능 최적화
- **MCP 네이티브 지원**: Copilot Studio에서 MCP를 통한 외부 도구 연결을 기본 지원, 플러그앤플레이 방식의 서드파티 통합

### 에이전트 아키텍처

- **Embedded Agents**: Dynamics 365, Microsoft 365 앱 내부에 직접 내장된 에이전트
- **Connected Agents**: Copilot Studio를 통해 외부 시스템과 연결된 에이전트
- **Autonomous Agents**: 장기 실행(long-running) 작업을 사용자 개입 없이 자율적으로 수행하는 에이전트. 동적 계획 수립(dynamic planning) 능력 보유

### 에코시스템 통합

- Microsoft 365 (Teams, Outlook, Word, Excel, PowerPoint) 네이티브 통합
- Azure AI Services (Azure OpenAI Service, Cognitive Services) 기반
- Power Platform (Power Automate, Power Apps, Power BI) 연동
- SharePoint 채널 배포 (GA), WhatsApp 채널 지원 (2025년 7월~)
- GitHub Copilot과의 개발자 워크플로우 연결

## UI·UX 분석

### 메인 인터페이스 구성

- **Sidecar 패턴**: 기존 Dynamics 365 애플리케이션 우측에 Copilot 사이드 패널을 배치하여 업무 흐름을 끊지 않는 컨텍스트 내 AI 지원 제공. 2025년 9월부터 전체 화면(full-screen) 뷰는 단계적 폐지(deprecated)되고 사이드 패널 중심으로 전환
- **Copilot Home**: 역할별 맞춤 대시보드로, 사용자의 직무에 따라 관련 인사이트, 추천 액션, 최근 활동 요약을 한눈에 제공
- **Embedded Copilot**: 레코드 상단에 요약/인사이트 배너를 배치하고, 사이드 패널에서 후속 질의를 처리하는 이중 구조

### 대화형 UI 패턴

- 자연어 입력 기반 인터랙션
- 실시간 스트리밍 응답으로 대기 시간 체감 최소화
- Follow-up Suggestions 자동 생성으로 대화 흐름 안내
- Timeline Highlights: 고객 인터랙션 이력에서 핵심 이벤트를 자동 추출·표시

### 에이전트 UI 패턴

- **Manager Insights Dashboard**: 관리자용 대화 분석, 에이전트 성과 지표, 사용량 추적 대시보드
- **Plugin 선택 과정 표시**: Copilot이 어떤 데이터 소스(Dataverse, 외부 커넥터)를 선택했는지 처리 과정을 투명하게 노출
- **Multi-Agent 경로 시각화**: 멀티 에이전트 오케스트레이션 시 각 에이전트의 실행 경로, 핵심 단계, 관련 시스템을 사용자에게 시각적으로 표시
- **Human-in-the-Loop**: Proposal Summary 검토/승인, Email Draft 편집 후 발송, Teams/Outlook 협업 피드백 수집 등 인간 확인이 필요한 단계에서 자동 일시 정지

### 데이터 시각화

- Opportunity Pipeline View: 영업 기회 파이프라인의 AI 기반 시각화
- Schedule Board 최적화: 서비스 일정 자동 배치 및 시각화
- Dynamic Grouping/Aggregation: 데이터를 자연어 요청에 따라 동적으로 그룹화·집계하여 표시
- Power BI 연동: 고급 분석 대시보드와 Copilot 인사이트 통합

## 경쟁 포지셔닝

### 강점

- **Microsoft 에코시스템 통합 깊이**: Teams, Outlook, Word, Excel 등 전 세계 사용자가 가장 많이 쓰는 업무 도구와 네이티브 통합. ERP 데이터를 일상 업무 도구에서 직접 활용할 수 있어 채택 장벽이 낮음
- **번들 가격 경쟁력**: $30/사용자/월에 Sales, Service, Finance용 Copilot을 모두 포함하는 번들 전략으로, 각 모듈별 과금하는 경쟁사 대비 TCO 우위
- **MCP 네이티브 지원**: Copilot Studio에서 MCP를 기본 지원하여 서드파티 AI 도구·데이터 소스와의 표준화된 연결이 용이. Dynamics 365 F&O MCP Server를 통해 ERP 데이터를 MCP 도구로 직접 노출
- **멀티 에이전트 오케스트레이션**: 단일 에이전트를 넘어 여러 에이전트가 협업하는 복합 워크플로우 지원은 복잡한 엔터프라이즈 시나리오에서 차별화 요소
- **글로벌 인프라**: Azure 글로벌 리전을 활용한 데이터 레지던시 준수 및 확장성

### 약점

- **Dynamics 365 의존성**: Copilot의 핵심 가치는 Dynamics 365 데이터와의 통합에서 나오므로, 비-Microsoft ERP 사용 기업에는 제한적
- **Sidecar 한계**: 사이드 패널 기반 인터페이스는 복잡한 분석이나 대규모 데이터 시각화에 공간적 제약이 있음. 전체 화면 뷰 폐지 결정은 일부 사용자의 불만 요소
- **커스텀 에이전트 복잡성**: Copilot Studio의 고급 기능(멀티 에이전트 오케스트레이션, Computer Use) 활용 시 Power Platform 및 Azure AI 지식이 필요
- **자체 추론 엔진 부재**: Salesforce Atlas나 SAP Knowledge Graph 같은 독자적 추론 엔진 없이 Azure OpenAI Service에 의존하여, LLM 성능 변동에 따른 품질 관리 부담

### 주요 경쟁사 비교

| 항목 | Microsoft Copilot (D365) | Salesforce Agentforce | SAP Joule |
|------|--------------------------|----------------------|-----------|
| 인터페이스 | Sidecar (사이드 패널) | 3-Panel Layout (빌더) | Cross-product Embedded |
| 에이전트 빌더 | Copilot Studio + Agent Builder | Agent Builder | Joule Studio |
| 데이터 기반 | Microsoft Graph + Dataverse | Data Cloud + Zero-Copy | SAP Knowledge Graph |
| 외부 연결 | 1,000+ Power Platform 커넥터 | MuleSoft API Fabric | SAP BTP Integration Suite |
| 멀티 에이전트 | 오케스트레이션 (GA) | 단일 에이전트 중심 | 멀티 에이전트 (초기) |
| 모델 | Azure OpenAI Service | 멀티 모델 (Claude, OpenAI 등) | SAP AI Core (멀티 LLM) |
| 가격 | $30/사용자/월 번들 | $2/대화 + 애드온 | AI Units 소비 기반 |
| 업무 도구 통합 | Teams·Outlook·Word 네이티브 | Slack 중심 | SAP Work Zone + M365 양방향 |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] — Copilot Sidecar 방식, Manager Insights, Conversation Analytics 관련 크로스 제품 비교 참조
- [[리서치 목표 및 벤치마크 대상]] — 엔터프라이즈 AI Agent 벤치마크 대상 제품 목록

## 참고 자료

- [Microsoft Copilot for Dynamics 365 공식 사이트](https://www.microsoft.com/en-us/dynamics-365/copilot)
- [Microsoft Build 2025: Multi-Agent Orchestration Announcement](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/)
- [Microsoft 365 Blog: Copilot Tuning and Multi-Agent Orchestration](https://www.microsoft.com/en-us/microsoft-365/blog/2025/05/19/introducing-microsoft-365-copilot-tuning-multi-agent-orchestration-and-more-from-microsoft-build-2025/)
- [Microsoft Ignite 2025: Copilot and Agents for the Frontier Firm](https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-ignite-2025-copilot-and-agents-built-to-power-the-frontier-firm/)
- [Microsoft Learn: Copilot for Finance and Operations Overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations)
- [Dynamicspedia: Enable MCP in Dynamics 365 F&O Sidecar](https://dynamicspedia.com/2025/10/enable-model-context-protocol-mcp-in-the-dynamics-365-fo-sidecar/)
- [Copilot Studio: What's New (November 2025)](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-microsoft-copilot-studio-november-2025/)
- [Microsoft 365 Copilot Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)
- [Dynamics 365 2025 Release Wave 2 Plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/)
- [Copilot Studio Multi-Agent Orchestration Architecture](https://holgerimbery.blog/multi-agent-orchestration)
