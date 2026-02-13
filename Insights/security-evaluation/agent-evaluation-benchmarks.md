---
type: insight-synthesis
topic_id: agent-evaluation-benchmarks
topic_name: 에이전트 평가 & 벤치마크 프레임워크
category: security-evaluation
tags:
- insight
- security-evaluation
- evaluation
- benchmarks
- SWE-bench
- GAIA
- testing
- agent-evaluation
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- google-gemini
- salesforce-agentforce
- microsoft-copilot
- servicenow-now-assist
- workday-assistant
- sap-joule
- samsung-sds-fabrix
- lgcns-agenticworks
- manus-ai
source_files:
- AI Agent Products/claude/claude.md
- AI Agent Products/openai/openai.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
- AI Agent Products/manus-ai/manus-ai.md
relevant_roles:
- planning_agent
- qa_agent
- sales_agent
auto_update:
  enabled: true
  keywords:
  - AI agent evaluation benchmarks
  - SWE-bench agent performance
  - enterprise AI agent testing
  - agent evaluation framework
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 평가 & 벤치마크 프레임워크

## TL;DR

- AI 에이전트 평가 체계는 **모델 벤치마크**(SWE-bench, MMLU, HumanEval 등), **에이전트 태스크 벤치마크**(WebVoyager, WebArena, OSWorld, GAIA), **엔터프라이즈 내부 평가**(A/B 테스트, 인간 평가, 자동 스코어링)의 3계층으로 분화되고 있으며, 각 계층의 상관관계가 검증되지 않았다는 점이 핵심 과제이다.
- **코딩 에이전트 영역**에서 SWE-bench Verified가 사실상 표준 벤치마크로 자리잡았으며, [[claude/claude|Claude]] Sonnet 5(82.1%)가 [[openai/openai|OpenAI]] GPT-5.2(80.0%)와 [[google-gemini/google-gemini|Google Gemini]](76.8%)를 앞서고 있다. [^1] [^2] [^3]
- **브라우저 에이전트 벤치마크**(WebVoyager, WebArena, OSWorld)에서는 [[openai/openai|OpenAI]]의 CUA 모델이 유일하게 정량 데이터(WebVoyager 87%, WebArena 58.1%, OSWorld 38.1%)를 공개했으며, 다른 벤더는 비교 가능한 수치를 제시하지 않고 있다. [^2]
- 엔터프라이즈 AI 에이전트 벤더(Salesforce, ServiceNow, SAP, Workday)는 **외부 학술 벤치마크 대신 내부 비즈니스 KPI**(해결률, 응답 시간, ROI, 사용자 만족도)를 평가 기준으로 사용하며, 벤더 간 직접 비교가 불가능한 폐쇄적 평가 구조를 형성하고 있다. [^4] [^6] [^8]
- 한국 벤더(삼성SDS, LG CNS)는 **실증 ROI 데이터**(일일 5시간 20분 절감, 연간 100억 원+ 비용 절감)를 공개하지만, 에이전트 자체의 정확도/성공률에 대한 기술적 벤치마크 데이터는 부재하다. [^9] [^10]

---

## Overview

AI 에이전트 시장이 성숙함에 따라, "어떤 에이전트가 더 나은가?"라는 질문에 대한 객관적 답변이 점점 더 중요해지고 있다. 그러나 현재 에이전트 평가 생태계는 심각하게 파편화되어 있다. LLM 벤더(Anthropic, OpenAI, Google)는 학술 벤치마크(SWE-bench, MMLU, GAIA)를 중심으로 경쟁하고, 엔터프라이즈 벤더(Salesforce, ServiceNow, SAP)는 자체 내부 KPI로 성과를 보고하며, 한국 벤더(삼성SDS, LG CNS)는 도입 기업의 ROI 수치를 마케팅 자료로 활용한다. 이 세 세계는 서로 다른 언어를 쓰고 있어, 크로스 벤더 비교가 극히 어렵다. [^12] [^13]

---

## Cross-Product Analysis

### 비교 매트릭스

| 항목 | Claude (Anthropic) | OpenAI | Google Gemini | Salesforce Agentforce | Microsoft Copilot | ServiceNow Now Assist | Workday Assistant | SAP Joule | 삼성SDS FabriX | LG CNS AgenticWorks | Manus AI | Source |
|------|-------------------|--------|---------------|----------------------|-------------------|----------------------|-------------------|-----------|---------------|---------------------|----------|--------|
| **외부 벤치마크 공개** | SWE-bench, MMLU, HumanEval | SWE-bench, WebVoyager, WebArena, OSWorld | SWE-bench, HLE, BrowseComp | 자체 (정확도 33% 개선) | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | [^1] [^2] [^3] [^4] |
| **코딩 벤치마크** | SWE-bench 82.1% (Sonnet 5), 80.9% (Opus 4.5) | SWE-bench 80.0% (GPT-5.2) | SWE-bench 76.8% | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | [^1] [^2] [^3] |
| **브라우저 에이전트 벤치마크** | 미공개 | WebVoyager 87%, WebArena 58.1%, OSWorld 38.1% | HLE/BrowseComp SOTA | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | [^2] |
| **내부 테스트 도구** | Claude Code 테스트 | OpenAI Evals (오픈소스) | 자체 평가 프레임워크 | Testing Center + AgentEval | Copilot Studio 테스트 | Testing Center | 미공개 | Joule Studio 테스트 | 미공개 | 미공개 | Self-Correction Loop | [^1] [^2] [^4] [^11] |
| **비즈니스 KPI 공개** | 매출 5.5배 성장 (Claude Code) | 미공개 | 미공개 | 응답 관련성 2배, 정확도 33% 개선 | 미공개 | 미공개 | 미공개 | 수작업 70% 절감 (Cash Mgmt) | 일일 5시간20분 절감, 67% 감소 | 생산성 10% 향상, 연 100억+ 절감, 채용 26% 개선 | 연 매출 런레이트 $1억 | [^1] [^4] [^8] [^9] [^10] [^11] |
| **A/B 테스트** | 미공개 | 미공개 | 미공개 | Test Drive 모드 | 미공개 | 시나리오 기반 검증 | 미공개 | 미공개 | 미공개 | 미공개 | 미공개 | [^4] |
| **인간 평가 체계** | RLHF/RLAIF 내장 | RLHF 내장 | 미공개 | Omni Supervisor 실시간 감독 | Manager Insights | Resolution Notes Review | Manager 검토 워크플로우 | Role-Based 검토 | 미공개 | 미공개 | 미공개 | [^1] [^4] [^7] |
| **자동 스코어링** | Extended Thinking 기반 | Evals 프레임워크 | 자체 평가 모델 | Atlas Engine 자기 반성 | 미공개 | Orchestrator 정책 대비 평가 | ASOR 성과 추적 | 미공개 | 미공개 | 미공개 | 미공개 | [^1] [^2] [^4] [^7] |
| **에이전트 모니터링** | CLI 로그 (Claude Code) | Codex 실행 로그 | 미공개 | Command Center (3.0) | Manager Insights Dashboard | Orchestrator 대시보드 | Agent Registry Dashboard | Joule Admin Center | 미공개 | 미공개 | 태스크 큐 대시보드 | [^1] [^4] [^6] [^7] [^11] |

### 패턴 분류

#### 패턴 A: 학술 벤치마크 경쟁 (Academic Benchmark Race)

**설명**: 공개 학술 벤치마크에서의 성능 순위를 핵심 마케팅/차별화 수단으로 사용하는 접근법. 주로 LLM 네이티브 벤더(Anthropic, OpenAI, Google)가 채택한다.

**예시 제품**: [[claude/claude|Claude]], [[openai/openai|OpenAI]], [[google-gemini/google-gemini|Google Gemini]]

**주요 벤치마크**:
- **SWE-bench Verified**: 실제 GitHub 이슈를 해결하는 소프트웨어 엔지니어링 벤치마크. 코딩 에이전트의 사실상 표준. Claude Sonnet 5(82.1%) > GPT-5.2(80.0%) > Gemini(76.8%) [^1] [^2] [^3] [^12]
- **MMLU / MMLU-Pro**: 다분야 지식 및 추론 능력 평가
- **HumanEval**: 코드 생성 정확도 평가
- **HLE (Humanity's Last Exam)**: Google Gemini가 SOTA를 달성한 초고난도 종합 평가 [^3]
- **BrowseComp**: 브라우저 기반 정보 검색 능력 평가

**장점**: 객관적, 재현 가능, 벤더 간 직접 비교 가능
**단점**: 실제 비즈니스 시나리오와의 상관관계 미검증, 벤치마크 과적합(overfitting) 우려, 에이전트 고유 역량(도구 사용, 멀티스텝 추론, HITL 핸드오프) 평가 부족

#### 패턴 B: 에이전트 태스크 벤치마크 (Agent Task Benchmarks)

**설명**: 에이전트가 실제 환경(브라우저, 데스크톱, API)에서 태스크를 완수하는 능력을 평가하는 벤치마크. 학술 벤치마크보다 실제 사용 시나리오에 가깝다.

**예시 제품**: [[openai/openai|OpenAI]] CUA (WebVoyager 87%, WebArena 58.1%, OSWorld 38.1%) [^2]

**주요 벤치마크**:
- **WebVoyager**: 실제 웹사이트에서 태스크를 수행하는 브라우저 에이전트 벤치마크 [^14]
- **WebArena**: 자체 호스팅된 웹 환경에서의 태스크 완수율 평가 [^15]
- **OSWorld**: 운영체제 수준의 데스크톱 태스크 수행 능력 평가 [^16]
- **GAIA**: 범용 AI 어시스턴트의 태스크 완수 능력을 평가하는 벤치마크 [^13]
- **TAU-bench**: 도구 사용 에이전트의 성능을 평가하는 벤치마크

**장점**: 실제 에이전트 사용 시나리오에 가까움, 도구 사용/브라우저 조작 능력을 직접 측정
**단점**: 벤치마크 환경이 통제되어 있어 실제 웹의 복잡성을 완전히 반영하지 못함, 엔터프라이즈 비즈니스 프로세스 시나리오 부재

#### 패턴 C: 내부 비즈니스 KPI 기반 평가 (Internal Business KPI Evaluation)

**설명**: 학술 벤치마크 대신 실제 비즈니스 성과 지표(ROI, 업무 시간 절감, 해결률, 사용자 만족도)를 평가 기준으로 사용하는 접근법. 엔터프라이즈 AI 벤더와 한국 벤더가 주로 채택한다.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] (응답 관련성 2배, 정확도 33% 개선), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] (일일 5시간 20분 절감), [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] (연 100억 원+ 절감)

**주요 KPI**:
- **업무 시간 절감**: 삼성SDS(일일 5시간 20분, 67% 감소), LG CNS(생산성 10% 향상) [^9] [^10]
- **비용 절감**: LG CNS(LG디스플레이 연 100억 원+), SAP(Cash Management Agent 수작업 70% 절감) [^10] [^8]
- **정확도/관련성**: Salesforce(Atlas Engine 정확도 33% 개선, 관련성 2배) [^4]
- **채택률/사용량**: 삼성SDS(20만 명 사용자, 절반 실업무 활용) [^9]
- **도입 기업 수**: 더존 ONE AI(5,800+ 기업) [출처 필요]

**장점**: 고객이 이해하기 쉬운 비즈니스 언어로 성과 입증, 실제 프로덕션 환경 데이터
**단점**: 벤더별 측정 기준이 달라 직접 비교 불가, 통제된 환경이 아니므로 재현성 부족, 마케팅 편향 가능성

#### 패턴 D: 내장형 테스트/모니터링 플랫폼 (Built-in Testing & Monitoring)

**설명**: 에이전트 빌더 또는 운영 플랫폼 내에 테스트와 모니터링을 내장하여, 배포 전후의 품질을 지속적으로 관리하는 접근법.

**예시 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] (Testing Center + Command Center), [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] (Testing Center + Orchestrator 대시보드), [[workday-assistant/workday-assistant|Workday Assistant]] (ASOR 성과 추적)

**특징**:
- Salesforce Testing Center: 실제 사용자 인터랙션을 시뮬레이션하여 에이전트 응답 품질과 지연 시간을 배포 전 검증 [^4]
- Salesforce Command Center (3.0): 에이전트 상태, 성능 지표, 비즈니스 성과를 단일 대시보드에서 실시간 모니터링 [^4]
- ServiceNow Orchestrator: 에이전트가 수행하는 모든 단계를 정책 대비 실시간 평가 [^6]
- Workday ASOR: 에이전트별 실행 로그, 완료율, 비용, 사용자 피드백을 인간 직원의 성과 관리와 동일한 방식으로 추적 [^7]
- OpenAI Evals: 오픈소스 평가 프레임워크로, 커스텀 평가 기준 정의 및 자동 스코어링 지원 [^2] [^17]

---

## Key Findings

1. **에이전트 평가의 "3세계" 단절**: LLM 네이티브 벤더의 학술 벤치마크 세계(SWE-bench, MMLU), 에이전트 태스크 벤치마크 세계(WebVoyager, WebArena), 엔터프라이즈 비즈니스 KPI 세계가 서로 완전히 단절되어 있다. [^1] [^2] [^4] SWE-bench에서 1등인 모델이 반드시 최고의 ERP 에이전트를 만드는 것이 아니며, 브라우저 벤치마크 성능이 엔터프라이즈 워크플로우 자동화 품질과 어떤 상관관계를 가지는지 아무도 검증하지 않았다.

2. **브라우저 에이전트 벤치마크에서 OpenAI CUA의 독주**: 조사 대상 중 브라우저 에이전트 태스크 벤치마크 수치를 공개한 것은 [[openai/openai|OpenAI]]의 CUA(WebVoyager 87%, WebArena 58.1%, OSWorld 38.1%)가 유일하다. [^2] [[claude/claude|Claude]] in Chrome과 [[google-gemini/google-gemini|Google Gemini]] Project Mariner는 브라우저 에이전트를 제공하지만 비교 가능한 벤치마크 수치를 공개하지 않았다. [^1] [^3] 이는 브라우저 에이전트 평가가 아직 표준화되지 않았음을 의미하며, OSWorld의 38.1%라는 수치는 데스크톱 수준의 자율 에이전트가 아직 초기 단계임을 보여준다.

3. **Salesforce Testing Center가 엔터프라이즈 에이전트 테스트의 참조 모델**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]의 Testing Center는 (1) 배포 전 에이전트 시뮬레이션, (2) 응답 품질 자동 스코어링, (3) 지연 시간 측정, (4) Command Center를 통한 프로덕션 모니터링까지 에이전트 라이프사이클 전체를 아우르는 가장 포괄적인 테스트 체계를 구축했다. [^4] Test Drive 모드를 통한 배포 전 인터랙티브 검증도 차별화 요소이다. ServiceNow 역시 Testing Center를 보유하나 Salesforce만큼의 상세 정보를 공개하지 않았다. [^6]

4. **Workday ASOR의 "에이전트 성과 관리" 패러다임이 평가 체계를 재정의**: [[workday-assistant/workday-assistant|Workday Assistant]]의 ASOR(Agent System of Record)는 AI 에이전트를 인간 직원과 동일한 방식으로 성과 관리하는 개념을 도입했다. [^7] 에이전트의 채용(등록) -> 온보딩(권한 설정) -> 운영(태스크 수행) -> 성과 추적(완료율, 비용, 피드백) -> 최적화/퇴직의 라이프사이클을 관리하는 이 접근법은 기존의 "벤치마크 점수" 중심 평가를 넘어 **지속적 성과 관리** 패러다임으로의 전환을 의미한다. 에이전트의 "해고"(비활성화) 결정까지 데이터 기반으로 내릴 수 있는 체계이다.

5. **한국 벤더의 평가 데이터가 "결과" 중심이고 "과정" 부재**: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]](일일 5시간 20분 절감, 67% 감소)와 [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]](LG디스플레이 생산성 10% 향상, 연 100억 원+ 절감, 채용 26% 개선) 모두 인상적인 ROI 수치를 공개하지만, 에이전트 자체의 기술적 성능 — 정확도, 할루시네이션 비율, 태스크 성공률, 도구 호출 정확도 — 에 대한 벤치마크 데이터는 전혀 공개하지 않았다. [^9] [^10] 고객 입장에서 "왜 이 에이전트가 좋은가?"에 대한 기술적 근거가 부족하며, 이는 한국 시장 전체의 에이전트 품질 투명성 문제이다.

6. **Manus AI의 Self-Correction Loop이 자동 평가의 새로운 패턴을 제시**: [[manus-ai/manus-ai|Manus AI]]의 에이전트는 작업 중 오류를 자동 감지하고 수정을 시도하는 Self-Correction Loop을 내장하고 있으며, 이 전체 과정이 사용자에게 투명하게 시각화된다. [^11] 이는 단순한 오류 처리를 넘어 "에이전트가 자신의 출력을 평가하고 개선하는" 자기 평가(self-evaluation) 패턴이며, Salesforce Atlas Engine의 자기 반성(self-reflection) 메커니즘과 유사한 방향성을 보인다. [^4] 에이전트 내부에 평가 루프를 내장하는 이 접근법은 외부 벤치마크에 의존하지 않고 실시간으로 품질을 개선하는 방법론으로 발전할 가능성이 있다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|

---

## References

### Vault
- [^1]: [[AI Agent Products/claude/claude|Claude (Anthropic)]] — SWE-bench 82.1%(Sonnet 5)/80.9%(Opus 4.5), Extended Thinking 추론 투명성
- [^2]: [[AI Agent Products/openai/openai|OpenAI ChatGPT]] — SWE-bench 80.0%(GPT-5.2), CUA WebVoyager 87%/WebArena 58.1%/OSWorld 38.1%, Evals 프레임워크
- [^3]: [[AI Agent Products/google-gemini/google-gemini|Google Gemini]] — SWE-bench 76.8%, HLE/BrowseComp SOTA, Deep Research 다단계 검증
- [^4]: [[AI Agent Products/salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Testing Center, Test Drive, Command Center, Atlas 정확도 33% 개선
- [^5]: [[AI Agent Products/microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] — Copilot Studio 테스트, Manager Insights
- [^6]: [[AI Agent Products/servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] — Testing Center, Orchestrator 대시보드, 정책 대비 실시간 평가
- [^7]: [[AI Agent Products/workday-assistant/workday-assistant|Workday Assistant]] — ASOR 에이전트 성과 관리 라이프사이클
- [^8]: [[AI Agent Products/sap-joule/sap-joule|SAP Joule]] — 2400+ 스킬, Cash Management Agent 수작업 70% 절감
- [^9]: [[AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] — 20만 명 사용, 일일 5시간 20분 절감
- [^10]: [[AI Agent Products/lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] — LG디스플레이 연 100억 원+ 절감, 채용 26% 개선
- [^11]: [[AI Agent Products/manus-ai/manus-ai|Manus AI]] — Self-Correction Loop, Glass Box 투명성

### External
- [^12]: [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://www.swebench.com/) — 코딩 에이전트 표준 벤치마크
- [^13]: [GAIA: General AI Assistants Benchmark](https://arxiv.org/abs/2311.12983) — 범용 AI 어시스턴트 벤치마크
- [^14]: [WebVoyager: Building an End-to-End Web Agent](https://arxiv.org/abs/2401.13919) — 브라우저 에이전트 벤치마크
- [^15]: [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://webarena.dev/) — 자체 호스팅 웹 환경 벤치마크
- [^16]: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://os-world.github.io/) — 데스크톱 에이전트 벤치마크
- [^17]: [OpenAI Evals GitHub Repository](https://github.com/openai/evals) — 오픈소스 평가 프레임워크
- [^18]: [Salesforce: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/) — Atlas Engine 자기 반성 메커니즘
- [^19]: [Workday: Agent System of Record](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html) — ASOR 에이전트 성과 관리

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
