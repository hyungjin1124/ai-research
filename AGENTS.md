# Agent 역할별 라우팅 가이드

> **이 파일은 특정 역할을 가진 AI 에이전트가 이 리서치 볼트에서 자기에게 필요한 문서를 빠르게 찾기 위한 라우팅 허브입니다.**
> 역할이 명확하면 아래에서 자신의 role을 찾아 `primary_sources`부터 읽으세요.
> 역할이 불명확하거나 범용 질문이면 `_CONTEXT.md`를 대신 읽으세요.

---

## 사용법

1. 자신의 **역할(role)**을 아래 8개 중 식별
2. 해당 역할의 `primary_sources` 목록에서 관련 문서 탐색
3. 문서의 TL;DR로 관련성을 빠르게 확인한 뒤, 본문 전체를 읽고 현재 맥락에 맞게 판단
4. 더 깊은 맥락이 필요하면 `secondary_sources` 참조
5. 제품별 상세가 필요하면 `AI Agent Products/{slug}/{slug}.md`로 이동

---

## 역할 정의

### frontend_agent
- **설명**: UI 컴포넌트 설계, 인터랙션 패턴, 디자인 시스템, 시각화 관련 의사결정을 담당하는 에이전트
- **primary_sources**:
  - `Insights/agent-ui/hitl-approval-patterns.md` — HITL 승인 UI 패턴 5종 비교, Risk-Based Rendering
  - `Insights/agent-ui/conversational-ui-patterns.md` — 대화형 UI 구조 (채팅, 사이드패널, 임베디드)
  - `Insights/agent-ui/artifacts-canvas-patterns.md` — Artifacts/Canvas 레이아웃 4종, 트리거 전략
  - `Insights/agent-ui/agent-reasoning-visualization.md` — 추론 과정 시각화 (Extended Thinking, Glass Box 등)
  - `Insights/agent-ui/dashboard-composition.md` — 멀티 에이전트 대시보드 레이아웃
  - `Insights/agent-ui/data-visualization-drilldown.md` — 데이터 시각화 드릴다운 패턴
- **secondary_sources**:
  - `Insights/protocols/protocol-comparison-mcp-a2a-a2ui.md` — A2UI/MCP-UI가 프론트엔드에 미치는 영향
  - `AI Agent Products/*/` — 각 제품 프로필의 "UI/UX 분석" 섹션
---

### backend_agent
- **설명**: 에이전트 런타임, 도구 연결, 데이터 파이프라인, API 설계를 담당하는 에이전트
- **primary_sources**:
  - `Insights/agent-runtime/agent-orchestration-loops.md` — 에이전트 루프 패턴 (Plan-Act-Observe 등)
  - `Insights/agent-runtime/agent-memory-context.md` — 메모리 & 컨텍스트 관리 4패턴
  - `Insights/agent-runtime/agent-parallel-processing.md` — 병렬 처리 패턴, Fan-Out/Fan-In
  - `Insights/agent-runtime/agent-filesystem-usage.md` — 파일시스템 접근 패턴, 샌드박스
  - `Insights/agent-runtime/agent-planning-reasoning.md` — 플래닝 & 리즈닝 3세대 분류
  - `Insights/agent-skills/tool-calling-patterns.md` — Tool Calling 4패턴 (Schema-First vs Semantic-First)
  - `Insights/agent-skills/mcp-server-implementations.md` — MCP 서버 구현 3패턴
  - `Insights/knowledge-data/rag-architecture-comparison.md` — RAG 아키텍처 3패턴
  - `Insights/knowledge-data/data-connector-integration.md` — 데이터 커넥터 통합 5패턴
- **secondary_sources**:
  - `Insights/knowledge-data/embedding-retrieval-strategies.md` — 임베딩 & 검색 전략
  - `Insights/knowledge-data/knowledge-graph-approaches.md` — KG 활용 5패턴
  - `Insights/security-evaluation/agent-permission-models.md` — 권한 모델 비교
  - `Insights/open-source/oss-tools-libraries.md` — OSS 도구/라이브러리 분석
  - `Insights/open-source/agent-frameworks-landscape.md` — OSS 프레임워크 랜드스케이프
  - `Insights/strategy/build-vs-buy-decision-framework.md` — Build vs Buy 프레임워크 (기술 스택 계층별 Build/Buy 판단 참고)
---

### architecture_agent
- **설명**: 시스템 아키텍처, 프로토콜 선택, 기술 스택 결정, 보안 아키텍처를 담당하는 에이전트
- **primary_sources**:
  - `Insights/protocols/protocol-comparison-mcp-a2a-a2ui.md` — MCP vs A2A vs A2UI vs MCP-UI 비교
  - `Insights/protocols/protocol-adoption-guide.md` — 프로토콜 단계별 채택 로드맵
  - `Insights/agent-runtime/agent-orchestration-loops.md` — 오케스트레이션 루프 패턴
  - `Insights/agent-runtime/agent-planning-reasoning.md` — 플래닝 & 리즈닝 전략
  - `Insights/agent-skills/mcp-server-implementations.md` — MCP 서버 구현 3패턴
  - `Insights/agent-skills/agent-skill-design.md` — Skill 설계 4패턴
  - `Insights/knowledge-data/knowledge-graph-approaches.md` — KG 활용 패턴
  - `Insights/security-evaluation/agent-permission-models.md` — 권한 모델 비교
  - `Insights/security-evaluation/agent-guardrails-safety.md` — 가드레일 & 안전성
  - `Insights/strategy/build-vs-buy-decision-framework.md` — Build vs Buy 프레임워크
- **secondary_sources**:
  - `Insights/agent-runtime/` — 전체 런타임 문서
  - `Insights/knowledge-data/` — 전체 지식/데이터 문서
  - `Insights/open-source/agent-frameworks-landscape.md` — OSS 프레임워크 선택지
  - `Insights/open-source/oss-models-for-agents.md` — OSS 모델 현황
  - `AI Agent Products/*/` — 각 제품 프로필의 "아키텍처" 섹션
---

### planning_agent
- **설명**: 제품 기획, 요구사항 정의, 사용자 시나리오 설계, 기능 스펙 작성을 담당하는 에이전트
- **primary_sources**:
  - `Insights/strategy/feature-gap-analysis.md` — 기능 격차 분석 & 우선순위 제안
  - `Insights/strategy/product-roadmap-comparison.md` — 경쟁사 로드맵 비교
  - `Insights/market/enterprise-vs-b2c-strategies.md` — Enterprise vs B2C 전략 분기점
  - `Insights/market/korea-erp-ai-landscape.md` — 한국 ERP AI 생태계
  - `Insights/agent-skills/agent-skill-design.md` — Skill 설계 패턴 (기획 관점)
  - `Insights/agent-skills/agent-marketplace-ecosystem.md` — 마켓플레이스 생태계
  - `Insights/agent-ui/hitl-approval-patterns.md` — HITL 승인 패턴 (UX 요구사항 도출용)
  - `Insights/agent-ui/conversational-ui-patterns.md` — 대화형 UI 패턴 (UX 요구사항 도출용)
- **secondary_sources**:
  - `Insights/agent-runtime/agent-planning-reasoning.md` — 에이전트 추론 패턴 (기능 스펙 참고)
  - `Insights/market/pricing-models-comparison.md` — 과금 모델 비교
  - `Insights/security-evaluation/agent-evaluation-benchmarks.md` — 평가 벤치마크
  - `AI Agent Products/*/` — 개별 제품 프로필 (경쟁사 기능 참고)
---

### pm_agent
- **설명**: 프로젝트 관리, 경쟁 분석, 경영진 보고, 시장 전략을 담당하는 에이전트
- **primary_sources**:
  - `Insights/strategy/competitive-landscape-executive-summary.md` — 경쟁 환경 Executive Summary
  - `Insights/strategy/feature-gap-analysis.md` — 기능 격차 분석
  - `Insights/strategy/go-to-market-patterns.md` — GTM 전략 패턴
  - `Insights/strategy/funding-valuation-tracker.md` — 투자·밸류에이션 추적
  - `Insights/market/competitive-positioning-matrix.md` — 경쟁 포지셔닝 매트릭스
  - `Insights/market/pricing-models-comparison.md` — 과금 모델 비교
  - `Insights/market/partnership-ecosystem-map.md` — 파트너십 생태계 맵
- **secondary_sources**:
  - `Insights/market/korea-erp-ai-landscape.md` — 한국 ERP AI 생태계
  - `Insights/market/enterprise-vs-b2c-strategies.md` — Enterprise vs B2C 전략
  - `Insights/strategy/product-roadmap-comparison.md` — 로드맵 비교
  - `Insights/strategy/build-vs-buy-decision-framework.md` — Build vs Buy 프레임워크
  - `AI Agent Products/*/` — 개별 제품 프로필 (경쟁사 분석)
---

### qa_agent
- **설명**: 품질 보증, 테스트 전략, 에이전트 평가, 안전성 검증을 담당하는 에이전트
- **primary_sources**:
  - `Insights/security-evaluation/agent-evaluation-benchmarks.md` — 에이전트 평가 벤치마크, 정확도/안전성 메트릭
  - `Insights/security-evaluation/agent-guardrails-safety.md` — 가드레일 & 안전성 패턴
  - `Insights/security-evaluation/agent-permission-models.md` — 권한 모델 비교 (테스트 시나리오 도출)
  - `Insights/agent-runtime/agent-planning-reasoning.md` — 추론 품질 평가 기준 참고
  - `Insights/agent-runtime/agent-orchestration-loops.md` — 에이전트 루프 테스트 포인트 도출
- **secondary_sources**:
  - `Insights/agent-runtime/agent-memory-context.md` — 메모리 누수/오염 테스트
  - `Insights/agent-skills/tool-calling-patterns.md` — Tool Calling 실패 시나리오
  - `AI Agent Products/*/` — 경쟁사 품질 기준 및 SLA 참고
---

### data_agent
- **설명**: 데이터 파이프라인, RAG 최적화, 임베딩 전략, Knowledge Graph 구축을 담당하는 에이전트
- **primary_sources**:
  - `Insights/knowledge-data/rag-architecture-comparison.md` — RAG 아키텍처 3패턴
  - `Insights/knowledge-data/embedding-retrieval-strategies.md` — 임베딩 & 검색 전략
  - `Insights/knowledge-data/knowledge-graph-approaches.md` — KG 활용 5패턴
  - `Insights/knowledge-data/data-connector-integration.md` — 데이터 커넥터 통합 5패턴
  - `Insights/agent-runtime/agent-memory-context.md` — 메모리 & 컨텍스트 관리 (데이터 관점)
- **secondary_sources**:
  - `Insights/open-source/oss-tools-libraries.md` — OSS 데이터 도구 분석
  - `Insights/open-source/oss-models-for-agents.md` — 임베딩/소형 모델 현황
  - `Insights/security-evaluation/agent-permission-models.md` — 데이터 접근 권한
  - `Insights/protocols/protocol-comparison-mcp-a2a-a2ui.md` — 데이터 연동 프로토콜
  - `AI Agent Products/snowflake-intelligence/snowflake-intelligence.md` — 시맨틱 레이어 참조
  - `AI Agent Products/databricks-mosaic-ai/databricks-mosaic-ai.md` — 데이터 레이크하우스 패턴
---

### sales_agent
- **설명**: 경쟁 PT 자료, 고객 제안서, 가치 제안, 차별화 포인트 도출을 담당하는 에이전트
- **primary_sources**:
  - `Insights/strategy/competitive-landscape-executive-summary.md` — 경쟁 환경 요약 (PT 자료용)
  - `Insights/strategy/feature-gap-analysis.md` — 기능 격차 분석 (차별화 포인트 도출)
  - `Insights/market/competitive-positioning-matrix.md` — 포지셔닝 매트릭스 (경쟁 비교표)
  - `Insights/market/pricing-models-comparison.md` — 과금 모델 비교 (가격 협상 참고)
  - `Insights/market/korea-erp-ai-landscape.md` — 한국 ERP AI 현황 (국내 고객 대응)
  - `Insights/market/partnership-ecosystem-map.md` — 파트너십 생태계 (협력사 연계)
- **secondary_sources**:
  - `Insights/strategy/go-to-market-patterns.md` — GTM 전략 (시장 접근 방법론)
  - `Insights/strategy/funding-valuation-tracker.md` — 경쟁사 투자 현황
  - `Insights/market/enterprise-vs-b2c-strategies.md` — Enterprise vs B2C 전략
  - `AI Agent Products/*/` — 개별 제품 프로필 (경쟁사별 약점 분석)
---

## 역할 간 공유 문서

아래 문서는 2개 이상의 역할에서 공통으로 참조합니다.

| 문서 | frontend | backend | architecture | planning | pm | qa | data | sales |
|------|:--------:|:-------:|:------------:|:--------:|:--:|:--:|:----:|:-----:|
| `protocols/protocol-comparison-mcp-a2a-a2ui.md` | ◑ | ● | ● | ○ | ○ | ○ | ◑ | ○ |
| `protocols/protocol-adoption-guide.md` | ○ | ● | ● | ◑ | ○ | ○ | ○ | ○ |
| `agent-skills/mcp-server-implementations.md` | ○ | ● | ● | ○ | ○ | ○ | ○ | ○ |
| `agent-skills/agent-skill-design.md` | ○ | ◑ | ● | ● | ○ | ○ | ○ | ○ |
| `agent-ui/hitl-approval-patterns.md` | ● | ○ | ◑ | ● | ○ | ○ | ○ | ○ |
| `strategy/feature-gap-analysis.md` | ○ | ○ | ○ | ● | ● | ○ | ○ | ● |
| `market/korea-erp-ai-landscape.md` | ○ | ○ | ○ | ● | ● | ○ | ○ | ● |
| `security-evaluation/agent-permission-models.md` | ○ | ● | ● | ○ | ○ | ● | ◑ | ○ |
| `security-evaluation/agent-evaluation-benchmarks.md` | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ |
| `security-evaluation/agent-guardrails-safety.md` | ○ | ○ | ◑ | ○ | ○ | ● | ○ | ○ |
| `open-source/agent-frameworks-landscape.md` | ○ | ● | ● | ○ | ○ | ○ | ◑ | ○ |
| `strategy/build-vs-buy-decision-framework.md` | ○ | ◑ | ● | ○ | ◑ | ○ | ○ | ○ |
| `knowledge-data/rag-architecture-comparison.md` | ○ | ● | ○ | ○ | ○ | ○ | ● | ○ |
| `knowledge-data/knowledge-graph-approaches.md` | ○ | ○ | ● | ○ | ○ | ○ | ● | ○ |
| `market/competitive-positioning-matrix.md` | ○ | ○ | ○ | ○ | ● | ○ | ○ | ● |
| `market/pricing-models-comparison.md` | ○ | ○ | ○ | ● | ● | ○ | ○ | ● |
> ● = primary, ◑ = secondary, ○ = 필요시 참조

---

## 빠른 질문 라우팅

에이전트 역할이 불명확하거나, 특정 질문에 대한 답을 바로 찾고 싶을 때 아래 표를 사용하세요.

| 질문 패턴 | 바로 가기 | 역할 |
|-----------|----------|------|
| "HITL 승인 UI를 어떻게 만들어야 하나?" | `Insights/agent-ui/hitl-approval-patterns.md` | frontend |
| "MCP 서버를 어떻게 구현하나?" | `Insights/agent-skills/mcp-server-implementations.md` | backend, architecture |
| "에이전트 루프를 어떻게 설계하나?" | `Insights/agent-runtime/agent-orchestration-loops.md` | backend, architecture |
| "RAG를 어떻게 구축하나?" | `Insights/knowledge-data/rag-architecture-comparison.md` | backend |
| "어떤 프로토콜을 채택해야 하나?" | `Insights/protocols/protocol-adoption-guide.md` | architecture |
| "경쟁사 기능 대비 우리 격차는?" | `Insights/strategy/feature-gap-analysis.md` | planning, pm |
| "한국 ERP AI 시장 현황은?" | `Insights/market/korea-erp-ai-landscape.md` | planning, pm |
| "경영진 브리핑 자료 필요" | `Insights/strategy/competitive-landscape-executive-summary.md` | pm |
| "과금 모델 어떻게 잡아야 하나?" | `Insights/market/pricing-models-comparison.md` | pm, planning |
| "Build vs Buy 결정 기준은?" | `Insights/strategy/build-vs-buy-decision-framework.md` | architecture, pm |
| "에이전트 권한 모델 비교" | `Insights/security-evaluation/agent-permission-models.md` | architecture, backend |
| "에이전트 병렬 처리 방법은?" | `Insights/agent-runtime/agent-parallel-processing.md` | backend, architecture |
| "Skill 설계를 어떻게 해야 하나?" | `Insights/agent-skills/agent-skill-design.md` | architecture, planning |
| "마켓플레이스를 어떻게 만드나?" | `Insights/agent-skills/agent-marketplace-ecosystem.md` | planning, architecture |
| "Artifacts/Canvas UI 패턴은?" | `Insights/agent-ui/artifacts-canvas-patterns.md` | frontend |
| "에이전트 품질을 어떻게 평가하나?" | `Insights/security-evaluation/agent-evaluation-benchmarks.md` | qa |
| "가드레일을 어떻게 설계하나?" | `Insights/security-evaluation/agent-guardrails-safety.md` | qa, architecture |
| "RAG 파이프라인을 어떻게 최적화하나?" | `Insights/knowledge-data/rag-architecture-comparison.md` | data, backend |
| "임베딩 모델을 어떻게 선택하나?" | `Insights/knowledge-data/embedding-retrieval-strategies.md` | data |
| "KG를 어떻게 구축하나?" | `Insights/knowledge-data/knowledge-graph-approaches.md` | data, architecture |
| "경쟁사 대비 차별화 포인트는?" | `Insights/market/competitive-positioning-matrix.md` | sales, pm |
| "제품 X에 대해 알려줘" | `AI Agent Products/{slug}/{slug}.md` | 모든 역할 |
| "이번 주 AI 뉴스 동향" | `Insights/maintenance/` (최신 파일) | 모든 역할 |

---

## 문서 활용 가이드

에이전트는 인사이트 문서의 **본문 전체를 읽고, 현재 맥락에 맞게 스스로 판단**합니다.

### 권장 읽기 흐름

```
1. AGENTS.md에서 자기 역할의 primary_sources 목록 확인
2. 해당 문서의 TL;DR 섹션으로 관련성 빠르게 확인
3. 관련성이 있으면 본문 전체를 읽고 Cross-Product Analysis, Key Findings 등에서 근거를 수집
4. 수집한 근거와 현재 프로젝트의 맥락(규모, 일정, 제약 조건 등)을 종합하여 판단
5. 필요 시 secondary_sources나 제품 프로필로 확장 탐색
```

### 주의사항

- 문서의 분석과 패턴 분류는 **참고 자료**이지 지시가 아닙니다
- 동일한 문서라도 프로젝트의 규모, 일정, 팀 역량, 시장 상황에 따라 다른 결론이 합리적일 수 있습니다
- 문서에 제시된 여러 패턴과 대안을 현재 맥락에 비추어 비교 평가하세요

---

*이 파일 최종 수정: 2026-02-12 (v3: decisions/decision_docs 제거, 문서 전체 읽기 방식으로 전환)*
