
## 1. 개요

### 조사 범위

- **조사 기간:** 2025년 11월 ~ 2026년 1월 (최근 2개월 이내 출시/업데이트 사례 중심)
- **조사 대상:**
  - 거대 AI 기업 서비스 (OpenAI, Google, Microsoft, Manus)
  - 오픈소스 프로젝트 (OpenWork, Open Claude Cowork, Eigent, Open Interpreter, Agent S2 등)
  - 기타 AI 에이전트 서비스 (Cursor, Windsurf, Devin 등)

### Claude Cowork 핵심 기능

| 기능               | 설명                         |
| ---------------- | -------------------------- |
| **로컬 파일 시스템 접근** | 로컬 파일 읽기/쓰기/편집             |
| **코드 실행**        | Python, JavaScript 등 코드 실행 |
| **브라우저 자동화**     | MCP를 통한 웹 브라우저 제어          |
| **문서 생성**        | DOCX, PPTX, XLSX 등 문서 생성   |
| **Skills 시스템**   | 맞춤형 에이전트 동작 확장             |
| **샌드박스 환경**      | 안전한 실행 환경 제공               |
### Claude Cowork의 강점

1. **Human-in-the-Loop**: 3단계 권한 시스템(Allow/Deny/Ask)으로 안전성과 효율성 균형
2. **Sub-Agent 아키텍처**: 최대 7개 sub-agent 병렬 실행으로 복잡한 작업 효율적 처리
3. **Visual To-Do List**: 직관적인 진행 상황 추적 및 투명성 제공
4. **Mid-Task Steering**: 작업 진행 중 실시간 방향 수정 가능

---

## 2. 거대 AI 기업 서비스
| 서비스                   | 개발사       | 출시일     | 브라우저 자동화 | 파일 시스템 | 코드 실행 | MCP 지원 |
| --------------------- | --------- | ------- | -------- | ------ | ----- | ------ |
| **Claude Cowork**     | Anthropic | 2026.01 | ✅        | ✅      | ✅     | ✅      |
| **ChatGPT Agent**     | OpenAI    | 2025.07 | ✅        | ❌      | ❌     | ❌      |
| **Project Mariner**   | Google    | 2025.05 | ✅        | ❌      | ❌     | ❌      |
| **Microsoft Copilot** | Microsoft | 2023.03 | ✅        | ✅      | ✅     | ✅      |

| 기능         | Microsoft Copilot  | OpenAI ChatGPT Agent | Google Mariner | Manus AI |
| ---------- | ------------------ | -------------------- | -------------- | -------- |
| 파일 시스템 접근  | ✅(Copilot Actions) | ❌                    | ❌              | ❌        |
| 코드 실행      | ⚠️(Python만)        | ✅                    | ❌              | ✅        |
| 브라우저 자동화   | ✅                  | ✅                    | ✅              | ✅        |
| 문서 생성      | ✅                  | ✅                    | ❌              | ✅        |
| Skills 시스템 | ✅                  | ✅                    | ⚠️             | ✅        |
| 샌드박스 환경    | ✅                  | ✅                    | ✅              | ✅        |

---

## 3. 오픈소스

### 3.1 OpenWork

#### 프로젝트 개요
OpenWork는 Claude Cowork의 오픈소스 대안으로, 2026년 1월 14일에 출시되었습니다. OpenCode를 기반으로 한 데스크톱 AI 에이전트 애플리케이션입니다.

#### 핵심 기능

| 기능 | 상세 설명 |
|------|----------|
| **파일 작업** | 읽기/생성/편집 |
| **브라우저 작업** | 웹 자동화 수행 |
| **폴더 스캔** | 폴더 구조 요약 |
| **문서 생성** | 생성/재작성 |
| **프로젝트 설정** | 폴더 구조 자동 설정 |

#### GitHub 정보

| 항목 | 정보 |
|------|------|
| **저장소** | [github.com/different-ai/openwork](https://github.com/different-ai/openwork) |
| **출시일** | 2026년 1월 14일 |
| **라이선스** | MIT |
| **상태** | 베타 |

---

### 3.2 Open Interpreter

#### 프로젝트 개요

컴퓨터를 위한 자연어 인터페이스로, LLM이 로컬에서 코드(Python, JavaScript, Shell 등)를 실행할 수 있게 합니다.

#### 핵심 기능

| 기능            | 상세 설명                |
| ------------- | -------------------- |
| **터미널 인터페이스** | ChatGPT 같은 CLI 인터페이스 |
| **미디어 처리**    | 사진, 비디오, PDF 생성/편집   |
| **인터넷 접근**    | 웹 리서치 가능             |
| **제한 없음**     | 파일 크기/시간 제한 없음       |
| **--os 모드**   | Anthropic 기반 OS 모드   |

#### GitHub 정보

| 항목 | 정보 |
|------|------|
| **저장소** | [github.com/openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) |
| **Stars** | ~61,676개 |
| **라이선스** | AGPL-3.0 |
| **최근 업데이트** | 2026년 1월 (uv 포팅, Python 3.14 지원) |

#### 설치 방법

```bash
pip install open-interpreter
interpreter
```
*Python 3.10 또는 3.11 필요*
#### 데모 영상

![[264166941-37152071-680d-4423-9af3-64836a6f7b60.mp4]]


---

### 3.3 Agent S2 (Simular AI)

#### 프로젝트 개요

Simular AI가 개발한 GUI 및 웹 작업을 위한 선도적인 오픈소스 자율 에이전트입니다. 2025년 말 주목받는 컴퓨터 자동화 에이전트로 부상했습니다.

#### 핵심 기능

| 기능          | 상세 설명                     |
| ----------- | ------------------------- |
| **GUI 자동화** | 데스크톱 애플리케이션 직접 조작         |
| **웹 작업**    | 브라우저 기반 작업 자동화            |
| **자율 실행**   | 사용자 개입 없이 복잡한 작업 수행       |
| **벤치마크 선도** | OSWorld, WebArena에서 높은 성과 |
#### 데모 영상
https://www.simular.ai/use-cases

---

## 5. 종합 비교표

### 5.1 오픈소스 프로젝트 비교

| 프로젝트                 | GitHub Stars | 최신 버전 | 라이선스     | 멀티 모델 | 브라우저 | 파일 시스템 |
| -------------------- | ------------ | ----- | -------- | ----- | ---- | ------ |
| **OpenWork**         | -            | Beta  | MIT      | O     | O    | O      |
| **Open Interpreter** | 61.6k        | -     | AGPL-3.0 | O     | X    | O      |
| **Agent S2**         | -            | -     | 오픈소스     | O     | O    | O      |


---

## 6. 결론 및 시사점

### 6.1 시장 동향

2025년은 "AI 에이전트의 해"로 불리며, 2026년에는 연구 단계에서 프로덕션 준비 솔루션으로 전환되고 있습니다. 주요 트렌드는 다음과 같습니다:

1. **브라우저 자동화 경쟁 심화**
   - OpenAI, Google, Microsoft, Anthropic 모두 브라우저 제어 에이전트 출시
   - 안전성(Takeover Mode, 사용자 확인)이 핵심 차별화 요소

2. **멀티 에이전트 아키텍처**
   - Microsoft, CrewAI 등에서 여러 에이전트 협업 기능 강화
   - 복잡한 작업을 분담하여 처리하는 방향으로 발전

3. **오픈소스 대안 급증**
   - Claude Cowork 출시 직후 OpenWork, Eigent 등 대안 등장
   - 비용 절감 및 모델 선택의 자유도 제공

4. **MCP(Model Context Protocol) 표준화**
   - Microsoft, Google, Anthropic 모두 MCP 지원
   - 도구 통합의 표준화 진행

### 6.2 Claude Cowork의 차별점

1. **범용성:** 코딩뿐 아니라 문서 작업, 데이터 분석, 웹 자동화 등 다목적
2. **Skills 시스템:** 맞춤형 에이전트 동작 확장 가능
3. **투명성:** 실시간 상호작용으로 작업 과정 확인 및 개입 가능
4. **로컬 실행:** 사용자 컴퓨터에서 직접 실행하여 프라이버시 보호

### 6.3 선택 가이드

| 요구사항          | 추천 서비스                                       |
| ------------- | -------------------------------------------- |
| **무료로 시작**    | OpenWork, Eigent, Open Interpreter, Agent S2 |
| **코딩 특화**     | Cursor, Windsurf, GitHub Copilot             |
| **완전 자율 개발**  | Devin                                        |
| **범용 자동화**    | Claude Cowork, Microsoft Copilot             |
| **웹 검색/리서치**  | Perplexity, ChatGPT Agent                    |
| **GUI/웹 자동화** | Agent S2, Project Mariner, ChatGPT Agent     |
| **엔터프라이즈**    | Microsoft Copilot, Google Workspace Studio   |


---

## 7. 참고 자료

### 공식 웹사이트

| 서비스 | URL |
|--------|-----|
| Claude Cowork | https://claude.ai |
| OpenAI Operator | https://openai.com/index/introducing-operator/ |
| ChatGPT Agent | https://openai.com/index/introducing-chatgpt-agent/ |
| Google Project Mariner | https://deepmind.google/models/project-mariner/ |
| Google Workspace Studio | https://workspace.google.com/studio/ |
| Microsoft Copilot | https://www.microsoft.com/en-us/microsoft-copilot |
| OpenWork | https://www.openwork.me/ |
| Open Interpreter | https://www.openinterpreter.com/ |
| Cursor | https://cursor.com/ |
| Windsurf | https://windsurf.com/ |
| Devin | https://devin.ai/ |
| GitHub Copilot | https://github.com/features/copilot |

### GitHub 저장소

| 프로젝트 | URL |
|---------|-----|
| OpenWork | https://github.com/different-ai/openwork |
| Open Claude Cowork | https://github.com/ComposioHQ/open-claude-cowork |
| Eigent | https://github.com/eigent-ai/eigent |
| Open Interpreter | https://github.com/openinterpreter/open-interpreter |
| AutoGPT | https://github.com/Significant-Gravitas/AutoGPT |
| CrewAI | https://github.com/crewAIInc/crewAI |
| LangGraph | https://github.com/langchain-ai/langgraph |

### 참고 문서

- OpenAI Operator Wikipedia: https://en.wikipedia.org/wiki/OpenAI_Operator
- Microsoft Copilot Wikipedia: https://en.wikipedia.org/wiki/Microsoft_Copilot
- Gemini API Pricing: https://ai.google.dev/gemini-api/docs/pricing
- Microsoft 365 Copilot Blog: https://www.microsoft.com/en-us/microsoft-365/blog/
- TechCrunch AI Coverage: https://techcrunch.com/category/artificial-intelligence/
- VentureBeat AI: https://venturebeat.com/ai/

---

**보고서 끝**

*본 보고서의 정보는 2026년 1월 20일 기준으로 작성되었으며, 각 서비스의 기능 및 가격은 변경될 수 있습니다.*
