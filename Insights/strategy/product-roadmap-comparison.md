---
type: insight-synthesis
topic_id: product-roadmap-comparison
topic_name: 경쟁사 제품 로드맵 비교 분석
category: strategy
tags:
- insight
- strategy
- roadmap
- product-planning
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- openai
- claude
- google-gemini
- salesforce-agentforce
- microsoft-copilot
- sap-joule
- servicenow-now-assist
- workday-assistant
- oracle-digital-assistant
- snowflake-intelligence
- databricks-mosaic-ai
- thoughtspot-spotter
- glean
- vercel-v0
- manus-ai
- samsung-sds-fabrix
- lgcns-agenticworks
- douzone-one-ai
- younglimwon-ksystem
source_files:
- AI Agent Products/openai/openai.md
- AI Agent Products/claude/claude.md
- AI Agent Products/google-gemini/google-gemini.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/microsoft-copilot/microsoft-copilot.md
- AI Agent Products/sap-joule/sap-joule.md
- AI Agent Products/servicenow-now-assist/servicenow-now-assist.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/oracle-digital-assistant/oracle-digital-assistant.md
- AI Agent Products/snowflake-intelligence/snowflake-intelligence.md
- AI Agent Products/databricks-mosaic-ai/databricks-mosaic-ai.md
- AI Agent Products/thoughtspot-spotter/thoughtspot-spotter.md
- AI Agent Products/glean/glean.md
- AI Agent Products/vercel-v0/vercel-v0.md
- AI Agent Products/manus-ai/manus-ai.md
- AI Agent Products/samsung-sds-fabrix/samsung-sds-fabrix.md
- AI Agent Products/lgcns-agenticworks/lgcns-agenticworks.md
- AI Agent Products/douzone-one-ai/douzone-one-ai.md
- AI Agent Products/younglimwon-ksystem/younglimwon-ksystem.md
relevant_roles:
- planning_agent
- pm_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - AI agent product roadmap 2026
  - enterprise AI agent release timeline
  - MCP A2A protocol adoption timeline
  - Korea AI agent market timeline
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 경쟁사 제품 로드맵 비교 분석

## TL;DR

- **2024년은 "코파일럿 원년"**, 2025년은 **"에이전트 원년"**, 2026년은 **"멀티 에이전트 오케스트레이션 원년"**으로 진화 단계가 명확하다. 각 세그먼트별로 진입 시점은 다르지만, 방향은 동일하게 수렴하고 있다.
- **기술 수렴점 3가지**: (1) MCP 프로토콜 표준화, (2) 멀티 에이전트 협업 아키텍처, (3) 소비 기반 가격 모델. 이 세 가지는 2026년 말까지 모든 주요 제품에서 기본 요건이 될 전망이다.
- **전략 분기점 3가지**: (1) 자체 LLM 보유 여부, (2) 에이전트 마켓플레이스 개방 수준, (3) 도메인 특화 vs 범용 접근. 이 세 가지에서 경쟁사 간 전략이 선명하게 갈리고 있다.
- **한국 시장은 글로벌 대비 약 12~18개월 후행**: 글로벌에서 2024년 하반기에 시작된 에이전트 전환이 한국에서는 2025년 하반기~2026년 초에 본격화되고 있어, 빠른 팔로워(Fast Follower) 전략이 유효하다.[^4] [^5] [^6]
- **2026년 하반기 이후 주요 이벤트**: SAP Joule Studio GA(2026 Q1), ThoughtSpot 4 에이전트 GA(2026 초), Workday Agent Gateway 프로덕션 배포, OpenAI Assistants API 종료 등이 시장 동향에 영향을 미칠 전망이다.[^9] [^15] [^11] [^1]

---

## Overview

경쟁사 제품의 로드맵을 시간축으로 분석하면, 개별 제품의 출시 시점과 기능 진화 패턴에서 업계 전반의 기술 성숙도 곡선과 전략적 베팅의 방향을 읽을 수 있다.[^1] [^2] [^3] 이 문서는 19개 경쟁 제품의 공개된 출시 이력, 발표된 로드맵, 그리고 기술 트렌드를 기반으로 2024~2026년의 제품 진화를 추적한다.

중요한 전제: 이 분석은 공개된 정보에 기반하며, 비공개 로드맵이나 인수합병 계획은 포함되지 않는다. 다만 Manus AI의 Meta 인수($2B, 2025.12), Workday의 Sana Labs 인수($1.1B, 2025.09) 등 이미 공개된 인수는 반영한다.[^18] [^11]

---

## Cross-Product Analysis

### 타임라인 매트릭스: 2024~2026 주요 이정표

| 시기 | AI-Native | Enterprise SaaS | Data Platform | Korea Market | Source |
|------|-----------|----------------|---------------|-------------|--------|
| **2024 H1** | GPT-4o 출시(05) | 더존 ONE AI 첫 공개(04), 삼성SDS FabriX 출시(05) | Databricks Agent Framework 발표(06) | 더존/삼성SDS 선제 출시 | [^1] [^5] [^4] [^14] |
| **2024 H2** | Claude 3.5 Sonnet, MCP 공개(11) | Salesforce Agentforce 1.0(10), Vercel v0 GA(10) | Snowflake Cortex Analyst Preview | MCP 생태계 시동 | [^2] [^7] [^17] [^13] |
| **2025 H1** | OpenAI Operator(01), Claude Code(02), GPT-5(08) | Agentforce 2.0(02), Workday ASOR(02), MS Build 멀티에이전트(05) | Snowflake Intelligence Preview | 더존 에이전트 고도화 | [^1] [^2] [^7] [^11] [^8] |
| **2025 H2** | Claude 4(06), Claude 4.5(11), GPT-5.2(12) | Agentforce 3.0+MCP(06), SAP Joule 14개 신규 에이전트(10), Workday Agent Gateway(06), ServiceNow Agent Orchestrator(03) | Snowflake Intelligence GA(11), ThoughtSpot 4 에이전트(12) | LG CNS AgenticWorks(08), 삼성SDS CES 2026 전략(09) | [^2] [^1] [^7] [^9] [^11] [^10] [^13] [^15] [^6] [^4] |
| **2026 H1** | Claude Cowork(01), Codex GPT-5.3(예정) | SAP Joule Studio GA(Q1), Workday Agent Gateway 프로덕션 | ThoughtSpot 에이전트 GA(초) | 영림원 K-System I&I(2025-04, 이후 고도화 진행) | [^2] [^9] [^11] [^15] [^19] |
| **2026 H2** | OpenAI Assistants API 종료(예정) | M365 Copilot Tuning 확산 | Databricks MLflow 3.0 확산 | 한국 기업 에이전트 본격 도입 | [^1] [^8] [^14] |

### 패턴 분류

#### 패턴 A: "6개월 주기 메이저 릴리스" (Rapid Versioning)

**설명**: 6개월 간격으로 메이저 버전을 출시하며 경쟁 압력을 유지하는 패턴. AI-Native 플레이어와 일부 Enterprise SaaS가 이 패턴을 따른다.[^7] [^1] [^2]

**해당 제품**:
- [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]]: 1.0(2024.10) → 2.0(2025.02) → 3.0(2025.06) -- 정확히 4개월/4개월 주기[^7]
- [[openai/openai|OpenAI]]: GPT-4o(2024.05) → GPT-5(2025.08) → GPT-5.2(2025.12) -- 약 15개월/4개월 주기로 가속[^1]
- [[claude/claude|Anthropic Claude]]: Claude 3(2024.03) → Claude 4(2025.06) → Claude 4.5(2025.11) -- 15개월/5개월 주기[^2]

**시사점**: AI-Native 벤더들은 경쟁 압력으로 출시 주기가 지속 단축되고 있다. Salesforce는 엔터프라이즈 벤더 중 가장 빠른 릴리스 주기를 보이며, 이는 에이전트 시장의 경쟁 강도를 반영한다.

#### 패턴 B: "인수를 통한 가속" (Acquisition-Driven Acceleration)

**설명**: 핵심 역량 부족을 M&A로 빠르게 보완하는 패턴. 자체 개발 대비 시간을 단축하지만 통합 리스크가 존재한다.[^11] [^18]

**해당 제품**:
- [[workday-assistant/workday-assistant|Workday]]: Sana Labs 인수($1.1B, 2025.09) → AI 검색/학습/에이전트 역량 내재화[^11]
- [[manus-ai/manus-ai|Manus AI]]: Meta에 인수($2B, 2025.12) → Meta의 에이전트 전략 핵심 자산으로 편입[^18]
- Google: DeepMind 통합(기 완료) → Gemini 브랜드로 통합 → 에이전트 생태계 확장[^3]

**시사점**: 자체 LLM이나 도메인 전문성을 보유하지 않은 기업들이 M&A로 격차를 해소하는 패턴이 가속화되고 있다.

#### 패턴 C: "프로토콜 연합 형성" (Protocol Alliance Building)

**설명**: 개방형 프로토콜을 통해 에이전트 생태계의 네트워크 효과를 추구하는 패턴.[^2] [^1] [^3]

**주요 이벤트 타임라인**:
- 2024.11: Anthropic, MCP 오픈소스 공개[^2]
- 2025.03: OpenAI, MCP 채택 (Agents SDK, Responses API)[^1]
- 2025.04: Google, MCP 지원 + A2A 프로토콜 제안[^3]
- 2025.06: Salesforce Agentforce 3.0 MCP 내장, Workday Agent Gateway MCP+A2A[^7] [^11]
- 2025.10: Snowflake Managed MCP Server, ThoughtSpot MCP Server[^13] [^15]
- 2025.11: MCP 스펙 대규모 업데이트 (비동기, 무상태, 서버 아이덴티티)
- 2025.12: MCP를 Linux Foundation AAIF에 기증

**시사점**: MCP 채택은 2025년 한 해 동안 폭발적으로 확산되었고, AAIF 이관으로 중립적 거버넌스가 확보되었다. 2026년에는 MCP 미지원이 곧 생태계 배제를 의미하는 수준이 될 것으로 예상된다. 한편 A2A는 Google 주도로 에이전트 간 통신에 집중하며 MCP와 보완적 관계를 형성하고 있다.

#### 패턴 D: "한국 시장 후발 진입" (Korea Market Late Entry)

**설명**: 한국 시장의 에이전트 전환은 글로벌 대비 지연되었으나, 2025년 하반기부터 급속히 가속되는 패턴.[^5] [^4] [^6] [^19]

**타임라인**:
- 2024.04: 더존 ONE AI 첫 공개 (한국 시장 최초 ERP AI)[^5]
- 2024.05: 삼성SDS FabriX & Brity Copilot 출시[^4]
- 2025.04: 영림원 K-System Ace I&I 출시[^19]
- 2025.08: LG CNS AgenticWorks 공개 (후발이지만 MCP/A2A 지원)[^6]
- 2025.10: 더존 에이전트 마켓플레이스 공개[^5]
- 2025.11: LG CNS 마케팅 AI 에이전트 출시[^6]
- 2026.01: 삼성SDS CES 2026에서 에이전트 전략 선언[^4]

**시사점**: 더존과 삼성SDS가 2024년에 선제적으로 출시했으나, 에이전틱 AI(자율 에이전트) 전략은 2025년 하반기에 본격화되었다. LG CNS는 후발이지만 MCP/A2A 프로토콜 지원과 코히어 협력으로 기술적 차별화를 시도하고 있다.

---

## Key Findings

1. **"Copilot → Agent → Orchestrator" 3단계 진화가 보편적**: 거의 모든 엔터프라이즈 제품이 (1단계) 대화형 어시스턴트/코파일럿 → (2단계) 자율 에이전트 → (3단계) 멀티 에이전트 오케스트레이션의 동일한 진화 경로를 따르고 있다.[^7] [^8] [^10] Salesforce는 이미 3단계(Agentforce 3.0 + Command Center), Microsoft도 3단계(멀티 에이전트 오케스트레이션 GA), ServiceNow도 3단계(AI Agent Orchestrator)에 도달했다. 반면 SAP Joule(2~3단계 전환 중), 더존 ONE AI(2단계), 영림원(1~2단계)은 아직 진화 중이다.[^9] [^5] [^19]

2. **AI-Native 벤더의 에이전트 스펙트럼 확장이 엔터프라이즈 시장을 위협**: OpenAI(ChatGPT Agent + Codex), Anthropic(Claude Code + Cowork + Chrome), Google(Project Mariner + Jules)이 B2C 기반에서 에이전트 풀스택을 구축하며 엔터프라이즈 영역으로 확장하고 있다.[^2] [^1] [^3] 특히 Claude Code의 매출 5.5배 성장(2025.07 기준)은 개발자 시장에서의 침투력을 보여주며, Claude Cowork(2026.01)은 비개발자 업무 자동화 시장으로의 확장을 시사한다.[^2]

3. **"에이전트 빌더" 플랫폼의 표준화 경쟁이 격화**: Salesforce Agent Builder(노코드, 3-Panel), Microsoft Copilot Studio(로코드, Agent Builder → Studio 이관), SAP Joule Studio(2026 Q1 GA), ServiceNow AI Agent Studio(자연어 기반), LG CNS Studio(노코드), 더존 AI Flow(노코드), Workday Build + Flowise(비주얼), Glean Agent Builder(노코드+API), Databricks AI Playground(코드 기반) 등 각사가 에이전트 빌더를 핵심 플랫폼 전략으로 밀고 있다.[^7] [^9] [^10] 빌더의 UI/UX 패턴도 수렴하고 있으나, "자연어 기반 정의"(ServiceNow, Glean) vs "비주얼 캔버스"(Salesforce, Oracle) vs "코드 기반"(Databricks, LG CNS Builder) 세 갈래가 공존한다.

4. **보안/거버넌스 접근법이 3가지 모델로 분화**:
   - **인프라 레벨 보안**: 삼성SDS(SCP 기반), 더존(프라이빗 AI PE/폐쇄망), Databricks(Lakeguard 샌드박스)[^4] [^5] [^14]
   - **에이전트-시스템 연결점 보안**: LG CNS(SecureXper AI), Workday(ASOR 권한 관리), Snowflake(RBAC+MCP 권한)[^6] [^11] [^13]
   - **플랫폼 거버넌스 보안**: ServiceNow(Orchestrator 정책 엔진), Salesforce(Agentforce Gateway ABAC), Glean(원본 권한 상속)[^10] [^7] [^16]
   이 중 에이전틱 AI 시대에 가장 구조적으로 적합한 것은 "에이전트-시스템 연결점 보안"과 "플랫폼 거버넌스 보안"의 결합이다.

5. **음성 에이전트가 차세대 인터페이스로 부상**: OpenAI의 gpt-realtime(Speech-to-Speech), ServiceNow의 AI Voice Agents(2025), 삼성SDS의 보이스 에이전트, LG CNS의 데일리 브리핑(음성) 등 음성 기반 에이전트 인터페이스가 확산되고 있다.[^1] [^10] [^4] 특히 ERP 환경에서 외근/현장 직원의 음성 명령 업무 처리는 제조업 시장에서 차별화 요소가 될 수 있다.

6. **Semantic Layer/Model이 데이터 에이전트의 핵심 인프라로 확립**: Snowflake의 Semantic View(YAML 기반 수동 정의), ThoughtSpot의 SpotterModel(AI 자동 생성), SAP의 Knowledge Graph, Databricks의 Unity Catalog 등 데이터와 AI 사이의 의미론적 계층(Semantic Layer)이 데이터 에이전트의 정확도를 결정하는 핵심 인프라로 확립되었다.[^13] [^15] [^9]

---

## Recent Updates

<!-- auto-append: 새로운 업데이트는 이 테이블 하단에 자동 추가됩니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| | | | |

---

## References

### Vault

[^1]: [[openai/openai|OpenAI]] -- GPT-5.2, ChatGPT Agent, Codex, Responses API 타임라인
[^2]: [[claude/claude|Anthropic Claude]] -- MCP 공개(2024.11), Claude Code(2025.02), Cowork(2026.01)
[^3]: [[google-gemini/google-gemini|Google Gemini]] -- Gemini 2.0(2024.12), A2A/A2UI, Project Mariner
[^4]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- 출시(2024.05), CES 2026 전략, MCP/A2A 적용
[^5]: [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] -- 첫 공개(2024.04), 마켓플레이스(2025.10), 5,800+ 기업
[^6]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 6종 모듈 공개(2025.08), 코히어 협력
[^7]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- 1.0→2.0→3.0 진화, MCP 내장, Command Center
[^8]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]] -- 멀티 에이전트 오케스트레이션(2025.05), MCP 네이티브
[^9]: [[sap-joule/sap-joule|SAP Joule]] -- 2,400+ 스킬, 14개 신규 에이전트, Joule Studio GA(2026 Q1)
[^10]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- AI Agent Orchestrator(2025.03), 3계층 아키텍처
[^11]: [[workday-assistant/workday-assistant|Workday Assistant]] -- ASOR(2025.02), Agent Gateway(2025.06), Sana 인수(2025.09)
[^12]: [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] -- Multi-Agent(2024+), LLM 블록 통합
[^13]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- GA(2025.11), Managed MCP Server
[^14]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- Agent Framework(2024.06), MLflow 3.0
[^15]: [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] -- 4 에이전트 발표(2025.12), 자기 검증 루프
[^16]: [[glean/glean|Glean]] -- 3세대 어시스턴트(2025.09), Agentic Engine 2, MCP 호스팅
[^17]: [[vercel-v0/vercel-v0|Vercel v0]] -- 복합 모델 아키텍처, 풀스택 빌더 진화
[^18]: [[manus-ai/manus-ai|Manus AI]] -- 출시(2025.03), ARR $1억(2025.11), Meta 인수(2025.12)
[^19]: [[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System I&I]] -- 출시(2025.04), ERP+MES+AI 통합

### External

[^20]: [MCP Spec Update (2025.11)](https://modelcontextprotocol.io/) -- 비동기, 무상태, 서버 아이덴티티
[^21]: [Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/) -- MCP 거버넌스 이관
[^22]: [Microsoft Build 2025 Announcements](https://www.microsoft.com/en-us/microsoft-365/blog/) -- 멀티 에이전트 오케스트레이션
[^23]: [SAP Connect 2025](https://news.sap.com/) -- 14개 신규 Joule Agent
[^24]: [Workday Rising 2025](https://newsroom.workday.com/) -- Agent Gateway, Sana 인수

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
