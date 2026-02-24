---
type: insight-synthesis
topic_id: drilldown-interaction-design
topic_name: 드릴다운 인터랙션 상세 설계
category: agent-ui
document_level: specific
parent_broad:
  - data-visualization-drilldown
catalog_components:
  - drill_down
tags:
  - insight
  - agent-ui
  - pattern
  - drill-down
  - interaction-design
  - data-exploration
  - hierarchical-navigation
status: draft
confidence: high
last_updated: '2026-02-15'
source_products:
  - thoughtspot
  - power-bi
  - tableau
  - looker
  - metabase
  - sigma-computing
  - google-gemini
source_files:
  - '[[ThoughtSpot vs Tableau vs Power BI 비교]]'
  - '[[BI 도구 네비게이션 패턴]]'
auto_update:
  enabled: true
  keywords:
    - drill-down
    - drill-through
    - hierarchical drill
    - drill-anywhere
    - data exploration
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
  - ui-designer
  - analytics-engineer
---

# 드릴다운 인터랙션 상세 설계

## TL;DR

- **드릴다운은 2가지 철학으로 나뉜다**: (1) Hierarchical Drill-Down(연도→분기→월 같은 사전정의 경로), (2) Drill-Anywhere(ThoughtSpot, Sigma Computing — 클릭한 데이터에서 자유롭게 어떤 차원이든 추가 가능). 전자는 제어되고 성능 우수, 후자는 유연하지만 UX 복잡도 높음. [^1][^2]
- **Drill-Through vs Drill-Down의 구분**이 중요하다. Drill-Down은 같은 시각화 내에서 더 상세 수준으로 진행, Drill-Through는 현재 필터 컨텍스트를 유지하며 다른 대시보드/보고서로 이동. Power BI와 Looker는 이 둘을 명확히 구분하며, Tableau는 선택적 드릴 업/다운으로 통합. [^3][^4]
- **Cross-Filter Drill(클릭 한 차트가 다른 모든 차트를 필터링)**은 현대 BI의 표준이 되었다. Metabase의 자동 X-ray, Sigma Computing의 Cross-Element Filter는 드릴-다운과 함께 탐색 경험을 완성. [^5][^6]
- **AI-Driven Drill(자연어 기반)**은 ThoughtSpot의 SpotIQ, Google Gemini Dynamic View 같은 최신 경향. Generative UI를 활용하여 다음 단계의 드릴 방향을 AI가 제안하거나, 자연어 질문으로 드릴을 진행. [^7]
- KonaI-Agent의 기존 3-level 드릴-다운(LiveboardView → DetailDashboard → InsightModal)은 **Hierarchical Pattern의 정형화된 구현**이다. 현재 상태는 프로덕션 기반이며, 향후 Cross-Filter와 AI-Suggested 확장이 로드맵 대상. [^8]

---

## Overview

드릴다운 인터랙션 설계는 분석 대시보드에서 "집계된 고수준(Year) 데이터에서 시작하여 상세 수준(Day)으로 탐색하는 경험"을 어떻게 구현할 것인가의 문제다. 2025~2026년 현재, BI/Analytics 업계는 두 가지 방향으로 진화 중이다:

1. **구조화된 계층 구조 기반 드릴다운**: Power BI, Tableau, Looker 같은 전통 BI는 데이터 모델에 정의된 계층(Year → Quarter → Month → Day)을 따라 드릴을 진행. 이는 **예측 가능하고 성능 최적화되어 있지만, 사전정의된 경로만 가능**.

2. **자유로운 탐색(Drill-Anywhere)**: ThoughtSpot, Sigma Computing은 임의의 차원으로 드릴을 진행할 수 있게 허용. "Year로 집계된 매출을 클릭하면 Region으로 분석" 같은 사전에 정의되지 않은 경로도 가능. **유연성은 높지만 UI/성능 설계 복잡도 증가**.

KonaI-Agent 프로젝트는 데모 및 내부 분석 도구로서, 기존의 정형화된 3-level 계층 구조를 **베스트 프랙티스로 강화**하면서, 향후 AI-Driven 제안(다음 분석 추천)으로 확장할 여지를 남기는 것이 전략적으로 가장 적절하다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 드릴 방식 | 계층 구조 유형 | 네비게이션 | Cross-Filter | AI 제안 | 드릴-Through |
|------|---------|-------------|----------|-----------|--------|------------|
| **ThoughtSpot** | Drill-Anywhere (자유) | 데이터 모델 기반 + 자유 추가 | Breadcrumb + Back Button | 자동 동기화 | SpotIQ 이상 감지 기반 | Limited |
| **Power BI** | Hierarchical Drill-Down | 사전정의 계층 (Year→Quarter→Month) | Drill Up/Down 버튼 + Expand All | Yes (선택적) | None | Yes (명시적 설정) |
| **Tableau** | Hierarchical Drill-Down | 사전정의 + 선택적 Set Actions | 계층 아이콘 클릭 + Breadcrumb | Yes (Set Actions) | None | Yes (Parameters) |
| **Looker** | LookML-Defined Drill Path | 명시적 drill_fields 정의 | Link Parameter + Breadcrumb | Yes (Dashboard Filters) | None | Yes (drill-to-dashboard) |
| **Metabase** | Click-to-Filter + X-ray | 자동 검색 + 사용자 정의 | Drill Menu (우측 클릭/버튼) | Yes (자동) | X-ray 자동 생성 | Limited |
| **Sigma Computing** | Drill-Anywhere (자유) | 그룹화 컬럼 + 자유 차원 추가 | 컨텍스트 메뉴 + Breadcrumb | Yes (Cross-Element Filter) | None | None |
| **Google Gemini Dynamic View** | AI-Driven Drill | AI 코드생성으로 동적 구성 | 자연어 질문 + Interactive UI | Dynamic | AI 생성 | AI 생성 |

### 경쟁사별 상세 분석

#### ThoughtSpot — Drill-Anywhere (자유 탐색) + SpotIQ AI

ThoughtSpot는 **Liveboards(대시보드)와 AI Insights에서 완전한 Drill-Anywhere를 지원**한다. 사용자가 어떤 데이터 포인트든 클릭하면, 컨텍스트 메뉴가 나타나 "Region으로 드릴", "Store로 드릴" 같은 **동적 옵션이 자동 생성**된다. 이는 사전정의된 계층 구조가 아니라, **현재 집계 수준과 사용 가능한 모든 차원의 조합**으로부터 생성된다. [^1]

**SpotIQ** 이상 감지 기능은 드릴다운 경험을 한 단계 더 강화한다. 사용자가 차트를 클릭하면 ThoughtSpot은 자동으로 데이터 패턴 분석을 수행하고, "이 Region에서 매출이 특이하게 낮습니다. 이유는 X입니다"라는 AI 인사이트를 제시한다. 이는 사용자가 다음 질문을 스스로 생성할 필요 없이 AI가 탐색 방향을 제안하는 것.

**왜 이 방식인가**: ThoughtSpot의 핵심 포지셍은 "민주화된 데이터 탐색(Democratized Analytics)"이다. BI 전문가가 아닌 비즈니스 사용자도 제약 없이 데이터를 탐색할 수 있어야 하기에, 드릴 경로를 사전에 정의하지 않는다. 대신 Liveboards(웹 기반)에서 실시간 렌더링으로 성능 비용을 감수한다. [^2]

#### Power BI — Hierarchical Drill-Down + Drill-Through

Power BI는 **사전정의된 계층 구조(Hierarchy)**를 핵심으로 한다. 데이터 모델러가 Year, Quarter, Month, Day를 순차적으로 필드 섹션에 드래그하여 계층을 구성하면, 사용자는 각 시각화에 "Drill Down" 버튼(아래 화살표)과 "Drill Up" 버튼(위 화살표)을 사용하여 계층을 따라 이동한다. 예: (2024 매출 → Q1 매출 → January 매출 → Day-by-Day). [^3]

**Expand All** 기능은 Power BI의 고유한 특징이다. 일반 Drill-Down은 한 계층만 내려가지만, Expand All은 현재 수준을 유지하면서 다음 계층을 트리 구조로 펼쳐 모든 자식 요소를 보여준다. 이는 "연도별 분석은 유지하면서 각 연도 내 분기별 세부를 한눈에 보고 싶을 때" 유용하다.

**Drill-Through**는 별도의 메커니즘이다. 요약 보고서의 특정 셀을 클릭하면, 필터 컨텍스트(예: Year=2024)가 유지되면서 상세 보고서 페이지로 네비게이션된다. 사용자가 매출 서머리에서 "2024년 세부사항 보기"를 클릭하면 2024 데이터만 필터된 상세 보고서가 열리는 것.

**왜 이 방식인가**: Power BI는 엔터프라이즈 BI 플랫폼으로서, **예측 가능성과 성능을 최우선**으로 한다. 계층을 사전정의함으로써 쿼리 최적화(캐싱, 쿼리 파라미터화)가 가능하고, 사용자는 "다음 단계가 명확하다"는 심리적 안정감을 얻는다. Drill-Through는 두 분석 간의 명시적 연결고리를 제공하여 보고서 아키텍처를 단순하게 유지한다. [^3]

#### Tableau — Hierarchical Drill + Set Actions + Parameters

Tableau는 Power BI와 유사하게 **계층 구조를 사용**하지만, **Set Actions과 Parameter Actions**를 통해 더 유연한 크로스-필터링을 지원한다. [^4]

계층 기반 드릴은 Power BI와 거의 같다. 하지만 Tableau의 차별화는 "클릭 → Set 값 변경 → 다른 시각화 필터링"의 메커니즘이다. 예를 들어, 지역 지도에서 특정 지역을 클릭하면 Set {SelectedRegion}이 업데이트되고, 이 Set을 참조하는 모든 다른 차트(제품별 매출, 월별 추이 등)가 즉시 필터링된다. 이는 드릴-다운을 넘어 **전체 대시보드의 동적 상호작용**으로 확장된다.

**왜 이 방식인가**: Tableau는 "Visual Analytics" 철학으로, 사용자가 여러 시각화를 조합하여 인사이트를 발견하는 경험을 중시한다. Set Actions으로 시각화 간 연결을 명시적으로 구성하면, 대시보드 설계자가 어떤 상호작용을 허용할지 의도적으로 제어할 수 있다. 동시에 사용자는 한 차트의 클릭이 전체 대시보드에 미치는 영향을 직관적으로 이해한다. [^4]

#### Looker — LookML-Defined Drill Path + Drill-to-Dashboard

Looker는 **LookML(데이터 모델 언어)에서 drill_fields 파라미터로 명시적 드릴 경로를 정의**한다. 예: drill_fields: [dimension1, dimension2, dimension3]. 사용자가 차트의 셀을 클릭하면, LookML에 정의된 순서대로 다음 드릴 단계가 결정된다. [^5]

**Drill-to-Dashboard는 Looker의 고유 기능**이다. drill_fields에 대시보드 이름을 지정하면, 클릭 시 해당 대시보드로 네비게이션되며, 클릭한 셀의 값이 필터로 자동 전달된다. 또한 "link" 파라미터를 사용하여 LookML이 아닌 외부 URL로도 드릴을 설정할 수 있다.

**왜 이 방식인가**: Looker는 BI 엔지니어/데이터 팀이 주 사용자이다. LookML에서 드릴 경로를 명시적으로 정의함으로써, (1) 성능 예측 가능성, (2) 데이터 보안(무단 드릴 방지), (3) 비즈니스 로직 중앙 집중화를 달성한다. 엔터프라이즈 환경에서 "어떤 드릴도 가능하다"는 자유도보다 "정의된 경로만 가능하다"는 통제가 더 중요하다. [^5]

#### Metabase — Click-to-Filter + Auto-Generated X-rays

Metabase는 **그래픽 쿼리 빌더로 자동 생성된 드릴 기능**을 제공한다. 사용자가 차트의 데이터 포인트를 클릭하면, **Action Menu**가 나타나 여러 드릴 옵션을 제시한다:
- 시간 기간 Zoom In (e.g., Year → Month → Day)
- 카테고리별 Breakout (e.g., 전체 매출 → Region별 매출)
- 개별 레코드 조회

**X-ray 기능은 AI 기반의 자동 리포트 생성**이다. 어디든 클릭하면 Metabase가 해당 데이터 세트에 대해 자동으로 다양한 시각화(히스토그램, 트렌드, 분포 등)를 생성하고 대시보드 형태로 제시한다. 사용자는 "다음에 뭘 봐야 할까?"라는 질문에 AI가 자동으로 대답하는 경험을 한다.

**왜 이 방식인가**: Metabase는 "No-code Analytics"를 표방한다. 일반 비즈니스 사용자가 쿼리를 작성하지 않고도 대시보드를 생성하고 탐색해야 한다. 따라서 드릴 옵션도 자동으로 제안되어야 하고, X-ray는 탐색의 다음 단계를 AI가 자동 제안하는 기능으로서 완벽한 no-code 철학의 구현이다. [^6]

#### Sigma Computing — Drill-Anywhere (자유) + Cross-Element Filter

Sigma Computing은 **스프레드시트 인터페이스에서 Drill-Anywhere를 구현**한다. 사용자가 테이블 셀을 클릭하면 컨텍스트 메뉴가 나타나, 사용 가능한 모든 차원으로 드릴할 수 있다. 예: (Region 집계 → Store 드릴 → Product 드릴). 이는 **사전정의된 계층 없이** 데이터 모델의 모든 차원을 자유롭게 탐색하는 것. [^7]

**Grouped Columns**는 Sigma의 계층 구조 표현 방식이다. "Year" 컬럼을 Grouped로 설정하면, 그 안에 Quarter, Month, Day가 Tree 구조로 중첩되어 나타난다. 사용자는 클릭으로 그룹을 펼쳤다 접었다 하며 탐색한다.

**Cross-Element Filter**는 "한 요소(트리거)의 클릭이 다른 요소(타겟)를 필터링"하는 메커니즘이다. 예: 지도에서 Region을 클릭 → 모든 차트가 해당 Region으로 필터링. 이는 "드릴-다운"과 "크로스-필터"를 통합한 인터랙션 모델이다.

**왜 이 방식인가**: Sigma Computing은 "Collaborative Analytics"를 강조한다. 스프레드시트 친숙성으로 비기술 사용자도 쉽게 사용하지만, 동시에 고급 사용자에게 자유로운 탐색을 제공한다. Drill-Anywhere로 사전정의된 경로 제약을 제거하면서도, Cross-Element Filter로 대시보드 수준의 상호작용을 간단하게 구현한다. [^7]

#### Google Gemini Dynamic View — AI-Generated Interactive Drill-Down

Google Gemini Dynamic View는 **Generative UI를 활용한 차세대 드릴다운 경험**을 제시한다. 사용자가 자연어 질문("2024년 매출 현황을 분석해줄래?")을 하면, Gemini 3 모델이 코드를 생성하여 **그 질문에 최적화된 대시보드를 동적으로 구성**한다. [^8]

이 대시보드 내에서 사용자가 "이 지역 세부 정보를 보고 싶어"라고 다시 질문하면, Gemini가 새로운 대시보드를 다시 생성한다. 즉, **드릴다운이 쿼리-응답-새로운 쿼리의 반복 사이클**이 된다. 각 드릴 단계마다 UI가 재구성되므로, 고정된 계층 구조나 사전정의된 경로가 필요 없다.

**왜 이 방식인가**: Generative UI는 "에이전트가 UI를 생성한다"는 패러다임이다. 드릴다운의 미래는 "사용자가 다음 분석을 직접 설계하는 것"이 아니라 "자연어로 의도를 표현하면 AI가 차트, 필터, 레이아웃을 자동 구성"하는 방향으로 진화하고 있다. [^8]

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Hierarchical Drill-Down (계층 기반 드릴)

사전정의된 계층 구조(Year → Quarter → Month → Day)를 따라 단계별로 더 상세 수준으로 진행하는 패턴.

- **대표**: Power BI (계층 마법사), Tableau (계층 아이콘), Looker (drill_fields)
- **장점**:
  - 성능 최적화 가능 (사전 계획된 쿼리)
  - 사용자가 "다음 단계"를 명확히 인식
  - 데이터 보안/거버넌스 강화 (정의된 경로만 접근)
  - 구현 복잡도 낮음
- **단점**:
  - 유연성 제약 (사전정의 경로만 가능)
  - "Year → Region"처럼 계층 순서와 다른 탐색 불가
  - 새로운 계층 추가 시 모델 재설계 필요
- **적합한 상황**: 엔터프라이즈 BI, 규제 산업 (금융/의료), 성능이 중요한 대규모 데이터셋

### 패턴 B: Drill-Anywhere (자유 탐색 드릴)

사전정의된 계층 없이, 클릭한 데이터 포인트에서 사용 가능한 모든 차원으로 자유롭게 드릴을 진행하는 패턴.

- **대표**: ThoughtSpot, Sigma Computing
- **장점**:
  - 최고의 탐색 유연성 (모든 차원 조합 가능)
  - 새로운 분석 방향을 제약 없이 발견
  - 사용자가 예상하지 못한 인사이트 추출 가능
  - 데이터 모델 변경에 덜 취약
- **단점**:
  - 성능 예측 어려움 (쿼리 최적화 제한)
  - 사용자가 "올바른" 다음 단계를 선택해야 함 (인지 부하 증가)
  - 데이터 보안: 무제한 접근으로 인한 위험
  - 구현 복잡도 높음 (동적 컨텍스트 메뉴 생성 등)
- **적합한 상황**: 현대 클라우드 BI (ThoughtSpot, Sigma), 데이터 분석가의 자유로운 탐색이 필요한 경우

### 패턴 C: Cross-Filter Drill (크로스필터 연동 드릴)

한 시각화의 클릭이 전체 대시보드의 다른 시각화를 필터링하는 상호작용을 드릴과 함께 제공하는 패턴.

- **대표**: Tableau (Set Actions), Sigma Computing (Cross-Element Filter), Metabase (Click-to-Filter)
- **장점**:
  - 단일 드릴이 아닌 전체 대시보드 상황 인식
  - "한 번의 클릭"으로 여러 시각화 동시 업데이트
  - 대시보드 내 인사이트 비교 용이
  - 사용자가 "연관 관계"를 시각적으로 이해
- **단점**:
  - 대시보드 설계 복잡도 증가 (필터 연결 관리)
  - 과도한 필터링으로 인한 "데이터 부족" 가능성
  - 필터 로직이 비직관적일 경우 혼동 유발
- **적합한 상황**: 다중 차원 분석이 필요한 대시보드, 엔드유저 셀프 서비스 분석

### 패턴 D: AI-Driven Drill Suggestion (AI 추천 드릴)

다음 드릴 방향을 사용자가 선택하는 것이 아니라, AI가 데이터 패턴 분석을 통해 제안하는 패턴.

- **대표**: ThoughtSpot SpotIQ, Metabase X-ray, Google Gemini Dynamic View
- **장점**:
  - 사용자가 "탐색 방향 결정"의 인지 부하 제거
  - AI가 이상 감지(anomaly)를 기반으로 다음 분석 제시
  - 새로운 인사이트 발견 확률 증가
  - 진입 장벽 낮음 (비전문가도 사용 가능)
- **단점**:
  - AI 제안이 항상 정확하지 않음
  - 사용자가 "원하는 것"과 "AI 제안"이 맞지 않을 수 있음
  - 설명 가능성 부족 (왜 이 드릴을 제안했는가?)
  - 계산 비용 높음 (실시간 패턴 분석)
- **적합한 상황**: 자기 주도 분석(Self-Service Analytics), 대시보드 발견(Dashboard Discovery), 비전문가 데이터 접근

### 트레이드오프 요약

| | 유연성 | 성능 | 사용 용이성 | 구현 복잡도 | 거버넌스 | 데모 임팩트 |
|---|---|---|---|---|---|---|
| **Hierarchical** | 낮음 | 높음 | 높음 | 낮음 | 높음 | 중간 |
| **Drill-Anywhere** | 최고 | 중간 | 중간 | 높음 | 낮음 | **높음** |
| **Cross-Filter** | 중간 | 중간 | 중간 | 중간 | 중간 | 높음 |
| **AI-Driven** | 높음 | 낮음 | 최고 | 높음 | 낮음 | **최고** |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 | 확장 방향 |
|----------|-----------|---------|
| `LiveboardView.tsx` (84KB) — 10개 위젯 그리드, react-grid-layout | 현재 3-level 드릴-다운의 기반. 각 위젯이 클릭 가능한 차트. | Level 1에 그대로 사용. 향후 Drill-Anywhere 전환 시 위젯별 동적 차원 렌더링 필요 |
| `DetailDashboard.tsx` — 2단계 드릴-다운 차트 + 컨텍스트 정보 | 계층 2단계(Liveboard → DetailDashboard)의 구현. breadcrumb으로 돌아가기 제공. | Breadcrumb 강화: 각 단계별 필터 상태 명시, 모든 단계로 즉시 점프 가능하게 |
| `InsightModal.tsx` — 3단계 AI 인사이트 + 구조화된 분석 | 3-level 계층의 최종 단계. AI-Generated 인사이트 표시. | AI 제안 확장: "다음 분석 추천" 섹션 추가. 사용자가 추천을 클릭 → 그 방향으로 드릴 진행 |
| `ChartWidgets.tsx` (Recharts 기반) | 각 드릴 레벨의 시각화 렌더링. BarChart, LineChart, PieChart 등. | 클릭 핸들러 강화: 임의의 데이터 포인트 클릭 감지 → 드릴 또는 필터 액션 트리거 |
| `react-grid-layout` | 위젯 드래그/리사이즈 | Cross-Filter Drill 구현 시, 위젯 간 "클릭-필터링 연결" 시각화 가능 |
| `NotificationContext` — 글로벌 알림 | 드릴 진행 상태 알림 (예: "Region으로 드릴 중...") | 드릴 애니메이션/로딩 상태 표시에 활용 |
| `useScenarioOrchestration.ts` — 멀티스텝 시나리오 | 드릴 과정을 "시나리오"의 단계로 모델링 가능 | 드릴 경로를 시나리오 단계로 추상화 → "어떤 드릴 경로인가"를 명시적으로 기술 |

### 권장 접근: Phase 1 (Validate) → Phase 2 (Enhance) → Phase 3 (Expand)

**Phase 1: 현재 3-Level Hierarchical 검증 및 표준화 (1~2주)**

기존 LiveboardView → DetailDashboard → InsightModal 3-level 구조는 **Pattern A (Hierarchical Drill-Down)의 정형화된 구현**이다. 현재 상태:
- (Level 1) Liveboard: 10개 위젯, 각 위젯은 집계 수준(예: "연도별 매출")
- (Level 2) DetailDashboard: 필터된 차트(예: "2024년 지역별 매출")
- (Level 3) InsightModal: 가장 상세 수준(예: "2024년 서울 매출 세부 데이터")

**할 일**:
1. 각 레벨 간 계층 구조 명시적 정의 (어떤 필터가 다음 레벨로 전달되는가?)
2. Breadcrumb UI 강화:
   - 현재: 단순 "← 돌아가기" 버튼
   - 개선: "Liveboard > 2024 > Seoul" 형태로 경로 표시, 각 단계 클릭으로 즉시 이동
3. 각 단계에서 "Reset" 옵션 추가 (Liveboard로 돌아가기)
4. 드릴 진행 로그 기록 (사용자 탐색 이력 추적)

**Phase 2: Cross-Filter Drill 추가 (2~3주)**

Liveboard 내 위젯 간 상호작용 추가. 예:
- 좌측 "지역 맵" 위젯 클릭 → 우측 "제품별 매출" 위젯이 해당 지역으로 필터링
- 구현: `react-grid-layout` 위젯 메타데이터에 "filter source/target" 관계 정의

**할 일**:
1. LiveboardView에서 위젯 간 클릭 이벤트 구독/발행 메커니즘 추가
2. 각 차트 위젯에 클릭 핸들러 추가 (ChartWidgets.tsx 확장)
3. 필터 전파 로직 (NotificationContext 활용)
4. UI: 필터 관계를 시각적으로 표시 (예: 연결선 또는 하이라이팅)

**Phase 3: AI-Suggested Drill 추가 (3~4주, 선택사항)**

InsightModal에서 "다음 분석 추천" 섹션 추가. InsightModal이 AI-generated 인사이트를 표시할 때, 추천되는 다음 드릴 방향도 함께 제시.

예: InsightModal에서 "2024년 서울 매출이 전년 동기 대비 -15% 감소했습니다. 다음으로 확인할 사항: (1) 제품별 추이 분석, (2) 일별 판매량 추세" 같은 AI 제안

**할 일**:
1. useScenarioOrchestration에서 AI 추천 드릴 인텐션(intent) 생성
2. InsightModal에 "추천 드릴" 카드 렌더링
3. 추천 카드 클릭 → 해당 방향으로 자동 드릴

### 이 접근을 권장하는 이유

1. **기존 코드 최대 활용**: 현재 3-level 구조를 그대로 두고 개선하므로 리팩토링 비용 최소화
2. **데모 완성도**: Phase 1-2 완료만으로도 "계층적 드릴-다운 + 크로스 필터"라는 현대 BI의 핵심 패턴 구현
3. **AI 통합 용이**: Phase 3은 기존 InsightModal의 기능 확장으로, 자연스럽게 AI-Driven 경험 추가
4. **점진적 복잡도**: 각 Phase가 독립적으로 가치 제공하므로 필요 시 Phase 2에서 멈춰도 완전한 기능
5. **성능/거버넌스**: Hierarchical 베이스이므로 성능 최적화(쿼리 캐싱) 및 보안(접근 제어) 구현 용이

### Acceptance Criteria

- [ ] Phase 1: Breadcrumb이 전체 드릴 경로를 "Liveboard > 필터1 > 필터2" 형태로 표시
- [ ] Phase 1: Breadcrumb의 각 단계를 클릭하면 해당 레벨로 즉시 이동 (뒤로/앞으로 네비게이션 불필요)
- [ ] Phase 1: "Reset" 버튼으로 Liveboard로 돌아가기 가능
- [ ] Phase 1: 각 드릴 단계에서 "다른 방향으로 드릴" 옵션 표시 (Context Menu 또는 Sidebar)
- [ ] Phase 2: Liveboard 내 두 개 이상의 위젯이 Cross-Filter 관계로 연결
- [ ] Phase 2: 한 위젯을 클릭하면 관련 위젯의 데이터가 실시간 필터링됨 (로딩 인디케이터 표시)
- [ ] Phase 2: 필터 관계를 시각적으로 명확히 표시 (숨겨진 로직 아님)
- [ ] Phase 3 (선택): InsightModal에 "추천 드릴" 섹션이 있으며, 추천 항목을 클릭하면 드릴 진행
- [ ] 전체: 3-level 드릴 내내 성능 저하 없음 (각 단계 로딩 < 500ms)

---

## Key Considerations

### 성능 vs. 유연성

KonaI-Agent는 데모 프로젝트이므로, **실시간 데이터 쿼리 성능이 매우 중요**하다. Phase 1의 Hierarchical 베이스를 선택한 이유다. 하지만 향후 Phase 3에서 AI-Driven drill을 추가할 때는 "매 드릴 단계마다 AI 분석 수행"이 필요하므로, 백엔드 최적화(비동기 쿼리, 캐싱)를 함께 고려해야 한다.

### 대시보드 설계의 "올바른" 드릴 경로

Hierarchical Drill은 데이터 설계자(모델러)가 "이 드릴 경로가 분석적으로 의미 있다"고 판단한 경로만 제공한다. 예: Year → Region → Product는 의미 있지만, Year → Store → Customer는 과도할 수 있다. KonaI-Agent의 Liveboard → DetailDashboard → InsightModal 구조도 "어떤 차원을 첫 번째 드릴로 할 것인가"를 명시적으로 설계해야 한다. 이는 비즈니스 로직에 해당하므로, 위젯별 메타데이터에 "드릴 가능한 차원"을 정의하는 방식을 권장한다.

### 모바일/반응형 고려

Breadcrumb과 Cross-Filter 인터랙션은 데스크톱 기준으로 설계되기 쉽다. 모바일에서는:
- Breadcrumb: 가로 스크롤 또는 "드롭다운" 형태로 표현
- Cross-Filter: 터치 친화적 피드백 (길게 눌러 필터 정보 보기 등)

현재 KonaI-Agent의 타겟이 데스크톱 데모라면, 모바일 고려는 Phase 4+로 미루는 것이 합리적이다.

### 드릴 실패 시나리오

"선택된 필터 조건에 데이터가 없음" 같은 Edge Case를 처리해야 한다. 예: "2024년 특정 Store의 매출"을 드릴하려 했으나 해당 Store에 2024년 매출 기록이 없는 경우. 이 경우:
1. 사용자에게 알림 표시 ("이 필터 조건에 해당하는 데이터가 없습니다")
2. 이전 레벨로 자동 복귀 또는 수동 Breadcrumb 클릭으로 복귀
3. "유사한 대안 데이터 보기" 제시 (AI 제안 활용)

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Web Research | ThoughtSpot Drill-Anywhere + SpotIQ: 자유 탐색 + AI 이상 감지 기반 다음 단계 제안. Liveboards에 AI 인사이트 통합. | drill-anywhere, thoughtspot |
| 2026-02-15 | Web Research | Power BI Hierarchical Drill + Expand All: 사전정의 계층 (Year→Quarter→Month)을 따라 진행. Expand All로 계층 유지하며 세부 표시. Drill-Through로 다른 보고서로 이동. | hierarchical, power-bi |
| 2026-02-15 | Web Research | Tableau Set Actions + Parameter Actions: 계층 기반 + Set Actions로 크로스 필터 연동. 클릭 → Set 값 변경 → 다른 시각화 필터링. | hierarchical, tableau |
| 2026-02-15 | Web Research | Looker LookML drill_fields + Drill-to-Dashboard: LookML에서 명시적 드릴 경로 정의. Drill-to-Dashboard로 다른 대시보드로 네비게이션 (필터 유지). | lookml, looker |
| 2026-02-15 | Web Research | Metabase Click-to-Filter + X-ray: 자동 생성된 드릴 옵션 (Zoom In, Breakout, Record). X-ray로 자동 리포트 생성. | auto-drill, metabase |
| 2026-02-15 | Web Research | Sigma Computing Drill-Anywhere + Grouped Columns + Cross-Element Filter: 스프레드시트 인터페이스에서 자유 드릴. 그룹화 컬럼으로 계층 표현. 크로스-요소 필터로 대시보드 상호작용. | drill-anywhere, sigma |
| 2026-02-15 | Web Research | Google Gemini Dynamic View: 자연어 질문 → AI 코드생성 → 동적 대시보드 구성. 각 드릴 단계마다 UI 재생성. Generative UI 기반 미래 트렌드. | ai-driven, gemini |

---

## References

### Vault
- [^8]: KonaI-Agent 코드베이스 — `LiveboardView.tsx` (3-level drill-down 기반), `DetailDashboard.tsx`, `InsightModal.tsx`, `react-grid-layout`

### External
- [^1]: [Tableau vs ThoughtSpot: 2026 Comparison | Luzmo](https://www.luzmo.com/blog/thoughtspot-vs-tableau) — ThoughtSpot Drill-Anywhere 철학과 Liveboards 아키텍처
- [^2]: [Generative UI: A rich, custom, visual interactive user experience for any prompt | Google Research](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/) — 일반화된 드릴-다운 경험
- [^3]: [Drill Down and Up in Power BI Explained - RADACAD](https://radacad.com/drill-down-and-up-in-power-bi-explained/) — Power BI 계층 기반 드릴-다운, Expand All 기능
- [^4]: [How to build a hierarchy to support drill mode in Microsoft Power BI - TechRepublic](https://www.techrepublic.com/article/how-to-build-hierarchy-support-drill-mode-microsoft-power-bi/) — 계층 구조 정의 및 drill-through 메커니즘
- [^5]: [drill_fields (for fields) | Looker | Google Cloud Documentation](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) — Looker LookML drill_fields 파라미터, drill-to-dashboard
- [^6]: [Drill-throughs | Metabase](https://www.metabase.com/features/drill-through) — Metabase 자동 드릴 옵션, X-ray 자동 생성 리포트
- [^7]: [Drill down into data - Sigma Documentation](https://help.sigmacomputing.com/docs/drill-into-data) — Sigma Computing Drill-Anywhere, Grouped Columns, Cross-Element Filter
- [^8]: [Use visual layout or dynamic view in Gemini Apps | Google Support](https://support.google.com/gemini/answer/16741341) — Google Gemini Dynamic View, AI 코드 생성 기반 동적 UI 구성

---

*Last synthesized: 2026-02-15 | Review: auto-trigger (Recent Updates 7건 누적)*
