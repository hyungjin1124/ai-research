#### 입력 전
![[Pasted image 20260203084852.png]]
초기 대기 화면. "할 일을 저와게 볼까요?" 메시지와 함께 추천 작업 버튼(자료 정리, 이메일 초안, 보고서/프레젠테이션, 파일 정리, 요약 분석, 클립보드에서 작업 등)이 표시됨. 우측에는 문맥 설정, 작업 폴더, 참페노트 선택 패널이 위치.

#### 스킬 및 폴더 탐색
![[Pasted image 20260203091730.png]]
사용자가 주간 경영 브리핑 프레젠테이션 생성을 요청한 후, Claude가 폴더 구조를 탐색하며 관련 파일(.pptx, .md 등)을 확인하는 과정. 체크박스와 함께 탐색된 파일 목록이 단계별로 표시되며, 하단에 "생각 중..." 상태 표시.

#### Human-In-The-Loop
![[Pasted image 20260203091835.png]]
3패널 레이아웃: 좌측 채팅 영역에서 작업 진행 상황이 표시되고, 중앙에는 Pygments 코드 Artifact가 렌더링됨. 하단에 질문과 함께 선택지(수정/예상 공제, 건너뛰기 등)를 제공하는 Human-In-The-Loop 다이얼로그 표시.

#### Markdown Artifacts 3-Panel
![[Pasted image 20260203091928.png]]
3패널 구성: 좌측 채팅 히스토리, 중앙 Markdown Artifact(Pygments 문법 가이드 - Common Pitfalls, Quick Reference 등), 우측 파일 트리(Demo_2 폴더 내 .png, .md 파일 목록). 각 파일의 용량 정보도 함께 표시.

#### Thinking & 진행 상황 업데이트
![[Pasted image 20260203092041.png]]
실시간 작업 진행 화면: 좌측에서 Claude의 사고 과정과 세부 작업 로그가 표시됨. 우측 패널에는 관련 파일 목록과 진행률 바가 시각적으로 표시되어 작업 완료 상태 확인 가능.

#### 웹 검색 Tool call
![[Pasted image 20260203092310.png]]
웹 검색 도구 호출 결과 화면: Credit Card Metal 관련 검색어로 다수의 웹 결과가 목록 형태로 표시됨. 각 결과에는 제목, URL, 간략한 설명이 포함되며, Claude가 관련성 높은 정보를 선별하여 요약 제공.

#### 웹 검색 과정 Artifacts
![[스크린샷 2026-02-03 오전 9.23.42.png]]
3패널 웹 검색 뷰: 좌측 채팅 영역에 검색 요약 및 분석 결과, 중앙 "웹 검색" Artifact에 카테고리별로 정리된 검색 결과(Comprehensive, CPI Card Group, Global 등), 우측 파일 트리. 검색 결과가 구조화되어 시각적으로 정리됨.

#### PPT Artifacts 2-Panel
![[Pasted image 20260203092944.png]]
2패널 PPT 미리보기: 좌측 채팅에서 작업 진행 로그와 Human-In-The-Loop 메시지가 표시되고, 우측에 생성된 "회장님 주간 경영 브리핑" PPT가 Microsoft PowerPoint에서 렌더링됨. Executive Summary 슬라이드에 주요 지표(주간 매출 8.2억원, 매출증가율 38.6% 등) 표시.

#### PPT Artifacts 3-Panel
![[Pasted image 20260203093130.png]]
3패널 PPT 편집 뷰: 좌측에 프레젠테이션 구성 테이블(슬라이드별 내용 정리), 중앙 PPT 미리보기(Executive Summary), 우측에 슬라이드 목차 패널. Claude가 PPT 내용을 설명하며 수정 제안을 제공하는 협업 화면.

#### 데이터 시각화 Artifacts 2-Panel
![[Pasted image 20260203093223.png]]
2패널 대시보드 뷰: 좌측 채팅 영역에 데이터 분석 테이블(경쟁사 조사 결과), 우측에 "데이터 시각화 대시보드" Artifact. 다크 테마로 총 매출(₩822.4M), 순이익(₩317.1M), 고객 수(663건) 등 KPI 카드와 라인 차트, 바 차트, 도넛 차트가 시각적으로 표시됨.

#### 데이터 시각화 Artifacts 3-Panel
![[Pasted image 20260203093159.png]]
3패널 대시보드 뷰: 좌측 채팅/테이블, 중앙 대시보드(판매 분석 - sales_export.csv 기반), 우측 Google Coworkit 패널. 월별 매출 추이, 카테고리별 매출, 지역별 매출 구성 등 다양한 차트가 인터랙티브하게 표시되는 전체 화면 구성.
