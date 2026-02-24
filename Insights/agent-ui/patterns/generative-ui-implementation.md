---
type: insight-synthesis
topic_id: generative-ui-implementation
topic_name: Generative UI 구현 전략
category: agent-ui
document_level: specific
parent_broad:
  - conversational-ui-patterns
  - artifacts-canvas-patterns
catalog_components:
  - generative_ui
tags:
  - insight
  - agent-ui
  - pattern
  - generative-ui
  - dynamic-ui
  - component-generation
  - ai-ui
status: draft
confidence: high
last_updated: '2026-02-15'
source_products:
  - vercel-ai-sdk
  - google-gemini
  - claude-artifacts
  - v0-by-vercel
  - copilotkit
  - mcp-ui
  - mcp-apps
  - chainlit
  - mesop
  - gradio
source_files:
  - '[[Generative UI 프레임워크 비교]]'
  - '[[Agent UI 패턴 분석]]'
auto_update:
  enabled: true
  keywords:
    - generative-ui
    - component-generation
    - ai-generated-ui
    - dynamic-ui
    - ui-spec
    - code-generation
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
  - ai-engineer
  - full-stack-engineer
---

# Generative UI 구현 전략

## TL;DR

- **Generative UI는 3단계 스펙트럼**으로 이해한다: (1) **Static (Component Selection)** — 에이전트가 사전정의 컴포넌트 라이브러리에서만 선택, 최안전/최빠름; (2) **Declarative (UI Spec 생성)** — 에이전트가 JSON/YAML 스펙을 반환, 프론트엔드가 렌더링, 중간 수준의 유연성; (3) **Open-Ended (Full Code Generation)** — 에이전트가 React/HTML 코드 생성, 샌드박스 실행, 최유연/최위험. [^1][^2]
- **2026년 표준화 동향**: MCP-UI(Anthropic/OpenAI 협력), AG-UI(CopilotKit), A2UI(Google) 같은 **표준 프로토콜이 Declarative 스펙을 중심으로 등장**. Static 방식은 거의 모든 제품의 기본 기능으로 정착. [^3][^4]
- **Claude Artifacts, v0 by Vercel**은 Open-Ended 방식의 프로덕션 구현. 각 요청마다 새로운 코드 생성 (무상태 stateless), 샌드박스 격리로 보안 보장, React/Tailwind/Shadcn UI 스택 고정. [^5][^6]
- **Vercel AI SDK 3.0**의 `streamUI()` 함수는 **React Server Components로 Generative UI를 스트리밍**, 즉 LLM 응답 진행 중에 UI 업데이트 가능. 이는 응답 완료까지 기다리지 않고 실시간 렌더링. [^7]
- **KonaI-Agent 권장 전략**: Level 1 (Static) 즉시 구현으로 MVP 완성. 기존 ChartWidgets, DataTable 등을 "컴포넌트 카탈로그"로 정의. 에이전트가 `{type: 'bar-chart', data: {...}}` 형태의 출력만 하면 프론트엔드가 자동 렌더링. Level 2 (Declarative)는 향후 확장, Level 3는 고려 불필요 (보안/성능 비용 대비 ROI 부족). [^8]

---

## Overview

Generative UI는 **"사용자의 요청에 응답하여 AI 에이전트가 UI를 동적으로 선택, 조립, 또는 생성하는 패턴"**이다. 기존 챗봇이 텍스트/마크다운만 반환했다면, Generative UI는 **구조화된 컴포넌트(차트, 테이블, 폼 등)를 에이전트가 응답에 포함**시킨다.

2025~2026년 현재, Generative UI는 세 가지 구현 수준으로 분화하고 있다:

1. **Static (Component Selection)**: 에이전트는 사전정의된 컴포넌트 라이브러리에서 **"어떤 컴포넌트를 보여줄 것인가"만 결정**. UI 구조/스타일은 개발자가 사전에 정의. 가장 안전하고 빠르지만 유연성 제약.

2. **Declarative (Spec-Based)**: 에이전트가 **구조화된 스펙(JSON/YAML)을 생성**하면, 프론트엔드가 이를 해석하여 렌더링. 표준 프로토콜(MCP-UI, AG-UI)로 다양한 클라이언트 지원 가능.

3. **Open-Ended (Full Generation)**: 에이전트가 **전체 UI 코드(React, HTML)를 생성**. 샌드박스에서 실행. 최고의 유연성이지만 보안/성능 비용 최대.

KonaI-Agent의 경우, **데모 프로젝트 특성상 Static 단계에서 완전히 만족할 수 있다**. 많은 사용자가 생각하기에 "AI가 UI를 생성한다 = 코드 생성"이라고 착각하지만, 사실 데모에서는 "컴포넌트 선택"만으로도 충분한 임팩트를 낼 수 있다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 구현 수준 | 메커니즘 | 컴포넌트 자산 | 보안 | 성능 | 프로토콜 표준화 |
|------|--------|--------|----------|------|------|-------------|
| **Vercel AI SDK 3.0** | Declarative + RSC Streaming | React Server Components, `streamUI()` 함수 | 자유 (개발자 정의) | 높음 (SSR) | 높음 (스트리밍) | 초안 단계 |
| **Google Gemini Dynamic View** | Open-Ended | Prompt → Gemini 3 코드생성 → 동적 렌더링 | Google 소유 라이브러리 | 중간 (샌드박스) | 낮음 (코드생성) | 비공개 |
| **Claude Artifacts** | Open-Ended | Prompt → Claude 코드생성 → iframe 샌드박스 | React, Tailwind, Shadcn, Lucide, Recharts | 높음 (iframe 격리) | 낮음 (코드생성) | 비공개 |
| **v0 by Vercel** | Open-Ended | Prompt → v0 모델 코드생성 → 다운로드 | React, Next.js, Tailwind, Shadcn | 높음 (로컬) | 낮음 (코드생성) | 미정 |
| **CopilotKit** | All 3 levels | 프레임워크로 Static/Declarative/Open-ended 지원 | 개발자 정의 | 제어 가능 | 제어 가능 | AG-UI 준수 |
| **MCP Apps** | Declarative + 선택적 HTML | Tools return UI metadata → HTML served | 제한된 라이브러리 | 높음 (MCP 제어) | 높음 (간단) | MCP spec 준수 |
| **MCP-UI (커뮤니티)** | Declarative | Agent returns intent → 클라이언트 렌더링 | 멀티클라이언트 호환 | 높음 (intent 기반) | 높음 | MCP-UI 표준 |
| **Chainlit** | Static + Limited Declarative | 사전정의 컴포넌트 선택 | Chainlit 라이브러리 고정 | 높음 | 최고 | 비표준 |
| **Mesop (Google)** | Static/Declarative 혼합 | Python UI 선언형, React 컴파일 | Google 컴포넌트 세트 | 높음 | 높음 | 비공개 |
| **Gradio** | Static + Limited Declarative | Interface 클래스, 사전정의 컴포넌트 | Gradio 라이브러리 고정 | 높음 | 최고 | 비표준 |

### 경쟁사별 상세 분석

#### Vercel AI SDK 3.0 — React Server Components + streamUI() 함수

Vercel AI SDK 3.0은 **OpenAI의 v0 기술을 오픈소스화**하면서, `streamUI()` 함수로 **React Server Components를 LLM 응답과 함께 스트리밍**한다. [^7]

핵심은 **"응답을 기다리지 않고 실시간 렌더링"**이다. 기존 방식: LLM → 전체 응답 생성 → UI 렌더링. 새로운 방식: LLM 첫 토큰부터 → 부분 응답 → 즉시 렌더링 → 계속 업데이트. 이는 응답 시간 체감을 극적으로 단축한다.

예시:
- 사용자: "Sales Dashboard 만들어줄래?"
- AI: 부분 응답 시작 → streamUI()가 즉시 `<Dashboard>` 컴포넌트 렌더링
- → 데이터 로딩 중 → 테이블 행 추가 → 차트 업데이트

**구현 메커니즘**: 개발자가 `streamUI()` 콜백에서 "가능한 컴포넌트 집합"을 정의. LLM이 해당 컴포넌트를 선택/호출하면, React가 즉시 렌더링. Declarative + Dynamic의 하이브리드.

**왜 이 방식인가**: Generative UI의 가장 큰 문제는 "응답 완료까지 사용자가 기다린다"는 것. streamUI()는 이를 **스트리밍으로 해결**. Next.js 15 + React 18의 Server Components 성숙화가 이를 가능하게 했다. [^7]

#### Google Gemini Dynamic View — AI-Driven Full Code Generation

Google Gemini Dynamic View는 **"자연어 프롬프트 → Gemini 3 코드생성 → 동적 대시보드"**의 완전 자동화다. [^8]

사용자가 "2024년 매출 분석하고 인터랙티브 차트 보여줄래?"라고 요청하면, Gemini는 **HTML/CSS/JavaScript(또는 React)를 생성**하여 그 자리에 렌더링한다. 스크린 내에 완전히 독립적인 UI가 나타난다.

**특징**:
- **무상태(Stateless)**: 매 요청마다 새로운 코드 생성. 이전 코드와 상태 공유 안 함.
- **동적 재구성**: 사용자가 "이제 지역별로 보여줄래?"라고 재요청 → 완전히 새로운 코드 생성 → 이전 UI 대체
- **라이브러리 고정**: Google의 내부 라이브러리만 사용. 외부 라이브러리 추가 불가.

**왜 이 방식인가**: Google은 Gemini 3의 추론 능력(thinking time)과 코드 생성 능력을 최대한 활용하고자 함. 사전정의 컴포넌트에 제약되기보다 "원하는 모양이면 생성"하는 자유도. 단, 응답 시간(코드생성)이 느리고, 보안(임의 코드 실행) 우려 존재. [^8]

#### Claude Artifacts — Sandbox Isolation + Production-Grade Components

Claude의 Artifacts는 **Open-Ended 방식의 가장 성숙한 프로덕션 구현**이다. [^5]

사용자가 "React로 투두리스트 앱 만들어줄래?"라고 요청하면, Claude는 완전한 React 컴포넌트 코드를 생성. 프론트엔드는 이를 **iframe 샌드박스**에서 실행한다. 샌드박스 내부는 완전 격리된 환경:
- 외부 API 호출 차단 (보안)
- 클라이언트 메모리만 사용
- 브라우저 로컬 스토리지 접근 가능

**사용 가능한 라이브러리**: React, React Hooks, Tailwind CSS, Shadcn UI, Lucide Icons, Recharts. 이들은 iframe 내부에 사전 번들링되어 있음.

**왜 이 방식인가**: Claude는 대화형 AI로서, 사용자가 "조금 더 이렇게 수정해줄래?"라고 반복 요청하는 워크플로우를 지원해야 함. 매번 새로운 아티팩트를 생성하는 것이 자연스럽다. 동시에 iframe 격리로 사용자의 메인 환경 보호. [^5]

**제약**: 외부 데이터 API 호출 불가. 따라서 실시간 데이터가 필요한 경우 제한적. 하지만 데모/프로토타입 용도로는 충분.

#### v0 by Vercel — Full-Stack Code Generation + One-Click Deploy

v0는 **UI 생성을 넘어 배포까지 원클릭으로 제공**한다. [^6]

사용자가 프롬프트 입력 → v0가 React + Next.js 완전 프로젝트 생성 → "Deploy to Vercel" 클릭 → 즉시 라이브 URL 획득. 이는 **Generative UI가 프로덕션 배포로 바로 연결**되는 첫 사례.

**설계 철학**: "빠른 프로토타이핑 → 즉시 배포 → 실시간 반복"의 개발 사이클을 가능케 함. 디자이너/비개발자가 앱 아이디어를 실행 가능한 서비스로 변환.

**왜 이 방식인가**: Vercel의 비즈니스 모델은 "개발자 경험(DX) 최적화"이므로, 생성 → 배포까지의 마찰 제거가 핵심. v0는 AI 코드생성 + Vercel 인프라의 완전한 통합. [^6]

#### CopilotKit — Framework Supporting All 3 Levels

CopilotKit는 **선택적 일관성**으로 Static/Declarative/Open-ended를 모두 지원한다. [^3]

개발자는 애플리케이션 특성에 따라 수준을 선택:
- **Static**: "차트, 테이블, KPI 중 선택만 하고 싶다" → 컴포넌트 카탈로그 정의
- **Declarative**: "더 유연한 레이아웃이 필요" → JSON 스펙 정의
- **Open-ended**: "완전 자유도" → 코드생성 에이전트 활용

이들은 **AG-UI 프로토콜**로 상호호환 가능. 즉, Static 컴포넌트도 AG-UI 스펙으로 기술되면, Declarative 에이전트가 이를 활용 가능.

**왜 이 방식인가**: 모든 사용 사례가 Open-ended를 필요로 하지는 않다. 보안, 성능, 예측 가능성이 더 중요한 경우도 많다. CopilotKit는 **점진적 복잡도 증가**를 지원하는 프레임워크로서, Static에서 시작하다가 필요시 Declarative로 진화 가능하게 설계됨. [^3]

#### MCP Apps (Model Context Protocol) — Declarative + Intent-Based

MCP Apps는 **Anthropic이 공식화한 표준**으로, MCP Tools의 반환값이 "UI 메타데이터"를 포함한다. [^4]

예시: 에이전트가 `get_sales_chart()` 도구 호출 → MCP Server가 반환:
```json
{
  "result": "sales chart data",
  "ui": {
    "type": "chart",
    "spec": {...}
  }
}
```

프론트엔드는 "ui" 섹션을 파싱하여 렌더링.

**왜 이 방식인가**: MCP는 "에이전트와 도구 간의 표준 프로토콜"이므로, UI 반환도 이 프로토콜에 포함하는 것이 자연스럽다. 이를 통해 **MCP-호환 모든 클라이언트**(Claude, OpenAI, 기타)가 동일 Generative UI를 경험 가능. [^4]

#### Chainlit, Mesop, Gradio — Python 프레임워크의 Generative UI

이들은 **Python 기반 AI 애플리케이션 개발을 위한 프레임워크**로서, Generative UI를 제한적으로 지원한다. [^9]

- **Chainlit**: LLM 응답에 사전정의 컴포넌트(Button, Form, Data Table) 첨부 가능. Static 수준.
- **Mesop (Google)**: Python에서 선언형 UI 작성 → React로 컴파일. 구조는 Static이지만 Python 개발자 친화적.
- **Gradio**: 머신러닝 모델 데모용으로 출발. 최근 Chatbot 지원 추가. 매우 간단한 Static UI 구성.

**공통점**: 모두 **"Python 개발자도 쉽게 AI UI를 만들 수 있도록"**이 목표. JavaScript/React 경험 불필요.

**왜 이 방식인가**: Python 생태계(데이터 사이언스, AI 모델)가 매우 크므로, 이들을 위한 UI 도구 필요. 하지만 UI 자체는 복잡할 필요 없으므로, Static + 간단한 컴포넌트로 충분. [^9]

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Static Component Selection (정적 컴포넌트 선택)

에이전트가 사전정의된 컴포넌트 라이브러리에서 **"어떤 컴포넌트를 사용할 것인가"만 결정**하는 패턴.

- **대표**: Chainlit, Gradio, 대부분의 초기 Generative UI 구현
- **메커니즘**:
  - 개발자가 미리 컴포넌트 정의: `ChartComponent`, `TableComponent`, `FormComponent` 등
  - 에이전트 프롬프트: "다음 중 적절한 컴포넌트를 선택하세요: [Chart, Table, Form]"
  - 에이전트 응답: `{type: 'chart', data: {...}}`
  - 프론트엔드: 타입 기반 렌더링
- **장점**:
  - 구현 난이도 낮음
  - 안전성 최고 (컴포넌트는 검증된 코드)
  - 성능 최고 (동적 코드 생성 없음)
  - 일관된 UX (모든 UI가 사전정의 스타일 준수)
  - 오류 가능성 최소
- **단점**:
  - 유연성 제약 (정해진 컴포넌트만 가능)
  - 복잡한 레이아웃 표현 어려움
  - 새 컴포넌트 추가 시 개발자 개입 필요
- **적합한 상황**:
  - 데모/프로토타입
  - 특정 도메인 전용 애플리케이션 (e.g., 분석 대시보드)
  - 성능/안전성이 유연성보다 중요한 경우

### 패턴 B: Declarative Spec Generation (선언형 스펙 생성)

에이전트가 **구조화된 스펙(JSON/YAML)을 생성**하고, 프론트엔드가 해석하여 렌더링하는 패턴.

- **대표**: Vercel AI SDK (streamUI), CopilotKit (Declarative Level), MCP Apps, Google A2UI
- **메커니즘**:
  - 에이전트가 다음과 같은 JSON 스펙 생성:
    ```json
    {
      "version": "1.0",
      "layout": "grid",
      "children": [
        {
          "type": "chart",
          "chartType": "bar",
          "title": "Sales Trend",
          "data": {...},
          "options": {...}
        }
      ]
    }
    ```
  - 프론트엔드 Renderer가 이를 해석 → 동적 레이아웃 구성
- **장점**:
  - Static과 Open-ended의 중간 지점 (유연성 + 안전성 균형)
  - 표준 프로토콜 준수 가능 (MCP-UI, AG-UI, A2UI)
  - 다양한 클라이언트에 같은 스펙 제공 가능
  - 성능 비교적 양호 (코드생성 없음)
  - 복잡한 레이아웃 표현 가능
- **단점**:
  - Static보다 구현 복잡 (스펙 파서 필요)
  - 스펙이 항상 정확하지 않을 수 있음 (에이전트 오류)
  - 스펙 버전 관리 필요
- **적합한 상황**:
  - 유연성이 필요하지만 안전성도 중요한 경우
  - 다중 플랫폼 지원 필요 (웹, 모바일, 데스크톱)
  - 표준 프로토콜 준수 필요

### 패턴 C: Open-Ended Full Code Generation (완전 코드 생성)

에이전트가 **UI 코드(React, HTML)를 전체 생성**하고, 샌드박스에서 실행하는 패턴.

- **대표**: Claude Artifacts, v0 by Vercel, Google Gemini Dynamic View
- **메커니즘**:
  - 에이전트가 완전한 React 컴포넌트 생성
  - 프론트엔드가 iframe 또는 기타 격리 메커니즘에서 실행
  - 사용자 상호작용 → 재 프롬프트 → 새로운 코드 생성
- **장점**:
  - 최고 유연성 (임의의 UI 구성 가능)
  - 사용자가 상상하는 모든 것을 구현 가능
  - 반복 개발 자연스럼 ("조금 더 이렇게 해줄래?" → 새 코드 생성)
  - 디자인 일관성 불필요 (매번 새로운 UI)
- **단점**:
  - 성능 낮음 (매번 코드생성 → 100~1000ms)
  - 보안 우려 (임의 코드 실행)
  - 구현 복잡 (샌드박스 격리, 에러 핸들링)
  - 예측 불가능 (생성된 코드 품질 가변적)
  - 외부 API 호출 제약
- **적합한 상황**:
  - 완전한 UI 맞춤화 필요
  - 프로토타입/데모 (성능 덜 중요)
  - 반복 개발 워크플로우 (사용자가 계속 수정 요청)

### 패턴 D: Declarative + RSC Streaming (선언형 + 스트리밍)

Vercel AI SDK의 특화 패턴. 에이전트가 컴포넌트를 선택/호출하면, **React Server Components로 변환되어 실시간 스트리밍 렌더링**.

- **대표**: Vercel AI SDK 3.0 (`streamUI()`)
- **메커니즘**:
  - 개발자가 `streamUI()` 콜백에서 가능 컴포넌트 정의
  - LLM이 이들을 호출 → 즉시 UI 렌더링 (응답 완료 대기 없음)
  - 응답 진행 중 → 계속 새로운 UI 요소 추가
- **장점**:
  - 응답 시간 극적 단축 (Perceived Latency 낮음)
  - Static의 안전성 + Dynamic의 유연성
  - 최신 React 기능(Server Components) 활용
  - 고성능 (스트리밍)
- **단점**:
  - Next.js 15 + React 18 필수 (모던 스택 강제)
  - 개발자가 스트림 아키텍처 이해 필요
  - 기존 레거시 시스템과 호환 어려움
- **적합한 상황**:
  - 모던 Next.js 스택 사용 중
  - 응답 시간 성능이 매우 중요
  - 실시간 데이터 업데이트 필요

### 트레이드오프 요약

| | 구현 난이도 | 유연성 | 성능 | 안전성 | 응답 시간 | 데모 임팩트 |
|---|---|---|---|---|---|---|
| **Static** | 낮음 | 낮음 | **최고** | **최고** | 낮음 | 중간 |
| **Declarative** | 중간 | 중간 | 높음 | 높음 | 중간 | 높음 |
| **Open-Ended** | 높음 | **최고** | 낮음 | 중간 | 높음 | **최고** |
| **Declarative + RSC** | 높음 | 중간 | **최고** | 높음 | **낮음** | **최고** |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 | Generative UI 역할 |
|----------|-----------|-------------|
| `ChartWidgets.tsx` (Recharts) | 직접 활용 가능 | Static Pattern의 핵심 컴포넌트. BarChart, LineChart, PieChart, AreaChart 등을 "선택 가능한 컴포넌트"로 정의. |
| `LiveboardView.tsx` | 컨테이너로 활용 | 생성된 차트/위젯을 배치하는 그리드 컨테이너. react-grid-layout으로 동적 배치 가능. |
| `DetailDashboard.tsx` | 상세 뷰 컨테이너 | Generative UI로 생성된 컴포넌트를 드릴-다운 뷰에 표시. |
| `DataTable` (미존재, 필요) | 신규 구현 필요 | 테이블 형태의 데이터 표시. Static Pattern에 필수 컴포넌트. |
| `InsightModal.tsx` | AI 인사이트 래퍼 | 에이전트가 선택한 컴포넌트 + 텍스트 분석을 함께 표시. |
| `useScenarioOrchestration.ts` | 시나리오 로직 | "어떤 컴포넌트를 선택할 것인가"의 결정을 시나리오 단계로 모델링 가능. |
| `Radix UI 컴포넌트` (Dialog, Select, Tabs, Tooltip) | 구조 컴포넌트 | Form, Modal, 탭 레이아웃 등에 활용. |
| `NotificationContext` | 상태 알림 | Generative UI 렌더링 상태 표시. |

### 권장 접근: 3-Level 점진적 구현

KonaI-Agent는 데모 프로젝트이므로, **Level 1 (Static)에서 완전히 만족할 수 있다**. 하지만 향후 확장성을 위해 Level 2로의 진화 경로를 남겨두는 것이 좋다.

#### Level 1 MVP (Static Component Selection) — 즉시 구현, 1~2주

**컴포넌트 카탈로그 정의**:
```typescript
type GenerativeComponentType =
  | 'bar-chart'
  | 'line-chart'
  | 'pie-chart'
  | 'area-chart'
  | 'data-table'
  | 'kpi-card'
  | 'stat-grid'
  | 'heatmap';

interface GenerativeUISpec {
  componentType: GenerativeComponentType;
  title?: string;
  description?: string;
  data: any;
  options?: Record<string, any>;
  layout?: {
    width?: 'full' | 'half' | 'third';
    height?: 'small' | 'medium' | 'large';
  };
}
```

**에이전트 프롬프트 엔지니어링**:
```
사용자의 요청을 분석하여 가장 적절한 시각화를 선택하세요.
가능한 컴포넌트:
- bar-chart: 범주별 비교
- line-chart: 시간 추이
- pie-chart: 비율 분석
- data-table: 상세 데이터
- kpi-card: 핵심 지표
- heatmap: 다차원 강도 분석

응답 형식 (JSON):
{
  "reasoning": "왜 이 컴포넌트를 선택했는가",
  "component": {
    "componentType": "bar-chart",
    "title": "2024년 월별 매출",
    "data": [{month: "Jan", value: 10000}, ...],
    "options": {
      "xAxis": "month",
      "yAxis": "value"
    }
  }
}
```

**프론트엔드 구현**:
```typescript
function GenerativeUIRenderer({ spec }: { spec: GenerativeUISpec }) {
  const renderComponent = () => {
    switch (spec.componentType) {
      case 'bar-chart':
        return <BarChart data={spec.data} {...spec.options} />;
      case 'line-chart':
        return <LineChart data={spec.data} {...spec.options} />;
      case 'data-table':
        return <DataTable data={spec.data} {...spec.options} />;
      // ... 등등
      default:
        return <div>Unknown component type</div>;
    }
  };

  return (
    <div className="generative-ui">
      {spec.title && <h3>{spec.title}</h3>}
      {renderComponent()}
      {spec.description && <p className="description">{spec.description}</p>}
    </div>
  );
}
```

**할 일**:
1. 위 카탈로그 기반 Enum 정의 + TypeScript 타입
2. GenerativeUIRenderer 컴포넌트 구현
3. 에이전트 프롬프트 최적화 (컴포넌트 선택 정확도)
4. InsightModal에 GenerativeUIRenderer 삽입
5. 각 컴포넌트 타입별 옵션 스키마 정의 (데이터 형식, 차트 옵션 등)
6. 에러 핸들링 (잘못된 데이터 형식, 알 수 없는 컴포넌트 타입)

**예상 효과**:
- "2024년 매출을 보고 싶어" → 에이전트가 자동으로 BarChart 선택 + 데이터 구성 + 렌더링
- "이 수치가 의미하는 것을 설명해줄래?" → KPI 카드 + 텍스트 분석
- 사용자는 "AI가 차트를 생성했다"는 경험 + 데모 임팩트

#### Level 2 Stretch Goal (Declarative Spec) — 향후 확장, 3~4주

Level 1 완료 후 3~6개월 뒤에 고려.

**변경점**:
- 에이전트가 JSON 스펙 생성 (단순 컴포넌트 선택 아님)
- 스펙에 "레이아웃, 그리드 구성, 필터" 등 포함 가능
- 프론트엔드가 더 복잡한 렌더링 로직 필요

**예시 스펙**:
```json
{
  "version": "1.0",
  "layout": "grid",
  "gridSize": 12,
  "children": [
    {
      "type": "chart",
      "componentType": "bar-chart",
      "gridCol": [1, 7],
      "gridRow": [1, 3],
      "title": "매출 현황",
      "data": {...}
    },
    {
      "type": "chart",
      "componentType": "pie-chart",
      "gridCol": [7, 13],
      "gridRow": [1, 3],
      "title": "제품 구성",
      "data": {...}
    },
    {
      "type": "table",
      "gridCol": [1, 13],
      "gridRow": [3, 5],
      "title": "상세 데이터",
      "data": {...}
    }
  ]
}
```

**할 일**:
1. Declarative Spec 스키마 정의 (JSON Schema 또는 TypeScript)
2. Grid-based Layout Renderer 구현 (react-grid-layout 재활용)
3. 다양한 컴포넌트를 동적으로 렌더링하는 Renderer 고도화
4. 에이전트 프롬프트 고도화 (레이아웃까지 결정)
5. 스펙 버전 관리 및 하위호환성

**이 수준은 Level 1에 비해 훨씬 강력**: 사용자가 여러 차트를 한 번에 볼 수 있는 완전한 대시보드를 AI가 구성.

#### Level 3 (선택 불필요) — 고려하지 말 것

Open-Ended 코드 생성(Claude Artifacts 방식)은 KonaI-Agent에 **불필요**하다:
- 데모 성능 저하 (코드생성 시간)
- 보안 오버헤드 (샌드박스 관리)
- ROI 부족 (Level 1-2로 충분한 임팩트)

필요하다면 향후 별도 "AI Playground" 피처로 분리하여 고려.

### 이 접근을 권장하는 이유

1. **빠른 MVP 완성**: Level 1은 1~2주로 완료 가능. 데모에 즉시 활용.
2. **기존 코드 활용**: ChartWidgets, InsightModal 기존 자산 최대 활용.
3. **안전성**: 정의된 컴포넌트만 사용하므로 예측 가능, 오류 최소.
4. **성능**: 동적 코드생성 없음. 실시간 응답성.
5. **명확한 확장 경로**: Level 2로의 진화 경로 설계됨. 증분 개선 가능.
6. **데모 임팩트**: 비기술 사용자 입장에서 "AI가 차트를 생성했다"는 경험 충분.

### Acceptance Criteria

**Level 1**:
- [ ] GenerativeUIRenderer 컴포넌트 구현 완료
- [ ] 8가지 이상의 컴포넌트 타입 렌더링 가능 (bar, line, pie, area, table, kpi, stat-grid, heatmap)
- [ ] 에이전트 프롬프트가 사용자 요청에서 올바른 컴포넌트 선택 (80% 이상 정확도)
- [ ] InsightModal에 Generative UI 렌더러 통합
- [ ] 컴포넌트별 데이터 검증 로직 (잘못된 형식 → 친절한 오류 메시지)
- [ ] 모든 생성 컴포넌트가 Liveboard의 반응형 레이아웃 적용 (드래그/리사이즈 가능)
- [ ] 에러 발생 시 Fallback UI (예: "차트를 렌더링할 수 없습니다. 데이터를 확인하세요.")
- [ ] NotificationContext로 "생성 중", "완료" 상태 표시

**Level 2** (선택사항, 나중):
- [ ] Declarative Spec 스키마 완성
- [ ] 동적 그리드 레이아웃 렌더러 구현
- [ ] 에이전트가 다중 컴포넌트를 포함한 스펙 생성 가능
- [ ] 생성된 대시보드가 Liveboard 그리드와 동등한 상호작용성 제공

---

## Key Considerations

### 에이전트 프롬프트 최적화

Static Pattern의 성패는 **에이전트가 올바른 컴포넌트를 선택하는 데 있다**. 따라서:

1. **구체적 가이드**: 단순히 "적절한 차트를 선택하세요"가 아니라, "시간 추이는 line-chart, 범주 비교는 bar-chart, 구성비는 pie-chart" 같이 명시적 매핑.
2. **예시 포함**: Few-shot prompting으로 사용자 입력 → 예상 컴포넌트 예시 제공.
3. **JSON 형식 강제**: Structured Output 형식으로 JSON 스키마 준수 강제 (Claude의 Tool Use, OpenAI의 Functions).

### 데이터 검증 및 안전성

에이전트가 생성한 데이터가 항상 정확하지 않을 수 있다:
- 잘못된 데이터 형식 (예: 숫자여야 할 필드가 문자열)
- 빈 데이터셋
- 범위 이탈 값

**대책**:
- 프론트엔드에서 엄격한 스키마 검증
- 유효하지 않은 데이터 → Fallback UI 렌더링
- 오류 로그 기록 (디버깅용)

### 사용자 반복 워크플로우

"이 차트를 조금 다르게 보여줄래?" 같은 재요청이 많을 것이다:
- Level 1: "옵션을 더 수정하고 싶으면 프롬프트를 다시 보내세요"
- Level 2: 생성된 컴포넌트의 수동 편집 UI 추가 (설정 패널 등)

현재는 Level 1 (재요청 전용)으로 충분.

### 다국어 및 로컬라이제이션

차트 라벨, 제목 등이 사용자 언어로 표시되어야 한다. 에이전트 프롬프트에 "사용자 언어: Korean"을 명시하여 생성되는 텍스트가 자동으로 한국어가 되도록.

### 성능 및 로딩 상태

Level 1에서는 에이전트 응답이 비교적 빠르지만(~1초), 대규모 데이터셋은 느릴 수 있다:
- 로딩 스피너 표시
- Progressive rendering (먼저 구조 표시 → 데이터 로드 → 렌더링)

### 커스터마이제이션 vs. 기본값

사용자가 생성 컴포넌트의 색상, 폰트 등을 커스터마이즈하고 싶을 수 있다. 이는 Level 1을 넘는 기능이므로, 향후 추가 고려.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Web Research | Vercel AI SDK 3.0: React Server Components + streamUI() 함수로 LLM 응답 스트리밍. Declarative 스펙을 부분 응답부터 즉시 렌더링. | declarative, rsc |
| 2026-02-15 | Web Research | Google Gemini Dynamic View: 자연어 질문 → Gemini 3 코드생성 → 동적 대시보드. 무상태(stateless) 접근. | open-ended, gemini |
| 2026-02-15 | Web Research | Claude Artifacts: Open-Ended 구현. iframe 샌드박스에서 실행. React, Tailwind, Shadcn, Lucide, Recharts 고정 라이브러리. | open-ended, artifacts |
| 2026-02-15 | Web Research | v0 by Vercel: Full-Stack 코드생성 + 원클릭 배포. 프로토타이핑 → 배포 완전 자동화. | open-ended, v0 |
| 2026-02-15 | Web Research | CopilotKit: Static/Declarative/Open-ended 모두 지원하는 프레임워크. AG-UI 프로토콜 기반 상호호환성. | framework, ag-ui |
| 2026-02-15 | Web Research | MCP Apps (Anthropic): MCP Tools의 반환값에 UI 메타데이터 포함. Declarative + Intent-Based. MCP 표준 준수. | declarative, mcp |
| 2026-02-15 | Web Research | Chainlit/Mesop/Gradio: Python 프레임워크. Static 컴포넌트 선택. 데이터 과학자/AI 개발자 친화적. | static, python |

---

## References

### Vault
- [^8]: KonaI-Agent 코드베이스 — `ChartWidgets.tsx` (Recharts), `LiveboardView.tsx` (react-grid-layout), `InsightModal.tsx`, `useScenarioOrchestration.ts`

### External
- [^1]: [Generative UI: Understanding Agent-Powered Interfaces | CopilotKit](https://www.copilotkit.ai/generative-ui) — 3가지 Generative UI 수준 정의 (Static, Declarative, Open-ended)
- [^2]: [The Three Types of Generative UI: Static, Declarative and Fully Generated | CopilotKit Blog](https://www.copilotkit.ai/blog/the-three-kinds-of-generative-ui) — 패턴별 깊이있는 분석
- [^3]: [The Developer's Guide to Generative UI in 2026 | CopilotKit Blog](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026) — 2026년 Generative UI 트렌드 및 표준화
- [^4]: [MCP Apps: Bringing UI Capabilities To MCP Clients | Model Context Protocol Blog](http://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) — MCP Apps 공식 발표, Declarative 접근
- [^5]: [Claude Artifacts: A Game-Changer Held Back by Frustrating Limits | Medium](https://medium.com/@intranetfactory/claude-artifacts-a-game-changer-held-back-by-frustrating-limits-6adcacdd95a7) — Claude Artifacts 오픈-엔디드 구현 분석
- [^6]: [v0 by Vercel: AI-Powered UI Generator | Refine](https://refine.dev/blog/vercel-v0/) — v0의 Full-Stack 코드생성 및 배포 자동화
- [^7]: [Introducing AI SDK 3.0 with Generative UI support - Vercel](https://vercel.com/blog/ai-sdk-3-generative-ui) — streamUI() 함수, React Server Components 기반 스트리밍
- [^8]: [Use visual layout or dynamic view in Gemini Apps | Google Support](https://support.google.com/gemini/answer/16741341) — Gemini Dynamic View, AI 코드생성 기반 동적 UI
- [^9]: [Mesop, Streamlit, Chainlit, and Gradio: A Comprehensive Comparison | AI Hive](https://www.ai-hive.net/post/mesop-streamlit-chainlit-and-gradio-a-comprehensive-comparison-of-ai-application-frameworks) — Python Generative UI 프레임워크 비교

---

*Last synthesized: 2026-02-15 | Review: auto-trigger (Recent Updates 7건 누적)*
