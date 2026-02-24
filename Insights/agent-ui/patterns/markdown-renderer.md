---
type: insight-synthesis
topic_id: "markdown-renderer"
topic_name: "마크다운 렌더러 구현 전략"
category: agent-ui
document_level: specific
parent_broad:
  - "conversational-ui-patterns"
catalog_components:
  - "markdown_renderer"
  - "code_block"
  - "mermaid_diagram"
tags:
  - insight
  - agent-ui
  - pattern
  - markdown
  - syntax-highlighting
  - streaming
  - react-markdown
status: draft
confidence: high
last_updated: "2026-02-24"
source_products:
  - "openai"
  - "claude"
  - "vercel-v0"
  - "cursor"
  - "google-gemini"
  - "perplexity"
  - "librechat"
  - "copilotkit"
source_files: []
auto_update:
  enabled: true
  keywords:
    - react-markdown
    - streamdown
    - shiki
    - syntax highlighting
    - markdown rendering
    - code block
    - mermaid
    - katex
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 마크다운 렌더러 구현 전략

## TL;DR

- **react-markdown + unified 생태계가 AI 채팅 마크다운 렌더링의 사실상 표준**이다. ChatGPT, LibreChat, CopilotKit, assistant-ui 등 주요 제품과 프레임워크가 모두 react-markdown 기반이며, remark/rehype 플러그인 체계로 GFM 테이블, 수식, 다이어그램까지 확장한다[^1][^2][^3]
- **Vercel Streamdown(2025)은 react-markdown의 스트리밍 한계를 해결한 드롭인 대체제**로 부상 중이다. 미완성 마크다운 자동 복구, Shiki 코드 하이라이팅, KaTeX 수식, Mermaid 다이어그램을 내장하며, 무거운 컴포넌트는 React.lazy()로 지연 로딩하여 번들 크기를 최적화한다[^4][^5]
- **코드 구문 강조는 Shiki가 업계 표준으로 수렴**했다. VS Code와 동일한 TextMate 문법을 사용하여 정확도가 높고, WASM 기반으로 서버/클라이언트 모두 동작한다. Prism은 레거시화 진행 중이나 번들 크기에서 여전히 유리하다[^6][^7]
- **KonaI-Agent는 기존 react-markdown + remark-gfm 자산을 활용하되, Shiki 코드 하이라이팅과 KaTeX 수식 지원을 추가하는 점진적 접근이 최적**이다. MarkdownPreviewPanel의 markdownComponents.tsx를 확장하고, ChatBubble의 수동 파싱을 react-markdown으로 교체하여 일관된 렌더링 파이프라인을 구축해야 한다[^8]
- **Mermaid 다이어그램은 dynamic import로 지연 로딩**하여 기본 번들에 포함하지 않는 것이 모든 구현체의 공통 패턴이다. markdown_renderer의 코드블록 렌더러가 `language-mermaid`를 감지하면 Mermaid 렌더러로 위임하는 구조가 권장된다[^4][^9]

---

## Overview

마크다운 렌더링은 AI 에이전트 채팅 인터페이스에서 가장 기본적이면서도 가장 많은 후속 기능에 영향을 미치는 핵심 인프라다. 에이전트 응답은 일반 텍스트, 코드 블록, 테이블, 수식, 다이어그램 등 다양한 형식을 포함하며, 이를 정확하고 일관되게 렌더링하는 것이 사용자 경험의 기반이 된다.

KonaI-Agent 프로젝트에서 markdown_renderer는 **3개 후속 컴포넌트(streaming_typing, code_block, mermaid_diagram)의 의존성**이며, artifact_panel의 MarkdownRenderer와 chat_view의 메시지 렌더링 모두에서 사용된다. 현재 ChatBubble 컴포넌트가 수동 regex로 **\*\*bold\*\*** 와 리스트만 처리하고 있어, GFM 테이블, 코드 블록 구문 강조, 수식 등은 미지원 상태다. react-markdown v10.1.0과 remark-gfm v4.0.1은 이미 설치되어 있으므로, 이를 활용한 통합 마크다운 렌더링 파이프라인 구축이 시급하다.

---

## 경쟁사 구현 분석

### 비교 매트릭스

| Product | 마크다운 라이브러리 | 코드 하이라이팅 | 수식 (LaTeX) | 테이블 | Mermaid | 스트리밍 호환 | Source |
|---------|----------------|--------------|------------|--------|---------|------------|--------|
| **ChatGPT** | react-markdown + rehype | Prism.js (추정) | KaTeX | GFM | 미지원 | Token-level progressive | [^1] |
| **Claude.ai** | 커스텀 렌더러 | 커스텀 (Shiki 계열) | KaTeX | GFM | 미지원 | Chunk-based deferred | [^10] |
| **Vercel v0 / Streamdown** | Streamdown (커스텀) | Shiki (내장) | KaTeX (내장) | GFM | Mermaid (내장) | 전용 스트리밍 엔진 | [^4][^5] |
| **Cursor** | 커스텀 (Monaco 기반) | Shiki / Monaco | 미지원 | 제한적 | 미지원 | Token-level + diff | [^11] |
| **Google Gemini** | 커스텀 (Dynamic View) | 브라우저 네이티브 | 미지원 | HTML 테이블 | 미지원 | Dynamic UI 생성 | [^12] |
| **Perplexity** | react-markdown (추정) | Prism / highlight.js | KaTeX | GFM | 미지원 | Chunk-based | [^13] |
| **LibreChat** | react-markdown + rehype | highlight.js → Shiki 전환 중 | KaTeX | GFM | Mermaid 플러그인 | Progressive | [^14] |
| **CopilotKit** | react-markdown (슬롯 기반) | Shiki | KaTeX | GFM | 미지원 | 스트리밍 최적화 | [^3] |

### 경쟁사별 상세 분석

#### ChatGPT — react-markdown + Progressive Parsing

ChatGPT는 react-markdown을 핵심 렌더링 엔진으로 사용하며, 토큰이 도착할 때마다 전체 마크다운을 재파싱하는 Progressive Parsing 방식을 채택한다. 미완성 마크다운(예: `**bold` 닫기 전)은 일반 텍스트로 폴백 렌더링하고, 다음 토큰에서 완성되면 재해석한다. 코드 블록에는 언어 감지와 Prism 기반 구문 강조가 적용되며, Copy 버튼이 코드 블록 우상단에 배치된다.

**왜 이 방식인가**: 빠른 응답감(latency perception)을 최우선 가치로 두며, 마크다운 정확성보다 즉각적 피드백을 선택했다. 일반 대화 맥락에서 사용자는 완벽한 포맷팅보다 빠른 응답 시작을 더 가치 있게 느낀다.

*참고 URL*: [OpenAI Community: Streaming Markdown](https://community.openai.com/t/streaming-markdown-or-other-formatted-text/510268)

#### Vercel Streamdown — 스트리밍 전용 마크다운 엔진

Vercel이 2025년 발표한 Streamdown은 react-markdown의 드롭인 대체제로, AI 스트리밍 환경에 특화되었다. 핵심 혁신은 **미완성 마크다운 자동 복구**: 버퍼링된 토큰에 정규식 기반 복구 규칙을 적용하여 닫히지 않은 코드 블록, 불완전한 테이블 등을 자동으로 보정한다. Shiki를 내장하여 코드 하이라이팅을 제공하고, KaTeX와 Mermaid도 내장하되 React.lazy()로 지연 로딩하여 번들 크기를 최적화한다. v2.3에서는 자체 커스텀 마크다운 렌더러로 전환하여 react-markdown 의존성을 제거했다.

**왜 이 방식인가**: react-markdown은 정적 마크다운에 최적화되어 있어, 스트리밍 중 불완전한 입력에서 깨지거나 깜빡이는 문제가 빈번하다. Streamdown은 이 문제를 전용 버퍼링/복구 레이어로 해결하여, 스트리밍과 마크다운 정확성을 동시에 달성한다.

*참고 URL*: [Vercel: Introducing Streamdown](https://vercel.com/changelog/introducing-streamdown) | [GitHub: vercel/streamdown](https://github.com/vercel/streamdown)

#### Claude.ai — Chunk 기반 Deferred Rendering

Claude는 마크다운 블록(문단, 코드 블록, 리스트 등)을 완성 단위로 스트리밍하여, 불완전한 마크다운이 사용자에게 노출되지 않도록 한다. 코드 블록은 언어별 정확한 구문 강조를 적용하며, Extended Thinking 블록은 별도의 collapsible 섹션으로 분리한다. Artifacts 시스템에서는 마크다운 렌더링 결과를 우측 패널에 표시하여 대화와 산출물을 분리한다.

**왜 이 방식인가**: 기술 문서와 코드가 주요 사용 사례이므로, 마크다운 정확성이 응답 속도보다 중요하다. 불완전한 코드 블록이나 깨진 테이블은 사용자 신뢰를 해치므로, 완성된 블록만 렌더링하는 전략을 선택했다.

*참고 URL*: [Claude Extended Thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)

#### CopilotKit — 슬롯 기반 커스터마이징

CopilotKit v1.50은 react-markdown을 기반으로 하되, 슬롯 기반 아키텍처로 개별 마크다운 요소의 렌더링을 호스트 앱이 완전히 커스터마이징할 수 있게 한다. components prop을 통해 모든 HTML 요소(h1, a, img, code 등)를 커스텀 React 컴포넌트로 교체 가능하며, 이를 통해 호스트 앱의 디자인 시스템과 일관된 마크다운 렌더링을 달성한다.

**왜 이 방식인가**: CopilotKit은 다양한 앱에 임베딩되는 SDK이므로, 각 호스트 앱의 디자인 시스템에 맞출 수 있는 유연성이 핵심이다. react-markdown의 components prop이 이 요구를 완벽히 충족한다.

*참고 URL*: [CopilotKit: Markdown Rendering](https://docs.copilotkit.ai/custom-look-and-feel/markdown-rendering)

#### LibreChat — 오픈소스 ChatGPT 클론

LibreChat은 react-markdown + rehype 체계를 사용하며, 코드 하이라이팅은 highlight.js에서 Shiki로 전환 중이다. Mermaid 다이어그램을 플러그인으로 지원하며, KaTeX를 통한 수식 렌더링도 포함한다. 오픈소스 프로젝트 중 가장 완성도 높은 마크다운 렌더링 파이프라인을 보유하고 있어 구현 참조로 적합하다.

**왜 이 방식인가**: ChatGPT와 동일한 사용자 경험을 목표로 하므로, ChatGPT의 기술 스택(react-markdown)을 채택하고 커뮤니티 기여를 통해 점진적으로 개선한다.

*참고 URL*: [LibreChat: Syntax Highlighting](https://www.librechat.ai/docs/documentation/syntax_highlighting) | [GitHub: LibreChat](https://github.com/danny-avila/LibreChat)

#### assistant-ui — AI 채팅 컴포넌트 라이브러리

assistant-ui는 react-markdown 기반의 `makeMarkdownText` 헬퍼를 제공하여, remark/rehype 플러그인을 한 번에 구성할 수 있게 한다. Shiki 코드 하이라이팅과 KaTeX 수식을 공식 문서에서 가이드하며, 컴포넌트 커스터마이징을 위한 깔끔한 API를 제공한다.

**왜 이 방식인가**: AI 채팅 UI의 재사용 가능한 빌딩 블록을 목표로 하며, react-markdown의 확장성을 최대한 활용하여 다양한 프로젝트에 적용 가능한 범용 솔루션을 지향한다.

*참고 URL*: [assistant-ui: LaTeX](https://www.assistant-ui.com/docs/guides/Latex)

---

## 패턴 분류 및 트레이드오프

### 패턴 A: react-markdown + 플러그인 체계

react-markdown을 핵심 렌더러로 사용하고, remark/rehype 플러그인으로 기능을 확장하는 접근. 가장 보편적이며 생태계가 풍부하다.

- **대표**: ChatGPT, LibreChat, CopilotKit, assistant-ui
- **장점**: 거대한 플러그인 생태계 (remark-gfm, remark-math, rehype-katex, rehype-highlight 등), 커뮤니티 지원 풍부, components prop으로 완전한 렌더링 커스터마이징, 보안 기본 내장 (HTML sanitize)
- **단점**: 스트리밍 환경에서 불완전한 마크다운 처리 미흡, 매 토큰마다 전체 재파싱으로 성능 이슈 가능, 복잡한 테이블/수식에서 불안정 가능
- **적합한 상황**: 정적 또는 준정적(chunk-based) 마크다운 렌더링, 기존 react-markdown 자산이 있는 프로젝트, 플러그인 확장이 중요한 경우

### 패턴 B: Streamdown (스트리밍 전용 엔진)

Vercel이 개발한 react-markdown 대체 라이브러리. 스트리밍 환경에 특화된 미완성 마크다운 복구와 지연 로딩을 내장한다.

- **대표**: Vercel v0, AI Elements
- **장점**: 스트리밍에 최적화된 버퍼링/복구, Shiki + KaTeX + Mermaid 내장, React.lazy()로 번들 최적화, react-markdown 드롭인 대체 (마이그레이션 용이)
- **단점**: 2025년 발표로 생태계가 아직 작음, Vercel 종속 리스크, 커스텀 플러그인 확장성이 react-markdown보다 제한적, 수식 렌더링에 일부 이슈 보고됨
- **적합한 상황**: 실시간 스트리밍이 핵심인 AI 채팅, Shiki + KaTeX + Mermaid 올인원이 필요한 경우, 빠른 구축이 중요한 경우

### 패턴 C: 커스텀 마크다운 파서

자체 마크다운 파서를 구축하거나 low-level 라이브러리(unified, micromark)를 직접 사용하는 접근.

- **대표**: Claude.ai, Cursor (부분적)
- **장점**: 완전한 제어권, 스트리밍 최적화 극대화, 제품 요구사항에 완벽히 맞는 파싱 전략
- **단점**: 구현 비용 매우 높음, 마크다운 스펙 완전 지원까지 시간 소요, 유지보수 부담
- **적합한 상황**: 대규모 팀이 장기 투자 가능한 경우, 극도로 특수한 요구사항, 성능이 절대적으로 중요한 경우

### 트레이드오프 요약

| | 구현 비용 | 스트리밍 호환 | 플러그인 확장 | 번들 크기 | 커뮤니티/생태계 | 커스터마이징 |
|---|---|---|---|---|---|---|
| **패턴 A (react-markdown)** | Low | Medium | Excellent | Medium | Excellent | Excellent |
| **패턴 B (Streamdown)** | Low | Excellent | Limited | Optimized | Growing | Good |
| **패턴 C (커스텀)** | Very High | Excellent | N/A | Minimal | None | Full |

---

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 기존 자산 | 위치 | 활용 가능성 |
|----------|------|-----------|
| react-markdown v10.1.0 | package.json | 핵심 렌더링 엔진으로 즉시 활용 |
| remark-gfm v4.0.1 | package.json | GFM 테이블, 태스크 리스트, 취소선 지원 |
| @tailwindcss/typography | package.json (devDeps) | prose 클래스로 기본 타이포그래피 스타일링 |
| markdownComponents.tsx | MarkdownPreviewPanel/ | h1-h4, code, table, list 등 커스텀 컴포넌트 정의. 확장하여 재사용 |
| MarkdownPreviewPanel.tsx | MarkdownPreviewPanel/ | Artifact 패널용 마크다운 미리보기/편집. 렌더링 로직 공유 가능 |
| ChatBubble.tsx | shared/atoms/ | 수동 마크다운 파싱 → react-markdown으로 교체 대상 |
| AgentResponse 컴포넌트들 | AgentResponse/ | `prose prose-sm` 클래스 사용 중. 마크다운 렌더러 통합 대상 |
| StreamingText.tsx | shared/ | 문자 단위 애니메이션. 마크다운 렌더러와 통합 필요 |
| globals.css | app/ | prose 커스텀 오버라이드 없음. 마크다운 전용 스타일 추가 필요 |

### 권장 접근: react-markdown + Shiki 점진적 확장

KonaI-Agent의 현재 상태(react-markdown 이미 설치, 데모/MVP 단계)를 고려할 때, 패턴 A(react-markdown + 플러그인)를 기반으로 하되, Shiki 코드 하이라이팅을 추가하는 것이 최적이다. Streamdown(패턴 B)은 실제 스트리밍 백엔드 구현 시점(Phase 2)에서 마이그레이션을 검토한다.

**Phase 1 (MVP — markdown_renderer 컴포넌트 구현)**:
- 통합 `MarkdownRenderer` 컴포넌트 생성 (ChatBubble, AgentResponse, ArtifactPanel 공통)
- react-markdown + remark-gfm 활용한 GFM 완전 지원 (테이블, 태스크 리스트, 취소선, 자동 링크)
- markdownComponents.tsx 확장: 코드 블록에 Copy 버튼 추가, 테이블에 수평 스크롤 래퍼
- @tailwindcss/typography의 prose 클래스를 기반으로 한 일관된 타이포그래피
- ChatBubble의 수동 파싱을 MarkdownRenderer로 교체

**Phase 2 (확장 — code_block + 수식)**:
- Shiki를 rehype-shiki 또는 커스텀 code 컴포넌트를 통해 통합. 라이트/다크 테마 지원
- remark-math + rehype-katex로 LaTeX 수식 렌더링 (KaTeX CSS lazy-loading)
- 코드 블록 라인 넘버, 라인 하이라이팅 지원
- "Artifact에서 열기" 버튼으로 코드 블록을 우측 패널로 전송

**Phase 3 (고급 — mermaid_diagram + streaming)**:
- Mermaid 다이어그램을 `language-mermaid` 코드 블록 감지로 dynamic import 렌더링
- 실제 SSE/WebSocket 스트리밍 연동 시 Streamdown 마이그레이션 검토
- 미완성 마크다운 복구 로직 (스트리밍 환경)
- Extended Thinking 블록 collapsible 렌더링

### 이 접근을 권장하는 이유

1. **기존 자산 최대 활용**: react-markdown, remark-gfm, @tailwindcss/typography가 이미 설치되어 있어, 새 라이브러리 도입 없이 Phase 1 완성 가능
2. **markdownComponents.tsx 재사용**: Artifact 패널용으로 이미 구축된 커스텀 컴포넌트(h1-h4, table, code, list)를 채팅 메시지에도 공유하여 일관성 확보
3. **점진적 복잡도 관리**: Phase 1은 추가 패키지 없이 구현 가능, Phase 2에서 Shiki + KaTeX 추가, Phase 3에서 Mermaid + 스트리밍
4. **후속 컴포넌트 언블로킹**: streaming_typing, code_block, mermaid_diagram이 모두 markdown_renderer에 의존하므로, Phase 1 완성이 3개 컴포넌트의 구현을 동시에 가능하게 함
5. **Streamdown 마이그레이션 경로 확보**: react-markdown의 components prop 패턴은 Streamdown에서도 동일하므로, 향후 드롭인 교체 가능

### Acceptance Criteria

- [ ] 통합 `MarkdownRenderer` 컴포넌트가 chat_view와 artifact_panel 양쪽에서 사용 가능
- [ ] GFM 완전 지원: 테이블(수평 스크롤, 스트라이핑), 태스크 리스트(체크박스), 취소선, 자동 링크
- [ ] 헤딩(h1-h6)이 시각적으로 구분되며, 적절한 크기/간격/색상 적용
- [ ] 코드 블록: 언어 라벨 표시, Copy 버튼, monospace 폰트, 배경색 구분
- [ ] 인라인 코드: 본문 내 `code` 텍스트가 배경색과 monospace로 구분
- [ ] 블록쿼트: 좌측 보더 + 배경색으로 인용 구분
- [ ] 이미지: 마크다운 이미지 구문이 `<img>` 태그로 렌더링 (max-width 제한)
- [ ] 링크: 외부 링크가 새 탭에서 열리며, 시각적으로 구분
- [ ] 중첩 마크다운: 리스트 안 볼드, 코드 안 볼드 등 중첩 구문 정상 처리
- [ ] ChatBubble의 기존 수동 파싱이 MarkdownRenderer로 완전 교체
- [ ] 보안: HTML sanitize 기본 적용 (react-markdown 기본 동작 유지)
- [ ] 성능: 10KB 이상 응답에서도 렌더링 지연 200ms 미만 (React.memo 활용)

---

## Key Considerations

### 코드 구문 강조 기술 선택: Shiki vs Prism

| 기준 | Shiki | Prism |
|------|-------|-------|
| 정확도 | VS Code와 동일 (TextMate 문법) | 자체 문법 (일부 부정확) |
| 언어 지원 | 200+ 언어 (VS Code 전체) | 300+ 언어 (경량 플러그인) |
| 테마 | VS Code 테마 직접 사용 | 자체 테마 시스템 |
| 번들 크기 | ~3MB WASM (지연 로딩 필수) | ~20KB 코어 + 언어별 추가 |
| 스트리밍 호환 | 토큰 단위 하이라이팅 가능 | 전체 코드 필요 |
| 유지보수 | 활발 (Vercel 후원) | 유지보수 모드 |
| SSR | WASM 기반 서버 실행 가능 | 브라우저 전용 |

**권장**: Shiki를 선택하되 지연 로딩으로 초기 번들 영향 최소화. Phase 1에서는 구문 강조 없이 monospace + 배경색으로 시작하고, Phase 2에서 Shiki를 통합한다.

### 마크다운 보안

- react-markdown은 기본적으로 HTML을 렌더링하지 않으므로 XSS에 안전하다
- `rehype-raw` 플러그인 사용 시 `rehype-sanitize`를 반드시 함께 사용
- AI 응답은 신뢰할 수 있으나, 사용자 입력 마크다운에는 별도 sanitizer 적용 권장
- `dangerouslySetInnerHTML` 사용 금지 — 현재 코드베이스에서도 마크다운 렌더링에는 사용하지 않음 (DOCXViewer만 예외)

### 성능 최적화

- **React.memo**: MarkdownRenderer를 memo로 감싸서 동일 content에 대한 재렌더링 방지
- **useMemo for plugins**: remark/rehype 플러그인 배열을 useMemo로 캐싱하여 매 렌더링마다 새 배열 생성 방지
- **Code 블록 지연 처리**: Shiki WASM 로딩은 첫 코드 블록 렌더링 시점에 트리거. 로딩 중에는 monospace 텍스트로 폴백
- **Mermaid 지연 로딩**: mermaid 패키지(~2MB)는 React.lazy() + Suspense로 첫 사용 시점에 로딩
- **KaTeX CSS 지연 로딩**: 수식이 포함된 메시지에서만 KaTeX CSS를 동적으로 `<link>` 삽입
- **대규모 응답**: 10KB 이상 마크다운에서는 가상화(virtualization)보다 전체 렌더링 + React.memo가 더 효과적 (마크다운 가상화는 블록 경계 판별이 복잡)

### 컴포넌트 구조 설계

```
src/components/shared/markdown/
├── MarkdownRenderer.tsx      ← 핵심 통합 컴포넌트 (react-markdown wrapper)
├── markdownComponents.tsx    ← 커스텀 컴포넌트 맵 (기존 MarkdownPreviewPanel 것을 이동/확장)
├── CodeBlock.tsx             ← 코드 블록 전용 컴포넌트 (Copy, 언어 라벨, Shiki Phase 2)
├── MermaidBlock.tsx          ← Mermaid 다이어그램 (dynamic import, Phase 3)
├── MathBlock.tsx             ← KaTeX 수식 (dynamic import, Phase 2)
└── index.ts
```

이 구조는 ChatBubble, AgentResponse, MarkdownPreviewPanel 등 모든 소비자가 동일한 `MarkdownRenderer`를 import하여 사용하도록 하여, 렌더링 일관성을 보장한다.

### Streamdown 마이그레이션 경로

향후 실제 스트리밍 구현 시점에서 Streamdown으로 마이그레이션을 검토할 경우:

1. `MarkdownRenderer.tsx`의 `<ReactMarkdown>` 호출을 `<Streamdown>` 으로 교체
2. `markdownComponents.tsx`의 커스텀 컴포넌트는 Streamdown에서도 components prop으로 동일하게 전달 가능
3. remark/rehype 플러그인은 Streamdown 내장 기능(Shiki, KaTeX, Mermaid)으로 대체
4. 미완성 마크다운 복구는 Streamdown이 자동 처리하므로 별도 로직 불필요

이 마이그레이션은 `MarkdownRenderer.tsx` 1개 파일만 수정하면 되므로, 현재 react-markdown 기반으로 구축해도 리스크가 낮다.

---

## Recent Updates
<!-- AUTO-APPEND ZONE -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-24 | 신규 생성 | react-markdown + Shiki 기반 마크다운 렌더러 구현 전략. 7개 제품 비교, 3개 패턴 분류, Phase 1-3 로드맵 | markdown, shiki, streaming |

---

## References

### Vault
- [^8]: 코드베이스 분석 — MarkdownPreviewPanel/markdownComponents.tsx, ChatBubble.tsx, AgentResponse 컴포넌트 직접 확인
- [^10]: [[conversational-ui-patterns|AI 에이전트 대화형 UI 패턴 종합 분석]] — Claude chunk-based rendering, Dual-Pane 아키텍처

### External
- [^1]: [OpenAI Community: Streaming Markdown](https://community.openai.com/t/streaming-markdown-or-other-formatted-text/510268) — ChatGPT의 react-markdown + progressive parsing 접근
- [^2]: [GitHub: remarkjs/react-markdown](https://github.com/remarkjs/react-markdown) — react-markdown 공식 레포지토리, components prop API
- [^3]: [CopilotKit: Markdown Rendering](https://docs.copilotkit.ai/custom-look-and-feel/markdown-rendering) — 슬롯 기반 마크다운 커스터마이징 아키텍처
- [^4]: [Vercel: Introducing Streamdown](https://vercel.com/changelog/introducing-streamdown) (2025) — react-markdown 드롭인 대체, 스트리밍 최적화
- [^5]: [GitHub: vercel/streamdown](https://github.com/vercel/streamdown) — Streamdown 소스 코드, React.lazy() 지연 로딩, 미완성 마크다운 복구
- [^6]: [Shiki: A Beautiful Yet Powerful Syntax Highlighter](https://shiki.style/) — VS Code TextMate 문법 기반, WASM 아키텍처
- [^7]: [prompt-kit: Markdown](https://www.prompt-kit.com/docs/markdown) — AI 채팅용 마크다운 컴포넌트 키트, Shiki 통합 패턴
- [^9]: [Mermaid.js Guide 2026](https://www.w3resource.com/javascript/mermaid-js-guide-to-create-diagrams-as-code.php) — Mermaid.js 최신 가이드, 다이어그램 유형별 구문
- [^11]: [Cursor IDE Architecture](https://blog.sshh.io/p/how-cursor-ai-ide-works) — Shiki/Monaco 기반 코드 스트리밍 + diff 뷰
- [^12]: [Google Research: Generative UI](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/) — Gemini Dynamic View 아키텍처
- [^13]: [Perplexity AI](https://www.perplexity.ai/) — Perplexity의 마크다운 + 인용 렌더링 패턴
- [^14]: [LibreChat: Syntax Highlighting](https://www.librechat.ai/docs/documentation/syntax_highlighting) — highlight.js → Shiki 전환, Mermaid 플러그인 지원

---

*Last synthesized: 2026-02-24 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
