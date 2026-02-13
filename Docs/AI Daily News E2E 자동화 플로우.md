---
title: AI Daily News E2E 자동화 플로우
tags:
  - architecture
  - automation
---

# AI Daily News — E2E 자동화 플로우

## 전체 파이프라인

```mermaid
flowchart TD
    subgraph TRIGGER["TRIGGER"]
        A["⏰ macOS launchd<br/>매일 03:00 KST"]
    end

    subgraph SCRIPT["SHELL SCRIPT"]
        B["🔧 daily-news.sh<br/>로그 생성 · 폴더 확인"]
    end

    subgraph CLAUDE["CLAUDE CLI — /daily-news 6단계"]
        direction LR
        C1["1️⃣ RSS 수집<br/>20개 피드"]
        C2["2️⃣ 웹 검색<br/>14개 키워드"]
        C3["3️⃣ 분석·분류<br/>중복제거·중요도"]
        C1 --> C2 --> C3
    end

    subgraph VAULT["OBSIDIAN VAULT 파일 생성"]
        direction LR
        V1["4️⃣ 다이제스트 생성<br/>YYYY-MM-DD.md"]
        V2["5️⃣ 제품 업데이트<br/>_updates.md 삽입"]
        V3["6️⃣ 최종 검증<br/>스키마·링크 확인"]
        V1 --> V2 --> V3
    end

    subgraph GIT["GIT AUTO-PUSH"]
        D["📤 git add → commit → push<br/>ai-research repo → main"]
    end

    subgraph ACTIONS["GITHUB ACTIONS — 병렬 실행"]
        direction LR
        E1["⚡ notify-teams.yml<br/>다이제스트 요약 추출"]
        E2["⚡ deploy-pages.yml<br/>Quartz v4 빌드 · Node 22"]
    end

    subgraph DELIVERY["팀 전달"]
        direction LR
        F1["💬 Teams 채널<br/>Adaptive Card 알림"]
        F2["🌐 GitHub Pages<br/>hyungjin1124.github.io<br/>/ai-research"]
    end

    G["👥 팀원 — 자동 수신 & 열람"]

    A --> B --> CLAUDE
    C3 --> VAULT
    V3 --> D
    D --> E1
    D --> E2
    E1 --> F1
    E2 --> F2
    F1 --> G
    F2 --> G

    style TRIGGER fill:#1a1a2e,stroke:#e94560,color:#fff
    style SCRIPT fill:#16213e,stroke:#0f3460,color:#fff
    style CLAUDE fill:#0f3460,stroke:#533483,color:#fff
    style VAULT fill:#2d2d44,stroke:#d4a373,color:#fff
    style GIT fill:#1a1a2e,stroke:#e94560,color:#fff
    style ACTIONS fill:#161b22,stroke:#58a6ff,color:#fff
    style DELIVERY fill:#1e3a2f,stroke:#3fb950,color:#fff
```

## 데이터 흐름 상세

```mermaid
flowchart LR
    subgraph SOURCES["외부 데이터 소스"]
        R1["일반 AI 피드 15개<br/>Agent&Framework 5 · Deep Tech 3<br/>AI News 2 · OSS&Research 4<br/>Security&Eval 1"]
        R2["벤더별 피드 5개<br/>Microsoft · Salesforce<br/>SAP · Databricks · Vercel"]
        W1["일반 웹 검색 4개<br/>AI agent · LLM updates<br/>product launch · funding"]
        W2["타겟 검색 10개<br/>제품 그룹 5 · 주제 타겟 5"]
    end

    subgraph PROCESS["처리"]
        P1["중복 제거"]
        P2["중요도 판단<br/>🔴높음 🟡보통 🟢낮음"]
        P3["제품 매칭<br/>search_aliases 대조"]
    end

    subgraph OUTPUT["산출물"]
        O1["AI Daily News/<br/>YYYY/MM/YYYY-MM-DD.md"]
        O2["AI Agent Products/<br/>slug/slug_updates.md"]
    end

    R1 --> P1
    R2 --> P1
    W1 --> P1
    W2 --> P1
    P1 --> P2 --> P3
    P3 -->|전체 기사| O1
    P3 -->|높음 + 제품매칭| O2

    style SOURCES fill:#2d2d44,stroke:#7b2d8e,color:#fff
    style PROCESS fill:#0f3460,stroke:#533483,color:#fff
    style OUTPUT fill:#1e3a2f,stroke:#3fb950,color:#fff
```

## 컴포넌트 매핑

| 컴포넌트 | 파일 위치 | 역할 |
|----------|----------|------|
| **launchd** | `~/.claude/scripts/com.konachain.daily-news.plist` | 매일 03:00 KST 스케줄 트리거 |
| **Shell Script** | `~/.claude/scripts/daily-news.sh` | Claude CLI 호출 + Git auto-push |
| **Claude 커맨드** | `~/.claude/commands/daily-news.md` | 6단계 수집·분석·생성 워크플로 |
| **컨텍스트 (뉴스)** | `AI Daily News/_CONTEXT.md` | 구조 규칙, RSS 목록, Frontmatter 스키마 |
| **컨텍스트 (제품)** | `AI Agent Products/_CONTEXT.md` | 제품 레지스트리, search_aliases |
| **템플릿** | `AI Daily News/_TEMPLATE_daily-digest.md` | 다이제스트 파일 구조 |
| **Teams 알림** | `.github/workflows/notify-teams.yml` | Adaptive Card via Webhook |
| **웹 배포** | `.github/workflows/deploy-pages.yml` | Quartz v4 + GitHub Pages |
| **랜딩 페이지** | `index.md` | Quartz 사이트 홈 |

## 트리거 조건

```mermaid
flowchart TD
    A["daily-news.sh 실행"] --> B{Claude CLI 성공?}
    B -->|Exit 0| C{변경사항 있음?}
    B -->|Exit != 0| X["❌ 로그에 실패 기록<br/>파이프라인 중단"]
    C -->|git status --porcelain| D["git add -A<br/>git commit<br/>git push origin main"]
    C -->|변경 없음| Y["ℹ️ push 스킵"]
    D --> E{push 성공?}
    E -->|Yes| F["GitHub Actions 자동 트리거"]
    E -->|No| Z["⚠️ push 실패 로그"]
    F --> G["notify-teams.yml<br/>AI Daily News/** 변경 감지"]
    F --> H["deploy-pages.yml<br/>main 브랜치 push"]
    G --> I["Teams Webhook 전송"]
    H --> J["Quartz 빌드 → Pages 배포"]

    style X fill:#8b0000,stroke:#ff4444,color:#fff
    style Y fill:#4a4a00,stroke:#ffd166,color:#fff
    style Z fill:#8b4500,stroke:#ff8c00,color:#fff
    style I fill:#464775,stroke:#7b83eb,color:#fff
    style J fill:#1e3a2f,stroke:#3fb950,color:#fff
```
