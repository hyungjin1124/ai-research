---
type: insight-synthesis
topic_id: inline-selection-patterns
topic_name: "인라인 선택지 UI 패턴"
category: agent-ui
document_level: specific
parent_broad:
  - hitl-approval-patterns
catalog_components:
  - inline_selection
tags:
  - insight
  - agent-ui
  - pattern
  - selection
  - choice
  - inline
status: draft
confidence: high
last_updated: "2026-02-15"
source_products: []
source_files: []
auto_update:
  enabled: true
  keywords: []
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 인라인 선택지 UI 패턴

## TL;DR

- Claude의 AskUserQuestion tool은 multi-choice cards + descriptions 구조로 명확한 선택 context 제공 [^1]
- ChatGPT의 suggested replies는 single-line chip 버튼으로 micro-interaction 최소화 [^2]
- SAP Joule의 guided prompts + carousel은 role-based structured options으로 discovery 향상 [^3]
- ServiceNow의 Genius Result Cards는 action buttons + expandable content로 inline editing 통합 [^4]
- KonaI-Agent PPT scenario 선택지는 Channel/Style/Structure 중 다중선택 가능한 choice cards 패턴이 최적

## Overview

인라인 선택지 UI 패턴은 Agent가 사용자에게 제한된 옵션 집합을 제시하여 의사결정을 촉진하는 메커니즘이다. 이는 open-ended 텍스트 입력의 ambiguity를 줄이면서도 사용자의 선택권을 보장한다. 패턴의 선택은 선택지 개수(2-5 vs 5+), 선택 모드(단일 vs 다중), 시각 richness(텍스트만 vs 이미지+설명), 모바일 지원도를 기준으로 결정된다.

PPT scenario context에서 "Channel(스타일) 선택" → "Content Structure 선택" → "Detail Level 조정" 단계의 선택지들은 conversation flow를 유지하면서 granular하게 설정 가능해야 한다.

## 경쟁사 구현 분석

| Product | 선택지 표현 | 구조 | 주요 특징 | 왜 이 방식인가? |
|---------|-----------|------|---------|---------------|
| Claude Code | Multiple-Choice Cards | Title + Description per option | 60초 timeout, 자동 recommended mark, "Other" custom input | Ambiguous 상황에서 AI의 권장을 trust anchor로 제공 |
| Claude Cowork | AskUserQuestion Cards | Emoji icon + title + optional explanation | Keyboard nav, multi-select support | 시각적 affordance로 빠른 recognition |
| ChatGPT | Suggested Replies | Single-line chips below message | Responsive, mobile-optimized | Low cognitive load, 1-2 tap으로 진행 |
| Salesforce | Topic-Based Action Cards | Icon + title + description + CTA button | Carousel swipeable, role-filtered | Discovery-driven, 사용자가 모르던 action도 노출 |
| SAP Joule | Guided Prompts Carousel | Structured options in carousel format | Filterable by role/area, Prompt Library | Role-aware filtering로 noise 제거 |
| ServiceNow | Genius Result Cards | Tagline + title (2 lines) + answer + action buttons | Show more button, sources button, thumbs up feedback | Expandable design으로 initial glance 간단, 심화 가능 |

### Claude Code: AskUserQuestion Tool [^1]

Claude Code의 AskUserQuestion은 3-option modal structure:
- Title: "어떤 방식으로 진행할까요?"
- Options: Array of {value, label, description, recommended?}
- Type: single | multiple
- Timeout: 60초 후 recommended option auto-select

**왜 이 방식인가**: Description field로 각 선택의 trade-off를 명시. "Recommended" mark는 trustworthiness signal로, 사용자가 "Claude's suggestion"을 빠르게 evaluate할 anchor point가 된다.

참고: [What is Claude Code's AskUserQuestion tool?](https://www.atcyrus.com/stories/claude-code-ask-user-question-tool-guide), [Handle approvals and user input - Claude API Docs](https://platform.claude.com/docs/en/agent-sdk/user-input)

### ChatGPT: Suggested Replies [^2]

Message 아래에 2-4개 chip buttons, single-line text, tap으로 즉시 선택.

**왜 이 방식인가**: Minimal friction. 사용자가 "다음 뭘 해야하지?" 하고 있을 때 suggested replies가 UX flow를 interrupt 없이 maintain.

참고: [Getting Suggested Replies with ChatGPT](https://learn.turn.io/l/en/article/o7umxxgojc-getting-suggested-replies-with-chat-gpt)

### SAP Joule: Guided Prompts + Carousel [^3]

- Prompt Guide: Quick-start tips per role
- Prompt Library: Filterable by role/area
- Carousel: Swipeable left/right for discovery

**왜 이 방식인가**: Role-based filtering은 information overload를 방지. Carousel은 "한 눈에 여러 option 훑기" UX를 enable.

참고: [SAP Joule for Developers](https://www.sap.com/products/artificial-intelligence/joule-for-developers.html)

### ServiceNow: Genius Result Cards [^4]

Card Layout: Tagline + title (2 lines) + answer (6 lines max) + action buttons

**왜 이 방식인가**: "Expandable" design은 initial cognitive load를 줄이면서 power users에게 deep dive 경로를 제공.

참고: [Now Assist Q&A Genius Result](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/now-assist-qna-genius-results.html)

## 패턴 분류 및 트레이드오프

### 패턴 분류

1. **Choice Cards** (Claude Code 패턴)
   - Structure: Icon/emoji + Title + Description + Recommended badge
   - Selection: Single or multi-select
   - Capacity: 3-7 options optimal

2. **Chip Buttons** (ChatGPT 패턴)
   - Structure: Text only, minimal padding
   - Selection: Single-select, click-through
   - Capacity: 2-4 options

3. **Carousel Selection** (SAP Joule 패턴)
   - Structure: Horizontally scrollable cards
   - Selection: Single-select with swipe
   - Capacity: 5+ options

4. **Expandable Cards** (ServiceNow 패턴)
   - Structure: Minimal preview + "Show More" → full content
   - Selection: Implicit (action button click)
   - Capacity: 3+ cards in list

### Trade-off Summary

| Dimension | Choice Cards | Chips | Carousel | Expandable |
|-----------|-------------|-------|----------|-----------|
| Clarity (descriptions) | 높음 | 낮음 | 중간 | 중간 |
| Visual Richness | 중간 | 낮음 | 높음 | 중간 |
| Capacity (options) | 3-7 | 2-4 | 5+ | 3+ |
| Mobile-Friendly | 좋음 | 우수 | 우수 | 좋음 |
| Click count to select | 1 | 1 | 1-2 | 2+ |
| Implementation Cost | 중간 | 낮음 | 높음 | 중간 |

## KonaI-Agent 적용 전략

### 권장 설계: Choice Cards + Multi-Select 패턴

**Stage 1: Channel Selection (Multi-select)**

Component props:
- title: "PPT 스타일 선택"
- description: "여러 개 선택 가능, 혼합 스타일 생성"
- type: 'multiple'
- cards with icon, title, description, recommended mark
- timeout: 60000ms

**Stage 2: Content Structure Selection (Single-select for clarity)**

Similar structure but type: 'single', ensures one structure is chosen.

**Stage 3: Detail Level (Slider + Inline Chips)**

Chips: ['최소', '간결', '중간', '풍부', '상세'], recommended: 2

### 구현 Rationale

1. **Multi-select for Channel**: PPT 생성 시 "corporate + creative 혼합" 같은 nuanced choice를 enable.

2. **Recommended Mark**: AI가 user's context를 기반으로 recommend할 수 있고, 사용자는 이를 override 가능.

3. **Description Per Option**: 각 선택지의 consequence를 명시.

4. **60-Second Timeout**: Claude Code 패턴. 사용자가 decision paralysis에 빠지면 recommended selection으로 auto-proceed.

5. **Conversation History Integration**: 사용자의 선택이 message history에 표시되어야 함.

## Acceptance Criteria

### Functional Criteria

1. **SelectionCardGroup Component**
   - type: 'single' | 'multiple' 지원
   - 3-7개 card option 렌더링
   - Recommended option에 badge + visual accent (#FF3C42)
   - Keyboard nav: arrow keys, space/enter for toggle

2. **Multi-select State Management**
   - 선택 결과가 array로 return
   - onSelect callback이 선택된 모든 option의 ID/value 반환
   - 선택 해제 (toggle) 지원

3. **Recommended Mark + AI Context**
   - Context analyze하여 recommended option 결정
   - 60초 timeout 시 recommended option auto-select

4. **Conversation Flow**
   - 사용자 선택이 message history에 명시적으로 기록
   - Selection result artifact에 반영

5. **Mobile Responsiveness**
   - < 768px: cards stack vertically, full-width
   - Touch-friendly: checkbox/radio size >= 44px

## Key Considerations

1. **Choice Overload (Hick's Law)**: 7개 이상 option은 decision time이 exponentially 증가. Stage별로 selection을 나누어 cognitive load 분산.

2. **Recommended Signal Calibration**: "Recommended" mark를 너무 자주 사용하면 신뢰도 하락.

3. **Multi-select vs Single-select Clarity**: UI에서 "선택할 수 있다" 명시 (description에 "여러 개 선택 가능" 명시).

4. **Undo/Revert**: 한 번 선택한 후에 "다시 선택하기" 버튼을 제공할지 고려.

## Recent Updates

| 날짜 | 변경사항 | 영향 범위 |
|------|---------|---------|
| 2026-02-15 | Claude AskUserQuestion multi-choice cards 분석 | Stage-based selection 설계 |
| 2026-02-15 | ChatGPT suggested replies chip pattern 검토 | Mobile-friendly rendering |
| 2026-02-15 | SAP Joule carousel pattern 추가 | 5+ options 처리 방안 |

## References

### External

- [What is Claude Code's AskUserQuestion tool?](https://www.atcyrus.com/stories/claude-code-ask-user-question-tool-guide)
- [Handle approvals and user input - Claude API Docs](https://platform.claude.com/docs/en/agent-sdk/user-input)
- [Getting Suggested Replies with ChatGPT](https://learn.turn.io/l/en/article/o7umxxgojc-getting-suggested-replies-with-chat-gpt)
- [SAP Joule for Developers](https://www.sap.com/products/artificial-intelligence/joule-for-developers.html)
- [Now Assist Q&A Genius Result - ServiceNow Docs](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/now-assist-qna-genius-results.html)

[^1]: Claude Code의 AskUserQuestion은 description + recommended badge로 "왜 이 선택이 좋은가"를 context-aware하게 설명.
[^2]: ChatGPT의 chip pattern은 "다음 뭘 하지?" 고민 중인 사용자에게 UX interrupt 없이 flow를 유지.
[^3]: SAP Joule의 role-based carousel은 정보 과부하를 방지하면서도 discovery를 유도.
[^4]: ServiceNow의 expandable cards는 initial glance 간단성 + deep dive capability을 동시 제공.
