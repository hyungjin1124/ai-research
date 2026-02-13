---
title: AI Research 리서치 허브 — 팀 온보딩 가이드
tags:
  - onboarding
  - guide
---

# AI Research 리서치 허브 — 팀 온보딩 가이드

> 이 문서는 리서치 디렉터리에 처음 접근하는 팀원을 위한 안내서입니다.
> "이게 뭔가요?", "저는 어디부터 봐야 하나요?", "어떻게 활용하나요?"에 대한 답을 담고 있습니다.

---

## 1. 이 디렉터리는 무엇인가요?

우리가 만들고 있는 **엔터프라이즈 ERP 기반 AI 에이전트 프로덕트**를 위한 경쟁사 리서치 허브입니다. 19개 AI 에이전트 제품의 심층 분석, 매일 자동 수집되는 AI 뉴스, 그리고 이 모든 것을 교차 분석한 인사이트 문서가 하나의 체계 안에 들어 있습니다.

**한 줄 요약**: "경쟁사가 뭘 하고 있는지"를 체계적으로 정리하고 비교 분석한 지식 시스템입니다.

### 핵심 수치

| 항목 | 규모 |
|------|------|
| 분석 대상 AI 에이전트 제품 | 19개 (글로벌 + 한국) |
| 교차 분석 인사이트 문서 | ~40개 (10개 카테고리) |
| 일일 뉴스 수집 | 매일 03:00 KST 자동 (RSS 20개 + 웹 검색 14개 키워드) |
| 정의된 에이전트 역할 | 8개 (frontend, backend, architecture, planning, pm, qa, data, sales) |

---

## 2. 3-Layer 구조 이해하기

이 디렉터리는 세 개의 층으로 구성되어 있고, 위로 갈수록 정제된 정보가 담겨 있습니다.

```
┌────────────────────────────────────────────────────────┐
│  Layer 3: Insights/                                     │
│  "주제를 관통하는 교차 분석"                                │
│  → 경쟁사 간 비교와 업계 패턴 분석이 여기에 있습니다           │
├────────────────────────────────────────────────────────┤
│  Layer 2: AI Agent Products/                            │
│  "특정 제품에 대한 모든 것"                                │
│  → 경쟁사 하나를 깊이 파야 할 때                            │
├────────────────────────────────────────────────────────┤
│  Layer 1: AI Daily News/                                │
│  "지금 무슨 일이 일어나고 있는가"                           │
│  → 매일 자동으로 쌓이는 최신 뉴스                           │
└────────────────────────────────────────────────────────┘
```

**읽는 순서**: 대부분의 경우 Layer 3(Insights)부터 시작하세요. 거기서 충분한 답을 얻지 못하면 Layer 2(Products)로 내려가고, 최신 동향이 궁금하면 Layer 1(Daily News)을 확인하면 됩니다.

---

## 3. 폴더별 상세 설명

### `Insights/` — 교차 분석 인사이트 (가장 먼저 볼 곳)

여러 제품과 소스를 교차 분석한 합성 문서입니다. 특정 주제에 대해 경쟁사 간 비교와 업계 패턴을 객관적으로 정리하고 있습니다.

| 하위 폴더                  | 주제                                | 주로 보는 팀원        |
| ---------------------- | --------------------------------- | --------------- |
| `agent-skills/`        | Tool calling, MCP 서버 구현, Skill 설계 | Agent Skill 개발  |
| `agent-runtime/`       | 에이전트 루프, 병렬 처리, 메모리               | Deep Agent 아키텍처 |
| `knowledge-data/`      | RAG, 시맨틱 레이어, 임베딩, KG             | Knowledge Graph |
| `agent-ui/`            | 대화형 UI, HITL, 추론 시각화, Canvas      | UI 개발           |
| `protocols/`           | MCP, A2A, A2UI 프로토콜 비교            | 전체              |
| `open-source/`         | OSS 모델, 프레임워크, 도구                 | 전체              |
| `market/`              | 경쟁 동향, 가격 전략, 한국 ERP AI           | 전체 (전략)         |
| `strategy/`            | 경쟁 환경 요약, 로드맵 비교, Feature Gap     | PM·팀장           |
| `security-evaluation/` | 가드레일, 권한 모델, 벤치마크                 | 전체 (품질)         |


### `AI Agent Products/` — 제품별 프로필

19개 AI 에이전트 제품을 하나씩 깊이 분석한 프로필(3,000~6,000 단어)과 업데이트 로그입니다. 각 제품 폴더 안에 `{제품명}.md`(메인 프로필)과 `{제품명}_updates.md`(뉴스 로그)가 있습니다.

**분석 대상 제품**:

| 분류 | 제품 |
|------|------|
| **B2C** | Claude, OpenAI, Google Gemini, Manus AI, Vercel v0 |
| **Enterprise** | Salesforce Agentforce, Microsoft Copilot, SAP Joule, ServiceNow Now Assist, Workday Assistant, Oracle Digital Assistant |
| **Analytics** | Snowflake Intelligence, ThoughtSpot Spotter, Databricks Mosaic AI |
| **Knowledge** | Glean |
| **Korea ERP** | 두존 One AI, 영림원 K-System, 삼성SDS Fabrix, LG CNS AgenticWorks |

### `AI Daily News/` — 일일 뉴스 다이제스트

매일 새벽 3시에 자동 수집되는 AI 업계 뉴스입니다. RSS 피드 20개와 웹 검색 14개 키워드를 조합해 중요도별로 분류합니다. `YYYY/MM/YYYY-MM-DD.md` 형태로 날짜별 파일이 생성됩니다.

---

## 4. 역할별 활용 시나리오

### 시나리오 1: AI Engineer — "MCP 서버를 다른 회사들은 어떻게 구현하고 있지?"

1. `AGENTS.md`에서 `backend_agent` 역할의 `primary_sources` 확인
2. `Insights/agent-skills/mcp-server-implementations.md` 열기
3. TL;DR 섹션에서 핵심 분석과 **분석 신뢰도**(`confidence`) 확인
4. 본문의 Cross-Product Analysis에서 7개 제품의 실제 구현 사례 비교
5. 더 깊은 맥락이 필요하면 `AI Agent Products/claude/claude.md`의 아키텍처 섹션 참조

**이런 질문에도 같은 방식으로 답을 찾을 수 있습니다**:
에이전트 루프 설계(`agent-orchestration-loops.md`), RAG 구축(`rag-architecture-comparison.md`), Tool calling 패턴 선택(`tool-calling-patterns.md`), 병렬 처리 아키텍처(`agent-parallel-processing.md`)

### 시나리오 2: PM — "경영진 브리핑 자료가 급하게 필요해"

1. `Insights/strategy/competitive-landscape-executive-summary.md` 열기 → 경쟁 환경 요약이 준비되어 있음
2. 과금 모델 비교가 필요하면 `Insights/market/pricing-models-comparison.md` 참조
3. 기능 격차 분석이 필요하면 `Insights/strategy/feature-gap-analysis.md` 참조
4. 투자 동향은 `Insights/strategy/funding-valuation-tracker.md`에서 확인

### 시나리오 3: 기획자 — "새 기능의 UX를 벤치마킹하고 싶어"

1. `Insights/agent-ui/hitl-approval-patterns.md`에서 5가지 HITL 승인 UI 패턴 비교
2. `Insights/agent-ui/conversational-ui-patterns.md`에서 대화형 UI 구조 참조
3. `Insights/agent-ui/artifacts-canvas-patterns.md`에서 Canvas 레이아웃 4종 확인
4. 경쟁사별 실제 UI 사례는 `AI Agent Products/{제품}/` 프로필의 "UI/UX 분석" 섹션에서 확인

### 시나리오 4: QA — "에이전트 품질 기준을 어떻게 잡아야 하지?"

1. `Insights/security-evaluation/agent-evaluation-benchmarks.md`에서 평가 메트릭 확인
2. `Insights/security-evaluation/agent-guardrails-safety.md`에서 가드레일 패턴 참조
3. `Insights/security-evaluation/agent-permission-models.md`에서 권한 경계 테스트 시나리오 도출

### 시나리오 5: 영업/BD — "경쟁사 대비 우리 차별화 포인트를 정리해야 해"

1. `Insights/market/competitive-positioning-matrix.md`에서 포지셔닝 비교표 확인
2. `Insights/strategy/feature-gap-analysis.md`에서 우리가 우위인 기능 식별
3. 한국 시장 특화 자료는 `Insights/market/korea-erp-ai-landscape.md` 참조
4. 과금 비교표는 `Insights/market/pricing-models-comparison.md`에서 확인

### 시나리오 6: 경쟁사가 새 기능을 발표했을 때 — "어떻게 대응하지?"

1. `AI Daily News/`에서 해당 뉴스 확인 (자동 수집되어 있을 가능성 높음)
2. 해당 제품의 `AI Agent Products/{제품}/{제품}_updates.md`에서 시계열 변화 파악
3. `Insights/strategy/feature-gap-analysis.md`에서 우리 제품과의 격차 확인
4. `Insights/strategy/competitive-landscape-executive-summary.md`에서 경쟁 환경 맥락 파악

---

## 5. 자동화 파이프라인

이 디렉터리는 여러 자동화가 연결되어 살아 있는 시스템입니다.

| 파이프라인 | 트리거 | 결과물 |
|-----------|--------|--------|
| **일일 뉴스 수집** | 매일 03:00 KST (macOS launchd) | `AI Daily News/YYYY/MM/DD.md` + 제품별 `_updates.md` |
| **Git Push → GitHub Actions** | main push | Teams 채널 알림 + Quartz 웹사이트 배포 |
| **주간 트렌드 합성** | 매주 월요일 09:00 KST | `Insights/maintenance/YYYY-Www-trends.md` |
| **월간 Health Check** | 매월 1일 09:00 KST | `Insights/maintenance/YYYY-MM-health-check.md` |
| **인사이트 갱신** | `review_trigger` 기반 (Recent Updates 누적량) | Insights 문서 자동 업데이트 (반자동) |

**팀원 입장에서의 자동화 경험**: 매일 아침 Teams 채널에 전날 수집된 AI 뉴스 요약이 올라옵니다. 중요도가 높은 뉴스(🔴)는 관련 제품 프로필에도 자동으로 기록되고, 웹사이트(GitHub Pages)에서도 확인할 수 있습니다.

---

## 6. 빠른 시작 가이드

### 처음 5분: 전체 구조 파악

1. **이 문서**를 다 읽습니다 (지금 하고 계신 것)
2. `index.md`를 열어 전체 카테고리를 훑어봅니다

### 다음 10분: 내 역할에 맞는 문서 찾기

3. `AGENTS.md`를 열고 자신의 역할(8개 중 택 1)을 찾습니다
4. 해당 역할의 `primary_sources` 목록에서 관심 있는 문서 2~3개를 읽습니다

### 이후: 일상적 활용

5. 매일 Teams 알림으로 AI 뉴스 확인
6. 설계 결정이 필요할 때 → `AGENTS.md`의 "빠른 질문 라우팅" 테이블에서 해당 문서 찾기
7. 경쟁사 하나를 깊이 분석해야 할 때 → `AI Agent Products/{제품명}/`

---

## 7. 핵심 파일 안내

| 파일 | 역할 | 언제 보나요? |
|------|------|------------|
| `ONBOARDING.md` | 이 문서. 팀 온보딩 가이드 | 처음 합류했을 때 |
| `AGENTS.md` | 역할별 문서 라우팅 허브 | 내 역할에 맞는 문서를 찾을 때 |
| `_CONTEXT.md` | 볼트 전체 구조와 규칙 설명 | 디렉터리 구조를 이해하고 싶을 때 |
| `index.md` | Quartz 웹사이트 랜딩 페이지 | 웹에서 접근할 때 |
| `Insights/_INDEX.md` | 인사이트 문서 동적 인덱스 | 교차 분석 문서를 탐색할 때 |
| `AI Agent Products/_INDEX.md` | 제품 프로필 인덱스 | 특정 제품을 찾을 때 |

---

## 8. 활용 팁

**TL;DR과 frontmatter를 활용하세요.** 각 인사이트 문서의 TL;DR 섹션에 핵심 분석이 3~5개 bullet로 요약되어 있습니다. frontmatter의 `confidence`(분석 신뢰도), `status`(문서 상태), `source_products`(참조 제품)를 통해 문서의 신뢰도와 범위를 빠르게 파악할 수 있습니다.

**Obsidian에서 여는 것을 권장합니다.** 이 디렉터리는 Obsidian 볼트로 설계되었습니다. `[[문서명]]` 형태의 위키링크, Dataview 쿼리, Graph View 등이 Obsidian에서 가장 잘 작동합니다. Obsidian이 없어도 마크다운 파일이므로 어떤 에디터에서든 읽을 수 있지만, 문서 간 연결과 동적 인덱스를 활용하려면 Obsidian을 추천합니다.

**GitHub Pages 웹사이트에서도 접근 가능합니다.** Quartz v4 기반으로 자동 배포되는 웹사이트에서 모든 문서를 읽을 수 있습니다. 별도 도구 설치 없이 브라우저로 접근하고 싶을 때 활용하세요.

---

## 9. 기여 방법

이 리서치 허브는 자동화와 수동 기여가 결합된 시스템입니다.

**자동으로 관리되는 부분** (직접 수정하지 않아도 됩니다): 일일 뉴스 다이제스트, 제품별 `_updates.md` 뉴스 로그, 주간 트렌드 합성, 월간 Health Check

**팀원이 기여할 수 있는 부분**: 인사이트 문서를 읽고 "이건 업데이트가 필요하다"고 판단되면 알려주세요. 새로운 AI 에이전트 제품을 분석에 추가해야 한다면 요청해주세요. 새로운 교차 분석 주제가 필요하면 제안해주세요.

---

## 10. 자주 묻는 질문

**Q: 특정 경쟁사에 대해 빠르게 알고 싶으면?**
`AI Agent Products/{제품명}/{제품명}.md`를 열면 됩니다. 3,000~6,000 단어 분량의 심층 프로필이 있습니다.

**Q: "이 기술을 다른 회사들은 어떻게 구현하고 있지?"**
`AGENTS.md`에서 자기 역할의 `primary_sources`를 확인하세요. 해당 문서의 TL;DR과 Cross-Product Analysis 섹션에서 업계 주요 패턴과 제품별 구현 사례를 비교할 수 있습니다.

**Q: 문서 내용이 오래된 것 같은데?**
각 문서의 frontmatter에 `last_updated`, `confidence`, `status` 필드가 있습니다. Confidence Decay 규칙에 의해 오래된 문서는 자동으로 `needs-update`로 표시됩니다. 월간 Health Check 보고서(`Insights/maintenance/YYYY-MM-health-check.md`)에서 전체 건강 상태를 확인할 수 있습니다.

**Q: 새로운 주제의 분석이 필요하면?**
`_CONTEXT.md`의 "신규 카테고리 생성 프로토콜"을 참고하세요. 주간 트렌드 합성에서 3건 이상 반복 등장하는 토픽은 자동으로 "신규 카테고리 후보"로 플래깅됩니다.

---

*이 문서 최종 수정: 2026-02-11*
