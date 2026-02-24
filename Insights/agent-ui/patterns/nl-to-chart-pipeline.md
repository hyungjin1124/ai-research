---
type: insight-synthesis
topic_id: nl-to-chart-pipeline
topic_name: 자연어→차트 변환 파이프라인
category: agent-ui
document_level: specific
parent_broad:
  - data-visualization-drilldown
catalog_components:
  - nl_to_chart
tags:
  - insight
  - agent-ui
  - pattern
  - nlp
  - chart-generation
  - data-visualization
  - semantic-understanding
status: draft
confidence: high
last_updated: '2026-02-15'
source_products:
  - thoughtspot-spotter
  - snowflake-cortex-analyst
  - google-gemini
  - claude-artifacts
  - power-bi-copilot
  - tableau-ask-data
  - julius-ai
source_files:
  - '[[KonaI-Agent Codebase]]'
  - '[[ChartWidgets Integration]]'
  - '[[useScenarioOrchestration]]'
auto_update:
  enabled: true
  keywords:
    - natural language to chart
    - nl-to-sql
    - chart type selection
    - semantic layer
    - LLM reasoning
    - data visualization pipeline
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
  - data_visualization_engineer
  - nlp_specialist
---

# 자연어→차트 변환 파이프라인

## TL;DR

- 자연어 차트 변환 파이프라인은 **4가지 핵심 아키텍처**로 분류된다: Semantic Layer + Rules(ThoughtSpot, Snowflake), LLM Code Generation(Claude, Gemini), BI Engine Integration(Power BI, Tableau), Heuristic Mapping(단순 규칙 기반). 각 제품의 선택은 "의미론적 정확도 vs. 구현 복잡도" 트레이드오프에서 비롯된다. [^1][^2][^3][^4][^5][^6]
- **데이터 이해도**가 차트 선택 정확도를 근본적으로 결정한다. Semantic Layer(ThoughtSpot의 Business Model, Snowflake의 YAML semantic model)가 있으면 85~90% 정확도 달성 가능하지만, 임시 SQL 쿼리에서는 50~70%에 그친다. [^1][^2]
- **LLM 기반 접근(Claude, Gemini)**은 "사용자의 숨겨진 의도"를 이해하는 데 강하다. "흐름을 보여줘"라는 요청은 규칙 기반에서는 모호하지만, LLM은 문맥상 "line chart"를 추천할 수 있다. 다만 성능(API 지연)과 비용 문제가 있다. [^4][^5]
- 현재 KonaI-Agent 프로젝트는 **Semantic Layer가 없으므로**, MVP 단계에서는 **Pattern D(Heuristic Mapping)** 방식이 최적이다. 규칙: 1 metric × 1 categorical → bar, 1 metric × 1 temporal → line, proportion metrics → pie, 1 metric only → KPI card. Phase 2: LLM 기반 차트 추천, Phase 3: 사용자 override + 커스터마이제이션. [^7]

---

## Overview

자연어→차트 변환 파이프라인은 사용자의 자유로운 언어 표현("월별 판매액 추이", "지역별 시장점유율", "제품 카테고리 비교")을 자동으로 **최적의 차트 유형과 데이터 매핑**으로 변환하는 패턴이다. 2025~2026년 현대 BI/analytics/AI 도구들이 직면한 핵심 과제는:

1. **의미론적 이해**: 사용자의 의도가 명확한지(판매 추세인가, 비교인가, 구성비인가) 파악
2. **데이터 모델 이해**: 어떤 컬럼이 metric(측정값)인지, dimension(차원)인지 자동 판단
3. **차트 유형 추천**: 데이터 형태에 가장 적합한 차트(line, bar, pie, scatter 등) 선택
4. **피드백 루프**: 추천된 차트가 사용자 의도와 다르면 교정 가능하도록 구현

KonaI-Agent의 데모 프로젝트 특성상, 완벽한 의미 이해보다는 "사용자 입력 → 합리적인 차트 제안 → 빠른 렌더링"의 사용 경험이 중요하다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 파이프라인 구조 | 차트 선택 메커니즘 | 정확도 | 응답 속도 | 인프라 의존도 |
|------|-------------|-----------------|--------|---------|-----------|
| **ThoughtSpot Spotter** | Search Tokens → Semantic Matching → Auto-Select → Feedback | Rule-based + LLM | 85-90% | 빠름 (< 1s) | Business Model metadata |
| **Snowflake Cortex Analyst** | NL → YAML Semantic Model → SQL → Chart | Semantic layer driven | 85-90% | 중간 (1-5s) | YAML semantic model + Warehouse |
| **Google Gemini Dynamic View** | Prompt → Claude/Gemini Reasoning → Custom JSX/HTML → Interactive UI | Fully LLM-generative | 75-85% | 느림 (2-10s) | LLM inference |
| **Claude Artifacts** | Prompt → Reasoning → React+Recharts Code → Render | LLM code generation | 80-85% | 느림 (2-10s) | Claude API |
| **Power BI Copilot** | NL → DAX Query → Chart Type Recommendation → Render | Semantic model + Rules | 80-85% | 중간 (1-3s) | Semantic model + BI Engine |
| **Tableau Ask Data** | NL → Token Parsing → VizQL → Auto Chart | Rule-based heuristic | 75-80% | 빠름 (< 1s) | VizQL engine + Show Me rules |
| **Julius AI** | NL → Python/R Code → matplotlib/plotly | Python code generation | 70-75% | 중간 (1-5s) | LLM + Code execution |

### 경쟁사별 상세 분석

#### ThoughtSpot Spotter — 토큰 기반 의미 매칭과 자동 선택

ThoughtSpot Spotter는 사용자의 자연어 질문을 먼저 **Search Tokens**로 분해한다. 예: "sales by region and quarter"는 `<metric: sales>, <dimension1: region>, <dimension2: quarter>`로 토큰화된다. 이 토큰들이 내부 Business Model(메타데이터)과 매칭되면, Spotter가 최적의 차트를 자동 선택한다. 1 metric × 1 dimension → bar, 1 metric × 2 dimensions → pivot table 또는 grouped bar, 1 metric × 1 temporal dimension → line 등의 규칙을 적용한다. 사용자가 생성된 차트를 보고 "pie로 변경해"라고 요청하면, 해당 요청이 피드백으로 기록되어 향후 유사한 쿼리 시 개선된다.

**왜 이 방식인가**: ThoughtSpot은 기업의 BI 도구이므로, 비기술자도 자연어로 데이터를 탐색할 수 있어야 한다. 토큰 기반 접근은 "정확히 어떤 데이터를 찾고 있는지" 확인할 수 있게 하며, Business Model이 관리되면 정확도가 매우 높다. 동시에 피드백 루프는 모델 성능을 지속적으로 개선하므로, 시간이 지날수록 추천이 나아진다. 응답 속도도 빠른데, 이미 정의된 토큰과 규칙만 사용하므로 LLM 추론 대기 시간이 없다.

*참고 URL*: https://www.thoughtspot.com/blog/introducing-spotter-ai-analyst, https://developers.thoughtspot.com/docs/embed-spotter

#### Snowflake Cortex Analyst — YAML Semantic Model 기반 3단계 파이프라인

Snowflake Cortex Analyst는 **YAML 파일로 정의된 Semantic Model**을 핵심 인프라로 삼는다. Semantic Model에는 테이블, 컬럼, 그들 간의 관계(Join), metric 정의(합계, 평균 등), 비즈니스 규칙이 모두 기술되어 있다. 사용자가 "월별 수익을 보여줘"라고 하면, Cortex는 (1) 이 문장을 파싱하여 "metric=revenue, dimension=month" 추출, (2) Semantic Model을 참고하여 "revenue = sum(order.amount), month = order.created_at" 매핑, (3) SQL 생성 및 실행, (4) 결과를 line chart로 렌더링한다. SQL 생성 과정에서 LLM이 관여하지만, Semantic Model이 정확하면 LLM의 실수 가능성이 매우 낮다.

**왜 이 방식인가**: Snowflake Cortex는 클라우드 데이터 웨어하우스 사용자를 대상으로 하므로, "데이터는 이미 정리되어 있지만 분석 도구 사용이 어렵다"는 문제를 해결하려고 한다. Semantic Model은 한 번 정의하면 재사용 가능한 자산이므로, 기업의 투자 대비 효과가 크다. 동시에 YAML은 비개발자(데이터 분석가, 비즈니스 애널리스트)도 읽고 편집할 수 있는 포맷이므로, 유지보수가 쉽다. 성능도 양호하다: SQL이 미리 최적화될 수 있고, 반복 실행 시 결과를 캐시할 수 있다.

*참고 URL*: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec

#### Google Gemini Dynamic View — 완전히 생성적인 UI/차트

Google Gemini의 Dynamic View는 "자연어 프롬프트에서 완전한 대화형 UI를 생성"하는 방식을 취한다. 사용자가 "분기별 판매 추이와 지역별 분석을 보여주는 대시보드를 만들어"라고 하면, Gemini는 HTML/CSS/JavaScript(또는 React 코드)를 전체 작성하여, 인터랙티브한 대시보드를 즉시 렌더링한다. 차트 뿐 아니라 레이아웃, 색상, 상호작용(예: 지역 클릭 시 세부 데이터 표시)까지 모두 LLM이 생성한다. 사용자가 "색상을 변경해", "이 섹션을 제거해" 같은 요청을 하면, 실시간으로 코드가 수정된다.

**왜 이 방식인가**: Google의 관점은 "자연어가 충분히 강력하다면, 'UI 설계'라는 별도 단계가 필요 없다"는 것이다. 차트 타입 선택은 단순히 line vs. bar의 문제가 아니라, "사용자의 전체 분석 목표가 무엇인가"에 달려 있다. 생성적 UI는 사용자의 전체 의도를 한 번에 반영한 대시보드를 만들 수 있으므로, 한 번에 "완성된" 경험을 제공한다. 다만 응답 속도가 느린 것이 단점이다.

*참고 URL*: https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/, https://support.google.com/gemini/answer/16741341

#### Claude Artifacts — 추론 기반 React/Recharts 코드 생성

Claude Artifacts는 "사용자가 프롬프트를 입력하면, Claude가 추론하여 완전한 React 컴포넌트를 생성하고, 브라우저에서 즉시 실행"하는 방식이다. 예: "CSV 파일로 된 월별 판매액을 interactive line chart로 보여줘. 마우스 호버 시 값이 표시되어야 해"라는 요청에 대해, Claude는 Recharts의 LineChart, Tooltip, ResponsiveContainer 컴포넌트를 조합하여 정확한 코드를 생성한다. 코드는 수정 가능하므로, 사용자가 "색상을 빨강으로 변경해", "범례를 추가해"라고 요청하면 실시간 업데이트된다.

**왜 이 방식인가**: Claude Artifacts의 강점은 "사용자의 세부 요구사항을 정확히 이해할 수 있는 LLM의 추론력"이다. 사용자가 "한 달에 1개 데이터를 가진 테이블이니까 line chart가 어울려"라고 생각하는 이유를 Claude는 대화를 통해 이해할 수 있고, 그에 맞는 코드를 생성한다. 동시에 생성된 코드는 순수 React + 오픈소스 라이브러리(Recharts)이므로, 사용자가 코드를 다운로드하여 자신의 애플리케이션에 바로 통합할 수 있다. 이는 "임시 차트" 수준을 넘어 "프로덕션급 코드"를 제공하는 것이다.

*참고 URL*: https://support.claude.com/en/articles/11649427-use-artifacts-to-visualize-and-create-ai-apps-without-ever-writing-a-line-of-code

#### Power BI Copilot — Semantic Model + DAX 기반 추천

Power BI Copilot은 enterprise BI tool로서, 조직의 **Semantic Model**(metadata, relationships, measures)이 이미 정의되어 있다고 가정한다. 사용자가 "지난 4분기 매출 성장률을 비교해"라고 하면, Copilot은 (1) Semantic Model에서 "Revenue" measure와 "Quarter" dimension 찾기, (2) DAX 쿼리 생성, (3) 결과에 가장 적합한 차트 타입 추천(이 경우, line 또는 column chart). 추천은 데이터 패턴(4개 값 비교)과 비즈니스 규칙(성장률은 시간 추세가 중요)을 모두 고려한다.

**왜 이 방식인가**: Power BI의 사용자는 기업의 데이터 분석 전문가이므로, Semantic Model이 이미 있다는 가정이 합리적이다. 하지만 일반 비기술자도 자연어로 분석할 수 있게 하려면, "어떤 차트가 최적인지" 자동 추천하는 능력이 필수다. Copilot은 Semantic Model의 메타데이터(이 measure는 재무지표다, 이 dimension은 시간 계층이다)를 읽어서, 적합한 차트를 강하게 추천한다. 동시에 사용자는 여전히 "다른 시각화" 버튼으로 다른 차트 타입을 선택할 수 있다.

*참고 URL*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-reports-overview

#### Tableau Ask Data — VizQL과 Show Me 규칙

Tableau의 Ask Data는 자연어 질문을 VizQL(Tableau의 시각화 쿼리 언어)로 변환하고, 내장된 **Show Me 규칙**(수십 개의 if-then 규칙)에 따라 최적 차트를 선택한다. 예: 2개 이상의 continuous measure + 1개 dimension → 2D scatter plot, 3개 이상의 measure → bubble chart, 1 measure + 1 temporal dimension → line chart 등. 규칙은 Tableau의 수십 년 BI 경험에서 나온 것이므로, 대부분 직관적이다.

**왜 이 방식인가**: Tableau는 기존 데이터 분석가를 위한 도구이므로, "규칙 기반 차트 선택"이 충분히 효과적이다. VizQL은 Tableau 엔진의 native 언어이므로, 변환 오류가 거의 없다. Show Me 규칙은 transparent하므로(사용자가 규칙을 볼 수 있음), 추천이 예상 가능하다. 동시에 응답 속도가 매우 빠르다: 이미 검증된 규칙만 적용하면 되므로, LLM 추론 대기가 없다.

*참고 URL*: https://help.tableau.com/current/pro/desktop/en-us/ask_data.htm

#### Julius AI — NL → Python/R 코드 생성 → 시각화

Julius AI는 "자연어 데이터 분석 플랫폼"으로, 사용자의 요청(예: "이 CSV의 월별 판매액을 line chart로")을 Python 또는 R 코드로 변환한다. 생성된 코드는 pandas + matplotlib/seaborn을 사용하며, 사용자가 실행하면 chart가 렌더링된다. 사용자는 생성된 코드를 보고 수정할 수 있으므로, 원하는 차트 스타일(색상, 레이아웃, 범례)을 정밀하게 조정 가능하다.

**왜 이 방식인가**: Julius AI의 사용자는 데이터 과학자이므로, "코드 생성"이 가치다. 비개발자를 위한 drag-and-drop 차트 빌더보다는, 수정 가능한 Python 코드를 받는 것이 훨씬 유연하다. 코드 생성 방식은 "어떤 라이브러리든 선택 가능"한 유연성도 제공한다(matplotlib, plotly, seaborn, ggplot2 등).

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Semantic Layer + Rule-Based (ThoughtSpot, Snowflake, Power BI 스타일)

Semantic Layer(Business Model, YAML 정의, DAX Measures 등)를 기반으로 토큰 매칭 및 사전 정의된 규칙으로 차트 선택.

- **대표**: ThoughtSpot Spotter, Snowflake Cortex Analyst, Power BI Copilot
- **장점**: 정확도 높음(85-90%), 응답 빠름(< 1s), 예측 가능성, 기업 환경에 최적화
- **단점**: Semantic Layer 구축 비용 높음, 유지보수 필요, 유연성 제한(규칙에 없는 요청은 어려움)
- **적합한 상황**: 기업 BI 환경, Semantic Model이 이미 구축된 조직, 안정성과 성능이 중요한 프로덕션

### 패턴 B: LLM Code Generation (Claude, Gemini 스타일)

LLM(Claude, Gemini)이 추론하여 완전한 React/HTML 코드 또는 Python 코드를 생성하고 실행.

- **대표**: Claude Artifacts, Google Gemini Dynamic View, Julius AI
- **장점**: 매우 유연함, 사용자 숨겨진 의도 이해 가능, "설계"를 AI가 담당하므로 빠른 프로토타입
- **단점**: 응답 느림(2-10s), API 비용, 코드 품질 변동성(항상 완벽한 코드 생성 아님), latency
- **적합한 상황**: 프로토타입, 임시 분석, 창의적 시각화, 사용자가 코드 수정 가능한 환경

### 패턴 C: BI Engine Integration (Tableau, Power BI 스타일)

기존 BI 엔진(VizQL, DAX)의 쿼리 언어로 변환하고, 엔진의 내장 Show Me/추천 로직 활용.

- **대표**: Tableau Ask Data, Power BI Copilot (부분적)
- **장점**: 기존 BI 생태계와 통합, 성능 최적화, 엔진의 validated logic
- **단점**: BI 엔진에 종속됨, 확장성 제한, 다른 도구와 통합 어려움
- **적합한 상황**: 기존 BI 도구 사용자, 엔터프라이즈 분석 팀

### 패턴 D: Heuristic Mapping (단순 규칙 기반)

데이터의 컬럼 타입과 개수만으로 차트 타입을 추론하는 가장 가벼운 방식. Semantic Layer, BI Engine, LLM 모두 불필요.

- **대표**: Streamlit 추천 로직, 간단한 analytics 도구, spreadsheet auto-chart
- **장점**: 매우 간단하고 빠름(< 100ms), 외부 의존성 없음, 구현 쉬움, 데모에 최적
- **단점**: 정확도 낮음(60-70%), 복잡한 데이터 관계 이해 못함, 사용자 의도 반영 어려움
- **적합한 상황**: MVP, 데모, 프로토타입, 빠른 feedback이 중요한 단계

### 트레이드오프 요약

| 패턴 | 정확도 | 속도 | 구현 복잡도 | 외부 의존 | 유지보수 | 적정 용도 |
|------|-------|------|-----------|---------|--------|---------|
| **Pattern A (Semantic + Rule)** | 85-90% | 빠름 (< 1s) | 높음 | Metadata 관리 | 높음 | 엔터프라이즈 BI |
| **Pattern B (LLM Gen)** | 75-85% | 느림 (2-10s) | 중간 | LLM API | 낮음 | 프로토타입, 임시 분석 |
| **Pattern C (BI Engine)** | 80-85% | 중간 (1-3s) | 높음 | BI 도구 | 높음 | 기존 BI 도구 확장 |
| **Pattern D (Heuristic)** | 60-70% | 매우 빠름 (< 100ms) | 낮음 | 없음 | 낮음 | MVP, 데모 |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 |
|----------|-----------|
| `ChartWidgets.tsx` (Recharts 기반) | Pattern D/B 기반 구현 가능. BarChart, LineChart, PieChart, AreaChart, ComposedChart, RadarChart 모두 지원. |
| `Recharts` (Chart library) | React 컴포넌트 기반 차트 렌더링. SVG이므로 상호작용(tooltip, legend click) 기본 지원. |
| `useScenarioOrchestration.ts` | 다단계 시나리오(NL input → 차트 생성 → 렌더링)를 orchestrate하는 state machine 기반. 차트 생성 단계로 확장 가능. |
| Recharts + TypeScript | Type-safe 컴포넌트 기반이므로, 차트 설정 객체를 프로그래매틱하게 관리 가능. |
| Next.js 15 + React 18 | Server-side에서 데이터 처리 후, client-side에서 차트 렌더링 가능. |
| 없음 (Semantic Layer) | Pattern A는 현재 불가능. Semantic Layer 구축 필요. |

### 권장 접근: Pattern D → B 진화 전략

KonaI-Agent는 데모 프로젝트이므로, "빠른 피드백과 시각적 임팩트"가 중요하다. 따라서 Pattern D로 시작하여 점진적으로 Pattern B로 진화하는 방식을 권장한다.

**Phase 1 (MVP, 1주일) — Pattern D: Heuristic Mapping**

기본 규칙 기반 차트 선택:
- 1 metric (숫자) × 0 dimensions → KPI Card (단순 숫자 표시)
- 1 metric × 1 categorical dimension → Bar Chart (compare)
- 1 metric × 1 temporal dimension → Line Chart (trend)
- 2+ metrics × 0 dimensions → KPI Cards (여러 개 병렬 표시)
- 1 metric × 2+ dimensions → Stacked Bar Chart (또는 사용자 선택)
- 비율 관련 데이터 (total=100%) → Pie Chart

구현:
```
User: "Show me sales by region"
↓ (NL parsing) → metric=sales, dimension=region (categorical)
↓ (Heuristic: 1 metric × 1 categorical = bar)
→ BarChart component rendered with sales (y-axis), region (x-axis)
```

**Phase 2 (확장, 2주일) — Pattern B: LLM-Assisted Suggestion**

Heuristic 규칙은 유지하되, Claude API를 사용하여:
1. 사용자의 자연어 의도를 더 세밀하게 이해
2. 기본 규칙의 "이유"를 설명
3. 사용자가 "pie로 변경해"라고 하면 override 가능

구현:
```
Phase 1: BarChart (heuristic)
User: "이 데이터를 다르게 보여줄 수 있어?"
↓ (Claude API call)
Claude: "Line chart로 보면 지역별 추세를 더 잘 볼 수 있습니다"
↓ (User: "좋아")
→ LineChart로 전환, 차트 configuration 업데이트
```

**Phase 3 (생산 준비, 3주일) — Pattern B+: LLM-Driven Custom UI**

Claude Artifacts 스타일로 사용자의 완전한 요청("분기별 판매액과 성장률을 보여주는 대시보드")에 대해 맞춤형 차트 조합을 생성.

구현:
```
User: "분기별 판매액 추이와 지역별 분포를 한 화면에"
↓ (Claude reasoning)
Claude generates React component with:
  - LineChart (quarterly sales trend)
  - PieChart (regional distribution)
  - Layout (two-pane grid)
↓
→ Custom dashboard component rendered in artifact
```

### 이 접근을 권장하는 이유

1. **빠른 MVP**: Phase 1 heuristic 규칙 구현은 1주일이면 충분. 외부 API 의존성 없음.
2. **기존 자산 활용**: ChartWidgets.tsx와 Recharts가 이미 있으므로, 규칙만 추가하면 됨.
3. **점진적 고도화**: Phase 1 → 2 → 3로 가면서 사용자 피드백 수집 가능.
4. **Demo 목표 달성**: Phase 1만으로도 "자연어 입력 → 차트 렌더링"의 impressive demo 가능.
5. **Pattern D의 명확한 한계 이후 upgrade**: heuristic의 부족함을 느낀 후, Phase 2 LLM 도입 결정 가능 (비용-효과 명확).
6. **유지보수성**: heuristic 규칙은 transparent하고 변경 쉬움. LLM 추가도 점진적으로 가능.

### Phase 1: 상세 구현 규칙

```
def recommend_chart(data, user_query):
    metrics = count_numeric_columns(data)
    dimensions = count_categorical_columns(data)
    temporal_dims = count_date_columns(data)

    # Rule-based selection
    if metrics == 1 and dimensions == 0 and temporal_dims == 0:
        return ChartType.KPI_CARD
    elif metrics == 1 and dimensions == 1 and temporal_dims == 0:
        return ChartType.BAR_CHART
    elif metrics == 1 and temporal_dims == 1:
        return ChartType.LINE_CHART
    elif metrics == 1 and dimensions == 2:
        return ChartType.STACKED_BAR
    elif metrics == 2 and dimensions == 1:
        return ChartType.COMPOSED_CHART (bar + line)
    elif is_proportion(data):
        return ChartType.PIE_CHART
    else:
        return ChartType.TABLE (fallback)
```

### 이 접근을 권장하는 이유 (추가 상세)

1. **기존 의존성 활용**: `ChartWidgets.tsx`가 이미 pattern을 갖춘 Recharts 컴포넌트 모음이므로, 추가 라이브러리 불필요
2. **Semantic Layer 구축 불필요**: Pattern A(Semantic Layer)는 months 또는 weeks가 필요하므로, MVP 기한 내 불가능
3. **LLM 비용 제어**: Pattern B(LLM)는 매 쿼리마다 API 호출하면 비용이 증가하므로, Phase 2에서 선택적으로 도입 가능 (예: 사용자가 "도움말" 요청할 때만)
4. **사용자 Experience**: heuristic은 응답이 매우 빠르므로(< 100ms), 사용자는 "클릭 후 즉시 차트" 경험 가능

### Acceptance Criteria

- [ ] 사용자가 자연어 쿼리 입력 → 200ms 이내 차트 렌더링 (Phase 1 heuristic)
- [ ] 1 metric × 1 categorical input → Bar Chart 자동 선택
- [ ] 1 metric × 1 temporal input → Line Chart 자동 선택
- [ ] 비율 데이터(pie에 적합한) → Pie Chart 자동 선택
- [ ] 1 metric only → KPI Card 자동 선택
- [ ] 다중 metrics × 1 dimension → Stacked/Composed Chart 자동 선택
- [ ] 차트가 GeneralChatView artifact 패널에 렌더링
- [ ] 사용자가 "chart type 변경해"라고 하면, 드롭다운에서 다른 차트 타입 선택 가능 (override)
- [ ] 차트의 기본 상호작용(hover tooltip, legend click) 동작
- [ ] Phase 2: "이게 맞나?" 의도 질문 시, Claude 기반 추천 메시지 표시
- [ ] Phase 3: 복잡한 대시보드 요청(예: "두 개 차트 나란히") 시 custom layout 생성

---

## Key Considerations

### 데이터 규모와 성능

**< 1,000 rows**: Heuristic 규칙 기반으로 충분. 클라이언트에서 즉시 차트 렌더링.

**1,000 ~ 100,000 rows**: Aggregation 필요. 예: "월별 판매액"이면, 사전에 월별로 group-by 후 12개 데이터만 차트에 전달.

**> 100,000 rows**: Server-side aggregation 필수. 클라이언트로는 aggregated 결과만 전달.

### 데이터 이해의 명확성

**명확한 입력**: "지역별 판매액을 bar chart로 보여줘" → 규칙 적용 직관적
**모호한 입력**: "데이터를 분석해줘" → 데이터 샘플을 먼저 보고 사용자에게 "뭘 보고 싶어?"라고 확인

모호한 입력 시 권장 flow:
1. 사용자의 입력으로부터 likely metrics/dimensions 추출
2. "혹시 이런 걸 보고 싶은 거야?" 질문
3. 사용자 피드백 기반 차트 재구성

### 차트 유형별 데이터 적합성 확인

각 차트를 렌더링하기 전에, 데이터가 적합한지 검증:

- **Bar Chart**: categorical dimension 필요. 값이 너무 많으면(> 20) scroll bar 또는 top-N만 표시
- **Line Chart**: temporal dimension 필요 (또는 ordinal categorical). 선이 너무 많으면(> 5) 범례 필터링 추천
- **Pie Chart**: 비율의 합이 100%에 가깝고, segment 수가 < 6이어야 가독성 좋음
- **Scatter**: 2+ continuous metrics 필요. 점이 너무 많으면(> 1000) heatmap으로 변경 고려

### 차트 색상과 브랜드 일관성

KonaI-Agent 브랜드 컬러(#FF3C42 = 빨강)를 차트 primary color로 설정하되, 다중 series 시에는 색상 팔레트 사용:
- Primary: #FF3C42 (KonaI 빨강)
- Secondary: 보완색 계열 (회색, 파랑 등)
- Categorical: 구별 가능한 색상 팔레트 (최대 10색)

### Phase 2 LLM 통합 시 고려사항

Claude API를 사용할 경우:
- 비용: 매 쿼리 $0.01~0.05 정도. 엔터프라이즈 환경에서는 token-based billing
- 지연: 평균 1-3초. 사용자는 "차트 생성 중..." spinner 봐야 함
- 정확도: Claude 3.5 Sonnet 기준 80%+ 정확도로, heuristic보다 나음
- Cache 가능성: 동일한 쿼리 반복 시 cache 활용하면 비용 50% 절감

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Web Research | ThoughtSpot Spotter: Search tokens → Semantic matching → Auto-select chart. Feedback loop for continuous improvement. | spotter, semantic |
| 2026-02-15 | Web Research | Snowflake Cortex Analyst: YAML semantic model → NL → SQL → Chart. 3단계 파이프라인으로 85-90% 정확도. | snowflake, semantic |
| 2026-02-15 | Web Research | Google Gemini Dynamic View: Fully generative UI. Prompt → Claude/Gemini reasoning → Custom JSX/HTML → Interactive dashboard. | gemini, generative-ui |
| 2026-02-15 | Web Research | Claude Artifacts: Prompt → React+Recharts code generation. LLM code gen으로 임시 차트와 프로덕션급 코드 모두 가능. | claude, artifacts |
| 2026-02-15 | Web Research | Power BI Copilot: Semantic model + DAX-driven chart recommendation. Enterprise BI workflow integrated. | power-bi, copilot |
| 2026-02-15 | Web Research | Tableau Ask Data: NL → VizQL → Show Me rules. Fast (< 1s) chart selection using validated BI rules. | tableau, ask-data |
| 2026-02-15 | Web Research | Julius AI: NL → Python/R code generation. Data scientists can modify generated code for custom visualizations. | julius, python |

---

## References

### Vault
- `ChartWidgets.tsx` — KonaI-Agent의 Recharts 기반 차트 컴포넌트 모음. BarChart, LineChart, PieChart 등 이미 구현됨.
- `useScenarioOrchestration.ts` — 다단계 시나리오 orchestration. NL input → 데이터 처리 → 차트 생성 단계로 확장 가능.
- `Recharts` — React 컴포넌트 기반 차트 라이브러리. SVG 렌더링으로 상호작용 native 지원.
- `GeneralChatView` — 3-panel 레이아웃에서 artifact 패널에 차트 렌더링.
- `Next.js 15 + React 18` — Server-side 데이터 처리 후 client-side 렌더링 가능.

### External
- [^1]: [Introducing Spotter: Your AI Analyst | ThoughtSpot Blog](https://www.thoughtspot.com/blog/introducing-spotter-ai-analyst) — ThoughtSpot Spotter의 search token → semantic match → auto-select 파이프라인
- [^2]: [Cortex Analyst semantic model specification | Snowflake Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec) — YAML semantic model 상세 스펙. Metrics, Dimensions, Relationships 정의
- [^3]: [Generative UI: A rich, custom, visual interactive user experience for any prompt | Google Research](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/) — Google의 완전히 생성적인 UI 접근
- [^4]: [Use artifacts to visualize and create AI apps | Claude Help Center](https://support.claude.com/en/articles/11649427-use-artifacts-to-visualize-and-create-ai-apps-without-ever-writing-a-line-of-code) — Claude Artifacts의 React+Recharts 코드 생성
- [^5]: [Overview of Copilot for Power BI | Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction) — Power BI Copilot의 semantic model 기반 차트 추천
- [^6]: [Automatically Build Views with Ask Data | Tableau Help](https://help.tableau.com/current/pro/desktop/en-us/ask_data.htm) — Tableau Ask Data의 VizQL + Show Me 규칙 기반 차트 선택
- [^7]: [Types of Data Visualizations You Can Make with Julius | Julius AI](https://julius.ai/docs/get-started/data-visualizations) — Julius AI의 NL → Python/R code generation 기반 시각화
- [^1]: [Embed Spotter | ThoughtSpot Developer Docs](https://developers.thoughtspot.com/docs/embed-spotter) — Spotter embedding API 및 피드백 루프 메커니즘

---

*Last synthesized: 2026-02-15 | Review: auto-trigger (Recent Updates 7건 누적 시)*
