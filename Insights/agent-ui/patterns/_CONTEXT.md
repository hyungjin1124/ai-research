# Agent UI Patterns — Specific 문서 컨텍스트 가이드

> 이 파일은 `Insights/agent-ui/patterns/` 서브폴더의 구조와 규칙을 설명하는 메타 가이드입니다.
> 상위 broad 문서(`Insights/agent-ui/*.md`)의 교차 분석을 **컴포넌트 수준의 구현 가이드**로 세분화합니다.

---

## Broad 문서와의 관계

```
Insights/agent-ui/
├── hitl-approval-patterns.md          ← Broad: HITL 승인 패턴 교차 분석
├── conversational-ui-patterns.md      ← Broad: 대화형 UI 패턴 교차 분석
├── artifacts-canvas-patterns.md       ← Broad: Artifacts/Canvas 패턴 교차 분석
├── agent-reasoning-visualization.md   ← Broad: 추론 과정 시각화 교차 분석
├── dashboard-composition.md           ← Broad: 대시보드 구성 패턴 교차 분석
├── data-visualization-drilldown.md    ← Broad: 데이터 시각화/드릴다운 교차 분석
│
└── patterns/                          ← Specific: 컴포넌트별 구현 가이드
    ├── _CONTEXT.md                    ← 이 파일
    ├── _TEMPLATE_pattern.md           ← Specific 문서 생성 템플릿
    └── {topic-slug}.md                ← 개별 패턴 문서
```

### 역할 분담
| 계층 | 질문 유형 | 예시 |
|------|----------|------|
| **Broad** 문서 | "A2A 프로토콜과 MCP-UI 중 뭐가 좋아?" "HITL 패턴은 몇 가지야?" | 전략적 의사결정, 경쟁사 벤치마킹 |
| **Specific** 문서 | "Tool Call Display를 어떻게 구현해?" "Parallel Execution UI 레퍼런스는?" | 컴포넌트 설계, 구현 착수 시 참고 |

---

## Frontmatter 스키마 (specific 문서)

| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | `insight-synthesis` (Insights 공통) |
| `topic_id` | string | kebab-case slug (파일명과 동일) |
| `topic_name` | string | 사람용 표시 이름 |
| `category` | string | `agent-ui` |
| `document_level` | string | `specific` (broad와 구분) |
| `parent_broad` | list | 관련 broad 문서의 topic_id 목록 |
| `catalog_components` | list | **component-catalog.yaml**의 component id 목록 |
| `tags` | list | `[insight, agent-ui, pattern, ...]` |
| `status` | string | `draft` \| `current` \| `needs-update` |
| `confidence` | string | `high` \| `medium` \| `low` |
| `last_updated` | date | YYYY-MM-DD |
| `source_products` | list | 참조한 product_id 목록 |
| `source_files` | list | wikilink 경로 목록 |
| `auto_update` | object | 자동화 설정 (Insights/_CONTEXT.md 참조) |
| `relevant_roles` | list | `[frontend_agent, ...]` |

### catalog_components 필드

`catalog_components`는 이 specific 문서가 구현 가이드를 제공하는 **component-catalog.yaml의 component id** 목록입니다. 양방향 동기화의 핵심 연결고리입니다.

```yaml
# 예시
catalog_components:
  - tool_call_display
  - agent_thinking
  - multi_step_progress
```

→ component-catalog.yaml에서는 역방향으로 `obsidian_sources` 필드가 이 문서를 참조합니다.

---

## 토픽 레지스트리

### 카테고리 1: Conversational Primitives

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `streaming-response-rendering` | 스트리밍 응답 렌더링 패턴 | `streaming_typing`, `markdown_renderer` | `conversational-ui-patterns` | critical |
| `markdown-renderer` | 마크다운 렌더러 구현 전략 | `markdown_renderer`, `code_block`, `mermaid_diagram` | `conversational-ui-patterns` | critical |
| `multimodal-input-patterns` | 멀티모달 입력 UI 패턴 | `chat_input` | `conversational-ui-patterns` | high |
| `message-interaction-patterns` | 메시지 인터랙션 패턴 | `message_actions`, `message_edit_regenerate`, `code_block` | `conversational-ui-patterns` | high |
| `citation-source-display` | 인용 및 출처 표시 패턴 | `citation_source_link` | `conversational-ui-patterns`, `agent-reasoning-visualization` | medium |
| `suggested-prompts-design` | 추천 프롬프트/질문 설계 | `suggested_prompts` | `conversational-ui-patterns` | medium |

### 카테고리 2: Agent Action Patterns

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `tool-call-visualization` | 도구 호출 시각화 패턴 | `tool_call_display` | `agent-reasoning-visualization` | critical |
| `thinking-block-design` | 사고 과정 블록 설계 | `agent_thinking` | `agent-reasoning-visualization` | high |
| `multi-step-progress-patterns` | 멀티스텝 진행 표시 패턴 | `multi_step_progress` | `agent-reasoning-visualization` | high |
| `parallel-execution-ui` | 병렬 실행 UI 패턴 | `parallel_execution_view` | `agent-reasoning-visualization`, `dashboard-composition` | high |
| `error-recovery-patterns` | 에러 및 복구 UI 패턴 | `error_retry_ui` | `agent-reasoning-visualization` | high |
| `agent-status-indicators` | 에이전트 상태 인디케이터 | `agent_status_indicator` | `dashboard-composition` | medium |

### 카테고리 3: HITL Patterns

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `approval-gate-component` | 승인 게이트 컴포넌트 설계 | `approval_rejection` | `hitl-approval-patterns` | critical |
| `inline-selection-patterns` | 인라인 선택지 UI 패턴 | `inline_selection` | `hitl-approval-patterns` | high |
| `diff-review-patterns` | Diff 리뷰 및 수정 제안 UI | `inline_edit` | `hitl-approval-patterns`, `artifacts-canvas-patterns` | high |
| `feedback-collection-ui` | 피드백 수집 UI 패턴 | `feedback_collection` | `hitl-approval-patterns` | medium |
| `variable-autonomy-controls` | 자율성 수준 조절 컨트롤 | `variable_autonomy_control` | `hitl-approval-patterns` | medium |
| `risk-based-rendering` | 위험도 기반 동적 UI 렌더링 | `approval_rejection`, `confirmation_dialog` | `hitl-approval-patterns` | high |

### 카테고리 4: Artifact & Visualization

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `artifact-panel-layout` | 아티팩트 패널 레이아웃 설계 | `artifact_panel` | `artifacts-canvas-patterns`, `conversational-ui-patterns` | critical |
| `document-viewer-patterns` | 문서 뷰어 (docx/pdf/pptx) 패턴 | `document_viewer`, `ppt_slide_preview` | `artifacts-canvas-patterns` | high |
| `interactive-table-design` | 인터랙티브 데이터 테이블 설계 | `interactive_table` | `data-visualization-drilldown` | high |
| `nl-to-chart-pipeline` | 자연어→차트 변환 파이프라인 | `nl_to_chart` | `data-visualization-drilldown` | high |
| `dashboard-builder-patterns` | 대시보드 빌더/커스터마이저 패턴 | `dashboard_builder` | `dashboard-composition`, `data-visualization-drilldown` | medium |
| `widget-grid-interaction` | 위젯 그리드 인터랙션 패턴 | `dashboard_widget_grid`, `kpi_card`, `chart_widget` | `dashboard-composition`, `data-visualization-drilldown` | medium |
| `mermaid-diagram-rendering` | 다이어그램 렌더링 패턴 | `mermaid_diagram` | `artifacts-canvas-patterns` | low |
| `artifact-content-types` | 아티팩트 콘텐츠 유형별 렌더러 | `artifact_panel`, `document_viewer` | `artifacts-canvas-patterns` | medium |
| `drilldown-interaction-design` | 드릴다운 인터랙션 상세 설계 | `drill_down` | `data-visualization-drilldown` | high |

### 카테고리 5: Navigation & Session

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `conversation-history-patterns` | 대화 이력 탐색 패턴 | `conversation_sidebar`, `chat_history_view` | `conversational-ui-patterns` | medium |
| `session-branching-ui` | 세션 분기/포크 UI 패턴 | `session_branching` | `conversational-ui-patterns` | medium |
| `context-management-ui` | 컨텍스트 윈도우 관리 UI | `context_window_indicator` | `conversational-ui-patterns` | low |
| `model-agent-switcher` | 모델/에이전트 전환 UI | `model_agent_switcher` | `conversational-ui-patterns` | medium |
| `notification-system-design` | 알림 시스템 설계 패턴 | `notification_center` | `dashboard-composition` | medium |

### 카테고리 6: Admin & Operations

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `audit-log-design` | 감사 로그 UI 설계 | `audit_log` | `dashboard-composition`, `hitl-approval-patterns` | medium |
| `usage-monitoring-dashboard` | 사용량 모니터링 대시보드 | `usage_monitoring` | `dashboard-composition` | medium |
| `agent-configuration-ui` | 에이전트 설정 관리 UI | `agent_config` | `dashboard-composition` | medium |
| `prompt-management-ui` | 프롬프트 관리 및 버전 관리 UI | `prompt_management` | `dashboard-composition` | low |

### 카테고리 7: Generative & Emerging

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `generative-ui-implementation` | Generative UI 구현 전략 | `generative_ui` | `conversational-ui-patterns`, `artifacts-canvas-patterns` | high |
| `ambient-agent-patterns` | Ambient Agent UI 패턴 | `ambient_agent` | `conversational-ui-patterns`, `dashboard-composition` | medium |
| `workflow-builder-patterns` | 비주얼 워크플로우 빌더 | `workflow_builder` | `dashboard-composition` | medium |
| `agent-memory-ui` | 에이전트 메모리 관리 UI | `memory_management` | `conversational-ui-patterns` | low |
| `realtime-collaboration-patterns` | 실시간 협업 패턴 | `realtime_collaboration` | `artifacts-canvas-patterns` | low |
| `sandbox-preview-patterns` | 샌드박스/프리뷰 모드 패턴 | `sandbox_mode` | `artifacts-canvas-patterns`, `hitl-approval-patterns` | medium |
| `voice-interface-patterns` | 음성 입출력 인터페이스 | `voice_io` | `conversational-ui-patterns` | low |
| `onboarding-wizard-patterns` | 온보딩/튜토리얼 위저드 | `onboarding_wizard` | `conversational-ui-patterns` | low |

### 카테고리 8: Cross-Cutting (횡단 관심사)

| topic_id | 표시명 | catalog_components | parent_broad | 우선순위 |
|----------|--------|-------------------|--------------|---------|
| `dark-mode-theming` | 다크모드 및 테마 시스템 설계 | `dark_mode` | — | low |
| `responsive-layout-patterns` | 반응형 레이아웃 패턴 | — (전체 해당) | `conversational-ui-patterns`, `dashboard-composition` | medium |
| `animation-microinteraction` | 애니메이션 및 마이크로인터랙션 | — (전체 해당) | — | low |
| `keyboard-accessibility` | 키보드 단축키 및 접근성 패턴 | — (전체 해당) | — | medium |
| `morning-briefing-patterns` | 모닝 브리핑 / 프로액티브 피드 | — (신규 추가 후보) | `dashboard-composition`, `data-visualization-drilldown` | high |

---

## 문서 작성 규칙

### Broad 문서와의 차이점

| 항목 | Broad 문서 | Specific 문서 |
|------|-----------|--------------|
| 범위 | 주제 전체 교차 분석 | 특정 컴포넌트/패턴 구현 가이드 |
| 비교 매트릭스 | 10+ 제품 전체 비교 | 해당 패턴 구현 제품 3~5개 집중 비교 |
| Key Findings | 전략적 인사이트 | 구현 시 고려사항, 기술 선택 가이드 |
| 추가 섹션 | — | **Implementation Guide** (기술 스택 권장, 컴포넌트 구조, acceptance criteria) |
| catalog 연결 | 없음 | `catalog_components` 필드로 양방향 매핑 |

### 필수 섹션 (specific 문서)

1. **TL;DR** — 3~5개 핵심 bullet (인라인 출처 필수)
2. **Overview** — 이 컴포넌트/패턴의 산업 배경 (1~2문단)
3. **Cross-Product Comparison** — 해당 패턴을 구현한 3~5개 제품 비교 (매트릭스 + 스크린샷 참조)
4. **Implementation Patterns** — 2~4개 구현 접근 방식 비교 (장단점, 적용 조건)
5. **Implementation Guide** — 기술 스택 권장, 컴포넌트 구조, acceptance criteria (catalog 참조)
6. **Key Considerations** — 구현 시 고려사항, 엣지 케이스, 성능
7. **Recent Updates** — 자동화 append 영역
8. **References** — 각주 상세 출처

### 인용 규칙

Insights/_CONTEXT.md의 인용 규칙을 동일하게 따릅니다.

### 자동화 규칙

- `auto_update.enabled: true` 기본
- `auto_update.keywords`에 해당 컴포넌트 관련 키워드 설정
- Daily News 라우팅: `topic_tag: agent-ui` + `keywords` 매칭으로 자동 수신
- `review_trigger.threshold: 3` 기본 (specific 문서는 더 자주 업데이트될 수 있음)

---

## 양방향 동기화 규칙

### Obsidian → Catalog (새 리서치 → 카탈로그 업데이트)

1. 새 specific 문서 생성 시 `catalog_components`에 관련 component id 기록
2. 문서 내용이 새로운 컴포넌트를 발견하면:
   - component-catalog.yaml에 `status: research_needed`로 추가
   - 해당 specific 문서의 `catalog_components`에 새 id 추가
3. Recent Updates에 새 데이터 축적 → 본문 반영 시 catalog의 `references` 및 `acceptance_criteria` 보강

### Catalog → Obsidian (개발 진행 → 리서치 보강 필요)

1. catalog에서 `status: not_implemented` + `priority: critical/high`인 컴포넌트 중 specific 문서가 없는 항목 식별
2. 해당 컴포넌트에 대한 specific 문서 생성을 "리서치 필요" 태스크로 플래깅
3. 개발 중 발견된 구현 이슈를 specific 문서의 Key Considerations에 피드백

---

## 신규 Specific 토픽 추가 시

1. 이 파일의 **토픽 레지스트리** 해당 카테고리 테이블에 행 추가
2. `_TEMPLATE_pattern.md`를 복사하여 `patterns/{new-slug}.md` 생성
3. `catalog_components` 필드에 관련 component id 매핑
4. component-catalog.yaml의 해당 component에 `obsidian_sources` 추가
5. `_INDEX.md`의 Dataview는 category + document_level 필드 기반이므로 자동 반영

---

*이 파일 최종 수정: 2026-02-24*
