---
type: insight-synthesis
topic_id: interactive-table-design
topic_name: 인터랙티브 데이터 테이블 설계
category: agent-ui
document_level: specific
parent_broad:
  - data-visualization-drilldown
catalog_components:
  - interactive_table
tags:
  - insight
  - agent-ui
  - pattern
  - data-visualization
  - table-design
  - sorting-filtering
status: draft
confidence: high
last_updated: '2026-02-15'
source_products:
  - airtable
  - notion
  - thoughtspot
  - retool
  - streamlit
  - ag-grid
  - chatgpt
source_files:
  - '[[KonaI-Agent Codebase]]'
  - '[[tanstack-react-table]]'
  - '[[Recharts Integration]]'
auto_update:
  enabled: true
  keywords:
    - interactive table
    - data grid
    - sorting
    - filtering
    - column operations
    - virtual scrolling
  feeds: []
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
  - data_visualization_engineer
---

# 인터랙티브 데이터 테이블 설계

## TL;DR

- 인터랙티브 테이블은 **5가지 핵심 상호작용 방식**으로 분류된다: Grid View(Airtable, Notion), Kanban/Gallery View(Airtable), Drill-Down Table(ThoughtSpot), Server-Side Pagination(Retool), Virtual Scrolling(AG Grid). 제품마다 선택한 패턴은 "데이터 규모와 사용자 개입 수준"에 따라 결정된다. [^1][^2][^3]
- **렌더링 방식**이 대규모 데이터(10k+ rows) 성능을 근본적으로 결정한다. DOM 기반 전체 렌더링은 구현이 간단하지만 1M row에서는 불가능하고, Virtual Scrolling(AG Grid)은 billions row 스케일까지 확장 가능하지만 복잡도가 높다. [^4][^5]
- **사용자 제어 수준**이 UI 복잡도를 좌우한다. Airtable/Notion의 다중 뷰(Grid, Kanban, Gallery, Calendar)는 동일 데이터를 다양한 관점으로 보여주되, 각 뷰별 독립 필터/정렬 상태를 유지한다. [^1][^2]
- 현재 KonaI-Agent 프로젝트는 `@tanstack/react-table`(이미 dependencies에 존재)을 기반으로 하므로, **Pattern D(Lightweight Rendered Table)** 방식이 MVP에 최적이다. Phase 1: 기본 정렬/필터/export 구현, Phase 2: 다중 정렬 + 컬럼 조작(resize/hide), Phase 3: 다중 뷰 모드 추가. [^6]

---

## Overview

인터랙티브 테이블 설계는 데이터 기반 대시보드와 분석 UI의 핵심 인터페이스 패턴으로, 사용자가 대규모 데이터셋을 탐색·조작·분석할 수 있게 한다. 2025~2026년 현대 BI/analytics/spreadsheet 도구들의 공통 특징은 단순한 "읽기 전용 표" 수준을 벗어나 다음을 모두 지원한다는 점이다:

1. **상호작용 깊이**: 기본 정렬/필터에서 인라인 편집, 드래그 리사이즈, 드릴다운까지 다단계 지원
2. **뷰 다양성**: 동일 데이터를 Grid, Kanban, Calendar, Gallery 등 다중 뷰로 표현
3. **확장성**: 데이터 규모에 따라 DOM 기반에서 Virtual Scrolling으로 자동 대응
4. **결과 내보내기**: CSV, Excel, JSON 등 다양한 포맷 지원

KonaI-Agent의 데모 프로젝트 특성상, 모든 기능을 구현할 필요는 없지만, 최소한의 상호작용(정렬/필터/export)과 확장 가능한 아키텍처를 갖춰야 한다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 핵심 상호작용 | 렌더링 방식 | 대규모 데이터 대응 | 다중 뷰 | 인라인 편집 | 관계 기능 |
|------|-------------|-----------|-----------------|--------|-----------|---------|
| **Airtable** | Grid/Kanban/Gallery/Calendar view switching | DOM-based (각 뷰별) | Pagination + Lazy Load | 4가지 기본 뷰 | 지원 | Relations & Rollups |
| **Notion** | Table/Board/Timeline/Calendar/Gallery view | DOM-based (뷰별 상태 독립) | Pagination + Lazy Load | 8가지 뷰 | 지원 | Two-way Relations |
| **ThoughtSpot** | Drill-anywhere table, dynamic aggregation | DOM-based + Canvas viz | Virtual Scroll (100k+ rows) | Table ↔ Chart 전환 | 제한적 | Drill-down hierarchy |
| **Retool** | Server-side pagination, column config, bulk edit | Server-driven (pagination) | Server-side handling | Table ↔ Form 전환 | 지원 | Custom columns, JavaScript |
| **Streamlit** | st.dataframe column config, sorting, filtering | DOM-based (전체 렌더) | Pagination (기본) | 제한적 | 지원 | 컬럼별 설정 |
| **AG Grid** | Virtual scrolling, column groups, pivoting, grouping | Virtual Scroll (이중) | Billions of rows | 제한적 (programmatic) | 지원 | Server-side Row Model |
| **ChatGPT** | Artifact canvas table, editable inline | React-based DOM | No handling | 1개 (Table) | 지원 | 없음 |

### 경쟁사별 상세 분석

#### Airtable — 다중 뷰(Grid, Kanban, Gallery, Calendar) 패턴

Airtable은 단일 Base와 Table 내의 데이터를 **5가지 이상의 서로 다른 뷰**로 표현한다. Grid View는 전통적인 스프레드시트 형태로 컬럼별 정렬/필터, Kanban View는 단일 선택 필드를 기준으로 카드를 열 단위로 정렬, Gallery View는 각 레코드를 카드 형태로 표시하며 이미지 포함 가능, Calendar View는 날짜 필드를 기준으로 일정을 표시한다. 각 뷰는 독립적인 필터, 정렬, 그룹화 상태를 유지하므로, 사용자가 Grid에서 필터를 적용한 후 Kanban으로 전환해도 해당 필터가 유지된다. 모든 뷰에서 인라인 편집이 가능하고, 변경사항은 즉시 모든 뷰에 반영된다.

**왜 이 방식인가**: Airtable의 핵심 가치는 "비기술자도 데이터베이스처럼 사용 가능한 스프레드시트"이다. 다중 뷰는 동일 데이터를 관점에 따라 다르게 보여줌으로써, 기술 배경이 다른 팀원들(PM은 Calendar로 일정 추적, 영업은 Kanban으로 파이프라인 관리, 분석가는 Grid로 상세 데이터 검토)이 각자의 워크플로우를 유지하면서도 동일 데이터베이스를 공유할 수 있게 한다. 뷰 전환의 빠른 응답성(Canvas 렌더링 없음)과 각 뷰별 독립 상태 관리는 가볍고 빠른 경험을 제공한다.

*참고 URL*: https://support.airtable.com/docs/getting-started-with-airtable-kanban-views, https://www.softr.io/blog/airtable-views

#### Notion — 8가지 뷰 + 양방향 Relations

Notion은 Airtable의 뷰 개념을 더 확장하여 Table, Board, Timeline, Calendar, List, Gallery, Chart, Feed 등 **8가지 뷰**를 제공한다. 각 뷰는 필터, 정렬, 그룹화, 숨기기 등을 독립적으로 설정할 수 있으며, 뷰별로 표시할 프로퍼티를 다르게 설정 가능하다. 특히 관계형 데이터를 다루기 위해 Relations 필드를 지원하는데, 양방향 관계를 설정하면 두 데이터베이스 간 변경사항이 자동 동기화된다. 인라인 편집, Rollup(집계), 그룹화 시 소계 표시 등이 모두 데이터베이스 뷰 내에서 구현된다.

**왜 이 방식인가**: Notion은 "프로젝트 관리, CRM, 재무 추적, 데이터 분석" 등 다양한 워크플로우를 하나의 도구로 지원해야 하므로, 뷰의 다양성이 핵심 차별화 요소이다. 양방향 Relations은 실제 관계형 데이터베이스의 JOIN을 간단한 UI로 구현한 것으로, 비기술자도 복잡한 데이터 모델을 구축할 수 있게 한다. Timeline 뷰는 Gantt 스타일의 프로젝트 관리에, Chart 뷰는 간단한 집계 시각화에, List 뷰는 상세 레코드 보기에 각각 최적화되어 있다.

*참고 URL*: https://www.notion.com/help/intro-to-databases, https://www.notion.com/help/relations-and-rollups

#### ThoughtSpot — Drill-Anywhere 테이블과 동적 드릴다운

ThoughtSpot의 테이블은 "먼저 뭘 드릴다운할지 미리 정의하지 않는" 접근법을 채택한다. 사용자가 테이블의 **어떤 셀이든 우클릭**하면 해당 값을 기준으로 필터를 적용하여 하위 데이터를 탐색할 수 있다. 예를 들어, "지역별 판매액" 테이블에서 "서울" 셀을 드릴다운하면, 서울의 상세 거래 데이터로 자동 전환된다. 드릴다운 경로는 사전에 정의되지 않으므로, 사용자는 자유롭게 데이터를 탐색할 수 있다. 동시에 테이블 헤더의 드래그로 컬럼을 재정렬하거나 숨길 수 있으며, 다중 컬럼 정렬도 지원한다.

**왜 이 방식인가**: ThoughtSpot의 핵심은 "BI 도구인데 비기술자도 사용 가능"한 것이다. 드릴다운 경로를 미리 정의하는 것은 분석가의 가정(이 경로로만 탐색할 거야)을 강제하므로, "데이터를 자유롭게 탐색하고 싶은" 사용자의 필요를 충족하지 못한다. Drill-Anywhere 방식은 테이블의 모든 값이 진입점이 될 수 있으므로, 탐색 가능성이 극대화된다. 동시에 드릴다운 시 자동 집계/필터링은 백엔드에서 처리하므로, 사용자는 "클릭하면 나타난다"는 것만 알면 된다.

*참고 URL*: https://docs.thoughtspot.com/cloud/10.10.0.cl/search-drill-down

#### Retool — 서버 사이드 페이지네이션과 대량 편집

Retool은 저코드 플랫폼으로 개발자가 쉽게 데이터 테이블을 구성할 수 있도록 하는 "Table" 컴포넌트를 제공한다. 특징은 **서버 사이드 페이지네이션**(매 페이지 로드 시 쿼리 실행), 커스텀 컬럼 추가(JavaScript 표현식), 다중 행 선택 후 대량 편집, 컬럼별 데이터 포맷(날짜, 통화, 이미지 등) 설정이다. 개발자가 "행 클릭 시" 또는 "셀 편집 시" 같은 이벤트를 JavaScript로 처리할 수 있어, 매우 유연한 상호작용 정의가 가능하다.

**왜 이 방식인가**: Retool은 "기업의 내부 도구"를 빠르게 만드는 저코드 플랫폼이므로, 대규모 데이터셋(수백만 행)을 모두 클라이언트로 로드할 수 없다. 서버 사이드 페이지네이션을 기본으로 제공하면, 개발자는 백엔드 데이터베이스 쿼리만 정의하면 되고, 테이블 렌더링은 Retool이 자동 처리한다. 커스텀 컬럼과 이벤트 핸들러는 개발자 유연성을 극대화한다.

*참고 URL*: https://docs.retool.com (Retool Table 컴포넌트 공식 문서)

#### AG Grid — Virtual Scrolling, Column Groups, Pivoting

AG Grid는 "엔터프라이즈급 데이터 그리드" 라이브러리로, **이중 virtual scrolling**(행과 열 모두)을 구현하여 billions row 데이터셋을 초 단위로 렌더링한다. 동시에 Column Groups(계층적 컬럼 헤더), Column Pivoting(엑셀 피벗 테이블 스타일), Row Grouping(데이터별 그룹화 및 소계), Server-Side Row Model(서버에서만 데이터 정렬/필터, 클라이언트는 보이는 부분만 처리) 등 고급 기능을 제공한다. Community 버전은 기본 기능만, Enterprise 버전은 고급 기능을 포함한다.

**왜 이 방식인가**: AG Grid의 목표는 "성능 손실 없이 모든 스프레드시트 고급 기능을 웹에 구현하는 것"이다. Virtual Scrolling은 DOM 노드 수를 최소화하므로, 1M row를 로드해도 화면에 보이는 50행만 DOM에 유지된다. rowBuffer 설정(기본값 10)으로 스크롤 시 부드러움도 유지한다. Column Groups와 Pivoting은 보고서 작성 시 자주 필요한 기능이므로, 이를 라이브러리 수준에서 지원하면 개발 시간을 대폭 단축할 수 있다.

*참고 URL*: https://www.ag-grid.com/javascript-data-grid/scrolling-performance/, https://www.ag-grid.com/javascript-data-grid/column-groups/

#### Streamlit — st.dataframe과 컬럼 설정

Streamlit은 Python 데이터 분석 도구로, `st.dataframe()`으로 pandas DataFrame을 표시한다. 기본적으로 정렬, 필터, 컬럼 드래그 리사이즈를 지원하고, 2024년부터는 `st.data_editor()`로 셀 편집도 가능해졌다. 컬럼별 데이터 타입 설정(숫자, 문자, 날짜, 이미지 등), 조건부 포맷팅, 컬럼 표시/숨기기 등을 Python 코드로 정의할 수 있다.

**왜 이 방식인가**: Streamlit의 사용자는 데이터 과학자/분석가이므로, "복잡한 UI 코드 없이 데이터를 빠르게 시각화하고 상호작용"하기 원한다. `st.dataframe()`은 Python dict/list를 바로 테이블로 렌더링할 수 있어, 프로토타입 단계에서 매우 효율적이다. 동시에 컬럼 설정으로 데이터 타입을 명시하면, 사용자의 의도(이 열은 날짜다, 이 열은 통화다)가 UI에 반영되어 가독성이 향상된다.

#### ChatGPT — Artifact Canvas 테이블과 인라인 편집

ChatGPT는 Artifacts 기능으로 사용자의 프롬프트에 따라 React 컴포넌트를 생성한다. 테이블의 경우, 사용자가 "CSV 데이터를 테이블로 보여줘"라고 요청하면, ChatGPT는 React + Tailwind CSS로 테이블 컴포넌트를 작성하고 Artifact Canvas에 렌더링한다. 테이블은 정렬, 필터링, 인라인 편집을 지원하며, 사용자가 "행을 추가해", "소계를 추가해" 같은 요청을 하면 실시간으로 코드가 업데이트된다. 컴포넌트는 순수 React이므로, 사용자가 코드를 다운로드하여 자신의 애플리케이션에 통합할 수 있다.

**왜 이 방식인가**: ChatGPT Artifacts는 "텍스트 기반 상호작용만으로 복잡한 컴포넌트 생성"이 가능하게 한다. 테이블의 경우, 사용자는 "설계"를 걱정할 필요 없이 "우리 데이터를 이렇�게 보여줘"라는 요청만 하면, AI가 적절한 기능(정렬, 필터, 편집)을 자동으로 포함시킨다. 동시에 생성된 코드는 오픈 소스 라이브러리(React, Tailwind)만 사용하므로, 라이선스 문제가 없고 재사용성이 높다.

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Full-Featured Data Grid (AG Grid 스타일)

모든 고급 기능(Virtual Scrolling, Column Groups, Pivoting, Grouping)을 기본으로 포함하는 종합 솔루션.

- **대표**: AG Grid (Enterprise), Salesforce Lightning (DataTable)
- **장점**: 대규모 데이터(billions) 처리 가능, 엔터프라이즈급 기능 모두 포함, 성능 최적화됨
- **단점**: 구현 복잡도 극히 높음, 학습 곡선 가파름, 라이선스 비용(AG Grid Enterprise)
- **적합한 상황**: 금융, BI, 데이터 분석 플랫폼 등 대규모 데이터 처리가 필수인 프로덕션 서비스

### 패턴 B: Configurable Database View (Airtable/Notion 스타일)

다중 뷰(Grid, Kanban, Gallery, Calendar)로 동일 데이터를 다양한 관점으로 표현. 각 뷰는 독립적인 필터/정렬/그룹화 상태 유지.

- **대표**: Airtable, Notion, ThoughtSpot (부분적)
- **장점**: 직관적 UX, 뷰 전환이 빠름, 비기술자 친화적, 데이터 탐색 유연성
- **단점**: 뷰별 상태 관리 복잡도 높음, 매우 대규모 데이터(100M+) 시 성능 저하 가능
- **적합한 상황**: 팀 협업 도구, 프로젝트 관리, CRM, 스프레드시트 대체 도구

### 패턴 C: Search-Driven Table (ThoughtSpot 스타일)

검색/드릴다운을 통해 테이블 진입, 동적으로 필터링된 결과 표시. 드릴다운 경로 사전 정의 불필요.

- **대표**: ThoughtSpot (Drill-Anywhere), Tableau Ask Data (부분적)
- **장점**: 자유로운 데이터 탐색, BI 도구 워크플로우에 최적화, 사용자 제어감 높음
- **단점**: 백엔드 집계 필요, 쿼리 성능 의존도 높음, 드릴다운 계층 설계 필요
- **적합한 상황**: BI/analytics 플랫폼, 의사결정 지원 도구, 데이터 탐색 중심 워크플로우

### 패턴 D: Lightweight Rendered Table (Streamlit/ChatGPT 스타일)

클라이언트 메모리에 전체 데이터셋을 로드하고 DOM으로 렌더링. 기본 정렬/필터/인라인 편집만 지원.

- **대표**: Streamlit, ChatGPT Artifacts, React Table (`@tanstack/react-table`)
- **장점**: 구현 간단, 의존성 최소화, 빠른 프로토타입, 경량 라이브러리로 충분
- **단점**: 10k+ rows 이상에서 성능 저하, Virtual Scrolling 미지원, 대규모 데이터 부적합
- **적합한 상황**: MVP, 데모, 프로토타입, 소규모 데이터셋(< 10k rows), 빠른 개발 필요

### 트레이드오프 요약

| 패턴 | 구현 복잡도 | 성능 (1k rows) | 성능 (100k rows) | 기능 풍부도 | 학습 곡선 | 적정 규모 |
|------|----------|---------------|-----------------|-----------|---------|---------|
| **Pattern A (Full Grid)** | 매우 높음 | 빠름 | 빠름 | 매우 높음 | 가파름 | 엔터프라이즈 |
| **Pattern B (Multi-View)** | 높음 | 빠름 | 중간~느림 | 높음 | 중간 | 팀 협업 (10k~100k) |
| **Pattern C (Search-Driven)** | 중간 | 빠름 | 백엔드 의존 | 높음 | 중간 | BI 플랫폼 |
| **Pattern D (Lightweight)** | 낮음 | 빠름 | 느림 | 낮음 | 낮음 | MVP, 데모 (< 10k) |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 |
|----------|-----------|
| `@tanstack/react-table` (dependencies) | Pattern D 기반. 이미 설치되어 있으므로 추가 라이브러리 불필요. 정렬, 필터링, 페이지네이션 기능 즉시 활용 가능. |
| `ChartWidgets.tsx` (Recharts) | 테이블과 차트 간 전환 가능성. 테이블 행을 선택하면 해당 데이터로 차트 렌더링. |
| `LiveboardView` (react-grid-layout) | Pattern B 확장 단계에서 다중 뷰를 그리드 위젯으로 배치 가능. |
| `Recharts` (Chart library) | 테이블 정렬/필터 결과를 그래프로 시각화. 예: 테이블에서 지역별 정렬 후, 해당 지역의 추세선 차트 표시. |
| `NotificationContext` (Global notifications) | 테이블 행 추가/삭제/편집 시 피드백. "행이 저장됐습니다" 등 사용자 확인 메시지. |
| `GeneralChatView` (3-panel layout) | 중앙 패널에 테이블 렌더링, 우측 사이드바에서 필터 조건 입력, 좌측에서 관련 데이터 소스 선택. |

### 권장 접근: Pattern D → B 진화 전략

KonaI-Agent는 데모 프로젝트이므로, 빠른 구현과 시각적 임팩트가 모두 중요하다. 따라서 Phase별 점진적 확장을 권장한다:

**Phase 1 (MVP, 1주일):**
- `@tanstack/react-table` 기반 기본 테이블 구현
- 기능: 단일 컬럼 정렬, 기본 필터(text/number), CSV 내보내기
- 예시 데이터: 영업 데이터(지역, 판매액, 분기) 또는 고객 목록
- 렌더링: DOM-based (< 1000 rows 가정)

**Phase 2 (확장, 2주일):**
- 다중 컬럼 정렬 (Shift+click)
- 컬럼 Visibility Toggle (헤더 우클릭 → "열 표시/숨기기")
- 컬럼 Resize (헤더 경계선 드래그)
- 고급 필터 (날짜 범위, 다중선택)
- 테이블 → Chart 전환 (선택된 행 데이터로 차트 렌더링)

**Phase 3 (생산 준비, 3주일):**
- Multiple View Mode (Grid 뷰, Summary 카드 뷰) — Pattern B 진입
- `react-grid-layout` 통합: Grid/Summary 뷰를 각각 다른 그리드 레이아웃으로 렌더링
- Virtual Scrolling 도입 (> 10k rows 필요 시) — `@tanstack/react-table` v8+는 Virtual Scrolling 지원
- Inline Editing (셀 더블클릭 → 편집 모드)

### 이 접근을 권장하는 이유

1. **기존 의존성 활용**: `@tanstack/react-table`이 이미 설치되어 있으므로, 추가 라이브러리(AG Grid 등) 없이 MVP 완성 가능
2. **점진적 복잡도 관리**: Phase 1에서 핵심만 구현하고, Phase 2~3에서 확장. 각 단계마다 사용자 피드백 수집 가능
3. **Pattern D에서 B로의 자연스러운 진화**: 초기 단일 Grid View → 나중에 Multi-View로 확장할 때 큰 리팩토링 불필요
4. **KonaI-Agent 아키텍처와 일관성**: GeneralChatView의 3-panel 레이아웃에 자연스럽게 통합 가능 (중앙에 테이블, 우측에 필터)
5. **데모 목표 달성**: Phase 2까지만 완성해도 "정렬/필터/export/차트 연계"로 충분한 인상적인 데모 가능

### Acceptance Criteria

- [ ] 테이블이 기본 데이터셋(500~1000 행)을 DOM으로 렌더링하고 스크롤 가능
- [ ] 컬럼 헤더 클릭 → 정렬 (오름/내림/미정렬 3단계)
- [ ] 정렬 상태를 화살표 아이콘으로 시각화
- [ ] 각 컬럼별 독립 필터 인터페이스 (text input, number range picker 등)
- [ ] CSV 내보내기 버튼 → 현재 필터/정렬 적용된 데이터를 CSV로 다운로드
- [ ] 테이블이 GeneralChatView의 중앙 패널에 적절한 크기로 렌더링
- [ ] 50ms 이상의 UI 응답 지연 없음 (1000 rows 기준)
- [ ] Phase 2: 다중 정렬, 컬럼 조작(hide/resize) 동작
- [ ] Phase 2: 선택된 행 데이터로 ChartWidgets.tsx의 차트 렌더링
- [ ] Phase 3: Grid/Summary 다중 뷰 전환 (선택 기능)

---

## Key Considerations

### 데이터 규모별 렌더링 전략

**< 1,000 rows**: DOM-based 전체 렌더링으로 충분. 정렬/필터는 메모리에서 처리 (자바스크립트 Array.sort/filter).

**1,000 ~ 10,000 rows**: DOM-based 렌더링 가능하지만, 페이지네이션 고려. `@tanstack/react-table`의 getPaginatedRowModel() 사용하여 한 페이지에 50~100행만 표시.

**10,000 ~ 100,000 rows**: Virtual Scrolling 도입. `@tanstack/react-table` v8+ 지원. 화면에 보이는 영역만 DOM에 유지하여, DOM 노드 수를 50~100개로 제한.

**> 100,000 rows**: Server-Side 페이지네이션 또는 Backend 필터링 필수. 데이터를 전체 로드하지 않고, 사용자의 정렬/필터 요청마다 서버에서 쿼리 실행 결과만 클라이언트로 반환.

### 인라인 편집의 UX 고려사항

인라인 편집을 구현할 때는 다음을 신경써야 한다:
- **셀 진입**: 더블클릭 또는 Enter 키 → 편집 모드 전환
- **값 저장**: Tab(다음 셀로) 또는 Enter(같은 컬럼 다음 행으로) 또는 Escape(취소)
- **유효성 검사**: 저장 전에 데이터 타입 확인 (숫자 컬럼에 문자 입력 거부)
- **다중 편집**: Ctrl+클릭으로 여러 행 선택 후 한 컬럼을 대량 편집 (Retool 스타일)
- **병렬 편집 충돌**: 여러 사용자가 동시에 편집 시, 최후 저장(Last-Write-Wins) 또는 낙관적 잠금(Optimistic Locking) 전략 선택

### 필터 UI의 사용성 개선

**컬럼 타입별 필터 UI**:
- 텍스트: 포함/정확히 일치/정규식 선택 가능한 텍스트 입력
- 숫자: 범위 슬라이더 또는 Min/Max 수치 입력
- 날짜: 날짜 피커 (시작일~종료일 범위)
- 선택 필드(Enum): 멀티셀렉트 체크박스
- Boolean: 체크박스 (True/False 필터)

**Filter UI 배치**:
- 각 컬럼 헤더 아래에 필터 아이콘 표시 → 클릭 시 필터 팝오버 열기
- 또는 테이블 위에 "필터 바" 두기 (Notion, Airtable 스타일)
- 활성 필터 개수를 배지로 표시 ("필터 3개 활성")

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Web Research | Airtable multi-view: 5가지 기본 뷰(Grid, Kanban, Gallery, Calendar, Timeline), 뷰별 독립 필터/정렬 상태 유지 | airtable, multi-view |
| 2026-02-15 | Web Research | Notion 8가지 뷰 + 양방향 Relations: 데이터베이스 중심 협업 도구, 인라인 편집 + Rollup(집계) 기능 | notion, relations |
| 2026-02-15 | Web Research | ThoughtSpot Drill-Anywhere: 어떤 셀이든 우클릭 드릴다운, 동적 필터링, 드릴다운 경로 사전 정의 불필요 | thoughtspot, drill-down |
| 2026-02-15 | Web Research | AG Grid Virtual Scrolling: 이중 virtual scrolling(행+열), billions row 스케일 처리, Enterprise 고급 기능 | ag-grid, performance |

---

## References

### Vault
- `@tanstack/react-table` — KonaI-Agent dependencies에 이미 포함. Pattern D 기본 구현용.
- `ChartWidgets.tsx` — 테이블과 차트 간 데이터 연계용.
- `GeneralChatView` — 3-panel 레이아웃 중 중앙/우측 패널에 테이블 및 필터 UI 통합용.
- `LiveboardView` (react-grid-layout) — Phase 3 다중 뷰 모드 구현용.

### External
- [^1]: [A 5-Minute Quick Guide to Working with Airtable Views - Bannerbear](https://www.bannerbear.com/blog/a-5-minute-quick-guide-to-working-with-airtable-views/) — Airtable 5가지 기본 뷰와 각 뷰의 특징
- [^2]: [Intro to databases – Notion Help Center](https://www.notion.com/help/intro-to-databases) — Notion 8가지 뷰, 필터/정렬/그룹화, 인라인 편집
- [^2]: [Relations & rollups – Notion Help Center](https://www.notion.com/help/relations-and-rollups) — Notion 양방향 Relations, Rollup 집계 함수
- [^3]: [Drill down into your data | ThoughtSpot Cloud](https://docs.thoughtspot.com/cloud/10.10.0.cl/search-drill-down) — ThoughtSpot Drill-Anywhere 메커니즘, 동적 드릴다운
- [^4]: [JavaScript Grid: Scrolling Performance | AG Grid](https://www.ag-grid.com/javascript-data-grid/scrolling-performance/) — AG Grid Virtual Scrolling, rowBuffer 설정, DOM 최소화
- [^5]: [JavaScript Grid: Column Groups | AG Grid](https://www.ag-grid.com/javascript-data-grid/column-groups/) — AG Grid Column Groups, 계층적 헤더
- [^6]: [Using database views – Notion Help Center](https://www.notion.com/help/guides/using-database-views) — 뷰별 독립 상태 관리, 필터/정렬/그룹화 설정

---

*Last synthesized: 2026-02-15 | Review: auto-trigger (Recent Updates 4건 누적 시)*
