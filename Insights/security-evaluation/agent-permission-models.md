---
type: insight-synthesis
topic_id: agent-permission-models
topic_name: 에이전트 권한 모델 비교 분석
category: security-evaluation
tags:
- insight
- security-evaluation
- permission-model
- RBAC
- HITL
- audit-logging
- compliance
- data-access
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- salesforce-agentforce
- microsoft-copilot
- google-gemini
- openai
- servicenow-now-assist
- workday-assistant
- sap-joule
- samsung-sds-fabrix
- lgcns-agenticworks
- manus-ai
source_files:
- AI Agent Products/claude/claude.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/openai/openai.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
- AI Agent Products/manus-ai/manus-ai.md
relevant_roles:
- architecture_agent
- backend_agent
- data_agent
- qa_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI agent permission model
  - ASOR agent system of record
  - RBAC ABAC agent access control
  - MCP A2A agent delegation
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 권한 모델 비교 분석

## TL;DR

- AI 에이전트 권한 모델은 **행동 제어형**(Allow/Deny/Ask -- Claude), **데이터 접근 제어형**(Trust Layer -- Salesforce, RBAC -- ServiceNow), **에이전트 신원 관리형**(ASOR -- Workday)의 3가지 패러다임으로 분류되며, 시장은 이 세 접근법의 하이브리드 모델로 수렴하고 있다.
- [[workday-assistant/workday-assistant|Workday Assistant]]의 ASOR(Agent System of Record)는 AI 에이전트를 인간 직원과 동일한 방식으로 관리(채용, 역할 배정, 권한 설정, 성과 추적, 퇴직)하는 업계 최초의 에이전트 신원 관리 시스템으로, 에이전트 권한 모델의 가장 혁신적 접근이다. [^5]
- HITL(Human-in-the-Loop) 승인 모델은 모든 벤더가 구현하지만, **승인 트리거 기준**(작업 유형, 금액 임계값, 위험도 레벨)과 **에스컬레이션 경로**(AI->인간, AI->관리자, AI->상위 에이전트)의 설계에서 큰 차이가 존재한다.
- **감사 로깅**(Audit Logging)은 엔터프라이즈 에이전트의 필수 요건이지만, 에이전트의 추론 과정까지 포함하는 "설명 가능한 감사 로그"를 제공하는 벤더는 [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]](Step-by-Step Reasoning 시각화)와 [[manus-ai/manus-ai|Manus AI]](Glass Box 실행 트리)에 한정된다. [^2] [^11]
- 한국 벤더의 에이전트 권한 모델은 **기존 기간계 시스템의 권한 체계를 그대로 상속**(삼성SDS)하거나 **폐쇄망 격리**(더존 프라이빗 AI)하는 인프라 중심 접근을 취하며, 에이전트 고유의 세분화된 권한 제어에 대한 공개 정보가 부족하다. [^8] [^9]

---

## Overview

에이전틱 AI에서 "권한"의 의미는 근본적으로 달라진다. 전통적 소프트웨어에서 권한은 "사용자가 어떤 메뉴/기능에 접근할 수 있는가"의 문제였지만, AI 에이전트에서는 "에이전트가 어떤 데이터를 읽을 수 있는가, 어떤 트랜잭션을 실행할 수 있는가, 어떤 외부 시스템에 접근할 수 있는가, 어떤 결정을 자율적으로 내릴 수 있는가"로 확장된다. 더 나아가, 에이전트가 다른 에이전트에게 태스크를 위임하거나(A2A), 외부 도구를 호출하거나(MCP), 사용자를 대신하여 행동할 때의 권한 위임(delegation) 문제까지 포함한다. [^12] 한국 엔터프라이즈 시장에서 개인정보보호법, 전자금융거래법, 내부통제 규정, SOC 2, ISMS-P 등의 컴플라이언스 프레임워크를 만족하는 에이전트 권한 모델이 시장 진입의 핵심 요건이다. [^14] [^15]

---

## Cross-Product Analysis

### 비교 매트릭스

| 항목 | Claude (Anthropic) | Salesforce Agentforce | Microsoft Copilot | ServiceNow Now Assist | Workday Assistant | SAP Joule | 삼성SDS FabriX | LG CNS AgenticWorks | OpenAI | Google Gemini | Manus AI | Source |
|------|-------------------|----------------------|-------------------|----------------------|-------------------|-----------|---------------|---------------------|--------|---------------|----------|--------|
| **권한 모델 패러다임** | Allow/Deny/Ask | Topic-Action 범위 제한 + ABAC | RBAC + Power Platform | RBAC + Orchestrator 정책 | ASOR (에이전트=직원) | Role-Based + 스킬 제한 | 기존 시스템 권한 상속 | MCP/A2A + SecureXper | 사용자 승인 기반 | Safety Settings | 크레딧 기반 + 샌드박스 | [^1] [^2] [^3] [^4] [^5] [^6] [^8] [^9] |
| **데이터 읽기 범위** | Projects 컨텍스트, 허용 폴더 | Data Cloud + Zero-Copy | Microsoft Graph + Dataverse | Now Platform CMDB | Workday Data Cloud + RBAC | SAP Business Data Cloud | MCP 기반 ERP 데이터 | MCP/A2A 연동 | 대화 컨텍스트 | Google 에코시스템 | 브라우저 접근 범위 | [^1] [^2] [^5] [^8] |
| **데이터 쓰기/실행** | 파일 I/O, Git 커밋, 터미널 (승인 기반) | Flow/Apex/API 실행 | Power Automate 액션 | 워크플로우 자동화 | 비즈니스 프로세스 실행 | SAP 트랜잭션 실행 | ERP 트랜잭션 (MCP) | ERP/그룹웨어 실행 | 브라우저 작업 실행 | Google 앱 작업 | 코드 실행, 파일 생성 | [^1] [^2] [^7] [^11] |
| **HITL 승인 패턴** | Pause & Ask (민감 작업) | 에스컬레이션 규칙 + Omni Supervisor | Proposal Review + Email Draft 편집 | Chat Summarization 전환 + Resolution Notes | Task Workflow Confirmation + Manager 검토 | SuccessFactors 승인 + Ariba 검토 | 미공개 | 미공개 | CUA 제어권 반환 | Deep Research 사용자 승인 | Watch & Intervene | [^1] [^2] [^4] [^5] [^7] [^11] |
| **에스컬레이션 경로** | AI -> 사용자 | AI -> 인간 에이전트 (Omni-Channel) | AI -> 관리자 (Teams) | AI -> 인간 에이전트 (Chat Summarization) | AI -> Manager (ASOR) | AI -> 역할별 승인자 | 미공개 | 미공개 | AI -> 사용자 | AI -> 사용자 | AI -> 사용자 (개입 요청) | [^1] [^2] [^4] [^5] |
| **감사 로깅** | CLI 실행 로그 | Step-by-Step Reasoning 시각화 | Plugin 선택 과정 표시 | Orchestrator 감사 로깅 | ASOR 실행 로그 + 성과 추적 | 미공개 | 미공개 | 미공개 | Codex 실행 로그 | 미공개 | 실행 트리 + Glass Box | [^2] [^4] [^5] [^7] [^11] |
| **멀티에이전트 권한** | 해당 없음 | 단일 에이전트 중심 | 멀티에이전트 오케스트레이션 | Orchestrator 팀 조율 | Agent Partner Network (50+) | Collaborative Agent | A2A 프로토콜 | A2A 프로토콜 | 해당 없음 | 해당 없음 | Planner -> 서브에이전트 | [^3] [^4] [^5] [^8] |
| **외부 에이전트 권한** | MCP 서버별 도구 접근 | MuleSoft + Agentforce Gateway (ABAC) | Power Platform 커넥터 | REST API 커넥터 | Agent Gateway (MCP/A2A) | A2A 프로토콜 | MCP/A2A 연동 | MCP/A2A + Hub 모듈 | MCP (채택) | MCP + A2A | 브라우저 자동화 | [^1] [^2] [^5] [^8] [^9] |
| **컴플라이언스** | SOC 2 Type II | SOC 2, ISO 27001, FedRAMP, HIPAA | SOC 2, ISO 27001, FedRAMP | SOC 2, ISO 27001, FedRAMP, HIPAA | SOC 2, ISO 27001 | SOC 2, ISO 27001 | ISMS-P, CSA STAR | 미공개 | SOC 2 Type II | SOC 2, ISO 27001 | 미공개 | [^1] [^2] [^8] |

### 패턴 분류

#### 패턴 A: 행동 수준 권한 제어 (Action-Level Permission Control)

**설명**: 에이전트가 수행하는 개별 행동(Action)에 대해 Allow(허용), Deny(거부), Ask(사용자 확인 요청)의 세 가지 상태를 정의하는 권한 모델. 에이전트의 각 도구 호출, 파일 접근, 시스템 명령에 대해 세분화된 제어를 제공한다.

**예시 제품**: [[claude/claude|Claude]] (Claude Code/Cowork의 Allow/Deny/Ask 패턴)

**특징**:
- Claude Code는 파일 읽기/쓰기, 터미널 명령 실행, Git 작업 등 각 행동에 대해 사용자가 승인 수준을 설정 [^1]
- Claude Cowork는 VM 샌드박스 내에서 허용 폴더를 한정하여 파일 접근 범위를 물리적으로 제한
- Claude in Chrome은 민감 작업(결제, 로그인 등)에서 "pause & ask" 패턴으로 사용자 확인을 요청
- 장점: 개별 행동 수준의 세밀한 제어, 사용자에게 직관적
- 단점: 행동 수가 많아질수록 설정 부담 증가, 엔터프라이즈 규모의 역할 기반 관리에는 부적합

#### 패턴 B: 토픽/역할 기반 범위 제한 (Topic/Role-Based Scope Restriction)

**설명**: 에이전트의 역할(Role)과 담당 토픽(Topic)/스킬(Skill)을 사전에 정의하고, 정의된 범위 밖의 요청은 자동 거부하거나 에스컬레이션하는 권한 모델. 엔터프라이즈 에이전트의 가장 보편적인 접근법이다.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] (Topic-Action + ABAC), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] (Skills + Orchestrator RBAC), [[sap-joule/sap-joule|SAP Joule]] (2,400+ 스킬 기반 + Role-Based Assistants), [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] (RBAC + Copilot Studio)

**특징**:
- Salesforce: Topic 기반으로 에이전트의 역할 범위를 정의하고, Agentforce Gateway에서 ABAC(속성 기반 접근 제어), 할당량 제한, 인증/인가를 처리. MuleSoft를 통한 외부 API 접근도 Gateway에서 통합 거버넌스 [^2] [^13]
- ServiceNow: Orchestrator에서 역할 기반 접근 제어, 감사 로깅, 서비스 윈도우 정책을 실시간 적용. Assist 토큰 예산 관리로 비용 수준의 제어도 포함 [^4]
- SAP Joule: 2,400+ 스킬 카탈로그에서 역할별로 접근 가능한 스킬을 자동 노출. Role-Based AI Assistants가 사용자 역할에 맞춤화된 에이전트를 자동 연결 [^6]
- Microsoft: Copilot Studio에서 에이전트별 권한과 액션 범위를 로코드로 구성. 1,000+ Power Platform 커넥터의 접근도 Studio에서 통합 관리 [^3]
- 장점: 엔터프라이즈 RBAC 체계와 자연스럽게 통합, 관리자 친화적
- 단점: 역할 정의의 초기 투자 비용 높음, 역할 경계의 유연성 제한

#### 패턴 C: 에이전트 신원 관리 (Agent Identity Management)

**설명**: AI 에이전트를 인간 직원과 동일한 방식으로 관리하는 혁신적 접근법. 에이전트의 "채용"(등록), "온보딩"(권한 설정), "역할 배정", "성과 추적", "퇴직"(비활성화)까지 전체 라이프사이클을 인사 관리 프레임워크로 통합한다.

**예시 제품**: [[workday-assistant/workday-assistant|Workday Assistant]] (ASOR)

**특징**:
- Agent Registry: 모든 에이전트의 메타데이터(역할, 권한, 상태, 성과)를 중앙 레지스트리에서 관리 [^5]
- 보안 그룹 할당: 에이전트를 인간 직원과 동일한 보안 그룹에 배치하여 데이터 접근 범위를 통제
- 국가별 가용성: 에이전트의 가동 범위를 국가/지역 단위로 제한 (데이터 레지던시 대응)
- Agent Partner Network: 50+ 파트너의 외부 에이전트도 ASOR에 등록하여 통합 관리. 자사 에이전트와 동일한 거버넌스 정책 적용 [^5] [^16]
- Agent Gateway: MCP/A2A 프로토콜 기반으로 내부/외부 에이전트 간 통신을 표준화하면서, ASOR의 권한 정책을 실시간 적용
- 장점: 기존 HR/거버넌스 프로세스와 완벽 통합, 감사/규제 대응에 최적, 멀티벤더 에이전트 통합 관리
- 단점: HR 도메인 특화 설계로 범용 적용 시 추상화 필요, ASOR 자체의 구축 복잡성

#### 패턴 D: 인프라 수준 접근 제어 (Infrastructure-Level Access Control)

**설명**: 에이전트 자체의 세분화된 권한 모델 대신, 인프라 수준에서 네트워크 격리, 전용 인스턴스, 기존 시스템의 인증/인가 체계 상속을 통해 접근을 통제하는 접근법.

**예시 제품**: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] (기존 시스템 권한 상속), 더존 ONE AI (프라이빗 AI 폐쇄망)

**특징**:
- 삼성SDS FabriX: "사내 시스템의 권한/인증 체계를 에이전트가 그대로 활용하여 보안 유지"라는 원칙. MCP를 통해 기간계 시스템에 접근할 때 해당 시스템의 기존 인증/인가를 상속 [^8]
- 더존 ONE AI: 프라이빗 AI(PE)를 통해 폐쇄망에서 AI를 구동하여 데이터 자체가 외부에 노출되지 않는 구조
- 장점: 기존 보안 투자를 재활용, 추가 권한 관리 시스템 불필요
- 단점: 에이전트 고유의 행동(추론, 도구 호출, 멀티스텝 실행)에 대한 세분화된 제어 부재, 에이전트 간 통신(A2A)에서의 권한 위임 모델 미비

---

## Key Findings

1. **Workday ASOR가 에이전트 권한 모델의 패러다임을 전환**: 조사 대상 11개 제품 중, [[workday-assistant/workday-assistant|Workday Assistant]]의 ASOR만이 에이전트를 "소프트웨어 컴포넌트"가 아닌 "디지털 직원"으로 관리하는 프레임워크를 제시했다. [^5] 에이전트의 채용-온보딩-역할배정-운영-성과추적-퇴직의 전체 라이프사이클을 HR 프로세스로 관리하고, 50개 이상 파트너의 외부 에이전트도 동일한 레지스트리에 등록하는 이 접근법은, 멀티벤더 에이전트 환경에서의 통합 거버넌스 모델로서 업계에 새로운 참조 아키텍처를 제시한다. [^16] Agent Gateway를 통한 MCP/A2A 프로토콜 연동도 ASOR 정책 하에서 수행된다는 점이 핵심이다.

2. **Salesforce Agentforce Gateway의 ABAC가 가장 세분화된 외부 접근 제어**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]의 Agentforce Gateway는 Envoy 기반 정책 엔진으로 에이전트 트래픽에 대한 ABAC(속성 기반 접근 제어), 할당량 제한, 인증/인가를 처리한다. [^2] [^13] MuleSoft API Fabric과 결합하여 외부 시스템(SAP, Workday 등) API를 에이전트 액션으로 직접 노출하면서도, Topic Center에서 설계 시점(design-time)에 API와 토픽/액션의 매핑을 정의한다. 이는 "런타임 접근 제어"와 "설계 시점 범위 정의"를 모두 갖춘 가장 포괄적인 외부 시스템 접근 제어 모델이다.

3. **HITL 승인 패턴의 성숙도 격차가 큼**: 모든 벤더가 HITL을 구현하지만 성숙도에 큰 차이가 있다. (1) **가장 성숙**: ServiceNow의 Chat Summarization 전환(AI가 인간 에이전트에게 대화 요약을 전달하며 핸드오프)과 Salesforce의 Omni Supervisor(관리자가 AI와 인간 에이전트를 동일 대시보드에서 실시간 감독, "Listen-in" 기능으로 진행 중 대화 감청 가능) [^4] [^2], (2) **중간**: Claude의 pause & ask(민감 작업 시 사용자 확인), OpenAI CUA의 제어권 반환(CAPTCHA, 로그인 시), Workday의 Manager 검토 워크플로우 [^1] [^7] [^5], (3) **기초**: 한국 벤더(삼성SDS, LG CNS)는 HITL 패턴에 대한 구체적 정보를 공개하지 않았다. [^8] [^9]

4. **MCP/A2A 환경에서의 권한 위임 문제가 미해결**: 에이전트가 MCP를 통해 외부 도구를 호출하거나, A2A를 통해 다른 에이전트에게 태스크를 위임할 때, 원래 사용자의 권한이 어떻게 전파(propagation)되는지에 대한 명확한 모델을 제시한 벤더가 없다. [^5] [^2] [^8] [[workday-assistant/workday-assistant|Workday]]의 Agent Gateway와 [[salesforce-agentforce/salesforce-agentforce|Salesforce]]의 Agentforce Gateway가 가장 가까운 솔루션이지만, 에이전트 A가 에이전트 B에게 태스크를 위임할 때 권한의 범위 축소(least privilege), 임시 토큰 발급, 위임 체인 추적 등의 세부 메커니즘은 아직 업계 표준이 정립되지 않았다. [출처 필요]

5. **감사 로깅의 "설명 가능성" 차원이 새로운 차별화 요소**: 단순한 행동 로그(누가, 언제, 무엇을 했는가)를 넘어, 에이전트의 추론 과정(왜 그 결정을 내렸는가)까지 포함하는 "설명 가능한 감사 로그"는 내부감사와 규제 대응에서 핵심적이다. [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]의 Step-by-Step Reasoning 시각화(Topic -> Action -> Record -> Grounding 단계별 표시)와 [[manus-ai/manus-ai|Manus AI]]의 Glass Box(실행 트리 + 코드 노출)가 이 방향의 선두에 있다. [^2] [^11] Claude의 Extended Thinking도 추론 과정 요약을 사용자에게 표시하지만, 이를 감사 로그 형태로 저장/검색하는 기능은 언급되지 않았다. [^1]

6. **한국 벤더의 권한 모델이 "시스템 권한 상속"에 머물러 있음**: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]]는 "사내 시스템의 권한/인증 체계를 에이전트가 그대로 활용"하는 접근을 취하고, [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]]는 SecureXper AI로 연결 포인트 보안을 제공하지만 에이전트 자체의 세분화된 권한 모델(ABAC, ASOR 등)에 대한 정보를 공개하지 않았다. [^8] [^9] MCP/A2A를 통해 에이전트가 기간계 시스템에 접근할 때 기존 ERP의 RBAC을 그대로 상속하는 것은 최소 기준일 뿐, 에이전트의 자율적 판단(어떤 트랜잭션을 실행할 것인가)에 대한 별도의 승인 체계가 필요하다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|

---

## References

### Vault
- [^1]: [[AI Agent Products/claude/claude|Claude (Anthropic)]] — Allow/Deny/Ask 패턴, VM 샌드박스 허용 폴더, pause & ask HITL
- [^2]: [[AI Agent Products/salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Topic-Action 범위 제한, Agentforce Gateway ABAC, Omni Supervisor, Step-by-Step Reasoning
- [^3]: [[AI Agent Products/microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — Copilot Studio RBAC, Power Platform 커넥터 거버넌스, 멀티에이전트 오케스트레이션
- [^4]: [[AI Agent Products/servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — Orchestrator RBAC, Assist 토큰 예산, Chat Summarization 전환, 감사 로깅
- [^5]: [[AI Agent Products/workday-assistant/workday-assistant|Workday Assistant]] — ASOR, Agent Registry, Agent Gateway (MCP/A2A), Agent Partner Network, 라이프사이클 관리
- [^6]: [[AI Agent Products/sap-joule/sap-joule|SAP Joule]] — Role-Based Assistants, 2400+ 스킬 범위 제한, Collaborative Agent, A2A 프로토콜
- [^7]: [[AI Agent Products/openai/openai|OpenAI ChatGPT]] — CUA 제어권 반환, Codex 샌드박스 격리
- [^8]: [[AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] — 기존 시스템 권한/인증 상속, MCP/A2A 프로토콜, SCP 인프라 보안
- [^9]: [[AI Agent Products/lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] — SecureXper AI 연결 포인트 보안, Hub 모듈 시스템 연동, MCP/A2A
- [^10]: [[AI Agent Products/google-gemini/google-gemini|Google Gemini]] — Safety Settings, Deep Research 사용자 승인
- [^11]: [[AI Agent Products/manus-ai/manus-ai|Manus AI]] — 샌드박스 격리, Glass Box 투명성, Watch & Intervene HITL

### External
- [^12]: [Model Context Protocol Specification](https://modelcontextprotocol.io/) — MCP 프로토콜 스펙
- [^13]: [Salesforce Architects: Architecting the Agentic Enterprise with MuleSoft](https://architect.salesforce.com/fundamentals/mulesoft-architecting-agentic-enterprise) — Agentforce Gateway 아키텍처
- [^14]: [한국 개인정보보호법](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=246275) — 한국 개인정보보호 규정
- [^15]: [금융분야 AI 가이드라인 -- 금융위원회](https://www.fsc.go.kr/) — 금융 AI 규제
- [^16]: [Workday: Agent Gateway & Partner Network](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces) — Agent Partner Network
- [^17]: [Salesforce: Agentforce Gateway + ABAC](https://www.salesforceben.com/everything-you-need-to-know-about-mulesoft-for-agentforce/) — ABAC 접근 제어
- [^18]: [ServiceNow: AI Agent Orchestrator](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-announces-new-agentic-AI-innovations-to-autonomously-solve-the-most-complex-enterprise-challenges-01-29-2025-traffic/default.aspx) — Orchestrator 거버넌스
- [^19]: [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) — AI 위험 관리 프레임워크

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
