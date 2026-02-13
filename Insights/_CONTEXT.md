# Insights 계층 — 컨텍스트 가이드

> 이 파일은 AI 에이전트가 Insights 디렉터리에 접근할 때 읽는 메타 가이드입니다.
> 루트 `_CONTEXT.md`를 먼저 읽고, 특정 인사이트 카테고리에 진입할 때 이 파일을 참조하세요.

## 디렉터리 목적

여러 제품과 소스(AI Agent Products, AI Daily News)를 **교차 분석**하여 도출한 **합성 인사이트** 문서를 관리합니다. 에이전트나 팀원이 특정 주제에 대한 분석을 빠르게 얻을 수 있습니다.

---

## 카테고리 레지스트리

| category_id           | 표시명              | 설명                                                     | 대상 팀               |
| --------------------- | ---------------- | ------------------------------------------------------ | ------------------ |
| `agent-skills`        | Agent Skills     | Tool calling, MCP 서버 구현, skill 설계, function calling 패턴 | Agent Skill 개발     |
| `agent-runtime`       | Agent Runtime    | 에이전트 루프, 병렬 처리, 파일시스템 활용, 메모리, 코드 실행                   | Deep Agent 아키텍처    |
| `knowledge-data`      | Knowledge & Data | RAG, 시맨틱 레이어, 임베딩, 컨텍스트 그래프, 데이터 카탈로그                  | Knowledge Graph 세팅 |
| `agent-ui`            | Agent UI         | 대화형 UI, HITL, 추론 시각화, Artifacts/Canvas, 대시보드           | UI 개발              |
| `protocols`           | Protocols        | MCP, A2A, A2UI, MCP-UI 프로토콜 비교 및 도입 가이드                | 전체                 |
| `open-source`         | Open Source      | OSS 모델, 프레임워크, 에이전트 도구, 라이브러리 동향                       | 전체                 |
| `market`              | Market           | 경쟁 동향, 가격 전략, 한국 ERP AI, 파트너십 생태계                      | 전체                 |
| `strategy`            | Strategy         | 경쟁 환경 요약, 로드맵 비교, Feature Gap, GTM 전략                  | PM·팀장              |
| `security-evaluation` | Security & Eval  | 가드레일, 권한 모델, 벤치마크, 에이전트 평가                             | 전체                 |
| `maintenance`         | Maintenance      | 주간 트렌드 합성 + 월간 Health Check                             | 전체                 |

---

## 문서 타입

| type 값 | 용도 | 템플릿 |
|---------|------|--------|
| `insight-synthesis` | 주제별 교차 분석 (패턴 분류, 핵심 발견 포함) | `_TEMPLATE_insight.md` |

---

## Frontmatter 스키마

### insight-synthesis (필수 필드)

| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | `insight-synthesis` |
| `topic_id` | string | kebab-case slug (파일명과 동일) |
| `topic_name` | string | 사람용 표시 이름 |
| `category` | string | 위 카테고리 레지스트리의 `category_id` 값 |
| `tags` | list | `[insight, {category}, ...]` |
| `status` | string | `draft` \| `current` \| `needs-update` |
| `confidence` | string | `high` \| `medium` \| `low` |
| `last_updated` | date | YYYY-MM-DD |
| `source_products` | list | 참조한 product_id 목록 |
| `source_files` | list | wikilink 경로 목록 |
| `auto_update` | object | 자동화 설정 (아래 참조) |
| `relevant_roles` | list | AGENTS.md 라우팅 기반 관련 역할 목록 (예: `[frontend_agent, pm_agent]`) |

### auto_update 필드

| 하위 필드 | 타입 | 설명 |
|-----------|------|------|
| `enabled` | boolean | 자동화 파이프라인 참여 여부 (모든 문서 `true` 기본) |
| `keywords` | list | RSS/웹 검색에 사용할 키워드 목록 (한국어+영어 혼합 권장) |
| `feeds` | list | 관련 RSS 피드 URL 목록 |
| `review_trigger` | object | 자동 트리거 기반 리뷰 (Recent Updates 누적량 기준) |
| `update_zones` | list | (선택) 본문 섹션별 자동 업데이트 영역 매핑 |

#### review_trigger

Recent Updates 누적량에 따라 본문 반영을 자동으로 트리거합니다.

| 하위 필드 | 타입 | 설명 |
|-----------|------|------|
| `mode` | string | `"auto"` (자동 트리거) |
| `threshold` | number | 본문 반영 트리거에 필요한 Recent Updates 최소 누적 건수 |
| `priority_override` | boolean | `true`이면 high-importance 항목 1건만으로도 즉시 트리거 |

#### update_zones (섹션별 자동 업데이트 매핑)

본문의 `<!-- auto-update-zone: {id} -->` 마커와 1:1 매핑됩니다. 뉴스 수집 시 `match_keywords`로 영향받는 섹션을 자동 분류하여 Recent Updates의 `Affected` 컬럼에 기록합니다.

| 하위 필드 | 타입 | 설명 |
|-----------|------|------|
| `id` | string | zone 식별자 (본문 마커의 id와 동일) |
| `section` | string | 대응하는 본문 섹션 제목 |
| `match_keywords` | list | 이 zone에 해당하는 뉴스를 매칭하는 키워드 |

---

## 문서 작성 규칙

### 필수 섹션 (인사이트 문서)
1. **TL;DR** — 3~5개 핵심 bullet. 에이전트가 이것만 읽어도 답을 얻을 수 있어야 함. 모든 bullet에 인라인 출처 필수
2. **Overview** — 주제의 산업 배경을 팩트 기반으로 서술. 주관적 해석 배제
3. **Cross-Product Analysis** — 비교 매트릭스(Source 컬럼 필수) + 패턴 분류
4. **Key Findings** — 교차 분석에서 도출된 비자명한 인사이트. 모든 항목에 인라인 출처 필수
5. **Recent Updates** — 자동화 시스템이 새 데이터를 append하는 영역 (아래 자동화 규칙 참조)
6. **References** — 각주 번호별 상세 출처 (Vault + External 2개 하위 섹션)

### 인용 규칙

#### 원칙
- **모든 팩트성 서술에 인라인 출처 필수** — 각주 번호 `[^N]` 사용
- References 섹션에 각주 번호별 상세 출처 기재
- 독자가 출처를 클릭하면 바로 원본에 접근 가능해야 함
- 출처 없는 팩트성 주장에는 `[출처 필요]` 태그 부착

#### 출처 유형별 포맷

| 유형 | References 섹션 포맷 |
|------|---------------------|
| Vault 제품 프로필 | `[^N]: [[AI Agent Products/product/product\|Display Name]] — 참조 섹션명` |
| 외부 문서/기사 | `[^N]: [Article Title](URL) (YYYY-MM-DD) — 참조한 내용 설명` |
| 공식 문서 (날짜 불명) | `[^N]: [Title](URL) — 참조한 내용 설명` |

#### 인라인 인용 예시

```markdown
<!-- 본문에서 -->
Salesforce Agentforce는 대화당 $2의 과금 모델을 채택했다 [^1].
Snowflake는 Managed MCP Server를 통해 RBAC 기반 접근 제어를 구현한다 [^2].

<!-- References 섹션에서 -->
### Vault
- [^1]: [[AI Agent Products/salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] — Pricing 섹션

### External
- [^2]: [Snowflake Managed MCP Server Docs](https://docs.snowflake.com/...) (2026-01-15) — RBAC 구현 상세
```

### 자동화 규칙 (Recent Updates)

#### 구조
- `## Recent Updates` 섹션은 **자동화 시스템 전용 append 영역**
- 기본 테이블 형식: `| Date | Source | Summary | Tags |`
- `update_zones` 사용 문서: `| Date | Source | Summary | Affected | Tags |` (`Affected`에 zone id 기록)
- 새 행은 테이블 **맨 위에** append (최신순)

#### 자동 append 규칙
- Date: ISO 8601 (`YYYY-MM-DD`)
- Source: 반드시 클릭 가능한 링크 (`[Title](URL)` 또는 `[[wikilink]]`)
- Summary: 100자 이내
- Tags: 기존 카테고리 태그 재활용 (`#market`, `#protocol` 등)

#### 리뷰 워크플로우

1. Recent Updates 누적 건수가 `threshold` 이상이거나, `priority_override: true`이고 high-importance 항목이 도착하면 리뷰 트리거
2. `Affected` 컬럼을 기준으로 영향받는 `auto-update-zone` 섹션을 식별
3. 해당 섹션의 테이블/분석 내용을 새 데이터 기반으로 업데이트
4. 반영된 항목은 테이블에서 제거하거나 아카이브

#### Daily News 라우팅 수신 (2단계 동적 매칭)

- `AI Daily News/`에서 `topic_tags` + 중요도 '높음' 조건을 충족한 뉴스가 자동으로 Recent Updates에 append됨
- append 형식은 위의 "자동 append 규칙"과 동일
- **2단계 동적 라우팅**: ① topic_tag → 해당 카테고리의 모든 enabled 문서를 후보로 수집 ② 뉴스 내용과 각 문서의 `auto_update.keywords`를 대조하여 매칭 문서만 라우팅 (매칭 0건이면 카테고리별 폴백 허브 문서에 라우팅)
- 새 문서 추가 시 `keywords`만 설정하면 자동으로 라우팅 대상에 포함됨
- 동일 뉴스 중복 감지: URL 기반으로 체크하여 먼저 append된 쪽을 유지

### Staleness 관리
- `review_trigger`를 사용하여 Recent Updates 누적량 기반으로 리뷰 시점을 자동 결정
- `status`가 `needs-update`인 문서는 `_INDEX.md`에서 하이라이트됨
- `auto_update.enabled: true`인 문서는 Recent Updates에 자동 데이터가 쌓이므로, 리뷰 시 반영 여부 판단 필수

### Confidence Decay (신뢰도 자동 감소)

AI 에이전트 시장은 빠르게 변하므로, 시간 경과에 따라 인사이트의 신뢰도를 자동으로 감소시킵니다.

#### 감소 규칙

| 카테고리 그룹 | 감소 주기 | `high` → `medium` | `medium` → `low` | `low` → `needs-update` |
|-------------|----------|-------------------|-------------------|----------------------|
| 고빈도 변동 (`market`, `maintenance`, `strategy`) | 2주 | `last_updated` + 14일 | `last_updated` + 28일 | `last_updated` + 42일 |
| 중빈도 변동 (`agent-skills`, `agent-runtime`, `knowledge-data`, `agent-ui`, `open-source`) | 3주 | `last_updated` + 21일 | `last_updated` + 42일 | `last_updated` + 63일 |
| 저빈도 변동 (`protocols`, `security-evaluation`) | 4주 | `last_updated` + 28일 | `last_updated` + 56일 | `last_updated` + 84일 |

#### 자동 적용 규칙
1. 월간 Health Check 스크립트가 매월 1일에 실행
2. `last_updated` 기준 경과일에 따라 `confidence`와 `status`를 자동 업데이트
3. `status: needs-update`로 변경된 문서는 `_INDEX.md`에서 🔴 하이라이트
4. Recent Updates에 미반영 항목이 5건 이상이면 `confidence`를 추가로 1단계 감소
5. 문서 본문 업데이트 시 `last_updated`를 갱신하면 `confidence`가 원래 설정값으로 복원됨

#### 예외
- `review_trigger` 방식을 사용하는 문서는 threshold 기반 트리거가 우선. Confidence Decay와 독립적으로 동작하되, 둘 중 더 빠른 시점에 리뷰가 트리거됨
- `maintenance` 카테고리의 주간 트렌드는 생성 시점에 `confidence: medium`이 기본이며, 다음 주 월요일에 `low`로 전환됨 (주간 데이터의 특성)

---

## 신규 카테고리 추가 시

1. 이 파일의 **카테고리 레지스트리** 테이블에 행 추가
2. `Insights/{new-slug}/` 폴더 생성
3. `AGENTS.md`의 역할별 `primary_sources`에 새 카테고리 문서 추가 + "빠른 질문 라우팅" 테이블에 대표 질문 추가
4. `_TEMPLATE_insight.md` 기반으로 첫 인사이트 문서 생성
5. `_INDEX.md`의 Dataview는 category 필드 기반이므로 자동 반영됨

---

## 기존 레이어와의 관계

| Insights 카테고리         | 주요 소스 (AI Agent Products)   | 주요 소스 (AI Daily News)            |
| --------------------- | --------------------------- | -------------------------------- |
| `agent-skills`        | MCP-Support 태그 제품들          | topic_tag: `agent-skills`        |
| `agent-runtime`       | 전 제품 아키텍처 섹션                | topic_tag: `agent-runtime`       |
| `knowledge-data`      | Analytics 카테고리 + Glean      | topic_tag: `knowledge-data`      |
| `agent-ui`            | 전 제품 UI/UX 분석 섹션            | topic_tag: `agent-ui`            |
| `protocols`           | MCP-Support, A2A-Support 태그 | topic_tag: `protocols`           |
| `open-source`         | (간접)                        | topic_tag: `open-source`         |
| `market`              | Korea-ERP 태그 + 전체           | topic_tag: `market`              |
| `strategy`            | 전 제품 경쟁 포지셔닝 섹션             | topic_tag: `strategy`            |
| `security-evaluation` | 전 제품 보안/권한 섹션               | topic_tag: `security-evaluation` |
| `maintenance`         | —                           | Daily Digest 전체 교차 분석 + Health Check |


> `maintenance` 카테고리는 `AI Daily News/`를 주 소스로 사용합니다.
> 나머지 카테고리는 2단계 동적 매칭(topic_tag → keywords)으로 자동 라우팅됩니다. 새 문서 추가 시 `auto_update.keywords`만 설정하면 자동으로 라우팅 대상에 포함됩니다.
