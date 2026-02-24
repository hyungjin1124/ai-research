---
type: research-brief
topic_id: streaming-response-rendering
topic_name: 스트리밍 응답 렌더링 패턴
category: conversational-ui-patterns
document_level: intermediate
parent_broad:
  - conversational-ui-patterns
catalog_components:
  - streaming_typing
  - markdown_renderer
  - code_highlighting
tags:
  - streaming
  - real-time-rendering
  - markdown
  - progressive-enhancement
  - websocket
  - sse
status: active
confidence: high
last_updated: 2025-02-15
source_products:
  - ChatGPT
  - Claude
  - Google-Gemini
  - Vercel-v0
  - Cursor
auto_update: quarterly
relevant_roles:
  - frontend-engineer
  - ui-designer
  - ai-product-manager
---

# 스트리밍 응답 렌더링 패턴

## TL;DR

- **Token vs Chunk 스트리밍**: ChatGPT는 토큰 단위(빠른 응답감), Claude는 청크 기반(효율적 마크다운 처리)으로 구현. 각 접근의 선택은 네트워크 비용과 렌더링 복잡도의 트레이드오프[^1][^2]
- **Progressive Markdown**: 도착하는 토큰을 실시간으로 마크다운 파싱하고 렌더링. 불완전한 문법(`**bold` 미완성)은 일반 텍스트로 폴백[^1]
- **Extended Thinking UI**: Claude의 사고 과정(thinking blocks)을 collapsible 섹션으로 표시. 초기 숨김 상태, 사용자 확장 시 전체 추론 과정 공개[^2]
- **Dynamic View 생성**: Gemini는 스트림 중 HTML/CSS/JS 코드를 생성하고 즉시 미리보기 렌더링. 기존 텍스트/코드 스트리밍과 다른 아키텍처[^3]
- **중단 메커니즘**: 모든 제품이 스트리밍 중단 버튼 제공. 부분 응답을 그대로 유지하거나 마지막 완성된 블록까지만 표시[^4]

## Overview

스트리밍 응답 렌더링은 현대 AI 채팅 인터페이스의 핵심 UX 패턴이다. 사용자가 완전한 응답을 기다리지 않고 즉시 텍스트가 나타나는 경험을 제공함으로써 응답 지연감(latency perception)을 개선한다. 하지만 마크다운 구문의 실시간 파싱, 코드 블록 하이라이팅, auto-scroll 동작 등에서 구현 복잡도가 높아진다.

크게 세 가지 스트리밍 전략이 존재한다: (1) 토큰 단위 스트리밍 - 1-5개 문자 단위로 빠르게 업데이트하나 마크다운 렌더링이 어려움, (2) 청크 기반 스트리밍 - 문장/블록 단위로 업데이트하며 마크다운 파싱 정확도가 높음, (3) 생성 UI 스트리밍 - 코드 생성 중 DOM 업데이트 수행.

KonaI-Agent는 현재 setTimeout 기반 시뮬레이션을 사용 중이므로, 진정한 스트리밍 구현 시 기술 선택이 필수다.

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 스트리밍 단위 | 마크다운 렌더링 | Extended Thinking | 중단 기능 | 코드 하이라이팅 | Auto-scroll |
|------|-----------|-------------|------------------|---------|-------------|-----------|
| ChatGPT | Token (1-4) | Progressive (on-stream) | 없음 | ✓ | ✓ (Prism) | Follow + pause |
| Claude | Chunk (문장) | Deferred (block-end) | ✓ Collapsible | ✓ | ✓ (custom) | Smart scroll |
| Gemini | Dynamic (HTML/CSS/JS) | N/A (UI 생성) | 없음 | ✓ | Native (browser) | Viewport |
| Cursor | Token (실시간) | Deferred (완성 후) | 없음 | ✓ | ✓ (Shiki) | Follow + diff |
| v0 | RSC Frame (React) | N/A (JSX 컴포넌트) | 없음 | ✓ | ✓ (native) | Live preview |

### 경쟁사별 상세 분석

#### ChatGPT: Token-by-Token 마크다운 렌더링

**구현 방식**: 토큰을 거의 실시간으로(50-100ms 간격) 디스플레이에 추가. 마크다운 파싱을 "부분 완성 상태"로 수행: `**bold` 중간 상태는 임시로 일반 텍스트로 렌더링하고, 다음 토큰에서 `**` 닫기를 받으면 재해석. Cursor 애니메이션: 마지막 토큰 뒤에 `.after { content: '|'; animation: blink 1s; }` 스타일 적용. react-markdown 라이브러리로 마크다운을 JSX로 변환[^1]

**왜 이 방식인가**: 즉각적인 응답감(느슨한 마크다운 구조에 강함). 대화형 AI의 핵심 UX로 "지금 뭔가 일어나고 있다" 느낌 제공. 사용자가 스크롤하여 위쪽을 읽는 동안 하단에서 계속 쓰기 가능. 마크다운 파싱 에러 시 일반 텍스트로 graceful fallback.

**참고**: [Streaming Markdown 커뮤니티 논의](https://community.openai.com/t/streaming-markdown-or-other-formatted-text/510268) | [How to Format ChatGPT Output](https://alexminnaar.com/2025/04/07/how-to-format-chatgpt-api-output.html)

#### Claude: Chunk 기반 + Extended Thinking

**구현 방식**: 마크다운 블록(문단, 코드 블록, 리스트 등)을 "완성 단위"로 스트리밍. Extended Thinking: `<thinking>` 태그 블록을 초기에 collapsible 섹션으로 숨김. 사용자가 "Show thinking" 클릭 시 펼침. Thinking 블록의 내용도 스트림되므로, 펼친 후 점진적으로 텍스트 추가. 중단(Stop) 시: thinking 블록은 그대로 유지, 본문 응답은 부분 표시[^2]

**왜 이 방식인가**: 마크다운 정확성이 중요한 기술 문맥(코드, 수식, 테이블)에서 불완전한 마크다운 표시 방지. Thinking 블록 숨김으로 사용자가 최종 답변에 먼저 집중하고, 호기심 있을 때만 추론 과정 확인. 네트워크 패킷 감소로 토큰 단위보다 대역폭 효율적. 투명성과 사용자 제어의 균형 달성.

**참고**: [Claude Extended Thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) | [AWS Bedrock Extended Thinking](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html)

#### Google Gemini: Dynamic View 생성 UI

**구현 방식**: 기존 마크다운/텍스트 스트리밍이 아닌 완전히 다른 패러다임. AI가 프롬프트에 따라 HTML, CSS, JavaScript를 생성하고, 생성되는 즉시 브라우저에서 렌더링. 예시: "일정표 만들기" → 생성되는 달력 UI를 실시간으로 렌더링. 코드 생성 후 이미지 생성, 검색, 외부 API 호출 등을 통해 UI에 데이터 주입[^3]

**왜 이 방식인가**: 텍스트 기반 답변이 아닌 "상호작용형 도구" 제공. 사용자가 UI를 조작하면 즉시 업데이트(일반 채팅보다 빠른 피드백 루프). 마크다운마다 버리고 새로운 코드 생성으로 매번 UI 업데이트 가능.

**참고**: [Gemini Dynamic View 가이드](https://support.google.com/gemini/answer/16741341) | [Google Research: Generative UI](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)

#### Cursor: 코드 스트리밍 + Diff 뷰

**구현 방식**: 코드를 토큰 단위로 스트림하되, 특수 마크업(예: `@@` 라인 표기)으로 변경 영역 표시. Diff 뷰에서 삭제되는 라인은 빨강, 추가되는 라인은 초록으로 실시간 하이라이팅. Shiki 또는 Prism으로 언어별 구문 강조. Apply 버튼으로 사용자가 명시적으로 승인 후 파일에 적용[^4]

**왜 이 방식인가**: 코드 에디터 문맥에서 "변경사항 미리보기"가 매우 중요. Apply 버튼으로 실수 방지(원치 않는 코드 자동 삽입 차단). 기존 코드와의 diff 구조를 명확히 함으로써 신뢰도 증가.

**참고**: [Cursor IDE 아키텍처](https://blog.sshh.io/p/how-cursor-ai-ide-works) | [Cursor 2025 가이드](https://skywork.ai/blog/vibecoding/cursor-2-0-ultimate-guide-2025-ai-code-editing/)

#### Vercel v0: React Server Component 스트리밍

**구현 방식**: 사용자 프롬프트에서 AI가 React/Tailwind/shadcn 컴포넌트 코드 생성 후 RSC 프레임워크로 즉시 브라우저 렌더링. streamUI 함수로 스트림 중인 컴포넌트를 리얼타임으로 업데이트. 완성된 코드와 live preview가 병렬 표시[^5]

**왜 이 방식인가**: "생성 즉시 확인" 패러다임으로 반복 개선 가능. 마크다운 이해 불필요하며 코드 자체가 UI. 프로토타이핑 속도 극대화.

**참고**: [Vercel AI SDK RSC Streaming](https://ai-sdk.dev/docs/ai-sdk-rsc/streaming-react-components) | [AI SDK 3.0 Generative UI](https://vercel.com/blog/ai-sdk-3-0-with-generative-ui-support)

## 패턴 분류 및 트레이드오프

### 패턴 A: Token-by-Token Progressive Markdown

**대표 제품**: ChatGPT

**장점**:
- 가장 빠른 시각적 피드백(즉각성)
- 사용자가 읽는 동안 계속 쓸 수 있음(scrolling 독립성)
- 마크다운 에러에 강함(partial fallback)
- 구현 상대적으로 간단(token append)

**단점**:
- 마크다운 정확성 낮음(incomplete 상태에서 렌더링)
- 시각적 떨림 가능(리렌더링 많음)
- 테이블, 복잡한 리스트 등 고급 마크다운에서 깨질 수 있음
- 네트워크 오버헤드 높음(패킷 수 증가)

**적합한 상황**: 일반 대화형 채팅(기술 문서 아님) | 빠른 응답감이 중요한 경우 | 사용자가 부분 응답이라도 먼저 보고 싶을 때

### 패턴 B: Chunk-based + Deferred Markdown

**대표 제품**: Claude

**장점**:
- 마크다운 완전성 보장(완성된 블록만 렌더링)
- 기술 문서, 코드, 수식 정확도 높음
- Extended Thinking으로 투명성 제공
- 네트워크 효율적

**단점**:
- 응답감 다소 떨어질 수 있음(블록 단위 지연)
- 사용자 scrolling 동안 새 블록 추가 시 시각 깜빡임
- 초기 구현 복잡(블록 경계 판별)

**적합한 상황**: 기술 문서, 코드 생성 중심 | 마크다운 정확성이 중요할 때 | 사용자가 "완성된 정보"를 신뢰하기를 원할 때

### 패턴 C: Dynamic View (Generative UI)

**대표 제품**: Gemini 3 Dynamic View

**장점**:
- 텍스트 이상의 상호작용형 UI 제공
- 단순 답변보다 훨씬 매력적
- 사용자가 UI 조작 → 즉시 업데이트

**단점**:
- 구현 매우 복잡(코드 생성 + 샌드박스 실행)
- 보안 이슈(임의 HTML/JS 실행)
- 모든 프롬프트에 적합하지 않음
- 오버헤드 높음(코드 생성만 해도 네트워크 대기)

**적합한 상황**: "도구 생성" 프롬프트(계산기, 스케줄러 등) | 데이터 시각화 필요한 경우 | 프리미엄 사용자 경험 제공 시

### 패턴 D: Code Streaming with Diff Preview

**대표 제품**: Cursor

**장점**:
- 코드 에디터 문맥에 최적화
- Diff 뷰로 변경사항 명확
- Apply 버튼으로 실수 방지

**단점**:
- 코드 생성 전용(일반 텍스트 부족)
- 에디터 통합 필수
- 대규모 파일 diff 시 성능 저하

**적합한 상황**: AI 코드 에디터(IDE) | 파일 직접 수정이 목표일 때 | 사용자가 변경사항을 검토하고 명시적 승인하기를 원할 때

### 트레이드오프 요약 테이블

| 기준 | Token-by-Token | Chunk-based | Dynamic View | Code Diff |
|------|------|------|------|------|
| 응답감(Latency Perception) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 마크다운 정확성 | ⭐⭐ | ⭐⭐⭐⭐⭐ | N/A | ⭐⭐⭐⭐⭐ |
| 구현 복잡도 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 네트워크 효율성 | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 사용자 신뢰도 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 확장성(여러 콘텐츠 타입) | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | ⭐⭐ |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 자산 | 위치 | 현황 | 재사용 가능성 |
|------|------|------|------------|
| Auto-resize Textarea | ChatInterface.tsx | 구현됨 | 100% |
| Context Chips | ChatInterface.tsx | 구현됨 | 100% |
| Chat Bubbles | ChatHistoryView.tsx | 구현됨 | 80% |
| setTimeout Simulation | simulatedResponses | 구현됨 | 30% |
| CSS Animation | Tailwind + custom | 기본 설정 | 90% |
| Brand Color (#FF3C42) | 전체 | 적용됨 | 100% |
| 마크다운 렌더러 | 없음 | 미구현 | 0% |
| 구문 강조 | 없음 | 미구현 | 0% |

### 권장 접근

**선택안: Chunk-based Progressive Markdown (Streaming Lite)**

현재 시뮬레이션 구조를 점진적으로 진정한 스트리밍으로 전환하되, ChatGPT의 토큰 단위와 Claude의 청크 기반의 중간 지점을 제안.

**초기 단계(v1 - Demo/MVP)**: setTimeout 시뮬레이션 유지하되, 마크다운 렌더링 추가. react-markdown + remark-gfm으로 마크다운 파싱. Prism.js 또는 Shiki로 코드 블록 구문 강조. cursor animation 추가. 비용: 낮음, 시뮬레이션이므로 백엔드 변경 불필요.

**중기 단계(v2 - Real Streaming)**: 실제 SSE 또는 WebSocket 구현. 청크 단위 스트리밍(문장/블록 경계). 중단 버튼 구현(AbortController). Auto-scroll 스마트 동작.

**장기 단계(v3 - Extended Thinking)**: Extended Thinking 지원(collapsible 섹션). 부분 응답 상태에서도 사용자가 "중간 결과 사용 가능" 인터페이스.

### 이 접근을 권장하는 이유

1. **점진적 구현 가능**: 현재 setTimeout 인프라를 버리지 않고 UI 레이어부터 시작하여, 나중에 통신 레이어만 교체
2. **마크다운 정확성**: Chunk 기반이므로 불완전한 마크다운 표시 안 함. 기술 문서(코드 포함)에 강함
3. **KonaI-Agent의 3-panel 레이아웃 활용**: 우측 패널에서 코드 블록을 별도 렌더링 가능
4. **네트워크 효율**: 토큰 단위보다 청크 단위가 대역폭 절약
5. **사용자 신뢰**: Chunk 단위 완성으로 "완성된 정보"만 표시
6. **Extended Thinking 준비**: v1부터 thinking 블록을 collapsible로 설계하면, v3에서 Claude 통합 용이

### Acceptance Criteria

- [ ] 마크다운 렌더링: react-markdown + remark-gfm 도입. 모든 GFM 구문 정상 렌더링
- [ ] 구문 강조: Prism.js 또는 Shiki로 코드 블록 언어별 색상. 최소 10개 언어 지원
- [ ] Cursor Animation: 응답 스트리밍 중 마지막 글자 뒤에 animated 커서 표시
- [ ] 중단 버튼: 스트리밍 중 "Stop generating" 버튼. 클릭 시 즉시 현재 상태 유지
- [ ] Auto-scroll: 스트리밍 중 자동 스크롤. 사용자 스크롤 시 중지 후 재개
- [ ] 코드 블록 특별 처리: Copy 버튼, "Open in right panel" 버튼 추가
- [ ] 부분 응답 체크: 스트리밍 중단 후에도 부분 응답이 올바른 마크다운으로 렌더링
- [ ] SSE 마이그레이션 경로: ChatInterface에서 마크다운 렌더링이 스트림 출처에 무관하게 동작

## Key Considerations

### 마크다운 보안
- 사용자 입력 마크다운을 그대로 렌더링하지 말 것. react-markdown은 기본적으로 HTML sanitize하나, `sanitize` 옵션 명시적 설정 권장(XSS 방지)
- AI 응답 마크다운은 신뢰할 수 있으므로, 사용자 입력 전용 별도 sanitizer 적용

### 네트워크 청크 크기
- Token 단위: 50-100ms 간격, 1-5 토큰(빠르지만 패킷 오버헤드)
- Chunk 단위: 200-500ms 간격, 문장/블록 경계(권장)
- 설정: 백엔드에서 `max_chunk_size` 파라미터로 조절 가능

### 코드 블록 고유 요구사항
- Language detection: Prism/Shiki는 자동 감지 지원하나, 명시적 지정이 정확함
- Line numbers: 장문 코드에서 유용하나 UI 스페이스 고려
- Copy to clipboard: 필수 기능
- "Apply" vs "Open in right panel": 3-panel 레이아웃이므로 후자 권장

### 성능 최적화
- 대규모 응답(10KB 이상)에서 마크다운 파싱 지연 가능. React.memo + useMemo 사용하여 재렌더링 최소화
- 코드 블록 구문 강조: Shiki가 정확하나 Prism이 더 가벼움. 초기에는 Prism 추천

### 모바일 고려사항
- Cursor animation은 성능 이슈 가능. 모바일에서는 discreet 점 표시로 대체 검토
- Auto-scroll이 모바일 touch gesture와 conflict할 수 있으므로 테스트 필수

## Recent Updates

| 날짜 | 변경사항 |
|------|---------|
| 2025-02-15 | 초안 작성. ChatGPT/Claude/Gemini/Cursor/v0 비교 분석 |

## References

[^1]: [Streaming Markdown - OpenAI Community](https://community.openai.com/t/streaming-markdown-or-other-formatted-text/510268)
[^2]: [Claude Extended Thinking Documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
[^3]: [Google Research: Generative UI](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
[^4]: [Cursor IDE Architecture](https://blog.sshh.io/p/how-cursor-ai-ide-works)
[^5]: [Vercel AI SDK 3.0: Streaming React Components](https://ai-sdk.dev/docs/ai-sdk-rsc/streaming-react-components)
