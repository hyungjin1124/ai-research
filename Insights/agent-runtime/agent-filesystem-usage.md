---
type: insight-synthesis
topic_id: agent-filesystem-usage
topic_name: 에이전트 파일시스템 활용 패턴
category: agent-runtime
tags:
- insight
- agent-runtime
- filesystem
- sandbox
- code-execution
status: draft
confidence: medium
last_updated: '2026-02-10'
source_products:
- claude
- openai
- manus-ai
- vercel-v0
- microsoft-copilot
source_files:
- '[[claude]]'
- '[[openai]]'
- '[[manus-ai]]'
- '[[vercel-v0]]'
- '[[microsoft-copilot]]'
relevant_roles:
- backend_agent
auto_update:
  enabled: true
  feeds: []
  keywords:
  - file system
  - sandbox
  - code execution
  - container
  - cloud sandbox
  - code interpreter
  review_trigger:
    mode: auto
    threshold: 3
    priority_override: true
---
# 에이전트 파일시스템 활용 패턴

## TL;DR

- **AI 에이전트의 파일시스템 접근 방식은 크게 4가지 패턴으로 분류된다**: (1) 로컬 파일시스템 직접 접근(Claude Code), (2) 클라우드 샌드박스 컨테이너 내 완전한 파일시스템(Manus AI, OpenAI Codex), (3) 프로젝트 스코프 샌드박스(Vercel v0), (4) 엔터프라이즈 데이터 레이어 간접 접근(Microsoft Copilot)
- **샌드박스 격리 수준과 에이전트 자율성 사이에 명확한 트레이드오프가 존재한다**: 로컬 파일시스템 직접 접근(Claude Code)은 최대 자율성을 제공하지만 보안 리스크가 크고, 완전 격리 샌드박스(Manus AI)는 안전하지만 사용자의 실제 작업 환경과 분리되는 한계가 있다
- **"Ephemeral Container" 패턴이 코딩 에이전트의 주류로 부상하고 있다**: OpenAI Codex와 Manus AI 모두 태스크별 독립 클라우드 컨테이너를 생성하여 코드 실행·파일 생성·브라우저 자동화를 수행하며, 태스크 완료 후 산출물만 추출하는 방식을 채택한다. 이 패턴은 보안·확장성·병렬 처리에서 이점이 크다
- **Claude의 듀얼 전략(Code: 로컬 직접 접근 + Cowork: VM 샌드박스)은 사용자 세그먼트별 파일시스템 접근 수준을 차별화하는 유일한 사례이다**: 개발자에게는 로컬 파일시스템의 완전한 제어를, 비개발자에게는 VM 내 제한된 폴더 접근을 제공하여 보안과 유용성의 균형을 맞추고 있다
- **엔터프라이즈 에이전트(Microsoft Copilot)는 파일시스템 직접 접근 대신 데이터 레이어(Dataverse, Microsoft Graph) 추상화를 통한 간접 접근을 채택한다**: 이는 기존 거버넌스·RBAC 체계를 유지하면서 에이전트의 데이터 접근을 제어하기 위한 전략적 선택이다

---

## Context

AI 에이전트가 단순한 대화형 Q&A를 넘어 실제 업무를 자율적으로 수행하기 위해서는 파일의 읽기·쓰기·실행이 필수적이다. 코드를 작성하고, 문서를 생성하며, 데이터를 분석하고, 빌드를 수행하는 모든 에이전틱 워크플로우의 기반에 파일시스템 접근이 있다. 엔터프라이즈 AI 에이전트를 설계함에 있어, 파일시스템 접근의 범위·격리 수준·지속성을 어떻게 설계할 것인지는 프로덕트의 보안성, 유용성, 확장성을 결정짓는 핵심 아키텍처 결정이다.

특히 2025~2026년 에이전트 시장에서 "코드 실행 환경"과 "작업 공간 관리" 방식이 제품별로 뚜렷이 분화하고 있는 상황에서, 산업의 파일시스템 활용 패턴을 비교하면 에이전트 런타임의 파일시스템 계층을 설계할 때 실질적 참고가 된다. 샌드박싱 전략, 파일 지속성, 작업 디렉토리 구조, 산출물 관리 방식 등 세부 설계 요소에 대한 교차 분석이 이 문서의 목적이다.

---

## Cross-Product Analysis

### 비교 매트릭스

| Product | 파일시스템 접근 방식 | 격리 수준 | 지속성 | 코드 실행 환경 | 작업 디렉토리 패턴 | 성숙도 |
|---------|-------------------|----------|--------|--------------|------------------|--------|
| [[claude]] (Code) | 로컬 파일시스템 직접 접근 | 없음 (사용자 권한 그대로) | 영구 (로컬 디스크) | 로컬 터미널 (bash/zsh) | 사용자의 프로젝트 디렉토리 (cwd) | 높음 (GA) |
| [[claude]] (Cowork) | VM 샌드박스 내 제한된 폴더 접근 | VM 격리 (허용 폴더 한정) | 세션 기반 + 산출물 추출 | VM 내 실행 환경 | 허용된 로컬 폴더 매핑 | 초기 (Research Preview) |
| [[openai]] (Codex) | 클라우드 샌드박스 전용 파일시스템 | 완전 격리 (태스크별 독립 컨테이너) | 태스크 수명 (완료 시 산출물만 보존) | 클라우드 컨테이너 (리포지토리 프리로드) | 리포지토리 루트 기반 | 중간 (GA) |
| [[openai]] (ChatGPT) | 업로드 파일 임시 저장 + Code Interpreter | 샌드박스 (세션 격리) | 세션 한정 (다운로드 필요) | Python 샌드박스 (Jupyter 유사) | /mnt/data (임시) | 높음 (GA) |
| [[manus-ai]] | 클라우드 VM 전용 파일시스템 | 완전 격리 (태스크별 독립 VM) | 최대 14일 (비동기 지속) | VM 내 Python/Shell + 브라우저 | VM 내 자유 구조 | 중간 (GA) |
| [[vercel-v0]] | 프로젝트 스코프 샌드박스 | 프로젝트 격리 (GitHub 리포지토리 클론) | 프로젝트 수명 (Vercel 배포와 연동) | Node.js/Python 샌드박스 터미널 | Next.js 프로젝트 구조 | 중간 (GA) |
| [[microsoft-copilot]] | 데이터 레이어 간접 접근 (Dataverse, Graph) | 엔터프라이즈 RBAC 기반 접근 제어 | 영구 (Dataverse/SharePoint 저장) | Python Code Interpreter (Copilot Studio) | 해당 없음 (데이터 레이어 추상화) | 높음 (GA) |

### 패턴 분류

#### 패턴 A: Local Direct Access (로컬 직접 접근)

**대표 제품**: [[claude]] (Claude Code)

에이전트가 사용자의 로컬 파일시스템에 직접 접근하여 파일을 읽고, 수정하고, 생성하며, 터미널 명령을 실행한다. 사용자의 실제 프로젝트 디렉토리를 작업 공간(working directory)으로 사용하며, Git 워크플로우와 네이티브로 통합된다. Claude Code는 `cwd`(current working directory)를 기준으로 파일 탐색·편집·실행을 수행하며, 파일 변경 시 diff를 표시하고 위험 작업(삭제, 강제 푸시 등)에는 사용자 승인을 요청하는 Human-in-the-Loop 안전장치를 내장한다.

- **장점**: 사용자의 실제 개발 환경과 완벽한 일치, 기존 도구 체인(Git, IDE, 빌드 시스템)과 마찰 없는 통합, 파일 변경이 즉시 영구 반영, 네트워크 지연 없는 I/O 성능
- **단점**: 보안 리스크가 가장 높음(에이전트 오류 시 실제 파일 손상 가능), 샌드박싱 부재로 악의적 MCP 서버 등에 의한 공격 표면이 넓음, 멀티 사용자/팀 환경에서 권한 관리가 OS 수준에 의존

#### 패턴 B: Ephemeral Cloud Container (임시 클라우드 컨테이너)

**대표 제품**: [[openai]] (Codex), [[manus-ai]]

각 태스크마다 독립된 클라우드 컨테이너(또는 VM)를 생성하여, 격리된 파일시스템 내에서 에이전트가 자유롭게 파일을 생성·수정·실행한다. OpenAI Codex는 리포지토리를 컨테이너에 프리로드한 후 코드 작성·테스트·PR 생성을 수행하며, Manus AI는 VM 내에서 브라우저 자동화, Python/Shell 실행, 파일 생성을 모두 처리한다. 태스크 완료 후 산출물(코드 diff, 생성된 파일, 보고서)만 사용자에게 전달되고 컨테이너는 폐기된다.

- **장점**: 완전한 격리로 보안 리스크 최소화, 태스크별 독립 환경으로 병렬 처리 용이(Manus: 20개 동시 태스크), 장기 실행 가능(Manus: 최대 14일, Codex: 7시간+), 사용자 환경에 대한 부작용 제로
- **단점**: 사용자의 실제 개발 환경과 분리되어 환경 불일치(dependency mismatch) 가능, 컨테이너 초기화 오버헤드, 네트워크 기반 파일 전송 지연, 로컬 도구 체인(IDE, 디버거)과의 통합 제약

#### 패턴 C: Project-Scoped Sandbox (프로젝트 스코프 샌드박스)

**대표 제품**: [[vercel-v0]]

특정 프로젝트(주로 GitHub 리포지토리)의 범위 내에서만 파일시스템 접근이 허용되는 격리 환경. Vercel v0는 GitHub 리포지토리를 임포트하여 샌드박스에 클론한 후, Next.js 프로젝트 구조 내에서 파일 생성·수정·빌드를 수행한다. 자율 터미널(Autonomous Terminal)을 통해 의존성 설치와 스크립트 실행이 가능하지만, 프로젝트 경계를 벗어난 파일 접근은 차단된다. 결과물은 Vercel 배포 파이프라인과 네이티브로 연결되어 Preview → Production 흐름이 원클릭으로 작동한다.

- **장점**: 프로젝트 단위 격리로 보안과 유용성의 균형, 배포 파이프라인과의 원활한 통합, 프레임워크 특화 최적화(Next.js 구조 인식), AutoFix 후처리로 코드 품질 보장
- **단점**: 특정 프레임워크/플랫폼(React/Next.js, Vercel)에 종속, 범용 파일 작업(문서 생성, 데이터 분석 등)에는 부적합, 프로젝트 외부 리소스 접근 불가

#### 패턴 D: Data Layer Abstraction (데이터 레이어 추상화)

**대표 제품**: [[microsoft-copilot]]

에이전트가 파일시스템에 직접 접근하지 않고, 엔터프라이즈 데이터 레이어(Dataverse, Microsoft Graph, SharePoint)를 통해 데이터를 읽고 쓴다. 파일이라는 개념 대신 레코드, 문서, 엔티티 단위로 데이터에 접근하며, 기존 RBAC/거버넌스 체계가 그대로 적용된다. Copilot Studio의 Python Code Interpreter는 제한된 코드 실행을 허용하지만, 이것도 데이터 분석/변환 목적에 한정되며 파일시스템 수준의 자유도는 제공하지 않는다.

- **장점**: 엔터프라이즈 거버넌스(RBAC, 감사 로그, 데이터 분류)와 완벽한 정합, 데이터 레지던시/규정 준수 자동 보장, 기존 보안 인프라 재사용, 멀티 테넌트 환경에서의 데이터 격리
- **단점**: 코드 실행·빌드·배포 등 개발자 워크플로우에 부적합, 파일 생성/편집의 유연성 극히 제한, 창의적 산출물(웹 앱, 시각화 등) 생성 불가

---

## Key Findings

1. **사용자 세그먼트별 파일시스템 접근 수준의 차별화가 핵심 설계 원칙으로 부상**: Claude는 개발자(Code: 로컬 직접 접근)와 비개발자(Cowork: VM 샌드박스)로 파일시스템 접근 수준을 명시적으로 분리한 유일한 제품이다. 이는 단일 파일시스템 전략이 모든 사용자 세그먼트를 만족시킬 수 없다는 것을 시사하며, 에이전트 프로덕트 설계 시 타겟 사용자의 기술 숙련도와 보안 요구사항에 따라 파일시스템 접근 계층을 다르게 설계해야 한다는 원칙을 제시한다 -- *Source*: [[claude]]

2. **"Fire and Forget" 비동기 파일시스템 패턴이 에이전트 UX의 새로운 기준을 만들고 있다**: Manus AI의 최대 14일 비동기 실행과 OpenAI Codex의 7시간+ 독립 작업은, 에이전트가 사용자의 세션을 넘어 장기간 파일시스템을 점유하며 작업을 수행하는 새로운 패러다임을 확립했다. 이를 위해서는 (1) 컨테이너의 상태 보존, (2) 중간 산출물의 체크포인팅, (3) 작업 완료 알림 메커니즘이 필수적이며, 세션 기반 임시 파일시스템(ChatGPT Code Interpreter의 /mnt/data)은 이 패턴에 부적합하다 -- *Source*: [[manus-ai]], [[openai]]

3. **샌드박스 격리 수준과 환경 충실도(fidelity) 사이의 트레이드오프가 코딩 에이전트의 핵심 과제이다**: Codex의 클라우드 샌드박스는 완벽한 격리를 제공하지만 사용자의 로컬 환경(환경 변수, 시스템 의존성, IDE 설정)을 완전히 재현하지 못한다. 반면 Claude Code의 로컬 직접 접근은 환경 충실도가 100%이지만 격리가 없다. Vercel v0의 프로젝트 스코프 샌드박스는 GitHub 리포지토리 + Vercel 환경변수를 자동 동기화하여 이 트레이드오프를 부분적으로 해소하지만, 특정 플랫폼에 종속된다 -- *Source*: [[claude]], [[openai]], [[vercel-v0]]

4. **엔터프라이즈 에이전트의 파일시스템 전략은 "접근하지 않는 것"이 최적해이다**: Microsoft Copilot이 파일시스템 직접 접근 대신 Dataverse/Graph 추상화를 선택한 것은, 엔터프라이즈 환경에서 파일 수준 접근이 거버넌스 복잡성을 기하급수적으로 증가시키기 때문이다. 파일 하나의 읽기/쓰기에도 데이터 분류(classification), 접근 제어, 감사 로그, 데이터 레지던시 검증이 필요한 환경에서는, 이미 이러한 제어가 내장된 데이터 레이어를 통한 간접 접근이 가장 현실적인 전략이다 -- *Source*: [[microsoft-copilot]]

5. **작업 디렉토리(Working Directory) 설계가 에이전트의 파일 조작 정확도를 결정한다**: Claude Code는 사용자의 `cwd`를 기준으로 상대/절대 경로를 해석하며, Codex는 리포지토리 루트를, v0는 Next.js 프로젝트 루트를 기준으로 한다. Manus AI는 VM 내에서 자유로운 디렉토리 구조를 에이전트가 스스로 설계한다. 작업 디렉토리의 명확한 기준점(anchor) 없이는 에이전트가 파일 경로를 혼동하거나 잘못된 위치에 파일을 생성하는 오류가 빈발하며, 이는 특히 복잡한 프로젝트 구조에서 심각한 문제가 된다 -- *Source*: [[claude]], [[openai]], [[vercel-v0]], [[manus-ai]]

---

## Recommended Implementation Approach

1. **사용자 세그먼트별 파일시스템 접근 계층을 설계해야 한다**: Claude의 듀얼 전략을 참고하여, 에이전트도 (1) 개발자/파워 유저를 위한 로컬 파일시스템 직접 접근 모드와, (2) 일반 업무 사용자를 위한 격리된 작업 공간 모드를 분리 설계해야 한다. 엔터프라이즈 맥락에서는 Microsoft Copilot처럼 데이터 레이어 추상화를 통한 간접 접근이 기본이 되어야 하며, 파일 직접 접근은 명시적 권한 부여 후에만 허용하는 계층 구조가 필요하다.

2. **Ephemeral Container 기반 코드 실행 환경을 기본 런타임으로 채택해야 한다**: Manus AI와 OpenAI Codex가 검증한 태스크별 독립 컨테이너 패턴은, 보안·격리·병렬 처리·장기 실행 모든 측면에서 이점이 크다. 에이전트가 데이터 분석, 보고서 생성, 코드 실행 등을 수행할 때 각 태스크를 독립 컨테이너에서 실행하고, 완료 후 산출물만 추출하는 아키텍처를 채택해야 한다. 특히 최대 실행 시간과 동시 태스크 수를 플랜별로 차별화하는 과금 설계도 함께 고려해야 한다.

3. **작업 디렉토리 표준 구조를 정의하고 에이전트에 명시적으로 주입해야 한다**: 경쟁사 분석에서 작업 디렉토리의 기준점(anchor)이 에이전트의 파일 조작 정확도를 결정한다는 점이 확인되었다. 에이전트 런타임에 표준 작업 디렉토리 구조(예: `/workspace/{task-id}/input/`, `/workspace/{task-id}/output/`, `/workspace/{task-id}/temp/`)를 정의하고, 에이전트 초기화 시 이 구조를 시스템 컨텍스트로 주입하여 파일 경로 혼동을 방지해야 한다.

4. **산출물 관리와 파일 지속성 전략을 명확히 해야 한다**: Manus AI의 14일 비동기 지속과 ChatGPT의 세션 한정 임시 파일이라는 두 극단 사이에서, 비즈니스 요구사항에 맞는 파일 지속성 정책을 수립해야 한다. 엔터프라이즈 컨텍스트에서는 에이전트가 생성한 산출물이 (1) Dataverse 등 중앙 저장소에 자동 보존되고, (2) 버전 관리되며, (3) 생성 경위(어떤 에이전트가, 어떤 입력을 기반으로, 어떤 단계에서 생성했는지)가 감사 로그에 기록되어야 한다.

5. **파일시스템 접근에 대한 거버넌스 레이어를 에이전트 런타임에 내장해야 한다**: Microsoft Copilot의 RBAC 기반 데이터 접근 제어를 참고하되, 파일시스템 수준에서도 (1) 에이전트별 접근 가능 경로 화이트리스트, (2) 파일 유형별 읽기/쓰기 권한, (3) 실행 가능 명령어 화이트리스트, (4) 파일 변경 감사 로그를 에이전트 런타임의 기본 기능으로 내장해야 한다. Claude Code의 diff 표시 + 위험 작업 승인 요청 패턴도 최소한의 안전장치로 참고할 수 있다.

---

## Source References

### 제품 프로필
- [[claude]] -- Claude Code의 로컬 파일시스템 직접 접근(cwd 기반 파일 탐색·편집·실행, diff 표시, 위험 작업 승인), Claude Cowork의 VM 샌드박스 파일 접근(허용 폴더 한정), Agentic Loop의 파일 I/O 도구 호출 패턴
- [[openai]] -- Codex의 클라우드 샌드박스(리포지토리 프리로드 → 독립 컨테이너 실행 → PR/diff 산출), ChatGPT Code Interpreter의 /mnt/data 임시 파일시스템, CUA 기반 브라우저 에이전트의 파일 다운로드/업로드 패턴
- [[manus-ai]] -- 클라우드 VM 전용 파일시스템(최대 14일 비동기 지속, 20개 동시 태스크), Glass Box를 통한 파일시스템 변경 실시간 관찰, Code Execution Agent의 Python/Shell 실행, 산출물(Artifact) 생성 및 추출
- [[vercel-v0]] -- 프로젝트 스코프 샌드박스(GitHub 리포지토리 클론 기반), Autonomous Terminal을 통한 의존성 설치·스크립트 실행, Next.js 프로젝트 구조 내 파일 생성·수정, Vercel 배포 파이프라인 연동
- [[microsoft-copilot]] -- Dataverse/Microsoft Graph 기반 데이터 레이어 간접 접근, Copilot Studio Python Code Interpreter, Power Platform 커넥터를 통한 외부 파일 시스템 연결, 1,000+ 커넥터 에코시스템

### UI 리서치
- 해당 없음

### 외부 참고 자료
- [OpenAI: Introducing Codex](https://openai.com/index/introducing-codex/) -- Codex 클라우드 샌드박스 아키텍처 상세
- [Manus AI 공식 사이트](https://manus.im) -- 클라우드 VM 실행 환경, 비동기 태스크 지속성
- [Claude Code 문서](https://code.claude.com/docs) -- 로컬 파일시스템 접근 패턴, diff 표시, 승인 프로세스
- [Vercel Blog: Introducing the new v0](https://vercel.com/blog/introducing-the-new-v0) -- Autonomous Terminal, 샌드박스 런타임
- [Microsoft Learn: Copilot for Finance and Operations Overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations) -- Dataverse 기반 데이터 접근 아키텍처

---

*Last synthesized: 2026-02-10 | Review: auto-trigger (Recent Updates 3건 이상 누적 시)*
