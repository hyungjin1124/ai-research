---
type: insight-synthesis
topic_id: agent-reasoning-visualization
topic_name: AI 에이전트 추론 과정 시각화 패턴   비교
category: agent-ui
tags:
- insight
- agent-ui
- reasoning-visualization
- thinking-blocks
- chain-of-thought
- progress-indicators
- source-citation
- transparency
status: draft
confidence: high
last_updated: '2026-02-10'
source_products:
- claude
- openai
- google-gemini
- manus-ai
- salesforce-agentforce
- snowflake-intelligence
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[google-gemini]]'
- '[[manus-ai]]'
- '[[salesforce-agentforce]]'
- '[[snowflake-intelligence]]'
- '[[엔터프라이즈 AI 서비스 비교 분  석]]'
- '[[Claude Cowork UI 분석]]'
- '[[Claude Cowork 플랜 아키텍처]]'
- '[[Claude Cowork 개요]]'
- '[[Manus AI UX 분석]]'
- '[[A2UI 프로토콜 및 MCP-UI 비교]]'
relevant_roles:
- frontend_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - reasoning visualization
  - thought process
  - transparency
  - glass box
  - explainability
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 추론 과정 시각화 패턴 비교

## TL;DR

- AI 에이전트의 추론 과정 시각화는 크게 **4가지 패턴**으로 분류된다: Collapsible Thinking Block, Glass Box Execution Mirror, Step-by-Step Reasoning Chain, Query Translation Transparency. 각 패턴은 정보 밀도와 사용자 개입 수준에 따라 적용 맥락이 다르다.
- **"무엇을 생각했는지"와 "무엇을 실행했는지"의 시각적 분리**가 사용자 신뢰도를 결정하는 핵심 설계 원칙이다. Claude/OpenAI는 사고 과정을 접이식 블록으로 요약하고, Manus AI는 실행 과정을 브라우저 미러링으로 실시간 노출하며, Salesforce는 의사결정 체인을 Topic-Action-Record-Grounding 단계로 구조화한다.
- **진행 상태 표시(Progress Indication)**는 단순 스피너에서 실행 트리/체크리스트/단계별 추적으로 진화하고 있다. Claude Cowork의 Visual To-Do List와 Manus의 실행 트리 시각화가 현재 가장 진보된 구현이며, 사용자의 Waiting Anxiety를 해소하는 데 가장 효과적이다.
- **소스 인용 및 확신도 표현**은 아직 업계 전반에서 미성숙한 영역이다. Perplexity 방식의 인라인 번호 인용이 사실상 표준으로 자리잡는 추세이며, 확신도(Confidence)의 명시적 수치 표현은 Snowflake/ThoughtSpot 같은 데이터 분석 특화 제품에서만 제한적으로 구현되고 있다.
- 엔터프라이즈 환경에서 ERP 에이전트를 구축할 경우, **Query Translation Transparency(SQL/규칙 적용 과정 투명화) + Step-by-Step Reasoning Chain + Risk-Aware Confidence Display**의 3중 조합이 최적의 추론 시각화 전략이다.

---

## Context

AI 에이전트가 단순 질의응답을 넘어 복잡한 비즈니스 의사결정을 지원하게 되면서, "에이전트가 어떻게 그 답을 도출했는지"를 사용자에게 투명하게 전달하는 추론 과정 시각화가 프로덕트 신뢰도의 핵심 결정 요인으로 부상하고 있다. 특히 엔터프라이즈 환경에서는 재무 데이터 분석, 의사결정 지원, 감사 추적 등의 요구사항이 존재하므로, "왜 이 숫자가 나왔는지"를 명확히 설명하는 능력이 단순한 UX 개선이 아닌 비즈니스 요구사항이다.

엔터프라이즈 AI 에이전트 프로덕트가 ERP 데이터를 기반으로 재무, 인사, 운영 영역의 분석과 의사결정을 지원할 경우, 경쟁사들이 추론 과정을 어떤 방식으로 시각화하고 있는지를 체계적으로 분석하고, 데이터 신뢰성이 특히 중요한 ERP 도메인에 최적화된 추론 시각화 전략을 수립할 필요가 있다. 이는 [[hitl-approval-patterns]]에서 다룬 승인 UI 패턴과 직접적으로 연결되는 주제로, 승인 요청 시 "왜 이 결정을 했는지"를 시각화하는 것이 HITL UI의 신뢰도를 높이는 핵심이기 때문이다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 추론 과정 시각화 방식 | 진행 상태 표시 | 소스 인용 | 확신도 표현 | 의사결정 투명성 | 비고 |
|---------|-------------------|-------------|----------|-----------|-------------|------|
| **Claude** | Extended Thinking 접이식 블록 (추론 요약 표시) | Claude Code: 단계별 실행 로그 + diff / Cowork: Visual To-Do List + 체크박스 | 웹 검색 시 인라인 출처 표기 | 명시적 수치 없음 | Agentic Loop 단계 표시, Plan 마크다운 영속화 | Reflect 단계 포함하는 유일한 아키텍처 |
| **OpenAI (ChatGPT)** | Thinking 모드 접이식 블록 (o3/GPT-5.2) | Agent Mode: 단계별 진행 표시 / Codex: 비동기 태스크 상태 | SearchGPT 인라인 인용 (번호 기반) | 명시적 수치 없음 | CUA 기반 스크린샷 인식 과정 비공개 | Adaptive Computation으로 추론 깊이 자동 조절 |
| **Google Gemini** | Deep Think 모드 / Flash Thinking 모드 | Deep Research: 실시간 계획 표시 + 사용자 승인 후 실행 | 답변 내 출처/근거 인라인 표시 | 명시적 수치 없음 | Dynamic View로 결과를 인터랙티브 UI로 변환 | A2UI로 에이전트가 동적 UI 생성 |
| **Manus AI** | Glass Box: 실시간 브라우저 미러링 + 실행 트리 + 코드 노출 | 실행 트리 시각화 (Main Goal -> Sub-tasks, 상태 아이콘) | 작업 과정 자체가 소스 증거 (Artifact as Evidence) | 명시적 수치 없음 | Self-Correction Loop 시각화, Code-First 검증 | 투명성이 사실상 추론 시각화를 대체 |
| **Salesforce Agentforce** | Atlas Engine: Topic -> Action -> Record -> Grounding 단계별 시각화 | Step-by-step reasoning 실시간 표시, Decision tree 시각화 | Data Cloud RAG 기반 Grounding 표시 | Atlas Engine 불확실성 판단 시 자동 에스컬레이션 | Omni Supervisor에서 추론 과정 실시간 감청(Listen-in) | 엔터프라이즈 감독자 뷰에서 추론 과정 모니터링 |
| **Snowflake Intelligence** | SQL 생성 및 실행 과정 시각화, Semantic View 논리 레이어 투명화 | Cortex Agent 실행 단계, 쿼리 실행 계획 표시 | Semantic Model 기반 메타데이터 참조 표시 | YAML 편집 후 즉시 테스트로 정확도 검증, RBAC 기반 신뢰 범위 정의 | RAG retrieval 투명화, LLM + rule-based 분리 표시 | 데이터 분석 도메인 특화 추론 투명성 |

### 패턴 분류

#### 패턴 A: Collapsible Thinking Block (접이식 사고 블록)

에이전트의 내부 추론 과정(Chain-of-Thought)을 접이식(collapsible) 블록으로 요약하여 표시하는 패턴. 사용자가 관심 있을 때만 펼쳐서 확인하고, 기본적으로는 최종 응답에 집중할 수 있도록 설계.

- **대표 제품**: Claude (Extended Thinking), OpenAI (o3/GPT-5.2 Thinking 모드), Google Gemini (Deep Think/Flash Thinking)
- **구현 방식**:
  - Claude: 내부 추론 블록 생성(원본 숨김) -> 추론 요약 표시 -> 최종 응답 출력. 사용자가 접이식 블록을 펼쳐서 단계별 사고 흐름을 확인 가능
  - OpenAI: Thinking 모드 활성 시 추론 과정을 접이식 블록으로 표시. GPT-5.2의 Adaptive Computation이 쿼리 복잡도에 따라 추론 깊이를 자동 조절
  - Google: Gemini 2.5 Flash의 Thinking 모드가 내부 추론을 단계별로 표시
- **장점**: 정보 과부하 방지, 일반 사용자와 전문 사용자 모두를 만족시키는 점진적 공개(Progressive Disclosure), 대화 흐름 유지
- **단점**: 추론 요약의 충실도에 의존(요약이 부실하면 신뢰 하락), 복잡한 멀티스텝 추론에서는 블록 내용이 지나치게 길어질 수 있음
- **적용**: ERP 환경에서 데이터 분석 질의에 대해 "왜 이 숫자인지"를 접이식 블록으로 요약. 기본 뷰에서는 결과만, 펼치면 데이터 소스/계산 로직/필터 조건을 단계별로 표시할 수 있음

*Source*: [[claude]], [[openai]], [[google-gemini]]

#### 패턴 B: Glass Box Execution Mirror (유리 상자 실행 미러링)

에이전트의 실행 과정 자체를 실시간으로 사용자에게 미러링하여, "Thinking..."이 아닌 실제 행동을 관찰하게 하는 패턴. 추론 과정을 별도로 요약하지 않고, 실행 그 자체가 추론의 증거가 됨.

- **대표 제품**: Manus AI (실시간 브라우저 미러링 + 실행 트리 + 코드 노출)
- **구현 방식**:
  - "Manus's Computer" 우측 패널에서 에이전트의 브라우저 활동, 코드 실행, 파일 변경을 실시간으로 관찰
  - 실행 트리로 Main Goal -> Sub-tasks를 계층적으로 표시하고, 각 단계의 상태(Running/Pending/Complete)를 시각화
  - Python/Shell 스크립트 코드를 직접 노출하여 Code-First 검증 가능
  - Self-Correction Loop 발생 시 오류 감지 -> 원인 분석 -> 대안 시도 -> 재실행 사이클을 시각적으로 표시
- **장점**: Waiting Anxiety 완전 해소, 검증 가능성(Verifiability) 극대화, 디버깅 및 학습 효과, 세션 재생(Replay) 가능
- **단점**: 정보 과부하 위험(비전문 사용자에게 코드 노출이 부담), 대역폭 요구(DOM Mutation Streaming), 엔터프라이즈 보안 환경에서 실시간 미러링의 네트워크 제약
- **적용**: ERP 환경에서 에이전트가 SQL 쿼리를 실행하거나 복수 시스템에서 데이터를 수집할 때, 실행 과정을 투명하게 노출. 단, 전체 미러링보다는 쿼리 실행 과정과 결과를 선별적으로 노출하는 "Selective Glass Box" 접근이 적합

*Source*: [[manus-ai]], [[Manus AI UX 분석]]

#### 패턴 C: Step-by-Step Reasoning Chain (단계별 추론 체인)

에이전트의 의사결정 과정을 구조화된 단계(Step)의 연쇄로 시각화하는 패턴. 각 단계가 입력 -> 처리 -> 출력의 명확한 경계를 가지며, 전체 추론 흐름을 선형 또는 트리 형태로 표시.

- **대표 제품**: Salesforce Agentforce (Atlas Engine: Topic -> Action -> Record -> Grounding), Claude Cowork (Observe-Plan-Act-Reflect 루프), Snowflake Intelligence (Cortex Agent 실행 단계)
- **구현 방식**:
  - Salesforce: Atlas Reasoning Engine의 사고 과정을 Topic(의도 분류) -> Action(실행할 작업 선택) -> Record(데이터 접근) -> Grounding(근거 확보) 단계로 실시간 표시. Decision tree 시각화로 분기점을 명확히 표현
  - Claude Cowork: Visual To-Do List로 전체 계획을 체크리스트로 표시하고, 각 항목의 진행 상태를 실시간 업데이트. Reflect 단계에서 자기 반성 결과를 표시
  - Snowflake: Cortex Agent의 실행 단계(질문 분석 -> Semantic Model 선택 -> SQL 생성 -> 실행 -> 결과 평가)를 시각화
- **장점**: 에이전트 행동의 감사 추적(Audit Trail) 용이, 엔터프라이즈 컴플라이언스 요건 충족, 오류 발생 시 정확한 단계 식별 가능
- **단점**: 과도한 단계 표시가 사용자를 압도할 수 있음, 비선형 추론(병렬 도구 호출 등)의 시각화가 어려움
- **적용**: ERP 작업의 의사결정 체인을 "데이터 소스 식별 -> 쿼리 생성 -> 비즈니스 규칙 적용 -> 결과 검증 -> 최종 응답" 단계로 구조화하여 표시할 수 있음. 감사 추적 요건이 있는 재무/인사 영역에서 특히 중요

*Source*: [[salesforce-agentforce]], [[Claude Cowork 플랜 아키텍처]], [[snowflake-intelligence]]

#### 패턴 D: Query Translation Transparency (쿼리 변환 투명성)

자연어 질문이 실제 데이터 쿼리(SQL, API 호출 등)로 변환되는 과정을 투명하게 노출하는 패턴. 데이터 분석 특화 제품에서 주로 사용되며, "어떤 데이터에서 어떤 로직으로 답을 도출했는지"를 기술적으로 검증 가능하게 함.

- **대표 제품**: Snowflake Intelligence (Text-to-SQL 과정 시각화), ThoughtSpot Spotter (Search Token 아키텍처, SQL 생성 표시)
- **구현 방식**:
  - Snowflake: 자연어 -> Semantic View 매핑 -> SQL 생성 -> 실행 -> 결과 시각화의 전 과정을 노출. YAML 기반 Semantic Model이 비즈니스 용어와 DB 스키마를 연결하는 논리 레이어를 투명하게 공개
  - ThoughtSpot: Search Token 아키텍처로 사용자 질문을 구조화된 검색 토큰으로 변환하는 과정을 표시. Patent-pending feedback loop로 단어/구문 단위 교정 가능
- **장점**: 데이터 정확성에 대한 높은 신뢰도, 비즈니스 사용자와 데이터 팀 간 소통 매개체 역할, 오류 원인의 정확한 식별 가능
- **단점**: SQL 가독성이 비기술 사용자에게 부담, 복잡한 조인/서브쿼리에서 시각화가 어려움
- **적용**: ERP 환경에서 데이터 질의 시 변환 과정을 투명하게 노출하는 것이 핵심. 쿼리문을 직접 보여주되, 비즈니스 용어와의 매핑을 함께 제공할 수 있음

*Source*: [[snowflake-intelligence]], [[엔터프라이즈 AI 서비스 비교 분석]], [[Manus AI UX 분석]]

---

## Key Findings

1. **"사고(Thinking)"와 "실행(Execution)"의 시각화는 완전히 다른 설계 문제이다**: Claude/OpenAI는 LLM의 내부 추론(Chain-of-Thought)을 요약하는 "사고 시각화"에 집중하는 반면, Manus AI는 에이전트의 외부 행동(브라우저 조작, 코드 실행)을 미러링하는 "실행 시각화"에 집중한다. Salesforce Agentforce는 이 둘을 결합하여 추론 단계(Atlas Engine 내부)와 실행 단계(Action/Record)를 하나의 체인으로 연결한다. ERP 도메인 특성상 "사고(왜 이 분석을 선택했는지)"와 "실행(어떤 데이터를 어떻게 조회했는지)" 모두를 시각화해야 한다. -- *Source*: [[claude]], [[manus-ai]], [[salesforce-agentforce]]

2. **Waiting Anxiety 해소의 핵심은 "의미 있는 중간 상태" 표시이다**: 경쟁사의 "작업 중..." 로딩 스피너가 유발하는 Waiting Anxiety를 해소하는 데 가장 효과적인 패턴은 단순 진행률 바가 아니라 "지금 무엇을 하고 있는지"를 의미론적으로 설명하는 중간 상태 표시이다. Manus의 실행 트리(Sub-task별 상태 표시), Claude Cowork의 Visual To-Do List(체크박스 기반 단계 추적), Salesforce의 Step-by-Step Reasoning(Topic-Action-Record 단계 표시)이 각각 다른 수준의 의미론적 중간 상태를 제공한다. 공통점은 모두 "현재 단계의 이름 + 상태 아이콘"을 최소 단위로 표시한다는 것이다. -- *Source*: [[Manus AI UX 분석]], [[Claude Cowork UI 분석]], [[엔터프라이즈 AI 서비스 비교 분석]]

3. **소스 인용 시각화의 사실상 표준이 형성되고 있다**: 인라인 번호 인용([1], [2] 등)이 AI 응답의 소스 참조 시각화에서 사실상 표준으로 자리잡고 있다. Google Gemini는 답변 내 출처/근거를 인라인으로 표시하며, Claude도 웹 검색 결과 활용 시 인라인 출처를 표기한다. 그러나 엔터프라이즈 제품에서의 소스 인용은 웹 URL이 아닌 내부 데이터 소스(테이블, 문서, 시스템)에 대한 참조이므로, 인용 클릭 시 해당 데이터 소스로의 드릴다운이 가능해야 한다는 추가 요구사항이 존재한다. -- *Source*: [[google-gemini]], [[claude]], [[snowflake-intelligence]]

4. **확신도(Confidence) 표현은 업계 전반에서 가장 미성숙한 영역이다**: B2C 제품(Claude, ChatGPT, Gemini)은 확신도를 명시적으로 표현하지 않는다. 유일하게 Salesforce Agentforce가 Atlas Engine의 불확실성 판단 시 자동 에스컬레이션을 수행하고, Snowflake Intelligence가 YAML 편집 후 즉시 테스트로 쿼리 정확도를 검증하는 간접적 확신도 표현을 구현한다. 확신도를 수치로 표시하면 사용자가 이를 절대적 정확도로 오해할 위험이 있어, "높음/중간/낮음" 수준의 정성적 표현이나 "이 응답에 대해 추가 검증을 권장합니다" 형태의 맥락적 경고가 더 적절할 수 있다. -- *Source*: [[salesforce-agentforce]], [[snowflake-intelligence]], [[엔터프라이즈 AI 서비스 비교 분석]]

5. **Claude Cowork의 Reflect 단계는 추론 시각화의 차세대 차별화 포인트이다**: [[Claude Cowork 플랜 아키텍처]]에서 분석된 바와 같이, Observe-Plan-Act-**Reflect** 루프에서 Reflect 단계는 에이전트가 실행 결과를 스스로 평가하고 전략을 조정하는 자기 반성 과정이다. 이를 시각화하면 "에이전트가 왜 방향을 바꿨는지"를 사용자에게 설명할 수 있어, 단순 실행 과정 노출을 넘어서는 깊은 투명성을 제공한다. ChatGPT Agent와 Project Mariner는 이 단계가 없어 실패 시 사용자에게 알림 후 직접 해결을 요청하는 수준에 머문다. -- *Source*: [[Claude Cowork 플랜 아키텍처]]

6. **A2UI/MCP-UI 프로토콜이 추론 시각화의 표현력을 혁신적으로 확장할 수 있다**: Google의 A2UI는 에이전트가 대화 맥락에 따라 동적으로 UI를 생성하므로, 추론 과정을 정적 텍스트가 아닌 인터랙티브 시각화(의사결정 트리, 데이터 흐름 다이어그램, 비교 테이블 등)로 표현할 수 있다. MCP-UI는 도구 호출 결과를 인터랙티브 웹 컴포넌트로 직접 반환하므로, 드릴다운/필터링이 가능한 풍부한 데이터 시각화를 추론 과정의 일부로 임베딩할 수 있다. 두 프로토콜 모두 "텍스트 벽(Text Wall)"을 넘어서는 추론 시각화를 가능하게 하는 인프라이다. -- *Source*: [[A2UI 프로토콜 및 MCP-UI 비교]], [[google-gemini]]

---

---

## 소스 제품 매핑

| 제품 | 추론 시각화 관련 핵심 참조 포인트 |
|------|---------------------------|
| [[claude]] | Extended Thinking 접이식 블록, Agentic Loop, Plan 마크다운 영속화, Reflect 단계 |
| [[openai]] | Thinking 모드 접이식 블록, Adaptive Computation, CUA 기반 에이전트 |
| [[google-gemini]] | Deep Think/Flash Thinking, Deep Research 실시간 계획 표시, A2UI 동적 UI 생성 |
| [[manus-ai]] | Glass Box 실시간 미러링, 실행 트리 시각화, Code-First 검증, Self-Correction Loop |
| [[salesforce-agentforce]] | Atlas Engine Step-by-Step Reasoning, Topic-Action-Record-Grounding, Omni Supervisor Listen-in |
| [[snowflake-intelligence]] | Text-to-SQL 변환 투명화, Semantic View/Model, Cortex Agent 실행 단계, RAG 투명화 |

---

## Source References

### 제품 프로필
- [[claude]] -- Extended Thinking Pipeline, 접이식 사고 블록, Agentic Loop, Claude Code 단계별 실행 로그, Claude Cowork Visual To-Do List
- [[openai]] -- GPT-5.2 Thinking 모드, o3 추론 특화 모델, Adaptive Computation, ChatGPT Agent 단계별 진행 표시, Codex 비동기 태스크 상태
- [[google-gemini]] -- Deep Think/Flash Thinking 모드, Deep Research 실시간 계획 표시 + HITL, Dynamic View Generative UI, A2UI 프로토콜
- [[manus-ai]] -- Glass Box 투명성, Two-Pane 아키텍처, 실시간 브라우저 미러링, 실행 트리 시각화, Code-First 검증, Self-Correction Loop 시각화
- [[salesforce-agentforce]] -- Atlas Reasoning Engine, Step-by-Step Reasoning (Topic-Action-Record-Grounding), Decision Tree 시각화, Omni Supervisor 실시간 감청
- [[snowflake-intelligence]] -- Cortex Analyst Text-to-SQL 시각화, Semantic View/Model 논리 레이어, Cortex Agent 실행 단계, RAG retrieval 투명화, RBAC 기반 신뢰 범위

### UI 리서치
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 10개 엔터프라이즈 AI 서비스의 에이전트 추론 과정 시각화, 작업 진행 상태 표현, 데이터 시각화 방식 비교
- [[Claude Cowork UI 분석]] -- Thinking & 진행 상황 업데이트 화면, 3패널 레이아웃, Human-In-The-Loop 다이얼로그, 웹 검색 Tool call 시각화
- [[Claude Cowork 플랜 아키텍처]] -- Observe-Plan-Act-Reflect 루프, Steering Model vs. Confirmation Model vs. Takeover Model, Plan 영속화 방식, Reflect 단계 분석
- [[Claude Cowork 개요]] -- Visual To-Do List, Sub-Agent 아키텍처, Mid-Task Steering, 3단계 권한 시스템
- [[Manus AI UX 분석]] -- Glass Box UX 상세 분석, Two-Pane 아키텍처, CodeAct 패턴, Self-Correction Loop, 경쟁사 투명성 비교
- [[A2UI 프로토콜 및 MCP-UI 비교]] -- A2UI/MCP-UI 프로토콜 비교, 데이터 시각화 측면 장점, 드릴다운/필터/정렬의 직접 조작 UI 패턴

### 외부 참고 자료
- [Anthropic Blog: Extended Thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) -- Extended Thinking Pipeline 공식 문서
- [Emerge Haus: The New Dominant UI Design for AI Agents](https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents) -- Two-Pane 아키텍처, Glass Box 패턴 분석
- [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) -- A2UI 오픈 프로젝트 발표
- [MCP-UI Documentation](https://mcpui.dev/guide/introduction) -- MCP-UI 프로토콜 공식 가이드
- [Salesforce Engineering: Inside the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/) -- Atlas 추론 엔진 내부 구조
- [Snowflake: Cortex Agent Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agent) -- Cortex Agent 에이전틱 루프 구현

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
