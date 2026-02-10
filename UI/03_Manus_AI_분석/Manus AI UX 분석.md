
https://www.baytechconsulting.com/blog/manus-ai-an-analytical-guide-to-the-autonomous-ai-agent-2025
https://www.analyticsvidhya.com/blog/2025/03/manus-ai-vs-openai-operator/
https://www.emerge.haus/blog/the-new-dominant-ui-design-for-ai-agents
https://uxdesign.cc/cursor-vibe-coding-and-manus-the-ux-revolution-that-ai-needs-3d3a0f8ccdfa

## Executive Summary

**Manus AI** (2025.03 출시)는 AI 에이전트 인터페이스를 **"Chat-to-Artifact"에서 "Chat-to-Execution"**으로 전환한 혁신적 제품입니다.

### 핵심 차별화 요소

| 혁신 영역 | 구현 방식 | 비즈니스 임팩트 |
|-----------|-----------|----------------|
| **Glass Box 투명성** | "Manus's Computer"로 에이전트 행동 실시간 관찰 | Waiting Anxiety 해소, 신뢰도 향상 |
| **진정한 작업 위임** | 클라우드 가상 환경, 최대 14일 작업 지속 | "시키고 잊기" 가능, 모바일 지원 |
| **Code-First 검증** | Python/Shell 스크립트 직접 노출 | 개발자 디버깅 가능, 학습 효과 |
| **Two-Pane UI** | 대화(CLI) + 실행 캔버스 분리 | "보면서 개입" 경험, Human-in-the-Loop |

---

## 1. UX 패러다임: "답변"에서 "작업물"로의 전환

### 전통적 AI Chat의 한계
```
기존 인터페이스                     문제점
┌─────────────────┐                 • "블랙박스" 응답
│                 │                 • 긴 작업 시 Waiting Anxiety
│   대화창 Only     │          →     • 일회성 상호작용
│                 │                 • 결과만 제공, 과정 불투명
│   (Q&A 패턴)     │
└─────────────────┘
```

### Manus의 해결책: Two-Pane 아키텍처
```
┌──────────────────┬─────────────────────────┐
│ Left: 대화       │ Right: Manus's Computer │
│ ─────────────    │ ───────────────────────  │
│ • 사용자 명령    │ • 실시간 브라우저       │
│ • 에이전트 계획  │ • 코드 실행 결과        │
│ • 개입 요청      │ • 파일 시스템 변경      │
│                  │                         │
│ (CLI 역할)       │ (작업 관찰 - 1급 시민)  │
└──────────────────┴─────────────────────────┘
```

**핵심 원칙**: 채팅을 읽는 대신 **실제 작업 과정을 관찰**하고 **언제든지 개입** 가능

---

## 2. Glass Box UX: 투명성의 재정의

### 경쟁사 vs. Manus

| 요소 | 경쟁사 (Claude, ChatGPT) | Manus AI |
|------|--------------------------|----------|
| **진행 표시** | "작업 중..." 로딩 스피너 | **실시간 브라우저 미러링** |
| **사고 과정** | "Thinking..." 텍스트 | **실행 트리 + 코드 노출** |
| **에러 처리** | "오류 발생" 메시지 | **Self-Correction Loop 시각화** |
### Human-in-the-Loop(개입 매커니즘)
Manus는 완전 자동화를 지향하면서도, 결정적인 순간에 사용자의 개입을 유도하여 신뢰도를 향상

- **Intervention Points:** 에이전트가 CAPTCHA나 모호한 선택지에 직면하면 작업을 일시 정지하고 "Help me out" 또는 "Confirm/Edit" 버튼을 노출
    
- **직관적 피드백:** 단순 채팅뿐만 아니라, 작업 중인 파일이나 화면에 직접 파일을 드래그 앤 드롭하여 멀티모달 컨텍스트를 제공

### 실시간 브라우저 미러링 구현

**기술 스택 (추정):**
- **DOM Mutation Streaming** (rrweb 방식)
- **WebSocket** 양방향 통신
- **Ghost Cursor** 오버레이

**효과:**
- ✅ AI가 보는 웹페이지를 사용자도 동시에 관찰
- ✅ 마우스 움직임, 클릭, 타이핑까지 시각화
- ✅ 픽셀 스트리밍 대비 **대역폭 90% 절약**

### 실행 트리 시각화
```
📋 Main Goal: 경쟁사 가격 조사
 ├─ 🔄 Sub-task 1: Google 검색 (Running)
 │   ├─ 🌐 Browser: google.com 접속
 │   └─ ⌨️ Input: "경쟁사 제품 가격"
 ├─ ⏸️ Sub-task 2: 데이터 추출 (Pending)
 └─ ⏸️ Sub-task 3: 정리 (Pending)
````

사용자는 관심 있는 단계만 펼쳐 **Python 코드, 스크린샷 등 상세 로그** 확인

### 세션 재생 및 공유

- ✅ 전체 작업 과정 **replay** 가능
- ✅ 다른 팀원과 **세션 링크 공유** 가능
- **활용**: 에이전트 오류 디버깅, 작업 프로세스 학습, 감사 추적

---

## 3. 기술 아키텍처

### 3.1 Frontend Stack

|레이어|기술|선택 이유|
|---|---|---|
|Framework|**Next.js**|SSR + CSR 하이브리드, 복잡한 상태 관리|
|Styling|**Tailwind CSS**|유동적 레이아웃, Artifact 스타일 일관성|
|State|**Zustand/Jotai**|가벼운 Atomic state (Redux보다 효율적)|
|UI Components|**Radix UI**|Headless, 접근성, 모던 디자인|

### 3.2 실시간 통신: WebSocket의 필요성

|요구사항|SSE|WebSocket|
|---|---|---|
|텍스트 스트리밍|✅|✅|
|파일 변경 알림|❌|✅|
|사용자 개입 (Pause/Resume)|❌|✅|
|DOM 스냅샷 전송|❌|✅|

### 3.3 Hybrid Rendering + Artifact Sandbox
```
┌─────────────────┬──────────────────┬──────────────┐
│ App Shell (SSR) │ Workspace (CSR)  │ Artifact     │
│ ─────────────── │ ──────────────── │ ──────────── │
│ • 빠른 초기 로딩│ • WebSocket 연결 │ • iFrame 격리│
│ • SEO 최적화    │ • 실시간 업데이트│ • XSS 방지   │
└─────────────────┴──────────────────┴──────────────┘
```

**Artifact Sandbox 보안:**
- **iFrame + Subdomain Isolation**: 메인 앱 쿠키 접근 차단
- **Shadow DOM**: CSS 충돌 방지
- **Content Security Policy**: XSS 공격 방어

---

## 4. 핵심 차별화 요소

### 4.1 CodeAct: "Show, Don't Tell"

**경쟁사:**
```
❌ "웹사이트에서 데이터를 가져왔습니다."
````

**Manus:**

python

```python
✅ 사용자가 보는 실제 코드:

import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com/products')
soup = BeautifulSoup(response.text, 'html.parser')
products = soup.find_all('div', class_='product-card')

for p in products:
    print(f"{p.find('h3').text}: {p.find('.price').text}")
```

**효과**: 검증 가능 + 학습 + 디버깅

### 4.2 Persistent Cloud Computer

| 비교 | OpenAI Operator | Manus AI |
|------|-----------------|----------|
| 환경 | 로컬 브라우저 | **클라우드 VM** |
| 지속성 | 탭 닫으면 종료 | **최대 14일** |
| 자원 | 사용자 CPU/메모리 | **서버 사이드** |
| 모바일 | 제한적 | **완전 지원** |

**실사용 시나리오:**
1. 모바일에서 "데이터 분석해줘" 명령
2. 퇴근 후 푸시 알림 "완료"
3. 재접속 시 전체 과정 + 결과 보존

### 4.3 비동기 실행 + 상태 복원
```
사용자: 탭 닫음 (로그아웃)
         ↓
서버: Task Loop 계속 실행
      • Redis: 세션 상태
      • PostgreSQL: 로그 저장
      • WebSocket 재연결 대기
         ↓
사용자: 30분 후 재접속
         ↓
결과: 전체 컨텍스트 복원 ✅
```

---

## 5. 경쟁사 비교

### 포지셔닝 맵
```
      완전 자율 ↑
         │
    Manus AI
         │
    ┌────┼────┐
 Cursor  │    Claude
         │   Artifacts
 ChatGPT Canvas
         │
    v0.dev (UI 특화)
         │
      반자율 ↓
````

### 핵심 비교

|제품|자율성|투명성|개입성|환경|지속성|
|---|---|---|---|---|---|
|**Manus**|⭐⭐⭐⭐⭐|⭐⭐⭐⭐⭐|⭐⭐⭐⭐⭐|Full OS|14일|
|Claude|⭐⭐⭐|⭐⭐⭐|⭐⭐⭐|File creation|Persistent|
|ChatGPT|⭐⭐⭐|⭐⭐|⭐⭐⭐|Export only|History|
|Cursor|⭐⭐⭐⭐|⭐⭐⭐⭐|⭐⭐⭐⭐|Full IDE|Git|
|v0.dev|⭐⭐|⭐⭐⭐|⭐⭐⭐|Export only|None|

### 경쟁 우위

**Manus 우위 영역:**

1. **End-to-end 자동화** (Claude/ChatGPT는 대화 필요)
2. **브라우저 제어 + 백엔드** (v0.dev는 UI만)
3. **비개발자 작업** (Cursor는 코딩 특화)
4. **진정한 위임** (로컬 제어 방식과 차별화)

**약점:**

- ⚠️ 높은 실패율 (초기 불안정성)
- ⚠️ 서버 가용성 이슈
- ⚠️ 작업당 과금 (장시간 작업 비용↑)

---

## 6. Kona I 프로젝트 적용 전략

### 벤치마크 포인트

|Manus 혁신|Kona I 적용 방안|
|---|---|
|**Two-Pane UI**|Left: 임원 대화 / Right: 실시간 ERP 데이터 시각화|
|**Glass Box**|SQL 쿼리 자동 생성 시 쿼리문 직접 노출|
|**CodeAct**|Text-to-SQL 변환 과정 투명하게 공개|
|**Cloud Computer**|Self-hosted Execution (데이터 주권)|
|**Human-in-the-Loop**|재무 데이터 처리 전 임원 확인 요청|

### 차별화 전략

**"Virtual Analyst for ERP"**

- Manus가 브라우저 제어 → **Kona I는 ERP 데이터 탐색**
- 회계 용어, 한국 기업 문화 맞춤 자연어 이해
- 모든 계산 과정 투명 공개 (재무 데이터 신뢰 구축)

### 기술 구현 로드맵

1. **Phase 1**: MCP UI Protocol로 BI 도구 통합
2. **Phase 2**: Semantic Layer 투명성 (SQL 노출)
3. **Phase 3**: 비동기 리포트 생성 + Slack 알림

---

## 결론

### 핵심 교훈

> **Manus AI는 "투명성 = 신뢰"라는 공식을 증명했습니다.**

**3가지 원칙:**

1. **Glass Box UX**: 블랙박스를 열어 Waiting Anxiety 해소
2. **진정한 위임**: 클라우드 실행으로 "시키고 잊기"
3. **Code-First**: 검증 가능한 프로세스 제공

### 최종 평가

|항목|점수|비고|
|---|---|---|
|혁신성|⭐⭐⭐⭐⭐|Chat-to-Execution 패러다임 창출|
|기술 완성도|⭐⭐⭐|초기 불안정성 존재|
|엔터프라이즈 적합성|⭐⭐⭐|보안 우려, Self-hosting 미지원|
|**Kona I 벤치마크 가치**|**⭐⭐⭐⭐⭐**|**필수 참고 사례**|

**권장사항:**

- ✅ Two-Pane + Glass Box UX를 Kona I 기본 구조로 채택
- ✅ SQL 쿼리 투명성으로 CodeAct 철학 구현
- ✅ Self-hosted 환경으로 데이터 주권 확보