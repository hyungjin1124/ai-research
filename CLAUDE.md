# KonaI-Agent — Project Guide for Claude Code

## Project Overview

KonaI-Agent는 AI 에이전트 기반 엔터프라이즈 대시보드 애플리케이션이다.
채팅 인터페이스, 에이전트 시나리오 오케스트레이션, 라이브보드 대시보드,
관리자 패널 등 다양한 뷰를 포함한다.

## Tech Stack

- **Framework**: Next.js 15 (App Router)
- **UI**: React 18, Tailwind CSS, Radix UI
- **Visualization**: Recharts, react-grid-layout, ReactFlow
- **State**: React Context (전역 상태), 컴포넌트 로컬 state
- **Language**: TypeScript (strict mode)

## Directory Structure

```
src/
├── app/                          # Next.js App Router 페이지
│   ├── page.tsx                  # 메인 페이지
│   ├── chat/                     # 채팅 뷰
│   ├── admin/                    # 관리자 뷰
│   ├── data/                     # 데이터 파이프라인
│   └── agent/                    # 에이전트 시나리오 (ppt, analysis)
│
├── components/
│   ├── ui/                       # Base UI 컴포넌트 (Radix UI 래핑)
│   │   ├── button.tsx
│   │   ├── dialog.tsx
│   │   ├── table.tsx
│   │   └── ...
│   │
│   ├── features/                 # Feature 단위 컴포넌트 그룹
│   │   ├── general-chat/         # 채팅 기능
│   │   │   ├── GeneralChatView.tsx
│   │   │   └── components/
│   │   │       ├── ChatPanel/
│   │   │       └── LeftSidebar/
│   │   ├── liveboard/            # 대시보드
│   │   │   ├── LiveboardView.tsx
│   │   │   └── components/widgets/
│   │   ├── dashboard/            # 대시보드 하위 기능
│   │   │   ├── components/
│   │   │   └── data/
│   │   ├── ppt/                  # PPT 생성 시나리오
│   │   └── data/                 # 데이터 관리
│   │
│   ├── ChatInterface.tsx         # 공통 채팅 인터페이스
│   ├── ChatHistoryView.tsx       # 채팅 이력 뷰
│   ├── AdminView.tsx             # 관리자 뷰
│   ├── Sidebar.tsx               # 글로벌 네비게이션
│   └── ...
│
├── hooks/                        # Custom React Hooks
│   ├── useScenarioOrchestration.ts
│   ├── usePPTScenario.ts
│   └── useSlideOutlineHITL.ts
│
├── context/                      # React Context Providers
│   └── NotificationContext.tsx
│
├── constants/                    # 상수 정의
│   ├── navigation.ts
│   └── widgets.ts
│
├── types/                        # TypeScript 타입 정의
│
└── lib/                          # 유틸리티, API 클라이언트
```

## Naming Conventions

- **컴포넌트 파일**: PascalCase (`ChatPanel.tsx`, `DrillDownContextMenu.tsx`)
- **Hook 파일**: camelCase, `use` prefix (`useScenarioOrchestration.ts`)
- **상수 파일**: camelCase (`navigation.ts`, `widgets.ts`)
- **타입 파일**: camelCase 또는 PascalCase (프로젝트 기존 패턴 따름)
- **디렉토리**: kebab-case (`general-chat/`, `left-sidebar/`)

## Component Conventions

### 새 컴포넌트 작성 시 규칙

1. **Feature 컴포넌트**는 `src/components/features/{feature-name}/` 아래에 배치
2. **공유 UI 프리미티브**는 `src/components/ui/` 아래에 배치
3. 컴포넌트 Props는 같은 파일 또는 `src/types/`에 인터페이스로 정의
4. Radix UI를 기본 프리미티브로 사용 — 가능하면 Radix 컴포넌트를 래핑
5. 스타일링은 Tailwind CSS utility classes 사용 (인라인 style 지양)
6. 복잡한 상태 로직은 커스텀 Hook으로 분리 (`src/hooks/`)

### 컴포넌트 파일 구조 (권장)

```tsx
// 1. Imports
import { useState, useCallback } from 'react';
import { SomeRadixComponent } from '@radix-ui/react-xxx';

// 2. Types
interface ComponentNameProps {
  // ...
}

// 3. Component
export function ComponentName({ prop1, prop2 }: ComponentNameProps) {
  // hooks
  // handlers
  // render
  return (
    <div className="...">
      {/* JSX */}
    </div>
  );
}
```

## Key References

### Component Catalog
- **위치**: `specs/component-catalog.yaml`
- **역할**: 58개 컴포넌트의 상태 추적 (status, priority, source_files)
- **obsidian_sources**: 리서치 문서 경로 (상세 분석, acceptance criteria 포함)

### Obsidian Vault (리서치 문서)

리서치 문서는 별도 Obsidian Vault에 관리된다. Catalog의 `obsidian_sources` 필드가
vault 내 상대 경로를 가리킨다.

- **Vault 경로**: `$OBSIDIAN_VAULT_PATH` (프로젝트 외부, 환경에 따라 다름)
- **패턴 문서**: `Insights/agent-ui/patterns/{topic-slug}.md`
- **문서 구조**: 경쟁사 분석 → 패턴 트레이드오프 → KonaI-Agent 적용 전략 → Acceptance Criteria

Claude Code가 obsidian_sources를 참조할 때는 다음 경로에서 읽는다:
```
{OBSIDIAN_VAULT_PATH}/{obsidian_sources_value}
```

### Context 라우팅

| Context | Routes | 설명 |
|---------|--------|------|
| chat_view | `/`, `/chat` | 메인 대화 인터페이스 |
| artifact_panel | `/chat` | 에이전트 생성 결과물 패널 |
| liveboard | `/`, `/liveboard` | 위젯 기반 대시보드 |
| admin | `/admin`, `/settings` | 관리자 인터페이스 |
| monitoring | — | 모니터링 |
| data_pipeline | `/data` | 데이터 파이프라인 |
| agent_scenario | `/agent/ppt`, `/agent/analysis` | 멀티스텝 시나리오 |
| global | `*` | 공통 |

## Implementation Pipeline

컴포넌트 구현 자동화를 위한 `/implement` 커맨드가 `.claude/commands/implement.md`에
정의되어 있다. 다음과 같이 사용한다:

```
/implement {component_id}
```

자세한 파이프라인 단계는 해당 파일 참조.
