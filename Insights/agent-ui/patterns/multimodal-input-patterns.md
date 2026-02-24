---
type: research-brief
topic_id: multimodal-input-patterns
topic_name: 멀티모달 입력 UI 패턴
category: conversational-ui-patterns
document_level: intermediate
parent_broad:
  - conversational-ui-patterns
catalog_components:
  - chat_input
  - file_attachment
  - drag_drop
  - context_chips
tags:
  - multimodal
  - file-upload
  - drag-and-drop
  - context-injection
  - ux-patterns
status: active
confidence: high
last_updated: 2025-02-15
source_products:
  - ChatGPT
  - Claude
  - Google-Gemini
  - Cursor
  - Manus-AI
auto_update: quarterly
relevant_roles:
  - frontend-engineer
  - ux-designer
  - ai-product-manager
---

# 멀티모달 입력 UI 패턴

## TL;DR

- **첨부 바(Attachment Bar) vs 인라인 칩(Inline Chips)**: ChatGPT는 입력 필드 하단에 첨부 미리보기 표시(공간 절약), Claude는 입력 필드 내부에 칩 형태로 표시(컨텍스트 시각화)[^1][^2]
- **드래그앤드롭 설계**: ChatGPT/Claude는 입력 전체 영역을 드롭 존으로 활용. Cursor는 코드베이스 대상 명시(루트 폴더만). Gemini는 네이티브 멀티모달 지원으로 별도 UI 최소화[^2][^3]
- **파일 유형 검증**: 모든 제품이 클라이언트 사이드 검증(허용된 확장자/MIME type 체크). 이미지는 PNG/JPEG/GIF, 문서는 PDF/DOCX/TXT 등으로 제한[^1]
- **컨텍스트 칩(@mentions)**: Cursor의 @file, @folder가 표준화. Claude는 Projects 시스템에서 파일 칩 표시. KonaI-Agent는 @data, @liveboard 같은 도메인 특화 칩 가능[^2][^3]
- **입력 영역 확장 동작**: 파일 추가 시 textarea auto-resize는 기본. 여러 첨부 시 가로 스크롤 바 또는 그리드 표시[^1][^2]

## Overview

멀티모달 입력은 사용자가 텍스트뿐 아니라 파일(이미지, 문서, 코드), 웹 링크, 프로젝트 컨텍스트 등을 함께 제공할 수 있게 하는 UI 패턴이다. 현대 AI 채팅 인터페이스에서는 거의 필수 기능이며, 특히 코드 분석, 이미지 이해, 대용량 문서 처리 시나리오에서 필수적이다.

다섯 가지 멀티모달 입력 방식이 존재한다:
1. **파일 첨부 + 드래그앤드롭(기본)**: 버튼 클릭 또는 끌어서 놓기로 파일 추가
2. **클립보드 붙여넣기(이미지)**: Ctrl+V로 이미지 직접 입력
3. **컨텍스트 칩(@mentions)**: 기존 파일, 폴더, 프로젝트 참조
4. **웹 검색 토글(ChatGPT)**: 실시간 정보 수집 활성화/비활성화
5. **카메라 입력(Gemini 모바일)**: 스마트폰 카메라로 직접 사진 촬영

KonaI-Agent는 현재 텍스트 입력만 지원하므로, 파일 첨부와 컨텍스트 칩 추가가 우선순위.

## 경쟁사 구현 분석

### 비교 매트릭스

| 제품 | 파일 첨부 | 드래그앤드롭 | 이미지 클립보드 | 컨텍스트 칩 | 웹 검색 | 카메라 입력 | 예상 공간(상태) |
|------|---------|-----------|-------------|-----------|--------|-----------|------------|
| ChatGPT | ✓ | ✓ | ✓ | ✓ (web search) | ✓ | ✓ (mobile) | 상단 + 하단 |
| Claude | ✓ | ✓ | ✓ | ✓ (@Projects) | ✗ | ✗ | 인라인 + 우측 |
| Gemini | ✓ (native) | ✓ | ✓ | ✓ (@mentions) | ✓ | ✓ | 최소 (native) |
| Cursor | ✓ (@file/@folder) | ✓ | ✗ (코드 중심) | ✓ | ✗ | ✗ | 인라인 |
| Manus AI | ✓ | ✓ | ✗ | 제한적 | ✗ | ✗ | 하단 바 |

### 경쟁사별 상세 분석

#### ChatGPT: 모달형 첨부 바 + Web Search 토글

**구현 방식**:
- 파일 첨부 버튼(클립 아이콘): 클릭 → 파일 선택 모달 열기. 한 번에 최대 10-20개 파일 선택 가능[^1]
- 드래그앤드롭: 입력 필드 또는 전체 채팅 영역에 파일을 끌어서 놓으면, 자동으로 첨부 목록에 추가
- 이미지 클립보드: Ctrl+V (또는 Cmd+V)로 클립보드의 이미지 직접 붙여넣기
- 첨부 미리보기: 입력 필드 하단에 작은 썸네일 또는 파일명 칩 표시. 각 칩 우측에 X 버튼으로 제거 가능
- Web Search 토글: 입력 필드 좌측에 "검색" 아이콘. 클릭 시 스트리밍 응답 시 웹 검색 결과 포함[^1]
- 파일 크기 제한: 2025년 업데이트로 더 큰 파일 지원(이전 20MB → 현재 제한 확대)

**왜 이 방식인가**:
- 입력 필드 높이 증가 방지(하단 바로 분리)
- 여러 파일 선택 UI가 모달이므로 스크린 정렬 명확
- Web Search 토글은 간단한 아이콘으로 차지하는 공간 최소
- 사용자가 "이 질문을 인터넷 검색으로 강화하고 싶다"는 의도 명확

**참고**: [ChatGPT Drag-and-Drop 가이드](https://www.pageon.ai/blog/chatgpt-drag-and-drop) | [ChatGPT Image Upload FAQ](https://help.openai.com/en/articles/8400551-image-inputs-for-chatgpt-faq)

#### Claude: 인라인 칩 + Projects 파일 시스템

**구현 방식**:
- 파일 첨부: 클립 버튼 또는 입력 필드에 직접 드래그앤드롭(Shift+drop은 파일경로 자동 삽입)
- 첨부 칩: 입력 필드 내부에 작은 태그 형태로 표시(예: "[document.pdf] [code.tsx]"). 각 칩을 클릭하면 미리보기 또는 제거 가능[^2]
- Projects 통합: Projects 메뉴에서 기존 업로드 파일을 "파일 칩"으로 참조 가능. 한 번 업로드한 파일은 여러 대화에서 재사용 가능
- 파일 크기: 최대 30MB 파일 지원, 동시 최대 20개 파일[^2]
- @ 메서드: `@Claude` 등으로 모델 설정 참조 가능(Claude 3.5, Claude 3 등)

**왜 이 방식인가**:
- 인라인 칩으로 "지금 이 대화에 어떤 파일이 포함되어 있나" 시각적으로 명확
- Projects 시스템으로 파일 재사용성 높임(Upload → Project에 저장 → 향후 대화에서 참조)
- 드래그앤드롭 후 Shift를 누르면 경로 자동 삽입되므로, 코드 분석 작업에 최적
- @ 시스템은 추후 @Knowledge, @CustomInstruction 같은 확장 가능

**참고**: [Claude File Upload Guide](https://support.claude.com/en/articles/8241126-uploading-files-to-claude) | [Claude Code File References](https://stevekinney.com/courses/ai-development/referencing-files-in-claude-code)

#### Google Gemini: 네이티브 멀티모달 설계

**구현 방식**:
- 파일 첨부: 음성, 이미지, 비디오, 파일을 모두 동일한 인터페이스로 처리(별도 UI 최소화)[^4]
- 드래그앤드롭: 입력 필드에 이미지/동영상/파일 끌어서 놓으면 즉시 미리보기
- 카메라 입력(모바일): 음성/카메라 아이콘으로 직접 촬영 가능
- 컨텍스트 멘션: `@query` 같은 형태로 이전 응답 참조 또는 외부 정보 포함
- Dynamic View와 연계: 업로드된 이미지/문서를 기반으로 즉시 Interactive UI 생성[^3]

**왜 이 방식인가**:
- Google AI는 처음부터 멀티모달(음성, 시각, 텍스트) 모델 기반이므로, UI도 멀티모달 우선
- 하나의 입력 영역에서 모든 타입 지원으로 학습곡선 낮춤
- Dynamic View와 결합하여 이미지 → 시각화 생성 워크플로우 자연스러움
- 모바일 우선 설계이므로 카메라, 음성 입력 기본 지원

**참고**: [Gemini Visual Layout Guide](https://support.google.com/gemini/answer/16741341)

#### Cursor: 코드 컨텍스트 주입(@file/@folder/@docs)

**구현 방식**:
- @file: 특정 파일 경로 입력 시(예: `@src/App.tsx`), Cursor가 해당 파일 전체 또는 청크를 AI 컨텍스트에 포함[^3]
- @folder: 폴더 경로 입력 시(예: `@src`), 해당 폴더의 파일 구조와 주요 파일 포함. 대규모 폴더는 자동으로 축약
- @docs: 외부 문서 URL 또는 로컬 README 참조. AI가 문서를 읽고 답변에 반영[^3]
- @code/@symbols: 특정 함수, 클래스, 변수 명시적 참조
- 드래그앤드롭: 파일을 채팅 창에 끌어서 놓으면 자동으로 @file 태그 생성
- 예상 공간: 입력 필드 아래에 자동완성 메뉴로 @file/@folder 옵션 제시

**왜 이 방식인가**:
- 코드 에디터 문맥에서 "파일 경로"는 자연스러운 참조 방식
- @symbol은 IDE의 "Go to Definition" 개념을 AI에 적용
- 대규모 폴더 자동 축약으로 context window 낭비 방지
- Cursor Index(벡터화)와 결합하여 관련 파일만 자동 선택[^3]

**참고**: [Cursor Context Management](https://stevekinney.com/courses/ai-development/cursor-context) | [Cursor Codebase Indexing Guide](https://eastondev.com/blog/en/posts/dev/20260115-cursor-codebase-index-guide/)

#### Manus AI: 간단한 파일 첨부 + 작업 설명

**구현 방식**:
- 파일 첨부: 클립 버튼 또는 드래그앤드롭으로 파일 추가
- 첨부 바: 입력 필드 하단에 파일 미리보기 표시
- 작업 설명: 텍스트 + 파일을 함께 입력하면, AI가 파일 분석 + 설명된 작업 수행
- 최소 UI: 컨텍스트 칩이나 복잡한 설정 없음. "파일을 드롭하고 질문하기"의 단순성 추구

**왜 이 방식인가**:
- 작업 자동화(특히 이미지 처리, 문서 변환) 중심 제품이므로, 파일 + 작업 설명 조합 최우선
- 복잡한 컨텍스트 관리 불필요(한 번에 처리 후 끝)
- UI 단순성으로 초보 사용자도 쉽게 사용

## 패턴 분류 및 트레이드오프

### 패턴 A: 모달형 파일 선택(ChatGPT)

**대표 제품**: ChatGPT

**장점**:
- 입력 필드 높이 증가 없음
- 여러 파일 선택 UI 명확(파일 탐색기와 유사)
- 첨부 미리보기가 깔끔(하단 바)

**단점**:
- 드래그앤드롭이 이미 있으면 모달은 중복
- 파일 제거 시 별도 UI 클릭 필요
- 모바일에서 모달 크기 조절 어려움

**적합한 상황**:
- 드래그앤드롭을 모르는 일반 사용자 배려
- 대량 파일 선택(10개 이상)
- 모바일 사용자가 많은 경우

### 패턴 B: 인라인 칩(Claude)

**대표 제품**: Claude

**장점**:
- 입력 필드와 첨부 파일의 관계 시각적으로 명확
- 칩을 클릭하면 미리보기 가능
- 컨텍스트 이력 저장(Projects)으로 재사용성 높음

**단점**:
- 여러 파일 시 입력 필드가 커짐
- 작은 화면에서는 가로 스크롤 필요
- 칩 UI가 복잡할 수 있음

**적합한 상황**:
- 사용자가 "어떤 파일을 지금 보내는가" 명확히 알고 싶을 때
- 파일 재사용(Projects)이 중요할 때
- 데스크톱 중심 사용

### 패턴 C: 네이티브 멀티모달(Gemini)

**대표 제품**: Gemini

**장점**:
- 음성, 이미지, 동영상, 파일을 통일된 UI로 처리
- 모바일 우선(카메라, 음성)
- 학습 곡선 낮음

**단점**:
- 텍스트 입력과 파일 첨부의 경계 불분명할 수 있음
- 처음부터 멀티모달 모델이 필요(GPT-4/Claude에는 최적화 아님)
- Dynamic View 의존도 높음

**적합한 상황**:
- 멀티모달 모델 기반 서비스
- 모바일 우선 앱
- 비전 + 음성 + 텍스트가 동일한 가치

### 패턴 D: 코드 컨텍스트 주입(@mentions - Cursor)

**대표 제품**: Cursor

**장점**:
- 파일 경로를 이미 알고 있는 개발자에게 직관적
- Context window 최적화(자동 선택)
- 폴더 레벨 접근으로 대규모 코드베이스 관리 용이

**단점**:
- 파일 경로를 알아야 함(초보자 진입장벽)
- @ 메뉴 자동완성 필수(그렇지 않으면 복잡)
- 코드 전용(일반 파일 처리 약함)

**적합한 상황**:
- 개발자 중심 도구
- 대규모 코드베이스 분석
- IDE 통합

### 트레이드오프 요약 테이블

| 기준 | 모달형 | 인라인 칩 | 네이티브 멀티모달 | 코드 @mentions |
|------|--------|---------|----------|----------|
| UI 공간 효율 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 시각적 명확성 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 초보자 친화성 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| 파일 재사용성 | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 드래그앤드롭 경험 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 멀티모달 확장성 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상태

| 자산 | 위치 | 현황 | 재사용 가능성 |
|------|------|------|------------|
| Textarea + Auto-resize | ChatInterface.tsx | 구현됨 | 100% |
| Context Chips 표시 UI | ChatInterface.tsx | 부분 구현 | 60% |
| Drag-drop 감지 | 없음 | 미구현 | 0% |
| 파일 첨부 버튼 | 없음 | 미구현 | 0% |
| 파일 미리보기 | 없음 | 미구현 | 0% |
| Brand Color 적용 | 전체 | 적용됨 | 100% |
| 3-panel 레이아웃 | GeneralChatView | 구현됨 | 100% |

### 권장 접근

**선택안: 인라인 칩 + 드래그앤드롭 + @컨텍스트 멘션**

Claude의 인라인 칩 패턴을 기본으로 하되, Cursor의 @컨텍스트 멘션을 KonaI-Agent 도메인에 맞게 변형. 세 단계 구현으로 진행.

**초기 단계(v1 - 파일 첨부 기본)**: 
- Textarea 하단에 "Attach files" 버튼 추가(클립 아이콘)
- 드래그앤드롭 구현(dropzone overlay)
- 첨부된 파일을 인라인 칩으로 입력 필드 상단 또는 내부에 표시
- 파일 타입 검증(이미지: PNG/JPG/GIF, 문서: PDF/TXT/JSON/CSV)
- 파일 크기 제한(초기 5MB, 향후 20MB)
- 비용: 중간, 파일 업로드 백엔드 필요

**중기 단계(v2 - 컨텍스트 칩)**: 
- @data 칩: "데이터셋" 참조(향후 데이터 업로드 기능과 연계)
- @liveboard 칩: 기존 Liveboard 대시보드 참조(크로스 피처 컨텍스트)
- @ 자동완성 메뉴로 칩 선택 가능
- 장기 동안 프로젝트 또는 "세션"에 파일 저장 가능

**장기 단계(v3 - 멀티모달)**: 
- 이미지 클립보드 붙여넣기(Ctrl+V)
- 음성 입력(모바일용 마이크 아이콘)
- 웹 링크 첨부(예: YouTube, GitHub 링크 직접 입력)

### 이 접근을 권장하는 이유

1. **점진적 구현**: v1부터 파일 기본 지원, v2에서 컨텍스트 추가, v3에서 멀티모달 확장
2. **KonaI-Agent 도메인 최적화**: @data, @liveboard는 "데이터 분석 AI" 용도에 정렬
3. **3-panel 레이아웃 활용**: 우측 패널에서 첨부된 파일 미리보기 또는 분석 결과 표시 가능
4. **클립보드 붙여넣기 지원**: 개발자/분석가가 데이터를 빠르게 붙여넣고 처리 원함
5. **드래그앤드롭 표준화**: 모던 웹 UX의 사실상 표준이므로 사용자 기대감 높음
6. **컨텍스트 재사용성**: @ 멘션 시스템으로 "이전에 분석한 데이터" 다시 참조 가능

### Acceptance Criteria

- [ ] 파일 첨부 버튼: ChatInterface에 "Attach" 또는 클립 아이콘 버튼 추가. 클릭 시 파일 선택 다이얼로그 열기
- [ ] 드래그앤드롭: ChatInterface 전체 영역을 dropzone으로 설정. 파일 드롭 시 첨부 목록에 추가. Visual feedback(overlay 하이라이트) 제공
- [ ] 파일 타입 검증: 클라이언트 사이드에서 MIME type 및 확장자 검증. 허용되지 않은 파일은 경고 메시지 표시
- [ ] 인라인 칩 표시: 첨부된 파일을 입력 필드 상단 또는 내부에 칩 형태로 렌더링. 각 칩에 파일명, 크기, 제거 버튼 표시
- [ ] 파일 미리보기: 이미지 파일은 작은 썸네일 표시. PDF/문서는 파일 아이콘 + 크기 표시
- [ ] 크기 제한: 파일당 5MB 제한(설정 가능). 초과 시 사용자 친화적 에러 메시지 제공
- [ ] @컨텍스트 멘션: 입력 필드에서 @ 입력 시 자동완성 메뉴 표시(@data, @liveboard 등). 멘션 선택 시 해당 컨텍스트 칩 추가
- [ ] 복수 첨부: 여러 파일 동시 첨부 지원(최대 5개 또는 설정 가능). 가로 스크롤 또는 그리드 레이아웃으로 표시
- [ ] 파일 제거: 각 칩의 X 버튼으로 파일 제거. 실시간으로 입력 필드 업데이트
- [ ] Textarea auto-resize: 파일 첨부 전후로도 정상 작동. 파일 칩이 추가돼도 scrollbar 안 생김

## Key Considerations

### 파일 보안 및 프라이버시
- **클라이언트 사이드 검증**: MIME type, 확장자, 크기 검증. 하지만 서버에서 재검증 필수(클라이언트 우회 가능)
- **암호화**: HTTPS 사용하여 전송 중 데이터 보호
- **사용자 파일 저장**: 사용자의 파일을 서버에 저장하기 전에 명시적 동의 받기(GDPR/개인정보보호 준수)
- **자동 삭제**: 일정 기간(예: 30일) 후 자동 삭제하거나, 대화 삭제 시 함께 삭제

### 모바일 UI 고려
- 드래그앤드롭은 모바일에서 작동 불가하므로, 파일 선택 버튼은 필수
- 모바일에서 여러 파일 칩이 한 줄에 표시 어려우므로, 수평 스크롤 또는 "N개 파일 첨부됨" 요약 표시 고려
- 이미지 클립보드 붙여넣기(Ctrl+V)는 데스크톱 중심이므로, 모바일에서는 카메라 버튼으로 대체

### 파일 메타데이터 표시
- 파일 크기를 항상 표시(사용자가 큰 파일 예상 가능)
- 파일 업로드 진행 상태 표시(대용량 파일의 경우)
- 업로드 실패 시 명확한 에러 메시지(예: "파일 크기가 초과했습니다" vs 애매한 "오류 발생")

### @멘션 시스템 확장성
- 초기: @data, @liveboard
- 향후 추가 가능: @model (모델 선택), @style (시각화 스타일), @export (출력 형식)
- @ 뒤에 필터링(예: "@data live" → "live"로 시작하는 데이터만 표시)

### 성능 최적화
- 대용량 파일(이미지) 썸네일 생성: 클라이언트 사이드에서 canvas API로 축소본 생성(서버 로드 감소)
- 드래그앤드롭 이벤트(dragover, drop) 과도하게 리렌더링하지 않도록 debounce 처리
- 파일 목록이 많아지면(10개 이상) 가상화(virtualization) 고려

### 이미지 클립보드 로직
- 사용자가 Ctrl+V를 누르면, 클립보드 내용 확인(이미지 있으면 자동 첨부)
- 단순 텍스트는 무시하고 입력 필드에 붙여넣기(기존 동작)
- 이미지와 텍스트가 함께 있으면, 이미지만 첨부하고 텍스트는 입력 필드에 추가

## Recent Updates

| 날짜 | 변경사항 |
|------|---------|
| 2025-02-15 | 초안 작성. ChatGPT/Claude/Gemini/Cursor 비교 분석. @멘션 시스템 추가 |

## References

[^1]: [ChatGPT Drag-and-Drop Feature Guide](https://www.pageon.ai/blog/chatgpt-drag-and-drop)
[^2]: [Claude File Upload & Projects Documentation](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)
[^3]: [Cursor Context Management & @symbols](https://stevekinney.com/courses/ai-development/cursor-context)
[^4]: [Gemini Multimodal Input Guide](https://support.google.com/gemini/answer/16741341)
