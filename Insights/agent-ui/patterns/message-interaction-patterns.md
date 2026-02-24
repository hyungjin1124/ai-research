---
type: research-brief
topic_id: message-interaction-patterns
topic_name: 메시지 인터랙션 패턴
category: conversational-ui-patterns
document_level: intermediate
parent_broad:
  - conversational-ui-patterns
catalog_components:
  - message_actions
  - message_edit_regenerate
  - code_block_actions
  - inline_citations
tags:
  - message-interaction
  - hover-actions
  - code-blocks
  - citations
  - conversation-branching
status: active
confidence: high
last_updated: 2025-02-15
source_products:
  - ChatGPT
  - Claude
  - Google-Gemini
  - Cursor
  - Perplexity
auto_update: quarterly
relevant_roles:
  - frontend-engineer
  - ux-designer
  - ai-product-manager
---

# 메시지 인터랙션 패턴

## TL;DR

- **Hover Actions vs Always-visible**: ChatGPT는 hover 시 Copy/Regenerate/Like/Share 버튼 표시(공간 절약), Claude는 최소한의 버튼 상시 표시(빠른 접근)[^1][^2]
- **메시지 편집 + 분기(Branching)**: ChatGPT는 사용자 메시지 재편집 → 새로운 응답 생성으로 conversation 분기(< 1/3 > 네비게이션). Claude는 "retry" 패턴으로 마지막 응답만 재생성[^1][^2]
- **코드 블록 특별 처리**: Copy 버튼은 기본, Claude의 "Open in Artifact" vs Cursor의 "Apply"가 핵심 차이. KonaI-Agent의 3-panel은 "Open in right panel" 패턴 최적화[^1][^2][^3]
- **Inline Citations**: Perplexity는 [1][2][3] 형태의 inline 번호 링크로 출처 표시. 클릭 시 출처 카드 확장[^5]
- **언어 감지 + 라인 번호**: 모든 제품이 코드 블록 언어 자동 감지. 라인 번호 표시는 optional하나 긴 코드(10+ 라인)에서 유용[^3][^4]

## Overview

메시지 인터랙션 패턴은 사용자가 AI 응답과 상호작용하는 방식을 정의한다. 단순히 읽기만 하는 것이 아니라, 응답을 수정하거나 재생성하거나, 코드를 복사/적용하거나, 출처를 확인하는 등의 작업을 포함한다. 특히 코드 생성, 장문 문서 작성, 리서치(출처 중요) 시나리오에서는 이러한 인터랙션이 필수적이다.

크게 네 가지 인터랙션 카테고리가 존재한다:
1. **메시지 레벨 액션**: Copy, Regenerate, Feedback(Like/Dislike), Share
2. **메시지 편집 및 분기**: 자신의 메시지 재편집 → 새 응답 분기
3. **코드 블록 액션**: Copy, Apply/Open in Artifact, Language detection, Line numbers
4. **출처 추적**: Inline citations [1][2], Source cards, Verification links

KonaI-Agent는 현재 기본 Chat 버블만 표시하므로, 호버 액션과 코드 블록 기능 추가가 우선순위.

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | Hover Actions | Always-visible | Edit Conversation | Regenerate | Copy Code | Apply/Artifact | Inline Citations | Language Detection | Line Numbers |
|------|--------|--------|---------|-----------|-----------|-------------|----------|----------|----------|
| ChatGPT | ✓ | ✗ | ✓ (분기) | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| Claude | ✗ | ✓ (최소) | ✗ | ✓ (Retry) | ✓ | ✓ (Artifact) | ✗ | ✓ | ✓ |
| Gemini | ✓ | 부분 | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| Cursor | ✗ | ✓ (Apply) | N/A | N/A | ✓ | ✓ (Apply) | ✗ | ✓ | ✓ |
| Perplexity | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ |

### 경쟁사별 상세 분석

#### ChatGPT: Hover 기반 + Conversation Branching

**구현 방식**:
- Hover 시 메시지 우측 하단에 아이콘 버튼 표시:
  - Copy (📋 아이콘): 응답 전체를 클립보드에 복사. 클릭 후 아이콘이 체크마크로 변경되어 복사 완료 확인[^1]
  - Regenerate (🔄 아이콘): 마지막 AI 응답 재생성. 동일한 프롬프트에 새로운 응답 생성
  - Feedback (👍👎 아이콘): Thumbs up/down으로 응답 품질 피드백. OpenAI 학습에 사용
  - Share (📤 아이콘): 대화 공유 링크 생성. 코드: `https://chat.openai.com/share/[id]`
- 메시지 편집 분기: 사용자가 자신의 메시지(이전 프롬프트)를 클릭하여 재편집 → 새로운 응답 생성. 기존 분기는 유지되고, 새 분기 시작(< 1/3 > 네비게이션)[^1]
- 코드 블록 내 Copy: 각 코드 블록 우측 상단에 별도의 Copy 버튼 (아이콘만)
- Language tag: 각 코드 블록 상단에 언어명 표시(예: "python", "javascript")

**왜 이 방식인가**:
- Hover 액션으로 기본 메시지 UI는 깔끔(공간 절약)
- 분기 네비게이션으로 사용자가 여러 응답 경로 비교 가능(< 1/3 > 형태)
- 피드백 시스템으로 지속적 모델 학습
- Share 기능으로 대화 공유 가능(협업, 버그 리포트)

**참고**: [ChatGPT Message Actions Guide](https://zapier.com/blog/how-to-use-chatgpt/) | [Export ChatGPT Conversations](https://edrawmind.wondershare.com/ai-features/export-chatgpt-conversation.html)

#### Claude: Minimal Always-visible + Artifact Pattern

**구현 방식**:
- Always-visible 버튼(호버 불필요): Copy, Retry 버튼이 메시지 우측에 항상 표시[^2]
- Retry (🔄 버튼): 마지막 응답만 재생성. 분기 네비게이션 없음
- Copy: 전체 응답 또는 선택 텍스트만 복사
- Feedback: 메시지 하단에 "Was this helpful?" 버튼 (별도 패널)
- Code Block Actions: "Open in Artifact" 버튼으로 코드를 우측 패널(Artifact)에서 렌더링[^2]
  - Artifact는 콘텐츠 미리보기 영역으로, 코드가 실행 가능한 형태(HTML/React/SVG)로 표시됨
  - 사용자는 Artifact에서 인터랙션 가능(예: 생성된 React 컴포넌트와 상호작용)
  - Copy/Export 버튼으로 코드 별도 저장 가능
- Language detection + Line numbers: 코드 블록에 언어명과 라인 번호 표시[^2]

**왜 이 방식인가**:
- Always-visible 버튼으로 기능 발견성(Discoverability) 높음
- Artifact 시스템으로 코드가 단순 텍스트가 아닌 "실행 가능한 결과"로 표현
- 분기 없이 "Retry"만 제공으로 UI 단순성
- 코드 + 미리보기 분리로 개발자 워크플로우 최적화

**참고**: [Claude Documentation](https://platform.claude.com/docs/en/build-with-claude/artifacts) | [Inside Claude Desktop](https://skywork.ai/blog/ai-agent/claude-desktop-ultimate-guide-architecture-workflow/)

#### Google Gemini: Hybrid Hover + Quick Actions

**구현 방식**:
- Hover 시 메시지 우측에 점 메뉴(⋮) 표시
- 메뉴 클릭 시 Copy, Share, "Modify response", "Google it" 옵션 제시[^3]
- "Modify response": 응답 내용을 직접 편집 또는 "Generate new response" 선택
- "Google it": 응답 내용을 웹 검색하여 추가 검증 정보 표시
- 코드 블록: Copy, "Run in Colab"(Python의 경우) 버튼 포함
- Language detection + 실행 가능 코드는 "Run" 버튼 제공

**왜 이 방식인가**:
- 점 메뉴로 추가 옵션 숨김(기본 UI 깔끔)
- "Modify response"는 사용자가 응답을 수정 후 재생성(편집 경험 개선)
- "Google it"로 실시간 웹 검색과 통합(사실 검증)
- Colab 통합으로 Python 코드 즉시 실행 가능

**참고**: [Gemini AI Features](https://blog.google/products/gemini/gemini-3-examples-demos/)

#### Cursor: Code-first Apply Pattern

**구현 방식**:
- 코드 블록 우측에 "Apply" 버튼(가장 눈에 띄는 위치)[^3]
- Apply 클릭 → 코드가 현재 에디터에 즉시 적용
- Diff preview: Apply 전에 "다음과 같이 변경됩니다" 시각화
- Copy: 별도의 Copy 버튼(Apply 옆)
- Language detection + Line numbers + Syntax highlighting: 기본[^3]
- Inline diff: 변경된 라인은 초록(추가), 빨강(삭제)으로 강조
- 메시지 편집: Cursor 메시지 UI에서 프롬프트 재편집 후 새로운 응답 생성(채팅 분기 없음)

**왜 이 방식인가**:
- "Apply"는 개발자의 주요 목적(코드 직접 적용)을 가장 명확하게 반영
- Diff preview로 실수 방지(자동 적용 아님)
- 에디터 통합이 깊으므로, 코드 블록 UI가 최소화 가능

**참고**: [Cursor IDE Features](https://skywork.ai/blog/vibecoding/cursor-2-0-ultimate-guide-2025-ai-code-editing/) | [How Cursor Works](https://blog.sshh.io/p/how-cursor-ai-ide-works)

#### Perplexity: Inline Citations + Source Cards

**구현 방식**:
- 응답 텍스트 내 [1], [2], [3] 등의 번호 링크 삽입[^5]
- 각 번호는 응답 하단의 Source 섹션에 있는 원본 URL과 연결
- 번호 클릭 → 해당 출처 카드 확장(제목, 요약, 링크, favicon 포함)
- 메시지 Copy 시 [1][2] 번호도 함께 복사됨
- Share: 대화 공유 시 모든 출처 정보 포함
- Feedback: Like/Dislike 버튼(호버 또는 항상 표시)
- 추가 출처 탐색: "Sources" 섹션 클릭 → 전체 Source 패널 확장

**왜 이 방식인가**:
- Inline citations로 "어느 부분이 어디서 나온 정보인가" 즉시 추적[^5]
- Source cards로 출처 신뢰도 시각화(특히 favicon으로 사이트 인식)
- 리서치 목적(논문, 기사 작성)에서 "출처 확인"이 매우 중요
- 분기 없이 Share 시 모든 정보(응답 + 출처) 보존

**참고**: [Perplexity Citation System Guide](https://www.unusual.ai/blog/perplexity-platform-guide-design-for-citation-forward-answers) | [How AI Engines Cite Sources](https://medium.com/@shuimuzhisou/how-ai-engines-cite-sources-patterns-across-chatgpt-claude-perplexity-and-sge-8c317777c71d)

## 패턴 분류 및 트레이드오프

### 패턴 A: Hover Actions (ChatGPT)

**대표 제품**: ChatGPT

**장점**:
- 기본 UI 깔끔(공간 효율)
- 기능이 많아도 숨겨져 있음
- 마우스 호버 시 발견 가능

**단점**:
- 터치/모바일에서 호버 불가
- 버튼 위치가 동적(메시지마다 다름)
- 초기 사용자는 액션 존재를 모를 수 있음

**적합한 상황**:
- 데스크톱 중심 사용
- 액션이 많은 경우(5개 이상)
- 기본 UI를 최대한 간단하게 원할 때

### 패턴 B: Always-visible Minimal (Claude)

**대표 제품**: Claude

**장점**:
- 기능 발견성 높음(항상 보임)
- 터치 기기에서도 쉽게 접근
- 일관된 버튼 위치

**단점**:
- UI가 상대적으로 복잡해 보임
- 많은 액션이 있으면 메시지 영역 축소
- 버튼이 필요 없는 상황에도 항상 표시

**적합한 상황**:
- 모바일 사용자 많음
- 3-5개의 핵심 액션만 필요
- 발견성이 중요할 때

### 패턴 C: Branching Conversation (ChatGPT)

**대표 제품**: ChatGPT

**장점**:
- 여러 응답 경로 비교 가능(< 1/3 > 네비게이션)
- 분기마다 독립적인 대화 유지
- A/B 테스트 같은 비교 워크플로우 가능

**단점**:
- UI 복잡도 높음(분기 관리)
- 히스토리 길어지면 전체 구조 파악 어려움
- 모바일에서 분기 네비게이션 어려움

**적합한 상황**:
- 탐색적 작업(여러 방향 시도)
- 창의적 작업(여러 버전 비교)
- 고급 사용자 대상

### 패턴 D: Artifact Pattern (Claude)

**대표 제품**: Claude

**장점**:
- 코드와 미리보기 분리(2-panel 패턴)
- 실행 가능한 코드(React, HTML, SVG)
- 사용자가 Artifact와 상호작용 가능

**단점**:
- 모든 코드 생성에 Artifact 적합하지 않음(shell script, 라이브러리 코드 등)
- 초기 구현 복잡(코드 감지, 미리보기 렌더링)
- 화면 공간 더 필요(2-panel)

**적합한 상황**:
- 시각적 결과가 필요한 코드(UI, 그래프)
- 사용자가 결과와 상호작용하길 원할 때
- 3-panel 이상의 레이아웃 가능할 때

### 패턴 E: Apply Button (Cursor)

**대표 제품**: Cursor

**장점**:
- 목표가 명확(코드 적용)
- Diff로 변경사항 미리 검토
- 에디터 통합 깊음

**단점**:
- 코드 아닌 콘텐츠는 처리 불가
- IDE 환경에서만 의미 있음
- 일반 대화 UI와 분리 필요

**적합한 상황**:
- 코드 에디터 통합 도구
- 파일 직접 수정이 목표
- 개발자 전용 도구

### 패턴 F: Inline Citations (Perplexity)

**대표 제품**: Perplexity

**장점**:
- 출처 추적이 명확
- 각 문장의 근거 확인 가능
- 신뢰도 높음(특히 리서치)

**단점**:
- 응답이 번호로 어수선해 보일 수 있음
- 모든 콘텐츠가 웹 기반 출처 필요
- 번호 관리 복잡(변경 시 재정렬)

**적합한 상황**:
- 리서치, 사실 검증 목적
- 웹 검색 기반 답변
- 학술, 저널리즘 분야

### 트레이드오프 요약 테이블

| 기준 | Hover | Always-visible | Branching | Artifact | Apply | Citations |
|------|--------|--------|---------|-----------|-------------|----------|
| UI 공간 효율 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 발견성(Discoverability) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 모바일 친화성 | ⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 고급 기능성 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 신뢰도(출처) | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 구현 복잡도 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 자산 | 위치 | 현황 | 재사용 가능성 |
|------|------|------|------------|
| Chat Bubbles | ChatHistoryView.tsx | 기본 렌더링 | 80% |
| Hover 이벤트 | 일부 | 부분 구현 | 50% |
| Copy to Clipboard | 없음 | 미구현 | 0% |
| 코드 블록 UI | 없음 | 미구현 | 0% |
| Language Detection | 없음 | 미구현 | 0% |
| 3-panel Layout | GeneralChatView | 구현됨 | 100% |
| Brand Color (#FF3C42) | 전체 | 적용됨 | 100% |

### 권장 접근

**선택안: Always-visible Minimal + Right Panel Pattern (Claude + 3-panel hybrid)**

Claude의 "최소한의 Always-visible 버튼"을 기본으로, 코드 블록은 KonaI-Agent의 3-panel 레이아웃을 활용하여 "Open in right panel" 패턴 구현. 세 단계 구현으로 진행.

**초기 단계(v1 - 기본 액션)**:
- 메시지 우측에 Copy 버튼(항상 표시)
- Hover 시 Regenerate 버튼 추가
- Copy 클릭 시 전체 응답을 클립보드에 복사
- 피드백 버튼(👍👎)은 메시지 하단에 표시(나중에 analytics 수집)
- 비용: 낮음, 기존 ChatHistoryView.tsx 수정만 필요

**중기 단계(v2 - 코드 블록 + Right Panel)**:
- 각 코드 블록에 Copy 버튼 추가(항상 표시)
- 코드 언어 자동 감지 + 블록 상단에 표시
- 라인 번호 표시(선택적, 10+ 라인부터)
- "Open in right panel" 버튼으로 코드를 우측 패널에 렌더링
  - 우측 패널에서 코드 실행 가능(Python, SQL, JavaScript 등에 따라)
  - 실행 결과(그래프, 테이블, 콘솔 출력) 우측 패널에 표시
- 언어별 구문 강조(Prism.js 또는 Shiki)

**장기 단계(v3 - Retry + 출처 통합)**:
- Retry 버튼(마지막 응답 재생성)
- Inline citations 지원(나중에 필요할 경우)
- Share 기능(대화 공유 링크)

### 이 접근을 권장하는 이유

1. **KonaI-Agent의 3-panel 활용**: 우측 패널이 이미 있으므로, 코드 블록을 "Open in right panel"로 렌더링하는 것이 자연스러움(Claude의 Artifact와 유사하나 3-panel 특화)
2. **Always-visible으로 발견성 높음**: 호버 불필요, 모바일에서도 접근 가능
3. **점진적 복잡도 증가**: v1은 Copy/Regenerate만, v2에서 코드 블록 특화, v3에서 고급 기능
4. **코드 실행 가능**: 우측 패널에서 Python/SQL/JavaScript 코드 직접 실행(데이터 분석 AI 용도에 최적)
5. **신뢰도 관리**: 향후 출처 추적 추가 시, 현재 구조에서 쉽게 확장 가능
6. **모바일 친화**: Always-visible 버튼은 터치 기기에 최적

### Acceptance Criteria

- [ ] Copy 버튼: 메시지 우측에 항상 표시. 클릭 시 전체 응답을 클립보드 복사. 복사 완료 후 아이콘 변경(체크마크) 또는 토스트 알림 표시
- [ ] Regenerate 버튼: Hover 시 메시지 우측에 표시. 클릭 시 마지막 AI 응답 재생성(동일한 프롬프트)
- [ ] 피드백 버튼: 메시지 하단에 👍👎 버튼 표시. 클릭 시 피드백 기록(analytics)
- [ ] 코드 블록 Copy: 각 코드 블록 우측 상단에 Copy 버튼 추가
- [ ] 언어 감지: 각 코드 블록 상단에 언어명 표시(예: "python", "sql", "javascript")
- [ ] 라인 번호: 코드 블록이 10 라인 이상이면 라인 번호 표시(설정 가능)
- [ ] 구문 강조: Prism.js 또는 Shiki로 코드 블록 언어별 색상 강조
- [ ] Open in Right Panel: 코드 블록에 "Open in right panel" 버튼 추가. 클릭 시 우측 패널에 코드 렌더링
- [ ] 우측 패널 렌더링: 우측 패널에서 코드 블록을 더 크게 표시. 복사, 실행(Python/SQL/JavaScript), 다운로드 버튼 제공
- [ ] 실행 결과 표시: 코드 실행 결과(그래프, 테이블, 콘솔 출력)를 우측 패널 하단에 표시
- [ ] 사용자 메시지 편집: 사용자 메시지를 클릭하여 편집 → 새로운 AI 응답 생성(분기 없이 기존 응답 대체)
- [ ] Conversation 상태 관리: 메시지 추가/삭제/편집 시 conversation tree 정확하게 유지

## Key Considerations

### 코드 실행 보안
- 사용자가 제출한 코드를 무작정 실행하지 않기 (XSS, RCE 위험)
- Python/SQL은 샌드박스 환경에서 실행 필수(예: RestrictedPython, SQL 쿼리 검증)
- JavaScript는 iframe 또는 Web Worker 내에서만 실행
- 사용자가 "Run" 클릭 시 명시적 확인 화면 표시

### 클립보드 복사 UX
- 복사 완료 후 "Copied!" 토스트 알림 표시(1-2초)
- 또는 Copy 버튼 아이콘을 체크마크로 변경했다가 복사 아이콘으로 복구
- 실패 시 명확한 에러 메시지(예: "Clipboard access denied")

### 모바일에서의 호버 대체
- 터치 기기에서는 hover 불가능
- Regenerate 같은 호버 액션은 항상 표시하거나, 메시지 길게 누르면 팝업 메뉴 표시

### 코드 블록 특수성
- 마크다운 코드 블록 vs 인라인 코드 구분(인라인은 Copy만)
- 매우 긴 코드(1000+ 라인)는 접기/펼치기 기능 제공
- JSON, YAML, CSV 같은 데이터 포맷은 표 형식으로 미리보기 가능

### 메시지 편집 워크플로우
- 사용자 메시지 클릭 → 편집 모드 전환(입력 필드처럼 변함)
- 편집 후 "Update" 또는 Enter 누르면 AI가 새로운 응답 생성
- 기존 응답은 "Regenerating..." 상태로 변경 후 새 응답으로 대체

### Regenerate 제약사항
- 마지막 AI 메시지만 Regenerate 가능(중간 메시지는 불가)
- 스트리밍 중에는 Regenerate 버튼 비활성화
- Regenerate 중복 클릭 방지 (한 번 시작되면 완료까지 기다려야 함)

### Feedback 데이터 수집
- 👍: 응답이 도움이 됨
- 👎: 응답이 도움이 안 됨 (선택 시 "이유가 뭐였나요?" 추가 물음)
- 수집된 데이터는 "향후 개선"을 위해 저장(사용자에게 명시)

## Recent Updates

| 날짜 | 변경사항 |
|------|---------|
| 2025-02-15 | 초안 작성. ChatGPT/Claude/Gemini/Cursor/Perplexity 비교 분석 |

## References

[^1]: [ChatGPT How to Use Guide](https://zapier.com/blog/how-to-use-chatgpt/)
[^2]: [Claude Documentation & Artifacts](https://platform.claude.com/docs/en/build-with-claude/artifacts)
[^3]: [Cursor IDE Features & Code Actions](https://skywork.ai/blog/vibecoding/cursor-2-0-ultimate-guide-2025-ai-code-editing/)
[^4]: [Google Gemini Features & Interactions](https://blog.google/products/gemini/gemini-3-examples-demos/)
[^5]: [Perplexity Citation System & Sources](https://www.unusual.ai/blog/perplexity-platform-guide-design-for-citation-forward-answers)
