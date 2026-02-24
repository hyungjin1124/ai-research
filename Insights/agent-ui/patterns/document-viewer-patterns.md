---
type: insight-synthesis
topic_id: "document-viewer-patterns"
topic_name: "문서 뷰어 (DOCX/PDF/PPTX) 패턴"
category: agent-ui
document_level: specific
parent_broad:
  - "artifacts-canvas-patterns"
catalog_components:
  - "document_viewer"
  - "ppt_slide_preview"
tags:
  - insight
  - agent-ui
  - pattern
  - document-handling
  - viewer
  - docx
  - pdf
  - pptx
  - table-of-contents
  - citation-panel
  - fullscreen
status: current
confidence: high
last_updated: "2026-02-21"
source_products:
  - "openai"
  - "google-gemini"
  - "claude"
  - "microsoft-copilot"
  - "perplexity"
  - "notion"
  - "gamma"
  - "coda"
source_files: []
auto_update:
  enabled: true
  keywords:
    - document viewer
    - PDF viewer
    - DOCX preview
    - PPTX viewer
    - react-pdf
    - mammoth.js
    - file preview
    - office document
    - table of contents
    - citation panel
    - fullscreen toggle
    - deep research viewer
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 문서 뷰어 (DOCX/PDF/PPTX) 패턴

## TL;DR

- **ChatGPT Deep Research**(2026-02-10 리디자인)가 풀스크린 문서 뷰어를 도입하여 **좌측 TOC 사이드바 + 중앙 리포트 + 우측 인용 패널**의 3패널 레이아웃을 표준화했으며, Markdown/Word/PDF 내보내기를 지원한다 [^1][^2]
- **인터랙티브 인덱스(TOC 사이드바)**는 ChatGPT, Notion, Google Docs가 공통 채택한 패턴으로, heading 기반 자동 생성 + 스크롤 스파이 + 클릭 점프가 핵심이며, Notion은 floating TOC를 우측에, ChatGPT는 좌측 사이드바에 배치한다 [^1][^3][^4]
- **인용 사이드패널**은 ChatGPT가 우측 확장 가능 패널로, Perplexity가 인라인 각주 + 확장형 소스 카드로, Gemini가 granular sourcing + 시각화 통합으로 각각 구현하며, 출처 검증을 핵심 UX로 삼는다 [^5][^6][^7]
- **풀스크린 토글**은 ChatGPT Deep Research 뷰어, Claude Artifacts(반스크린 기본 → 풀스크린 확장), Manus AI(Full-Screen Takeover)에서 채택한 패턴으로, Fullscreen API 기반 또는 CSS 레이아웃 전환으로 구현된다 [^1][^8][^9]
- **KonaI-Agent 권장**: 현재 DocumentViewer(PDF/DOCX/XLSX/CSV 구현 완료)에 **(1) TOC 사이드바**(heading 파싱 + 스크롤 스파이), **(2) 인용 사이드패널**(소스 목록 + 인라인 하이라이트), **(3) 풀스크린 토글**(CSS 기반 portal 레이아웃)을 확장하는 전략이 기존 아키텍처와 최소 충돌하며 가장 현실적이다

---

## Overview

문서 뷰어 패턴은 AI 에이전트가 생성하거나 참조하는 문서를 인라인으로 프리뷰하고 탐색하는 방식을 정의한다. 2026년 2월, ChatGPT Deep Research의 풀스크린 문서 뷰어 리디자인이 이 영역의 새로운 기준을 설정했다. 좌측 TOC 사이드바, 중앙 리포트, 우측 인용 패널의 3패널 구조는 AI 리서치 리포트의 "읽기 경험"을 웹 앱 레벨에서 최적화한 첫 사례로, 이전의 단순한 채팅 내 마크다운 표시와 질적으로 다른 접근이다.

KonaI-Agent의 맥락에서, document_viewer는 Phase 1+2 구현이 완료되어 PDF(react-pdf), DOCX(docx-preview), XLSX(SheetJS), CSV 뷰잉을 지원한다. ArtifactPreviewPanel의 멀티탭 시스템, DocumentViewerToolbar의 공통 줌/내비게이션, ArtifactPanelContext의 상태 관리가 이미 성숙해 있다. 이 기반 위에 TOC 사이드바, 인용 패널, 풀스크린 토글의 3가지 확장을 추가하면, ChatGPT Deep Research 수준의 문서 열람 경험을 구현할 수 있다. 특히 현재 feature/document_viewer 브랜치에서 작업 중이므로 타이밍이 최적이다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | TOC 사이드바 | 인용 패널 | 풀스크린 | 내보내기 | 3패널 구조 | 핵심 차별점 |
|------|:----------:|:---------:|:-------:|:-------:|:---------:|-----------|
| ChatGPT Deep Research | ✓ 좌측 | ✓ 우측 확장형 | ✓ 풀스크린 뷰어 | MD, DOCX, PDF | ✓ TOC+Doc+Citation | 리서치 리포트 전용 뷰어, 실시간 진행 추적 |
| Google Gemini | ✗ | ✓ Granular sourcing | ✗ | Canvas 통합 | ✗ | Dynamic View, 인터랙티브 시각화 임베딩 |
| Claude Artifacts | ✗ | ✗ | ✓ 반→풀 확장 | 복사, 웹 퍼블리시 | ✗ | antThinking 자동 트리거, 인라인 코드 실행 |
| Perplexity | ✗ (Pages 별도) | ✓ 인라인 각주+소스패널 | ✗ | 제한적 | ✗ | Citation-forward 설계, 실시간 웹 검색 기반 |
| Notion | ✓ Floating TOC (우측) | ✗ | ✗ | MD, PDF, HTML | ✗ | heading 기반 자동 TOC, @멘션 컨텍스트 |
| Microsoft Copilot | ✓ Word Navigation Pane | ✗ | ✓ 네이티브 | DOCX 네이티브 | ✗ | Office Object Model 직접 조작 |
| Google Docs | ✓ Outline sidebar (좌측) | ✗ | ✗ | DOCX, PDF, ODT | ✗ | Gemini 인라인 편집, @filename 참조 |

### 경쟁사별 상세 분석

#### ChatGPT Deep Research (Feb 2026 리디자인) — 3패널 풀스크린 문서 뷰어

2026년 2월 10일, OpenAI는 Deep Research의 UI를 전면 리디자인했다 [^1][^2]. 핵심 변경은 풀스크린 문서 뷰어의 도입이다. 이 뷰어는 채팅 창과 분리된 독립적인 읽기 환경을 제공한다.

**레이아웃**: 좌측에 Table of Contents가 배치되어 문서 섹션 간 점프를 지원하고, 중앙에 AI 생성 리포트 본문이 렌더링되며, 우측에 확장 가능한 인용(Citations) 패널이 위치한다. 3패널 구조는 학술 논문 뷰어나 법률 문서 리더와 유사한 UX를 AI 리서치 리포트에 적용한 것이다.

**인터랙션**: 리서치 시작 전 계획을 편집할 수 있고, 진행 중 실시간으로 어떤 쿼리가 실행 중이고 어떤 사이트를 방문 중인지 추적할 수 있다. 리서치 범위를 중간에 조정하거나 소스를 추가할 수 있다. 완료된 리포트는 Markdown, Word, PDF로 내보내기가 가능하다.

**왜 이 방식인가**: Deep Research는 수십 분에 걸쳐 수백 개의 소스를 분석하여 긴 리포트를 생성한다. 채팅 내 마크다운으로는 긴 문서의 탐색이 어렵고, 출처 검증이 불편하다. 3패널 구조는 (1) TOC로 빠른 섹션 탐색, (2) 본문에서 읽기 몰입, (3) 인용 패널로 출처 즉시 검증이라는 세 가지 핵심 니즈를 동시에 충족한다. GPT-5.2 모델 업그레이드와 함께 출시되어 리포트 정확도도 향상되었다.

*참고 URL*: https://www.macrumors.com/2026/02/11/chatgpt-deep-research-mode-document-viewer/

#### Google Gemini Deep Research — 인터랙티브 시각화 + Granular Sourcing

Gemini Deep Research는 2026년 들어 정적 리포트를 넘어 인터랙티브 시각 리포트를 생성하는 방향으로 진화했다 [^7][^10]. 차트, 다이어그램, 인터랙티브 시뮬레이터가 리포트에 직접 임베딩되며, Canvas에서 추가 생성·수정이 가능하다. Gmail, Google Drive, 채팅 이력에서 정보를 자동 수집하여 개인화된 리포트를 만든다.

인용 시스템은 "granular sourcing"을 표방하여, 개별 주장 수준에서 출처를 제공한다. Sources 패널은 링크, 문서, 파일 등 모델이 참조한 소스의 스냅샷을 표시하며, 사용자가 데이터 출처를 직접 검증할 수 있게 한다 [^6].

**왜 이 방식인가**: Google은 "인터랙티브 데이터 탐색"을 핵심 가치로 본다. 정적 텍스트 리포트보다는 사용자가 차트를 조작하고 데이터를 드릴다운할 수 있는 대시보드형 산출물이 더 가치 있다고 판단한다. Dynamic View(Generative UI)와의 통합으로 리포트 형태 자체를 AI가 동적으로 결정한다.

*참고 URL*: https://gemini.google/overview/deep-research/

#### Perplexity — Citation-Forward 설계

Perplexity는 "Citation-Forward" 철학으로 AI 검색의 신뢰성 문제를 정면으로 공략한다 [^5][^11]. 모든 응답에 인라인 각주 번호가 표시되며, 이를 클릭하면 원본 소스의 확장형 스니펫이 표시된다. Sources 패널은 번호 인용과 함께 원본 사이트의 제목, URL, 관련 발췌문을 보여준다.

Pages 기능은 리서치 결과를 구조화된 장문 문서로 변환하며, 섹션별 헤딩, 인용, 멀티미디어 요소를 포함한다. Library 탭에서 저장된 리서치와 Pages에 접근할 수 있다.

**왜 이 방식인가**: Perplexity는 "AI 환각"의 가장 큰 해독제가 "출처 투명성"이라고 본다. 모든 주장에 출처를 달아 사용자가 즉시 검증할 수 있게 하는 것이 핵심 UX이다. 이 접근은 엔터프라이즈 환경에서 AI 리포트의 신뢰성 확보에 직접 적용 가능하다.

*참고 URL*: https://www.unusual.ai/blog/perplexity-platform-guide-design-for-citation-forward-answers

#### Notion — Floating TOC + 인라인 AI 편집

Notion은 heading 기반의 floating Table of Contents를 문서 우측에 자동 표시한다 [^3][^4]. H1/H2/H3 레벨의 헤딩이 문서에 존재하면 TOC가 자동으로 생성되며, 클릭하면 해당 섹션으로 스크롤된다. 스크롤 스파이(scroll spy)로 현재 읽고 있는 섹션이 TOC에서 하이라이트된다.

AI 편집은 텍스트 선택 후 드롭다운에서 요약, 번역, 톤 변경 등을 수행하며, @멘션으로 다른 Notion 페이지를 참조하여 컨텍스트를 자동 로드한다. 2026년에는 GPT-5, Claude Opus 4.1, o3 등 다수의 모델을 토글할 수 있게 되었다.

**왜 이 방식인가**: Notion은 "마크다운-중심" 워크스페이스이므로, TOC는 heading 파싱으로 자연스럽게 생성된다. 별도의 인용 시스템보다는 @멘션 기반의 워크스페이스 내 참조를 강조하며, AI는 편집 보조 도구로 위치한다.

*참고 URL*: https://www.notion.com/help/navigate-with-the-sidebar

#### Claude Artifacts — 반스크린 기본 + 풀스크린 확장

Claude Artifacts는 Side Panel 레이아웃에서 대화 옆에 산출물을 표시한다 [^8]. 2025년 중반부터 반스크린(half screen) 팝업이 기본이 되었고, 사용자가 필요 시 풀스크린으로 확장할 수 있다. 인라인 코드 실행(HTML/CSS/JS, React, Mermaid), 버전 히스토리, Shareable Link, 원클릭 웹 퍼블리시를 지원한다.

**왜 이 방식인가**: Claude는 "대화와 산출물의 자연스러운 공존"을 강조한다. 반스크린이 기본이어서 대화 맥락을 유지하면서 산출물을 확인할 수 있고, 집중이 필요할 때만 풀스크린으로 전환한다. TOC나 인용 패널은 별도로 제공하지 않으며, 산출물 자체의 렌더링 품질에 집중한다.

*참고 URL*: https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them

#### Microsoft Copilot Word — Navigation Pane + Agent Mode

Microsoft Word의 Navigation Pane(탐색 창)은 문서의 heading 구조를 좌측 사이드바에 트리 형태로 표시하는 오래된 기능이다 [^12]. Copilot Agent Mode는 이 기존 UI 위에 AI 기능을 추가하여, 자연어로 문서 초안 생성, 섹션 재구성, 스타일 적용 등을 수행한다.

**왜 이 방식인가**: Microsoft는 수십 년간 검증된 Office UI 위에 AI를 레이어링하는 전략을 취한다. Navigation Pane의 heading 트리, 검색, 페이지/heading/결과 탭 전환은 복잡한 문서 탐색의 표준이다.

*참고 URL*: https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-word-excel-and-powerpoint-agents-in-microsoft-365-copilot/4470604

---

## 패턴 분류 및 트레이드오프

### 패턴 A: Embedded Viewer (라이브러리 기반 렌더링)

문서를 웹 표준(HTML, Canvas, WebGL)으로 렌더링하는 오픈소스 또는 상용 라이브러리를 사용한다. `react-pdf`, `docx-preview`, `SheetJS` 같은 라이브러리로 클라이언트 사이드에서 바이너리 파일을 직접 렌더링한다.

- **대표**: KonaI-Agent 현재 구현, 웹 기반 문서 포털
- **장점**: 빠른 구현 (1~2주), 가벼움, 모바일 친화적, 오픈소스 활용 시 무료, PDF는 매우 정확한 렌더링
- **단점**: 복잡한 DOCX/XLSX (병합 셀, 고급 서식) 렌더링 부정확, 대용량 파일 성능 저하, WYSIWYG 편집 어려움
- **적합한 상황**: PDF 뷰잉, 간단한 DOCX 미리보기, 빠른 MVP, 모바일 대응 필요 시

### 패턴 B: 3-Panel Research Viewer (TOC + Doc + Citation)

문서를 좌측 TOC, 중앙 본문, 우측 인용 패널의 3패널 구조로 표시한다. AI 리서치 리포트, 학술 논문, 법률 문서에 최적화된 레이아웃이다.

- **대표**: ChatGPT Deep Research (2026-02 리디자인)
- **장점**: 긴 문서의 빠른 탐색, 출처 즉시 검증, 몰입감 있는 읽기 경험, 전문 리포트 느낌
- **단점**: 넓은 화면 필요 (최소 1024px+), 모바일에서 패널 축소/숨김 필요, 구현 복잡도 증가
- **적합한 상황**: AI 생성 리서치 리포트, 인용이 중요한 문서, 전문가용 데스크톱 환경

### 패턴 C: Floating TOC + Inline Citation (인라인 통합형)

TOC를 floating 위젯으로, 인용을 인라인 각주로 표시하여 별도 패널 없이 문서 내에 통합한다.

- **대표**: Notion (floating TOC), Perplexity (인라인 각주)
- **장점**: 화면 공간 효율적, 모바일 친화적, 구현 상대적으로 단순
- **단점**: TOC와 인용을 동시에 볼 수 없음, 많은 인용 시 문서가 복잡해짐
- **적합한 상황**: 일반 문서 편집기, 모바일 우선, 간단한 인용 구조

### 패턴 D: Fullscreen Takeover + Embedded Visualization

문서가 전체 화면을 점유하면서 차트, 시뮬레이터 등 인터랙티브 요소를 임베딩한다.

- **대표**: Gemini Deep Research (인터랙티브 시각화), Manus AI (풀스크린 앱), Gamma (인터랙티브 슬라이드)
- **장점**: 최대 몰입감, 인터랙티브 데이터 탐색, 프레젠테이션 품질
- **단점**: 대화 맥락 완전 분리, 컨텍스트 전환 비용 높음, 단순 문서에는 과도
- **적합한 상황**: 대시보드, 인터랙티브 리포트, 프레젠테이션 최종 프리뷰

### 트레이드오프 요약

| 차원 | Embedded Viewer | 3-Panel Research | Floating+Inline | Fullscreen+Viz |
|------|:--------------:|:----------------:|:---------------:|:--------------:|
| 구현 속도 | 빠름 (1~2주) | 중간 (3~4주) | 빠름 (1~2주) | 느림 (4주+) |
| 문서 탐색성 | 낮음 | 높음 (TOC) | 중간 (floating) | 높음 |
| 출처 검증 | 없음 | 높음 (패널) | 중간 (인라인) | 중간 |
| 화면 공간 | 효율적 | 넓은 화면 필요 | 효율적 | 전체 점유 |
| 모바일 지원 | 우수 | 약함 | 우수 | 약함 |
| 읽기 몰입감 | 낮음 | 높음 | 중간 | 최고 |
| 기존 코드 활용 | 현재 구현 | 확장 필요 | 확장 필요 | 대규모 변경 |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 파일 경로 | 확장 활용 가능성 |
|----------|---------|---------------|
| DocumentViewer.tsx (라우터) | `src/.../DocumentViewer/DocumentViewer.tsx` (76줄) | fileType 분기로 TOC 추출 로직 추가 가능 |
| PDFViewer.tsx | `src/.../DocumentViewer/PDFViewer.tsx` (134줄) | react-pdf의 `getTextContent()` API로 heading 파싱 가능 |
| DOCXViewer.tsx | `src/.../DocumentViewer/DOCXViewer.tsx` (132줄) | docx-preview 렌더링 후 DOM에서 heading 추출 가능 |
| DocumentViewerToolbar.tsx | `src/.../DocumentViewer/DocumentViewerToolbar.tsx` (225줄) | 풀스크린 토글 버튼 추가 지점 (이미 maximize 아이콘 존재) |
| ArtifactPreviewPanel.tsx | `src/.../ArtifactPreviewPanel/ArtifactPreviewPanel.tsx` (194줄) | isMaximized 상태 이미 존재, 풀스크린 확장 자연스러움 |
| ArtifactPanelContext.tsx | `src/.../context/ArtifactPanelContext.tsx` (218줄) | isMaximized, toggleMaximize 이미 구현, TOC/Citation 상태 추가 가능 |
| ArtifactPanelHeader.tsx | `src/.../ArtifactPreviewPanel/ArtifactPanelHeader.tsx` (73줄) | 액션 버튼 그룹에 TOC/Citation 토글 추가 가능 |
| XLSXViewer/CSVViewer | `src/.../DocumentViewer/` | 테이블 데이터에는 TOC 불필요, 인용 패널만 해당 |

### 권장 접근: 점진적 3-Panel 확장 (Embedded Viewer → 3-Panel Research 하이브리드)

**패턴 선택 근거**:
1. 현재 Embedded Viewer (패턴 A)가 이미 구현 완료되어 기반이 견고함
2. ChatGPT Deep Research의 3-Panel 구조(패턴 B)가 2026년 표준이 되고 있음
3. 풀스크린 토글은 이미 isMaximized 상태가 존재하여 확장 비용이 낮음
4. 엔터프라이즈 환경(데스크톱 중심)에서 3패널은 자연스러움

**Phase 1 — TOC 사이드바 (1~2주)**:
- heading 추출 유틸리티: PDF(pdfjs `getTextContent` API로 폰트 크기 기반 heading 감지), DOCX(렌더링된 DOM에서 `h1`~`h6` 추출), Markdown(heading regex 파싱)
- `DocumentTOCSidebar` 컴포넌트: 접이식(collapsible) 좌측 사이드바, heading 계층 표시, 클릭 시 해당 위치로 smooth scroll
- 스크롤 스파이: IntersectionObserver로 현재 보이는 섹션을 TOC에서 하이라이트
- 토글: DocumentViewerToolbar에 TOC 아이콘 버튼 추가, 기본값은 접힘(좁은 화면에서 공간 절약)

**Phase 2 — 인용 사이드패널 (2~3주)**:
- `CitationSidePanel` 컴포넌트: 우측 확장형 패널, 인라인 각주 번호 클릭 시 해당 소스 카드로 스크롤
- 인라인 인용 마커: 문서 본문에 `[^N]` 스타일 각주 표시, 호버 시 소스 툴팁
- 소스 카드: 제목, URL, 발췌문, 신뢰도 표시
- 데이터 모델: `Citation { id, number, title, url, excerpt, relevance }` 인터페이스
- 초기에는 에이전트가 생성한 리포트의 소스 메타데이터를 파싱하여 표시

**Phase 3 — 풀스크린 토글 (1주)**:
- 기존 `isMaximized`를 확장하여 `viewMode: 'embedded' | 'maximized' | 'fullscreen'` 3단계 전환
- `embedded`: 현재 ArtifactPreviewPanel 내 표시 (기본)
- `maximized`: 현재 구현 유지 (패널 확장)
- `fullscreen`: React Portal로 뷰포트 전체 점유, ESC로 복귀
- DocumentViewerToolbar의 기존 maximize 아이콘 옆에 fullscreen 아이콘 추가
- CSS 기반 전환 (Fullscreen API 대신 Portal + z-index), 모바일에서도 동작

**Phase 4 — 내보내기 (1주)**:
- Markdown 내보내기: 리포트 본문의 마크다운 소스 다운로드
- PDF 내보내기: `window.print()` 기반 또는 `html2pdf.js` 활용
- DOCX 내보내기: `docx` npm 패키지(이미 설치됨)로 서버 사이드 변환

### 이 접근을 권장하는 이유

1. **최소 변경 원칙**: 기존 DocumentViewer 아키텍처(라우터 + 형식별 뷰어 + 공통 툴바)를 유지하고, 사이드바/패널을 컴포지션으로 추가
2. **ChatGPT 수준 UX**: 3패널 구조가 2026년 AI 리서치 도구의 표준이 되고 있어, 이를 지원하면 경쟁력 확보
3. **점진적 구현**: TOC → Citation → Fullscreen → Export 순서로, 각 단계가 독립적이어서 어느 시점에서든 멈출 수 있음
4. **기존 자산 최대 활용**: isMaximized, toggleMaximize, DocumentViewerToolbar의 버튼 그룹, ArtifactPanelContext의 상태 관리가 이미 존재

### Acceptance Criteria

- [ ] **TOC 사이드바**: PDF, DOCX, Markdown 문서에서 heading이 자동 추출되어 좌측 사이드바에 계층적으로 표시됨
- [ ] **스크롤 스파이**: 문서를 스크롤하면 TOC에서 현재 섹션이 하이라이트됨
- [ ] **TOC 점프**: TOC 항목 클릭 시 해당 섹션으로 smooth scroll
- [ ] **TOC 토글**: 툴바 버튼으로 TOC 사이드바 접기/펼치기 가능
- [ ] **인용 패널**: 에이전트 생성 리포트의 인용 소스가 우측 패널에 카드 형태로 표시됨
- [ ] **인라인 인용**: 본문의 각주 번호 클릭/호버 시 소스 정보 표시
- [ ] **풀스크린 토글**: 문서 뷰어를 풀스크린(뷰포트 전체)으로 전환 가능, ESC로 복귀
- [ ] **반응형**: 1024px 미만에서 TOC는 자동 숨김(토글로 오버레이 표시)
- [ ] **접근성**: TOC 항목에 aria-current, 풀스크린 토글에 aria-expanded, 키보드 내비게이션 지원
- [ ] **성능**: 50페이지 PDF에서 TOC 추출 ≤ 1초, 스크롤 스파이 프레임 드롭 없음

---

## Key Considerations

### TOC Heading 추출의 형식별 차이

PDF, DOCX, Markdown 각각 heading 추출 방식이 다르다. PDF는 텍스트 레이어에서 폰트 크기로 heading을 추론해야 하므로 정확도가 낮을 수 있다 — pdfjs의 `getTextContent()` API가 텍스트 아이템과 폰트 정보를 반환하지만, 일관된 heading 감지를 위해 폰트 크기 임계값 기반 휴리스틱이 필요하다. DOCX는 docx-preview가 렌더링한 HTML DOM에서 `h1`~`h6` 태그를 직접 쿼리할 수 있어 정확도가 높다. Markdown은 `#` 기반 heading 파싱이 가장 단순하고 정확하다. 형식별 heading 추출기를 별도 유틸리티로 분리하고, 공통 `TOCItem { id, level, text, element }` 인터페이스로 통합하는 것이 권장된다.

### 인용 데이터 모델과 에이전트 통합

인용 패널이 유의미하려면 에이전트가 리포트 생성 시 출처 메타데이터를 구조화하여 반환해야 한다. 현재 KonaI-Agent는 에이전트 응답에 출처 정보를 포함하지 않으므로, 초기에는 (1) 에이전트 응답의 마크다운 각주를 파싱하거나, (2) 하드코딩된 목업 데이터로 UI만 먼저 구현하고, 에이전트 통합은 별도 태스크로 분리하는 것이 현실적이다. Perplexity의 Citation-Forward 접근처럼 `Citation` 인터페이스를 미리 설계하고, 에이전트 응답 스키마에 `citations: Citation[]` 필드를 예약하는 것이 장기적으로 유리하다.

### 풀스크린 구현: Fullscreen API vs CSS Portal

웹 표준 Fullscreen API (`element.requestFullscreen()`)는 브라우저 네이티브 풀스크린을 제공하지만, 모바일 브라우저 호환성 이슈와 키보드 단축키 제약이 있다. 대안으로 React Portal + CSS(`position: fixed; inset: 0; z-index: 9999`)를 사용하면 브라우저 탭 내에서 "시각적 풀스크린"을 구현할 수 있어 호환성이 높고, ESC 핸들링도 React 이벤트로 처리할 수 있다. ChatGPT Deep Research의 풀스크린 뷰어도 브라우저 Fullscreen API가 아닌 CSS 기반 레이아웃 전환으로 구현된 것으로 보인다. KonaI-Agent에서도 CSS Portal 방식을 권장한다 — 기존 `isMaximized` 로직을 확장하기가 더 자연스럽다.

### 3패널 레이아웃의 반응형 전략

3패널(TOC + Doc + Citation)은 최소 1280px 이상의 뷰포트에서 가장 잘 작동한다. 1024px~1280px에서는 TOC 또는 Citation 중 하나를 오버레이로 전환하고, 768px 미만에서는 둘 다 숨기되 토글 버튼으로 접근 가능하게 한다. CSS Container Queries 또는 JavaScript ResizeObserver로 DocumentViewer의 실제 렌더링 영역 크기를 감지하는 것이 뷰포트 기준 미디어 쿼리보다 정확하다 — ArtifactPreviewPanel 내에서 렌더링되므로 뷰포트와 실제 가용 공간이 다를 수 있다.

---

## Recent Updates
<!-- 🤖 AUTO-APPEND ZONE — 자동화 시스템이 아래에 행을 추가합니다. 수동 편집 금지. -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-15 | 초판 작성 | 6개 경쟁사 분석, 4패턴 분류, Phase별 로드맵 수립 | New |
| 2026-02-16 | 업데이트 | 템플릿 스키마 정렬, 코드베이스 탐색 결과 반영, 라이브러리 비교 강화 | Update |
| 2026-02-21 | 업데이트 | ChatGPT Deep Research 3패널 뷰어(TOC+인용패널+풀스크린) 반영, Gemini/Perplexity/Notion 인용 시스템 분석 추가, Phase 구조를 TOC→Citation→Fullscreen→Export로 재편, 현재 코드베이스(Phase 1+2 완료) 반영 | Major Update |

---

## References

### Vault
- artifacts-canvas-patterns.md — Artifacts/Canvas 레이아웃 4종, 편집 패턴, 트리거 전략
- artifact-panel-layout.md — 아티팩트 패널 레이아웃 설계 (관련 패턴)

### External

[^1]: ChatGPT's Deep Research Mode Gets a Fullscreen Document Viewer. MacRumors. https://www.macrumors.com/2026/02/11/chatgpt-deep-research-mode-document-viewer/

[^2]: ChatGPT Launches Full-Screen Document Viewer for Deep Research Reports. Android Headlines. https://www.androidheadlines.com/2026/02/chatgpt-deep-research-full-screen-document-viewer-update.html

[^3]: Navigate with the sidebar. Notion Help Center. https://www.notion.com/help/navigate-with-the-sidebar

[^4]: The New "Floating" Notion Table of Content or Page Navigation. Simple.ink. https://www.simple.ink/guides/the-new-floating-notion-table-of-content-or-page-navigation

[^5]: Perplexity Platform Guide: Design for Citation-Forward Answers. Unusual AI. https://www.unusual.ai/blog/perplexity-platform-guide-design-for-citation-forward-answers

[^6]: Gemini Deep Research Sources Panel: Citation System Explained. Skywork AI. https://skywork.ai/blog/ai-agent/gemini-sources-panel/

[^7]: Bring your research to life with integrated visual reports from Gemini Deep Research. Google Blog. https://blog.google/products/gemini/visual-reports/

[^8]: What are artifacts and how do I use them? Claude Help Center. https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them

[^9]: Making Fullscreen Experiences. web.dev. https://web.dev/fullscreen/

[^10]: Gemini Deep Research — your personal research assistant. Google. https://gemini.google/overview/deep-research/

[^11]: Introducing Perplexity Pages. Perplexity Blog. https://www.perplexity.ai/hub/blog/perplexity-pages

[^12]: Introducing Word, Excel, and PowerPoint Agents in Microsoft 365 Copilot. Microsoft Community Hub. https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-word-excel-and-powerpoint-agents-in-microsoft-365-copilot/4470604

---

*Last synthesized: 2026-02-21 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
