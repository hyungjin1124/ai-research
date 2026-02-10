- MCP UI
- A2UI
- 대시보드
- 에이전트 성능 모니터링
- 문서 생성
- AI-Assisted Suggestion Patterns

### MCP UI
--- 
#### 정의 
- 정의: MCP(Model Context Protocol) 환경에서, 에이전트/툴이 “텍스트”가 아니라 “상호작용 가능한 UI”를 클라이언트에 표시하도록 요청하는 방식을 표준화하려는 SDK/프로토콜 묶음
- 목적: 클라이언트 애플리케이션 안에서 rich HTML 인터페이스를 표시(display) 요청하는 방법을 표준화

#### 사용 예시
- MCP-UI 적용 전(왼쪽): 링크와 원시 변환이 포함된 스타일 없는 텍스트 블록
- MCP-UI 적용 후(오른쪽): 인터랙티브 카드 및 미리보기
	![[Pasted image 20251217162631.png]](https://block.github.io/goose/blog/2025/09/08/turn-any-mcp-server-mcp-ui-compatible/)
- MCP-UI 적용 전![[Pasted image 20251217163211.png]]
- MCP-UI 적용 후![[Pasted image 20251217163221.png]]
- UI 액션은 정적인 레이아웃을 에이전트와 상호작용할 수 있는 대화형 도구로 바꿔줍니다.
	 ![[462652379-7180c822-2dd9-4f38-9d3e-b67679509483.mp4]]
- 데이터 시각화 활용
	- Goose AI Agent MCP-UI
		- ![[Pasted image 20251218132615.png]]
		- ![[Pasted image 20251218132658.png]]
		- ![[Pasted image 20251218132726.png]]
	- Goose Auto visualizer
		- ![[Pasted image 20251218140715.png]]
		- ![[Pasted image 20251218140727.png]]
		- ![[Pasted image 20251218140737.png]]

#### 무엇이 다른가?
- MCP UI ❌
	- **텍스트/마크다운 표**로 요약(가독성 한계, 드릴다운 어려움)
	- **이미지(차트 PNG) 반환** 또는 **외부 BI 링크** 제공(사용자 맥락 전환/상호작용 제한)
	- Host 앱이 별도의 차트 라이브러리로 **자체 렌더링**(각 tool마다 데이터 계약/렌더링 로직을 개별 구현해야 함)
	➡️“시각화 UI”는 가능하지만 **표준 흐름이 없어서** 서비스마다 구현 부담과 UX 일관성 문제가 생기기 쉽습니다(특히 드릴다운/필터/정렬 같은 상호작용)
	- ✳️요약
		- Tool 결과: 주로 텍스트/표/링크
		- UI 상호작용: 대화로 “다시 물어보기” 형태가 많음 ➡️ UX 저하
		- 드릴다운/필터: Host가 별도 구현하지 않으면 어렵고 일관성 낮음
- MCP UI ✅
	- MCP Server의 tool result `content` 안에 `type: "resource"`로 UI 리소스를 포함
	- Host는 `mimeType`에 따라 렌더링 방식을 결정(대표 3종):
	    - `text/html` : **Inline HTML → sandboxed iframe srcdoc**
	    - `text/uri-list` : **Remote resource URL → sandboxed iframe src**
	    - `application/vnd.mcp-ui.remote-dom` : **Remote DOM → 클라이언트에서 렌더**
	- iframe(또는 remote-dom) 안의 UI가 버튼 클릭/필터 변경 등을 하면 Host로 이벤트를 보내고(`onUIAction`), Host는 이를 해석해 **추가 tool 호출**로 이어가며, 그 결과를 다시 UI에 반영
	- ✳️요약
		- Tool 결과: 텍스트 + **UIResource(임베디드)**
		- UI 표시: `UIResourceRenderer`가 `mimeType` 기반으로 렌더
		- 사용자 상호작용: 클릭/선택 → `onUIAction` → Agent가 tool 재호출 → UI 업데이트
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
	- **의도 이벤트 → tool 재호출 → UI 업데이트**의 폐루프가 만들어지면, 사용자가 “근거 데이터/필터 조건”을 UI에서 명시적으로 조작하고 확인할 수 있어 해석 실수를 줄이는 UX를 설계하기가 유리합니다.
	- e.g. 코나아이 “부서별 전월 KPI 시각화”에 적용하면 생기는 차이
		- **미사용**: “전월 KPI 표 만들어줘 → 표/텍스트 → ‘DID만 더 보여줘’ 재질문 → 또 표”
		- **사용**: “전월 KPI 대시보드 UIResource 렌더 → DID 막대 클릭 → 드릴다운 tool 호출 → 같은 Canvas에서 즉시 갱신”


#### 핵심 개념

**툴 결과에 UIResource를 포함**시키고, Host는 **`UIResourceRenderer`가 mimeType에 맞춰 자동 렌더**하도록 하는 “표준 렌더링 계약”

- **UIResource: 서버가 클라이언트로 반환하는 주요 페이로드**
	- ```TypeScript
	  interface UIResource {
		  type: 'resource';
		  resource: {
		    uri: string; // 예: ui://component/id
		    mimeType: 'text/html' | 'text/uri-list' | 'application/vnd.mcp-ui.remote-dom';
		    // text/html: HTML 콘텐츠용
		    // text/uri-list: URL 콘텐츠용
		    // application/vnd.mcp-ui.remote-dom: remote-dom 콘텐츠용 (Javascript)
		    text?: string; // 인라인 HTML, 외부 URL, 또는 remote-dom 스크립트
		    blob?: string; // Base64로 인코딩된 HTML, URL, 또는 remote-dom 스크립트
		  };
}
	  ```
	- `uri`: 캐싱 및 라우팅을 위한 고유 식별자
	    - `ui://<component-name>/<instance-id>` — UI 리소스 (렌더링 방식은 mimeType에 의해 결정됨)
	- `mimeType`: 렌더링 방식을 결정
	    - `text/html`: HTML 콘텐츠 (iframe srcDoc)
	    - `text/uri-list`: URL 콘텐츠 (iframe src)
		    - `text/uri-list` 형식은 여러 URL을 지원하지만, MCP-UI는 **첫 번째 유효한 http/s URL**만 사용
	    - `application/vnd.mcp-ui.remote-dom`: remote-dom 콘텐츠 (Javascript), 클라이언트에서 직접 렌더링
	- `text` vs `blob`: 실제 HTML/URL/스크립트 payload
		- 간단한 문자열에는 text를 선택하고, 크거나 인코딩된 콘텐츠에는 blob을 사용
	- e.g. MVNO 요금제별 매출 시각화 - UIResource
		- ```html
		  {
		  "jsonrpc": "2.0",
		  "id": "call_101",
		  "result": {
			"content": [
			  {
				"type": "text",
				"text": "전월(2025-11) MVNO 요금제별 매출을 차트로 구성했습니다. 막대를 클릭하면 해당 요금제 드릴다운을 불러옵니다."
			  },
			  {
				"type": "resource",
				"resource": {
				  "uri": "ui://kona/mvno-plan-revenue/2025-11",
				  "mimeType": "text/html",
				  "text": "<!doctype html><html><style>body{font-family:sans-serif;margin:0} .wrap{padding:12px} ...</html>",
				  "_meta": {
					"initial_render_data": {
					  "month": "2025-11",
					  "title": "전월(2025-11) MVNO 요금제별 매출",
					  "series": [
						{ "planCode": "PLAN_A", "planName": "요금제 A", "revenue": 1820000000, "deltaPct": 3.2 },
						{ "planCode": "PLAN_B", "planName": "요금제 B", "revenue": 1450000000, "deltaPct": -1.4 },
						{ "planCode": "PLAN_C", "planName": "요금제 C", "revenue": 980000000, "deltaPct": 5.8 }
					  ]
					}
				  }
				}
			  }
			]
		  }
}

		  ```
- **Resource Renderer**: 서버가 보낸 UIResource를 클라이언트 측에서 실제 화면에 그려주는 렌더러
	- **`<UIResourceRenderer />`**: `mimeType`을 보고 내부적으로 HTML 또는 RemoteDOM 렌더러를 선택해 렌더링하는 “메인 컴포넌트”
	- **`<HTMLResourceRenderer />`**: `text/html`, `text/uri-list`를 `<iframe>`로 렌더링하며, 샌드박스/프록시/CSP 대응 및 메시징(onUIAction)을 담당
	- **`<RemoteDOMResourceRenderer />`**: `application/vnd.mcp-ui.remote-dom` 리소스를 Remote DOM 기반으로 렌더링(호스트 네이티브 룩앤필 통합)
- **React 컴포넌트 / Web Component**
	- MCP-UI는 클라이언트 렌더링을 위해 **React 컴포넌트(`UIResourceRenderer`)**와 **표준 Web Component(`<ui-resource-renderer>`)**를 함께 제공
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

- UI 구성: 대화(채팅) 흐름 안에 “임베드된 인터랙티브 카드/패널”이 섞여 들어오는 형태
	- ![[Pasted image 20251217154054.png]]
	- 예를 들어 검색 결과는 단순 텍스트 리스트가 아니라, 아래 요소를 가진 “제품 카드 UI”로 나타날 수 있습니다.
		- 제품 이미지(여러 각도/갤러리)
		- 색상 스와치, 사이즈 셀렉터(옵션 연동)
		- 번들/구독 옵션(빈도 선택 등)
		- 재고/가격(로케일 반영)
		- Add to cart / Checkout 같은 CTA
- 사용자 인터렉션 -> 에이전트가 "중재"
	- 버튼 클릭(예: Add to cart)이 **컴포넌트 내부에서 장바구니를 ‘직접’ 수정하는 게 아니라** intent를 올리고, 에이전트가 이를 받아 **MCP Tool 호출(예: cart 업데이트)**로 상태를 갱신하는 패턴입니다.
		- UI 컴포넌트(iframe 안의 버튼)가 장바구니를 ‘직접’ 바꾸면, 에이전트/호스트 입장에서는 상태가 꼬이기 쉽습니다.
		- 사용자 경험은 **시각적·직접조작(Direct Manipulation)**으로 좋아지고
		- “실제 상태 변경”은 에이전트가 통제하므로 **일관성과 안전장치**를 두기 쉬워집니다.
	- 흐름 예시
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
#### 정의 및 목적
- 정의: 에이전트가 UI를 말하게(speak UI) 하는 **선언형(declarative) 생성 UI 프로토콜**
- 목적: **원격/다기관 환경에서** HTML/JS를 그대로 실행하지 않고도, 텍스트 왕복 대신 **폼·차트·맵 같은 상호작용 UI**로 업무를 빠르게 처리

#### 사용 예시
 - a2ui-custom-component
	 ![[a2ui-custom-compnent.mp4]]

#### 핵심 개념 및 기술
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

#### 기존 UI와의 차이
- **전통적 UI**: 개발자가 화면 구조/상호작용 로직을 앱에 “고정” 구현(React/Flutter/Native).
- **A2UI**: 대화 맥락에 따라 에이전트가 **그때그때 최적 UI를 조합**해 보내고, 호스트는 이를 네이티브로 렌더링(스타일/보안 통제권은 호스트)

#### 데이터 시각화 측면 장점
- **상호작용 차트/맵 같은 “커스텀 컴포넌트”를 호스트 카탈로그로 제공**하고, 에이전트가 상황에 따라 이를 선택해 응답(UI로 설명)
- **브랜드/디자인 시스템 일치**: 호스트가 네이티브 컴포넌트로 렌더링하므로, 시각화 UI가 앱과 “이질감 없이” 통합
- **드릴다운/필터링 루프가 자연스러움**: 사용자가 차트에서 구간 선택/필터 변경 → 액션이 에이전트로 전달 → 추가 질의/계산 후 UI 업데이트를 다시 스트리밍(“대화+시각화”의 고대역 상호작용)

#### MCP-UI와의 차이점

**두 접근은 모두 “대화형/시각적 UI”를 목표로 하지만, UI를 전달하는 형태와 실행 모델이 다릅니다.**

<관점별 비교>

| 관점          | A2UI                                                                       | MCP-UI                                                                              |
| ----------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| UI 전달물      | **컴포넌트 설명 데이터(JSONL 메시지)**: `surfaceUpdate`, `dataModelUpdate` 등으로 점진 업데이트 | **UIResource**: `text/html`, `text/uri-list`, `application/vnd.mcp-ui.remote-dom` 등 |
| 실행 모델       | 원칙적으로 **임의 코드 실행 없음**(호스트가 가진 위젯으로 렌더)                                     | iframe 기반 **원격 코드 실행을 샌드박스에 격리**                                                    |
| 디자인 일관성     | 호스트 네이티브 위젯이므로 **브랜드·디자인 시스템 일치**가 비교적 쉬움                                  | HTML/URL 모드는 **이질감 가능**. Remote DOM은 호스트 컴포넌트 매핑으로 완화                               |
| 크로스플랫폼      | “동일 A2UI 페이로드를 여러 렌더러(Lit/Angular/Flutter 등)”로                             | 웹 임베드 성격이 강함(React/Web Components 중심 렌더러 언급)                                        |
| 업데이트/상태     | **데이터 바인딩 + 데이터모델 업데이트**로 “부분 갱신”에 최적화                                     | iframe/Remote DOM 내부 상태와 호스트 상태를 **메시지로 동기화**(postMessage/액션 콜백)                    |
| 기존 웹 UI 재사용 | 가능은 하나, 네이티브 카탈로그/스키마 설계가 필요                                               | **가장 강점**: 이미 있는 대시보드/웹 폼을 HTML/URL로 빠르게 임베드 가능                                     |

<장단점 비교>
- A2UI
	- 장점
		- LLM 생성에 맞춘 포맷: 중첩 트리 대신 Flat/Adjacency List + JSONL 스트리밍으로, **조각 생성 ➡️ 점진적 렌더링**
		- 프레임워크/플랫폼 독립성을 지향(여러 렌더러를 통한 네이티브 렌터)
	- 단점
		- 호스트 책임 부담: 카탈로그 정의, 위젯 레지스트리, 데이터 모델 스토어, 바인딩 리졸버 등 **렌더러 책임**이 큼
		- 웹 UI 재사용 어려움: 네이티브 컴포넌트로 매핑이 핵심이기 때문에 초기 투자(컴포넌트 설계)가 필요
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
	- databricks dashborad: https://www.youtube.com/watch?v=dTH_WrFNM2g (11:17~)
	- https://youtu.be/RcWLQqj8pfw?si=z-XtAtKPp0zA1eTN
- side bar 질의
	- https://help.agencyanalytics.com/en/articles/9797349-ask-ai
- Navigating between tabs on a multi-tab dashboard
	- ![[graphic3.gif]]
	- ![[clone-page.gif]]
- AI forcasting
	- ![[line-forecasting.gif]]

### 에이전트 성능 모니터링
---

- 휴면 피드백
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

- PPT
	- Thesys demo: https://demo.thesys.dev/chat?model=gpt-5&threadId=local-placeholder

### AI-Assisted Suggestion Patterns
---
 - Follow-up chips(추가 질문 버튼)
	- MS copilot
		- ![[Pasted image 20251223142000.png]]
- Suggested prompt(추천 질문/명령어)
	- ![[Pasted image 20251223150037.png]]
	- ![[Pasted image 20251223144113.png]]
- UI 패턴 모음: https://www.aiuxplayground.com/patterns?q=follow


