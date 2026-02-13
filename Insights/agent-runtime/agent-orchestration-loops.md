---
type: insight-synthesis
topic_id: agent-orchestration-loops
topic_name: 에이전트 오케스트레이션 루프 패턴 비교
category: agent-runtime
tags:
- insight
- agent-runtime
- agent-loop
- orchestration
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- salesforce-agentforce
- workday-assistant
- claude
- openai
- servicenow-now-assist
- databricks-mosaic-ai
- manus-ai
source_files:
- '[[salesforce-agentforce]]'
- '[[workday-assistant]]'
- '[[claude]]'
- '[[openai]]'
- '[[servicenow-now-assist]]'
- '[[databricks-mosaic-ai]]'
- '[[manus-ai]]'
relevant_roles:
- architecture_agent
- backend_agent
- qa_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - orchestration
  - agent loop
  - Plan-Act-Observe
  - ReAct loop
  - error recovery
  - multi-agent orchestration
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 오케스트레이션 루프 패턴 비교

## TL;DR

- 에이전트 오케스트레이션 루프는 크게 **4가지 패턴**으로 분류된다: (1) Plan-Act-Observe 반복 루프, (2) 계층적 Skills-Agents-Orchestrator 구조, (3) 멀티 에이전트 분산 오케스트레이션, (4) 비동기 샌드박스 실행 루프
- **Plan-Act-Observe 루프**가 사실상 업계 표준으로 수렴하고 있으며, Salesforce Atlas, Claude Agentic Loop, OpenAI CUA 모두 이 패턴의 변형을 채택한다. 차이는 루프 내부의 self-reflection 깊이와 error recovery 전략에서 발생한다
- **에러 복구 패턴**이 제품 성숙도의 핵심 지표로 부상하고 있다. Manus AI의 Self-Correction Loop 시각화와 Salesforce Atlas의 self-reflection 메커니즘이 대표적이며, 단순 재시도를 넘어 원인 분석 후 대안 전략을 시도하는 "적응형 복구"가 차세대 기준이 되고 있다
- **거버넌스 통합형 오케스트레이션**(ServiceNow Orchestrator, Workday ASOR)이 엔터프라이즈 시장에서 핵심 차별화 요소로 작동한다. 단순히 태스크를 수행하는 루프가 아니라, 정책 준수를 실시간으로 평가하며 실행하는 "정책 인식형 루프(Policy-Aware Loop)"가 B2B에서는 필수적이다
- 에이전트 시스템은 Plan-Act-Observe 기본 루프에 **도메인 특화 가드레일**과 **계층적 오케스트레이션**을 결합한 하이브리드 접근이 효과적이다

---

## Context

에이전트 오케스트레이션 루프는 AI 에이전트가 사용자의 목표를 달성하기 위해 추론-실행-검증을 반복하는 핵심 런타임 메커니즘이다. 이 루프의 설계가 에이전트의 신뢰성, 확장성, 그리고 엔터프라이즈 적합성을 결정한다. 2025~2026년 에이전트 시장이 급격히 성숙하면서, 단순한 LLM 프롬프트 체이닝을 넘어 체계적인 오케스트레이션 아키텍처가 경쟁의 핵심 축으로 부상하고 있다.

엔터프라이즈 AI 에이전트 프로덕트 개발에서 오케스트레이션 루프 설계는 가장 근본적인 아키텍처 결정이다. 루프의 구조가 에이전트의 자율성 수준, Human-in-the-Loop 포인트, 에러 복구 전략, 멀티 에이전트 협업 방식을 결정하기 때문이다. 산업의 다양한 패턴을 분석하고, 각 패턴의 트레이드오프를 이해하는 것이 효과적인 아키텍처 전략 수립에 필수적이다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 오케스트레이션 루프 패턴 | 핵심 특징 | 에러 복구 전략 | 멀티 에이전트 지원 | 거버넌스 통합 |
|---------|----------------------|----------|-------------|-----------------|-------------|
| Salesforce Agentforce | Plan-Act-Observe + Self-Reflection (Atlas) | Topic 기반 분류 후 Action 실행, 자기 반성 단계 내장 | Self-reflection으로 재추론 후 재실행 | Topic 간 라우팅으로 간접 지원 | Guardrails + 토픽 범위 제한 |
| Workday Assistant | ASOR 기반 라이프사이클 관리 | 에이전트를 디지털 직원으로 관리, 역할-권한-성과 추적 | Agent Gateway를 통한 에이전트 간 폴백 | MCP + A2A 프로토콜 기반 멀티 에이전트 | ASOR Registry + RBAC |
| Claude (Code/Cowork) | Goal → Plan → Tool Call → Verify → Iterate | Extended Thinking 기반 심층 추론 후 도구 호출, HITL 승인 포인트 내장 | 결과 검증 실패 시 계획 재수립 후 재시도 | 단일 에이전트 루프 (MCP로 도구 확장) | Constitutional AI 기반 안전성 가드레일 |
| OpenAI (CUA/Codex) | Screenshot → Action → Verify (CUA) / Plan → Code → Test → Submit (Codex) | 비전 기반 웹 인식 + RL 강화, 비동기 샌드박스 실행 | 막힐 경우 사용자에게 제어권 반환 (CUA), 테스트 기반 재시도 (Codex) | Codex: 독립 샌드박스 병렬 실행 | 민감 작업 시 사용자 확인 요청 |
| ServiceNow Now Assist | Skills → Agents → Orchestrator 3계층 | 정책 대비 실시간 평가, 토큰 예산 관리, 감사 로깅 | Orchestrator가 대안 Skill/Agent로 재라우팅 | Orchestrator 기반 멀티 에이전트 팀 조율 | 역할 기반 접근 제어 + Assist 토큰 예산 |
| Databricks Mosaic AI | Build → Evaluate → Deploy → Monitor 라이프사이클 | Compound AI Systems 패러다임, LangGraph 기반 에이전트 플로우 | Agent Evaluation 기반 품질 게이트, Lakeguard 샌드박스 격리 | LangGraph 기반 멀티 에이전트 그래프 구성 | Unity Catalog + Lakeguard |
| Manus AI | Planner → 서브태스크 분배 → 병렬 실행 → 결과 통합 | 멀티 에이전트 분산 오케스트레이션, 14일 비동기 실행, 20개 동시 태스크 | Self-Correction Loop (오류 감지 → 원인 분석 → 대안 시도 → 재실행) | Planner Agent + 전문 에이전트(Browser, Code, File) 분산 협업 | 제한적 (B2C 중심) |

### 패턴 분류

#### 패턴 A: Plan-Act-Observe 반복 루프 (Deliberative Loop)

가장 보편적인 오케스트레이션 패턴으로, 에이전트가 계획을 수립하고, 행동을 실행하고, 결과를 관찰한 뒤 다음 단계를 결정하는 순환 구조이다.

**대표 제품**: Salesforce Atlas, Claude Agentic Loop, OpenAI CUA

**구조**:
```
사용자 입력 → [계획 수립] → [행동 실행] → [결과 관찰] → [목표 달성?]
                  ↑                                          |
                  └──────────── No ───────────────────────────┘
```

**변형 비교**:
- **Salesforce Atlas**: Plan-Act-Observe에 Self-Reflection 단계를 추가. 각 관찰 후 "이 결과가 충분한가?"를 자체 평가하여 추론 품질을 높임. Topic Classification이 루프 진입 전에 적용되어, 잘못된 도메인 진입을 사전에 차단. 응답 관련성 2배 향상, 엔드투엔드 정확도 33% 개선이라는 수치가 self-reflection의 효과를 입증 -- *Source*: [[salesforce-agentforce]]
- **Claude Agentic Loop**: Extended Thinking을 루프의 계획 단계에 통합하여, 내부 추론 블록 생성 후 도구 호출을 수행. Human-in-the-Loop 승인 포인트가 위험 작업(파일 수정, Git 커밋 등) 전에 내장되어 있어 자율성과 안전성의 균형을 달성 -- *Source*: [[claude]]
- **OpenAI CUA**: 스크린샷 기반 비전 인식이 "관찰" 단계를 대체. 강화학습으로 훈련된 액션 생성이 "행동" 단계를 수행. 전통적 API 호출 대신 GUI 인터랙션을 통한 범용 웹 작업 수행이 차별점 -- *Source*: [[openai]]

**장점**: 직관적 구조, 검증된 패턴, 단일 에이전트로 구현이 단순함
**단점**: 순차 실행으로 인한 레이턴시, 복잡한 멀티스텝 태스크에서 계획 드리프트 발생 가능

#### 패턴 B: 계층적 Skills-Agents-Orchestrator (Hierarchical Orchestration)

단일 에이전트 루프가 아닌, 기능 단위(Skill) → 업무 단위(Agent) → 조율 단위(Orchestrator)로 이루어진 3계층 구조이다.

**대표 제품**: ServiceNow Now Assist, Workday ASOR

**구조**:
```
Orchestrator (정책·예산·감사)
    ├── Agent A (ITSM) ← [Skill 1, Skill 2, Skill 3]
    ├── Agent B (HRSD) ← [Skill 4, Skill 5]
    └── Agent C (CSM)  ← [Skill 6, Skill 7, Skill 8]
```

**변형 비교**:
- **ServiceNow**: Skills가 원자적 GenAI 작업(요약, 분류, 생성), Agents가 복수 Skill을 조합한 엔드투엔드 워크플로우, Orchestrator가 멀티 에이전트 팀 조율과 거버넌스를 담당. 특히 Assist 토큰 예산 관리와 서비스 윈도우 정책이 Orchestrator 수준에서 실시간 적용되는 점이 엔터프라이즈에 적합 -- *Source*: [[servicenow-now-assist]]
- **Workday ASOR**: 에이전트를 인간 직원과 동일한 라이프사이클(채용→온보딩→역할배정→운영→성과추적→퇴직)로 관리. Agent Registry가 모든 에이전트의 메타데이터를 중앙 관리하며, MCP + A2A 프로토콜로 자사/파트너 에이전트 간 표준화된 통신을 지원 -- *Source*: [[workday-assistant]]

**장점**: 엔터프라이즈 거버넌스에 최적화, 재사용 가능한 Skill 단위 구성, 크로스 도메인 확장 용이
**단점**: 아키텍처 복잡성 높음, 초기 구축 비용 큼, Skill 간 의존성 관리 어려움

#### 패턴 C: 멀티 에이전트 분산 오케스트레이션 (Distributed Multi-Agent)

중앙 Planner가 태스크를 분해하고, 전문화된 에이전트들이 병렬로 서브태스크를 수행하는 분산 구조이다.

**대표 제품**: Manus AI

**구조**:
```
사용자 입력 → [Planner Agent]
                ├── Browser Agent (웹 탐색) ──┐
                ├── Code Agent (코드 실행)  ──┤── [결과 통합] → 산출물
                └── File Agent (파일 생성)  ──┘
```

- **Manus AI**: Planner Agent가 복잡한 프롬프트를 수십 개 서브태스크로 분해하고, Browser/Code/File 전문 에이전트에 분배하여 병렬 처리. 클라우드 샌드박스에서 최대 14일 비동기 실행 가능. Self-Correction Loop가 각 에이전트 수준에서 독립적으로 작동하여, 개별 에이전트의 실패가 전체 워크플로우를 중단시키지 않음 -- *Source*: [[manus-ai]]

**장점**: 대규모 병렬 처리, 전문 에이전트별 최적화, 장기 비동기 작업 지원
**단점**: 에이전트 간 상태 동기화 복잡, 결과 통합 시 일관성 보장 어려움, 디버깅 난이도 높음

#### 패턴 D: 평가 주도형 라이프사이클 루프 (Evaluation-Driven Loop)

런타임 오케스트레이션보다 빌드-평가-배포-모니터링의 전체 라이프사이클에 초점을 맞추는 접근법이다.

**대표 제품**: Databricks Mosaic AI

**구조**:
```
[Build] → [Evaluate] → [Deploy] → [Monitor]
   ↑                                   |
   └──── 품질 미달 시 재구축 ─────────────┘
```

- **Databricks Mosaic AI**: Agent Evaluation이 AI Judge(LLM 기반 자동 평가) + 규칙 기반 검사 + 사람 피드백의 하이브리드 평가를 수행. Lakeguard 샌드박스가 런타임 안전성을 보장하고, MLflow 3.0이 크로스 플랫폼 관측성을 제공. 런타임 루프 자체는 LangChain/LangGraph에 위임하되, 평가와 모니터링 계층을 두텁게 구축하는 전략 -- *Source*: [[databricks-mosaic-ai]]

**장점**: 체계적 품질 보증, 프로덕션 안정성, 데이터 과학 팀에 친숙한 MLOps 패러다임
**단점**: 실시간 적응성 제한, 개발자 중심으로 비즈니스 사용자 접근성 낮음

---

## Key Findings

1. **Plan-Act-Observe의 수렴과 분화**: 7개 제품 중 5개가 Plan-Act-Observe의 변형을 핵심 루프로 채택하고 있어, 이 패턴이 사실상 업계 표준으로 수렴하고 있다. 그러나 차별화 지점은 루프 내부의 "관찰" 단계 구현에서 발생한다. Salesforce는 self-reflection, Claude는 Extended Thinking, OpenAI는 비전 기반 스크린샷 인식, Manus는 Self-Correction Loop로 각각 관찰 단계를 특화했다. 이는 루프의 기본 구조보다 **관찰-반성 메커니즘의 깊이**가 에이전트 품질을 결정한다는 것을 시사한다 -- *Source*: [[salesforce-agentforce]], [[claude]], [[openai]], [[manus-ai]]

2. **거버넌스 통합이 엔터프라이즈 결정적 차별화**: ServiceNow의 Orchestrator와 Workday의 ASOR는 오케스트레이션 루프에 거버넌스를 내장한다. ServiceNow는 매 실행 단계마다 정책 준수를 평가하고 토큰 예산을 실시간 관리하며, Workday는 에이전트의 역할-권한-데이터 접근 범위를 인사 관리 방식으로 제어한다. B2C 제품(Claude, OpenAI, Manus)에는 이러한 수준의 거버넌스 계층이 부재하여, 엔터프라이즈 도입 시 별도의 거버넌스 래퍼를 구축해야 한다 -- *Source*: [[servicenow-now-assist]], [[workday-assistant]]

3. **에러 복구 패턴의 3세대 진화**: 에러 복구 전략이 세대별로 진화하고 있다. 1세대는 단순 재시도(retry), 2세대는 사용자에게 제어권 반환(OpenAI CUA의 "막히면 사용자에게 돌려줌"), 3세대는 자율적 원인 분석 후 대안 전략 시도(Manus Self-Correction Loop, Salesforce Atlas self-reflection)이다. 3세대 적응형 복구를 구현한 제품이 복잡한 실세계 태스크에서 유의미하게 높은 성공률을 보인다 -- *Source*: [[manus-ai]], [[salesforce-agentforce]], [[openai]]

4. **동기 vs. 비동기 루프의 이원화**: Claude Code/Cowork와 OpenAI CUA는 사용자 세션에 바인딩된 동기 루프를 운영하는 반면, Manus AI(14일), OpenAI Codex(7시간+)는 사용자 이탈 후에도 지속되는 비동기 루프를 구현한다. 비동기 루프는 장기 태스크에 적합하나, 중간 결과 확인과 방향 수정의 어려움이라는 트레이드오프가 존재한다. Manus의 "시키고 잊기(Fire and Forget)" 패턴과 실시간 Glass Box 미러링의 결합이 이 트레이드오프를 가장 효과적으로 해결하고 있다 -- *Source*: [[manus-ai]], [[openai]], [[claude]]

5. **프로토콜 기반 멀티 에이전트 통신의 부상**: Workday가 MCP + A2A 프로토콜을 네이티브로 채택하고, Salesforce가 MCP를 3.0부터 내장 지원하면서, 표준 프로토콜 기반의 에이전트 간 통신이 엔터프라이즈 멀티 에이전트 시스템의 기반이 되고 있다. 반면 ServiceNow와 Databricks는 아직 MCP/A2A를 공식 지원하지 않아, 이종 에이전트 간 상호운용성에서 불리한 위치에 있다 -- *Source*: [[workday-assistant]], [[salesforce-agentforce]]

6. **평가-루프 분리 vs. 통합의 설계 철학 차이**: Databricks는 런타임 루프(LangGraph)와 평가 계층(Agent Evaluation)을 명시적으로 분리하여, 루프 실행과 품질 검증을 독립적으로 운영한다. 반면 Salesforce Atlas와 Claude는 self-reflection/Extended Thinking을 루프 내부에 통합하여 런타임 중 자체 품질 평가를 수행한다. 전자는 프로덕션 안정성에, 후자는 실시간 적응성에 유리하다 -- *Source*: [[databricks-mosaic-ai]], [[salesforce-agentforce]], [[claude]]

---

### 1. 기본 루프 아키텍처: Plan-Act-Observe + Self-Reflection 채택

업계 수렴 방향에 맞춰 Plan-Act-Observe를 기본 루프로 채택하되, Salesforce Atlas의 self-reflection 메커니즘을 참조하여 매 관찰 단계 후 "결과 충분성 자체 평가" 단계를 추가할 것을 권장한다. 이를 통해 불필요한 루프 반복을 줄이고 응답 품질을 높일 수 있다.

### 2. 엔터프라이즈 거버넌스 계층 우선 설계

ServiceNow Orchestrator의 정책 인식형 루프를 참조하여, 오케스트레이션 루프의 매 단계에 정책 평가 훅(Policy Evaluation Hook)을 내장해야 한다. 최소 요구사항으로 (1) 역할 기반 액션 범위 제한, (2) 토큰/비용 예산 실시간 관리, (3) 실행 단계별 감사 로그 기록을 루프 아키텍처 수준에서 지원해야 한다.

### 3. 적응형 에러 복구 전략 구현

3세대 에러 복구 패턴(자율적 원인 분석 + 대안 전략 시도)을 구현하되, 복구 시도 횟수와 비용에 상한을 두어 무한 루프와 크레딧 소모를 방지해야 한다. Manus의 Self-Correction Loop 시각화를 참조하여, 에러 복구 과정을 사용자에게 투명하게 공개하는 UX를 병행 설계할 것을 권장한다.

### 4. 하이브리드 동기/비동기 실행 모델

단기 태스크(수 분 이내)는 동기 루프로, 장기 태스크(수 시간~수 일)는 비동기 루프로 자동 분기하는 하이브리드 실행 모델을 검토해야 한다. 비동기 루프 채택 시 Manus의 Glass Box 패턴을 참조하여 실시간 진행 상황 관찰 기능을 필수 포함해야 한다.

### 5. MCP 기반 도구 확장 + 향후 A2A 대비

MCP를 기본 도구 연결 프로토콜로 채택하고, Workday의 A2A 채택 사례를 참조하여 향후 멀티 에이전트 간 통신 프로토콜 지원을 아키텍처 수준에서 대비해야 한다. 초기에는 MCP 기반 단일 에이전트 도구 확장에 집중하되, 에이전트 간 메시지 패싱 인터페이스를 확장 가능하게 설계할 것을 권장한다.

### 6. 계층적 오케스트레이션 로드맵

초기 MVP에서는 단일 Plan-Act-Observe 루프로 시작하되, ServiceNow의 Skills → Agents → Orchestrator 3계층 모델을 로드맵에 반영하여 점진적으로 계층화해야 한다. 이를 위해 초기 설계부터 Skill(원자적 기능 단위)과 Agent(Skill 조합 단위)의 인터페이스를 분리하여 정의할 것을 권장한다.

---

## Source References

### 제품 프로필
- [[salesforce-agentforce]] -- Atlas Reasoning Engine의 Plan-Act-Observe + Self-Reflection 루프, Topic-Action 오케스트레이션
- [[workday-assistant]] -- ASOR 에이전트 라이프사이클 관리, MCP + A2A 프로토콜 기반 Agent Gateway
- [[claude]] -- Agentic Loop (Goal → Plan → Tool Call → Verify → Iterate), Extended Thinking Pipeline
- [[openai]] -- CUA (Screenshot → Action → Verify) 루프, Codex 비동기 샌드박스 실행
- [[servicenow-now-assist]] -- Skills → Agents → Orchestrator 3계층 아키텍처, 정책 인식형 오케스트레이션
- [[databricks-mosaic-ai]] -- Compound AI Systems, Agent Evaluation 기반 품질 게이트, Lakeguard 샌드박스
- [[manus-ai]] -- Planner Agent 기반 멀티 에이전트 분산 오케스트레이션, Self-Correction Loop, Glass Box 투명성

### 외부 참고 자료
- [Salesforce Engineering: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)
- [Workday Blog: AI Agent Protocols Guide](https://blog.workday.com/en-us/building-enterprise-intelligence-a-guide-to-ai-agent-protocols-for-multi-agent-systems.html)
- [Databricks Blog: Mosaic AI Agent Framework and Agent Evaluation](https://www.databricks.com/blog/announcing-mosaic-ai-agent-framework-and-agent-evaluation)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
