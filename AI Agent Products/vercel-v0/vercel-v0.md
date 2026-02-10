---
type: product-profile
product_id: vercel-v0
product_name: Vercel v0
vendor: Vercel
category: B2C
tags:
  - AI-Agent
  - LLM-Native
  - Full-Stack-AI
url: https://v0.app
launched: 2023-09
last_updated: "2026-02-10"
status: in-progress
related: []
---

# Vercel v0

## 개요

Vercel이 개발한 AI 기반 프론트엔드/풀스택 코드 생성 플랫폼. 자연어 프롬프트를 입력하면 React + Next.js + Tailwind CSS + shadcn/ui 기반의 프로덕션 수준 UI 컴포넌트와 웹 애플리케이션을 즉시 생성한다. 2023년 9월 초기 출시 후, 2025년에는 자체 복합 모델(Composite Model) 아키텍처를 도입하고, 단순 UI 생성 도구에서 풀스택 AI 에이전트 빌더로 진화하였다. "Vibe Coding" 철학을 선도하며, 비개발자부터 전문 개발자까지 자연어만으로 웹 애플리케이션을 설계·구현·배포할 수 있는 엔드투엔드 워크플로우를 제공한다.

| 항목 | 내용 |
|------|------|
| 회사 | Vercel |
| 출시일 | 2023-09 (Public Preview), 2024-10 GA |
| 가격 | Free $0 (월 $5 크레딧) / Premium $20/월 ($20 크레딧) / Team $30/유저/월 / Enterprise 커스텀 |
| 플랫폼 | Web (v0.app) |
| 공식 사이트 | https://v0.app |

## 핵심 기능

- **자연어 → UI 코드 생성 (Text-to-UI)**: 사용자가 원하는 인터페이스를 자연어로 설명하면, React 컴포넌트 코드를 즉시 생성한다. shadcn/ui 컴포넌트 라이브러리와 Tailwind CSS를 기본으로 활용하여 일관된 디자인 시스템 기반의 프로덕션 수준 코드를 출력. 네비게이션 바, 히어로 섹션, 인증 화면, 대시보드, CRUD 폼 등 표준 UI 패턴에서 특히 강력한 성능을 발휘
- **Figma-to-Code**: Figma 링크나 스크린샷을 업로드하면, 시각 디자인을 고정밀(High-Fidelity) React 컴포넌트로 자동 변환한다. 디자이너의 시안을 개발자가 수작업으로 구현하는 과정을 대폭 단축
- **풀스택 AI 에이전트 빌더**: 2025년 이후 단순 UI 생성을 넘어, Next.js 애플리케이션 전체를 계획·코딩·배포하는 풀스택 빌더로 진화. GitHub 리포지토리를 직접 임포트하고, Vercel 환경변수·설정을 자동으로 가져와 프로덕션 환경에서 바로 동작하는 코드를 생성
- **자율 터미널 접근 (Autonomous Terminal)**: 보안 샌드박스 내에서 스크립트 실행, 의존성 설치, Node.js/Python 코드 실행이 가능하여, AI 에이전트가 단순 코드 생성을 넘어 빌드·테스트까지 자율적으로 수행
- **실시간 프리뷰 & 원클릭 배포**: 생성된 코드를 즉시 브라우저에서 프리뷰할 수 있으며, Vercel 플랫폼을 통해 원클릭으로 프로덕션 배포가 가능. Pull Request가 1급 시민(First-Class Citizen)으로 취급되며, 프리뷰가 실제 배포와 매핑
- **대화형 반복 수정 (Chat-based Iteration)**: 생성된 코드에 대해 채팅 인터페이스로 수정을 요청하고, 점진적으로 원하는 결과를 정제. 초기 생성 → 피드백 → 수정의 반복 사이클을 자연어로 수행

## 아키텍처

### 복합 모델 (Composite Model) 아키텍처
Vercel은 단일 LLM에 의존하지 않고, 세 가지 핵심 레이어를 결합한 복합 모델 아키텍처를 구축하였다:

1. **RAG (Retrieval-Augmented Generation) 레이어**: shadcn/ui, Tailwind CSS, Next.js 등 프레임워크별 최신 문서와 베스트 프랙티스를 검색·주입하여, LLM이 최신 API와 패턴을 정확하게 반영한 코드를 생성하도록 보장
2. **Base LLM 추론 레이어**: v0-1.0-md는 Anthropic Sonnet 3.7, v0-1.5-md는 Sonnet 4를 베이스 모델로 사용. 복합 아키텍처 덕분에 베이스 모델 업그레이드 시 나머지 스택은 안정적으로 유지
3. **AutoFix 후처리 모델**: 베이스 모델이 코드를 스트리밍 출력하는 동안, 커스텀 AutoFix 모델(vercel-autofixer-01)이 실시간으로 오류·비일관성·베스트 프랙티스 위반을 검출하고 수정. Fireworks AI와 협력하여 강화 미세조정(RFT, Reinforcement Fine-Tuning)으로 학습

### 모델 변형
- **v0-1.0-md**: 기본 모델 (128K 컨텍스트)
- **v0-1.5-md / v0-1.5-lg**: 대형 모델 (최대 512K 토큰 컨텍스트), 더 복잡한 풀스택 프로젝트에 적합

### 실행 환경
- **샌드박스 런타임**: 각 프롬프트마다 격리된 샌드박스에서 코드를 실행·프리뷰. GitHub 리포지토리를 임포트하면 실제 프로젝트 환경을 복제하여 프로덕션에 가까운 조건에서 코드를 생성
- **Vercel 배포 통합**: 생성된 코드가 Vercel의 배포 인프라와 네이티브로 통합되어, Preview → Staging → Production의 배포 파이프라인이 원클릭으로 작동

### 프로토콜/통합
- **Vercel AI SDK**: Vercel의 오픈소스 AI SDK와 긴밀히 연동되어, 생성된 프로젝트에 AI 기능(채팅, 스트리밍, 도구 사용 등)을 쉽게 통합 가능
- **GitHub 연동**: 리포지토리 임포트, PR 기반 워크플로우, 환경변수 자동 동기화
- **Next.js 생태계**: App Router, Server Components, Server Actions 등 Next.js의 최신 기능을 기본 지원

## UI·UX 분석

### 메인 인터페이스 구조
- **채팅 + 프리뷰 분할 레이아웃**: 좌측(또는 상단)의 채팅 패널에서 프롬프트를 입력하고, 우측(또는 하단)의 프리뷰 패널에서 생성된 UI를 실시간으로 확인하는 Two-Pane 구조. Manus AI의 Two-Pane과 유사하나, v0는 "코드 미리보기"에 초점을 맞추고 Manus는 "작업 과정 관찰"에 초점
- **코드 뷰어**: 생성된 코드를 직접 열람·복사할 수 있는 코드 탭 제공. 프리뷰와 코드를 토글하며 결과를 검증

### 반복 수정 패턴 (Iterative Refinement)
- **"Good First Draft" 철학**: v0의 핵심 UX 전략은 완벽한 결과를 한 번에 생성하는 것이 아니라, 빠르게 초안을 제시하고 대화형으로 정제하는 것. 사용자는 "여기에 다크 모드 추가해줘", "버튼 색상을 파란색으로 변경" 등 자연어로 점진적 수정을 요청
- **버전 히스토리**: 각 반복 결과를 버전으로 관리하여, 이전 버전으로 되돌아가거나 비교 가능

### HITL (Human-in-the-Loop) 패턴
- **프롬프트 기반 제어**: 전적으로 사용자의 프롬프트에 의해 방향이 결정되는 "지시형" HITL. Manus AI의 "관찰 후 개입" 방식과 대조적으로, v0는 매 턴마다 사용자가 명시적으로 다음 단계를 지시
- **비주얼 비교 검증**: 생성된 UI를 즉시 프리뷰로 확인하고, 원하는 방향과의 차이를 시각적으로 판단하여 다음 프롬프트를 결정

### 알려진 UX 한계
- **비주얼 에디터 부재**: Figma 같은 WYSIWYG 편집 기능이 없어, 디자인 수정은 항상 프롬프트를 통해야 함. 디자이너 관점에서 직관성이 떨어질 수 있음
- **디버깅 복잡성**: 복잡한 프로젝트에서 생성된 코드의 디버깅이 어려워지는 경우가 보고됨

## 경쟁 포지셔닝

### 강점
- **Next.js/React 생태계 최적화**: Vercel이 Next.js의 개발사인 만큼, Next.js 생태계에 가장 깊이 통합된 AI 코드 생성 도구. App Router, Server Components, Tailwind CSS, shadcn/ui 등 현대 React 스택과의 궁합이 가장 뛰어남
- **프로덕션 배포 통합**: 생성에서 배포까지 원스톱 워크플로우. 경쟁사(Bolt, Lovable 등)도 배포를 지원하나, Vercel의 글로벌 CDN 인프라 + Preview Deployment + 도메인 관리까지 네이티브로 통합된 것은 v0만의 차별점
- **복합 모델 아키텍처**: RAG + Base LLM + AutoFix의 3단 파이프라인으로 코드 품질을 보장. 단일 LLM만 사용하는 경쟁사 대비 오류율이 낮고, 베스트 프랙티스 준수율이 높음
- **GitHub 워크플로우 통합**: PR 기반 코드 리뷰, 브랜치 관리 등 기존 개발 워크플로우와 자연스럽게 연결. 팀 단위 협업 시나리오에서 강점
- **"Vibe Coding" 트렌드 선도**: 자연어로 코딩하는 새로운 패러다임을 대중화시킨 핵심 제품 중 하나

### 약점
- **프론트엔드 편중**: 역사적으로 UI/프론트엔드에 특화되어 있어, 백엔드·데이터베이스·인증 등 풀스택 기능은 Bolt, Lovable 대비 상대적으로 약함. 2025년 이후 풀스택 지원을 강화 중이나 아직 따라잡는 중
- **Vercel 종속성**: 생성된 코드와 배포 워크플로우가 Vercel 플랫폼에 밀접하게 결합되어 있어, 다른 클라우드/호스팅 환경으로의 이식성이 제한적
- **React/Next.js 한정**: Vue, Svelte, Angular 등 다른 프레임워크 지원이 없어, 비-React 프로젝트에는 활용이 불가
- **크레딧 소진 문제**: 크레딧 기반 과금에서 복잡한 프로젝트의 반복 수정 시 크레딧이 빠르게 소진될 수 있음
- **자체 LLM 미보유**: 베이스 모델을 외부(Anthropic)에 의존하여, 모델 성능 발전에 대한 직접적 통제력이 제한적. 단, 복합 아키텍처로 베이스 모델 교체가 용이

### 주요 경쟁사 비교
| 항목 | Vercel v0 | Bolt.new | Lovable | Cursor |
|------|-----------|----------|---------|--------|
| 제품 유형 | AI UI/풀스택 빌더 | AI 풀스택 빌더 | AI 풀스택 앱 빌더 | AI 코딩 어시스턴트 (IDE) |
| 기술 스택 | React/Next.js + Tailwind + shadcn/ui | 다양한 프레임워크 | React + Supabase | 스택 무관 (IDE) |
| 배포 | Vercel 네이티브 (원클릭) | Netlify 기반 | 자체 호스팅 | 사용자 직접 배포 |
| 백엔드 지원 | Next.js API Routes (제한적) | Supabase 내장 | Supabase 내장 | 풀 자유도 |
| 대상 사용자 | React 개발자, 디자이너, PM | 비개발자~개발자 | 비개발자~초급 개발자 | 전문 개발자 |
| 가격 (기본 유료) | $20/월 | $20/월 | $20/월 | $20/월 |
| 차별점 | Next.js 생태계 최적화 + 프로덕션 배포 | 제로 셋업 브라우저 개발 | 가장 빠른 풀스택 MVP | IDE 통합, 스택 무관 |

## 관련 리서치

<!-- 기존 노트 wikilink -->

## 참고 자료

- [v0 공식 사이트](https://v0.app)
- [v0 가격 정책](https://v0.app/pricing)
- [Vercel Blog: Introducing the v0 composite model family](https://vercel.com/blog/v0-composite-model-family)
- [Vercel Blog: Introducing the new v0](https://vercel.com/blog/introducing-the-new-v0)
- [Vercel Blog: Announcing v0 — Generative UI](https://vercel.com/blog/announcing-v0-generative-ui)
- [TechCrunch: Vercel debuts an AI model optimized for web development](https://techcrunch.com/2025/05/22/vercel-debuts-an-ai-model-optimized-for-web-development/)
- [Vercel Academy: UI with v0](https://vercel.com/academy/ai-sdk/ui-with-v0)
- [DataCamp: v0 by Vercel Guide](https://www.datacamp.com/tutorial/vercel-v0)
