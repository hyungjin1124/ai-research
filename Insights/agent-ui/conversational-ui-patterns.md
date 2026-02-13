---
type: insight-synthesis
topic_id: conversational-ui-patterns
topic_name: AI 에이전트 대화형 UI 패턴 종합 분  석
category: agent-ui
tags:
- insight
- agent-ui
- conversational-ui
- chat-patterns
- response-rendering
- multimodal-input
- context-management
status: draft
confidence: high
last_updated: '2026-02-10'
source_products:
- claude
- openai
- google-gemini
- microsoft-copilot
- manus-ai
- salesforce-agentforce
- servicenow-now-assist
- sap-joule
- snowflake-intelligence
- thoughtspot-spotter
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[google-gemini]]'
- '[[microsoft-copilot]]'
- '[[manus-ai]]'
- '[[엔터프라이즈 AI 서비스 비교 분  석]]'
- '[[MCP-UI 프로토콜 분석]]'
- '[[A2UI 프로토콜 및 MCP-UI 비교]]'
- '[[Manus AI UX 분석]]'
- '[[Claude Cowork UI 분석]]'
- '[[Claude Cowork 플랜 아키텍처]]'
- '[[Claude Cowork 개요]]'
- '[[Artifacts Canvas 패턴 개요]]'
- '[[Artifacts 레이아웃 및 인터랙션 상세  ]]'
relevant_roles:
- frontend_agent
- planning_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - conversational UI
  - chat interface
  - UX pattern
  - natural language interface
  - dialog design
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 대화형 UI 패턴 종합 분석

## TL;DR

- AI 에이전트의 대화형 UI는 **Chat + Canvas/Artifacts 이중 패널(Dual-Pane)** 구조가 사실상 업계 표준으로 수렴하고 있다. 좌측 대화 + 우측 산출물/실행 관찰 영역의 분리가 Claude, ChatGPT, Gemini, Manus, Snowflake 등 주요 제품 전반에서 채택되었으며, 엔터프라이즈 제품(Microsoft Copilot, SAP Joule)은 기존 애플리케이션 내 **Sidecar 패널** 방식으로 변형 적용한다.
- 응답 렌더링은 **정적 마크다운 → 리치 미디어 카드 → 인터랙티브 UI 컴포넌트**로 진화 중이며, MCP-UI(HTML/URL 임베딩)와 A2UI(선언적 JSON 컴포넌트)가 에이전트 응답의 리치 UI 표준 프로토콜로 경쟁하고 있다. 텍스트 전용 응답의 시대는 종료되었고, **에이전트가 맥락에 맞는 최적 UI를 동적으로 생성하는 Generative UI**가 차세대 핵심 패턴이다.
- 입력 방식은 **텍스트 + 파일 첨부 + 이미지**가 기본이며, OpenAI의 gpt-realtime(Speech-to-Speech)과 Google Gemini Live가 **음성 네이티브 입력**을 선도한다. 에이전트 제품에서는 자연어 입력 외에 **Suggested Prompts, Follow-up Chips, Slash Commands** 등 구조화된 입력 보조 패턴이 대화 효율성을 크게 좌우한다.
- 컨텍스트 관리 UI는 **대화 히스토리 + Projects/워크스페이스 + Memory(장기 기억)** 3계층 구조로 분화되고 있으며, Claude의 Projects(200K 토큰 상시 컨텍스트), ChatGPT의 Memory(대화 간 개인화), Gemini의 1M 토큰 컨텍스트 윈도우가 각각 다른 접근으로 장기 맥락 유지 문제를 해결한다.
- 엔터프라이즈 ERP 에이전트는 **Sidecar 임베딩(맥락 유지) + MCP-UI 기반 리치 응답 렌더링 + 구조화된 입력 보조(도메인 프롬프트 템플릿) + 세션 간 컨텍스트 영속화**를 4대 축으로 대화형 UI를 설계할 수 있다.

---

## Context

AI 에이전트가 단순 Q&A 챗봇을 넘어 실질적인 업무 수행 도구로 진화하면서, 대화형 UI의 설계는 제품의 성패를 결정하는 핵심 요소가 되었다. 메시지 구조, 입력 방식, 응답 렌더링, 컨텍스트 관리 등 대화형 UI의 각 계층이 사용자 경험과 업무 효율에 직접적으로 영향을 미치며, 특히 엔터프라이즈 환경에서는 기존 업무 시스템과의 통합 방식이 채택률을 좌우한다.

엔터프라이즈 ERP AI 에이전트를 구축할 경우, B2C AI 제품(Claude, ChatGPT, Gemini)이 선도하는 최신 대화형 UI 혁신과 엔터프라이즈 AI 제품(Microsoft Copilot, SAP Joule, Salesforce)이 검증한 업무 맥락 내 통합 패턴을 모두 분석하여, 두 영역의 강점을 결합한 최적의 대화형 UI 전략을 수립할 필요가 있다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 레이아웃 패턴 | 입력 방식 | 응답 렌더링 | 컨텍스트 관리 | 추론 과정 시각화 | 비고 |
|---------|------------|---------|-----------|------------|-------------|------|
| **Claude** | Chat + Artifacts 이중 패널 / Cowork 3패널 | 텍스트, 이미지, 파일 첨부 | 마크다운, 코드블록, Artifacts(React/HTML/Mermaid), 데이터 시각화 대시보드 | Projects(200K 토큰), Memory, Styles | Extended Thinking 접이식 블록 | Artifacts 버전 히스토리, Highlight-to-Edit |
| **ChatGPT (OpenAI)** | Chat + Canvas 이중 패널 | 텍스트, 이미지, 파일, 음성(Voice Mode/gpt-realtime) | 마크다운, Canvas(인라인 편집), Deep Research 보고서 | Memory(대화 간 개인화), Custom GPTs | Thinking 모드 접이식 블록 | GPT Store, Voice Mode S2S |
| **Google Gemini** | Chat + Canvas 이중 패널, Dynamic View(Generative UI) | 텍스트, 이미지, 비디오, 오디오, 파일 | 마크다운, Canvas, Dynamic View(실시간 커스텀 UI 생성), 카드/테이블/비교 뷰 | 1M 토큰 컨텍스트, Gems | Thinking 모드 접이식 블록 | A2UI 프로토콜 주도, 멀티모달 네이티브 |
| **Microsoft Copilot** | Sidecar 패널(애플리케이션 내 임베딩) | 자연어 텍스트 | 실시간 스트리밍, Follow-up Suggestions, Timeline Highlights, Rich UI Elements | Dataverse + Microsoft Graph 통합 | Plugin 선택 과정 표시, Multi-Agent 경로 시각화 | 전체 화면 뷰 폐지 → Sidecar 전환 |
| **SAP Joule** | SAP Start/Work Zone 임베딩 | 자연어 텍스트, Guided AI Prompts | Rich UI Elements(List/Card/Carousel), Content Loader, Fiori 컴플라이언트 | SAP Knowledge Graph, 크로스 제품 컨텍스트 | Scenario Catalog 매칭, RAGe 프로세스 투명화 | 2,400+ 스킬 기반 |
| **Salesforce Agentforce** | 3-Panel Layout(Steps/Config/Guidance) | 자연어, Topic-based Organization | Follow-up 질문 제안, 시각화 미리보기, RAG feedback loop | Data Cloud + Zero-Copy, Topic 기반 조직화 | Atlas Engine Step-by-Step Reasoning(Topic→Action→Record→Grounding) | Omni Supervisor 통합 |
| **Manus AI** | Two-Pane(대화 + Manus's Computer) | 텍스트, 파일 드래그앤드롭 | 실시간 브라우저 미러링, 실행 트리, 코드 노출, 산출물(PDF/스프레드시트/웹앱) | 태스크 큐(최대 20개 동시), 세션 재생/공유 | Glass Box(실시간 브라우저 미러링), Self-Correction Loop 시각화 | 최대 14일 비동기 실행 |
| **Snowflake Intelligence** | 독립 인터페이스 + Dual-Pane | Natural Language to SQL | SQL 생성/실행 시각화, Metrics/Dimensions/Facts 구조 | Semantic View 기반, 다수 Semantic Layer | SQL 생성 과정 시각화, RAG 검색 투명화 | YAML 편집 후 즉시 테스트 |
| **ThoughtSpot Spotter** | Chat + Analytics Canvas | 자연어 데이터 질의, Starter Questions | Best-fit 차트 자동 선택, Drill-anywhere, Liveboards | 검색 토큰 아키텍처, 대시보드 PIN 개인화 | Search Token → SQL 생성 표시 | Patent-pending 피드백 루프 |

### 패턴 분류

#### 패턴 A: Dual-Pane 아키텍처 (Chat + Canvas/Artifacts)

대화 영역과 산출물/실행 관찰 영역을 물리적으로 분리하는 레이아웃 패턴. 사용자는 좌측에서 지시하고, 우측에서 결과를 실시간으로 확인하며, 두 영역이 양방향으로 연동된다.

- **대표 제품**: Claude(Chat + Artifacts), ChatGPT(Chat + Canvas), Gemini(Chat + Canvas), Manus(대화 + Manus's Computer), Snowflake Intelligence(Chat + SQL 결과)
- **변형**: Claude Cowork는 3패널(채팅 + Artifact + 파일 트리)로 확장, Manus는 브라우저 미러링으로 특화
- **장점**: 맥락 전환 최소화, 대화와 산출물을 동시에 참조 가능, 복잡한 결과물(코드/차트/문서)의 가독성 확보
- **단점**: 화면 공간 분할로 모바일 환경에서 제약, 단순 Q&A에는 과도한 구조

*Source*: [[claude]], [[openai]], [[google-gemini]], [[manus-ai]], [[Manus AI UX 분석]], [[Claude Cowork UI 분석]]

#### 패턴 B: Sidecar 임베딩 (기존 앱 내 AI 패널)

기존 엔터프라이즈 애플리케이션의 우측 또는 하단에 AI 대화 패널을 삽입하는 패턴. 사용자가 현재 업무 화면을 유지한 채 AI와 상호작용한다.

- **대표 제품**: Microsoft Copilot for Dynamics 365(Sidecar 패널), SAP Joule(SAP Start/Work Zone 임베딩), ServiceNow Now Assist(Now Assist Panel)
- **장점**: 기존 업무 흐름을 유지하면서 AI 활용 가능, 채택 장벽이 낮음, 현재 레코드/데이터에 대한 컨텍스트 자동 전달
- **단점**: 패널 크기 제약으로 복잡한 시각화/분석에 한계, Microsoft는 전체 화면 뷰를 폐지하고 Sidecar로 전환하는 추세
- **적용**: 엔터프라이즈 ERP 환경에서 트랜잭션 화면 내 Sidecar가 1차 인터페이스, 복잡한 분석은 전체 화면 Canvas로 전환하는 하이브리드 전략이 적합

*Source*: [[microsoft-copilot]], [[sap-joule]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 C: Generative UI (동적 UI 생성)

에이전트가 대화 맥락에 따라 최적의 UI 컴포넌트(폼, 차트, 카드, 테이블 등)를 실시간으로 생성하여 응답하는 패턴. 정적 마크다운을 넘어 인터랙티브한 리치 UI를 대화 흐름 내에 삽입한다.

- **대표 제품**: Google Gemini(Dynamic View - 프롬프트에 맞춰 커스텀 UI 코딩/렌더링), Shopify MCP UI(제품 카드 + 옵션 선택 + 장바구니 연동)
- **프로토콜**: MCP-UI(HTML/URL/Remote DOM 기반 UIResource 임베딩), A2UI(선언적 JSON 컴포넌트 스트리밍)
- **장점**: 텍스트만으로는 불가능한 인터랙션(드릴다운, 필터, 폼 입력 등) 제공, 에이전트 응답의 표현력 극대화
- **단점**: MCP-UI는 디자인 일관성 이슈(iframe 이질감), A2UI는 호스트 컴포넌트 카탈로그 구축 부담
- **적용**: ERP 환경에서 데이터 시각화(KPI 카드, 드릴다운 차트)를 MCP-UI로 구현하되, 엔터프라이즈 디자인 시스템으로 일관성을 확보할 수 있음

*Source*: [[MCP-UI 프로토콜 분석]], [[A2UI 프로토콜 및 MCP-UI 비교]], [[google-gemini]]

#### 패턴 D: Glass Box 투명성 (실시간 실행 관찰)

에이전트의 작업 과정을 실시간으로 사용자에게 노출하는 패턴. 로딩 스피너 대신 에이전트가 실제로 무엇을 하는지를 투명하게 보여준다.

- **대표 제품**: Manus AI(실시간 브라우저 미러링 + 실행 트리 + 코드 노출), Claude(Extended Thinking 접이식 블록), Salesforce Agentforce(Atlas Engine Step-by-Step Reasoning)
- **장점**: 대기 불안(Waiting Anxiety) 해소, 에이전트 신뢰도 향상, 디버깅/학습 효과
- **단점**: 구현 복잡도 높음(특히 실시간 미러링), 과도한 정보 노출은 오히려 인지 부하 증가 가능
- **ERP 적용 참고**: SQL 생성 과정 투명화(Snowflake 패턴), ERP 액션의 데이터 소스 → 규칙 적용 → 결과 도출 시각화

*Source*: [[Manus AI UX 분석]], [[claude]], [[salesforce-agentforce]], [[엔터프라이즈 AI 서비스 비교 분석]]

#### 패턴 E: 구조화된 입력 보조 (Guided Input)

사용자의 자연어 입력을 보조하여 대화 효율성을 높이는 패턴. 빈 입력창에서 시작하는 것이 아니라, 맥락에 맞는 질문/명령을 제안하여 사용자의 인지 부하를 줄인다.

- **대표 제품**: Microsoft Copilot(Follow-up Suggestions 자동 생성), SAP Joule(Guided AI Prompts), ThoughtSpot Spotter(Starter Questions), Claude Cowork(추천 작업 버튼 - 자료 정리/이메일 초안/보고서 등), ServiceNow(Carousel format results)
- **장점**: 사용자가 에이전트의 능력 범위를 직관적으로 파악, 프롬프트 엔지니어링 부담 감소, 대화 진행 속도 향상
- **단점**: 제안이 부적절하면 오히려 혼란, 도메인별 정교한 프롬프트 설계 필요
- **적용**: ERP 환경에서 도메인별(재무/인사/구매) 프롬프트 템플릿을 사전 정의하고, 브리핑 후 드릴다운 질문을 자동 제안할 수 있음

*Source*: [[microsoft-copilot]], [[sap-joule]], [[엔터프라이즈 AI 서비스 비교 분석]], [[Claude Cowork UI 분석]]

---

## Key Findings

1. **Dual-Pane 아키텍처가 AI 에이전트 UI의 사실상 표준으로 수렴하고 있다**: Claude Artifacts(2024-06), ChatGPT Canvas(2024-10), Gemini Canvas, Manus Two-Pane, Snowflake Intelligence 등 주요 제품 모두가 Chat + 산출물 영역의 이중 패널 구조를 채택했다. 단일 채팅창 시대는 종료되었으며, "대화"와 "작업/결과"를 물리적으로 분리하되 양방향으로 연동하는 것이 핵심이다. 엔터프라이즈 제품은 이를 Sidecar 변형으로 구현하여 기존 업무 시스템 내에 자연스럽게 통합한다. -- *Source*: [[claude]], [[openai]], [[google-gemini]], [[manus-ai]], [[microsoft-copilot]]

2. **응답 렌더링이 "텍스트 → 리치 미디어 → 인터랙티브 UI → Generative UI"로 4단계 진화하고 있다**: 1세대(마크다운 텍스트) → 2세대(코드블록/이미지/카드) → 3세대(Artifacts/Canvas 실시간 렌더링 + 인라인 편집) → 4세대(에이전트가 맥락에 맞는 최적 UI를 동적 생성). Google Gemini의 Dynamic View와 MCP-UI/A2UI 프로토콜이 4세대를 선도하고 있으며, Shopify MCP UI의 제품 카드 임베딩 사례는 대화 내 리치 UI의 상업적 가치를 입증했다. -- *Source*: [[MCP-UI 프로토콜 분석]], [[A2UI 프로토콜 및 MCP-UI 비교]], [[google-gemini]], [[Artifacts Canvas 패턴 개요]]

3. **MCP-UI와 A2UI는 상호 보완적이며, ERP 환경에서는 MCP-UI 우선 채택이 유리하다**: MCP-UI는 기존 웹 UI 재사용이 용이하고(HTML/URL 임베딩) MCP 생태계와 직접 결합되나 디자인 일관성에 약점이 있다. A2UI는 호스트 네이티브 위젯으로 렌더링하여 브랜드 일관성이 강점이나 컴포넌트 카탈로그 구축 비용이 크다. 기존 ERP 대시보드/리포트를 빠르게 임베딩하려면 MCP-UI가 적합하고, 장기적으로 자체 디자인 시스템과 결합하려면 A2UI 접근도 병행할 수 있다. -- *Source*: [[A2UI 프로토콜 및 MCP-UI 비교]], [[MCP-UI 프로토콜 분석]]

4. **추론 과정 시각화(Thinking Visualization)의 구현 수준이 제품의 신뢰도를 결정한다**: Manus의 Glass Box(실시간 브라우저 미러링)가 가장 높은 투명성을 제공하지만 구현 복잡도도 최고이며, Claude의 Extended Thinking(접이식 추론 요약)이 구현 대비 효과가 가장 균형 잡혀 있다. Salesforce Atlas의 Topic → Action → Record → Grounding 단계별 시각화는 엔터프라이즈 맥락에서 "왜 이 결정을 했는지"를 구조적으로 설명하는 최적 패턴이다. 단순 "작업 중..." 로딩 스피너는 사용자의 대기 불안을 유발하여 이탈률을 높인다. -- *Source*: [[Manus AI UX 분석]], [[claude]], [[salesforce-agentforce]]

5. **음성 입력이 차세대 대화형 UI의 핵심 입력 채널로 부상하고 있다**: OpenAI의 gpt-realtime(Speech-to-Speech 아키텍처)과 Google Gemini Live가 실시간 음성 대화를 선도하고 있으며, Claude는 음성 모드에서 후발 주자다. 엔터프라이즈 ERP 환경에서는 키보드 입력이 여전히 주력이지만, 현장(물류, 제조)이나 이동 중 접근 시나리오에서 음성 입력의 수요가 커지고 있다. -- *Source*: [[openai]], [[google-gemini]]

6. **컨텍스트 관리가 "세션 내 → 세션 간 → 조직 지식" 3계층으로 분화하고 있다**: (1) 세션 내: 멀티턴 대화 맥락 유지(모든 제품). (2) 세션 간: Claude Memory/ChatGPT Memory(개인 선호 기억), Claude Projects(200K 토큰 상시 컨텍스트). (3) 조직 지식: SAP Knowledge Graph, Microsoft Dataverse + Graph, Salesforce Data Cloud. 엔터프라이즈 제품은 3번째 레이어에서 차별화하며, ERP 에이전트라면 ERP 데이터 기반의 조직 지식 레이어를 반드시 갖추어야 한다. -- *Source*: [[claude]], [[openai]], [[sap-joule]], [[microsoft-copilot]]

7. **Artifacts/Canvas의 인터랙션 패턴이 Highlight-to-Edit + Iterative Refinement로 수렴한다**: Claude, ChatGPT, Gemini 모두 산출물의 특정 영역을 선택하여 AI에 수정을 지시하는 Highlight-to-Edit 패턴과, 대화를 통한 점진적 수정(Iterative Refinement) 패턴을 채택했다. ChatGPT Canvas는 Direct Manipulation(사용자 직접 편집)까지 지원하며, ThoughtSpot은 Drill-Down(시각화에서 상세 분석으로 이동) 패턴이 핵심이다. -- *Source*: [[Artifacts Canvas 패턴 개요]], [[Artifacts 레이아웃 및 인터랙션 상세]]

---

---

## 소스 제품 매핑

| 패턴 | 관련 제품 | 소스 문서 |
|------|---------|---------|
| Chat + Artifacts 이중 패널 | Claude, ChatGPT, Gemini | [[claude]], [[openai]], [[google-gemini]] |
| Sidecar 임베딩 | Microsoft Copilot, SAP Joule, ServiceNow | [[microsoft-copilot]], [[sap-joule]], [[servicenow-now-assist]] |
| Generative UI / Dynamic View | Google Gemini, Shopify MCP UI | [[google-gemini]], [[MCP-UI 프로토콜 분석]] |
| Glass Box 투명성 | Manus AI, Claude Extended Thinking, Salesforce Atlas | [[manus-ai]], [[claude]], [[salesforce-agentforce]] |
| 구조화된 입력 보조 | Copilot, SAP Joule, ThoughtSpot, Claude Cowork | [[microsoft-copilot]], [[sap-joule]], [[Claude Cowork UI 분석]] |
| Artifacts 인터랙션 | Claude, ChatGPT, Gemini, ThoughtSpot | [[Artifacts Canvas 패턴 개요]], [[Artifacts 레이아웃 및 인터랙션 상세]] |
| 프로토콜 (MCP-UI/A2UI) | MCP 생태계, Google A2UI | [[MCP-UI 프로토콜 분석]], [[A2UI 프로토콜 및 MCP-UI 비교]] |
| 추론 과정 시각화 | Manus, Claude, Salesforce, Snowflake | [[Manus AI UX 분석]], [[Claude Cowork 플랜 아키텍처]] |
| 컨텍스트 관리 | Claude Projects/Memory, ChatGPT Memory, SAP Knowledge Graph | [[claude]], [[openai]], [[sap-joule]] |

---

## Source References

### 제품 프로필
- [[claude]] -- Chat + Artifacts 이중 패널, Extended Thinking 시각화, Projects/Memory 컨텍스트 관리, Styles 개인화, MCP 생태계
- [[openai]] -- Chat + Canvas 이중 패널, Voice Mode(gpt-realtime S2S), Memory 개인화, Thinking 시각화, Custom GPTs
- [[google-gemini]] -- Dynamic View(Generative UI), 1M 토큰 컨텍스트, 멀티모달 네이티브 입력, A2UI 프로토콜 주도, Gems
- [[microsoft-copilot]] -- Sidecar 패턴(전체 화면 뷰 폐지), Follow-up Suggestions, Dataverse/Graph 통합, Multi-Agent 경로 시각화
- [[manus-ai]] -- Two-Pane 아키텍처, Glass Box 투명성, 실시간 브라우저 미러링, 비동기 실행(14일), 실행 트리 시각화
- [[salesforce-agentforce]] -- 3-Panel Layout, Atlas Engine Step-by-Step Reasoning, Topic-based Organization, Follow-up 질문 제안
- [[sap-joule]] -- Rich UI Elements(List/Card/Carousel), Guided AI Prompts, Fiori 컴플라이언트 렌더링, SAP Knowledge Graph
- [[servicenow-now-assist]] -- Now Assist Panel 임베딩, Carousel format, LLM-based intent recognition, Multi-turn with context
- [[snowflake-intelligence]] -- Natural Language to SQL, SQL 생성 과정 시각화, Semantic View 기반 응답, YAML 편집/테스트
- [[thoughtspot-spotter]] -- Best-fit 차트 자동 선택, Drill-anywhere, Starter Questions, Liveboards PIN 개인화

### UI 리서치
- [[엔터프라이즈 AI 서비스 비교 분석]] -- 10개 엔터프라이즈 AI 서비스의 대화형 UI 패턴 비교 매트릭스, 메인 인터페이스/데이터 시각화/에이전트 추론 시각화 크로스 분석
- [[MCP-UI 프로토콜 분석]] -- MCP-UI UIResource/UIResourceRenderer 아키텍처, 데이터 시각화 장점, Shopify MCP UI 사례
- [[A2UI 프로토콜 및 MCP-UI 비교]] -- A2UI 선언적 JSON 구조, JSONL 스트리밍, MCP-UI와의 관점별/장단점 비교
- [[Manus AI UX 분석]] -- Two-Pane 아키텍처, Glass Box UX, CodeAct 투명성, 경쟁사 비교, Kona I 적용 전략
- [[Claude Cowork UI 분석]] -- 3패널 레이아웃, Thinking/진행 상황 업데이트, PPT/데이터 시각화 Artifacts, Human-In-The-Loop 다이얼로그
- [[Claude Cowork 플랜 아키텍처]] -- Observe-Plan-Act-Reflect 루프, Steering Model vs. Confirmation Model vs. Takeover Model, Plan 영속화 방식 비교
- [[Claude Cowork 개요]] -- Claude Cowork 핵심 기능, 거대 AI 기업 서비스 비교, 오픈소스 대안 조사
- [[Artifacts Canvas 패턴 개요]] -- Layout/Interaction/Trigger/Persistence 패턴 분류, Side Panel vs Full-Screen vs Embedded
- [[Artifacts 레이아웃 및 인터랙션 상세]] -- Highlight-to-Edit, Direct Manipulation, Drill-Down, Region-based Prompting 상세 분석, Artifacts 구성 요소 비교

### 외부 참고 자료
- [MCP-UI Documentation](https://mcpui.dev/guide/introduction) -- MCP-UI 프로토콜 공식 문서
- [A2UI Official Site](https://a2ui.org/) -- Google A2UI 오픈 프로토콜 공식 사이트
- [Shopify MCP UI Breaking the Text Wall](https://shopify.engineering/mcp-ui-breaking-the-text-wall) -- Shopify의 MCP-UI 제품 카드 임베딩 사례
- [Emerge Haus: The New Dominant UI Design for AI Agents](https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents) -- Two-Pane 아키텍처, Glass Box 패턴 분석
- [Anthropic Blog: Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) -- Pause & Ask 패턴, Prompt Injection 방어
- [OpenAI: Introducing gpt-realtime](https://openai.com/index/introducing-gpt-realtime/) -- Speech-to-Speech 아키텍처
- [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) -- A2UI 오픈 프로젝트 발표

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
