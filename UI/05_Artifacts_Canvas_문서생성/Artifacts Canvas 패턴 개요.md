# Layout 패턴
---
•	Side Panel: 대화와 분리된 전용 영역, 버전 관리 용이 (Claude, Gemini)
	•	Inline Expandable: 대화 흐름 내 확장 가능 영역, 직접 편집 지원 (ChatGPT Canvas)

vercel - v0![[Pasted image 20260122175523.png]]

•	Full-Screen Takeover: 복잡한 대시보드나 앱 실행 시 전체 화면 점유 (Manus)
* https://manus.im/share/CXARwKT84KlXT4pFTcQ8Og?replay=1
•	Embedded Widget: 외부 애플리케이션 내 임베딩 (ThoughtSpot, AgentForce)

# Interaction 패턴
---
•	Iterative Refinement: 대화를 통한 점진적 수정 요청 (모든 서비스)
•	Highlight-to-Edit: 특정 영역 선택 후 수정 지시 (Claude, ChatGPT, Gemini)
![[Pasted image 20260122175116.png]]
![[Pasted image 20260122175124.png]]
•	Direct Manipulation: 사용자가 직접 편집 가능 (ChatGPT Canvas, v0 Annotation Mode)
•	Drill-Down: 데이터 시각화에서 상세 분석으로 이동 (ThoughtSpot, Snowflake)
•	Action Trigger: Artifact에서 외부 시스템 액션 실행 (AgentForce, Spotter)

# Trigger 패턴
---
•	자연어 문맥 감지: 콘텐츠 길이, 복잡성, 재사용 가능성 기반 자동 판단 (Claude 'antthinking')
•	명시적 명령: 슬래시 커맨드(/canvas), 버튼 선택, 키워드 트리거 ('use canvas')
•	데이터 변경 트리거: 특정 조건 충족 시 자동 Artifact 생성 (Salesforce AgentForce)
•	후속 분석 연쇄: 기존 Artifact에서 드릴다운/필터링 시 새 Artifact 생성 (ThoughtSpot)

# Persistence 패턴
---
•	Session-based: 대화 세션 내에서만 유지
•	Account-linked: 사용자 계정에 저장, 세션 간 접근 가능 (대부분의 서비스)
•	Shareable Link: 퍼블릭 링크 생성으로 외부 공유 (Claude, Gemini, Manus)
•	Versioned: 버전 히스토리 유지, 롤백 가능 (Claude, ChatGPT)
![[Pasted image 20260122175233.png]]
![[Pasted image 20260122175240.png]]
•	Persistent Storage API: 세션 간 데이터 저장 (Claude window.storage)
•	External Integration: 외부 시스템(Google Docs, Salesforce)과 동기화
