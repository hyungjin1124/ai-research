---
type: insight-synthesis
topic_id: funding-valuation-tracker
topic_name: AI 에이전트 기업 투자·밸류에이션 추적
category: strategy
tags:
- insight
- strategy
- funding
- valuation
- investment
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- openai
- claude
- google-gemini
- salesforce-agentforce
- microsoft-copilot
- servicenow-now-assist
- workday-assistant
- sap-joule
- snowflake-intelligence
- databricks-mosaic-ai
- glean
- manus-ai
- vercel-v0
- samsung-sds-fabrix
- lgcns-agenticworks
source_files:
- AI Agent Products/openai/openai.md
- AI Agent Products/claude/claude.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/snowflake-intelligence/snowflake-intelligence.md
- AI Agent Products/databricks-mosaic-ai/databricks-mosaic-ai.md
- AI Agent Products/glean/glean.md
- AI Agent Products/manus-ai/manus-ai.md
- AI Agent Products/vercel-v0/vercel-v0.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
relevant_roles:
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI startup funding round
  - AI company valuation
  - AI IPO
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# AI 에이전트 기업 투자·밸류에이션 추적

## TL;DR

- AI 에이전트 시장의 투자 규모는 역대 최대 수준이며, **OpenAI($157B+)와 Anthropic($60B+)이 비상장 AI 기업 밸류에이션의 양대 축**을 형성한다. 두 기업의 합산 밸류에이션은 많은 Fortune 500 기업의 시가총액을 초과한다.
- 상장 엔터프라이즈 벤더 중 **Salesforce(시가총액 ~$260B), Microsoft(~$3.1T), Google(~$2.1T)**가 AI 에이전트 전략에 가장 공격적으로 투자하고 있으며, 이들의 R&D 지출 규모는 스타트업과 비교 불가능한 수준이다.
- **엔터프라이즈 AI 검색/에이전트 스타트업**인 Glean($7.2B 밸류에이션, ARR $100M+)은 가장 빠른 성장세를 보이며, Manus AI는 출시 8개월 만에 ARR $100M을 돌파한 뒤 Meta에 $2B로 인수되었다.
- 한국 기업(삼성SDS, LG CNS)은 독립적 AI 밸류에이션 산정이 어렵지만, **모기업 그룹사 차원의 AI 투자 규모**(삼성 그룹 AI 투자, LG AI연구원 엑사원)는 글로벌 스타트업을 상회한다.
- 투자 트렌드는 **"LLM 인프라"에서 "에이전트 애플리케이션"으로 이동** 중이며, 이는 애플리케이션 레이어에 더 많은 자본이 유입될 것임을 시사한다.

---

## Overview

2025-2026년 AI 투자 시장은 2000년대 닷컴 버블 이후 가장 큰 규모의 자본이 유입되고 있으며, 특히 에이전트 AI 영역은 "생성형 AI의 다음 단계"로 인식되어 투자자들의 관심이 집중되고 있다. [^1] [^2] 이 문서는 리서치 대상 15개 제품의 기업별 투자/밸류에이션 현황을 추적하고, 그 패턴에서 유의미한 전략적 시사점을 도출한다.

---

## Cross-Product Analysis

### 기업 유형별 밸류에이션/시가총액 매트릭스

#### A. 비상장 LLM 네이티브 기업

| 기업 | 최근 밸류에이션 | 주요 투자 라운드 | ARR/매출 | 핵심 제품 | Source |
|------|---------------|----------------|---------|----------|--------|
| **OpenAI** | ~$157B (2025-03) | SoftBank $40B 리드, 총 $300B+ 누적 | ARR $12.7B+ (2025-10 추정) | [[openai/openai\|ChatGPT, GPT-5.2, Codex]] | [^1] |
| **Anthropic** | ~$60B (2025-01) | Lightspeed $2B, Google $2B+, Amazon $4B | ARR $2B+ (2025 추정) | [[claude/claude\|Claude, Claude Code, MCP]] | [^2] |

#### B. 비상장 에이전트 애플리케이션 기업

| 기업 | 최근 밸류에이션 | 주요 투자 라운드 | ARR/매출 | 핵심 제품 | Source |
|------|---------------|----------------|---------|----------|--------|
| **Glean** | $7.2B (2025-06) | Series E $150M | ARR $100M+ (2025) | [[glean/glean\|Enterprise Search, AI Agents]] | [^11] |
| **Manus AI** | $2B (인수가, 2025-12) | Meta에 ~$2B 인수 | ARR $100M 런레이트 (출시 8개월) | [[manus-ai/manus-ai\|자율 AI 에이전트]] | [^12] |
| **Vercel** | ~$3.5B (2024-05) | Series E $250M | 비공개 | [[vercel-v0/vercel-v0\|v0, Next.js 플랫폼]] | [^13] |
| **Databricks** | ~$62B (2024-09) | Series J $10B | ARR $2.4B+ (2024) | [[databricks-mosaic-ai/databricks-mosaic-ai\|Mosaic AI, Unity Catalog]] | [^10] |

#### C. 상장 글로벌 엔터프라이즈 벤더

| 기업 | 시가총액 (2026-02 추정) | AI 관련 매출 | AI 에이전트 전략 강도 | 핵심 제품 | Source |
|------|----------------------|------------|---------------------|----------|--------|
| **Microsoft** | ~$3.1T | Copilot 매출 비공개, Azure AI $10B+ 런레이트 | 매우 높음 | [[microsoft-copilot/microsoft-copilot\|Copilot for D365]] | [^5] |
| **Google (Alphabet)** | ~$2.1T | Google Cloud AI 매출 $X0B+ [출처 필요] | 매우 높음 | [[google-gemini/google-gemini\|Gemini, Project Mariner]] | [^3] |
| **Salesforce** | ~$260B | Data Cloud + AI 매출 급성장 | 매우 높음 | [[salesforce-agentforce/salesforce-agentforce\|Agentforce]] | [^4] |
| **SAP** | ~$290B | RISE with SAP AI 번들, AI Unit 과금 | 높음 | [[sap-joule/sap-joule\|Joule, 2400+ Skills]] | [^8] |
| **ServiceNow** | ~$200B | Now Assist AI 매출 빠른 성장 | 높음 | [[servicenow-now-assist/servicenow-now-assist\|Now Assist, AI Agents]] | [^6] |
| **Workday** | ~$70B | Illuminate AI 매출 초기 | 중간-높음 | [[workday-assistant/workday-assistant\|Illuminate, ASOR]] | [^7] |
| **Snowflake** | ~$55B | Cortex AI 크레딧 매출 초기 | 중간 | [[snowflake-intelligence/snowflake-intelligence\|Intelligence, Cortex]] | [^9] |

#### D. 한국 기업

| 기업 | 시가총액/규모 | AI 투자 현황 | 핵심 제품 | Source |
|------|-------------|-------------|----------|--------|
| **삼성SDS** | ~15조 원 (상장) | 삼성 그룹 차원 AI 투자 (SCP, NVIDIA GPU 대규모 확보), OpenAI 리셀러 | [[samsung-sds-fabrix/samsung-sds-fabrix\|FabriX, Brity Copilot]] | [^14] |
| **LG CNS** | 비상장 (LG 계열) | LG AI연구원 엑사원 투자, 코히어 기술 협력, 클라인 JDA | [[lgcns-agenticworks/lgcns-agenticworks\|AgenticWorks, a:xink]] | [^15] |

### 투자 단계별 시장 구조

```
[Tier 1: 조단위 투자]
  OpenAI ($157B), Anthropic ($60B), Databricks ($62B)
  → LLM 인프라 + 플랫폼 레이어

[Tier 2: 대형 상장사]
  Microsoft ($3.1T), Google ($2.1T), Salesforce ($260B), SAP ($290B)
  → 기존 엔터프라이즈 플랫폼에 AI 통합

[Tier 3: 중형 상장사/유니콘]
  ServiceNow ($200B), Workday ($70B), Snowflake ($55B), Glean ($7.2B)
  → 도메인 특화 AI 에이전트

[Tier 4: 고성장 스타트업]
  Manus AI ($2B 인수), Vercel ($3.5B)
  → 새로운 카테고리 창출형 제품

[Tier 5: 한국 기업]
  삼성SDS (~15조 원), LG CNS (비상장)
  → 그룹사 생태계 기반 AI 전환
```

### 밸류에이션 대비 매출 배수 분석

| 기업 | 밸류에이션/시총 | ARR 추정 | 매출 배수 (P/S) | 성장률 | Source |
|------|---------------|---------|---------------|--------|--------|
| OpenAI | $157B | $12.7B | ~12x | 매우 높음 (전년 대비 3x+) | [^1] |
| Anthropic | $60B | $2B | ~30x | 매우 높음 (전년 대비 5x+) | [^2] |
| Databricks | $62B | $2.4B | ~26x | 높음 (전년 대비 60%+) | [^10] |
| Glean | $7.2B | $100M+ | ~60-70x | 매우 높음 (ARR $100M 돌파) | [^11] |
| Salesforce | $260B | ~$38B (전체) | ~7x | 중간 (AI 매출은 고성장) | [^4] |
| ServiceNow | $200B | ~$12B (전체) | ~17x | 높음 (AI 매출 급성장) | [^6] |
| Snowflake | $55B | ~$3.5B (전체) | ~16x | 중간-높음 | [^9] |

**패턴**: AI 네이티브 스타트업(Anthropic 30x, Glean 60-70x)이 기존 엔터프라이즈 벤더(Salesforce 7x, ServiceNow 17x)보다 훨씬 높은 매출 배수를 받고 있다. 이는 시장이 **AI 네이티브 성장 잠재력**에 프리미엄을 부여하고 있음을 의미한다.

---

## Key Findings

### 1. "LLM 인프라"에서 "에이전트 애플리케이션"으로 자본 이동

2023-2024년 AI 투자는 LLM 인프라(OpenAI, Anthropic)에 집중되었으나, 2025년부터 에이전트 애플리케이션 레이어로 자본이 이동하고 있다. [^11] [^12] Glean은 LLM을 직접 개발하지 않으면서도 Enterprise Graph와 검색 기술로 $7.2B 밸류에이션을 달성했고, Manus는 자체 LLM 없이 멀티모델 오케스트레이션으로 출시 8개월 만에 ARR $100M을 돌파했다. 이는 **LLM을 자체 보유하지 않아도 애플리케이션 레이어에서 대규모 가치를 창출할 수 있다**는 강력한 증거이다.

### 2. Anthropic의 Claude Code 매출 폭발이 시사하는 "개발자 채택 = 밸류에이션" 공식

Anthropic의 Claude Code 매출이 2025년 7월 기준 전년 대비 5.5배 성장한 사실은, 개발자 시장에서의 채택이 밸류에이션에 직접적으로 반영됨을 보여준다. [^2] Anthropic의 밸류에이션이 $18B(2024-03)에서 $60B(2025-01)로 1년 만에 3.3배 증가한 것은 Claude Code와 MCP 생태계의 확산이 주요 동인이었다. 유사하게 Vercel도 v0의 개발자 채택을 기반으로 $3.5B 밸류에이션을 확보했다. [^13] 이는 **개발자 채널 확보가 밸류에이션에 매우 유리**함을 의미한다.

### 3. 엔터프라이즈 AI 에이전트 매출의 "번들 vs 독립" 딜레마

상장 엔터프라이즈 벤더들은 AI 에이전트 매출을 기존 제품에 번들링하는 전략과 독립 과금하는 전략 사이에서 고심하고 있다. [^4] [^5] [^8] Salesforce의 대화당 $2 과금은 기존 시트 라이선스와 완전히 분리된 독립 과금이며, Microsoft의 $30/사용자/월 번들은 기존 M365 라이선스에 추가하는 방식이다. SAP는 RISE with SAP 번들에 기본 포함시키되 추가 사용은 AI Unit으로 과금하는 하이브리드를 채택했다. 투자자 관점에서는 **독립 과금이 AI 매출의 성장성을 더 명확히 보여줘** 밸류에이션에 유리하다.

### 4. Workday의 Sana Labs 인수($1.1B)가 보여주는 "AI 역량 인수" 트렌드

Workday가 2025년 9월 Sana Labs를 $1.1B에 인수한 것은, 대형 엔터프라이즈 벤더가 유기적 AI 개발보다 **인수를 통한 역량 확보**를 선호하는 트렌드를 보여준다. [^7] [^12] Meta의 Manus AI $2B 인수도 동일한 맥락이다. 이는 두 가지를 시사한다: (1) AI 에이전트 스타트업의 exit 경로로 M&A가 유효하며, (2) 대형 벤더가 자체 AI 개발의 속도 한계를 인정하고 있다.

### 5. 한국 기업의 "숨은 AI 투자"와 글로벌 격차

삼성SDS와 LG CNS는 독립적인 AI 밸류에이션을 받지 못하지만, 모기업 차원의 투자 규모는 상당하다. [^14] [^15] 삼성SDS는 SCP에 NVIDIA B300 GPU를 대규모 확보하고 OpenAI 공식 리셀러 지위를 확보했으며, LG CNS는 LG AI연구원 엑사원 투자와 코히어 기술 협력을 진행 중이다. 그러나 이러한 투자가 **독립적인 AI 플랫폼 밸류에이션**으로 전환되지 못하는 것은 대기업 계열사 구조의 한계이다. 한국 AI 에이전트 시장에서 독립적 밸류에이션을 받을 수 있는 스타트업에 대한 기회가 있으며, 더존비즈온(상장사)의 AI 전환 사례가 주목할 벤치마크이다. [출처 필요]

### 6. "ARR $100M 마일스톤"의 의미와 달성 속도 경쟁

AI 에이전트 시장에서 ARR $100M은 밸류에이션 inflection point로 인식된다. [^11] [^12] Glean은 2019년 설립 후 약 6년 만에, Manus AI는 출시 후 단 8개월 만에 이 마일스톤을 달성했다. Manus의 속도는 AI 에이전트 시장의 수요 폭발을 반영하지만, 지속 가능성은 검증이 필요하다(Meta 인수 후 매출 추적 불가).

---

## Recent Updates

<!-- auto-append: 새로운 투자·밸류에이션 뉴스를 아래 테이블에 추가 -->
| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-11 | [AI agents aren't eating SaaS — they're using it](https://fortune.com/2026/02/10/ai-agents-anthropic-openai-arent-killing-saas-salesforce-servicenow-microsoft-workday-cant-sleep-easy/) · [[2026/02/2026-02-11\|다이제스트]] | $2조 SaaS 시가총액 증발. Salesforce -26%, ServiceNow -28% YTD. AI 에이전트 좌석 기반 모델 구조적 위협 | #market |
| 2026-02-11 | [Harvey reportedly raising at $11B valuation](https://techcrunch.com/2026/02/09/harvey-reportedly-raising-at-11b-valuation-just-months-after-it-hit-8b/) · [[2026/02/2026-02-11\|다이제스트]] | Harvey AI $200M 투자 $11B 밸류에이션. Sequoia/GIC 주도, ARR $190M, 14개월 내 4차 | #market |
| 2026-02-10 | [Anthropic closes in on $20B round](https://techcrunch.com/2026/02/09/anthropic-closes-in-on-20b-round/) | Anthropic $20B 신규 라운드 마무리 임박. Nvidia·Microsoft 등 전략적 파트너 참여, Pre-IPO 메가라운드 | #market |
| 2026-02-12 | [Modal Labs $2.5B 밸류에이션 협상](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/) · [[2026/02/2026-02-12\|다이제스트]] | AI 인퍼런스 인프라 Modal Labs, General Catalyst 주도 $2.5B 밸류에이션. 5개월 전 $1.1B에서 2배 이상 급등. ARR ~$50M | #market |
| 2026-02-12 | [Nebius, Tavily $275M 인수](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform) · [[2026/02/2026-02-12\|다이제스트]] | 클라우드 인프라 Nebius가 에이전틱 검색 Tavily를 $275M에 인수. Fortune 500 고객, 월 300만+ SDK 다운로드. 인퍼런스+실시간 검색 통합 플랫폼 | #market |

---

## References

### Vault

[^1]: [[openai/openai|OpenAI]] -- GPT-5.2, ARR $12.7B+, $157B 밸류에이션
[^2]: [[claude/claude|Claude (Anthropic)]] -- Claude Code 5.5x 매출 성장, $60B 밸류에이션
[^3]: [[google-gemini/google-gemini|Google Gemini]] -- Alphabet $2.1T 시총, Gemini 3 Pro
[^4]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- $260B 시총, $2/대화 과금
[^5]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] -- $3.1T 시총, $30/사용자/월
[^6]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- $200B 시총, Assist 토큰 과금
[^7]: [[workday-assistant/workday-assistant|Workday Assistant]] -- $70B 시총, Sana Labs $1.1B 인수
[^8]: [[sap-joule/sap-joule|SAP Joule]] -- $290B 시총, AI Unit 과금
[^9]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- $55B 시총, 크레딧 기반 과금
[^10]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- $62B 밸류에이션, ARR $2.4B+
[^11]: [[glean/glean|Glean]] -- $7.2B 밸류에이션, ARR $100M+
[^12]: [[manus-ai/manus-ai|Manus AI]] -- Meta $2B 인수, ARR $100M 런레이트
[^13]: [[vercel-v0/vercel-v0|Vercel v0]] -- $3.5B 밸류에이션
[^14]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- ~15조 원 시총
[^15]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 비상장 (LG 계열)

### External

[^16]: [CNBC: Glean $7.2B 기업가치 도달](https://www.cnbc.com/2025/06/10/glean-gen-ai-search-startup-raises-150-million-at-7-billion-value.html)
[^17]: [TechCrunch: Meta acquires Manus AI](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)
[^18]: [Workday Newsroom: Sana Labs 인수 완료](https://newsroom.workday.com/2025-11-04-Workday-Completes-Acquisition-of-Sana)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
