---
type: insight-synthesis
topic_id: competitive-landscape-executive-summary
topic_name: 경쟁 환경 Executive Summary
category: strategy
tags:
- insight
- strategy
- executive-briefing
- competitive-analysis
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
- pm_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - enterprise AI agent competitive landscape
  - MCP protocol adoption enterprise
  - agentic AI market segmentation
  - Korea enterprise AI agent market
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 경쟁 환경 Executive Summary

## TL;DR

- **19개 경쟁 제품을 5개 세그먼트로 분류**: AI-Native 플랫폼(OpenAI, Anthropic, Google), Enterprise SaaS(Salesforce, SAP, Microsoft, ServiceNow, Workday, Oracle), Data Platform(Snowflake, Databricks, ThoughtSpot), Enterprise Search(Glean), Developer/Agent Tools(Vercel v0, Manus AI), Korea Market(삼성SDS, LG CNS, 더존, 영림원) -- 각 세그먼트별로 경쟁 강도와 위협 수준이 상이하다.
- **MCP 프로토콜이 사실상 업계 표준으로 확립**: Anthropic이 창안한 MCP를 OpenAI(2025.03), Google(2025.04), Salesforce(3.0), Microsoft(Copilot Studio), Snowflake, Glean 등 주요 플레이어가 채택.[^1] [^2] [^3] A2A(Google 주도)는 보조 프로토콜로 자리잡는 중이며, 프로토콜 전쟁은 MCP 승리로 수렴 중이다.
- **에이전틱 AI(Agentic AI)가 2025~2026년 모든 세그먼트의 핵심 경쟁축**: 단순 Copilot/Assistant에서 자율 에이전트로의 전환이 업계 전반에서 동시에 진행 중이며, 멀티 에이전트 오케스트레이션이 차세대 경쟁 우위가 되고 있다.
- **한국 시장은 글로벌 대비 1~2년 격차**: 삼성SDS와 LG CNS가 MCP/A2A를 조기 채택했으나, 실제 한국 중소기업 ERP 데이터를 보유한 더존/영림원은 프로토콜 표준화가 미비하여 구조적 비효율이 존재한다.[^4] [^5] [^6]

---

## Overview

2026년 2월 현재, 엔터프라이즈 AI 에이전트 시장은 역사상 가장 치열한 경쟁 국면에 진입했다.[^1] [^2] [^3] 2022년 ChatGPT 출시로 촉발된 생성형 AI 열풍이 2024~2025년을 거치면서 "대화형 AI"에서 "에이전틱 AI"로 패러다임이 전환되었고, 모든 주요 벤더가 자율 에이전트 전략을 공개하고 실행에 옮기고 있다. Salesforce Agentforce 3.0, Microsoft의 멀티 에이전트 오케스트레이션, SAP Joule의 Collaborative Agents, ServiceNow의 AI Agent Orchestrator 등 엔터프라이즈 벤더들의 에이전트 전략은 2025년 하반기를 기점으로 GA 단계에 진입하기 시작했다.[^7] [^8] [^9] [^10]

세부 분석은 [[product-roadmap-comparison|경쟁사 제품 로드맵 비교 분석]]과 [[feature-gap-analysis|기능 격차 분석 & 우선순위 제안]]에서 다룬다.

---

## Cross-Product Analysis

### 세그먼트별 경쟁 매트릭스

| 세그먼트 | 제품 | 핵심 전략 | MCP 지원 | 에이전트 자율성 | 한국 시장 영향 | 위협 수준 | Source |
|---------|------|----------|---------|-------------|------------|---------|--------|
| **AI-Native** | [[openai/openai\|OpenAI]] | B2C 시장 지배 + API 에코시스템 | O (채택) | 높음 (CUA, Codex) | 간접 (API 의존) | ★★★★☆ | [^1] |
| | [[claude/claude\|Anthropic Claude]] | 안전성 + MCP 표준 + 코딩 특화 | O (창안) | 높음 (Code, Cowork, Chrome) | 간접 (API/프로토콜) | ★★★★☆ | [^2] |
| | [[google-gemini/google-gemini\|Google Gemini]] | 멀티모달 + Workspace 통합 | O (채택) | 높음 (Mariner, Jules) | 중간 (Workspace 보급) | ★★★☆☆ | [^3] |
| **Enterprise SaaS** | [[salesforce-agentforce/salesforce-agentforce\|Salesforce Agentforce]] | CRM 네이티브 에이전트 + Atlas Engine | O (3.0) | 높음 (Atlas 추론) | 중간 (CRM 시장) | ★★★★☆ | [^7] |
| | [[microsoft-copilot/microsoft-copilot\|Microsoft Copilot]] | M365 에코시스템 + 번들 가격 | O (네이티브) | 높음 (멀티 에이전트) | 높음 (D365/M365 보급) | ★★★★★ | [^8] |
| | [[sap-joule/sap-joule\|SAP Joule]] | ERP 네이티브 + 2,400+ 스킬 | X (A2A 채택) | 중간 (Collaborative) | 높음 (대기업 ERP) | ★★★★☆ | [^9] |
| | [[servicenow-now-assist/servicenow-now-assist\|ServiceNow Now Assist]] | ITSM 도메인 독점 + 3계층 아키텍처 | X | 높음 (Orchestrator) | 중간 (ITSM 도메인) | ★★★☆☆ | [^10] |
| | [[workday-assistant/workday-assistant\|Workday Assistant]] | ASOR + HR/Finance 특화 | O (네이티브) | 중간 (Illuminate) | 낮음 (한국 보급 제한) | ★★☆☆☆ | [^11] |
| | [[oracle-digital-assistant/oracle-digital-assistant\|Oracle Digital Assistant]] | Skills 기반 모듈형 + 멀티채널 | X | 중간 (Multi-Agent) | 중간 (Oracle ERP 고객) | ★★★☆☆ | [^12] |
| **Data Platform** | [[snowflake-intelligence/snowflake-intelligence\|Snowflake Intelligence]] | NL-to-SQL + Managed MCP Server | O (서버) | 중간 (Cortex Agent) | 낮음 | ★★☆☆☆ | [^13] |
| | [[databricks-mosaic-ai/databricks-mosaic-ai\|Databricks Mosaic AI]] | 에이전트 프레임워크 + MLOps | X | 높음 (Framework) | 낮음 | ★★☆☆☆ | [^14] |
| | [[thoughtspot-spotter/thoughtspot-spotter\|ThoughtSpot Spotter]] | 에이전틱 분석 + 4 에이전트 팀 | O (서버) | 높음 (자기 검증) | 낮음 | ★☆☆☆☆ | [^15] |
| **Enterprise Search** | [[glean/glean\|Glean]] | Enterprise Graph + 벤더 중립 검색 | O (호스팅) | 높음 (Agentic Engine 2) | 낮음 | ★★☆☆☆ | [^16] |
| **Developer/Agent** | [[vercel-v0/vercel-v0\|Vercel v0]] | AI UI/풀스택 빌더 + 배포 통합 | X | 중간 (자율 터미널) | 낮음 | ★☆☆☆☆ | [^17] |
| | [[manus-ai/manus-ai\|Manus AI]] | 범용 자율 에이전트 + Glass Box | X | 매우 높음 (14일 비동기) | 낮음 | ★★☆☆☆ | [^18] |
| **Korea Market** | [[samsung-sds-fabrix/samsung-sds-fabrix\|삼성SDS FabriX]] | AI 풀스택 + OpenAI 리셀러 | O | 중간 | 높음 (대기업/공공) | ★★★★☆ | [^4] |
| | [[lgcns-agenticworks/lgcns-agenticworks\|LG CNS AgenticWorks]] | 6종 모듈 풀스택 + 코히어 협력 | O | 중간 | 높음 (대기업) | ★★★★☆ | [^6] |
| | [[douzone-one-ai/douzone-one-ai\|더존 ONE AI]] | ERP 네이티브 + 에이전트 마켓플레이스 | 미공개 | 중간 | 매우 높음 (중소기업) | ★★★★★ | [^5] |
| | [[younglimwon-ksystem/younglimwon-ksystem\|영림원 K-System]] | 제조 특화 + ERP+MES 통합 | 미공개 | 낮음 (가이드봇) | 중간 (제조 중견) | ★★☆☆☆ | [^19] |

### 패턴 분류

#### 패턴 1: "에코시스템 락인형" (Ecosystem Lock-in)

**설명**: 자사 에코시스템(CRM, ERP, 생산성 도구) 안에서 AI 에이전트 가치를 극대화하는 전략. 에코시스템 내 데이터 접근 깊이가 핵심 moat이며, 기존 고객 기반 위에 AI를 자연스럽게 침투시킨다.[^7] [^8] [^9]

**해당 제품**: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]], [[microsoft-copilot/microsoft-copilot|Microsoft Copilot]], [[sap-joule/sap-joule|SAP Joule]], [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]], [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]], [[douzone-one-ai/douzone-one-ai|더존 ONE AI]]

이 패턴에서는 기존 고객 기반이 최대 자산이다.

#### 패턴 2: "프로토콜 표준 주도형" (Protocol Standard Leadership)

**설명**: 개방형 프로토콜(MCP, A2A)을 창안하거나 조기 채택하여 에이전트 생태계의 표준 인프라 위치를 선점하는 전략. 프로토콜 중심성이 플랫폼 가치로 전환된다.[^2] [^3]

**해당 제품**: [[claude/claude|Anthropic Claude]] (MCP 창안), [[google-gemini/google-gemini|Google Gemini]] (A2A/A2UI 주도), [[workday-assistant/workday-assistant|Workday Assistant]] (MCP+A2A 네이티브), [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]], [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]]

MCP 생태계 참여는 에이전트 제품의 필수 요건으로 자리잡고 있다.

#### 패턴 3: "데이터 네이티브형" (Data-Native Intelligence)

**설명**: 데이터 플랫폼/웨어하우스 위에 AI 분석 에이전트를 네이티브로 구축하여, 데이터 거버넌스와 AI를 통합하는 전략.[^13] [^14] [^15]

**해당 제품**: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]], [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]], [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]]

NL-to-SQL, Semantic Layer, 데이터 거버넌스 등 이 세그먼트의 기술 패턴은 ERP 데이터 분석에 직접 응용 가능하다. 특히 Snowflake의 Semantic View와 ThoughtSpot의 SpotterModel 접근법은 참조할 가치가 높다.

#### 패턴 4: "범용 자율 에이전트형" (General-Purpose Autonomous Agent)

**설명**: 특정 에코시스템에 종속되지 않고, 브라우저 자동화/코드 실행 등을 통해 범용적 업무를 자율 수행하는 전략.[^1] [^2] [^18]

**해당 제품**: [[manus-ai/manus-ai|Manus AI]], [[openai/openai|OpenAI ChatGPT Agent/Codex]], [[claude/claude|Claude Code/Cowork]]

이 패턴의 UX 혁신(Manus의 Glass Box, Claude의 Agentic Loop)은 에이전트 인터페이스 설계의 핵심 참조점이다.

---

## Key Findings

1. **가격 모델의 근본적 전환: 시트 기반에서 소비 기반으로**: 전통적 시트당 월 과금 모델이 소비 기반(Salesforce $2/대화, SAP AI Units, ServiceNow Assist 토큰, Workday Flex Credits, Snowflake 크레딧)으로 급속히 전환되고 있다.[^7] [^9] [^11] 이는 AI 에이전트의 사용량 예측 불확실성을 반영한다. Microsoft의 $30/사용자/월 번들 전략만이 전통적 모델을 유지하며 가격 경쟁력으로 차별화하고 있다.[^8]

2. **"에이전트 관리" 자체가 새로운 제품 카테고리로 부상**: Workday의 ASOR(Agent System of Record)은 AI 에이전트를 인간 직원처럼 채용-온보딩-역할배정-성과관리하는 패러다임을 제시했고, ServiceNow의 AI Agent Orchestrator는 멀티 에이전트 팀의 거버넌스(토큰 예산, 역할 기반 접근 제어, 감사 로깅)를 중앙 관리한다.[^11] [^10] 이는 에이전트 수가 증가함에 따라 "에이전트 거버넌스 플랫폼"이 독립적 가치를 가진다는 신호이다.

3. **한국 시장의 구조적 비대칭: MCP 지원자 =/= 데이터 보유자**: 삼성SDS와 LG CNS가 MCP/A2A를 지원하지만 자체 ERP를 보유하지 않고, 실제 한국 중소기업 ERP 데이터를 보유한 더존과 영림원은 MCP를 미지원한다.[^4] [^5] [^6] 이 "프로토콜-데이터 분리"는 한국 에이전트 생태계의 구조적 비효율이며, 이 간극을 메우는 미들웨어/브릿지 솔루션은 높은 전략적 가치를 가진다.

4. **노코드 에이전트 빌더가 Table Stakes로 확립**: Salesforce Agent Builder, Microsoft Copilot Studio, SAP Joule Studio, ServiceNow AI Agent Studio, LG CNS Studio, 더존 AI Flow, Glean 에이전트 빌더 등 거의 모든 엔터프라이즈 제품이 노코드/로코드 에이전트 빌더를 제공한다.[^7] [^6] [^5] 이는 더 이상 차별화 요소가 아닌 기본 요건(Table Stakes)이다.

5. **멀티 에이전트 오케스트레이션이 차세대 경쟁축**: Microsoft의 멀티 에이전트 오케스트레이션(2025.05 GA), ServiceNow의 AI Agent Orchestrator, SAP의 Collaborative Agents, Manus의 Planner Agent, ThoughtSpot의 4 에이전트 팀 등 단일 에이전트를 넘어 에이전트 간 협업/위임/조율이 핵심 경쟁 영역으로 부상했다.[^8] [^10] [^18]

6. **더존 ONE AI의 에이전트 마켓플레이스가 한국 시장의 게임 체인저**: 19개 제품 중 에이전트 마켓플레이스를 운영하는 것은 더존 ONE AI, OpenAI(GPT Store), Workday(Marketplace) 뿐이며, 한국 시장에서는 더존이 유일하다.[^5] [^1] 5,800+ 기업 고객 기반 위에 서드파티 에이전트 생태계를 구축하는 전략은 한국 중소기업 시장 접근의 핵심 통로가 될 수 있다. [출처 필요]

---

## Recent Updates

<!-- auto-append: 새로운 업데이트는 이 테이블 하단에 자동 추가됩니다 -->

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| | | | |

---

## References

### Vault

[^1]: [[openai/openai|OpenAI]] -- B2C AI 시장 지배자, GPT-5.2/o3/Codex 에이전트
[^2]: [[claude/claude|Anthropic Claude]] -- MCP 창안자, 코딩 벤치마크 최상위, 풀스택 에이전트
[^3]: [[google-gemini/google-gemini|Google Gemini]] -- 멀티모달 네이티브, 1M 컨텍스트, A2A/A2UI 주도
[^4]: [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] -- AI 풀스택, MCP/A2A, 20만 사용자
[^5]: [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] -- ERP 네이티브, 에이전트 마켓플레이스, 5,800+ 기업
[^6]: [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] -- 6종 모듈, 코히어 협력, SecureXper AI
[^7]: [[salesforce-agentforce/salesforce-agentforce|Salesforce Agentforce]] -- CRM 네이티브 에이전트, Atlas Engine, $2/대화
[^8]: [[microsoft-copilot/microsoft-copilot|Microsoft Copilot for Dynamics 365]] -- M365 통합, 멀티 에이전트 오케스트레이션
[^9]: [[sap-joule/sap-joule|SAP Joule]] -- ERP 네이티브 2,400+ 스킬, Collaborative Agents
[^10]: [[servicenow-now-assist/servicenow-now-assist|ServiceNow Now Assist]] -- ITSM 도메인 리더, 3계층 AI 아키텍처
[^11]: [[workday-assistant/workday-assistant|Workday Assistant]] -- ASOR 혁신, MCP+A2A 네이티브, HR/Finance 특화
[^12]: [[oracle-digital-assistant/oracle-digital-assistant|Oracle Digital Assistant]] -- Skills 기반 모듈형, 35+ 사전 구축 Skills
[^13]: [[snowflake-intelligence/snowflake-intelligence|Snowflake Intelligence]] -- NL-to-SQL, Managed MCP Server, 데이터 거버넌스
[^14]: [[databricks-mosaic-ai/databricks-mosaic-ai|Databricks Mosaic AI]] -- 에이전트 프레임워크, Agent Evaluation, Unity Catalog
[^15]: [[thoughtspot-spotter/thoughtspot-spotter|ThoughtSpot Spotter]] -- 4 에이전트 팀, 자기 검증 루프, Drill-Anywhere
[^16]: [[glean/glean|Glean]] -- Enterprise Graph, 벤더 중립 검색, $7.2B 기업가치
[^17]: [[vercel-v0/vercel-v0|Vercel v0]] -- AI UI/풀스택 빌더, 복합 모델 아키텍처
[^18]: [[manus-ai/manus-ai|Manus AI]] -- 범용 자율 에이전트, Glass Box, Meta 인수($2B)
[^19]: [[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]] -- 제조 특화, ERP+MES 통합, AI 경영분석

### External

[^20]: [MCP Official Site](https://modelcontextprotocol.io/) -- Model Context Protocol 공식 스펙 및 서버 레지스트리
[^21]: [Google A2A Protocol](https://developers.googleblog.com/) -- Agent-to-Agent 프로토콜 공식 문서
[^22]: [Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/) -- MCP 거버넌스 주체

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
