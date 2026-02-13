---
type: insight-synthesis
topic_id: protocol-comparison-mcp-a2a-a2ui
topic_name: '에이전트 프로토콜 비교: MCP vs A2A vs A2UI   vs MCP-UI'
category: protocols
tags:
- insight
- protocols
- MCP-Support
- A2A-Support
- comparison
status: done
confidence: high
last_updated: '2026-02-12'
source_products:
- claude
- workday-assistant
- salesforce-agentforce
- openai
source_files:
- UI/02_에이전트_UI_프로토콜/MCP-UI 프로토  콜 분석.md
- UI/02_에이전트_UI_프로토콜/A2UI 프로토  콜 및 MCP-UI 비교.md
- AI Agent Products/claude/claude.md
- AI Agent Products/workday-assistant/workday-assistant.md
- AI Agent Products/salesforce-agentforce/salesforce-agentforce.md
- AI Agent Products/openai/openai.md
- '[[2026/02/2026-02-12]]'
relevant_roles:
- architecture_agent
- data_agent
- frontend_agent
auto_update:
  enabled: true
  feeds:
  - https://github.com/modelcontextprotocol/specification/releases.atom
  keywords:
  - MCP specification update
  - A2A protocol release
  - agent interoperability standard
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 프로토콜 비교: MCP vs A2A vs A2UI vs MCP-UI

## TL;DR

- **MCP(Model Context Protocol)** 는 에이전트-도구 연결의 사실상 업계 표준으로, Anthropic이 창안하고 OpenAI/Google/Salesforce 등이 채택했다. 핵심 프리미티브는 Tools, Resources, Prompts이며, 2025년 12월 Linux Foundation AAIF에 기증되어 거버넌스가 중립화되었다.
- **A2A(Agent-to-Agent Protocol)** 는 에이전트 간 통신/협업 프로토콜로, Workday가 MCP와 함께 Agent Gateway에서 네이티브 지원한다. MCP가 "에이전트 <-> 도구" 연결이라면, A2A는 "에이전트 <-> 에이전트" 연결에 초점을 맞춘다.
- **MCP-UI** 는 MCP의 tool result에 UIResource를 포함시켜 sandboxed iframe/Remote DOM으로 인터랙티브 UI를 렌더링하는 확장 프로토콜이다. 기존 웹 UI/대시보드를 빠르게 임베드할 수 있으나, 디자인 일관성 확보가 과제이다.
- **A2UI(Agent to UI)** 는 Google이 2025년 12월 공개한 선언형 생성 UI 프로토콜로, JSON 기반 컴포넌트 설명을 JSONL 스트리밍으로 전송하여 호스트가 네이티브 위젯으로 렌더링한다. 보안과 디자인 일관성에서 유리하나, 호스트 측 구현 부담이 크다.
- **OpenAI Skills(2026.02)** 는 SKILL.md 매니페스트 기반의 도구 번들 패키징·실행 시스템으로, MCP의 "외부 서버 연결" 모델과 다른 "번들 실행" 모델을 제시한다. MCP와 보완적이나, Tool Connection Layer에서 간접 경쟁을 형성한다 [^6].
- **에이전트 플랫폼 관점에서** 는 MCP를 기본 도구 연결 레이어로 채택하되, UI 표현 계층에서 MCP-UI(기존 웹 자산 재활용)와 A2UI(네이티브 룩앤필 통합) 중 제품 전략에 맞는 선택이 필요하다.

---

## Context

엔터프라이즈 AI 에이전트 시장이 "단일 챗봇"에서 "다중 에이전트 협업 + 리치 UI" 방향으로 빠르게 진화하면서, 에이전트가 도구를 호출하고(MCP), 에이전트끼리 협업하며(A2A), 사용자에게 인터랙티브 UI를 전달하는(MCP-UI, A2UI) 프로토콜 표준화가 핵심 기술 의사결정 포인트로 부상하고 있다.

엔터프라이즈 AI 에이전트 플랫폼은 (1) 외부 시스템/도구 연결, (2) 멀티 에이전트 오케스트레이션, (3) 텍스트를 넘어선 리치 UI 응답이라는 세 가지 기술 레이어를 설계해야 한다. 이 세 레이어에 대응하는 프로토콜(MCP, A2A, MCP-UI, A2UI)의 기술적 차이와 생태계 성숙도를 정확히 파악하는 것이 아키텍처 결정의 선결 조건이다.

---

## Cross-Product Analysis

### 비교 매트릭스

| 프로토콜 | 주도 조직 | 핵심 목적 | Transport Layer | UI 전달 방식 | 생태계 성숙도 | 주요 채택 사례 |
|---------|----------|----------|----------------|-------------|-------------|-------------|
| **MCP** | Anthropic (AAIF 기증) | 에이전트 <-> 도구/데이터 연결 | JSON-RPC 2.0 (stdio, HTTP+SSE) | 없음 (텍스트/데이터 반환) | 높음 (업계 표준) | Claude, ChatGPT, Gemini, Salesforce 3.0, Workday |
| **A2A** | Google | 에이전트 <-> 에이전트 협업 | HTTP+JSON (Agent Card 기반) | 없음 | 초기 | Workday Agent Gateway |
| **MCP-UI** | MCP-UI Org (Block/Goose 중심) | MCP tool result에 리치 UI 포함 | MCP 확장 (UIResource in tool result) | HTML iframe / URL iframe / Remote DOM | 초기-성장 (2025.11 공식 MCP 확장) | Shopify MCP UI, Goose AI |
| **A2UI** | Google (Thesys) | 에이전트가 선언형 UI를 생성 | JSONL 스트리밍 | 컴포넌트 설명 JSON -> 네이티브 렌더링 | 초기 (2025.12 공개) | Thesys C1 Playground |
| **OpenAI Skills** | OpenAI | 에이전트 도구 번들 패키징·실행 | Responses API (REST) | 없음 (Shell Tool에서 코드 실행) | 초기 (2026.02 출시) | OpenAI Responses API |

### 프로토콜 레이어 분류

```
┌─────────────────────────────────────────────────┐
│            UI Presentation Layer                │
│         (MCP-UI / A2UI)                         │
│   "에이전트 응답을 어떻게 시각적으로 표현할 것인가"   │
├─────────────────────────────────────────────────┤
│          Agent Collaboration Layer              │
│                  (A2A)                           │
│     "에이전트끼리 어떻게 대화/협업할 것인가"         │
├─────────────────────────────────────────────────┤
│          Tool Connection Layer                  │
│           (MCP / OpenAI Skills)                  │
│   "에이전트가 외부 도구/데이터에 어떻게 접근할 것인가" │
│   MCP: 외부 서버 연결 | Skills: 도구 번들 패키징    │
└─────────────────────────────────────────────────┘
```

이 네 가지 프로토콜은 경쟁 관계가 아니라 **서로 다른 레이어**를 담당하며, 조합하여 사용할 수 있다.

### 패턴 분류

#### 패턴 A: Tool-Centric (MCP 단독)

**설명**: 에이전트가 MCP를 통해 외부 도구를 호출하고, 결과를 텍스트/마크다운/JSON으로 반환한다. UI는 호스트 앱이 자체적으로 구현한다.

**예시 제품**: Claude Code, ChatGPT(MCP 채택 후), Salesforce Agentforce 3.0

**장점**:
- 가장 성숙한 생태계. 수백 개의 MCP 서버가 이미 존재
- 구현 단순성. 서버는 데이터만 반환하고 UI 책임 없음
- 3가지 프리미티브(Tools, Resources, Prompts)로 명확한 역할 분리

**단점**:
- UI 표현이 텍스트/마크다운에 제한되어 드릴다운/필터/차트 등 인터랙티브 UX 구현이 어려움
- 호스트가 tool 결과마다 별도 UI를 개발해야 하는 부담

#### 패턴 B: UI-Embedded Tool (MCP + MCP-UI)

**설명**: MCP tool result의 `content` 배열 안에 `type: "resource"`로 UIResource를 포함시킨다. 호스트는 `UIResourceRenderer`가 `mimeType`(`text/html`, `text/uri-list`, `application/vnd.mcp-ui.remote-dom`)에 따라 자동으로 렌더링한다.

**예시 제품**: Shopify MCP UI, Goose AI Agent

**장점**:
- 기존 웹 UI(대시보드, 폼 등)를 `text/html` 또는 `text/uri-list`로 빠르게 임베드 가능
- Tool이 UI까지 제공하는 형태로, MCP 생태계 확장과 자연스럽게 연결
- `onUIAction` -> tool 재호출 -> UI 업데이트의 폐루프로 인터랙티브 드릴다운 구현 가능

**단점**:
- HTML/URL 임베드는 호스트 디자인 시스템과 이질감이 발생할 수 있음
- Remote DOM은 React/Web Components 중심으로 프레임워크 제약
- sandboxed iframe 기반이라 보안과 성능 간 트레이드오프 존재

#### 패턴 C: Declarative Generative UI (A2UI)

**설명**: 에이전트가 컴포넌트 설명(JSON)을 JSONL 스트리밍으로 전송하고, 호스트가 정의된 네이티브 컴포넌트 카탈로그(Button, Card, Table, Chart 등)로 매핑하여 렌더링한다. 임의 코드 실행 없이 선언적 데이터만 전송한다.

**예시 제품**: Thesys C1 Playground, Google 생태계 프로토타입

**장점**:
- LLM 생성에 최적화된 Flat/Adjacency List + JSONL 스트리밍으로 점진적 렌더링
- 임의 코드 실행이 없어 보안 강화
- 호스트 네이티브 위젯 렌더링으로 브랜드/디자인 시스템 일치

**단점**:
- 호스트가 컴포넌트 카탈로그, 위젯 레지스트리, 데이터 모델 스토어, 바인딩 리졸버 등을 구현해야 하는 부담
- 기존 웹 UI 재사용이 어렵고 네이티브 컴포넌트로 매핑하는 초기 투자 필요
- 생태계가 초기 단계라 레퍼런스 구현이 제한적

#### 패턴 D: Multi-Agent Orchestration (MCP + A2A)

**설명**: MCP로 도구 연결을 해결하고, A2A로 이종 에이전트 간 협업을 지원한다. Agent Gateway를 통해 내부/외부 에이전트를 통합 관리한다.

**예시 제품**: Workday Agent Gateway (MCP + A2A 네이티브 지원)

**장점**:
- 멀티벤더 에이전트 환경에서 상호운용성 확보
- ASOR(Agent System of Record)과 결합하여 에이전트 라이프사이클 통합 관리

**단점**:
- A2A 생태계가 아직 초기 단계
- Gateway 구축 및 에이전트 등록/관리의 운영 복잡성

#### 패턴 E: Bundled Skill Execution (OpenAI Skills + Shell Tool)

**설명**: 에이전트가 SKILL.md 매니페스트로 정의된 도구 번들(스크립트, 에셋, 인스트럭션)을 호스팅 컨테이너(Debian 12)에서 직접 실행한다. MCP가 "외부 서버에 연결"하는 모델이라면, Skills는 "도구를 번들로 패키징하여 에이전트 환경 내에서 실행"하는 모델이다. Server-side Compaction으로 장기 실행 안정성을 확보한다 [^6].

**예시 제품**: OpenAI Responses API (2026년 2월~)

**장점**:
- 도구의 버전 관리·재현성이 내장 (스킬 버전 고정)
- 컨테이너 기반 실행으로 의존성 격리 및 네트워크 접근 가능
- 스크립트 기반이라 복잡한 데이터 처리·변환 작업에 적합
- 인라인 스킬(base64 zip)로 별도 호스팅 없이 즉시 배포 가능

**단점**:
- OpenAI Responses API에 종속적 (범용 프로토콜이 아닌 플랫폼 기능)
- MCP의 수백 개 기존 서버 생태계 대비 스킬 생태계가 초기 단계
- 에이전트가 스킬 코드를 직접 실행하므로 보안 검증 부담 (OpenAI는 "Skills를 privileged code로 취급"할 것을 권고)
- 외부 시스템 통합에서는 MCP의 서버 기반 연결이 더 적합

**MCP와의 관계**:
MCP와 Skills는 경쟁보다 **보완적** 관계에 가깝다. MCP는 외부 시스템(DB, API, 서비스)에 표준 인터페이스로 연결하는 "연결 프로토콜"이고, Skills는 재사용 가능한 도구 로직을 패키징하여 에이전트 환경 내에서 실행하는 "실행 프레임워크"이다. OpenAI 자체도 MCP를 지원하면서 Skills를 추가한 것은, 두 접근법이 다른 사용 사례를 커버함을 인정한 것이다. 다만, 에이전트 도구 생태계의 표준 주도권을 놓고 간접적 경쟁이 발생할 수 있다.
<!-- Deep Dive: 2026-02-12 | OpenAI Skills vs MCP | 패턴 E(Bundled Skill Execution) 추가 및 MCP와의 관계 분석 -->

---

## Key Findings

1. **MCP와 A2A는 경쟁이 아닌 보완 관계이다** -- MCP는 "에이전트가 도구에 접근하는 방법"을, A2A는 "에이전트가 다른 에이전트와 대화하는 방법"을 정의한다. Workday가 Agent Gateway에서 두 프로토콜을 모두 네이티브 지원하는 것은 이 보완성을 인식한 결과이다. -- *Source*: [[workday-assistant]]

2. **MCP-UI와 A2UI는 같은 문제(텍스트 벽 문제)를 다른 실행 모델로 해결한다** -- MCP-UI는 "서버가 HTML/URL/Remote DOM을 보내면 클라이언트가 sandbox에서 실행"하는 모델이고, A2UI는 "서버가 컴포넌트 설명 데이터를 보내면 클라이언트가 네이티브 위젯으로 렌더"하는 모델이다. 핵심 트레이드오프는 **기존 웹 자산 재활용(MCP-UI 유리)** vs **보안/디자인 일관성(A2UI 유리)** 이다. -- *Source*: [[A2UI 프로토콜 및 MCP-UI 비교]]

3. **MCP 생태계가 압도적으로 성숙하다** -- Anthropic이 2024년 11월 공개한 MCP는 2025년 3월 OpenAI 채택, 4월 Google DeepMind 지원, 12월 AAIF 기증으로 사실상 업계 표준이 되었다. Salesforce Agentforce 3.0, Workday Agent Gateway, Microsoft Copilot Studio 등 주요 엔터프라이즈 플랫폼이 모두 MCP를 채택했다. 반면 A2A, MCP-UI, A2UI는 모두 2025년 하반기에 공개된 초기 단계이다. -- *Source*: [[claude]], [[salesforce-agentforce]]

4. **MCP-UI의 "Intent 중재 패턴"이 에이전트 기반 UI의 핵심 아키텍처 패턴이다** -- Shopify MCP UI에서 확인된 패턴으로, UI 컴포넌트(iframe)가 상태를 직접 변경하지 않고 Intent 메시지를 Host로 보내면, 에이전트가 이를 해석하여 tool 호출로 상태를 갱신한다. 이는 사용자 경험은 Direct Manipulation으로 좋아지면서, 실제 상태 변경은 에이전트가 통제하여 일관성과 안전장치를 확보하는 구조이다. -- *Source*: [[MCP-UI 프로토콜 분석]]

5. **A2UI의 JSONL 스트리밍 + Adjacency List 구조는 LLM 네이티브 생성에 유리하다** -- LLM이 중첩 트리를 한 번에 완벽히 생성하기 어렵다는 현실을 전제로, ID 기반 참조가 가능한 평면 컴포넌트 리스트와 JSONL 순차 전송으로 점진적 렌더링을 구현한다. 부분 갱신(dataModelUpdate)도 지원하여 전체 UI 재전송 없이 최소 변경만 보낼 수 있다. -- *Source*: [[A2UI 프로토콜 및 MCP-UI 비교]]

6. **OpenAI Skills는 MCP의 "서버 연결" 모델과 다른 "번들 실행" 모델로 Tool Connection Layer에 새로운 축을 추가한다** -- 2026년 2월 발표된 OpenAI Skills는 SKILL.md 매니페스트 + 파일 번들을 컨테이너에서 직접 실행하는 방식으로, MCP의 JSON-RPC 기반 외부 서버 연결과 근본적으로 다른 실행 모델을 제시한다. MCP가 "연결(connection)"에 초점이라면 Skills는 "패키징과 실행(packaging & execution)"에 초점이다. 두 접근법은 보완적이나, 에이전트 도구 생태계의 사실상 표준을 놓고 간접적 경쟁이 형성될 수 있다. OpenAI가 MCP를 지원하면서 동시에 Skills를 도입한 것은 단일 프로토콜로 모든 도구 사용 시나리오를 커버하기 어렵다는 현실적 판단의 반영이다 [^6]. -- *Source*: [[openai]]
<!-- Deep Dive: 2026-02-12 | OpenAI Skills vs MCP | Key Finding 6 추가: Skills의 번들 실행 모델과 MCP 서버 연결 모델 비교 -->

---


---

## Source References

### 제품 프로필
- [[claude]] -- MCP 창안 및 생태계 주도, 프로토콜 전략 분석
- [[workday-assistant]] -- MCP + A2A 네이티브 지원, Agent Gateway 아키텍처
- [[salesforce-agentforce]] -- Agentforce 3.0 MCP 내장 지원, MuleSoft Agent Fabric
- [[openai]] -- Skills API, Shell Tool, MCP 채택, 도구 번들 실행 모델

### UI 리서치
- [[MCP-UI 프로토콜 분석]] -- MCP-UI 핵심 개념, UIResource 스펙, Shopify 사례 분석
- [[A2UI 프로토콜 및 MCP-UI 비교]] -- A2UI 핵심 기술, MCP-UI와의 관점별/장단점 비교

### External
- [^6]: [OpenAI Skills Documentation](https://developers.openai.com/api/docs/guides/tools-skills) (2026-02-11) — Skills API 아키텍처, SKILL.md 매니페스트, Shell Tool 컨테이너, 버전 관리, 보안 가이드라인

### 외부 참고 자료
- [MCP Architecture Spec (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/architecture)
- [MCP-UI Documentation](https://mcpui.dev/guide/introduction)
- [MCP-UI GitHub](https://github.com/MCP-UI-Org/mcp-ui)
- [A2UI 공식 사이트](https://a2ui.org/)
- [Thesys MCP-UI Overview](https://www.thesys.dev/blogs/mcp-ui-overview)
- [Shopify MCP UI Engineering Blog](https://shopify.engineering/mcp-ui-breaking-the-text-wall)
- [Goose MCP-UI Extensions](https://block.github.io/goose/docs/guides/interactive-chat/mcp-ui/)
- [Workday Blog: AI Agent Protocols Guide](https://blog.workday.com/en-us/building-enterprise-intelligence-a-guide-to-ai-agent-protocols-for-multi-agent-systems.html)

---

## Recent Updates

| Date | Source | Summary | Tags |
|------|--------|---------|------|
| 2026-02-11 | [Vercel MCP server: runtime logs](https://vercel.com/changelog/agents-can-now-access-runtime-logs-with-vercels-mcp-server) · [[2026/02/2026-02-11\|다이제스트]] | Vercel MCP 서버에 get_runtime_logs 도구 추가. 에이전트가 Functions 런타임 로그 직접 조회 | #protocols |
| 2026-02-12 | [OpenAI Skills API + Shell Tool + Compaction](https://venturebeat.com/orchestration/openai-upgrades-its-responses-api-to-support-agent-skills-and-a-complete) · [[2026/02/2026-02-12\|다이제스트]] | ✅ SKILL.md 매니페스트 기반 재사용 모듈 + Debian 12 Shell Tool + 컨텍스트 Compaction. MCP 생태계와 간접 경쟁 | #agent-skills #protocols |

---

*Last synthesized: 2026-02-12 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
