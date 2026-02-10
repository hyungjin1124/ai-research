# AI Agent Products 리서치 — 컨텍스트 가이드

> 이 파일은 AI 에이전트(Claudian, 자동화 스크립트 등)가 이 디렉터리의 구조와 규칙을 이해하기 위한 메타 문서입니다. 이 디렉터리에 접근할 때 **가장 먼저** 이 파일을 읽으세요.

## 디렉터리 목적

AI Agent 서비스별 종합 리서치를 제품 단위로 정리합니다. B2C부터 Enterprise 제품까지 **플랫 구조**로 관리하며, YAML frontmatter 태그로 분류합니다.

---

## 구조 규칙

### 폴더 구성
- 각 제품은 `kebab-case` 폴더명을 가짐 (예: `salesforce-agentforce/`)
- 모든 폴더에는 반드시 다음 파일이 존재:
  - `{slug}.md` — 제품 메인 프로필 (`type: product-profile`)
  - `{slug}_updates.md` — 업데이트 로그 (`type: product-updates`)
  - `assets/` — 미디어 파일 (스크린샷, 다이어그램)

### 메타 파일 (루트)
| 파일 | 용도 |
|------|------|
| `_CONTEXT.md` | 이 파일. AI 에이전트용 메타 가이드 |
| `_INDEX.md` | 사람용 인덱스 (Dataview 쿼리) |
| `_TEMPLATE_product.md` | 제품 프로필 생성 템플릿 |
| `_TEMPLATE_updates.md` | 업데이트 로그 생성 템플릿 |

### 네이밍 규칙
- 폴더명 = slug (`kebab-case`, 영문 소문자)
- 메인 노트 파일명 = `{slug}.md`
- 업데이트 로그 파일명 = `{slug}_updates.md`
- slug는 frontmatter의 `product_id`와 반드시 동일

---

## Frontmatter 스키마

### product-profile (필수 필드)
| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | 항상 `product-profile` |
| `product_id` | string | 폴더명과 동일한 slug |
| `product_name` | string | 사람용 표시 이름 |
| `vendor` | string | 회사/개발사 |
| `category` | string | `B2C` \| `Enterprise` \| `Analytics` \| `Knowledge` |
| `tags` | list | 분류 태그 배열 |
| `status` | string | `draft` \| `in-progress` \| `done` |
| `last_updated` | date | YYYY-MM-DD 형식 |

### product-updates (필수 필드)
| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | 항상 `product-updates` |
| `product_id` | string | 부모 제품 slug |
| `tags` | list | 태그 배열 |
| `last_appended` | date | 마지막 append 날짜 |

---

## 카테고리 체계

| category 값 | 설명 | 예시 |
|-------------|------|------|
| `B2C` | 일반 사용자 대상 AI 어시스턴트 | Claude, OpenAI, Google Gemini, Manus AI |
| `Enterprise` | 기업용 에이전트 (ERP/CRM/ITSM 통합) | Salesforce, SAP, Microsoft, ServiceNow, Workday, Oracle, 삼성SDS, LG CNS, 더존비즈온, 영림원 |
| `Analytics` | 데이터 분석 특화 에이전트 | Snowflake, ThoughtSpot, Databricks |
| `Knowledge` | 기업 지식 관리/검색 특화 | Glean |

---

## 제품 레지스트리

| product_id | product_name | vendor | category |
|------------|-------------|--------|----------|
| claude | Claude | Anthropic | B2C |
| openai | OpenAI | OpenAI | B2C |
| google-gemini | Google Gemini | Google | B2C |
| manus-ai | Manus AI | Manus | B2C |
| salesforce-agentforce | Salesforce Agentforce | Salesforce | Enterprise |
| microsoft-copilot | Microsoft Copilot for Dynamics 365 | Microsoft | Enterprise |
| sap-joule | SAP Joule | SAP | Enterprise |
| servicenow-now-assist | ServiceNow Now Assist | ServiceNow | Enterprise |
| workday-assistant | Workday Assistant | Workday | Enterprise |
| oracle-digital-assistant | Oracle Digital Assistant | Oracle | Enterprise |
| snowflake-intelligence | Snowflake Intelligence | Snowflake | Analytics |
| thoughtspot-spotter | ThoughtSpot Spotter | ThoughtSpot | Analytics |
| databricks-mosaic-ai | Databricks Mosaic AI | Databricks | Analytics |
| glean | Glean | Glean | Knowledge |
| vercel-v0 | Vercel v0 | Vercel | B2C |
| samsung-sds-fabrix | 삼성SDS FabriX & Brity Copilot | 삼성SDS | Enterprise |
| lgcns-agenticworks | LG CNS AgenticWorks & a:xink | LG CNS | Enterprise |
| douzone-one-ai | 더존 ONE AI (위하고) | 더존비즈온 | Enterprise |
| younglimwon-ksystem | 영림원 K-System Ace I&I | 영림원소프트랩 | Enterprise |

### 제품 검색 별칭 (search_aliases)

> 뉴스 수집 시 제품명 매칭 정확도를 높이기 위한 별칭 목록입니다. 뉴스 본문에 아래 키워드가 등장하면 해당 `product_id`로 매칭합니다.

| product_id | search_aliases |
|------------|---------------|
| claude | Claude, Claude AI, Anthropic Claude |
| openai | OpenAI, ChatGPT, GPT-4, GPT-5, o1, o3 |
| google-gemini | Gemini, Google Gemini, Gemini AI, Bard |
| manus-ai | Manus AI, Manus |
| salesforce-agentforce | Agentforce, Salesforce Agentforce, Einstein AI |
| microsoft-copilot | Microsoft Copilot, Copilot for Dynamics 365, M365 Copilot, Copilot Studio |
| sap-joule | SAP Joule, Joule AI, SAP Business AI |
| servicenow-now-assist | Now Assist, ServiceNow AI, Now Platform AI |
| workday-assistant | Workday Assistant, Workday AI |
| oracle-digital-assistant | Oracle Digital Assistant, ODA, Oracle AI |
| snowflake-intelligence | Snowflake Intelligence, Snowflake Cortex |
| thoughtspot-spotter | ThoughtSpot Spotter, Spotter AI |
| databricks-mosaic-ai | Mosaic AI, Databricks AI, DBRX |
| glean | Glean, Glean AI |
| vercel-v0 | v0, Vercel v0, v0.dev |
| samsung-sds-fabrix | 삼성SDS, FabriX, Brity Copilot, 삼성SDS AI |
| lgcns-agenticworks | LG CNS, AgenticWorks, a:xink, LG CNS AI |
| douzone-one-ai | 더존, 더존비즈온, ONE AI, 위하고, 더존 AI |
| younglimwon-ksystem | 영림원, K-System, 영림원소프트랩, K-System Ace |

---

## 자동화 규칙

### 새 업데이트 추가 시

1. 대상 파일: `{slug}/{slug}_updates.md`
2. `<!-- UPDATES_END -->` 마커 바로 **위**에 새 엔트리를 삽입
3. frontmatter의 `last_appended`를 오늘 날짜(YYYY-MM-DD)로 갱신
4. 엔트리 형식:

```
### YYYY-MM-DD | 제목

**소스**: [기사 제목](URL)
**요약**: 1~3문장 요약
**카테고리**: 신기능 | 가격변경 | 파트너십 | 기술업데이트 | 실적 | 기타
**영향도**: 높음 | 보통 | 낮음
```

### 새 제품 추가 시

1. 이 파일의 **제품 레지스트리** 테이블에 행 추가
2. `{new-slug}/` 폴더 생성
3. `_TEMPLATE_product.md`를 복사 → `{new-slug}/{new-slug}.md` 생성, 필드 채우기
4. `_TEMPLATE_updates.md`를 복사 → `{new-slug}/{new-slug}_updates.md` 생성, 필드 채우기
5. `{new-slug}/assets/` 폴더 생성
6. `_INDEX.md`는 Dataview가 자동 갱신하므로 수동 편집 불필요

### 기존 리서치 참조

`KonaChain/리서치/UI/` 폴더의 기존 분석은 제품 메인 노트의 `related` frontmatter 필드와 "관련 리서치" 섹션에서 wikilink로 참조합니다. 기존 파일은 이동하지 않습니다.

| 기존 위치 | 연결 대상 |
|-----------|----------|
| `UI/04_Claude_Cowork_분석/` | `claude/claude.md` |
| `UI/03_Manus_AI_분석/` | `manus-ai/manus-ai.md` |
| `UI/01_벤치마크_서비스비교/` | 크로스 제품 비교 — 개별 제품에서 링크 |
