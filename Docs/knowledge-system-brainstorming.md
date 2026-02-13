# KonaChain AI Research 지식 체계 — 역할별 활용 가치 & 개선 아이디어

> 2026-02-11 | 현재 볼트 구조를 분석하고, AI Engineer / PM / 기획자 각 역할이 어떤 가치를 얻을 수 있는지 브레인스토밍한 문서입니다.

---

## 1. 현재 지식 체계 진단

### 핵심 강점

이 볼트는 "경쟁사 리서치"라는 단일 목적에 맞춰 3-Layer 아키텍처(News → Products → Insights)를 일관되게 설계한 점이 가장 큰 강점입니다. 특히 Daily News가 자동 수집되어 제품 프로필의 `_updates.md`에 적재되고, 이것이 다시 Insights 문서의 `Recent Updates`로 라우팅되는 **데이터 흐름의 자동화**가 인상적입니다. AGENTS.md의 역할 기반 라우팅과 frontmatter의 `decisions` 블록은 AI 에이전트가 문서 본문을 읽지 않고도 핵심 결론에 접근할 수 있게 하여 토큰 효율성을 극대화합니다.

### 현재 커버리지 요약

현재 볼트는 19개 제품 프로필, 10개 인사이트 카테고리(약 38개 문서), 매일 자동 수집되는 뉴스 다이제스트, 그리고 UI/UX 원본 리서치를 포함합니다. 5개 에이전트 역할(frontend, backend, architecture, planning, pm)에 대한 라우팅이 정의되어 있고, Context Graph 개념 문서를 통해 코나아이 자체 제품 방향성도 기록되어 있습니다.

---

## 2. 역할별 활용 가치 분석

### 2.1 AI Engineer

AI Engineer가 이 지식 체계에서 얻을 수 있는 가장 핵심적인 가치는 **"구현 전 의사결정 비용의 절감"**입니다.

**즉시 활용 가능한 시나리오들:**

에이전트 루프를 설계해야 할 때 `agent-orchestration-loops.md`의 `decisions` 블록만 읽으면 "Plan-Act-Observe + Self-Reflection"이 권장 패턴이라는 결론을 즉시 얻을 수 있습니다. 7개 제품의 실제 구현 사례가 비교되어 있으므로 각 패턴의 trade-off를 별도로 리서치할 필요가 없습니다.

MCP 서버를 구현할 때 `mcp-server-implementations.md`에서 3가지 구현 패턴(Managed, Self-hosted, Hybrid)의 장단점이 정리되어 있어 아키텍처 결정을 빠르게 내릴 수 있습니다. RAG 구축 시에도 `rag-architecture-comparison.md`에서 3가지 아키텍처 패턴을 바로 비교할 수 있습니다.

Tool calling 패턴 선택(Schema-First vs Semantic-First), 에이전트 메모리 관리 전략, 병렬 처리 아키텍처 등 개발 과정에서 반복적으로 마주치는 설계 결정들이 이미 교차 분석된 상태로 존재합니다.

**추가적으로 기대할 수 있는 가치:**

OSS 프레임워크 랜드스케이프 문서를 통해 LangChain, CrewAI, AutoGen 등의 비교 분석을 얻을 수 있고, `agent-permission-models.md`에서 보안 아키텍처 설계 시 참고할 권한 모델 패턴을 확인할 수 있습니다. 일일 뉴스 파이프라인이 새로운 OSS 도구나 프레임워크 릴리스를 자동으로 포착하므로 기술 트렌드를 놓치지 않을 수 있습니다.

---

### 2.2 PM (Product Manager)

PM에게 이 지식 체계의 핵심 가치는 **"데이터 기반 전략 수립과 경영진 커뮤니케이션의 효율화"**입니다.

**즉시 활용 가능한 시나리오들:**

경영진 브리핑이 필요할 때 `competitive-landscape-executive-summary.md`를 열면 경쟁 환경 요약이 준비되어 있습니다. 19개 제품의 포지셔닝, 투자 현황, 주요 전략이 한 문서에 정리되어 있어 별도의 리서치 시간 없이 보고 자료의 뼈대를 잡을 수 있습니다.

과금 모델을 설계해야 할 때 `pricing-models-comparison.md`에서 Salesforce의 대화당 $2 모델, Snowflake의 크레딧 기반 모델 등 실제 시장에서 검증된 과금 체계를 비교할 수 있습니다. GTM 전략 수립 시에도 `go-to-market-patterns.md`에서 경쟁사들의 GTM 패턴을 참조할 수 있습니다.

`feature-gap-analysis.md`는 KonaChain의 현재 기능 수준을 경쟁사 19개와 비교하여 어떤 기능을 우선 개발해야 하는지 우선순위 제안까지 포함합니다. `funding-valuation-tracker.md`는 경쟁사의 투자 동향을 추적하여 시장의 자금 흐름과 밸류에이션 트렌드를 파악할 수 있게 합니다.

**일일 뉴스 자동 수집의 PM 관점 가치:**

매일 자동으로 수집되는 뉴스 다이제스트와 Teams 알림을 통해 경쟁사의 새 기능 출시, 가격 변경, 파트너십 체결 등을 놓치지 않고 추적할 수 있습니다. 이 정보가 자동으로 해당 제품의 `_updates.md`에 적재되므로, 특정 경쟁사에 대한 시계열 변화를 한눈에 파악할 수 있습니다.

---

### 2.3 기획자 (Product Planner)

기획자에게 이 지식 체계는 **"경쟁사 벤치마킹 기반의 구체적인 요구사항 도출"**에 핵심 가치를 제공합니다.

**즉시 활용 가능한 시나리오들:**

새 기능의 UX를 기획할 때 `hitl-approval-patterns.md`에서 5가지 HITL 승인 UI 패턴을 비교하고, Risk-Based Rendering 전략을 참고하여 "어떤 상황에서 사용자 승인을 요청할 것인가"를 체계적으로 설계할 수 있습니다. `conversational-ui-patterns.md`에서는 채팅, 사이드패널, 임베디드 등 대화형 UI의 기본 구조를 정의할 때 경쟁사 사례를 참조할 수 있습니다.

제품 로드맵을 기획할 때 `product-roadmap-comparison.md`에서 경쟁사들의 로드맵을 비교하고, `feature-gap-analysis.md`에서 "우리에게 없는데 경쟁사에는 있는 기능"을 정량적으로 파악할 수 있습니다. `enterprise-vs-b2c-strategies.md`는 시장 진입 전략의 방향성을 결정할 때 핵심 참고 자료가 됩니다.

에이전트 Skill 기획 시 `agent-skill-design.md`에서 4가지 설계 패턴을, `agent-marketplace-ecosystem.md`에서 마켓플레이스 생태계 설계 방법론을 참고할 수 있습니다. 한국 시장 특화 기획에는 `korea-erp-ai-landscape.md`가 두존, 영림원, 삼성SDS, LG CNS 등 국내 경쟁사 현황을 제공합니다.

---

## 3. 추가 아이디어: 새로운 카테고리 & 콘텐츠

### 3.1 Implementation Playbook 카테고리 (`Insights/playbooks/`)

현재 인사이트 문서들은 "무엇을 선택할 것인가"에 초점이 맞춰져 있지만, "어떻게 구현할 것인가"에 대한 단계별 가이드가 부족합니다. 예를 들어 `mcp-server-implementations.md`에서 "Managed 패턴을 채택하라"는 결론을 얻은 후, 실제 구현 시 어떤 순서로 무엇을 해야 하는지를 담은 플레이북이 있으면 Engineer의 실행 속도가 크게 향상됩니다.

제안하는 플레이북 목록으로는 MCP 서버 구축 플레이북, RAG 파이프라인 구축 플레이북, 에이전트 루프 구현 플레이북, HITL 승인 플로우 구현 플레이북, Context Graph 구축 플레이북 등이 있습니다.

### 3.2 Use Case Library (`Insights/use-cases/`)

현재 볼트는 "기술 패턴"과 "경쟁사 분석" 중심이지만, "사용자 시나리오" 관점의 정리가 약합니다. `Research_v4.1_Context Graphs.md`에 신용 한도 증액 시나리오가 있지만, 이런 시나리오를 체계적으로 관리하는 레이어가 없습니다.

ERP 맥락에서의 핵심 사용 사례를 유형별로 정리하면 기획자가 요구사항을 도출할 때, PM이 고객에게 가치를 설명할 때, Engineer가 기술 요구사항을 이해할 때 모두 활용할 수 있습니다. 예를 들어 매출 하락 원인 분석, 발주 자동화, 채권 관리 알림, 원가 이상 탐지 등 ERP 도메인에 특화된 시나리오 라이브러리가 필요합니다.

### 3.3 Performance & Cost Benchmark (`Insights/benchmarks/`)

현재 `agent-evaluation-benchmarks.md`가 있지만, 실제 운영 관점의 성능/비용 벤치마크가 부족합니다. 에이전트 응답 레이턴시(경쟁사별), 토큰 소비량(패턴별), API 호출 비용(모델별), RAG 검색 정확도(아키텍처별) 등을 정량적으로 비교하는 문서가 있으면 Engineer의 아키텍처 결정과 PM의 비용 예측에 큰 도움이 됩니다.

### 3.4 Compliance & Regulatory Landscape (`Insights/compliance/`)

엔터프라이즈 AI 에이전트 제품에서 규제 준수는 점점 더 중요해지고 있습니다. EU AI Act, 한국 AI 기본법(안), 금융/의료 분야별 규제, 데이터 프라이버시(GDPR, 개인정보보호법) 등을 경쟁사의 대응 전략과 함께 정리하면, 특히 엔터프라이즈 고객 대상 영업과 제품 설계에서 차별화 포인트가 됩니다.

### 3.5 Customer Voice & Adoption Tracker

경쟁사 제품의 실제 사용자 피드백(G2, Gartner Peer Insights, Reddit, Hacker News 등)을 수집하여 "사용자들이 무엇에 불만인가", "어떤 기능을 가장 원하는가"를 추적하는 레이어입니다. 이 데이터는 기획자의 요구사항 우선순위와 PM의 차별화 전략 수립에 직접 활용됩니다.

---

## 4. 수정 아이디어: 기존 구조 개선

### 4.1 AGENTS.md에 역할 추가

현재 5개 역할(frontend, backend, architecture, planning, pm)이 정의되어 있으나, 실무에서 필요한 몇 가지 역할이 빠져 있습니다.

**`qa_agent` (QA/테스트)**를 추가하면 `agent-evaluation-benchmarks.md`, `agent-guardrails-safety.md`, `agent-permission-models.md`를 primary source로 하여 품질 보증과 테스트 전략 수립에 활용할 수 있습니다.

**`data_agent` (데이터 엔지니어/사이언티스트)**를 추가하면 Knowledge & Data 카테고리 전체를 primary source로 하여 데이터 파이프라인 설계와 RAG 최적화를 담당할 수 있습니다.

**`sales_agent` (영업/BD)**를 추가하면 Market, Strategy 카테고리와 제품 프로필의 가격/GTM 섹션을 primary source로 하여 경쟁 PT 자료 작성과 고객 제안서 준비에 활용할 수 있습니다.

### 4.2 Decision Records 독립 레이어

현재 `decisions` 블록이 각 인사이트 문서의 frontmatter에 분산되어 있어, "우리 팀이 지금까지 내린 모든 기술 결정"을 한눈에 보기 어렵습니다.

`Insights/decisions/` 디렉터리를 만들어 ADR(Architecture Decision Record) 형식의 독립 문서로 관리하고, 인사이트 문서에서는 해당 ADR을 참조하는 구조로 바꾸면 의사결정 이력 추적이 훨씬 용이해집니다. 각 ADR에는 "결정 상태(proposed/accepted/deprecated/superseded)", "결정 일자", "결정자", "대체된 이전 결정 링크"를 포함합니다.

### 4.3 Insight 성숙도 모델 (Confidence Decay)

현재 `confidence` 필드가 `high/medium/low`로 정적으로 설정되어 있습니다. AI 에이전트 시장은 매우 빠르게 변하므로, 시간이 지남에 따라 confidence가 자동으로 감소하는 모델을 도입하면 좋겠습니다.

예를 들어, `last_updated`로부터 2주 경과 시 confidence를 한 단계 낮추고, `status`를 `needs-update`로 자동 변경하는 규칙을 추가합니다. `review_trigger`의 자동 트리거 방식과 결합하면 "Recent Updates에 새 데이터가 5건 이상 쌓였는데 아직 본문에 반영되지 않은 문서"를 자동으로 식별하여 리뷰 우선순위를 매길 수 있습니다.

### 4.4 Cross-Reference 시각화

현재 문서 간 관계가 `source_files`와 wikilink로 표현되지만, 전체 지식 그래프를 시각화하는 뷰가 없습니다. Obsidian의 Graph View를 활용하되, 다음과 같은 커스텀 뷰를 추가하면 좋겠습니다.

첫째, "의사결정 의존성 그래프" — 어떤 결정이 다른 결정에 의존하는지(예: MCP 구현 패턴 결정 → Tool Calling 패턴 결정 → Skill 설계 패턴 결정). 둘째, "정보 흐름 그래프" — Daily News → Product Updates → Insights로 데이터가 어떻게 흘러가는지. 셋째, "역할별 문서 맵" — 특정 역할이 어떤 문서를 참조하는지를 시각적으로 표현.

### 4.5 주간 트렌드 합성 자동화 강화

현재 주간 트렌드 합성이 "매주 월요일 수동/반자동"으로 되어 있습니다. Daily News 파이프라인처럼 완전 자동화하되, 단순 요약이 아니라 "이번 주의 전략적 시사점"을 도출하는 합성을 자동화하면 PM과 기획자의 주간 리듬에 맞는 인텔리전스를 제공할 수 있습니다.

자동화 시 포함할 요소는 이번 주 가장 임팩트 높은 뉴스 Top 5, 경쟁사별 주요 움직임 요약, KonaChain 제품에 대한 시사점(Action Items), 그리고 신규 카테고리 후보 플래깅(3건 이상 반복 토픽)입니다.

### 4.6 내부 의사결정 로그 레이어

현재 볼트는 "외부 경쟁 정보"에 집중되어 있지만, "내부 의사결정과 그 근거"를 기록하는 레이어가 없습니다. 스프린트 리뷰, 기술 검토 회의, 제품 전략 회의에서 나온 결정사항을 기록하고, 해당 결정의 근거가 된 인사이트 문서를 역참조하면 "왜 이 결정을 내렸는가"를 나중에 추적할 수 있습니다.

이는 Context Graph 문서에서 강조한 "Decision Traces(의사결정 이력 + 근거)"의 개념을 볼트 자체에도 적용하는 것입니다.

---

## 5. 새로운 자동화 파이프라인 아이디어

### 5.1 경쟁사 기능 변경 알림 (Feature Change Alert)

Daily News 파이프라인을 확장하여, 경쟁사의 기능 업데이트가 감지되면 `feature-gap-analysis.md`의 해당 항목을 자동으로 하이라이트하고 PM/기획자에게 알림을 보내는 파이프라인입니다. 예를 들어 "Salesforce Agentforce가 새로운 MCP 지원을 발표"하면, 기능 격차 분석 문서의 MCP 관련 행이 자동으로 업데이트되고 Teams 알림이 발송됩니다.

### 5.2 월간 인사이트 Health Check

매월 1일에 자동으로 실행되는 파이프라인으로, 모든 인사이트 문서의 `last_updated`, `status`, `confidence`, `next_review`를 검사하여 "건강 보고서"를 생성합니다. 어떤 문서가 stale한지, 어떤 문서에 반영되지 않은 Recent Updates가 쌓여 있는지, 어떤 카테고리의 커버리지가 부족한지를 한눈에 파악할 수 있습니다.

### 5.3 온디맨드 Q&A 봇

현재 AGENTS.md의 "빠른 질문 라우팅" 테이블이 정적입니다. 이를 Slack/Teams 봇으로 확장하여, 팀원이 자연어로 질문하면 AGENTS.md 라우팅을 기반으로 가장 관련성 높은 문서를 찾아주고, `decisions` 블록에서 핵심 권장사항을 즉시 반환하는 봇을 만들 수 있습니다. RAG 기반으로 볼트 전체를 인덱싱하면 더 정확한 답변이 가능합니다.

---

## 6. 우선순위 제안

위 아이디어들을 영향도(Impact)와 구현 난이도(Effort)로 분류하면 다음과 같습니다.

**높은 영향 / 낮은 노력 (즉시 실행):**
- AGENTS.md에 qa_agent, data_agent, sales_agent 역할 추가
- Insight Confidence Decay 규칙 추가 (frontmatter 자동 검사 스크립트)
- 주간 트렌드 합성 완전 자동화

**높은 영향 / 중간 노력 (1-2주 내 실행):**
- Use Case Library 카테고리 신설 및 초기 시나리오 5개 작성
- ADR(Architecture Decision Records) 독립 레이어 구축
- 월간 인사이트 Health Check 파이프라인

**높은 영향 / 높은 노력 (로드맵에 반영):**
- Implementation Playbook 카테고리 (문서 작성에 시간 소요)
- Compliance & Regulatory Landscape 카테고리 (리서치 필요)
- 온디맨드 Q&A 봇 (RAG 인덱싱 + 봇 개발)

**중간 영향 / 중간 노력 (기회가 되면):**
- Customer Voice & Adoption Tracker
- Performance & Cost Benchmark
- Cross-Reference 시각화

---

*이 문서는 현재 볼트 구조(`_CONTEXT.md`, `AGENTS.md`, `Insights/_CONTEXT.md`, `AI Daily News E2E 자동화 플로우.md`)를 분석하여 작성되었습니다.*
