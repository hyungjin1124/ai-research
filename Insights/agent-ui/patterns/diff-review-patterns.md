---
type: insight-synthesis
topic_id: diff-review-patterns
topic_name: "Diff 리뷰 및 수정 제안 UI"
category: agent-ui
document_level: specific
parent_broad:
  - hitl-approval-patterns
  - artifacts-canvas-patterns
catalog_components:
  - inline_edit
tags:
  - insight
  - agent-ui
  - pattern
  - diff
  - review
  - editing
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

# Diff 리뷰 및 수정 제안 UI

## TL;DR

- Claude Artifacts의 Highlight-to-Edit는 inpainting 패턴으로 선택 영역만 수정하고 context 유지 [^1]
- ChatGPT Canvas는 direct manipulation으로 user가 즉시 편집 가능, AI assist는 optional [^2]
- Cursor의 per-hunk diff view는 accept/reject granularity로 fine-grained control 제공 [^3]
- Vercel v0는 prompt-only refinement로 구현 complexity 최소화 (vs visual editor) [^4]
- GitHub Copilot Workspace는 file-by-file diff editor로 incremental refinement 지원 [^5]
- KonaI-Agent는 Claude Artifacts (Highlight-to-Edit) 패턴이 모드 중간 complexity, 최대 impact인 선택

## Overview

Diff 리뷰 및 수정 제안 UI는 Agent가 생성한 artifact (코드, 마크다운, 설정)와 user가 원하는 형태 사이의 gap을 interactive하게 좁히는 메커니즘이다. 패턴의 스펙트럼은:
- **Low Complexity**: Prompt-only (v0 초기 버전) → ask & iterate
- **Medium Complexity**: Highlight-to-Edit (Claude Artifacts) → 선택지에만 집중
- **High Complexity**: Direct Manipulation (Canvas) → full editor control
- **Fine-Grained**: Per-Hunk Diff (Cursor) → 변경사항 선택적 수용

PPT artifact의 맥락에서 "생성된 outline → 사용자가 특정 섹션만 수정 제안" 흐름은 Highlight-to-Edit 패턴과 완벽하게 align.

## 경쟁사 구현 분석

| Product | 패턴 | 수정 메커니즘 | 컨텍스트 유지 | 적합한 시점 |
|---------|------|-------------|----------|-----------|
| Claude Artifacts | Highlight-to-Edit | 선택 영역만 AI rewrite | 우수 (inpainting) | 부분 수정 |
| ChatGPT Canvas | Direct Manipulation | User types directly, AI co-edits | 우수 (shared editor) | Full artifact control |
| Cursor | Per-Hunk Diff | Accept/reject per change block | 중간 (diff view context만) | Code diff review |
| Vercel v0 | Prompt-Only Refinement | "Change X to Y" natural language | 낮음 (full regenerate) | High-level iterations |
| GitHub Copilot Workspace | File-by-File Diff Editor | Editable diff with inline edits | 중간 (file scope) | Multi-file coordination |

### Claude Artifacts: Highlight-to-Edit Inpainting [^1]

Workflow:
1. User 보기: artifact content in read-only panel
2. Selection: 마우스로 텍스트/코드 블록 선택 (highlight)
3. Edit Instruction: "이 부분을 X로 바꿔" 입력 (short form)
4. AI Response: 선택 영역만 rewrite, 나머지는 context에서 infer & preserve
5. Update: artifact panel에 선택 영역만 replace

**왜 이 방식인가**: 선택 영역을 제한하면 AI의 rewrite scope가 명확해지고, context preservation이 자동으로 된다. User가 "전체를 다시 쓰지 말고 이 부분만" 신호를 주는 것이 natural한 interaction.

참고: [Claude Artifacts get a big update — highlight and edit code with text](https://www.tomsguide.com/ai/claude-artifacts-get-a-big-update-now-you-can-highlight-and-edit-code-with-text), [Claude.AI's quiet revolution in artifact editing](https://hyperdev.matsuoka.com/p/claudeais-quiet-revolution-in-artifact)

### ChatGPT Canvas: Direct Manipulation [^2]

Canvas panel이 editable textarea/code editor로 제공:
- User: 직접 타이핑 & 수정 (traditional editing)
- AI: "이 부분이 이상해 보이는데" highlight & suggestion 제시 (optional)
- Update: 실시간 preview (React component면 live re-render)

**왜 이 방식인가**: User가 "생성된 artifact는 참고만, 난 내가 원하는 대로 직접 만들거야" 마인드셋일 때 best.

참고: [How to Use ChatGPT Canvas](https://ai-basics.com/how-to-use-chatgpt-canvas/), [ChatGPT Canvas Review 2025](https://skywork.ai/blog/chatgpt-canvas-review-2025-features-coding-pros-cons/)

### Cursor: Per-Hunk Diff View [^3]

Workflow:
1. Cursor generates code changes, presents as diff view
2. Visual: green (+) and red (-) lines, traditional diff format
3. Interaction: Checkbox per hunk (related changes grouped)
4. User: selective accept/reject, Apply button
5. Result: accepted hunks only applied to file

**왜 이 방식인가**: Code generation은 종종 "좋은 부분 + 엉뚱한 부분 혼재." Per-hunk selection으로 "이 hunk는 좋지만 저 hunk는 버려" 선택 가능.

참고: [Cursor Tab Completion vs GitHub Copilot](https://apidog.com/blog/cursor-tab/)

### Vercel v0: Prompt-Only Refinement [^4]

Workflow:
1. v0 generates initial UI component
2. User: "change the button color to blue" (natural language)
3. v0: Full regeneration based on prompt + previous version context
4. Version History: 클릭으로 이전 버전 복원
5. Design Mode (v0.app): Click element → adjust properties directly

**왜 이 방식인가**: UI 생성은 종종 "완벽한 첫 버전"이 어려움. Prompt-only는 user가 코드를 이해할 필요가 없고, natural language로 iteration.

참고: [How to prompt v0 - Vercel](https://vercel.com/blog/how-to-prompt-v0), [v0.dev -> v0.app migration](https://vercel.com/blog/v0-app)

### GitHub Copilot Workspace: File-by-File Diff Editor [^5]

Workflow:
1. Copilot generates multi-file changes, presents Diff View per file
2. Each file diff is itself editable (no separate "accept/reject modal")
3. User: directly edit the diff lines (green/red), add/remove lines as needed
4. All Files View: see which files are affected
5. Create PR: with user's final edits

**왜 이 방식인가**: Multi-file change는 "cross-file consistency 유지" 중요. Copilot Workspace는 모든 file diff를 editable로 놔둬서, user가 한 파일 edit하면 AI가 다른 파일의 dependent change를 coordinate.

참고: [GitHub Copilot Workspace: A Comprehensive Guide](https://createaiagent.net/tools/github-copilot-workspace/)

## 패턴 분류 및 트레이드오프

### 패턴 분류

1. **Highlight-to-Edit (Inpainting)**
   - 선택 영역 + instruction → AI inpaint & preserve context
   - 적합: 부분 수정, context preservation critical

2. **Direct Manipulation (Canvas Editor)**
   - Full artifact를 editable field로 제공
   - 적합: user가 "직접 제어" 원할 때

3. **Per-Hunk Diff View (Selective Accept)**
   - Diff 렌더링, hunk별 checkbox → selective apply
   - 적합: code generation with multiple independent changes

4. **Prompt-Only Refinement (Regenerate)**
   - Natural language prompt → full artifact regenerate
   - 적합: user가 code-unfamiliar, high-level intent만 명시

5. **File-by-File Diff Editor (Editable Diffs)**
   - Multi-file diff, each file individually editable
   - 적합: multi-file coordination with interdependencies

### Trade-off Summary

| Dimension | Highlight | Direct | Per-Hunk | Prompt-Only | File-by-File |
|-----------|-----------|--------|----------|------------|--------------|
| Complexity (impl) | 낮음 | 높음 (editor) | 중간 | 낮음 | 높음 |
| Context Preservation | 우수 | 우수 | 중간 | 낮음 | 중간 |
| User Control Granularity | 중간 (영역) | 높음 (문자) | 중간 (hunk) | 낮음 (intent) | 높음 (file) |
| Token Efficiency | 우수 (partial) | 중간 | 좋음 (partial) | 낮음 (full regen) | 낮음 |
| Code Understanding Required | 낮음 | 높음 | 중간 | 낮음 | 높음 |
| Mobile-Friendly | 좋음 | 어려움 | 어려움 | 좋음 | 어려움 |

## KonaI-Agent 적용 전략

### 권장 설계: Highlight-to-Edit (Claude Artifacts 패턴)

**Phase 1: Artifact Highlight Detection**

Artifact panel에서 text selection 감지:
- onMouseUp handler로 selection change 감지
- Selection range 추출 (start/end offset)
- Selection이 3 characters 이상일 때만 action bar 표시

**Phase 2: Edit Instruction Input**

UI Layout:
- Selection highlight 표시
- Action bar: "이 부분을 수정하시겠어요?" input box
- Button: Send (Ctrl+Enter 지원)
- Cancel: Esc key

**Phase 3: Inpainting + Update**

Flow:
1. AI receives: {selectedText, instruction, fullArtifactContext}
2. AI generates: new version of selected text (only)
3. UI: show diff inline (old → new highlight)
4. User: accept/reject inline diff
5. Artifact update: replace selected region, preserve rest

## Acceptance Criteria

### Functional Criteria

1. **Selection Detection**
   - Artifact panel에서 text selection 감지
   - Selection이 3 characters 이상일 때만 action bar 표시
   - Selection range 추출 (start/end offset)

2. **Edit Instruction UI**
   - Selection 주변에 action bar
   - Text input for instruction
   - Send button (Ctrl+Enter 지원)
   - Cancel button (Esc key)

3. **Inpainting Call**
   - API call: {selectedText, fullArtifact, instruction} → Claude
   - System prompt: "Preserve artifact context, only modify selected region"
   - Response parsing: 수정된 text extract

4. **Inline Diff Preview**
   - Old text: strikethrough + gray color
   - New text: green background, bold
   - Accept/Reject buttons

5. **Artifact Update**
   - Accept: artifact state 업데이트, selection clear
   - Reject: original 유지, action bar close
   - Undo (Ctrl+Z): 이전 artifact 상태 복원

## Key Considerations

1. **Over-Selection Prevention**: User가 실수로 전체 artifact 선택 후 "이거 전체 다시 쓰기"는 방지해야 함. Highlight-to-Edit는 "부분 수정"인데, 전체는 "Regenerate" 버튼으로 별도 제공.

2. **Instruction Clarity**: 좋은 instruction examples를 제시해야 함. Edit action bar에 examples as suggestions.

3. **Multi-Selection (non-contiguous)**: 초기는 contiguous selection만 지원.

4. **Artifact Type Flexibility**: PPT outline은 markdown-like text인데, JSON/code도 edit 하려면 syntax highlighting 필요 (future phase).

5. **Error Handling**: Approve handler에서 예외 발생 시, 실패 상태를 사용자에게 즉시 feedback.

## Recent Updates

| 날짜 | 변경사항 | 영향 범위 |
|------|---------|---------|
| 2026-02-15 | Claude Artifacts Highlight-to-Edit inpainting 패턴 분석 | Phase 1-3 아키텍처 |
| 2026-02-15 | ChatGPT Canvas direct manipulation 검토 | MVP에서는 제외 (복잡도) |
| 2026-02-15 | Cursor per-hunk diff 검토 | Future phase (code diff) |

## References

### External

- [Claude Artifacts get a big update — highlight and edit code with text](https://www.tomsguide.com/ai/claude-artifacts-get-a-big-update-now-you-can-highlight-and-edit-code-with-text)
- [Claude.AI's quiet revolution in artifact editing](https://hyperdev.matsuoka.com/p/claudeais-quiet-revolution-in-artifact)
- [How to Use ChatGPT Canvas](https://ai-basics.com/how-to-use-chatgpt-canvas/)
- [ChatGPT Canvas Review 2025](https://skywork.ai/blog/chatgpt-canvas-review-2025-features-coding-pros-cons/)
- [Cursor Tab Completion vs GitHub Copilot](https://apidog.com/blog/cursor-tab/)
- [GitHub Copilot Workspace: A Comprehensive Guide](https://createaiagent.net/tools/github-copilot-workspace/)
- [How to prompt v0 - Vercel](https://vercel.com/blog/how-to-prompt-v0)
- [v0.dev -> v0.app migration](https://vercel.com/blog/v0-app)

[^1]: Claude Artifacts의 inpainting은 선택 영역만 rewrite하고 context를 preserve하는 최적의 partial-edit 패턴.
[^2]: Canvas direct manipulation은 user autonomy가 최대지만 구현 복잡도도 높음.
[^3]: Cursor의 per-hunk acceptance는 code generation의 "섞인 quality"를 selective accept로 해결.
[^4]: Vercel v0는 prompt-only로 simplicity를 극대화, 대신 code understanding 요구하지 않음.
[^5]: GitHub Copilot Workspace는 multi-file diff를 모두 editable로 놔둬서, cross-file consistency maintain.
