- MCP UI
- A2UI
- 대시보드
- 에이전트 성능 모니터링
- 문서 생성
- AI-Assisted Suggestion Patterns

### MCP UI
--- 
#### 정의 
- MCP(Model Context Protocol) 환경에서, AI 에이전트가 텍스트 응답 대신 **풍부한 인터랙티브 웹 컴포넌트**를 직접 반환할 수 있게 하는 프로토콜

#### 사용 예시
- MCP-UI 적용 전(왼쪽): 링크와 원시 변환이 포함된 스타일 없는 텍스트 블록
- MCP-UI 적용 후(오른쪽): 인터랙티브 카드 및 미리보기
	![[Pasted image 20251217162631.png]](https://block.github.io/goose/blog/2025/09/08/turn-any-mcp-server-mcp-ui-compatible/)
- MCP-UI 적용 전![[Pasted image 20251217163211.png]]
- MCP-UI 적용 후![[Pasted image 20251217163221.png]]
- UI 액션은 정적인 레이아웃을 에이전트와 상호작용할 수 있는 대화형 도구로 바꿔줍니다.
	 ![[462652379-7180c822-2dd9-4f38-9d3e-b67679509483.mp4]]
- MCP-UI Demos: https://mcp-aharvard.netlify.app/
- 데이터 시각화 활용
	- Goose AI Agent MCP-UI
		- ![[Pasted image 20251218132615.png]]
		- ![[Pasted image 20251218132658.png]]
		- ![[Pasted image 20251218132726.png]]
	- Goose Auto visualizer
		- ![[Pasted image 20251218140715.png]]
		- ![[Pasted image 20251218140727.png]]
		- ![[Pasted image 20251218140737.png]]

#### 기존 UI vs MCP UI

| 구분             | MCP UI ❌                                          | MCP UI ✅                                                     |
| -------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| **Tool 결과 형태** | • 텍스트/마크다운 표<br>• 이미지(차트 PNG)<br>• 외부 BI 링크       | • 텍스트 + UIResource(임베디드)<br>• `type: "resource"` 형태로 UI 포함   |
| **UI 렌더링 방식**  | • Host 앱이 자체 차트 라이브러리로 구현                         | • `UIResourceRenderer`가 `mimeType` 기반 자동 렌더링                 |
| **사용자 상호작용**   | • 대화로 "다시 물어보기" 형태<br>• 상호작용 제한적                  | • 클릭/선택 → `onUIAction`<br>• Agent가 tool 재호출<br>• UI 실시간 업데이트 |
| **드릴다운/필터**    | • Host가 별도 구현하지 않으면 불가능                           | • UI 내 직접 상호작용                                               |
| **표준화**        | ❌ 표준 흐름 없음<br>• 서비스마다 개별 구현                       | ✅ MCP 프로토콜 표준<br>• 일관된 구현 패턴                                 |
| **구현 부담**      | 🔴 높음<br>• 각 서비스가 시각화 로직 개별 개발<br>• UX 일관성 확보 어려움 | 🟢 낮음<br>• MCP Server가 UI 제공<br>• Host는 렌더러만 구현              |
| **주요 제약사항**    | • 가독성 한계<br>• 드릴다운 어려움<br>• UX 저하                 | • Sandboxed 환경 필요                                            |

#### 데이터 시각화 측면 장점
- **드릴다운/필터/정렬을 “대화”가 아니라 “직접 조작 UI”로 제공**
	- 텍스트만으로는 사용자가 KPI를 탐색할 때 “무엇을 클릭하면 다음이 나오는지”가 약합니다.
	- mcp-ui에서는 차트 막대 클릭, 범위 선택, 테이블 정렬 같은 액션을 **UI 이벤트로 표준 전달**하고, Agent가 이를 받아 다음 tool 호출로 연결하기 쉬워집니다.
- **“표준화된 렌더링 계약”으로 Host 구현 부담 감소**
	- Host가 매번 “이 tool 결과는 어떤 UI로 그릴까”를 개별 구현하면 비용이 커집니다. mcp-ui는 **UIResource + UIResourceRenderer** 패턴으로 “서버가 전달한 UI를 클라이언트가 공통 렌더러로 표시”하게 해, 여러 도구/서버에서 재사용 가능한 형태를 지향합니다.
	- e.g. 경영진: “MVNO 사업은 가입자/해지율을 ‘요금제 Mix’로 드릴다운하는 히트맵도 넣어주세요.”
		- mcp-ui 미사용
			- Host 프론트에 히트맵 컴포넌트 추가
			- tool 결과 스키마 확장에 맞춘 매핑 로직 추가
			- 드릴다운 이벤트/로딩 처리 추가
			- 배포/QA 범위 확대
		- mcp-ui 사용
			- MCP Server(tool) 쪽에서 `ui://kona/mvno-heatmap/...` UIResource를 반환하도록 확장
			- Host는 기존 `<UIResourceRenderer />`로 그대로 렌더
			- Host 변경이 필요하더라도 보통은 **공통 이벤트 핸들러(intent 처리)** 정도에서 끝남
- **맥락 전환 감소(외부 BI 링크로 튀지 않고 같은 화면에서 탐색)**
	- sandboxed iframe 로드로 **외부 앱을 ‘현재 앱 내부에서’ 안전하게 표시**하는 방향이어서, “링크 열고 돌아오기”보다 흐름이 덜 끊깁니다.
- **“결과 표현”이 데이터와 더 강하게 결합되어 오해를 줄이기 쉬움**
	- **의도 이벤트 → tool 재호출 → UI 업데이트**의 폐루프가 만들어지면, 사용자가 “근거 데이터/필터 조건”을 UI에서 명시적으로 조작하고 확인할 수 있어 해석 실수를 줄이는 UX를 설계하기가 유리
	- e.g. 코나아이 “부서별 전월 KPI 시각화”에 적용하면 생기는 차이
		- **미사용**: “전월 KPI 표 만들어줘 → 표/텍스트 → ‘DID만 더 보여줘’ 재질문 → 또 표”
		- **사용**: “전월 KPI 대시보드 UIResource 렌더 → DID 막대 클릭 → 드릴다운 tool 호출 → 같은 Canvas에서 즉시 갱신”


#### 외부 MCP UI 활용

➡️ 2025년 11월 21에 MCP UI가 공식 MCP 확장으로 표준화되어, 현재는 MCP UI를 지원하는 독립적인 MCP 서버가 많지 않지만 생태계가 확장 중이며 추후 외부 MCP UI 활용시 아래와 같은 이점이 있음

- **전문가가 만든 UI 품질** - 차트 라이브러리 전문 업체가 만든 인터랙티브 차트
- **개발 시간 절약** - PDF 렌더링, 지도 통합 등을 직접 구현하지 않음
- **유지보수 부담 감소** - 외부 서버가 업데이트하면 자동 반영
- **기능 확장 용이** - 새로운 MCP UI 서버 등장 시 즉시 활용

#### 전체 흐름
![[Pasted image 20251223140518.png]]
[![[Pasted image 20251218122340.png]]](obsidian://open?vault=Obsidian%20Vault&file=KonaChain%2FUI%2F%EB%A6%AC%EC%84%9C%EC%B9%98%2FDrawing%202025-12-18%2012.17.49.excalidraw)
[![[Pasted image 20251218160652.png]]](obsidian://open?vault=Obsidian%20Vault&file=KonaChain%2FUI%2F%EB%A6%AC%EC%84%9C%EC%B9%98%2FDrawing%202025-12-18%2015.52.04.excalidraw)

#### 참고 문서
- MCP-UI Documentation: https://mcpui.dev/guide/introduction
- MCP-UI Demos: https://mcp-aharvard.netlify.app/
- MCP-UI Demo GitHub: https://github.com/aharvard/mcp_aharvard
- MCP-UI GitHub: https://github.com/MCP-UI-Org/mcp-ui
- MCP-UI PlayGround: https://mcpui.dev/
- Goose Auto Visualiser with MCP-UI: 
	- https://block.github.io/goose/blog/2025/08/27/autovisualiser-with-mcp-ui
	- https://block.github.io/goose/docs/mcp/autovisualiser-mcp/#configuration
- Goose MCP-UI Extensions: https://block.github.io/goose/docs/guides/interactive-chat/mcp-ui/
- MCP Architecture: https://modelcontextprotocol.io/specification/2025-06-18/architecture
- @mcp-ui/server Usage & Examples: `createUIResource(rawHtml/externalUrl/remoteDom)` 예시: https://mcpui.dev/guide/server/python/usage-examples
- @mcp-ui/client Overview + HTML/RemoteDOM renderer: https://mcpui.dev/guide/client/overview
- https://www.thesys.dev/blogs/mcp-ui-overview
#### 서비스 예시: Shopify MCP UI
- 목적: **제품 이미지/갤러리, 옵션(사이즈·색상) 선택, 장바구니/체크아웃 플로우** 같은 상호작용을 텍스트만으로 처리할 때 생기는 UX 한계를 넘는 것
- https://www.youtube.com/watch?v=ZPo8n66_6-w
- UI 구성: 대화(채팅) 흐름 안에 “임베드된 인터랙티브 카드/패널”이 섞여 들어오는 형태
	- ![[Pasted image 20251217154054.png]]
	- 예를 들어 검색 결과는 단순 텍스트 리스트가 아니라, 아래 요소를 가진 “제품 카드 UI”로 나타날 수 있습니다.
		- 제품 이미지(여러 각도/갤러리)
		- 색상 스와치, 사이즈 셀렉터(옵션 연동)
		- 번들/구독 옵션(빈도 선택 등)
		- 재고/가격(로케일 반영)
		- Add to cart / Checkout 같은 CTA
- 사용자 인터렉션 -> 에이전트가 "중재"
		- 사용자가 대화에서 상품 검색을 요청
		- 에이전트가 “검색 결과 데이터”와 함께 “상품 카드 UI(`ui://...`)”를 반환
		- Host가 `ui://...`를 렌더링 (iframe/remote/remote-dom 중 하나)
		- 사용자가 카드에서 옵션 선택/버튼 클릭
		- **UI는 장바구니를 직접 바꾸지 않고**, “사용자가 장바구니 담기를 원한다”는 **Intent 메시지**를 Host로 보냄(보통 postMessage 기반)
		- Host(또는 에이전트)가 그 Intent를 해석해서 “진짜 장바구니 업데이트 tool 호출”을 수행
		- 결과를 다시 UI에 반영(성공/실패/로딩 등)
- 참고자료
	- https://shopify.engineering/mcp-ui-breaking-the-text-wall?utm_source=chatgpt.com

### A2UI(Agent to UI)
---
#### A2UI란?
- Google이 2025년 12월 15일에 공개적으로 발표한 오픈소스 프로토콜
- AI 에이전트가 텍스트 응답 대신 풍부하고 인터랙티브한 사용자 인터페이스를 선언적 JSON 형식으로 생성

#### 사용 예시
 - a2ui-custom-component
	 ![[a2ui-custom-compnent.mp4]]
 - landscape architect demo
	![[landscape-architect-demo 1.mp4]]
- Thesys C1 Playground: https://console.thesys.dev/playground
	- 드릴다운 분석
Create a hierarchical sales dashboard:
1. Overview level: Total sales by region (Asia, Europe, Americas)
2. When user clicks a region, show country breakdown
3. When user clicks a country, show city-level details

	- 폼 생성
		Generate a purchase order form with fields: Supplier Name, Product Category (dropdown: Electronics, Office Supplies, Raw Materials), Quantity (number), Unit Price, Expected Delivery Date, and a Submit button.

#### 핵심 개념 및 기술

대화 맥락에 따라 에이전트가 **그때그때 최적 UI를 조합**해 보내고, 호스트는 이를 네이티브로 렌더링

- 코드가 아니라 데이터로 UI를 전송
	- A2UI는 임의의 JS/HTML 실행 대신, **컴포넌트 설명(JSON데이터)**을 전송하고 **호스트는 정의된 네이티브 컴포넌트(버튼/카드/테이블/차트 등)**로 매핑해 렌더링
	- **에이전트**는 "어떤 위젯을 어떤 데이터로 조합할지"만 선언하고, 실제 실행은 호스트 앱이 통제하는 네이티브 코드로만 동작 ➡️ 보안 강화
- 스트리밍 메시지(대개 JSONL)와 점진 렌더링
	- A2UI는 UI를 한 번에 거대한 JSON 트리로 보내기보다, **여러 개의 JSON 메시지(보통 JSON Lines, JSONL)**를 순차 전송해 **점진적으로 화면을 완성**
	- LLM 생성에 유리하고(조각조각 생성), 사용자 입장에서도 “바로 그려지는” 체감 속도가 빠름
- LLM 친화적 구조(평면 컴포넌트 리스트/Adjacency List)
	- “중첩 트리”를 한 번에 완벽히 생성하기 어렵다는 점을 전제로, **ID 기반 참조가 가능한 평면(Flat) 컴포넌트 리스트(Adjacency List)** 설계
	- 데이터 업데이트 시 UI 전체를 다시 보낼 필요가 없고, 데이터 모델 업데이트로 최소 변경만 보낼 수 있도록 설계
	-  e.g.
		- 중첩 트리
			- ```json
			{
			  "surfaceId": "s1",
				  "root": {
					"type": "Column",
					"props": {
					  "children": [
						{
						  "type": "Text",
						  "props": {
							"text": "환영합니다"
						  }
						},
						{
						  "type": "Button",
						  "props": {
							"label": "확인",
							"action": {
							  "name": "submit"
				            }
				          }
				        }
				      ]
				    }
				  }
			}	  
				```
		- 평면 컴포넌트 리스트(Adjacency List)
			- ```json
			  {"surfaceUpdate":{"surfaceId":"s1","components":[
				  {"id":"root","component":{"Column":{"children":{"explicitList":["title","btn"]}}}},
				  {"id":"title","component":{"Text":{"text":{"literalString":"환영합니다"}}}},
				  {"id":"btn","component":{"Button":{"label":{"literalString":"확인"},"action":{"name":"submit"}}}}
				]}}
				{"beginRendering":{"surfaceId":"s1","root":"root"}} ＃렌더 시작점
				```
				```
- Diagram
	- ![[Pasted image 20251219103042.png]]
	- ![[Pasted image 20251219104034.png]]

#### 데이터 시각화 측면 장점
- **상호작용 차트/맵 같은 “커스텀 컴포넌트”를 호스트 카탈로그로 제공**하고, 에이전트가 상황에 따라 이를 선택해 응답(UI로 설명)
- **브랜드/디자인 시스템 일치**: 호스트가 네이티브 컴포넌트로 렌더링하므로, 시각화 UI가 앱과 “이질감 없이” 통합
- **드릴다운/필터링 루프가 자연스러움**: 사용자가 차트에서 구간 선택/필터 변경 → 액션이 에이전트로 전달 → 추가 질의/계산 후 UI 업데이트를 다시 스트리밍(“대화+시각화”의 고대역 상호작용)

#### MCP-UI와의 차이점

**두 접근은 모두 “대화형/시각적 UI”를 목표로 하지만, UI를 전달하는 형태와 실행 모델이 다릅니다.**

<관점별 비교>

| 관점          | A2UI                                      | MCP-UI                                                                              |
| ----------- | ----------------------------------------- | ----------------------------------------------------------------------------------- |
| UI 전달물      | **컴포넌트 설명 데이터(JSONL 메시지)**                | **UIResource**: `text/html`, `text/uri-list`, `application/vnd.mcp-ui.remote-dom` 등 |
| UI 스트리밍     | 네이티브 지원                                   | 제한적                                                                                 |
| 동적 업데이트     | **데이터 바인딩 + 데이터모델 업데이트**로 “부분 갱신”에 최적화    | 전체 HTML을 재로딩                                                                        |
| 실행 모델       | 원칙적으로 **임의 코드 실행 없음**(호스트가 가진 위젯으로 렌더)    | iframe 기반 **원격 코드 실행을 샌드박스에 격리**                                                    |
| 디자인 일관성     | 호스트 네이티브 위젯이므로 **브랜드·디자인 시스템 일치**가 비교적 쉬움 | HTML/URL 모드는 **이질감 가능**. Remote DOM은 호스트 컴포넌트 매핑으로 완화                               |
| 기존 웹 UI 재사용 | 가능은 하나, 네이티브 카탈로그/스키마 설계가 필요              | 이미 있는 대시보드/웹 폼을 HTML/URL로 빠르게 임베드 가능                                                |
| 안정성         | 낮음. 버튼 위치 이동, 색상 변경 시 실패 확률 존재            | 높음. UI가 변경되어도 내부 스키마만 같으면 유지됨.                                                      |

<장단점 비교>
- A2UI
	- 장점
		- LLM 생성에 맞춘 포맷: 중첩 트리 대신 Flat/Adjacency List + JSONL 스트리밍으로, **조각 생성 ➡️ 점진적 렌더링**
		- 프레임워크/플랫폼 독립성을 지향(여러 렌더러를 통한 네이티브 렌터)
	- 단점
		- 호스트 책임 부담: 카탈로그 정의, 위젯 레지스트리, 데이터 모델 스토어, 바인딩 리졸버 등 **렌더러 책임**이 큼
		- 웹 UI 재사용 어려움: 네이티브 컴포넌트로 매핑이 핵심이기 때문에 초기 투자(컴포넌트 설계)가 필요
		- **낮은 신뢰성:** 픽셀 단위의 변화, 로딩 지연, 팝업 등으로 인해 에이전트가 오작동할 확률이 높음
- MCP UI
	- 장점
		- 웹 UI 재사용 용이: `text/html`(raw HTML) 또는 `text/uri-list`(외부 URL)로 대시보드/폼을 빠르게 임베드
		- MCP 도구/서버 흐름과 결합: Tool이 UI까지 제공하는 형태. MCP Apps로 표준화 가능성 ➡️ 생태계 측면에서 확장 가능성이 큼
	- 단점
		- 디자인 일관성: HTML/URL 임베드는 호스트 디자인 시스템과 어긋나기 쉽고, Remote DOM이 이를 완화하지만 구현/제약 존재
		- 프레임워크/환경 제약 가능성: Remote DOM 접근은 React/Web Components 중심

#### 참고 문서
- https://a2ui.org/


### 대시보드
---

- 자연어 기반 대시 보드 생성
	- 기업의 데이터 소스, 업로드 파일(xlsx, csv)을 기반으로 대시보드 생성
	- SpotterViz Demo(2025.12.17): https://www.youtube.com/watch?v=q9_DJ6syFSo
	- ThoughtSpot Agentic MCP Server Demo(2025.07.29): https://www.youtube.com/watch?v=kiTpUPzgCbg
	- databricks dashborad: https://www.youtube.com/watch?v=dTH_WrFNM2g (11:17~)
- Navigating between tabs on a multi-tab dashboard
	- ![[graphic3.gif]]
	- ![[clone-page.gif]]
- AI forecasting
	- ![[line-forecasting.gif]]

### 에이전트 성능 모니터링
---

- 휴먼 피드백
	- ![[Pasted image 20251223172214.png]]
- Agentforce Moments 
	- [![[Pasted image 20251223130852.png]]](https://admin.salesforce.com/blog/2025/gain-complete-visibility-into-your-ai-agents-with-agentforce-optimization)
- W&B Weave
	- ![[Pasted image 20251223193949.png]]
	- ![[Pasted image 20251223193955.png]]
	- ![[Pasted image 20251223193959.png]]
- databricks
	- ![[image1_5.gif]]
- snowflake intelligence
	- ![[Pasted image 20251223194628.png]]
	- ![[Pasted image 20251223194633.png]]
	- ![[Pasted image 20251223194637.png]]
	- ![[Pasted image 20251223194641.png]]
### 문서 생성
---

- Thesys demo: https://demo.thesys.dev/chat?model=gpt-5&threadId=local-placeholder
	- PPT 생성![[화면 기록 2025-12-27 오후 8.37.27.mov]]
	- ![[화면 기록 2025-12-27 오후 8.45.17.mov]]
	- PPT 수정
		![[화면 기록 2025-12-27 오후 9.05.49.mov]]
	- 보고서 생성 및 수정
		![[화면 기록 2025-12-27 오후 8.52.00 1.mov]]

