# AI Daily News 리서치 — 컨텍스트 가이드

> 이 파일은 AI 에이전트(Claudian, Claude CLI, 자동화 스크립트 등)가 이 디렉터리의 구조와 규칙을 이해하기 위한 메타 문서입니다. 이 디렉터리에 접근할 때 **가장 먼저** 이 파일을 읽으세요.

## 디렉터리 목적

AI 관련 일일 뉴스와 커뮤니티 인사이트를 자동으로 수집·정리하여 두 가지 역할을 수행합니다:

1. **트리거 + 가이드**: `AI Agent Products/`와 `Insights/`의 최신화가 필요한 시점과 범위를 식별합니다.
   - **자동 처리**: Product `_updates.md` 로그 추가, Insight `Recent Updates` 테이블 행 추가 (확장 요약으로 충분)
   - **Deep Dive 트리거**: Product Profile 본문, Insight 본문 갱신이 필요한 경우 ⚠️ 플래그 + Deep Dive Queue로 관리 (추가 조사 필요)
2. **팀 일일 다이제스트**: AI Engineer 팀원/PM/팀장/기획자가 매일 접근하여 새로운 이슈, 커뮤니티 트렌드, 실전 팁을 파악합니다.

RSS 피드, 웹 검색, 커뮤니티 소스(X, Reddit, HN)를 사용합니다.

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
| `sources` | list | `rss`, `web-search`, `community` 등 수집 소스 |
| `product_mentions` | list | 언급된 제품 slug 배열 (AI Agent Products 레지스트리 기준) |
| `topic_tags` | list | Insights 카테고리와 매칭된 주제 태그 배열 |
| `article_count` | number | 수집된 뉴스 총 건수 |
| `community_count` | number | 커뮤니티 소스에서 수집된 항목 수 |
| `deep_dive_count` | number | Deep Dive Queue에 등록된 항목 수 |
| `status` | string | `done` (자동화이므로 생성 즉시 done) |

### weekly-summary (필수 필드)
| 필드 | 타입 | 설명 |
|------|------|------|
| `type` | string | 항상 `weekly-summary` |
| `week` | string | `YYYY-Www` (ISO 주차) |
| `date_range` | string | 시작일 ~ 종료일 |
| `tags` | list | `weekly-summary`, `AI-News` 포함 |
| `total_articles` | number | 주간 총 기사 수 |
| `total_community` | number | 주간 커뮤니티 수집 항목 수 |
| `deep_dive_resolved` | number | 이번 주 처리 완료된 Deep Dive 항목 수 |
| `deep_dive_pending` | number | 미처리 Deep Dive 항목 수 (다음 주 이월) |
| `top_products` | list | 가장 많이 언급된 제품 slug |
| `top_topics` | list | 가장 많이 태그된 topic_tag 목록 |
| `status` | string | `done` |

---

## 뉴스 수집 소스

### RSS 피드 (20개)

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
| 10 | Microsoft Azure Blog | `https://azure.microsoft.com/en-us/blog/feed/` | Vendor |
| 11 | Salesforce Blog | `https://www.salesforce.com/blog/feed/` | Vendor |
| 12 | SAP News Center | `https://news.sap.com/feed/` | Vendor |
| 13 | Databricks Blog | `https://www.databricks.com/feed` | Vendor |
| 14 | Vercel News | `https://vercel.com/atom` | Vendor |
| 15 | Microsoft Research | `https://www.microsoft.com/en-us/research/feed/` | Deep Tech |
| 16 | HuggingFace Blog | `https://huggingface.co/blog/feed.xml` | OSS & Research |
| 17 | GitHub Blog | `https://github.blog/feed/` | OSS & Research |
| 18 | arXiv cs.AI | `https://export.arxiv.org/rss/cs.AI` | OSS & Research |
| 19 | AI Safety Newsletter (CAIS) | `https://newsletter.safe.ai/feed` | Security & Eval |
| 20 | Changelog | `https://changelog.com/feed` | OSS & Research |

### 커뮤니티 소스

> 공식 채널(RSS/웹 검색)에서 포착되지 않는 실전 활용법, 개발자 팁, 커뮤니티 반응을 수집합니다.

#### 모니터링 대상

| 플랫폼 | 수집 대상 | 수집 방법 |
|--------|----------|----------|
| X (Twitter) | AI 인플루언서 20-30명 리스트 | WebSearch `site:x.com` 또는 `from:@handle` 검색 |
| Reddit | r/MachineLearning, r/LocalLLaMA, r/ChatGPTPro | WebSearch `site:reddit.com` 키워드 검색 |
| Hacker News | AI 관련 프론트페이지 게시물 | WebSearch `site:news.ycombinator.com` 키워드 검색 |
| YouTube (선택) | AI 기술 채널 신규 영상 | WebSearch `site:youtube.com` 키워드 검색 |

#### X 주요 모니터링 계정 (초기 리스트)

| 카테고리        | 계정                                                  |
| ----------- | --------------------------------------------------- |
| AI 연구/사고 리더 | @kaborek, @AndrewYNg, @ylecun, @sama                |
| 개발자/엔지니어    | @simonw, @swyx, @karpathy, @jeremyphoward, @bcherny |
| AI 에이전트/도구  | @LangChainAI, @CrewAIInc, @AnthropicAI, @OpenAI     |
| 엔터프라이즈 AI   | @datababoreks, @ServiceNow, @workaborday            |

> 이 리스트는 초기 버전이며, 수집 결과의 가치를 기반으로 주기적으로 갱신합니다.

#### 커뮤니티 검색 키워드

- `site:reddit.com (r/MachineLearning OR r/LocalLLaMA) "AI agent" OR "MCP" OR "LLM" tip workflow`
- `site:reddit.com r/ChatGPTPro "Claude" OR "GPT" workflow prompt`
- `site:news.ycombinator.com "AI agent" OR "MCP" OR "LangGraph" OR "Claude Code"`
- `site:x.com "AI agent" tip OR workflow OR "how I use" from:(@karpathy OR @simonw OR @swyx)`

---

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

#### 주제 타겟 검색
- **OSS 프레임워크**: `"CrewAI" OR "AutoGen" OR "smolagents" OR "LangGraph" agent framework release`
- **데이터 인프라**: `"LlamaIndex" OR "Pinecone" OR "Weaviate" OR "Qdrant" vector database RAG update`
- **AI 시장/전략**: `"AI agent" market analysis OR "enterprise AI" strategy report 2026`
- **AI 안전/규제**: `"AI safety regulation" OR "LLM guardrails" OR "EU AI Act" OR "OWASP LLM" 2026`
- **프로토콜**: `"MCP server" OR "Model Context Protocol" OR "A2A protocol" specification update`

---

## 자동화 규칙

### 일일 다이제스트 생성

1. 실행 시간: 매일 03:00 KST (macOS launchd + Claude CLI)
2. 실행 흐름:
   - RSS 피드 20개를 WebFetch로 수집 → 오늘/어제 발행 기사 필터링
   - WebSearch로 일반 키워드 4개 + 제품 그룹 5개 + 주제 타겟 5개 = 14개 검색
   - 커뮤니티 검색 키워드 4개로 WebSearch 수집 → Community Pulse 소스 확보 (아래 `Community Pulse 수집` 규칙 참조)
   - 중복 제거 (같은 URL 또는 매우 유사한 제목)
   - 중요도 판단 후 높음/보통/낮음으로 분류
   - product_mentions 매핑 (제품 레지스트리 + search_aliases 대조)
   - topic_tags 매핑 (topic_tags 매핑 테이블 대조)
   - ⚠️ 본문 갱신 필요 판단 → Deep Dive Queue 항목 등록 (아래 `Deep Dive Queue 생성` 규칙 참조)
   - `YYYY/MM/YYYY-MM-DD.md` 파일 생성 (주요 뉴스 + Community Pulse + Deep Dive Queue 포함)
   - 조건 충족 뉴스 → Products _updates.md에 자동 반영
   - 조건 충족 뉴스 → Insights Recent Updates에 자동 라우팅
   - 이메일 요약 전송 (높음 + 보통 + Community Pulse + Deep Dive 알림)
3. 폴더 자동 생성: `YYYY/MM/` 폴더가 없으면 자동 생성

### Community Pulse 수집

1. RSS/웹 검색 수집 완료 후 실행
2. 실행 흐름:
   - 커뮤니티 검색 키워드 4개를 WebSearch로 실행
   - 높은 engagement(리트윗 500+, 업보트 200+, HN 포인트 100+) 게시물 필터링
   - 뉴스 섹션과 중복 여부 확인 (같은 주제의 공식 발표가 이미 수집된 경우 커뮤니티 반응만 기록)
   - 화제의 스레드(2-5건)와 실전 Tip(1-3건)으로 분류
   - 커뮤니티 센티먼트는 해당일 주요 뉴스에 대한 반응이 뚜렷할 때만 작성
3. 작성 원칙:
   - 화제의 스레드: "왜 화제인지"와 "핵심 주장"을 명확히 기술
   - 실전 Tip: 도구명, 구체적 단계, 기대 효과를 명시하여 팀원이 바로 시도할 수 있는 수준으로 작성
   - 커뮤니티 센티먼트: 긍정/부정/혼재를 구분하고 대표적 의견을 인용
4. 수집 건수가 0인 날도 있을 수 있음 (커뮤니티 활동이 적은 주말 등). 이 경우 섹션 자체를 비워둠

### Deep Dive Queue 생성

1. 뉴스 작성 시 "본문 갱신 필요" 여부를 판단하여 ⚠️ 플래그 부착
2. 판단 기준:
   - **Product Profile 갱신 대상**: 뉴스가 등록 제품의 핵심 기능, 아키텍처, 가격, 경쟁 포지셔닝에 영향을 주는 경우
   - **Insight 본문 갱신 대상**: 뉴스가 기존 Insight의 비교 매트릭스, Key Findings, 패턴 분류에 영향을 주는 경우
3. ⚠️ 플래그가 부착된 항목을 `## Deep Dive Queue` 테이블에 집약
4. 각 항목에 다음을 기재:
   - **갱신 범위**: 어떤 섹션이 영향받는지 구체적으로 명시 (예: "패턴 B 재분류, Key Finding 재검토")
   - **확인 소스**: Deep Dive 시 참조해야 할 소스 (예: "공식 문서, API 레퍼런스, Migration Guide")
   - **난이도**: 높음(원문+문서+코드 확인) / 보통(원문+문서 확인) / 낮음(원문만으로 충분)
5. frontmatter의 `deep_dive_count`를 Queue 항목 총수로 갱신

### Deep Dive 실행 (수동/반자동, 주 1-2회)

> Daily Digest의 자동화 범위 밖. Deep Dive Queue를 기반으로 별도 실행합니다.

1. 해당 주의 미처리 Deep Dive Queue 항목을 수집 (일일 다이제스트에서 추출)
2. 우선순위 결정: 높음 난이도 + 높음 중요도 뉴스 → 먼저 처리
3. 실행 흐름:
   - Queue 항목의 "확인 소스"를 참조하여 원문, 공식 문서, API 레퍼런스 등을 조사
   - Product Profile: 해당 제품 `.md` 본문의 관련 섹션을 갱신하고 `last_updated` 수정
   - Insight 본문: 비교 매트릭스, Key Findings 등 관련 섹션을 갱신하고 `last_updated` 수정
   - 갱신 완료 후 원본 다이제스트의 ⚠️ 플래그에 처리 완료 표시 추가
4. 처리 결과는 주간 요약의 "Deep Dive 처리 현황" 섹션에 집약

---

### 이메일 전략 브리핑 전송

다이제스트 생성 완료 후 KonaChain 전략 인텔리전스 브리핑을 이메일로 전송합니다.

**전송 서비스**: Resend API
| 설정 | 값 |
|------|-----|
| API Endpoint | `https://api.resend.com/emails` |
| API Key | 환경변수 `RESEND_API_KEY` 사용 (`~/.zshrc` 또는 `~/.bash_profile`에 설정) |
| 발신자 | `KonaChain Intel <onboarding@resend.dev>` (도메인 인증 전 기본값) |
| 수신자 | `hyungjin9758@gmail.com` |
| Content-Type | `text/html` (Markdown → HTML 변환) |

> **도메인 인증 후**: `resend.com/domains`에서 자체 도메인을 인증하면 발신자를 `intel@yourdomain.com` 등으로 변경 가능합니다.

**수신자**: 형진 (hyungjin9758@gmail.com)

**이메일 형식:**

```
제목: [KonaChain Intel] YYYY-MM-DD — {오늘의 핵심 신호 1} · {오늘의 핵심 신호 2}

본문:

## 오늘의 핵심 판단

{Executive Signal 3-5문장. KonaChain 관점에서 오늘의 뉴스를 하나의 내러티브로 합성.}

---

## 🔴 긴급 대응 (N건)

### 뉴스 제목
[역할태그] | 소스: [기사 제목](URL)

**무슨 일인가:** 핵심 사실 2-3문장.

**KonaChain 임팩트:**
- 🏗️/📊/💰/🎯/⚠️ **차원명**: 구체적 임팩트 1-2문장 (해당 차원만)

**다음 단계:**
- [ ] [역할] 구체적 액션 (시간 프레임)

---

## 🟡 경쟁 동향 & 시장 신호 (M건)

| 뉴스 | 대상 | KonaChain 시사점 | 소스 |
|------|------|-----------------|------|
| **제목** [역할] | 관련 제품 | 한 줄 시사점 | [원문](URL) |

---

## 💬 개발자 레이더 (K건)

| 신호 | 시사점 |
|------|--------|
| **제목** (플랫폼, 반응 수) | 한 줄 시사점 [역할] |

---

## ⚠️ Deep Dive 필요 (해당 시에만)

- **뉴스 제목** → `대상-문서.md` (갱신 범위) — 난이도

---
전체 다이제스트: [[YYYY/MM/YYYY-MM-DD]]
🌐 [웹에서 보기](https://hyungjin1124.github.io/ai-research/AI-Daily-News/YYYY/MM/YYYY-MM-DD)
미처리 Deep Dive: N건
```

**전송 규칙:**
- Executive Signal: 반드시 포함 (이메일의 핵심)
- 긴급 대응: 높음 중 KonaChain 직접 영향 항목만 (최대 4건)
- 경쟁 동향: 보통 + 나머지 높음. 테이블 형식. KonaChain 시사점 컬럼 필수
- 개발자 레이더: 커뮤니티 상위 3-4건. 테이블 형식
- 낮음: 이메일에 포함하지 않음
- 제목: `[KonaChain Intel]` 프리픽스 + 오늘의 핵심 신호 2개

### 다이제스트 본문 작성 규칙

각 뉴스 항목은 다음 형식으로 작성:

```
#### 뉴스 제목
**소스**: [기사 제목](URL) | **관련 제품**: [[product-slug/product-slug|제품명]]
**태그**: `#topic-tag-1` `#topic-tag-2`
확장 요약 5-8문장. 핵심 수치, 기술 상세, 영향 분석을 포함. (중요도 높음일 때)
요약 2-3문장. (중요도 보통일 때)
요약 1문장. (중요도 낮음일 때)
```

> **작성 원칙**: 확장 요약(높음)은 Products `_updates.md` 로그 추가와 Insights `Recent Updates` 테이블 행 추가의 **1차 소스**로 사용된다. 원문 재방문 없이도 로그/테이블 반영이 가능한 수준의 정보(수치, 기능명, 비교 대상, 영향 범위 등)를 포함해야 한다. 단, Product Profile 본문이나 Insight 본문의 갱신은 확장 요약만으로는 불충분하며, ⚠️ 플래그를 통해 Deep Dive Queue로 분리한다.

**`**태그**` 라인 규칙:**
- 모든 중요도의 뉴스에 topic_tags 매핑 테이블 기준으로 부여
- 관련 제품 없이도 태그 부여 가능 (product_mentions와 독립)
- 태그가 없는 뉴스는 `**태그**: —` 로 표시

**연동 표시 규칙:**

관련 제품이 있고 중요도가 '높음' 또는 '보통'이면 다음 표시 추가:
```
> 💡 **제품 업데이트 반영 완료** → [[product-slug/product-slug_updates]]
```

topic_tags가 있고 중요도가 '높음'이면 다음 표시 추가:
```
> 📌 **Insights 라우팅 완료** → topic: `protocols`, `open-source`
```

**본문 갱신 필요 (⚠️) 플래그 규칙:**

뉴스가 기존 Product Profile 또는 Insight 본문의 실질적 내용(비교 매트릭스, 아키텍처, Key Findings, 핵심 기능, 경쟁 포지셔닝 등)에 영향을 주는 경우 다음 표시 추가:
```
> ⚠️ **본문 갱신 필요**:
>   - `대상-문서.md` — 갱신 범위 설명 (어떤 섹션이 영향받는지)
>   - 예상 난이도: 높음|보통|낮음
```

⚠️ 플래그는 `_updates.md` 로그 추가나 `Recent Updates` 테이블 행 추가와는 독립적이다. 로그/테이블 추가는 확장 요약으로 충분하지만, 본문 갱신은 원문·공식 문서·API 레퍼런스 등 추가 소스 확인이 필요하므로 Deep Dive Queue로 분리한다.

**⚠️ 플래그 판단 기준:**

| 대상 | 플래그 부착 조건 |
|------|---------------|
| Product Profile | 뉴스가 등록 제품의 핵심 기능 추가/변경, 아키텍처 전환, 가격 모델 변경, 경쟁 포지셔닝 변화에 해당 |
| Insight 본문 | 뉴스가 기존 Insight의 패턴 분류, 비교 매트릭스, Key Findings의 전제를 변경하거나 무효화하는 경우 |

**⚠️ 플래그가 불필요한 경우:**
- 기존 내용을 보강하지만 구조적 변화가 없는 뉴스 (예: 기존 기능의 마이너 업데이트)
- Product _updates.md 로그 추가만으로 충분한 뉴스
- Insights Recent Updates 테이블 행 추가만으로 충분한 뉴스

### 중요도 판단 기준 (엔터프라이즈 ERP AI 에이전트 개발 관점)

> 이 리서치의 핵심 목적은 **개발 중인 엔터프라이즈 ERP 기반 AI 에이전트**에 반영하거나 파악해야 할 소식을 수집하는 것입니다.

| 중요도 | 기준 |
|--------|------|
| 🔴 높음 | ① Enterprise ERP/CRM AI 에이전트 관련 신기능·업데이트 (SAP, Salesforce, ServiceNow, Workday, Oracle, 한국 ERP 등) ② AI 에이전트 아키텍처 변화 (MCP, A2A 등 프로토콜, 에이전트 오케스트레이션, 멀티에이전트 시스템) ③ 주요 LLM 모델 출시·성능 변화 (에이전트 활용에 직접 영향) ④ 대형 인수/투자, 가격 변경, 보안 사고 ⑤ 경쟁 제품의 기능 우위 변화 (벤치마크, 비교 분석) ⑥ 에이전트 개발에 직접 영향을 주는 비제품 기술 변화 (주요 OSS 프레임워크 메이저 릴리즈, 벡터 DB 아키텍처 전환, MCP/A2A 스펙 변경, OWASP LLM Top 10 개정, 주요 AI 규제 시행 등) |
| 🟡 보통 | ① B2C AI 제품 업데이트 (Claude, OpenAI, Gemini 등 일반 업데이트) ② 파트너십, 기술 블로그, API 변경 ③ AI 개발 도구·프레임워크 업데이트 (LangChain, CrewAI 등) ④ 데이터/분석 플랫폼 AI 기능 ⑤ 비제품 생태계 동향 (OSS 모델 출시, 학술 연구 트렌드, 인프라 도구 업데이트) |
| 🟢 낮음 | ① 오피니언, 일반 기술 해설 ② 간접 관련 뉴스, 커뮤니티 동향 ③ AI 교육·행사 소식 |

### topic_tags 매핑

> 뉴스 주제에 따라 Insights 카테고리와 연결합니다. `product_mentions`와 독립적으로 부여합니다.
> 하나의 뉴스에 여러 topic_tags를 부여할 수 있습니다.

| topic_tag | 매핑 키워드 | 설명 |
|-----------|-----------|------|
| `agent-skills` | MCP server, tool calling, function calling, skill, plugin | 에이전트 스킬 설계 |
| `agent-runtime` | agent loop, orchestration, ReAct, planning, multi-agent, parallel | 에이전트 런타임 아키텍처 |
| `knowledge-data` | RAG, vector database, embedding, semantic layer, knowledge graph | 지식·데이터 관리 |
| `agent-ui` | agent UI, HITL, human-in-the-loop, artifacts, canvas, chat UI | 에이전트 UI/UX |
| `protocols` | MCP, A2A, A2UI, protocol, interoperability | 프로토콜 표준 |
| `open-source` | open source, OSS, HuggingFace, GitHub, CrewAI, AutoGen, LangGraph | 오픈소스 생태계 |
| `market` | funding, acquisition, valuation, partnership, market share | 시장·경쟁 동향 |
| `strategy` | roadmap, go-to-market, pricing, strategy | 전략·포지셔닝 |
| `security-evaluation` | guardrail, safety, benchmark, evaluation, regulation, OWASP, NIST | 보안·평가·규제 |

---

## AI Agent Products 연동

### 자동 반영 기준

다음 조건을 **모두** 충족하는 뉴스를 제품 `_updates.md`에 자동 append:
1. 중요도 '높음' 또는 '보통'
2. 뉴스가 특정 제품에 **직접** 관련 (제품명/서비스명이 명시적으로 등장)
3. `AI Agent Products/_CONTEXT.md`의 제품 레지스트리에 해당 `product_id`가 존재

> 변경 이력: 기존 '높음'만 반영 → '보통' 이상으로 확대 (2026-02-11). 보통 등급 신기능·파트너십 뉴스 누락 방지.

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

## Insights 연동

> **중요: Insights 연동은 2개 레이어로 구성됩니다.**
>
> | 레이어 | 실행 시점 | 내용 | Daily Digest로 충분? |
> |--------|---------|------|-------------------|
> | **Layer 1: Recent Updates 테이블** | 일일 자동화 | `## Recent Updates` 테이블에 행 추가 (날짜, 출처, 100자 요약) | ✅ 충분 |
> | **Layer 2: 본문 갱신** | Deep Dive (주 1-2회) | 비교 매트릭스, Key Findings 등 본문 섹션 수정 | ❌ 추가 조사 필요 |
>
> Layer 1은 기존 자동 라우팅 프로세스로 처리합니다. Layer 2는 Daily Digest의 ⚠️ 플래그로 트리거하고, Deep Dive Queue를 통해 별도 처리합니다.

### 자동 라우팅 기준 (Layer 1: Recent Updates 테이블)

다음 조건을 **모두** 충족하는 뉴스를 해당 Insights 문서의 `Recent Updates` 테이블에 append:
1. 중요도 '높음'
2. `topic_tags`가 1개 이상 부여됨
3. 해당 topic_tag의 카테고리에 `auto_update.enabled: true`인 Insights 문서가 존재

### 라우팅 대상 문서

| topic_tag | 라우팅 대상 Insight 문서 |
|-----------|----------------------|
| `protocols` | `Insights/protocols/protocol-comparison-mcp-a2a-a2ui.md` |
| `open-source` | `Insights/open-source/agent-frameworks-landscape.md` |
| `security-evaluation` | `Insights/security-evaluation/agent-guardrails-safety.md` |
| `knowledge-data` | `Insights/knowledge-data/rag-architecture-comparison.md` |
| `market` | `Insights/strategy/funding-valuation-tracker.md` |
| `strategy` | `Insights/strategy/build-vs-buy-decision-framework.md`, `Insights/strategy/feature-gap-analysis.md` |

> 위 목록에 없는 topic_tag는 Daily News에만 기록됩니다. 라우팅 대상은 필요 시 추가합니다.

### 라우팅 프로세스

1. 뉴스의 `**태그**` 라인에서 topic_tags 확인
2. 조건 충족 시 대상 Insight 문서의 `## Recent Updates` 테이블 최상단에 행 삽입
3. 대상 문서에 `update_zones`가 있으면 `Affected` 컬럼도 채움 (아래 규칙 참조)
4. 다이제스트에 라우팅 완료 표시 추가
5. 다이제스트 frontmatter의 `topic_tags`에 해당 태그 추가

> **중요**: 라우팅 대상 문서에는 반드시 `## Recent Updates` 섹션이 존재해야 합니다. 없으면 라우팅이 실패합니다.

### 라우팅 엔트리 형식 (Insights 규칙 준수)

**기본 형식** (update_zones 없는 문서):

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| YYYY-MM-DD | [기사 제목](URL) · [[YYYY/MM/YYYY-MM-DD\|다이제스트]] | 100자 이내 요약 | #topic-tag |

**확장 형식** (update_zones 있는 문서, 예: build-vs-buy-decision-framework):

| Date | Source | Summary | Affected | Tags |
|------|--------|---------|----------|------|
| YYYY-MM-DD | [기사 제목](URL) · [[YYYY/MM/YYYY-MM-DD\|다이제스트]] | 100자 이내 요약 | `zone-id` | #topic-tag |

**Affected 컬럼 결정 방법:**
1. 대상 문서 frontmatter의 `auto_update.update_zones[].match_keywords` 배열과 뉴스 내용 대조
2. 매칭된 zone의 `id` 값을 기입 (복수 매칭 시 쉼표 구분: `llm, agent-framework`)
3. 매칭 zone이 없으면 `—` 기입

> Source 컬럼에 Daily News 다이제스트 역참조 링크를 포함합니다. 시간이 지나 원문 URL이 깨져도 확장 요약을 통해 정보를 복원할 수 있습니다.

### 제품 연동과의 관계

- 하나의 뉴스가 `product_mentions`와 `topic_tags`를 **동시에** 가질 수 있음
- 예: "Salesforce가 MCP 서버 공식 지원" → product_mentions: `salesforce-agentforce` + topic_tags: `protocols`, `agent-skills`
- 이 경우 Products `_updates.md` **와** Insights `Recent Updates` **양쪽에** 반영

---

## 관련 디렉터리 참조

| 디렉터리 | 관계 |
|----------|------|
| `AI Agent Products/` | 뉴스 → 제품 업데이트 반영 대상. `_CONTEXT.md`의 제품 레지스트리 참조 |
| `RSS articles/` | 기존 RSS 저장소 (레거시, 신규 저장은 이 디렉터리 사용) |
| `UI/` | UI/UX 리서치 참조 |
| `Insights/maintenance/` | 주간 트렌드 합성 + 월간 Health Check. Daily Digest를 교차 분석하여 트렌드·패턴 도출 |
| `Insights/` | 뉴스 → topic_tags 기반 라우팅 대상. **Layer 1**: 중요도 높음 + topic_tags 매칭 시 Recent Updates에 자동 append. **Layer 2**: ⚠️ 플래그 뉴스는 Deep Dive Queue를 통해 본문 갱신. 트렌드 파악은 `Insights/maintenance/` 참조 |
