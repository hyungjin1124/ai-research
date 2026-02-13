---
type: insight-synthesis
topic_id: artifacts-canvas-patterns
topic_name: Artifacts/Canvas/문서 생성 UI 패턴 비교
category: agent-ui
tags:
- insight
- agent-ui
- artifacts
- canvas
- document-generation
- code-preview
- version-control
status: draft
confidence: high
last_updated: '2026-02-10'
source_products:
- claude
- openai
- google-gemini
- vercel-v0
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[google-gemini]]'
- '[[vercel-v0]]'
- '[[Artifacts Canvas 패턴 개요]]'
- '[[Artifacts 레이아웃 및 인터랙션 상세  ]]'
- '[[문서 생성 HITL 패턴]]'
relevant_roles:
- frontend_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - artifacts
  - canvas
  - collaboration UI
  - code generation UI
  - document generation
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# Artifacts/Canvas/문서 생성 UI 패턴 비교

## TL;DR

- AI 어시스턴트의 콘텐츠 생성 UI는 크게 **4가지 레이아웃 패턴**으로 분류된다: Side Panel(Claude, Gemini), Inline Expandable(ChatGPT Canvas), Full-Screen Takeover(Manus), Chat+Preview Split(v0). 대부분의 제품이 **Chat + 결과물 이중 패널(Two-Pane)** 구조를 기본으로 채택하며, 이것이 2026년 현재 Artifacts/Canvas UI의 지배적 레이아웃 패턴이다.
- **Artifact Trigger 방식**이 사용자 경험을 결정짓는 핵심 분기점이다. Claude는 콘텐츠 유형/길이를 자동 감지하여 Artifact를 생성(antThinking 기반)하고, ChatGPT Canvas는 10줄 이상 콘텐츠 또는 글쓰기/코딩 시나리오에서 자동 열리며, v0는 매 프롬프트마다 프리뷰를 생성한다. 자동 트리거와 명시적 트리거의 균형이 UX 핵심이다.
- **편집 인터랙션의 깊이**에서 제품 간 명확한 차이가 존재한다. ChatGPT Canvas가 가장 깊은 수준의 Direct Manipulation(사용자 직접 편집)을 지원하고, Claude와 Gemini는 Highlight-to-Edit(선택 후 AI 수정 지시) 패턴을 중심으로 하며, v0는 프롬프트 기반 Iterative Refinement에 의존한다.
- **코드 생성 및 프리뷰**에서 v0의 복합 모델(RAG + Base LLM + AutoFix) 아키텍처가 가장 진보된 코드 품질 보장 파이프라인이며, Claude Artifacts의 인라인 코드 실행(HTML/CSS/JS, React, Mermaid)이 가장 폭넓은 실시간 렌더링을 지원한다.
- 엔터프라이즈 ERP 에이전트에 문서 생성 기능을 구축할 경우, **Side Panel 레이아웃 + 자동 Trigger + Highlight-to-Edit + 버전 히스토리**의 조합을 기본으로 하되, ERP 도메인 특화 렌더러(재무 보고서, 대시보드, 전표 프리뷰)를 추가하는 전략이 최적이다.

---

## Context

AI 어시스턴트가 단순한 텍스트 응답을 넘어 코드, 문서, 시각화, 인터랙티브 앱 등 구조화된 산출물(Artifact)을 생성하는 것이 표준이 되면서, "대화 흐름과 산출물을 어떻게 배치하고, 사용자가 어떻게 편집/수정/재사용하는가"가 AI 제품 UX의 핵심 설계 문제로 부상하고 있다. Claude Artifacts, OpenAI Canvas, Gemini Canvas, Vercel v0는 각각 다른 철학과 아키텍처로 이 문제를 접근하고 있으며, 이들의 패턴을 체계적으로 분석하는 것은 엔터프라이즈 AI 에이전트 제품에서 보고서 생성, 대시보드 구성, 데이터 시각화 등의 문서 생성 UI를 설계하는 데 필수적이다.

특히 엔터프라이즈 ERP 맥락에서는 B2C 제품과 달리 (1) 산출물의 정확성 검증이 비즈니스 리스크와 직결되고, (2) 다수의 이해관계자가 산출물을 검토/승인해야 하며, (3) 버전 관리와 감사 추적이 컴플라이언스 요건이므로, B2C 제품의 패턴을 그대로 적용하기보다 엔터프라이즈 필수 요구사항에 맞게 재해석해야 한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 레이아웃 | Artifact Trigger | 편집 방식 | 코드 프리뷰 | 버전 관리 | 공유/협업 | 비고 |
|---------|---------|-----------------|----------|-----------|----------|---------|------|
| **Claude Artifacts** | Side Panel (Chat + 우측 패널) | 자동 감지 (antThinking 기반, 15줄 이상 콘텐츠) | Highlight-to-Edit, Inline Editing | HTML/CSS/JS, React, Mermaid 실시간 렌더링 | Versioned (버전 히스토리, 롤백) | Shareable Link, 원클릭 웹 임베딩 | 무료 포함 전 사용자 이용 가능, window.storage로 세션 간 데이터 영속화 |
| **ChatGPT Canvas** | Inline Expandable (대화 흐름 내 확장) | 자동 (10줄+ 또는 글쓰기/코딩 감지) + 명시적 ("/canvas", "use canvas") | Direct Manipulation (사용자 직접 편집), Highlight-to-Edit | 코드 편집 + 실행 | Version History (이전 버전 복원) | 제한적 | 가장 깊은 수준의 사용자 직접 편집 지원 |
| **Gemini Canvas** | Side Panel (Chat + 우측 패널) | Deep Research 결과 변환, 대화형 생성 | Highlight-to-Edit, Inline Editing | 차트, 대시보드, 인터랙티브 시각화 | 제한적 | Shareable Link | Dynamic View(Generative UI)로 프롬프트에 맞춰 커스텀 UI 동적 렌더링 |
| **Vercel v0** | Chat + Preview Split | 매 프롬프트마다 자동 생성 | 프롬프트 기반 Iterative Refinement | React/Next.js 실시간 프리뷰 + 원클릭 Vercel 배포 | 버전 히스토리 (반복 결과 비교/롤백) | GitHub PR 기반 팀 협업 | RAG + Base LLM + AutoFix 3단 파이프라인으로 코드 품질 보장 |

### 패턴 분류

#### 패턴 A: Side Panel Artifact (사이드 패널 분리형)

대화 영역과 산출물 영역을 좌/우로 분리하여, 대화 맥락을 유지하면서 산출물을 독립적으로 조작하는 패턴. 가장 널리 채택된 레이아웃.

- **대표 제품**: Claude Artifacts (우측 패널에서 코드/문서/시각화 실시간 렌더링), Gemini Canvas (Deep Research 결과를 우측 Canvas에서 인터랙티브 시각화), v0 (좌측 채팅 + 우측 프리뷰)
- **장점**: 대화와 산출물의 명확한 분리로 인지 부하 최소화, 독립적 편집/복사/공유 용이, 버전 관리 자연스럽게 통합
- **단점**: 화면 공간을 많이 차지, 모바일 환경에서 적용 어려움, 산출물이 대화 맥락에서 분리되어 "어떤 대화에서 생성된 것인지" 추적이 어려울 수 있음
- **적용**: ERP 보고서/대시보드 생성 시 대화 맥락을 유지하면서 산출물을 독립적으로 검토/편집할 수 있어 최적. 엔터프라이즈 환경의 넓은 데스크톱 화면에 적합

*Source*: [[claude]], [[google-gemini]], [[vercel-v0]], [[Artifacts Canvas 패턴 개요]]

#### 패턴 B: Inline Expandable Artifact (인라인 확장형)

대화 흐름 내에서 산출물이 직접 확장되어 편집 가능한 영역으로 전환되는 패턴. 대화와 산출물의 맥락적 연속성이 가장 높음.

- **대표 제품**: ChatGPT Canvas (대화 중 자동 또는 수동으로 Canvas 영역이 열리며, 사용자가 직접 텍스트/코드를 편집), ThoughtSpot Spotter (답변 흐름 중간에 차트/데이터 시각화 삽입), Gemini 3 AI mode (답변 내 인터랙티브 요소 삽입)
- **장점**: 맥락 전환 없이 산출물을 확인/편집, "어떤 질문에 대한 결과인지" 명확, Direct Manipulation이 자연스러움
- **단점**: 대화가 길어질수록 산출물 위치 찾기 어려움, 복수 산출물 동시 비교 어려움, 버전 관리 UI 배치가 제약적
- **적용**: ERP 환경에서 단일 질의에 대한 즉각적 데이터 조회/시각화(예: "이번 달 매출 현황 보여줘")에 적합. 복잡한 보고서보다는 간단한 인라인 결과 표시에 활용할 수 있음

*Source*: [[openai]], [[Artifacts 레이아웃 및 인터랙션 상세]]

#### 패턴 C: Full-Screen Takeover (전체 화면 점유형)

복잡한 산출물(대시보드, 앱 실행, 멀티페이지 문서)이 전체 화면을 점유하는 패턴. 산출물의 몰입감과 조작성이 가장 높음.

- **대표 제품**: Manus AI (복잡한 웹앱/대시보드 생성 시 전체 화면 렌더링), 프레젠테이션 생성 도구들(Gamma, Presenton, Genspark -- 슬라이드 편집 시 전체 화면 전환)
- **장점**: 복잡한 산출물의 세부 조작에 최적, 프레젠테이션/대시보드 같은 공간 집약적 콘텐츠에 적합
- **단점**: 대화 맥락과 완전 분리, 컨텍스트 전환 비용 높음, 단순 산출물에는 과도한 UI
- **적용**: 엔터프라이즈 환경에서 대시보드, 보고서 등 복잡한 시각화 결과물의 최종 프리뷰/편집 단계에서 활용. 기본 모드가 아닌 "확대 보기" 옵션으로 제공할 수 있음

*Source*: [[Artifacts Canvas 패턴 개요]], [[Artifacts 레이아웃 및 인터랙션 상세]], [[문서 생성 HITL 패턴]]

#### 패턴 D: Auto-Trigger vs. Explicit-Trigger (자동 트리거 vs. 명시적 트리거)

산출물 생성이 시작되는 방식에 관한 패턴. 사용자 의도를 자동 감지하여 Artifact를 생성하는 방식과, 사용자가 명시적으로 요청하는 방식의 스펙트럼.

- **Auto-Trigger 제품**: Claude (antThinking 기반 콘텐츠 유형/길이/복잡성 자동 감지 -- React 컴포넌트는 라이브 인터랙션, HTML은 실시간 미리보기, 코드는 구문 강조로 렌더링 방식을 자동 분기), ChatGPT Canvas (10줄 이상 콘텐츠 또는 글쓰기/코딩 유용 시나리오 자동 감지), v0 (모든 프롬프트에 대해 코드 + 프리뷰 자동 생성)
- **Explicit-Trigger 제품**: ChatGPT Canvas ("use canvas", "/canvas" 명시적 명령), Salesforce AgentForce (데이터 변경 조건 충족 시 트리거), ThoughtSpot (기존 Artifact에서 드릴다운/필터링 시 새 Artifact 연쇄 생성)
- **장점(Auto)**: 사용자가 별도 명령 없이 자연스러운 경험, 의도 파악의 정확도가 높을수록 UX 우수
- **단점(Auto)**: 불필요한 Artifact 생성으로 인한 노이즈, 사용자가 원하지 않는 시점에 UI 변경
- **적용**: ERP 환경에서는 "보고서를 만들어줘"와 같은 명시적 요청이 대부분이므로, 명시적 트리거를 기본으로 하되, 특정 패턴(데이터 조회 결과가 테이블/차트에 적합한 경우)에서 자동 트리거를 보조적으로 적용할 수 있음

*Source*: [[Artifacts Canvas 패턴 개요]], [[Artifacts 레이아웃 및 인터랙션 상세]], [[claude]], [[openai]]

#### 패턴 E: Progressive Edit Depth (점진적 편집 깊이)

산출물에 대한 사용자 편집 개입의 깊이에 관한 스펙트럼. 가장 얕은 수준(프롬프트만으로 수정)에서 가장 깊은 수준(직접 편집 + AI 협업)까지.

- **Level 1 -- Prompt-Only Refinement**: v0 (프롬프트로만 수정 요청, 비주얼 에디터 부재)
- **Level 2 -- Highlight-to-Edit**: Claude, Gemini (특정 영역 선택 후 AI에게 수정 지시)
- **Level 3 -- Direct Manipulation + AI**: ChatGPT Canvas (사용자가 직접 텍스트/코드 편집 + AI가 실시간 보조), v0 Annotation Mode (제한적 직접 편집)
- **적용**: ERP 보고서에서는 Level 2(Highlight-to-Edit)를 기본으로 하되, 숫자/금액 필드에 대해서는 Level 3(Direct Manipulation)을 지원하여 사용자가 직접 수정 후 관련 계산이 자동 업데이트되는 패턴이 이상적

*Source*: [[Artifacts 레이아웃 및 인터랙션 상세]], [[openai]], [[claude]], [[vercel-v0]]

---

## Key Findings

1. **Two-Pane 레이아웃이 Artifacts/Canvas의 사실상 표준이다**: Claude, Gemini, v0 모두 Chat + Artifact/Preview의 이중 패널 구조를 채택하였고, ChatGPT Canvas도 인라인 형태이지만 결국 대화 영역과 편집 영역을 분리하는 구조이다. 이는 "대화(지시)와 산출물(결과)을 동시에 볼 수 있어야 한다"는 사용자 니즈가 보편적임을 입증한다. Manus AI의 Two-Pane 구조와도 일맥상통한다. — *Source*: [[Artifacts Canvas 패턴 개요]], [[Artifacts 레이아웃 및 인터랙션 상세]]

2. **Artifact Trigger의 자동화 수준이 "마법같은 경험"과 "짜증나는 경험"의 분기점이다**: Claude의 antThinking 기반 자동 감지는 콘텐츠 유형(React 컴포넌트, HTML, 코드, 문서)을 구분하여 최적의 렌더링 방식을 자동 선택하는 반면, ChatGPT Canvas는 10줄 이상이라는 단순 임계값과 "use canvas" 명시적 명령을 병행한다. 자동 트리거의 정확도가 낮으면 사용자가 원하지 않는 시점에 UI가 전환되어 오히려 방해가 되므로, 자동 트리거와 명시적 트리거의 하이브리드 전략이 필요하다. — *Source*: [[claude]], [[openai]], [[Artifacts 레이아웃 및 인터랙션 상세]]

3. **ChatGPT Canvas의 Direct Manipulation이 가장 깊은 편집 경험을 제공하나, 대부분의 사용자는 Highlight-to-Edit로 충분하다**: Canvas에서 사용자가 직접 텍스트를 수정하고 AI가 보조하는 패턴은 Google Docs + AI 협업에 가장 가까운 경험이다. 그러나 Claude와 Gemini의 Highlight-to-Edit(특정 영역 선택 후 AI 수정 지시) 패턴도 사용자들에게 충분한 편집 제어감을 제공하며, 구현 복잡도가 낮다. Direct Manipulation은 "글쓰기" 작업에 최적이고, Highlight-to-Edit는 "생성된 결과물 수정" 작업에 더 적합하다. — *Source*: [[openai]], [[claude]], [[Artifacts 레이아웃 및 인터랙션 상세]]

4. **v0의 RAG + AutoFix 파이프라인이 코드 생성 품질의 새로운 기준을 제시한다**: v0는 단일 LLM에 의존하지 않고, RAG 레이어(최신 프레임워크 문서 검색 주입) + Base LLM(Anthropic Sonnet 기반) + AutoFix 후처리 모델(vercel-autofixer-01)의 3단 파이프라인으로 코드 품질을 보장한다. 특히 AutoFix 모델이 코드 스트리밍 중 실시간으로 오류를 검출/수정하는 방식은, 엔터프라이즈 환경에서 AI가 생성한 보고서/쿼리의 정확성을 보장하는 데 직접 적용 가능한 아키텍처이다. — *Source*: [[vercel-v0]]

5. **버전 관리 기능의 깊이가 제품 간 큰 격차를 보인다**: Claude와 ChatGPT Canvas는 Artifact별 버전 히스토리와 롤백을 지원하지만, 이는 개인 사용자의 작업 흐름 내 버전 관리에 한정된다. v0는 GitHub PR 기반의 팀 단위 버전 관리를 지원하여 협업 시나리오에 강하다. 반면 Gemini Canvas의 버전 관리는 제한적이다. 엔터프라이즈 환경에서는 v0의 PR 기반 워크플로우처럼 다수 이해관계자가 참여하는 검토/승인 기반 버전 관리가 필수적이다. — *Source*: [[claude]], [[openai]], [[vercel-v0]], [[Artifacts Canvas 패턴 개요]]

6. **Gemini의 Generative UI(Dynamic View)가 Artifacts/Canvas의 다음 진화 방향을 제시한다**: Gemini 3는 프롬프트에 맞춰 탭, 스크롤, 드릴다운 등 커스텀 인터랙티브 UI를 실시간으로 코딩/렌더링하는 Dynamic View를 도입하였다. 이는 미리 정의된 Artifact 유형(텍스트, 코드, 차트) 중 하나를 선택하는 기존 패턴과 달리, 산출물의 형태 자체를 AI가 동적으로 결정하는 것이다. Google의 A2UI(Agent-to-UI) 프로토콜이 이 방향을 표준화하려는 시도이다. — *Source*: [[google-gemini]], [[Artifacts 레이아웃 및 인터랙션 상세]]

7. **프레젠테이션/문서 생성에서 HITL 패턴이 제품마다 크게 다르다**: Gamma, Plus AI, Canva AI, Decktopus AI 등의 프레젠테이션 생성 도구와 Claude Cowork의 Skills 기반 문서 생성은 각각 다른 HITL 접근을 취한다. 프레젠테이션 도구들은 "템플릿 선택 -> AI 초안 생성 -> 슬라이드별 편집" 순서를 따르는 반면, Claude Cowork는 "자연어 지시 -> 에이전트 자율 생성 -> 결과 검토" 패턴을 사용한다. — *Source*: [[문서 생성 HITL 패턴]], [[claude]]

---

---

## 소스 제품 매핑

| 제품 | 핵심 Artifacts/Canvas 기능 | 인사이트 기여 영역 |
|------|-------------------------|----------------|
| [[claude]] | Artifacts (Side Panel, antThinking 자동 트리거, Highlight-to-Edit, 인라인 코드 실행, 버전 히스토리, Shareable Link, window.storage) | 레이아웃 표준, 자동 트리거 메커니즘, 편집 패턴, 영속화 |
| [[openai]] | Canvas (Inline Expandable, Direct Manipulation, 10줄+ 자동/명시적 트리거, 버전 히스토리, 코멘트) | 가장 깊은 편집 경험, 인라인 레이아웃 패턴, 직접 편집 + AI 협업 |
| [[google-gemini]] | Canvas + Dynamic View (Generative UI, Deep Research 변환, A2UI 프로토콜, 인터랙티브 시각화) | 차세대 Generative UI 방향, 동적 산출물 형태 결정 |
| [[vercel-v0]] | Chat+Preview Split, RAG+AutoFix 파이프라인, React 실시간 프리뷰, 원클릭 배포, GitHub PR 협업 | 코드 품질 보장 아키텍처, 팀 협업 버전 관리, Iterative Refinement |

---

## Source References

### 제품 프로필
- [[claude]] -- Artifacts 기능 상세, Side Panel 레이아웃, antThinking 자동 트리거, Highlight-to-Edit, 인라인 코드 실행, 버전 관리, 원클릭 웹 임베딩
- [[openai]] -- Canvas 기능 상세, Inline Expandable 레이아웃, Direct Manipulation, 명시적/자동 트리거, 버전 히스토리
- [[google-gemini]] -- Canvas + Dynamic View, Generative UI, Deep Research 결과 변환, A2UI 프로토콜, 인터랙티브 시각화
- [[vercel-v0]] -- Chat+Preview Split 레이아웃, RAG+AutoFix 3단 파이프라인, React 프리뷰, 원클릭 Vercel 배포, GitHub PR 워크플로우

### UI 리서치
- [[Artifacts Canvas 패턴 개요]] -- Layout/Interaction/Trigger/Persistence 4대 패턴 분류, 제품별 특성 비교
- [[Artifacts 레이아웃 및 인터랙션 상세]] -- Side Panel/Full-Screen/Inline 레이아웃 비교, Highlight-to-Edit/Direct Manipulation/Region-based Prompting 인터랙션 상세, Artifacts 구성 요소 매트릭스, 프레젠테이션/Excel 생성 사례
- [[문서 생성 HITL 패턴]] -- Gamma, Plus AI, Canva AI, Decktopus AI의 프레젠테이션 생성 HITL 패턴 스크린샷 비교

### 외부 참고 자료
- [Anthropic Blog: Collaborate with Claude on Projects](https://www.anthropic.com/news/projects) -- Artifacts 기능 및 Projects 통합
- [Vercel Blog: Introducing the v0 composite model family](https://vercel.com/blog/v0-composite-model-family) -- v0의 RAG + AutoFix 아키텍처 상세
- [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) -- Generative UI 표준화 시도
- [Emerge Haus: The New Dominant UI Design for AI Agents](https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents) -- Two-Pane 아키텍처 분석

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
