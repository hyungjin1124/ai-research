---
type: product-updates
product_id: vercel-v0
tags:
  - AI-Agent
  - updates-log
last_appended: "2026-02-12"
---

# Vercel v0 업데이트 로그

<!--
  APPEND RULE: 새 엔트리는 UPDATES_END 마커 바로 위에 추가합니다.
  각 엔트리는 아래 형식을 따릅니다:

  ### YYYY-MM-DD | 제목
  **소스**: [기사 제목](URL)
  **요약**: 1~3문장 요약
  **카테고리**: 신기능 | 가격변경 | 파트너십 | 기술업데이트 | 실적 | 기타
  **영향도**: 높음 | 보통 | 낮음

  AI 에이전트가 자동 append할 때 frontmatter의 last_appended도 함께 갱신합니다.
-->

<!-- UPDATES_START -->

### 2025-05-22 | v0 복합 모델(Composite Model) 아키텍처 공개

**소스**: [Vercel debuts an AI model optimized for web development](https://techcrunch.com/2025/05/22/vercel-debuts-an-ai-model-optimized-for-web-development/)
**요약**: Vercel이 v0-1.0-md 모델을 공개하며 RAG + Base LLM(Sonnet 3.7) + AutoFix 후처리 모델로 구성된 복합 모델 아키텍처를 발표. 이후 v0-1.5-md(Sonnet 4 기반)로 업그레이드. 웹 개발 특화 AI 모델로서 코드 품질과 베스트 프랙티스 준수율을 대폭 향상.
**카테고리**: 기술업데이트
**영향도**: 높음

### 2024-10-15 | v0 GA 출시 및 주요 기능 업데이트

**소스**: [Live from launch day: Discover what's new with v0](https://vercel.com/go/v0-launch-virtual-session)
**요약**: v0가 퍼블릭 프리뷰를 거쳐 정식 출시(GA). 도메인이 v0.dev에서 v0.app으로 이전되며, 풀스택 빌더 방향으로 확장.
**카테고리**: 신기능
**영향도**: 높음

### 2023-09-01 | v0 초기 출시 (Public Preview)

**소스**: [Announcing v0: Generative UI](https://vercel.com/blog/announcing-v0-generative-ui)
**요약**: Vercel이 AI 기반 UI 생성 도구 v0를 퍼블릭 프리뷰로 발표. 첫 3주 만에 10만 명 이상이 대기자 명단에 등록하며 높은 관심을 받음.
**카테고리**: 신기능
**영향도**: 높음

### 2026-02-11 | MCP 서버에 런타임 로그 접근 + CLI 에이전트 최적화
**소스**: [Agents can now access runtime logs with Vercel's MCP server](https://vercel.com/changelog/agents-can-now-access-runtime-logs-with-vercels-mcp-server)
**요약**: Vercel MCP 서버에 `get_runtime_logs` 도구 추가. 에이전트가 Functions 배포 전반의 런타임 로그 조회 가능. `vercel logs` CLI도 에이전트 워크플로우 최적화(히스토리컬 로그, Git 컨텍스트 자동 인식).
**카테고리**: 신기능
**영향도**: 보통

### 2026-02-12 | GLM-5 AI Gateway 추가 + Sandbox 방화벽 + Flags 공개 베타
**소스**: [GLM-5 is live on AI Gateway](https://vercel.com/changelog/glm-5-is-live-on-ai-gateway)
**요약**: (1) GLM-5를 AI Gateway에 추가, (2) Sandbox에 SNI 필터링+CIDR 블록 기반 egress 방화벽 추가로 데이터 유출 방지, (3) Flags 공개 베타($30/1M flag requests)로 Next.js/SvelteKit 피처 플래그 제공.
**카테고리**: 신기능
**영향도**: 보통

<!-- UPDATES_END -->
