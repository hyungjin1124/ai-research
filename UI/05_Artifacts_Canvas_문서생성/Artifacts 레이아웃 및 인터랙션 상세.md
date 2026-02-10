## Layout 패턴

- Side Panel: 대화와 분리된 전용 영역, 버전 관리 용이 (Claude, Gemini, ChatGPT, vercel v0)
    - Claude
	    ![[Pasted image 20260123085309.png]]
	- Gemini
	    ![[Pasted image 20260123085932.png]]
- Full-Screen Takeover: 복잡한 대시보드나 앱 실행 시 전체 화면 점유 (Manus)
	![[Pasted image 20260123090009.png]]
	![[Pasted image 20260123090048.png]]
- 답변 흐름 중간에 삽입 (ThoughtSpot)
	- ThoughtSpot Spotter
		![[Pasted image 20260123090159.png]]
		![[Pasted image 20260123090218.png]]

		* https://youtu.be/SOZPuu7tjzY?si=jrotsVojy4mL3Nca (1:45~)
	- Gemini3 in AI mode
		![[Pasted image 20260126083222.png]]
		- https://x.com/i/status/2014107136465227875
		- https://x.com/i/status/2013684372033900557
---
## Interaction 패턴

- Iterative Refinement: 대화를 통한 점진적 수정 요청
- Region-based Prompting: 시각적 영역 선택 후 AI 질의
	![[20260126-0052-46.9326058.mp4]]
    
- Highlight-to-Edit: 특정 영역 선택 후 수정 지시 (Claude, ChatGPT, Gemini)
	![[Pasted image 20260123091258.png]] ![[Pasted image 20260123091328.png]]
- Direct Manipulation: 사용자가 제한적 편집 가능 (ChatGPT Canvas, v0 Annotation Mode)
	- Manus: https://manus.im/share/EJ0ET35km9bubiQSmgOJXn
    
- Drill-Down: 데이터 시각화에서 상세 분석으로 이동 (ThoughtSpot, Snowflake)
    - ThoughtSpot: 
	    - https://youtu.be/0yRxIqUI00M?si=af7aPBHxo0MMNCos&t=80
-  Gemini: https://x.com/i/status/2014020819173687626

---

## Artifact Trigger 패턴

- 자연어 문맥 감지: 콘텐츠 길이, 복잡성, 재사용 가능성 기반 자동 판단
	- Claude Artifacts: 콘텐츠 유형을 자동 감지하여 React 컴포넌트는 라이브 인터랙션으로, HTML은 실시간 미리보기로, 코드는 구문 강조로 렌더링
	- ChatGPT Canvas: 10줄 이상의 콘텐츠 생성 시 또는 글쓰기/코딩에 유용한 시나리오 감지 시 자동 열림
    
- 명시적 명령: 슬래시 커맨드(/canvas), 버튼 선택, 키워드 트리거
	- ChatGPT Canvas
		- "use canvas", "open a canvas", "open a coding canvas" 프롬프트 또는 백슬래시(/) 명령어로 수동 활성화

---
## Presentations
### Presenton
* 사용자의 pptx를 업로드하면 AI가 파싱하여 템플릿으로 저장
* 저장된 템플릿을 활용하여 새로운 pptx 생성 가능
* https://presenton.ai/
* https://youtu.be/vvCj23ySjLg?si=IGasp4tk4TxEX5Ty

#### Genspark
- PPT 생성 데모: https://www.genspark.ai/agents?id=f37837b4-184c-49d0-828a-8f2db216132f
- ![[genspark PPT 생성 데모.zip]]

## Excel
### Claude in Excel
* https://x.com/claudeai/status/2014834616889475508?s=20
![[Pasted image 20260126091324.png]]
---

## Artifacts 구성 요소
| 구성 요소                    | 설명               | 적용 플랫폼                              |
| ------------------------ | ---------------- | ----------------------------------- |
| **Inline Editing**       | 결과물 내 직접 편집      | Claude, ChatGPT, Gemini             |
| **Section Selection**    | 특정 부분 선택 후 AI 명령 | Claude, ChatGPT, Gemini, Jasper     |
| **Version History**      | 이전 버전 복원         | ChatGPT Canvas, Notion              |
| **Real-time Preview**    | 실시간 렌더링          | Claude, ChatGPT, Gemini, v0, Replit |
| **Export/Share**         | 외부 공유 및 내보내기     | 모든 플랫폼                              |
| **Multi-Model Support**  | 여러 AI 모델 선택      | Notion, LibreChat, Cursor           |
| **Collaboration**        | 다중 사용자 동시 편집     | Copilot Pages, Perplexity, Replit   |
| **Memory/Context**       | 세션 간 컨텍스트 유지     | Claude, ChatGPT, Notion Agents      |
| **Tool/API Integration** | 외부 도구 연동         | MCP 지원 플랫폼들                         |


