# AI Daily News 리서치 — 컨텍스트 가이드

> 이 파일은 AI 에이전트(Claudian, Claude CLI, 자동화 스크립트 등)가 이 디렉터리의 구조와 규칙을 이해하기 위한 메타 문서입니다. 이 디렉터리에 접근할 때 **가장 먼저** 이 파일을 읽으세요.

## 디렉터리 목적

AI 관련 일일 뉴스를 자동으로 수집, 정리, 요약하고 `AI Agent Products/` 디렉터리의 제품 업데이트 로그와 연동합니다. RSS 피드와 웹 검색을 주 소스로 사용합니다.

---

## 구조 규칙

### 폴더 구성
- `YYYY/MM/` — 연도/월별 폴더. 일일 다이제스트와 주간 요약을 포함
- 개별 기사 파일은 생성하지 않음 — 모든 뉴스는 다이제스트에 인라인 작성

### 파일 네이밍
| 파일 유형 | 네이밍 패턴 | 예시 |
|-----------|------------|------|
| 일일 다이제스트 | `YYYY-MM-DD.md` | `2026-02-10.md` |
| 주간 요약 | `YYYY-MM-Www.md` (ISO 주차) | `2026-02-W07.md` |

### 메타 파일 (루트)
| 파일 | 용도 |
|------|------|
| `_CONTEXT.md` | 이 파일. AI 에이전트용 메타 가이드 |
| `_INDEX.md` | 사람용 인덱스 (Dataview 쿼리) |
| `_TEMPLATE_daily-digest.md` | 일일 다이제스트 참조 템플릿 |
| `_TEMPLATE_weekly-summary.md` | 주간 요약 참조 템플릿 |

---

## Frontmatter 스키마

### daily-digest (필수 필드)
| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | 항상 `daily-digest` |
| `date` | date | YYYY-MM-DD 형식 |
| `tags` | list | `daily-digest`, `AI-News` 포함 |
| `sources` | list | `rss`, `web-search` 등 수집 소스 |
| `product_mentions` | list | 언급된 제품 slug 배열 (AI Agent Products 레지스트리 기준) |
| `article_count` | number | 수집된 뉴스 총 건수 |
| `status` | string | `done` (자동화이므로 생성 즉시 done) |

### weekly-summary (필수 필드)
| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | 항상 `weekly-summary` |
| `week` | string | `YYYY-Www` (ISO 주차) |
| `date_range` | string | 시작일 ~ 종료일 |
| `tags` | list | `weekly-summary`, `AI-News` 포함 |
| `total_articles` | number | 주간 총 기사 수 |
| `top_products` | list | 가장 많이 언급된 제품 slug |
| `status` | string | `done` |

---

## 뉴스 수집 소스

### RSS 피드 (14개)

| # | 피드 이름 | URL | 카테고리 |
|---|----------|-----|---------|
| 1 | LangChain Blog | `https://blog.langchain.dev/rss/` | Agent & Framework |
| 2 | OpenAI News | `https://openai.com/blog/rss.xml` | Agent & Framework |
| 3 | Google AI Blog | `https://blog.google/technology/ai/rss/` | Agent & Framework |
| 4 | Anthropic News | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml` | Agent & Framework |
| 5 | Anthropic Engineering | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml` | Agent & Framework |
| 6 | Simon Willison's Weblog | `https://simonwillison.net/atom/everything/` | Deep Tech |
| 7 | Latent.Space | `https://www.latent.space/feed` | Deep Tech |
| 8 | TechCrunch AI | `https://techcrunch.com/category/artificial-intelligence/feed/` | AI News |
| 9 | MIT Technology Review | `https://www.technologyreview.com/feed/` | AI News |
| 10 | Microsoft AI Blog | `https://blogs.microsoft.com/ai/feed/` | Vendor |
| 11 | Salesforce Blog | `https://www.salesforce.com/blog/feed/` | Vendor |
| 12 | SAP News Center | `https://news.sap.com/feed/` | Vendor |
| 13 | Databricks Blog | `https://www.databricks.com/feed` | Vendor |
| 14 | Vercel News | `https://vercel.com/atom` | Vendor |

### 웹 검색 키워드

#### 일반 키워드
- `AI agent news today`
- `LLM updates YYYY-MM-DD`
- `artificial intelligence product launch`
- `AI startup funding news`

#### 제품 그룹 타겟 검색
- **B2C**: `"Claude" OR "OpenAI" OR "Gemini" OR "Manus AI" OR "Vercel v0" AI news today`
- **Enterprise 1**: `"Salesforce Agentforce" OR "Microsoft Copilot" OR "SAP Joule" OR "ServiceNow Now Assist" news`
- **Enterprise 2**: `"Workday Assistant" OR "Oracle Digital Assistant" OR "Glean AI" news`
- **Analytics**: `"Snowflake Intelligence" OR "ThoughtSpot Spotter" OR "Databricks Mosaic AI" news`
- **한국**: `"삼성SDS" OR "LG CNS" OR "더존비즈온" OR "영림원" AI 에이전트 뉴스`

---

## 자동화 규칙

### 일일 다이제스트 생성

1. 실행 시간: 매일 03:00 KST (macOS launchd + Claude CLI)
2. 실행 흐름:
   - RSS 피드 14개를 WebFetch로 수집 → 오늘/어제 발행 기사 필터링
   - WebSearch로 일반 키워드 4개 + 제품 그룹 5개 = 9개 검색
   - 중복 제거 (같은 URL 또는 매우 유사한 제목)
   - 중요도 판단 후 높음/보통/낮음으로 분류
   - `YYYY/MM/YYYY-MM-DD.md` 파일 생성 (이미 존재하면 최신 데이터로 덮어쓰기)
3. 폴더 자동 생성: `YYYY/MM/` 폴더가 없으면 자동 생성

### 다이제스트 본문 작성 규칙

각 뉴스 항목은 다음 형식으로 작성:

```
#### 뉴스 제목
**소스**: [기사 제목](URL) | **관련 제품**: [[product-slug/product-slug|제품명]]
요약 2-3문장. (중요도 높음일 때)
요약 1-2문장. (중요도 보통/낮음일 때)
```

관련 제품이 있고 중요도가 '높음'이면 다음 표시 추가:
```
> 💡 **제품 업데이트 반영 완료** → [[product-slug/product-slug_updates]]
```

### 중요도 판단 기준 (엔터프라이즈 ERP AI 에이전트 개발 관점)

> 이 리서치의 핵심 목적은 **개발 중인 엔터프라이즈 ERP 기반 AI 에이전트**에 반영하거나 파악해야 할 소식을 수집하는 것입니다.

| 중요도 | 기준 |
|--------|------|
| 🔴 높음 | ① Enterprise ERP/CRM AI 에이전트 관련 신기능·업데이트 (SAP, Salesforce, ServiceNow, Workday, Oracle, 한국 ERP 등) ② AI 에이전트 아키텍처 변화 (MCP, A2A 등 프로토콜, 에이전트 오케스트레이션, 멀티에이전트 시스템) ③ 주요 LLM 모델 출시·성능 변화 (에이전트 활용에 직접 영향) ④ 대형 인수/투자, 가격 변경, 보안 사고 ⑤ 경쟁 제품의 기능 우위 변화 (벤치마크, 비교 분석) |
| 🟡 보통 | ① B2C AI 제품 업데이트 (Claude, OpenAI, Gemini 등 일반 업데이트) ② 파트너십, 기술 블로그, API 변경 ③ AI 개발 도구·프레임워크 업데이트 (LangChain, CrewAI 등) ④ 데이터/분석 플랫폼 AI 기능 |
| 🟢 낮음 | ① 오피니언, 일반 기술 해설 ② 간접 관련 뉴스, 커뮤니티 동향 ③ AI 교육·행사 소식 |

---

## AI Agent Products 연동

### 자동 반영 기준

다음 조건을 **모두** 충족하는 뉴스만 제품 `_updates.md`에 자동 append:
1. 중요도 '높음'
2. 뉴스가 특정 제품에 **직접** 관련 (제품명/서비스명이 명시적으로 등장)
3. `AI Agent Products/_CONTEXT.md`의 제품 레지스트리에 해당 `product_id`가 존재

### 반영 프로세스

1. 뉴스 요약 시 `AI Agent Products/_CONTEXT.md`의 제품 레지스트리 및 `search_aliases`와 매칭
2. 조건 충족 시 `AI Agent Products/{slug}/{slug}_updates.md`의 `<!-- UPDATES_END -->` 마커 바로 위에 엔트리 삽입
3. frontmatter의 `last_appended`를 오늘 날짜로 갱신
4. 다이제스트에 반영 완료 표시 추가
5. 다이제스트 frontmatter의 `product_mentions`에 해당 slug 추가

### 업데이트 엔트리 형식 (AI Agent Products 규칙 준수)

```
### YYYY-MM-DD | 뉴스 제목
**소스**: [기사 제목](URL)
**요약**: 1~3문장 요약
**카테고리**: 신기능 | 가격변경 | 파트너십 | 기술업데이트 | 실적 | 기타
**영향도**: 높음 | 보통 | 낮음
```

---

## 관련 디렉터리 참조

| 디렉터리 | 관계 |
|----------|------|
| `AI Agent Products/` | 뉴스 → 제품 업데이트 반영 대상. `_CONTEXT.md`의 제품 레지스트리 참조 |
| `RSS articles/` | 기존 RSS 저장소 (레거시, 신규 저장은 이 디렉터리 사용) |
| `UI/` | UI/UX 리서치 참조 |
