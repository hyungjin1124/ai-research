---
type: insight-synthesis
topic_id: agent-frameworks-landscape
topic_name: 오픈소스 에이전트 프레임워크 랜드스케이프
category: open-source
tags:
- insight
- open-source
- agent-framework
- LangChain
- LangGraph
- CrewAI
- AutoGen
- Semantic-Kernel
status: done
confidence: high
last_updated: '2026-02-12'
source_products:
- databricks-mosaic-ai
- glean
- openai
- claude
- microsoft-copilot
- google-gemini
- salesforce-agentforce
- samsung-sds-fabrix
- manus-ai
source_files:
- '[[databricks-mosaic-ai]]'
- '[[glean]]'
- '[[openai]]'
- '[[claude]]'
- '[[microsoft-copilot]]'
- '[[google-gemini]]'
- '[[salesforce-agentforce]]'
- '[[samsung-sds-fabrix]]'
- '[[manus-ai]]'
- '[[2026/02/2026-02-12]]'
relevant_roles:
- architecture_agent
- backend_agent
auto_update:
  enabled: true
  feeds:
  - https://github.com/crewAIInc/crewAI/releases.atom
  keywords:
  - AI agent framework comparison
  - CrewAI vs AutoGen vs LangGraph
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 오픈소스 에이전트 프레임워크 랜드스케이프

## TL;DR

- **주요 오픈소스 에이전트 프레임워크는 아키텍처 패러다임에 따라 3가지로 분류된다**: (1) 체인/파이프라인 기반(LangChain), (2) 그래프 기반 상태 머신(LangGraph), (3) 멀티 에이전트 대화형(CrewAI, AutoGen, OpenAI Agents SDK). 각 패러다임은 해결하려는 복잡도 수준과 에이전트 자율성 정도가 다르다
- **LangChain/LangGraph가 엔터프라이즈 플랫폼의 사실상 표준 통합 대상이다**: Databricks Mosaic AI가 `databricks-langchain` 패키지로 LangChain/LangGraph를 공식 지원하고, Glean이 LangChain Agent Protocol을 Agents API의 기반으로 채택하는 등, 엔터프라이즈 플랫폼들이 LangChain 생태계를 우선 통합 대상으로 선택하고 있다
- **프레임워크 경쟁은 "오케스트레이션 레이어"에서 "프로토콜 레이어"로 이동 중이다**: MCP(Anthropic), A2A(Google), LangChain Agent Protocol이 에이전트 상호운용성의 표준 경쟁을 벌이면서, 개별 프레임워크의 오케스트레이션 로직보다 프로토콜 호환성이 프레임워크 선택의 핵심 기준으로 부상하고 있다
- **엔터프라이즈 벤더들은 OSS 프레임워크를 "직접 사용"하기보다 "호환 레이어"로 활용한다**: Microsoft(Semantic Kernel), Salesforce(Atlas Engine), ServiceNow(자체 3계층 아키텍처)는 독자 오케스트레이션 엔진을 유지하면서 OSS 프레임워크와의 호환성만 확보하는 전략을 취한다
- **LangGraph 기반 그래프 오케스트레이션 + MCP 프로토콜 조합이 최적 출발점이다**: 복잡한 비즈니스 워크플로우의 상태 관리와 조건부 분기가 필수적인 엔터프라이즈 에이전트 시나리오에서, LangGraph의 그래프 기반 상태 머신이 가장 적합하며 MCP 생태계와의 즉시 호환이 가능하다
- **오픈소스 LLM의 성능 역전으로 프레임워크의 "모델 독립성"이 핵심 요건으로 부상하고 있다**: GLM-5(744B MoE, MIT, AA-Omniscience 1위)를 비롯한 오픈소스 모델이 프로프라이어터리 모델을 벤치마크에서 추월하면서, 에이전트 프레임워크가 다양한 LLM 백엔드를 유연하게 전환할 수 있는 능력이 기술 스택 선정의 새로운 축이 되고 있다 [^7]

---

## Context

엔터프라이즈 AI 에이전트 프로덕트 개발에 있어, 에이전트의 추론-계획-실행 루프를 구현하는 오케스트레이션 프레임워크의 선택은 프로덕트의 개발 속도, 확장성, 유지보수성을 결정짓는 핵심 기술 의사결정이다. 2025~2026년 현재 LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel, OpenAI Agents SDK 등 다수의 오픈소스 에이전트 프레임워크가 경쟁하면서, 각기 다른 아키텍처 철학과 성숙도를 보이고 있다.

특히 분석 대상 엔터프라이즈 제품들이 이들 프레임워크를 어떻게 채택하거나 참조하고 있는지를 교차 분석하면, 시장이 실제로 검증한 프레임워크와 아키텍처 패턴을 식별할 수 있으며, 이는 기술 스택 선정에 직접적 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| 프레임워크 | 아키텍처 패턴 | 주요 활용 제품 | 프로토콜 지원 | 커뮤니티 규모 (GitHub Stars) | 성숙도 | 적합 사용 사례 |
|-----------|------------|-------------|------------|--------------------------|--------|-------------|
| LangChain | 체인/파이프라인, 모듈 조합 | Databricks Mosaic AI, Glean | MCP, LangChain Agent Protocol | ~100K+ | 높음 (GA, 활발한 업데이트) | RAG, 도구 호출 체인, 프로토타이핑 |
| LangGraph | 그래프 기반 상태 머신 | Databricks Mosaic AI | MCP, LangChain Agent Protocol | ~10K+ | 중간 (GA, 빠른 성장) | 복잡한 멀티스텝 워크플로우, 조건부 분기, HITL |
| CrewAI | 멀티 에이전트 역할 기반 | (직접 채택 제품 미확인) | MCP 지원 | ~25K+ | 중간 (GA) | 역할 분담형 멀티 에이전트 협업 태스크 |
| AutoGen (Microsoft) | 멀티 에이전트 대화형 | (MS 생태계 내부 참조) | MCP 지원 | ~40K+ | 중간 (v0.4 아키텍처 전환 중) | 에이전트 간 토론/협상, 코드 생성 |
| Semantic Kernel (Microsoft) | 플러그인 기반 오케스트레이션 | Microsoft Copilot (간접) | MCP 지원 | ~25K+ | 높음 (GA, 엔터프라이즈 안정) | C#/.NET 기반 엔터프라이즈 통합, Copilot 확장 |
| OpenAI Agents SDK | 경량 에이전트 루프 | OpenAI (Responses API) | MCP 지원 | ~20K+ | 초기 (2025-03 출시) | OpenAI 모델 기반 에이전트 빠른 구축 |

### 패턴 분류

#### 패턴 A: 체인/파이프라인 기반 (Chain-based Orchestration)

**대표 프레임워크**: LangChain

LLM 호출, 도구 호출, 데이터 검색 등 개별 단계를 선형적 또는 분기적 체인으로 조합하는 방식이다. LangChain이 이 패턴의 대표 주자로, 풍부한 통합(벡터 DB, 도구, LLM 프로바이더)과 대규모 커뮤니티가 강점이다. Databricks Mosaic AI가 `databricks-langchain` 패키지를 통해 Unity Catalog 도구와 LangChain을 직접 연결하고, Glean이 LangChain Agent Protocol을 Agents API의 기반 프로토콜로 채택하는 등 엔터프라이즈 검증이 이루어지고 있다.

- **장점**: 가장 넓은 통합 생태계, 풍부한 문서/튜토리얼, 빠른 프로토타이핑, 엔터프라이즈 플랫폼의 공식 지원
- **단점**: 복잡한 상태 관리에 한계, 멀티 에이전트 시나리오에서 추상화 부족, 버전 간 호환성 변동이 잦음

#### 패턴 B: 그래프 기반 상태 머신 (Graph-based State Machine)

**대표 프레임워크**: LangGraph

에이전트의 실행 흐름을 방향성 그래프(DAG 또는 순환 그래프)로 정의하고, 각 노드에서 상태를 명시적으로 관리하는 방식이다. LangGraph는 LangChain 위에 구축되어 LangChain의 통합 생태계를 그대로 활용하면서, 조건부 분기, 루프, Human-in-the-Loop 승인 포인트, 체크포인팅을 네이티브로 지원한다. Databricks가 LangChain과 함께 LangGraph를 공식 지원 프레임워크로 명시하여, 엔터프라이즈 에이전트의 복잡한 멀티스텝 플로우 구현에 적합함을 인정하고 있다.

- **장점**: 명시적 상태 관리로 디버깅/감사 용이, 조건부 분기와 루프의 자연스러운 표현, 체크포인팅을 통한 장기 실행 에이전트 지원, Human-in-the-Loop 네이티브 통합
- **단점**: LangChain 대비 학습 곡선이 높음, 단순 태스크에는 과도한 추상화, 아직 LangChain 대비 커뮤니티 규모가 작음

#### 패턴 C: 멀티 에이전트 대화형 (Multi-Agent Conversational)

**대표 프레임워크**: CrewAI, AutoGen, OpenAI Agents SDK

복수의 전문화된 에이전트가 역할을 분담하여 대화 또는 메시지 교환을 통해 태스크를 협업 수행하는 방식이다. CrewAI는 "크루(crew)"와 "역할(role)" 메타포로 에이전트 팀을 직관적으로 구성할 수 있고, AutoGen(Microsoft)은 에이전트 간 자유 형식 대화를 통한 협상/토론 패턴에 강점이 있다. OpenAI Agents SDK는 2025년 3월 출시된 경량 프레임워크로, 핸드오프(handoff) 패턴을 통한 에이전트 간 작업 위임을 핵심으로 한다.

Manus AI의 Planner Agent + 전문 에이전트(Browser, Code, File) 아키텍처나, Salesforce Atlas Engine의 계획-행동-관찰 루프, Microsoft Copilot의 멀티 에이전트 오케스트레이션이 이 패턴의 상용 구현 사례에 해당한다.

- **장점**: 복잡한 태스크를 역할 분담으로 분해, 에이전트별 독립적 최적화 가능, 인간 조직 구조와 유사한 직관적 모델링
- **단점**: 에이전트 간 통신 오버헤드, 조율 실패(에이전트 간 모순, 무한 루프) 가능성, 디버깅 난이도 증가

#### 오픈소스 LLM 백본 모델 동향

에이전트 프레임워크의 선택과 별개로, 프레임워크 위에서 동작하는 **LLM 백본 모델**의 오픈소스 생태계가 급격히 성숙하고 있다. 2026년 2월 Zhipu AI(Z.ai)가 공개한 GLM-5(744B MoE, 40B active, MIT 라이선스)는 AA-Omniscience Index에서 업계 1위 지식 신뢰도를 기록하고, BrowseComp 오픈소스 1위(75.9), Humanity's Last Exam에서 Claude Opus 4.5를 능가(50.4점)하여, 오픈소스 모델이 프로프라이어터리 모델과 동등하거나 우월한 성능을 달성할 수 있음을 실증했다 [^7]. 가격은 입력 $0.80-1.00/M, 출력 $2.56-3.20/M으로 GPT-5.2 대비 상당한 비용 우위를 보인다. DeepSeek R1, Alibaba Qwen 등과 함께 오픈소스 LLM 선택지가 확대됨에 따라, 에이전트 프레임워크 선택 시 "어떤 프레임워크가 다양한 오픈소스 LLM을 유연하게 백엔드로 지원하는가"가 추가적인 기술 의사결정 축이 되고 있다.
<!-- Deep Dive: 2026-02-12 | GLM-5 출시 | 오픈소스 LLM 백본 모델 동향 하위 섹션 추가 (원래 '오픈소스 모델 비교 매트릭스' 갱신 범위이나 해당 섹션 미존재로 신규 생성) -->

#### 패턴 D: 플러그인 기반 엔터프라이즈 오케스트레이션 (Plugin-based Enterprise Orchestration)

**대표 프레임워크**: Semantic Kernel (Microsoft)

엔터프라이즈 기존 코드 자산과 AI를 연결하는 "플러그인" 중심 아키텍처로, C#/.NET/Java/Python 환경에서 기존 비즈니스 로직을 AI 에이전트의 도구로 바로 노출할 수 있다. Microsoft Copilot의 내부 오케스트레이션 레이어가 Semantic Kernel을 기반으로 하며, Azure AI 서비스와의 깊은 통합이 특징이다.

- **장점**: .NET 엔터프라이즈 환경에 최적, Microsoft 에코시스템과 네이티브 통합, 기존 비즈니스 로직 재사용 용이, 안정적 GA 상태
- **단점**: Python 중심 AI 생태계 대비 커뮤니티 제한, Microsoft 스택 외 환경에서 활용도 저하, LangChain 대비 통합 커넥터 수 적음

---

## Key Findings

1. **엔터프라이즈 플랫폼들은 OSS 프레임워크를 "오케스트레이션 호환 레이어"로 활용하지 "핵심 엔진"으로 사용하지 않는다**: Databricks가 LangChain/LangGraph를 공식 지원하지만 자체 Agent Framework를 별도 구축하고, Glean이 LangChain Agent Protocol을 채택하지만 자체 Agentic Engine 2를 핵심 추론 엔진으로 운영하며, Microsoft가 Semantic Kernel을 기반으로 하되 Copilot Orchestrator라는 독자 레이어를 추가하는 패턴은 공통적이다. OSS 프레임워크는 진입점이자 호환성 레이어이며, 핵심 비즈니스 로직은 자체 구축하는 것이 업계 표준이다 -- *Source*: [[databricks-mosaic-ai]], [[glean]], [[microsoft-copilot]]

2. **LangChain Agent Protocol이 에이전트 API의 사실상 표준으로 부상하고 있다**: Glean이 자사 Agents API의 기반 프로토콜로 LangChain Agent Protocol을 채택한 것은, 개별 프레임워크의 내부 오케스트레이션 방식보다 에이전트를 외부에 노출하는 API 인터페이스의 표준화가 더 중요해지고 있음을 시사한다. 이는 MCP가 도구 연결을, Agent Protocol이 에이전트 호출을 각각 표준화하는 "이중 프로토콜 스택"의 형성을 의미한다 -- *Source*: [[glean]]

3. **프레임워크 선택의 핵심 기준이 "기능"에서 "프로토콜 호환성"으로 전환되고 있다**: MCP를 Anthropic(Claude), OpenAI, Google, Microsoft, Salesforce, Snowflake, Glean, 삼성SDS가 모두 채택/지원하는 상황에서, 에이전트 프레임워크가 MCP 클라이언트/서버를 얼마나 자연스럽게 지원하는지가 프레임워크 선택의 결정적 기준이 되고 있다. LangChain/LangGraph, CrewAI, AutoGen, OpenAI Agents SDK 모두 MCP 지원을 추가한 것은 이 추세의 반영이다 -- *Source*: [[claude]], [[openai]], [[google-gemini]], [[samsung-sds-fabrix]]

4. **그래프 기반 상태 머신(LangGraph)이 엔터프라이즈 에이전트의 아키텍처 패턴으로 수렴하고 있다**: Salesforce Atlas Engine의 계획-행동-관찰 루프, Manus AI의 Planner Agent + 실행 트리, ServiceNow의 Skills-Agents-Orchestrator 3계층, Microsoft Copilot의 멀티 에이전트 오케스트레이션 모두 본질적으로 상태 기반 그래프 실행 모델을 따른다. 이는 복잡한 비즈니스 워크플로우가 조건부 분기, 루프, 체크포인팅, Human-in-the-Loop를 필수적으로 요구하기 때문이며, LangGraph가 이를 가장 명시적으로 프레임워크 수준에서 지원한다 -- *Source*: [[salesforce-agentforce]], [[manus-ai]], [[servicenow-now-assist]], [[microsoft-copilot]]

5. **멀티 에이전트 오케스트레이션은 OSS 프레임워크보다 상용 플랫폼이 앞서 있다**: Microsoft Copilot의 멀티 에이전트 오케스트레이션(GA), Manus AI의 Planner + 전문 에이전트 병렬 처리, ServiceNow의 AI Agent Orchestrator가 프로덕션 수준의 멀티 에이전트 협업을 구현한 반면, OSS 프레임워크(CrewAI, AutoGen)의 멀티 에이전트 기능은 아직 프로덕션 안정성 면에서 검증이 부족하다. 특히 AutoGen은 v0.4에서 대규모 아키텍처 전환을 진행 중이어서 안정성 리스크가 있다 -- *Source*: [[microsoft-copilot]], [[manus-ai]], [[servicenow-now-assist]]

6. **한국 시장의 엔터프라이즈 벤더(삼성SDS, LG CNS)는 OSS 프레임워크 직접 채택보다 프로토콜(MCP/A2A) 수준의 표준화를 우선시한다**: 삼성SDS FabriX가 LangChain이나 LangGraph 같은 특정 OSS 프레임워크를 공식 채택하기보다, MCP와 A2A 프로토콜 지원을 통해 기존 기간계 시스템과의 무수정 연동을 강조하는 것은, 한국 엔터프라이즈 시장에서 프레임워크보다 프로토콜이 더 중요한 기술 의사결정 축임을 보여준다 -- *Source*: [[samsung-sds-fabrix]]

7. **오픈소스 LLM의 프로프라이어터리 모델 추월이 에이전트 프레임워크의 "모델 독립성"을 핵심 요건으로 격상시킨다**: 2026년 2월 GLM-5(744B MoE, MIT 라이선스)가 AA-Omniscience Index 업계 1위, BrowseComp 오픈소스 1위를 달성하고 가격이 입력 $0.80-1.00/M으로 프로프라이어터리 모델 대비 상당한 비용 우위를 보이면서, 에이전트 프레임워크가 특정 LLM 프로바이더에 락인되지 않고 다양한 오픈소스 모델을 백엔드로 유연하게 전환할 수 있는 능력이 기술 의사결정의 새로운 기준이 되고 있다. LangChain/LangGraph와 CrewAI가 다중 LLM 프로바이더를 기본 지원하는 반면, OpenAI Agents SDK는 OpenAI 모델 중심으로 설계되어 이 측면에서 제약이 있다 [^7] -- *Source*: [[2026/02/2026-02-12|2026-02-12 다이제스트]]
<!-- Deep Dive: 2026-02-12 | GLM-5 출시 | Key Finding 7 추가: 오픈소스 LLM이 프레임워크 선택에 미치는 영향 -->

---

---

## 소스 제품 매핑

| 제품 | OSS 프레임워크 관련성 | 참조 포인트 |
|------|---------------------|-----------|
| [[databricks-mosaic-ai]] | LangChain/LangGraph 공식 지원 (`databricks-langchain` 패키지) | Agent Framework와 OSS 프레임워크 호환 패턴 |
| [[glean]] | LangChain Agent Protocol 기반 Agents API | 에이전트 API 표준화 사례 |
| [[openai]] | OpenAI Agents SDK (OSS), MCP 채택 | 경량 에이전트 프레임워크, Function Calling 패턴 |
| [[claude]] | MCP 창안/주도, Agentic Loop 아키텍처 | 프로토콜 중심 에이전트 아키텍처 |
| [[microsoft-copilot]] | Semantic Kernel (간접), 멀티 에이전트 오케스트레이션 | 엔터프라이즈 오케스트레이션 패턴 |
| [[google-gemini]] | A2A/A2UI 프로토콜, MCP 지원 | 프로토콜 경쟁 구도 |
| [[salesforce-agentforce]] | Atlas Engine (독자 구축), MCP 3.0 내장 | 독자 오케스트레이션 + 프로토콜 호환 전략 |
| [[samsung-sds-fabrix]] | MCP + A2A 프로토콜 우선 전략 | 한국 엔터프라이즈 프로토콜 채택 사례 |
| [[manus-ai]] | 멀티 에이전트 오케스트레이션 (Planner + 전문 에이전트) | 상용 멀티 에이전트 아키텍처 참조 |

---

## Source References

### 제품 프로필
- [[databricks-mosaic-ai]] -- Agent Framework의 LangChain/LangGraph 공식 지원, `databricks-langchain` 패키지, Unity Catalog 도구 연동
- [[glean]] -- LangChain Agent Protocol 기반 Agents API, 호스팅 MCP 서버, Agentic Engine 2
- [[openai]] -- Responses API, Function Calling, MCP 채택, Agents SDK 오픈소스
- [[claude]] -- MCP 창안/주도, Constitutional AI, Agentic Loop (Claude Code/Cowork)
- [[microsoft-copilot]] -- Copilot Studio, 멀티 에이전트 오케스트레이션, Semantic Kernel 간접 활용, MCP 네이티브 지원
- [[google-gemini]] -- MCP + A2A + A2UI 프로토콜 지원, Interactions API
- [[salesforce-agentforce]] -- Atlas Reasoning Engine, Agent Builder, MuleSoft Agent Fabric, MCP 3.0 내장
- [[samsung-sds-fabrix]] -- FabriX 생성형 AI 플랫폼, MCP/A2A 프로토콜 적용, 기간계 무수정 연동
- [[manus-ai]] -- Planner Agent + 전문 에이전트 멀티 에이전트 오케스트레이션, Glass Box 투명성
- [[servicenow-now-assist]] -- Skills-Agents-Orchestrator 3계층 아키텍처, AI Agent Studio

### UI 리서치
- [[MCP-UI 프로토콜 분석]] -- MCP-UI 핵심 개념, 프레임워크와 UI 프로토콜의 관계
- [[A2UI 프로토콜 및 MCP-UI 비교]] -- A2UI 선언형 모델, 프레임워크 수준의 UI 프로토콜 경쟁

### External
- [^7]: [Z.ai's open source GLM-5 achieves record low hallucination rate](https://venturebeat.com/technology/z-ais-open-source-glm-5-achieves-record-low-hallucination-rate-and-leverages) (2026-02-11) — GLM-5 744B MoE 모델 출시, AA-Omniscience 1위, BrowseComp 오픈소스 1위, 가격 정보

### 외부 참고 자료
- [LangChain 공식 문서](https://python.langchain.com/)
- [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
- [CrewAI 공식 사이트](https://www.crewai.com/)
- [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen)
- [Microsoft Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [OpenAI Agents SDK GitHub](https://github.com/openai/openai-agents-python)
- [LangChain Agent Protocol Specification](https://langchain-ai.github.io/agent-protocol/)
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)

---

## Recent Updates

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-11 | [The two patterns by which agents connect sandboxes](https://blog.langchain.com/the-two-patterns-by-which-agents-connect-sandboxes/) · [[2026/02/2026-02-11\|다이제스트]] | LangChain 에이전트-샌드박스 연결 2가지 패턴 분석. 에이전트 내부 실행 vs 원격 도구 방식 | #open-source |
| 2026-02-12 | [Z.ai GLM-5: 744B 오픈소스 모델](https://venturebeat.com/technology/z-ais-open-source-glm-5-achieves-record-low-hallucination-rate-and-leverages) · [[2026/02/2026-02-12\|다이제스트]] | ✅ GLM-5(744B MoE, MIT 라이선스) 출시. AA-Omniscience 1위, BrowseComp 오픈소스 1위. Huawei 칩 훈련, 가격 $0.80-1.00/M 입력 | #open-source |

---

*Last synthesized: 2026-02-12 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
