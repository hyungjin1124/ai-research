## Claude Cowork의 동적 Plan 수정 구현 방법

### 1. 핵심 아키텍처: Observe-Plan-Act-Reflect 루프

Claude Cowork는 **Master Agent Loop**라 불리는 단일 스레드 while-loop 기반의 에이전트 제어 루프를 사용합니다. 이 루프가 동적 Plan 수정의 핵심입니다.
```
┌──────────────┐
│  User Input  │
└──────┬───────┘
       ▼
┌──────────────┐
│   Observe    │ ← 환경 상태/파일 읽기
└──────┬───────┘
       ▼
┌──────────────┐
│    Plan      │ ← Chain of Thought 생성/업데이트
└──────┬───────┘
       ▼
   Decision?
   ├── Yes → Act (Tool Call) → Execute → Reflect
   │                                        │
   │   ┌────────────────────────────────────┘
   │   │ 성공/실패 결과 분석
   │   ▼
   └── Observe로 복귀 (루프 반복)
       │
   └── No → Final Response → End
```

## Claude Cowork vs ChatGPT Agent vs Project Mariner: 구조적 차이 비교

### 1. 핵심 아키텍처 비교

|구분|Claude Cowork|ChatGPT Agent|Project Mariner|
|---|---|---|---|
|**제어 루프**|Observe-Plan-Act-**Reflect**|Observe-Plan-Act|Observe-Plan-Act|
|**Plan 저장 방식**|마크다운 파일로 영속화|메모리 내 임시 보관|메모리 내 임시 보관|
|**사용자 개입 지점**|Plan 생성/실행 전 과정|주로 확인 프롬프트|Pause/Cancel 버튼|
|**Plan 수정 가능성**|✅ 사용자가 직접 수정 가능|❌ 중단/재시작만 가능|❌ 중단/인수인계만 가능|
### 2. 사용자 개입 메커니즘의 차이

#### Claude Cowork: **Steering 모델**

```
사용자 요청 → Plan 생성 → [사용자 검토/수정] → 실행 → [사용자 방향 수정] → 반영 → 완료
                              ↑                        ↑
                        Human-in-the-Loop      Course Correction
```

Cowork는 실행 중에도 사용자가 **"Jump in to course-correct or provide additional direction"**할 수 있도록 설계되어 있습니다. Plan이 마크다운 파일로 저장되기 때문에 에이전트가 자신의 계획 파일을 edit할 수 있고, 사용자 피드백에 따라 동적으로 수정됩니다.

#### ChatGPT Agent: **Confirmation 모델**

```
사용자 요청 → Plan 생성 → 실행 → [High-impact Action?] → 확인 요청 → 승인/거부 → 계속/중단
                                       ↓
                               Yes: 일시 정지 후 확인
                               No: 자동 진행
```

ChatGPT Agent는 **"confirmation prompts before critical actions"**에 의존합니다. 사용자는 작업을 중단하거나 "Take over browser"로 직접 제어를 인수받을 수 있지만, **기존 Plan을 수정하는 것이 아니라 새로운 요청으로 대체**해야 합니다.

#### Project Mariner: **Takeover 모델**

```
사용자 요청 → Plan 생성 → 실행 ──────────────→ 완료
                           ↓
                    [Pause/Cancel 버튼]
                           ↓
                    사용자가 직접 수행
```

Mariner는 **"pause/cancel" 버튼**으로 에이전트를 멈추고 사용자가 직접 작업을 이어받을 수 있습니다. 그러나 에이전트의 Plan 자체를 수정하는 것이 아니라 **중단 후 사용자가 직접 수행**하는 방식입니다.

### 3. Reflect 단계의 유무 - 핵심 차이점

Claude Cowork만이 명시적인 **Reflect(반성) 단계**를 포함합니다:

```
┌─────────────────────────────────────────────────────────────┐
│  Claude Cowork: Evaluator-Optimizer Loop                    │
│                                                             │
│  실행 결과 분석 → 성공/실패 판단 → 전략 조정 → Plan 업데이트  │
│                                                             │
│  예: CSS Selector 실패 → 시각적 좌표 클릭으로 전환           │
│      코드 에러 발생 → 에러 스택 분석 → 수정안 적용           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  ChatGPT Agent / Project Mariner: Linear Execution          │
│                                                             │
│  실행 결과 확인 → 다음 단계 진행 (또는 실패 시 중단)         │
│                                                             │
│  예: 실패 시 사용자에게 알림 → 사용자가 직접 해결            │
└─────────────────────────────────────────────────────────────┘
```

### 4. Plan 영속화 방식의 차이

|서비스|Plan 저장|수정 가능성|재사용성|
|---|---|---|---|
|**Claude Cowork**|마크다운 파일 (`.md`)|에이전트 + 사용자 모두 수정 가능|파일로 저장되어 재사용 가능|
|**ChatGPT Agent**|컨텍스트 메모리|새 프롬프트로 대체만 가능|세션 종료 시 소멸|
|**Project Mariner**|컨텍스트 메모리|Teach & Repeat으로 학습 가능|워크플로우 녹화로 재사용|