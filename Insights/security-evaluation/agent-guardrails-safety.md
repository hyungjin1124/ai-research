---
type: insight-synthesis
topic_id: agent-guardrails-safety
topic_name: 에이전트 가드레일 & 안전성 비교 분석
category: security-evaluation
tags:
- insight
- security-evaluation
- guardrails
- safety
- Constitutional-AI
- Trust-Layer
- prompt-injection
- hallucination
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
- qa_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - OWASP LLM Top 10
  - AI safety framework
  - LLM guardrails benchmark
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 가드레일 & 안전성 비교 분석

## TL;DR

- AI 에이전트 가드레일은 **모델 계층**(Constitutional AI, RLHF), **플랫폼 계층**(Trust Layer, Orchestrator 정책), **인프라 계층**(샌드박스, 네트워크 격리)의 3단 방어 구조로 수렴하고 있으며, 각 벤더별로 강조하는 계층이 다르다.
- **Prompt injection 방어**는 에이전틱 AI 시대의 최대 보안 과제이며, [[claude/claude|Claude]]만이 구체적 수치(공격 성공률 23.6% → 11.2% 저감)를 공개하여 정량적 벤치마크를 제시한 유일한 벤더이다. [^1]
- 엔터프라이즈 에이전트 플랫폼에서는 **토픽/스킬 기반 범위 제한**(Salesforce Topics, ServiceNow Skills)이 가드레일의 핵심 설계 패턴으로 부상하고 있으며, 이는 모델 자체의 안전성보다 비즈니스 로직 수준의 제어에 초점을 맞추는 접근이다. [^3] [^6] [^8]
- 한국 벤더의 보안 접근법은 **인프라 수준 격리**(삼성SDS SCP, 더존 프라이빗 AI)와 **연결 포인트 보안**(LG CNS SecureXper AI)으로 양분되며, 모델 계층 가드레일에 대한 공개 정보가 극히 제한적이다. [^9] [^10]
- 할루시네이션 완화를 위한 **데이터 그라운딩**(RAG, Knowledge Graph, Data Cloud)은 모든 벤더가 채택하는 공통 전략이지만, 인용 강제(citation enforcement)와 자기 반성(self-reflection) 메커니즘의 성숙도에서 큰 차이가 존재한다.

---

## Overview

에이전틱 AI의 핵심 전환은 AI가 "답변을 생성"하는 것에서 "행동을 실행"하는 것으로 패러다임이 바뀐다는 점이다. 에이전트가 ERP 트랜잭션을 실행하고, 이메일을 발송하고, 코드를 커밋하고, 웹 페이지에서 결제를 수행하는 시대에서, 가드레일의 실패는 단순한 부정확한 답변이 아니라 **재무적 손실, 데이터 유출, 비즈니스 프로세스 오염**으로 직결된다. [^12] 한국 엔터프라이즈 시장은 데이터 보안과 컴플라이언스에 대한 민감도가 높아, 글로벌 벤더와 한국 벤더의 가드레일 접근법을 비교 분석하는 것이 중요하다. 프롬프트 인젝션, 할루시네이션, 독성 콘텐츠 등 에이전트 고유의 안전성 위험에 대한 체계적 대응 전략이 필요하다.

---

## Cross-Product Analysis

### 비교 매트릭스

| 항목 | Claude (Anthropic) | Salesforce Agentforce | Microsoft Copilot | Google Gemini | OpenAI ChatGPT | ServiceNow Now Assist | Workday Assistant | SAP Joule | 삼성SDS FabriX | LG CNS AgenticWorks | Source |
|------|-------------------|----------------------|-------------------|---------------|----------------|----------------------|-------------------|-----------|---------------|---------------------|--------|
| **가드레일 프레임워크** | Constitutional AI (CAI) | Trust Layer + Topic Guardrails | Responsible AI Framework | Safety Settings (4단계) | Safety System (미공개 상세) | Orchestrator 정책 엔진 | ASOR 역할 기반 제어 | SAP AI Foundation 거버넌스 | SCP 인프라 보안 | SecureXper AI 내장 | [^1] [^3] [^4] [^5] [^6] [^9] [^10] |
| **모델 계층 안전성** | RLHF + RLAIF (헌법적 원칙) | Atlas Engine 자기 반성 | Azure OpenAI Safety API | Safety Filters (4단계 조정) | RLHF + 규칙 기반 | 자체 도메인 모델 | 서드파티 LLM 의존 | 멀티 LLM (AI Core) | 멀티 LLM (자체+GPT-4o) | 코히어+엑사원 | [^1] [^2] [^3] |
| **입력 필터링** | Prompt injection 방어 (11.2% 성공률) | Topic 범위 제한 | Content Safety API | Safety Settings 레벨 조정 | Moderation API | 의도 분류 기반 라우팅 | ASOR 액션 범위 정의 | 스킬 기반 범위 제한 | 권한/인증 연계 | MCP/A2A 보안 계층 | [^1] [^3] [^8] |
| **출력 필터링** | 유해 콘텐츠 거부 | 에스컬레이션 규칙 | Content Moderator | SafeSearch 통합 | Output Moderation | Resolution Notes Review | Manager 검토 워크플로우 | Fiori UI 제한 표시 | 미공개 | 미공개 | [^1] [^3] |
| **할루시네이션 완화** | Extended Thinking + 출처 인용 | Data Cloud RAG + 정확도 33% 개선 | Microsoft Graph 그라운딩 | Deep Research 다단계 검증 | Retrieval + Code Interpreter | Genius Results 출처 합성 | Data Cloud 크로스앱 | Knowledge Graph + RAGe | ERP 데이터 그라운딩 | Knowledge Lake | [^1] [^3] [^5] [^6] |
| **데이터 그라운딩** | Projects (200K 컨텍스트) | Data Cloud + Vector DB | Dataverse + Graph | Google Search 실시간 | Retrieval API | Now Platform CMDB | Workday Data Cloud | SAP Business Data Cloud | MCP 기반 ERP 연동 | MCP/A2A 연동 | [^1] [^3] [^9] |
| **HITL 패턴** | Pause & Ask (민감 작업) | Omni Supervisor + 에스컬레이션 | Proposal Review + Email Draft | Deep Research 사용자 승인 | CUA 제어권 반환 | Chat Summarization 전환 | Task Workflow Confirmation | Role-Based 승인 | 미공개 | 미공개 | [^1] [^2] [^3] |
| **샌드박스/격리** | VM 샌드박스 (Cowork) | Salesforce Platform 멀티테넌트 | Azure 리전 격리 | 클라우드 샌드박스 | Codex 독립 샌드박스 | Now Platform 인스턴스 | Workday 테넌트 격리 | BTP 인스턴스 격리 | SCP 인프라 격리 | DAP 플랫폼 격리 | [^1] [^2] [^9] [^11] |
| **보안 인증** | SOC 2 Type II | SOC 2, ISO 27001, FedRAMP | SOC 2, ISO 27001, FedRAMP | SOC 2, ISO 27001 | SOC 2 Type II | SOC 2, ISO 27001, FedRAMP | SOC 2, ISO 27001 | SOC 2, ISO 27001 | ISMS-P, CSA STAR | 미공개 | [^1] [^3] [^9] |

### 패턴 분류

#### 패턴 A: 모델 내재형 가드레일 (Model-Native Guardrails)

**설명**: LLM 학습 단계에서 안전성 원칙을 내재화하여, 모델 자체가 위험한 출력을 생성하지 않도록 설계하는 접근법. 외부 필터 없이도 모델이 자체적으로 안전한 응답을 생성하는 것이 목표이다.

**예시 제품**: [[claude/claude|Claude]] (Constitutional AI), [[openai/openai|OpenAI]] (RLHF 기반 Safety System)

**특징**:
- 학습 데이터와 강화학습 보상 함수에 안전성 원칙을 인코딩
- Anthropic의 Constitutional AI는 인간 피드백(RLHF)과 헌법적 원칙 기반 자기감독(RLAIF)을 결합한 업계 가장 체계적 프레임워크 [^1] [^12]
- 모델 버전 업그레이드 시 안전성도 함께 개선되는 구조적 이점
- 단점: 모델 외부의 비즈니스 로직 수준 제어가 어려우며, 에이전틱 시나리오에서 도구 사용 안전성까지 커버하지 못할 수 있음

#### 패턴 B: 플랫폼 오케스트레이션 가드레일 (Platform Orchestration Guardrails)

**설명**: 에이전트 실행 플랫폼 계층에서 정책 엔진, 토픽/스킬 범위 제한, 에스컬레이션 규칙 등을 통해 에이전트 행동을 제어하는 접근법. 모델의 안전성과 별개로, 비즈니스 프로세스 수준에서 에이전트가 할 수 있는 일의 경계를 명시적으로 정의한다.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] (Topic Guardrails + Atlas 자기 반성), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] (Orchestrator 정책 엔진), [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] (Copilot Studio 제어)

**특징**:
- Salesforce는 Topic 기반으로 에이전트의 역할 범위를 정의하고, 범위 밖 요청은 자동 거부 또는 에스컬레이션 [^3]
- ServiceNow는 Orchestrator에서 Assist 토큰 예산 관리, 역할 기반 접근 제어, 감사 로깅, 서비스 윈도우 정책을 실시간 적용 [^6]
- Microsoft는 Copilot Studio에서 에이전트별 권한과 액션 범위를 로코드로 구성 [^4]
- 장점: 비즈니스 프로세스에 맞춤화된 세밀한 제어가 가능하고, 엔터프라이즈 거버넌스 요구사항에 직접 대응
- 단점: 정책 설정의 복잡성, 초기 구성에 상당한 노력 필요

#### 패턴 C: 인프라 격리형 보안 (Infrastructure Isolation Security)

**설명**: 네트워크 격리, 프라이빗 클라우드, 전용 인스턴스 등 인프라 수준에서 보안을 확보하는 접근법. 모델이나 플랫폼의 가드레일보다 물리적/논리적 격리를 통한 데이터 보호에 초점을 맞춘다.

**예시 제품**: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] (SCP 인프라 보안), 더존 ONE AI (프라이빗 AI / PE)

**특징**:
- 삼성SDS는 Samsung Cloud Platform(SCP) 기반의 인프라 보안과 NVIDIA GPU 통합으로 전용 환경 제공 [^9]
- 더존은 폐쇄망 전용 프라이빗 AI(PE)로 데이터가 외부에 노출되지 않는 구조
- 한국 공공기관과 금융기관의 보안 규정(ISMS-P, 개인정보보호법)에 최적화
- 단점: 에이전트 자체의 행동 제어보다는 데이터 유출 방지에 초점이 맞춰져 있어, 에이전트가 잘못된 행동을 하는 것 자체를 방지하지는 못함

#### 패턴 D: 에이전트-시스템 연결 포인트 보안 (Agent-System Junction Security)

**설명**: AI 에이전트와 기업 시스템 간의 연결 포인트 전체에 보안을 내재화하는 접근법. 에이전트가 외부 시스템에 접근하는 모든 지점에서 인증, 인가, 감사, 이상 탐지를 수행한다.

**예시 제품**: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] (SecureXper AI)

**특징**:
- LG CNS의 SecureXper AI는 에이전트-ERP, 에이전트-그룹웨어, 에이전트-CRM 등 모든 연결 포인트에 보안 솔루션을 내장 [^10]
- MCP/A2A 프로토콜 통신 과정에서의 보안을 별도 계층으로 관리
- 에이전틱 AI 시대에 구조적으로 적합한 모델로 평가 — 에이전트가 다수의 외부 시스템과 통신하는 구조에서 연결 포인트별 보안이 필수적
- 단점: 에이전트 내부의 추론 과정이나 출력 품질에 대한 제어는 별도로 필요

---

## Key Findings

1. **Constitutional AI가 유일한 체계적 모델 안전성 프레임워크**: 조사 대상 11개 제품 중, 모델 학습 단계에서 안전성 원칙을 체계적으로 내재화한 프레임워크를 공개한 것은 [[claude/claude|Claude]]의 Constitutional AI가 유일하다. [^1] [^12] OpenAI도 RLHF 기반 안전성을 적용하지만 구체적 프레임워크 명칭과 방법론을 Anthropic만큼 상세히 공개하지 않았다. [^2] 엔터프라이즈 벤더(Salesforce, Microsoft, SAP, ServiceNow)는 모델 자체 안전성보다 플랫폼 수준의 정책 제어에 집중하여 외부 LLM에 의존하는 구조적 한계를 보여준다.

2. **Prompt injection 정량 데이터의 극심한 부재**: 브라우저 에이전트 시대에 prompt injection은 가장 위험한 공격 벡터이지만, 방어 성공률을 정량적으로 공개한 벤더는 [[claude/claude|Claude]] (Claude in Chrome에서 23.6% → 11.2% 저감) 한 곳뿐이다. [^1] [^13] [[openai/openai|OpenAI]]의 CUA(Computer-Using Agent)는 민감 작업 시 사용자 확인을 요청하는 HITL 패턴을 적용하지만 방어율 수치는 미공개이다. [^2] [[google-gemini/google-gemini|Google Gemini]]의 Project Mariner 역시 pause & ask 패턴을 사용하나 정량 데이터가 없다. [^5] 이는 업계 전체가 에이전트 보안 벤치마크의 초기 단계에 있음을 의미한다.

3. **토픽/스킬 기반 범위 제한이 엔터프라이즈 가드레일의 지배적 패턴**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]의 Topic-Action 모델, [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]]의 Skills 아키텍처, [[sap-joule/sap-joule|SAP Joule]]의 2,400+ 스킬 카탈로그 모두 에이전트가 수행할 수 있는 범위를 사전에 정의하고 그 밖의 요청은 거부하는 "허용 목록(allowlist)" 방식을 채택한다. [^3] [^6] [^8] 이는 범용 LLM의 개방적 특성을 비즈니스 프로세스에 맞게 제한하는 가장 실용적인 접근법이다.

4. **할루시네이션 완화 전략의 3가지 계층**: 모든 벤더가 RAG(Retrieval-Augmented Generation)를 기본으로 채택하지만, 그 위에 얹는 추가 안전장치에서 차이가 난다. (1) **데이터 그라운딩**: Salesforce Data Cloud, Microsoft Graph/Dataverse, SAP Knowledge Graph 등 1차 데이터 소스 연결, (2) **추론 투명성**: Claude Extended Thinking, Atlas Engine 자기 반성(self-reflection)으로 추론 과정을 표면화하여 오류를 사전 탐지, (3) **출처 강제**: Claude의 인라인 출처 표기, ServiceNow Genius Results의 출처 문서 링크, Deep Research의 근거 인라인 표시 등으로 사용자가 검증 가능한 형태로 정보를 제공. Salesforce는 Atlas Engine 도입 후 응답 관련성 2배 향상, 정확도 33% 개선이라는 구체적 수치를 공개했다. [^3] [^1]

5. **한국 벤더의 가드레일 정보 공개 수준이 글로벌 대비 현저히 낮음**: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]]와 [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] 모두 MCP/A2A 프로토콜 지원과 인프라 보안을 강조하지만, 모델 계층의 입출력 필터링, 독성 콘텐츠 방지, 할루시네이션 완화율, prompt injection 방어 메커니즘 등에 대한 구체적 정보를 공개하지 않았다. [^9] [^10] 이는 (1) 외부 LLM(GPT-4o, 코히어, 엑사원)에 안전성을 위임하고 있거나, (2) 자체 가드레일을 보유하되 공개하지 않는 것 중 하나이며, 어느 경우든 고객의 신뢰 확보에 불리하다.

6. **샌드박스 격리가 에이전트 안전성의 물리적 최후 방어선**: [[claude/claude|Claude]] Cowork의 VM 샌드박스, [[openai/openai|OpenAI]] Codex의 독립 클라우드 샌드박스, [[manus-ai/manus-ai|Manus AI]]의 14일 비동기 클라우드 샌드박스 모두 에이전트의 코드 실행과 파일 시스템 접근을 격리된 환경에서 수행한다. [^1] [^2] [^11] 에이전트가 호스트 시스템에 직접적으로 해를 끼칠 수 없도록 물리적으로 차단하는 이 패턴은 가드레일의 소프트웨어적 한계를 보완하는 마지막 방어선이다. 엔터프라이즈 ERP 에이전트에서도 트랜잭션 실행 전 스테이징 환경에서 사전 검증하는 유사한 패턴이 필요하다. [출처 필요]

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-11 | [Minitap: AndroidWorld 100% success](https://arxiv.org/abs/2602.07787) · [[2026/02/2026-02-11\|다이제스트]] | Minitap 멀티에이전트 AndroidWorld 벤치마크 116개 태스크 100% 달성. 인간 성능 초과 | #security-evaluation |
| 2026-02-11 | [NAAMSE: Evolutionary Security Evaluation](https://arxiv.org/abs/2602.07391) · [[2026/02/2026-02-11\|다이제스트]] | 에이전트 보안 평가 진화적 프레임워크. 유전적 프롬프트 변이 + 계층적 코퍼스 탐색 | #security-evaluation |
| 2026-02-12 | [OpenAI Mission Alignment Team 해산](https://techcrunch.com/2026/02/11/openai-disbands-mission-alignment-team-which-focused-on-safe-and-trustworthy-ai-development/) · [[2026/02/2026-02-12\|다이제스트]] | OpenAI 두 번째 안전팀 해체(2024 Superalignment에 이어). 리더 'Chief Futurist'로 전환, 나머지 재배치. 안전 우선주의 후퇴 우려 | #security-evaluation |

---

## References

### Vault
- [^1]: [[AI Agent Products/claude/claude|Claude (Anthropic)]] — Constitutional AI, Extended Thinking, Prompt injection 방어
- [^2]: [[AI Agent Products/openai/openai|OpenAI ChatGPT]] — CUA HITL 패턴, Codex 샌드박스
- [^3]: [[AI Agent Products/salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Atlas Engine, Topic Guardrails, Omni Supervisor
- [^4]: [[AI Agent Products/microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — Responsible AI, Copilot Studio 제어
- [^5]: [[AI Agent Products/google-gemini/google-gemini|Google Gemini]] — Safety Settings, Deep Research 검증
- [^6]: [[AI Agent Products/servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — Orchestrator 정책 엔진, Skills 가드레일
- [^7]: [[AI Agent Products/workday-assistant/workday-assistant|Workday Assistant]] — ASOR 역할 기반 에이전트 제어
- [^8]: [[AI Agent Products/sap-joule/sap-joule|SAP Joule]] — SAP AI Foundation 거버넌스, 2400+ 스킬 범위 제한
- [^9]: [[AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] — SCP 인프라 보안, 권한/인증 연계
- [^10]: [[AI Agent Products/lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] — SecureXper AI 연결 포인트 보안
- [^11]: [[AI Agent Products/manus-ai/manus-ai|Manus AI]] — 클라우드 샌드박스 격리, Self-Correction Loop

### External
- [^12]: [Anthropic: Claude's Constitutional AI Approach](https://www.anthropic.com/research/constitutional-ai) — Constitutional AI 프레임워크 상세
- [^13]: [Anthropic: Piloting Claude in Chrome — Safety](https://claude.com/blog/claude-for-chrome) — Prompt injection 방어율 수치
- [^14]: [Salesforce Engineering: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/) — Atlas Engine 자기 반성 메커니즘
- [^15]: [Microsoft: Responsible AI Principles](https://www.microsoft.com/en-us/ai/responsible-ai) — Microsoft AI 안전성 원칙
- [^16]: [OWASP: LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — LLM 보안 위협 프레임워크
- [^17]: [ServiceNow: AI Agent Orchestrator — Governance](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-announces-new-agentic-AI-innovations-to-autonomously-solve-the-most-complex-enterprise-challenges-01-29-2025-traffic/default.aspx) — Orchestrator 거버넌스

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
