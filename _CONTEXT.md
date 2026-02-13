# AI Research — 루트 컨텍스트 가이드

> **이 파일은 이 리서치 볼트의 구조, 스키마, 자동화 규칙을 설명하는 메타 문서입니다.**
> 질문에 대한 답을 찾거나 역할별 문서 라우팅이 필요하면 `AGENTS.md`를 읽으세요.

---

## 볼트 개요

이 볼트는 **엔터프라이즈 ERP 기반 AI 에이전트 프로덕트 개발**을 위한 경쟁사 분석 및 시장 리서치 허브입니다.
19개 AI 에이전트 제품의 심층 프로필, 일일 뉴스 수집, 그리고 이들을 교차 분석한 인사이트 문서를 포함합니다.

### 3-Layer Knowledge System

```
┌──────────────────────────────────────────────────────────┐
│  Layer 3: Insights/ (합성 레이어)                          │
│  "주제를 관통하는 교차 분석 인사이트"                         │
│  → 에이전트·팀원이 빠르게 답을 얻는 곳                       │
├──────────────────────────────────────────────────────────┤
│  Layer 2: AI Agent Products/ (깊이 레이어)                 │
│  "특정 제품에 대한 모든 것"                                 │
│  → 개별 제품 deep-dive가 필요할 때                          │
├──────────────────────────────────────────────────────────┤
│  Layer 1: AI Daily News/ (시의성 레이어)                    │
│  "지금 무슨 일이 일어나고 있는가"                            │
│  → 매일 트렌드 파악, 뉴스 자동 수집                          │
└──────────────────────────────────────────────────────────┘
```

### 데이터 규모

| 영역 | 파일 수 | 갱신 주기 | 설명 |
|------|---------|----------|------|
| Insights | ~38 | `review_trigger` 기반 반자동 (Recent Updates 누적량) | 교차 분석 인사이트, 비교 매트릭스, 의사결정 가이드 |
| AI Agent Products | ~42 | 수시 (뉴스 연동 자동) | 19개 제품별 프로필 + 업데이트 로그 |
| AI Daily News | 증가중 | 매일 03:00 KST 자동 | 일일 22건 내외 다이제스트 |

---

## 디렉터리 구조

### Insights/ (교차 분석 인사이트 계층)
주제별로 여러 제품과 소스를 교차 분석한 합성 문서.

| 카테고리                   | 대상                 | 설명                                 |
| ---------------------- | ------------------ | ---------------------------------- |
| `agent-skills/`        | Agent Skill 개발     | Tool calling, MCP 서버 구현, skill 설계  |
| `agent-runtime/`       | Deep Agent 아키텍처    | 에이전트 루프, 병렬 처리, 파일시스템, 메모리         |
| `knowledge-data/`      | Knowledge Graph 세팅 | RAG, 시맨틱 레이어, 임베딩, KG 활용           |
| `agent-ui/`            | UI 개발              | 대화형 UI, HITL, 추론 시각화, Canvas       |
| `protocols/`           | 전체 (크로스커팅)         | MCP, A2A, A2UI 프로토콜 비교/도입          |
| `open-source/`         | 전체                 | OSS 모델, 프레임워크, 에이전트 도구             |
| `market/`              | 전체 (전략)            | 경쟁 동향, 가격 전략, 한국 ERP AI            |
| `strategy/`            | PM·팀장              | 경쟁 환경 요약, 로드맵 비교, Feature Gap, GTM |
| `security-evaluation/` | 전체 (품질)            | 가드레일, 권한 모델, 벤치마크                  |
| `maintenance/`         | 전체                 | 주간 트렌드 합성 + 월간 Health Check        |

- `_CONTEXT.md`: 인사이트 계층 전용 가이드 (카테고리 레지스트리, 토픽 분류)
- `_INDEX.md`: Dataview 기반 동적 인덱스 (카테고리별/최근 수정별)

### AI Agent Products/ (제품별 원본 데이터 계층)
19개 AI 에이전트 제품의 심층 프로필(3,000-6,000 words)과 업데이트 로그.
- `_CONTEXT.md`: 제품 레지스트리, 스키마, 자동화 규칙
- 각 제품: `{slug}/{slug}.md` (프로필) + `{slug}_updates.md` (뉴스 로그)

### AI Daily News/ (뉴스 수집 계층)
매일 자동 수집되는 AI 뉴스 다이제스트. RSS 20개 + 웹 검색.
- `_CONTEXT.md`: 수집 소스, 중요도 기준, 자동화 규칙
- `YYYY/MM/YYYY-MM-DD.md`: 일일 다이제스트

---

## Frontmatter 타입 레지스트리

| type 값 | 위치 | 설명 |
|---------|------|------|
| `product-profile` | AI Agent Products/{slug}/ | 제품 메인 프로필 |
| `product-updates` | AI Agent Products/{slug}/ | 제품 뉴스 업데이트 로그 |
| `daily-digest` | AI Daily News/YYYY/MM/ | 일일 뉴스 다이제스트 |
| `weekly-summary` | AI Daily News/YYYY/MM/ | 주간 뉴스 요약 |
| `insight-synthesis` | Insights/*/ | 주제별 교차 분석 인사이트 |

---

## 태그 체계

### 제품 분류 태그
`B2C`, `Enterprise`, `Analytics`, `Knowledge`, `AI-Agent`

### 기능 태그
`MCP-Support`, `A2A-Support`, `Agent-Builder`, `ERP-Integrated`, `LLM-Native`, `NL-to-SQL`, `Full-Stack-AI`, `Enterprise-Search`, `Agent-Marketplace`, `Korea-ERP`, `Manufacturing-ERP`

### 인사이트 태그
`insight`, `comparison`, `agent-skills`, `agent-runtime`, `knowledge-data`, `agent-ui`, `protocols`, `open-source`, `market`, `strategy`, `security-evaluation`, `maintenance`

---

## 자동화 연동 개요

| 파이프라인 | 트리거 | 산출물 |
|-----------|--------|--------|
| 일일 뉴스 수집 | macOS launchd 03:00 KST | AI Daily News/YYYY/MM/DD.md + 제품 _updates.md |
| Git Push → GitHub Actions | main push | Teams 알림 + Quartz 웹사이트 배포 |
| 주간 트렌드 합성 | 매주 월요일 09:00 KST 자동 | Insights/maintenance/YYYY-Www-trends.md (전략적 시사점 포함) |
| 인사이트 갱신 | `review_trigger` 기반 (Recent Updates 누적량) | Insights/ 문서 업데이트 (반자동: Recent Updates → 본문 반영) |
| 월간 Health Check | 매월 1일 09:00 KST 자동 | Insights/maintenance/YYYY-MM-health-check.md (Confidence Decay 적용 + 커버리지 보고) |

---

## 신규 카테고리 생성 프로토콜

새로운 기술 영역에 대한 인사이트가 필요할 때, 에이전트는 아래 순서를 따릅니다.

### Step 1: 카테고리 폴더 생성
- `Insights/{new-category-slug}/` 폴더 생성 (kebab-case, 영문)

### Step 2: Insights/_CONTEXT.md 카테고리 레지스트리 업데이트
- "카테고리 레지스트리" 테이블에 새 행 추가

### Step 3: AGENTS.md 라우팅 가이드 업데이트
- `AGENTS.md`의 역할별 `primary_sources`에 새 카테고리 문서 추가
- "빠른 질문 라우팅" 테이블에 대표 질문 + 경로 추가

### Step 4: 초기 인사이트 문서 생성
- `Insights/_TEMPLATE_insight.md`를 기반으로 첫 번째 인사이트 문서 생성
- `category` 필드에 새 카테고리 ID 입력
- 관련 제품 프로필에서 데이터를 읽어 초기 내용 채우기

### Step 5: _INDEX.md Dataview 쿼리 확인
- Dataview 쿼리가 category 필드 기반이므로 별도 수정 불필요 (자동 포함됨)

> **중요**: 새 카테고리 생성 전 반드시 팀원에게 확인을 받으세요. 주간 트렌드 합성 시 기존 카테고리에 매핑되지 않는 토픽이 3건 이상 반복 등장하면 "🆕 신규 카테고리 후보"로 플래깅합니다.

---

*이 파일 최종 수정: 2026-02-11*
