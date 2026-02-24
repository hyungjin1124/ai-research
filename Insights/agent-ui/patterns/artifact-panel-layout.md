---
type: insight-synthesis
topic_id: "artifact-panel-layout"
topic_name: "아티팩트 패널 레이아웃 설계"
category: agent-ui
document_level: specific
parent_broad:
  - "artifacts-canvas-patterns"
  - "conversational-ui-patterns"
catalog_components:
  - "artifact_panel"
tags:
  - insight
  - agent-ui
  - pattern
  - layout
  - panel
  - artifacts
  - canvas
  - competitive-analysis
status: draft
confidence: high
last_updated: "2026-02-18"
source_products: ["claude-artifacts", "chatgpt-canvas", "google-gemini", "v0-vercel", "cursor", "windsurf", "chatgpt-deep-research"]
source_files:
  - "src/components/features/agent-chat/components/ArtifactPreviewPanel/ArtifactPreviewPanel.tsx"
  - "src/components/features/agent-chat/AgentChatView.tsx"
  - "src/components/features/agent-chat/components/RightSidebar/ArtifactsSection.tsx"
  - "src/components/features/agent-chat/types.ts"
auto_update:
  enabled: true
  keywords: ["artifact panel", "canvas", "side panel", "preview pane", "cowork", "artifacts"]
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 아티팩트 패널 레이아웃 설계

## TL;DR

- **Side Panel → Cowork 진화**: Claude Artifacts는 Cowork 모드(데스크톱 앱 전용)로 진화하여 Chat/Code/Cowork 3탭 구조 + VM 기반 실행 환경을 제공하며, 웹에서는 여전히 우측 패널 방식을 유지한다 [^1][^7]
- **Canvas 생태계 확장**: ChatGPT Canvas는 2025-2026에 걸쳐 인터랙티브 앱 빌드, PDF/MD/DOCX 내보내기, Record Mode(음성 협업), Projects 통합 등으로 편집 도구에서 "생산성 워크스페이스"로 확장했다 [^3][^8]
- **Full-Screen Document Viewer 신규 패턴**: ChatGPT Deep Research의 보고서 뷰어가 TOC 사이드바 + 본문 + 소스 사이드바의 3-패널 풀스크린 레이아웃을 도입하여, 긴 분석 결과물에 최적화된 새로운 아티팩트 패턴을 확립했다 [^9][^10]
- **Generative UI 본격화**: Gemini 3 Dynamic View가 프롬프트에서 HTML/CSS/JS를 실시간 생성·렌더링하고, Visual Layout(잡지형 리치 포맷)을 도입하여 아티팩트 패널의 역할이 "미리보기"에서 "동적 인터페이스 생성"으로 확장되고 있다 [^2][^11]
- **KonaI-Agent 권장**: 현재 `ArtifactPreviewPanel`(10+ 타입 지원, 50+ props)의 구조적 문제(거대 props, 탭 부재, 히스토리 부재)를 해결하면서, Phase 1 탭+리사이즈 → Phase 2 히스토리+키보드 내비게이션 → Phase 3 Deep Research 풀스크린 뷰어 통합 순으로 점진 개선

---

## Overview

아티팩트 패널은 AI 에이전트가 생성한 결과물(코드, 문서, 시각화, 대시보드)을 채팅 컨텍스트와 함께 표시하는 핵심 UI 패턴이다. 2024년 Claude Artifacts와 ChatGPT Canvas가 이 패턴을 업계 표준으로 확립한 이후, 2025-2026년에는 세 가지 주요 진화가 관찰된다:

1. **편집 도구 → 생산성 워크스페이스**: ChatGPT Canvas가 Projects 통합, Record Mode, 앱 빌드 기능을 추가하면서 단순 텍스트/코드 편집을 넘어 멀티모달 워크스페이스로 확장했다.
2. **Generative UI 본격화**: Gemini Dynamic View와 Claude Cowork가 각각 HTML/CSS/JS 실시간 생성과 VM 기반 코드 실행을 도입하여, 아티팩트가 정적 렌더링에서 동적 인터랙티브 경험으로 진화하고 있다.
3. **Long-form Document Viewer**: ChatGPT Deep Research가 긴 분석 보고서를 위한 전용 풀스크린 뷰어(TOC + 소스 패널)를 도입하여, 기존 사이드 패널 패턴으로는 불충분한 대형 결과물을 위한 새 패턴이 등장했다.

KonaI-Agent는 이미 `ArtifactPreviewPanel`이 PDF, DOCX, XLSX, CSV, PPTX, Markdown, PPT 생성, 대시보드, 슬라이드 개요 등 10가지 이상의 프리뷰 타입을 지원하며, `AgentChatView`의 CoworkLayout으로 3-패널(좌측 채팅 + 중앙 아티팩트 + 우측 사이드바) 구조를 갖추고 있다. 그러나 탭 관리, 버전 히스토리, 패널 분리(detach), 키보드 내비게이션이 부재하고, 50개 이상의 props가 하나의 컴포넌트에 결합되어 있는 구조적 문제가 있다. 이 리서치는 2026년 시점의 경쟁사 동향을 반영하여 개선 방향을 제시한다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 레이아웃 유형 | 탭/다중 아티팩트 | 버전 히스토리 | 인라인 편집 | 내보내기 | Generative UI | Full-Screen 모드 |
|------|-------------|----------------|-------------|-----------|---------|-------------|----------------|
| Claude Artifacts (Web) | Side Panel | 순차 표시 | 제한적 | 부분 (코드) | 복사/다운로드 | React 컴포넌트 실행 | 없음 |
| Claude Cowork (Desktop) | 3-탭 워크스페이스 | 탭 기반 | Cowork 세션 | VM 기반 전체 편집 | 파일 시스템 연동 | VM 실행 | Cowork 탭 전체 |
| ChatGPT Canvas | Two-Pane Canvas | 탭 기반 (Projects) | 전체 히스토리 | 하이라이트-편집 | PDF/MD/DOCX | 인터랙티브 앱 빌드 | Canvas 전체 |
| ChatGPT Deep Research | 3-Panel Full-Screen | N/A (단일 보고서) | N/A | 읽기 전용 | PDF 복사 | 없음 | TOC+본문+소스 |
| Gemini Dynamic View | Side Panel + Visual Layout | 미지원 | 미지원 | 제한적 | 없음 | HTML/CSS/JS 생성 | 없음 |
| v0 by Vercel | Split Pane | 파일 탐색기 | 프로젝트 Git | 코드 에디터 | Vercel 배포 | Vercel Sandbox | 프리뷰 전체화면 |
| Cursor | Inline Diff | N/A (에디터 탭) | 에디터 히스토리 | 인라인 diff+apply | 파일 저장 | 없음 | 없음 |
| Windsurf Cascade | Context-Aware Panel | N/A (에디터 탭) | 정보 표시 | 직접 디스크 기록 | 파일 저장 | 없음 | 없음 |

### 경쟁사별 상세 분석

#### Claude Artifacts/Cowork — Side Panel에서 VM 워크스페이스로의 진화

Claude Artifacts는 웹에서 여전히 우측 사이드 패널에 아티팩트를 표시하는 기본 방식을 유지한다. Preview/Code 탭, 줌 인/아웃, 복사/다운로드 기능을 제공하며, React 컴포넌트와 HTML/SVG 실시간 렌더링을 지원한다 [^1].

2025년 하반기부터 도입된 Claude Cowork 모드(Claude Desktop 전용)는 큰 전환점이다. Chat/Code/Cowork 3개 탭 구조를 도입하여, Cowork 탭에서는 VM 기반 가상 환경이 실행된다. 이 VM에서 파일 시스템 접근, 터미널 실행, MCP(Model Context Protocol) 서버 연동이 가능하며, 코드 실행 결과가 실시간으로 반영된다. 웹 Artifacts가 "미리보기 패널"이라면, Desktop Cowork는 "완전한 개발 환경"으로 격이 다르다 [^7].

**왜 이 방식인가**: Anthropic은 웹과 데스크톱에서 다른 전략을 취한다. 웹은 가벼운 미리보기에 집중하여 진입장벽을 낮추고, 데스크톱은 파워유저를 위해 VM 기반 전체 환경을 제공한다. 이 이원화는 사용자 세그먼트별 최적화를 가능케 하지만, 경험의 일관성 문제를 야기할 수 있다.

*참고 URL*: https://docs.anthropic.com/en/docs/build-with-claude/artifacts, https://www.anthropic.com/news/claude-computer-use-cowork

#### ChatGPT Canvas — 편집 도구에서 생산성 워크스페이스로

ChatGPT Canvas는 2024년 출시 이후 가장 공격적인 확장을 보여준다. 초기 텍스트/코드 편집 기능에서, 2025-2026년 사이 다음 기능들이 추가되었다 [^3][^8]:

- **인터랙티브 앱 빌드**: 프롬프트로 HTML/CSS/JS 기반 인터랙티브 앱을 Canvas 내에서 생성하고 즉시 실행. Gemini Dynamic View와 유사하지만 Canvas의 기존 편집 워크플로우와 통합.
- **Record Mode**: 마이크를 통한 음성 협업. 사용자가 말하면서 Canvas 내용을 수정 지시.
- **PDF/Markdown/DOCX 내보내기**: Canvas에서 작성한 콘텐츠를 다양한 포맷으로 내보내기.
- **Projects 통합**: 여러 Canvas를 프로젝트 단위로 묶어 관리. 탭 기반 다중 아티팩트 관리의 상위 개념.
- **버전 히스토리**: 모든 편집 이력을 타임라인으로 추적하고 롤백 가능.

**왜 이 방식인가**: OpenAI는 Canvas를 단순 편집기가 아닌 "AI 네이티브 생산성 도구"로 포지셔닝한다. GPT-4o의 멀티모달 역량(텍스트+코드+음성+이미지)을 Canvas라는 통합 워크스페이스에서 활용하게 함으로써, Google Docs/Notion 같은 기존 도구와의 경쟁을 노린다.

*참고 URL*: https://openai.com/index/introducing-canvas/, https://help.openai.com/en/articles/canvas

#### ChatGPT Deep Research — Full-Screen Document Viewer 패턴

ChatGPT Deep Research는 긴 분석 보고서를 위한 전혀 새로운 아티팩트 패턴을 도입했다 [^9][^10]. 기존 Canvas의 사이드 패널이 아닌, 보고서 전용 풀스크린 3-패널 뷰어를 사용한다:

- **좌측 사이드바**: Table of Contents(목차). 보고서 섹션 간 빠른 이동. 스크롤에 따라 현재 위치 하이라이트.
- **중앙 본문**: 마크다운 렌더링된 보고서 본문. 인라인 각주 번호 클릭 시 우측 소스 패널과 연동.
- **우측 사이드바**: Sources(출처). 보고서 작성에 사용된 모든 웹 소스 목록. 각주와 양방향 링크.

이 패턴은 Academic Paper Viewer(Google Scholar, arXiv)와 유사하지만, AI가 생성한 보고서에 최적화되어 있다. 특히 인라인 각주 ↔ 소스 패널의 양방향 연동이 핵심 차별점이다.

**왜 이 방식인가**: Deep Research의 결과물은 2,000-10,000 단어에 달하는 장문 보고서로, 기존 Canvas 사이드 패널(너비 제한)로는 읽기 불편하다. 학술 논문/보고서 열람에 익숙한 사용자 경험을 차용하되, AI 생성물의 특성(출처 투명성)을 극대화하는 소스 사이드바를 추가했다.

*참고 URL*: https://openai.com/index/introducing-deep-research/

#### Google Gemini — Dynamic View와 Visual Layout

Gemini는 2025-2026년 사이 두 가지 주요 아티팩트 기능을 도입했다 [^2][^11]:

**Dynamic View**: 프롬프트에 응답하여 HTML/CSS/JS 기반 인터랙티브 인터페이스를 실시간으로 생성·렌더링한다. 예를 들어 "3D 태양계 시뮬레이터를 만들어줘"라는 프롬프트에 Gemini가 완전한 인터랙티브 웹앱을 코딩하여 우측 패널에서 실행한다. 사용자는 수정을 지시하여 반복 개선할 수 있다.

**Visual Layout**: 응답을 잡지형 리치 포맷으로 표시하는 기능이다. 텍스트, 이미지, 차트, 인터랙티브 요소를 매거진 스타일로 배치하여, 기존의 단조로운 마크다운 응답을 시각적으로 풍부하게 만든다. 이는 Generative UI의 가장 접근 가능한 형태로, 전문 지식 없이도 리치 콘텐츠를 생성할 수 있다.

**왜 이 방식인가**: Google은 Gemini를 "모든 것을 만들 수 있는 AI"로 포지셔닝한다. Dynamic View는 개발자뿐 아니라 비개발자도 프롬프트만으로 인터랙티브 콘텐츠를 만들 수 있게 하며, Visual Layout은 AI 응답 자체를 "디자인된 콘텐츠"로 격상시킨다.

*참고 URL*: https://blog.google/products/gemini/google-gemini-updates-february-2026/

#### v0 by Vercel — Vercel Sandbox와 프로덕션급 프리뷰

v0는 Vercel Sandbox라는 경량 VM 환경에서 생성된 앱을 실행한다 [^4]. 좌측 채팅 + 우측 프리뷰(코드/프리뷰 탭 전환) 구조를 유지하면서, 프리뷰 영역이 서버 사이드 렌더링, API 라우트, DB 연결까지 지원하는 완전한 실행 환경이다. 파일 탐색기로 프로젝트 구조를 탐색할 수 있으며, Vercel에 원클릭 배포가 가능하다.

**왜 이 방식인가**: v0의 핵심 가치는 "프리뷰 = 프로덕션" 등가성이다. 프론트엔드만 렌더링하는 샌드박스로는 서버 사이드 로직의 정확성을 보장할 수 없기에, Vercel의 인프라 역량을 활용하여 완전한 실행 환경을 제공한다.

*참고 URL*: https://v0.dev/docs

#### Cursor — Inline Diff와 Apply 모델

Cursor는 별도 아티팩트 패널 없이 에디터 내 인라인 diff를 표시한다 [^5]. AI의 변경 제안이 빨강(삭제)/초록(추가) 하이라이트로 코드 내에 직접 표시되며, 사용자는 라인별 또는 블록별로 Accept/Reject할 수 있다. 내부적으로 "Sketching" 모델(변경 의도 생성)과 "Apply" 모델(기존 코드에 통합)의 2단계 파이프라인을 사용한다.

**왜 이 방식인가**: 개발자는 IDE를 떠나고 싶지 않다. 별도 패널로 시선을 분산시키기보다는 코드가 있는 그 자리에서 변경사항을 리뷰하는 것이 가장 자연스러운 워크플로우다.

*참고 URL*: https://www.cursor.com/features

#### Windsurf Cascade — Direct-to-Disk 패턴

Windsurf의 Cascade는 AI 편집을 에디터에서 직접 파일에 기록하는 "write-first" 방식을 취한다 [^6]. Cursor와 달리 diff를 먼저 보여주고 승인을 받는 것이 아니라, 변경을 바로 적용하고 "Open Diff" 버튼으로 사후 리뷰할 수 있게 한다. 컨텍스트 윈도우 사용량을 시각적으로 표시하여 세션 관리를 돕는다.

**왜 이 방식인가**: Windsurf는 "신뢰 기반 자동화"를 지향한다. 매번 diff를 확인하는 것은 생산성을 저해하므로, AI를 신뢰하고 결과를 사후 검증하는 워크플로우를 제안한다.

*참고 URL*: https://docs.windsurf.com/windsurf/cascade

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Side Panel with Chat Retention

채팅을 좌측/중앙에 유지하면서 아티팩트를 우측 패널에 표시하는 기본 방식. 패널 크기 조정 가능하며, 채팅과 아티팩트가 독립적으로 스크롤된다.

- **대표**: Claude Artifacts (Web), Gemini Dynamic View
- **장점**: 채팅 컨텍스트 완전 보존, 낮은 구현 복잡도, 유연한 패널 비율 조정
- **단점**: 좁은 패널에서 복잡한 UI 표시 어려움, 다중 아티팩트 관리 복잡, 버전 히스토리 추가 어려움
- **적합한 상황**: 빠른 프로토타입, 중소 규모 아티팩트, 채팅 중심 워크플로우

### 패턴 B: Two-Pane Canvas (Editing Workspace)

화면을 명확히 분할하여 우측에 전용 편집 공간 운영. 하이라이트-편집, 버전 히스토리, 내보내기 등 생산성 도구 기능 포함.

- **대표**: ChatGPT Canvas, Claude Cowork
- **장점**: 집중 편집 경험, 강력한 버전 히스토리, 하이라이트-편집으로 정밀 수정, 다양한 내보내기 포맷
- **단점**: 높은 구현 복잡도, 화면 공간 요구, Canvas 모드 전환 시 인지 비용
- **적합한 상황**: 문서/코드 편집 중심 작업, 버전 관리 중요한 경우, 단일 대형 아티팩트 중심

### 패턴 C: Full-Screen Document Viewer

장문 분석 결과물을 위한 전용 풀스크린 뷰어. TOC 사이드바 + 본문 + 소스/메타 사이드바의 3-패널 구조.

- **대표**: ChatGPT Deep Research
- **장점**: 장문 콘텐츠 최적화, TOC로 빠른 내비게이션, 출처 투명성 극대화(소스 패널), 학술/보고서 열람에 익숙한 UX
- **단점**: 채팅 컨텍스트와 완전 분리, 짧은 아티팩트에는 과도, 단일 결과물 전용(다중 탭 부적합)
- **적합한 상황**: Deep Research 보고서, 장문 분석 결과, 출처 추적이 중요한 엔터프라이즈 보고서

### 패턴 D: Live Preview Split (Development-Focused)

좌측 채팅/코드와 우측 실시간 애플리케이션 프리뷰 병렬 운영. 프로덕션급 런타임에서 실행.

- **대표**: v0 by Vercel, Gemini Dynamic View (Generative UI)
- **장점**: WYSIWYG 신뢰도, 풀스택 프리뷰, 실시간 피드백
- **단점**: 높은 인프라 비용, 구현 복잡도, 코드 전용 아티팩트에는 오버스펙
- **적합한 상황**: 풀스택 웹앱 개발, 서버 사이드 로직 중요, 배포 후 예측 불가 버그 최소화

### 패턴 E: Inline Diff (Editor-Centric)

별도 패널 없이 에디터 내 인라인 diff로 변경 표시. 라인별 Accept/Reject 지원.

- **대표**: Cursor, Windsurf Cascade
- **장점**: 에디터 이탈 불필요, 직관적 diff, 빠른 리뷰 사이클
- **단점**: 시각적 프리뷰 부재, 다중 파일 변경 추적 어려움, IDE 전용
- **적합한 상황**: 코드 편집 전용, IDE 통합, 개발자 대상

### 트레이드오프 요약

| | 채팅 가시성 | 편집 영역 | 구현 복잡도 | 버전 관리 | 멀티 아티팩트 | 장문 적합성 | Generative UI |
|---|---|---|---|---|---|---|---|
| **Side Panel** | 높음 | 중간 | 낮음 | 약함 | 탭 추가 가능 | 낮음 | 가능 |
| **Two-Pane Canvas** | 높음 | 높음 | 높음 | 강함 | 탭 기반 | 중간 | 가능 |
| **Full-Screen Viewer** | 없음 | 높음 | 중간 | N/A | N/A | 높음 | 없음 |
| **Live Preview** | 높음 | 높음 | 매우 높음 | Git 기반 | 파일 기반 | 낮음 | 강함 |
| **Inline Diff** | 높음 | 높음 | 중간 | 에디터 의존 | 에디터 탭 | 낮음 | 없음 |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 활용 가능성 |
|----------|-----------|
| `ArtifactPreviewPanel` (349줄, 50+ props) | 10+ 타입 지원(pdf/docx/xlsx/csv/pptx/markdown/ppt/dashboard/chart/slide-outline). **구조 리팩터링 필요** — props를 컨텍스트 기반 주입으로 전환하여 컴포넌트 분리 |
| `AgentChatView` CoworkLayout (1797줄) | 3-패널 레이아웃 기반 확보. 중앙 패널 open 시 사이드 패널 자동 숨김/복원 로직 존재. `rightPanelWidth` 리사이즈(25-70%) 지원 |
| `ArtifactsSection` (115줄) | 우측 사이드바 아티팩트 목록 + 드래그앤드롭(ARTIFACT_DRAG_MIME_TYPE). 아이콘 매핑(PDF/DOCX/XLSX/CSV/PPTX 등) 완비 |
| `DocumentViewer` | PDF(react-pdf), DOCX(mammoth), XLSX(xlsx), CSV(커스텀), PPTX(info card) 렌더링 구현 완료 |
| `MarkdownPreviewPanel` | 마크다운 read/edit 모드 전환, 편집 상태 관리 구현 완료 |
| `types.ts` Artifact 타입 | `ArtifactType` 11가지 정의, `ArtifactPreviewState` 상태 관리 타입 정의 |
| PPT/Dashboard 프리뷰 | `PPTGenPanel`, 대시보드 컴포넌트 렌더링 기존 구현 |
| `usePPTScenario` 훅 | 다단계 시나리오 오케스트레이션 기반 — 아티팩트 생성 → 리뷰 → 수정 사이클에 활용 가능 |

### 권장 접근: Hybrid Side Panel + Full-Screen Viewer

**패턴 선택**: 기본 Side Panel (Pattern A)에 Full-Screen Document Viewer (Pattern C)를 상황별 전환으로 결합한다.

- **일반 아티팩트** (코드, 짧은 마크다운, 차트, 대시보드): Side Panel에 탭 기반으로 표시
- **장문 보고서** (분석 결과, Deep Research 스타일): Full-Screen Viewer로 전환 (TOC + 본문 + 소스/메타)
- **문서 뷰어** (PDF, DOCX, XLSX): 기존 DocumentViewer를 Side Panel 내에서 운영하되, 전체화면 전환 지원

**Phase 1 (MVP — 탭 관리 + 구조 리팩터링)**:
- `ArtifactPreviewPanel`의 50+ props를 `ArtifactContext`로 리팩터링하여 타입별 서브 컴포넌트 분리
- 패널 상단에 탭 바 추가 (Radix UI Tabs). 열린 아티팩트를 탭으로 관리 (최대 8개)
- 탭에 아티팩트 타입 아이콘 + 제목 + 닫기 버튼
- 키보드 내비게이션: `Ctrl+Tab`으로 탭 전환, `Ctrl+W`로 탭 닫기
- 패널 리사이즈 핸들 개선: 드래그 리사이즈 + 더블클릭으로 기본 너비 복원

**Phase 2 (히스토리 + 내비게이션 강화)**:
- 아티팩트별 버전 히스토리 (생성 시간, 관련 메시지 ID로 채팅 위치 추적)
- 아티팩트 클릭 시 관련 채팅 메시지로 자동 스크롤 (양방향 링크)
- Breadcrumb 내비게이션: 아티팩트 타입 > 파일명 > 버전
- 아티팩트 검색/필터: 타입별, 날짜별, 키워드별

**Phase 3 (Full-Screen Viewer + 고급 기능)**:
- Deep Research 스타일 풀스크린 뷰어: TOC 사이드바 + 본문 + 소스 사이드바
- 기존 `citation_source_link` 컴포넌트와 통합하여 소스 패널 자동 생성
- 패널 분리(detach to window): 아티팩트를 별도 브라우저 탭/창으로 분리
- 내보내기 강화: PDF, Markdown, DOCX 포맷

### 이 접근을 권장하는 이유

1. **기존 자산 최대 활용**: CoworkLayout 3-패널 구조와 DocumentViewer가 이미 구현되어 있어, 탭 추가와 구조 리팩터링만으로 Phase 1 달성 가능
2. **상황별 최적 패턴 적용**: 짧은 아티팩트는 Side Panel, 장문 보고서는 Full-Screen Viewer로 사용자 경험 최적화
3. **점진적 복잡도 관리**: Phase 1이 구조 리팩터링에 집중하므로 이후 Phase의 기능 추가가 용이
4. **Deep Research 보고서 뷰어 차별화**: 엔터프라이즈 환경에서 장문 분석 보고서 열람은 핵심 유스케이스이며, 기존 `citation_source_link`와의 통합으로 출처 투명성 확보

### Acceptance Criteria

- [ ] `ArtifactPreviewPanel`의 props를 `ArtifactContext`로 리팩터링하여 타입별 서브 컴포넌트 3개 이상 분리
- [ ] 패널 상단 탭 바에서 최대 8개 아티팩트를 탭으로 관리 (열기, 닫기, 전환)
- [ ] 탭에 아티팩트 타입 아이콘 + 제목(truncate) + 닫기 버튼 표시
- [ ] 키보드 내비게이션: `Ctrl+Tab` 탭 전환, `Ctrl+W` 탭 닫기
- [ ] 드래그 리사이즈 핸들로 패널 너비 조정 (25%-70% 범위 유지)
- [ ] 전체화면(Maximize) 토글이 탭 상태를 보존하면서 동작
- [ ] 아티팩트 생성 시 자동으로 해당 탭이 열리고 포커스 전환
- [ ] 우측 사이드바 ArtifactsSection에서 아티팩트 클릭 시 기존 탭으로 전환 또는 새 탭 열기
- [ ] (Phase 2) 아티팩트 클릭 시 관련 채팅 메시지로 스크롤
- [ ] (Phase 3) 장문 보고서를 TOC+본문+소스 3-패널 풀스크린 뷰어로 표시

---

## Key Considerations

### Props 폭발 문제 해결 전략

현재 `ArtifactPreviewPanel`은 PPT, Dashboard, SlideOutline, Document, Markdown 각각의 상세 props를 모두 받고 있어 50개 이상의 props가 하나의 인터페이스에 존재한다. 이는 유지보수와 확장의 최대 병목이다.

권장 접근은 **Compound Component + Context** 패턴이다:
- `ArtifactPanelProvider`가 공통 상태(열린 탭 목록, 현재 탭, 리사이즈 상태)를 관리
- 각 타입별 렌더러(`PPTRenderer`, `DocumentRenderer`, `MarkdownRenderer` 등)가 자신의 props만 받음
- 타입별 props는 `ArtifactContext`를 통해 전달하거나, 렌더러 컴포넌트에 직접 전달
- `renderPreview()` 스위치문을 Registry 패턴으로 전환하여 새 타입 추가 시 코드 변경 최소화

### 탭 관리와 메모리 최적화

8개 탭이 동시에 열릴 수 있으므로 메모리 관리가 중요하다:
- 비활성 탭의 무거운 렌더러(PDF 뷰어, XLSX 테이블)는 `React.lazy` + `Suspense`로 지연 로드
- 탭 닫기 시 관련 상태를 정리하되, 히스토리(Phase 2)를 위해 메타데이터는 보존
- 탭이 8개를 초과하면 가장 오래된 비활성 탭을 자동으로 닫고, 드롭다운 "최근 닫은 탭"에서 복원 가능

### Full-Screen Viewer와 Side Panel의 전환 UX

사용자가 Side Panel과 Full-Screen Viewer 사이를 자연스럽게 전환할 수 있어야 한다:
- Side Panel에서 "전체화면" 버튼 클릭 → 트랜지션 애니메이션으로 Full-Screen Viewer로 확장
- Full-Screen Viewer에서 "패널로 복귀" 버튼 → 이전 Side Panel 상태로 복원
- 장문 보고서 타입 아티팩트는 생성 시 자동으로 Full-Screen Viewer 제안 (사용자 선택)
- URL 해시로 뷰 모드를 인코딩하여 새로고침 시 상태 보존

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다. 수동 편집 금지. -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | Initial | 초판 작성 — 6개 경쟁사 분석, 4개 패턴 분류 | initial |
| 2026-02-18 | Research Update | 전면 재작성 — Claude Cowork, ChatGPT Deep Research Viewer, Gemini Dynamic View, 현재 코드베이스 반영. 5개 패턴으로 확장. Acceptance Criteria 구체화 | major-update, competitive-analysis |

---

## References

### Vault
- [^V1]: [[Insights/agent-ui/artifacts-canvas-patterns|Artifacts & Canvas Patterns (Broad)]] — 4대 레이아웃 패턴 + 트리거 전략 + 편집 깊이 분류
- [^V2]: [[Insights/agent-ui/conversational-ui-patterns|Conversational UI Patterns (Broad)]] — Dual-Pane, Sidecar, Glass Box 투명성 패턴
- [^V3]: [[Insights/agent-ui/patterns/document-viewer-patterns|Document Viewer Patterns]] — PDF/DOCX/XLSX 뷰어 구현 패턴

### External
- [^1]: LogRocket — Implementing Claude's Artifacts feature (https://blog.logrocket.com/implementing-claudes-artifacts-feature-ui-visualization/) — Claude Artifacts 아키텍처 분석
- [^2]: 9to5Google — Gemini Chrome side panel (https://9to5google.com/2026/01/28/gemini-chrome-side-panel-more/) — Gemini Dynamic View Chrome 통합
- [^3]: OpenAI — Introducing Canvas (https://openai.com/index/introducing-canvas/) — ChatGPT Canvas 초기 설계 철학
- [^4]: v0 Docs (https://v0.dev/docs) — v0 Vercel Sandbox 아키텍처
- [^5]: Fabian Hertwig — Code Surgery: How AI Assistants Make Precise Edits (https://fabianhertwig.com/blog/coding-assistants-file-edits/) — Cursor/Windsurf diff 모델 비교
- [^6]: Windsurf Cascade Docs (https://docs.windsurf.com/windsurf/cascade) — Windsurf 컨텍스트 인식 패턴
- [^7]: Anthropic — Claude Computer Use & Cowork (https://www.anthropic.com/news/claude-computer-use-cowork) — Claude Cowork VM 기반 워크스페이스
- [^8]: OpenAI Help — Canvas Features (https://help.openai.com/en/articles/canvas) — Canvas 2025-2026 기능 확장 목록
- [^9]: OpenAI — Introducing Deep Research (https://openai.com/index/introducing-deep-research/) — Deep Research 보고서 뷰어 UX
- [^10]: Ars Technica — ChatGPT Deep Research Review (https://arstechnica.com/information-technology/2025/02/openais-deep-research-agent-produces-impressive-results/) — Deep Research 3-패널 뷰어 분석
- [^11]: Google Blog — Gemini Updates Feb 2026 (https://blog.google/products/gemini/google-gemini-updates-february-2026/) — Dynamic View + Visual Layout 기능

---

*Last synthesized: 2026-02-18 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
