---
type: insight-synthesis
topic_id: agent-skill-design
topic_name: 에이전트 Skill 설계 패턴
category: agent-skills
tags:
- insight
- agent-skills
- skill-design
- agent-builder
- low-code
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- salesforce-agentforce
- workday-assistant
- glean
- claude
- microsoft-copilot
- servicenow-now-assist
source_files:
- '[[salesforce-agentforce]]'
- '[[workday-assistant]]'
- '[[glean]]'
- '[[claude]]'
- '[[microsoft-copilot]]'
- '[[servicenow-now-assist]]'
relevant_roles:
- architecture_agent
- planning_agent
- sales_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - skill design
  - skill composition
  - agent skills
  - visual builder
  - natural language skill
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 Skill 설계 패턴

## TL;DR

- **에이전트 Skill 설계는 크게 4가지 패턴으로 분류된다**: (1) 비즈니스 도메인을 Topic으로 분류하고 Action을 매핑하는 Topic-Action 모델(Salesforce), (2) 패키징된 개별 GenAI 기능 단위(Skill)를 에이전트가 조합하는 Skill Composition 모델(ServiceNow), (3) 자연어 프롬프트로 에이전트의 목적·지식·행동을 정의하는 Natural Language Definition 모델(Glean, Claude Cowork), (4) 비주얼 캔버스에서 노드·플로우를 연결하여 에이전트를 구성하는 Visual Builder 모델(Copilot Studio, Workday Flowise)
- **"생성 용이성"과 "실행 정밀도"는 구조적으로 트레이드오프 관계에 있다**: 자연어 정의 방식은 진입 장벽이 가장 낮으나 복잡한 비즈니스 로직의 정밀 제어가 어렵고, Topic-Action이나 Skill Kit 방식은 설계 비용이 높으나 거버넌스·감사·재현성에서 우수하다. 6개 제품 모두 이 트레이드오프를 해소하기 위해 "자연어 프로토타이핑 + 구조화 정제" 2단계 워크플로우로 수렴하고 있다
- **Skill의 "재사용 단위(Unit of Reuse)" 설계가 플랫폼 생태계의 경쟁력을 결정한다**: ServiceNow의 NASK(Now Assist Skill Kit), Salesforce의 Action Library, Glean의 프리빌트 에이전트 카탈로그 등 Skill을 패키징·공유·마켓플레이스화하는 전략이 생태계 확장의 핵심 동력이다
- **엔터프라이즈 Skill 설계에서 "빌드 타임 거버넌스"가 런타임 거버넌스만큼 중요해지고 있다**: Salesforce의 Topic 범위 제한(Guardrails), ServiceNow의 AI Agent Orchestrator 정책 적용, Workday의 ASOR 기반 에이전트 역할·권한 사전 정의 등 Skill을 배포하기 전에 행동 범위를 구조적으로 제한하는 패턴이 보편화
- **MCP Tools가 Skill의 "원자적 실행 단위(Atomic Execution Unit)"로 수렴하는 추세가 관찰된다**: Claude의 MCP Tools, Salesforce의 MuleSoft Agent Fabric을 통한 MCP 매핑, Copilot Studio의 MCP 네이티브 지원 등 Skill의 실행 계층에서 MCP가 표준 인터페이스로 자리잡고 있다

---

## Context

엔터프라이즈 AI 에이전트 프로덕트를 개발하면서, "사용자(관리자, 개발자, 비즈니스 사용자)가 에이전트의 능력(Skill)을 어떻게 정의·구축·관리하는가"는 프로덕트의 채택률과 확장성을 결정짓는 핵심 UX 결정이다. Skill 설계 패턴은 단순한 UI/UX 문제가 아니라, 에이전트의 행동 범위 제어(거버넌스), 재사용성(생태계), 실행 정밀도(비즈니스 로직 충실도)를 동시에 결정하는 아키텍처 결정이다.

2025~2026년 주요 경쟁사들이 Agent Builder를 앞다투어 출시하면서, Skill 설계 방식이 급격히 다양화되고 있다. Salesforce의 Topic-Action 모델, ServiceNow의 Skills-Agents-Orchestrator 3계층, Glean의 자연어 에이전트 빌더, Claude의 MCP Tools 기반 확장, Copilot Studio의 비주얼 빌더, Workday의 Flowise Agent Builder 등 서로 다른 철학과 구현이 공존한다. 이 다양한 접근법을 체계적으로 비교·분석하여, Skill 설계 경험이 어떤 패턴을 채택하고 어떻게 차별화해야 하는지에 대한 근거를 제공한다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | Skill 설계 방식 | 빌더 도구 | Skill 정의 단위 | 재사용 메커니즘 | 거버넌스 수준 | 대상 사용자 |
|---------|---------------|----------|---------------|--------------|------------|-----------|
| Salesforce Agentforce | Topic-Action 매핑 (구조화) | Agent Builder (3-Panel Layout) | Topic + Action (Flow/Apex/API) | Agentforce Studio Action Library | Topic 범위 제한 + Guardrails + Gateway ABAC | Admin / Low-code Dev |
| ServiceNow Now Assist | Skill Composition (패키징) | AI Agent Studio (로코드) | Now Assist Skill (패키징된 GenAI 단위) | NASK(Skill Kit) + ServiceNow Store | Orchestrator 정책 + Assist 토큰 예산 | Admin / Platform Dev |
| Glean | Natural Language Definition | 에이전트 빌더 (노코드) + Agents API | 자연어 프롬프트 + 지식 소스 + 도구 | 프리빌트 에이전트 카탈로그 (20+종) | Enterprise Graph 권한 상속 | Business User / Admin |
| Claude | MCP Tools + Agentic Loop | Claude Code CLI / Cowork Skills | MCP Tool (Tools/Resources/Prompts) | MCP 서버 레지스트리 + 커뮤니티 생태계 | Constitutional AI + Human-in-the-Loop | Developer / Power User |
| Microsoft Copilot | Visual Builder + Plugin | Copilot Studio + Agent Builder | Plugin / Connector / MCP Tool | Power Platform 1,000+ 커넥터 | Copilot Orchestrator + Entra 인증 | Citizen Dev / Pro Dev |
| Workday | Visual Agent Builder + ASOR | Flowise Agent Builder + Workday Build | Agent (ASOR 등록 단위) + Gateway API | Agent Partner Network (50+) Marketplace | ASOR 역할·권한·국가별 가용성 사전 정의 | Dev / HR-Finance Admin |

### 패턴 분류

#### 패턴 A: Topic-Action Model (구조화 매핑형)

**대표 제품**: Salesforce Agentforce

사용자 의도를 비즈니스 도메인 단위인 "Topic"으로 분류하고, 각 Topic에 실행 가능한 "Action"(Salesforce Flow, Apex 코드, 외부 API)을 매핑하는 구조화된 설계 방식이다. Agent Builder의 3-Panel Layout에서 좌측 단계 패널로 Topic을 정의하고, 중앙 패널에서 Action을 연결하며, 우측 가이드 패널에서 인스트럭션을 작성한다. Atlas Reasoning Engine이 런타임에 사용자 입력을 Topic으로 자동 분류하여 적절한 Action을 트리거한다.

- **장점**: 에이전트 행동 범위를 Topic 수준에서 명시적으로 제한할 수 있어 거버넌스가 강력하다. Action이 기존 Salesforce Flow/Apex와 연결되므로 레거시 자동화 자산을 재활용할 수 있다. MuleSoft Agent Fabric을 통해 외부 API를 Action으로 직접 노출하는 것이 자연스럽다.
- **단점**: Topic-Action 구조를 설계하려면 비즈니스 프로세스에 대한 깊은 이해가 필요하다. 복잡한 다단계 워크플로우 설계 시 Flow, Apex, MuleSoft 지식이 필요하여 학습 곡선이 존재한다. Topic 분류 체계가 경직되면 새로운 사용자 의도에 대한 유연한 대응이 어려워진다.

#### 패턴 B: Skill Composition Model (패키징 조합형)

**대표 제품**: ServiceNow Now Assist

개별 GenAI 기능을 "Skill"이라는 표준화된 패키지 단위로 캡슐화하고, 에이전트가 다수의 Skill을 조합하여 엔드투엔드 워크플로우를 구성하는 방식이다. Skills -> Agents -> Orchestrator의 3계층 아키텍처로, 단일 Skill(티켓 요약, 해결 노트 초안 등)부터 복수 Skill을 체인하는 Agent, 그리고 멀티 에이전트를 조율하는 Orchestrator까지 체계적으로 확장된다. Now Assist Skill Kit(NASK)으로 커스텀 Skill 개발도 가능하다.

- **장점**: Skill이 독립적 패키지이므로 재사용성과 조합 유연성이 높다. Orchestrator가 Assist 토큰 예산, RBAC, 감사 로깅을 중앙에서 관리하여 엔터프라이즈 거버넌스가 강력하다. Skill 단위로 활성화/비활성화할 수 있어 점진적 도입이 용이하다.
- **단점**: Skill 간 데이터 전달과 상태 관리를 위한 오케스트레이션 로직이 복잡해질 수 있다. NASK를 통한 커스텀 Skill 개발은 Now Platform 전문 지식이 필요하다. MCP/A2A 같은 개방형 프로토콜 채택이 아직 공식화되지 않아 외부 에이전트와의 상호운용성이 제한적이다.

#### 패턴 C: Natural Language Definition (자연어 정의형)

**대표 제품**: Glean Agent Builder, Claude Cowork Skills

에이전트의 목적, 지식 범위, 사용 도구, 행동 지침을 자연어 프롬프트로 정의하는 방식이다. Glean은 노코드 에이전트 빌더에서 자연어로 전문 에이전트를 정의하고, 지식 소스(Enterprise Graph 연결 앱)와 도구를 선택적으로 부착한다. Claude Cowork는 Skills 기반으로 산출물 유형(문서, 프레젠테이션 등)을 지정하고, Agentic Loop가 자율적으로 계획-실행-검증을 반복한다.

- **장점**: 진입 장벽이 가장 낮아 비즈니스 사용자도 에이전트를 직접 정의할 수 있다. 프롬프트 수정만으로 에이전트 행동을 빠르게 반복(iterate)할 수 있어 프로토타이핑 속도가 빠르다. LLM의 추론 능력을 최대한 활용하여 미리 정의되지 않은 상황에도 유연하게 대응한다.
- **단점**: 자연어 정의의 모호성이 에이전트 행동의 재현성(reproducibility)을 저하시킨다. 복잡한 비즈니스 규칙(승인 체인, 조건부 분기, 예외 처리)을 자연어만으로 정밀하게 표현하기 어렵다. 거버넌스 경계가 암시적(implicit)이어서 엔터프라이즈 감사 요구사항을 충족하기 힘들다.

#### 패턴 D: Visual Builder (비주얼 캔버스형)

**대표 제품**: Microsoft Copilot Studio, Workday Flowise Agent Builder

시각적 캔버스(노드-엣지 다이어그램, 플로우차트)에서 에이전트의 대화 흐름, 도구 호출, 조건 분기를 드래그앤드롭으로 구성하는 방식이다. Copilot Studio는 Agent Builder에서 프로토타입을 빠르게 생성한 뒤 Copilot Studio로 이관하여 엔터프라이즈급으로 확장하는 2단계 워크플로우를 채택한다. Workday는 Flowise 기반 비주얼 에이전트 빌더와 Workday Build 플랫폼을 결합하여 로코드/노코드 에이전트 개발을 지원한다.

- **장점**: 에이전트의 실행 흐름을 시각적으로 파악할 수 있어 디버깅과 팀 협업이 용이하다. Power Platform 1,000개 이상 커넥터(Copilot Studio)나 Agent Gateway API(Workday Build)와 자연스럽게 연결된다. MCP 네이티브 지원(Copilot Studio)으로 외부 도구 연결이 표준화되어 있다.
- **단점**: 복잡한 에이전트일수록 캔버스가 거대해져 관리가 어려워지는 "스파게티 플로우" 문제가 발생한다. 비주얼 빌더의 표현력이 코드 기반 접근법에 비해 제한적일 수 있다. 플랫폼별 비주얼 빌더의 학습 곡선이 존재한다.

---

## Key Findings

1. **모든 제품이 "자연어 프로토타이핑 -> 구조화 정제" 2단계 수렴을 보인다**: Copilot Studio의 "Agent Builder -> Copilot Studio 이관", Salesforce의 "자연어 인스트럭션 -> Topic-Action 구조화", Glean의 "자연어 에이전트 정의 -> Agents API 코드 확장"까지, 6개 제품 모두 초기 설계는 자연어/로코드로 빠르게 시작하되, 프로덕션 배포 시에는 구조화된 형태로 정제하는 워크플로우를 채택하고 있다. 이는 자연어의 속도와 구조화의 정밀성 사이의 트레이드오프를 2단계 프로세스로 해소하려는 업계 공통 전략이다 -- *Source*: [[microsoft-copilot]], [[salesforce-agentforce]], [[glean]]

2. **"Skill의 재사용 단위" 설계가 플랫폼 vs 도구의 포지셔닝을 결정한다**: ServiceNow는 Skill을 NASK로 패키징하여 ServiceNow Store에서 유통하고, Salesforce는 Action을 Agentforce Studio Library에서 공유하며, Workday는 Agent 자체를 ASOR에 등록하여 Marketplace에서 배포한다. 반면 Claude는 MCP Server를 재사용 단위로 삼아 커뮤니티 레지스트리에서 공유한다. 재사용 단위의 추상화 수준(Skill < Action < Agent < MCP Server)이 각 제품의 생태계 전략을 반영한다. 추상화 수준이 낮을수록(Skill 단위) 조합 유연성이 높고, 높을수록(Agent/MCP Server 단위) 즉시 활용 가능성이 높다 -- *Source*: [[servicenow-now-assist]], [[salesforce-agentforce]], [[workday-assistant]], [[claude]]

3. **빌드 타임 거버넌스(Design-Time Governance)가 엔터프라이즈 차별화의 새로운 전선이다**: 기존에는 에이전트 실행 시점(런타임)의 거버넌스(RBAC, 감사 로그)에 집중했으나, Salesforce의 Topic Guardrails(에이전트가 벗어날 수 없는 주제 경계), Workday의 ASOR 사전 역할 배정(에이전트가 접근할 수 있는 데이터와 액션을 배포 전에 확정), ServiceNow의 Orchestrator 정책 사전 적용 등 Skill을 설계하는 시점에서부터 행동 범위를 구조적으로 제한하는 패턴이 부상하고 있다. 이는 "AI 에이전트가 예측 불가능한 행동을 하는 것을 사전 방지"하려는 엔터프라이즈의 핵심 요구를 반영한다 -- *Source*: [[salesforce-agentforce]], [[workday-assistant]], [[servicenow-now-assist]]

4. **Claude의 MCP Tools 모델은 Skill 설계의 "실행 계층 표준"으로 다른 패턴의 하부에 침투하고 있다**: Salesforce는 MuleSoft Agent Fabric을 통해 외부 API를 MCP 도구로 매핑하고(3.0부터), Copilot Studio는 MCP를 네이티브 지원하여 외부 MCP 서버를 플러그앤플레이로 연결하며, Workday는 Agent Gateway에서 MCP를 통해 에이전트에 비즈니스 데이터를 제공한다. 즉, 상위 레이어에서는 각 제품이 고유한 Skill 설계 패턴을 유지하되, 실행 계층(외부 도구 호출)에서는 MCP가 공통 인터페이스로 수렴하고 있다. Skill 설계 패턴은 다양하지만, Skill의 "손발"은 MCP로 통일되는 구조이다 -- *Source*: [[claude]], [[salesforce-agentforce]], [[microsoft-copilot]], [[workday-assistant]]

5. **ServiceNow의 3계층(Skills-Agents-Orchestrator) 모델이 가장 체계적인 Skill 아키텍처를 제시한다**: 다른 제품들은 Skill 정의와 에이전트 구축을 하나의 레이어에서 처리하는 반면, ServiceNow는 개별 Skill(원자 단위) -> Agent(Skill 조합) -> Orchestrator(멀티 에이전트 조율)의 명시적 3계층을 제공한다. 이는 단순 자동화부터 크로스 도메인 복합 워크플로우까지 동일한 아키텍처 안에서 확장할 수 있는 구조적 우수성을 가진다. 특히 Orchestrator의 토큰 예산 관리는 GenAI 비용 통제라는 현실적 과제에 직접 대응한다 -- *Source*: [[servicenow-now-assist]]

6. **Glean의 "지식 기반 Skill 정의"는 비개발자 채택에서 가장 낮은 진입 장벽을 보인다**: Glean의 에이전트 빌더는 (1) 자연어로 에이전트 목적 기술, (2) Enterprise Graph에서 지식 소스 선택, (3) 필요 시 도구 부착의 3단계로 에이전트를 정의한다. 기존 업무 데이터의 권한을 그대로 상속하므로 별도의 보안 설정이 불필요하고, 20개 이상의 프리빌트 에이전트를 시작점으로 제공하여 "빈 캔버스" 문제를 해소한다. 다만 이 단순성은 복잡한 비즈니스 로직 구현의 한계와 직결된다 -- *Source*: [[glean]]

---

## Source References

### 제품 프로필
- [[salesforce-agentforce]] -- Agent Builder 3-Panel Layout, Topic-Action 모델, MuleSoft Agent Fabric, Agentforce Studio, Atlas Reasoning Engine, Topic Guardrails
- [[servicenow-now-assist]] -- Now Assist Skills 3계층 아키텍처(Skills-Agents-Orchestrator), NASK(Skill Kit), AI Agent Studio, Assist 토큰 예산 관리, Virtual Agent
- [[glean]] -- 노코드 에이전트 빌더, 자연어 에이전트 정의, Enterprise Graph 지식 소스 연결, 프리빌트 에이전트 카탈로그(20+종), Agents API(LangChain Agent Protocol)
- [[claude]] -- MCP 3가지 프리미티브(Tools/Resources/Prompts), Claude Code Agentic Loop, Claude Cowork Skills, MCP 서버 레지스트리, Constitutional AI
- [[microsoft-copilot]] -- Copilot Studio Agent Builder, MCP 네이티브 지원, Power Platform 1,000+ 커넥터, 멀티 에이전트 오케스트레이션, Python Code Interpreter
- [[workday-assistant]] -- Workday Build + Flowise Agent Builder, ASOR 에이전트 라이프사이클(등록-온보딩-역할배정-운영-성과추적), Agent Gateway(MCP/A2A), Agent Partner Network 50+ Marketplace

### 관련 인사이트
- [[mcp-server-implementations]] -- MCP 서버 구현 방식 비교: Skill 실행 계층에서의 MCP 표준 인터페이스 분석

### 외부 참고 자료
- [Trailhead: Explore the New Agentforce Builder](https://trailhead.salesforce.com/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder)
- [Now Assist Skill Kit (NASK) FAQ](https://www.servicenow.com/community/now-assist-articles/now-assist-skill-kit-nask-faq/ta-p/3007953)
- [Glean AI Agents](https://www.glean.com/product/ai-agents)
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)
- [Microsoft Build 2025: Multi-Agent Orchestration](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/)
- [Workday Build: AI Developer Toolset](https://investor.workday.com/2025-06-03-Workday-Unveils-AI-Developer-Toolset,-Empowering-Developers-to-Customize-and-Connect-AI-Apps-and-Agents-on-the-Workday-Platform)

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
