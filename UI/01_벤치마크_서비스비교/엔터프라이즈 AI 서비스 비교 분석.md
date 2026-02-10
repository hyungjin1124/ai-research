보고자료: ![[UI, UX 분석 1.pptx]]
- 기본 UI/UX 분석
	- 메인 인터페이스 구성 
	- 대화형 UI 패턴 (입력창, 응답 표시, 후속 질문, Human-in-the-loop) 
	- 데이터 시각화 방식(드릴다운 방식)
	- 작업 진행 상태 표현
	- 에이전트 추론 과정 시각화
	- 운영 관제
	- 대시보드 구성
		- 사용자 맞춤형 대시보드: 사용자가 직접 원하는 지표나 데이터 포인트를 선택하여 대시보드를 개인화할 수 있는 기능.
	- MCP 활용
- 추가 기능 분석
	- Morning Briefing 모드
	- 권한 기반 UI 및 데이터 접근 제어

| 분석 대상 서비스                              | 1. Main Interface Composition                                                                                   | 2. Conversational UI Patterns                                                                          | 3. Human-In-The-Loop                                                                       | 4. Data Visualization                                                                     | 5. Task Progress Representation                                                                  | 6. Agent Process Visualization                                                      | 7. Operational Monitoring/Control                                                        | 8. Dashboard Composition                                                                 | 9. MCP Utilization                                                                            |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Microsoft Copilot for Dynamics 365** | • Sidecar 방식 (애플리케이션 옆 배치)  <br>• Copilot Home (역할별 대시보드)  <br>• Embedded Copilot (앱 내 통합)                      | • Natural language 입력  <br>• 실시간 스트리밍 응답  <br>• Follow-up suggestions 자동 생성  <br>• Timeline highlights | • Proposal summary 검토/승인  <br>• Email drafts 편집 후 발송  <br>• Teams/Outlook 협업 피드백           | • Opportunity pipeline view  <br>• Schedule board 최적화  <br>• Dynamic grouping/aggregation | • Teams에서 task 자동 생성  <br>• 담당자 할당 및 상태 추적  <br>• Service console handoff                        | • Plugin 선택 과정 표시  <br>• Dataverse 연결 자동 식별  <br>• 프롬프트 처리 로그                       | • Manager insights dashboard  <br>• Conversation analytics  <br>• Usage tracking         | • Widget 기반 모듈형  <br>• Role-specific views  <br>• Real-time 데이터 업데이트                     | • Microsoft 365 앱 간 연결  <br>• Teams/Outlook seamless 통합  <br>• Third-party 시스템 지원             |
| **SAP Joule**                          | • SAP Start/Work Zone embedded  <br>• Cross-product UX (80% 트랜잭션)  <br>• Joule Studio (커스텀 빌더)                  | • Rich UI Elements (List, Card, Carousel) streaming  <br>• Content loader  <br>• Guided AI Prompts     | • SuccessFactors goals 승인  <br>• Ariba segmentation 검토  <br>• Natural language instruction | • Informational pattern  <br>• Summarization pattern  <br>• Proposal creation pattern     | • Multi-stage streaming  <br>• 단계별 progress indicator  <br>• Status updates                      | • Scenario Catalog matching  <br>• Knowledge Catalog retrieval  <br>• RAGe 프로세스 투명화 | • Joule Admin Center  <br>• Correlation IDs 추적  <br>• Message history JSON export        | • SAP Fiori compliant UI  <br>• Role-based homepage  <br>• Context-aware recommendations | • Microsoft 365 Copilot 양방향  <br>• SAP Knowledge Graph bridge  <br>• Multi-product context 유지 |
| **Salesforce Agentforce**              | • Agentforce Builder (통합 workspace)  <br>• 3-Panel Layout (Steps/Config/Guidance)  <br>• Atlas Reasoning Engine | • Natural language instruction  <br>• Topic-based organization  <br>• Follow-up questions 제안           | • **Omni Supervisor** (실시간 모니터링)  <br>• Conversation listen-in  <br>• Test-drive 후 배포      | • Vector Database 처리  <br>• Visualization 미리보기  <br>• RAG feedback loop 시각화               | • Step-by-step reasoning 실시간  <br>• Topic → Action → Record → Grounding  <br>• Decision tree 시각화 | • **Atlas Engine 가시화**  <br>• Agent Script 하이브리드  <br>• Flow 실행 상세 view             | • Omni Supervisor dashboard  <br>• Interactions table with summary  <br>• Testing Center | • Agentforce Studio gateway  <br>• Agent Actions library  <br>• Learning resources 통합    | • MuleSoft API 직접 연결  <br>• Human-like API 대화  <br>• Multi-channel deployment                 |
| **ServiceNow Now Assist**              | • Now Assist Panel (embedded)  <br>• MyNow (개인화)  <br>• Admin Console (중앙 관리)                                   | • LLM-based intent recognition  <br>• Multi-turn with context  <br>• Carousel format results           | • Chat summarization (전환)  <br>• Resolution notes review  <br>• Knowledge article approval | • **Genius Result card**  <br>• Multiple articles 합성  <br>• Result-card customization     | • **Proactive triggers/notifications**  <br>• Case/incident summarization  <br>• Workflow 단계별 추적 | • Virtual Agent Designer  <br>• Slash commands  <br>• Topic Description discovery   | • Skills/Plugins 관리  <br>• Usage aggregation  <br>• Dynamic Translation 설정               | • Theme Builder branding  <br>• Service Portal config  <br>• Multiple assistant profiles | • Watsonx LLM connector  <br>• Generic LLM connector  <br>• SharePoint 통합                     |
| **Snowflake Intelligence**             | • Snowsight Wizard  <br>• ai.snowflake.com (독립 인터페이스)  <br>• Cortex Analyst UI                                  | • Natural language to SQL  <br>• Follow-up 데이터 탐색  <br>• Semantic View 기반 응답                           | • YAML 편집 후 즉시 테스트  <br>• Human-in-the-loop validation  <br>• RBAC 세밀한 권한                  | • **Metrics/Dimensions/Facts 구조**  <br>• TPC-DS 샘플 시각화  <br>• Derived metrics 계산          | • Cortex Agent 실행 단계  <br>• Data indexing progress  <br>• Query execution plan                   | • Semantic View logical layer  <br>• RAG retrieval 투명화  <br>• LLM + rule-based 분리   | • Usage statistics  <br>• Row/column governance tracking  <br>• Cost and latency metrics | • Data Agent selector  <br>• Multiple semantic layers  <br>• Cortex Search integration   | • **Snowflake MCP Server**  <br>• Auto-generation as MCP tool  <br>• Universal data access    |



| **Workday Assistant (ASOR)**           | • Unified Experience (single view)  <br>• Workday Marketplace  <br>• **Agent Gateway** (MCP/A2A)                | • Natural language HR/Finance  <br>• Complex process guidance  <br>• Copilot/Slack 스타일                 | • Manager bonus 결정 지원  <br>• Job Architecture agent 검토  <br>• Task workflow confirmation      | • Real-time cross-app info  <br>• Expense/logistics dashboards  <br>• Budget overrun alerts               | • Transaction step-by-step  <br>• Workflow completion status  <br>• Rule-based alerts                | • **ASOR 역할/데이터/액션 정의**  <br>• Agent lifecycle 표시  <br>• Performance tracking                                | • Agent Partner Network  <br>• **Agent를 직원처럼 관리**  <br>• Rate limits/governance                     | • Illuminate agents 통합  <br>• Business process orchestration  <br>• Cross-platform coordination   | • **MCP + A2A protocol**  <br>• Agent Gateway  <br>• Seamless cross-system collaboration                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **ThoughtSpot Sage (Spotter)**         | • Spotter (agentic engine)  <br>• SpotterModel (semantic generator)  <br>• SpotterViz (dashboarding)            | • GPT/Gemini + search token  <br>• Conversational BI (Ask Sage)  <br>• Starter questions 제안            | • **Patent-pending feedback loop**  <br>• 단어/구문 단위 correction  <br>• Human expert labeling UI | • **Best-fit visualization 자동**  <br>• **Drill-anywhere**  <br>• Liveboards collaboration                 | • Real-time chart generation  <br>• Multi-step analysis progress  <br>• Forecasting execution status | • Search token architecture  <br>• SQL generation 표시  <br>• Data model to query translation                  | • Usage analytics dashboard  <br>• Cost/latency trade-off  <br>• SpotterCode IDE integration        | • Note tiles, cross filters  <br>• Verified Liveboards  <br>• In-app commenting                   | • Custom app embedding  <br>• REST API 다양한 연결  <br>• Multi-skilled agentic analytics                                     |
| **Glean**                              | • **No-code Agent Builder**  <br>• Glean Assistant (personalized)  <br>• Universal Knowledge (100+ connectors)  | • Natural language prompts  <br>• Quickstart templates  <br>• Multi-turn with context                  | • Agent testing 먼저  <br>• Human feedback integration  <br>• Permission-aware filtering        | • Structured + unstructured 통합  <br>• Enterprise Graph 시각화  <br>• Real-time search results                | • Workflow branching/looping  <br>• Multi-step execution tracking  <br>• Autonomous decision tree    | • **Adaptive planning 표시**  <br>• Tool selection 투명화  <br>• RAG relevance scoring                            | • Agent orchestration dashboard  <br>• Content-based triggers  <br>• Governance continuous scanning | • AI Apps gallery  <br>• Custom action buttons  <br>• Agent recommendation system                 | • **Remote MCP server** (agent protocol로 확장)  <br>• LangChain/OpenAI SDK/Bedrock  <br>• Cross-system agent collaboration |
| **Oracle Digital Assistant**           | • Skills-based architecture  <br>• Visual Flow Designer  <br>• Skill Store (repository)                         | • Intent-entity recognition  <br>• Multi-turn conversations  <br>• Context-aware responses             | • Expense approval workflows  <br>• Receipt photo + review  <br>• Policy compliance check     | • Oracle Cloud ERP dashboards  <br>• GPS tracking (Transportation)  <br>• Account reconciliation views    | • Dialog flow canvas  <br>• State transitions tracking  <br>• Composite bag resolution               | • Intent resolution confidence  <br>• Entity matching process  <br>• UnresolvedIntent trigger                | • Skill Tester evaluation  <br>• Point-and-click design  <br>• **Zero-shot multilingual NLU**       | • Unified for HR/ERP/CRM  <br>• Skill catalog management  <br>• Channel config (Teams/Slack)      | • REST/SOAP integration  <br>• Oracle Integration Cloud  <br>• Pre-built skills for Oracle SaaS                          |
| **Databricks Mosaic AI**               | • **Agent Evaluation Review App**  <br>• AI Playground (sandboxed)  <br>• Monitoring UI (production)            | • MLflow-based logging  <br>• Trace-based debugging  <br>• LangChain/LanGraph integration              | • **SME Review App** (외부 stakeholder)  <br>• Golden examples 정의  <br>• Human feedback loops   | • Evaluation metrics visualization  <br>• Cost/latency/quality trade-off  <br>• Root cause analysis views | • MLflow tracking UI  <br>• Deployment pipeline status  <br>• Model serving monitoring               | • **Detailed production traces**  <br>• AI judge grading (accuracy/groundness)  <br>• Compound AI components | • **Unity Catalog governance**  <br>• Rate limits/guardrails  <br>• Data lineage tracking           | • Agent Framework lifecycle  <br>• Tools Catalog (Unity Catalog)  <br>• Vector Search integration | • Lakeguard sandboxed execution  <br>• Multi-framework support  <br>• Unity Catalog across all agents                    |



- #### 메인 인터페이스 구성 
---
- **Microsoft Copilot for Dynamics 365**: Sidecar 방식
	- Copilot in Dynamics 365 Sales in full-screen view -> full-screen 채팅 종료
		```
		Effective September 2025, the full-screen view of Copilot in Dynamics 365 Sales is deprecated region-wise. After the deprecation, you can no longer select, view, or use Copilot option in app’s site map.  
		Alternatively, you may utilize the Copilot side pane for supported functions, allowing banner summaries to appear within context rather than in an immersive canvas. This approach minimizes context switching and aligns with the strategy of engaging sellers directly within grids and forms.
		```
	- [![[Pasted image 20251216193150.png]]](https://youtu.be/OP7oVMR1o1E)
- SAP Joule
	- SAP Start/Work Zone embedded
	- ![[Pasted image 20251216194205.png]](https://youtu.be/YtCA_Xjysb4?si=_9SHRc8_LXtv0rDE)
	- ![[Pasted image 20251216161334.png]]
- Salesforce - Agentforce
	-  3-Panel Layout (Steps/Config/Guidance)
	- ![[Pasted image 20251216195002.png]](https://youtu.be/V4TnJP-oCZ4?si=yTvw7j51ZRY4bwUC)
- Snowflake Intelligence
	- 독립 인터페이스
	- ![[Pasted image 20251216195440.png]](https://youtu.be/va-l7sYp3OA?si=aoW_UXg7MdLwJDol)
- Glean
	- ![[Pasted image 20251216200317.png]](https://www.glean.com/resources/product-videos/introducing-glean-work-ai-for-all)

| **구성**        | **특징**                                        | **장점**                                              | **단점**                                        |
| ------------- | --------------------------------------------- | --------------------------------------------------- | --------------------------------------------- |
| **패널형 구성**    | - 기존 애플리케이션 내 패널로 AI 기능 제공<br>- 퀵 액세스 및 지원 기능 | - 사용자 흐름의 연속성<br>- 직관적이고 친숙한 UI- 빠른 업무 처리           | - 복잡한 기능에 제한적<br>- UI가 과도하게 혼잡할 수 있음          |
| **독립된 화면 구성** | - 별도의 화면에서 AI 작업 처리<br>- 데이터 분석 및 복잡한 작업 가능   | - 강력한 데이터 분석 및 대규모 작업 처리<br>- 세밀한 제어 가능<br>- 유연성 높음 | - 애플리케이션과의 전환 필요<br>- 사용자 경험 분리<br>- 업무 흐름 단절 |
Dual-Pane Architecture (이중 패널 구조)

- Chat 홈
	- **Left/Bottom (Chat):** 자연어 대화 및 간단한 카드 뷰.
	- **Center/Right (Canvas):** 대화 결과로 생성된 **심층 리포트, 차트, 비교 분석 테이블**이 넓게 표시되는 영역.
	- claude
		- ![[Pasted image 20251216203521.png]]
	- snowflake intelligence
		- ![[Pasted image 20251216210716.png]]

- 대시보드
	- Dynamics 패턴처럼 **레코드 상단 요약/인사이트 + 사이드 패널 후속질의**를 기본으로.
	- ![[Pasted image 20251216204535.png]]
--- 

- #### 데이터 시각화 방식(드릴다운 방식)
---
- Google Looker Conversational Analytics
	- **Chat 입력 창:** 자연어 기반 질의 입력
	- **Visual Results Canvas:** 결과 차트, 테이블, 시각화 뷰 생성
	- ![[Pasted image 20251216202635.png]]
- ThoughtSpot Spotter
	- **Chat/Query 입력:** 자연어로 데이터 질문 입력
	- **Analytics Canvas:** 질의 결과를 기반으로 **차트, 표, 인사이트 대시보드**를 시각화하는 작업 공간
	- ![[Pasted image 20251216203055.png]]
	- ![[Pasted image 20251216203123.png]]
	- ![[Pasted image 20251216203152.png]]
	- ![[Pasted image 20251216205356.png]](https://www.youtube.com/watch?v=FnxdG591b0E)
	- ![[Pasted image 20251216210046.png]]
- Snowflake Intelligence
	- ![[Pasted image 20251216210537.png]]
---

- #### 에이전트 추론 과정 시각화
	- Snowflake
		- SQL 생성 및 실행 시각화
		- ![[Pasted image 20251216210510.png]]
- #### 대시보드 구성
	- 사용자 맞춤형 대시보드: 사용자가 직접 원하는 지표나 데이터 포인트를 선택하여 대시보드를 개인화할 수 있는 기능.
	- 사이드패널 후속 질의
	- Salesforce Einstein Copilot
		- ![[Pasted image 20251216211058.png]](https://www.salesforce.com/ap/form/conf/ai-demos/?leadcreated=true&redirect=true&sfuuid=828a48f1-8cfd-42bd-ae52-2fc7f1b3c7cf&tid=e186c3ab-6732-478b-ba80-3246c2e12021&chapter=&d=70130000000sUVq&player=&nc=7013y000002aTsYAAU&videoId=&playlistId=&utm_source=chatgpt.com)
	- ThoughtSpot - Spotter
		- 대시보드 특정 지표에 대한 질의 가능
		- **![[Pasted image 20251216211656.png]]**
		- ![[Pasted image 20251216211735.png]]
		- 드릴 다운, pin을 통한 대시보드 개인화
		- ![[Pasted image 20251216212005.png]](https://docs.thoughtspot.com/cloud/10.10.0.cl/spotter?utm_source=chatgpt.com)
- #### Human-in-the-loop
	- 에이전트가 계획을 수립하고 유저는 액션을 통해 계획을 검수 
	- ![[Pasted image 20251217083705.png]](https://youtu.be/9YYv3LesotU?si=j1Gldb2l8k5UWxa1)
	- 계획에 맞춰 Task 수행
	- ![[Pasted image 20251217084103.png]]
- 승인이 필요한 작업의 성격에 따라 완전히 다른 UI 렌더링
	- 예: 주식 구매는 카드, 이메일 발송은 프리뷰, 파일 삭제는 경고 모달
- 단순히 "승인하시겠습니까?"가 아닌 "왜 이 결정을 했는지" 시각화
- 대화 흐름 내에서 직접 승인
- #### 추가 기능
	- "Morning Briefing" 모드:
		- 앱 실행 시, 밤사이 변동된 주요 ERP 지표(자금 현황, 이슈 사항)를 **카드 뉴스 형태의 슬라이드 UI**로 먼저 브리핑하고 대화를 시작.
		- 오늘의 핵심 KPI, 이상징후(변동/리스크), 원인 Top 3, 추천 액션 Top 3
		- 각 카드마다 **“왜?” 버튼(드릴다운 질문 템플릿)** 제공 → ThoughtSpot 패턴.

#### 피드백
--- 
- 이번 달까지 UI / UX 리서치 계속 진행
- 리서치는 개발하면서도 계속 진행
- 최신 UI 기술을 모두 리스트업
- PIN 기능 좋음 → 이런게 엄청 많이 모여야 좋은 서비스가 됨
- 너무 PPT로 잘 정리해줄 필요 없음
- 운영 관리(관제) 필요할 것 같음. 기와에는 그런게 없어서 힘들었음. 대부분 에이전트 소프트웨어에서 사용하고 있을 것 같은데, 어떤 방식이 최선인지 생각 → 엄지 누르는건 신뢰성 문제가 있을 수 있음
- UI는 해외 사례를 찾되 UX는 국내 사례(더존 비즈온)을 조사해라
- **데이터 시각화 기능을 어떻게 구현할 지 생각 → 개발자가 다 정의, AI가 알아서 생성**
- **대시보드를 어떤 방식으로 보여주는 것이 효과적인지 생각**
- 지금은 뭘 써야할지 선택하는 단계가 아닌 뭐가 있는지를 최대한 많이 알아야하는 단계임