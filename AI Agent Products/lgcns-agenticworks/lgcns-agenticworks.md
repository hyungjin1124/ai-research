---
type: product-profile
product_id: lgcns-agenticworks
product_name: LG CNS AgenticWorks & a:xink
vendor: LG CNS
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
  - Korea-ERP
  - Full-Stack-AI
  - MCP
  - A2A
url: https://www.lgcns.com/
launched: 2025-08
last_updated: 2026-02-10
status: in-progress
related:
  - "[[douzone-one-ai/douzone-one-ai|더존 ONE AI]]"
  - "[[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]]"
  - "[[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]]"
---

# LG CNS AgenticWorks & a:xink

## 개요

LG CNS가 개발한 에이전틱 AI 풀스택 플랫폼으로, 6종 모듈형 플랫폼 'AgenticWorks(에이전틱웍스)'와 업무혁신 서비스 'a:xink(에이엑스씽크)'로 구성된다. 캐나다 AI 기업 코히어(Cohere)와의 기술 협력과 LG AI연구원의 엑사원(EXAONE) 모델을 기반으로 하며, MCP와 A2A 프로토콜을 지원하여 ERP·CRM 등 기간계 시스템을 수정하지 않고 AI 에이전트를 연결한다. 500여 개의 AX 프로젝트 경험을 바탕으로 산업별·밸류체인별 노하우를 축적하였으며, LG디스플레이 적용 시 일일 업무 생산성 10% 향상, 연간 100억 원 이상 비용 절감 효과를 실증했다.

| 항목 | 내용 |
|------|------|
| 회사 | LG CNS |
| 출시일 | 2025-08 (AgenticWorks & a:xink 공개) |
| 가격 | 비공개 (엔터프라이즈 구독 모델 추정) |
| 플랫폼 | DAP GenAI 플랫폼 기반 |
| 공식 사이트 | https://www.lgcns.com/ |

## 핵심 기능

- **AgenticWorks (6종 모듈 풀스택 플랫폼)**: 에이전틱 AI 서비스의 설계·구축·운영·관리 전 주기를 지원하는 국내 유일의 6종 모듈형 풀스택 플랫폼
  1. **빌더(Builder)**: 코딩 기반 에이전트 개발 환경
  2. **스튜디오(Studio)**: 노코드 에이전트 개발 환경
  3. **지식 저장소(Knowledge Lake)**: 데이터 전처리 및 지식 관리
  4. **허브(Hub)**: AI 에이전트와 기업 기간계 시스템(ERP·CRM 등) 연동 모듈
  5. **리파이너(Refiner)**: 모델 고도화 및 비용 효율 최적화
  6. **라우터(Router)**: 요청에 최적인 AI 모델 자동 선택
- **a:xink (업무혁신 서비스)**: 임직원 공통업무(일정, 회의, 메일, 번역 등)를 에이전틱 AI로 즉시 전환하는 7종 통합 서비스
- **자연어 업무 실행**: "오늘 회의록 기반으로 출장 결재를 만들고 주간보고에 추가해줘" 같은 복합 명령을 에이전트가 자율적으로 분업하여 ERP·그룹웨어와 연동 실행
- **데일리 브리핑**: 출근 시 음성 안내로 일정·미확인 메일·중요 공지 사항 자동 요약
- **회의 AI**: 실시간 다국어 통번역 및 자동 보고서 작성
- **AI 보안 솔루션 (SecureXper AI)**: 기업 시스템과 AI 에이전트 간 연결 포인트 전반에 내장된 보안 솔루션
- **마케팅 AI 에이전트**: 고객·타깃 분석에서 캠페인 실행까지 자동화하는 마케팅 전용 에이전트 (2025-11 출시)

## 아키텍처

### 기술 스택
| 구성 요소 | 설명 |
|-----------|------|
| DAP GenAI | LG CNS의 기업용 종합 생성형 AI 플랫폼. AgenticWorks의 기반 인프라 |
| LLM 엔진 | 코히어(Cohere) 모델 + LG AI연구원 엑사원(EXAONE) |
| AgenticWorks | 6종 모듈 풀스택 에이전틱 AI 플랫폼 |
| SecureXper AI | AI 보안 솔루션. 에이전트-시스템 연결 포인트 보안 |
| PerfecTwin | LG CNS의 디지털 트윈 ERP 솔루션 (SAP 파트너) |

### 에이전틱 아키텍처
```
[DAP GenAI Platform]
        ↓
[AgenticWorks 6종 모듈]
  ├─ Builder (코딩 개발)    ├─ Studio (노코드 개발)
  ├─ Knowledge Lake (지식)   ├─ Hub (시스템 연동)
  ├─ Refiner (모델 최적화)   └─ Router (모델 선택)
        ↓
[프로토콜 계층] MCP + A2A
        ↓
[기업 시스템 연동] ERP · CRM · 그룹웨어 · MES
        ↓
[보안 계층] SecureXper AI
```

### 에이전트 연동 방식
- **MCP (Model Context Protocol)**: AI 에이전트가 기업의 ERP·CRM 등 기간계 시스템의 데이터에 표준 프로토콜로 접근
- **A2A (Agent-to-Agent)**: 다수의 에이전트가 역할을 분담하여 복합 업무를 협업으로 처리
- **무수정 연동 (Zero-Modification)**: 기존 기업 시스템의 코드 수정이나 통합 코드 개발 없이 연결. 구축 시간과 비용 대폭 절감
- **허브(Hub) 모듈**: 시스템 연동 전담 모듈로 ERP·CRM·그룹웨어 등과의 커넥터 관리

### 외부 파트너 에코시스템
- **코히어(Cohere)**: 에이전틱 AI 기술 협력 파트너
- **LG AI연구원**: 엑사원(EXAONE) 모델 공급
- **SAP**: PerfecTwin ERP 에디션을 통한 SAP ERP 연동
- **클라인(Cline)**: 미국 AI 코딩 에이전트 기업과 차세대 에이전틱 AI 솔루션 공동 개발 (JDA 체결)

## UI·UX 분석

### a:xink 7종 통합 서비스
| 기능 | 설명 |
|------|------|
| 업무포털/그룹웨어 | 일정·결재·공지 등 통합 업무 허브 |
| 모바일 오피스 | 이동 중 업무 처리 앱 |
| 회의관리/지원 | AI 통번역, 자동 회의록, 화상회의 |
| AI 통번역 | 다국어 실시간 번역 |
| 문서작성 어시스턴트 | AI 기반 문서 자동 작성·교정 |
| 메신저 | 팀 커뮤니케이션 |
| Work&Life 슈퍼앱 | 공간관리·편의 서비스 통합 |

### 대화형 UI 패턴
- **자연어 → 멀티 에이전트 분업**: 하나의 자연어 명령을 여러 에이전트가 분담하여 ERP·그룹웨어 등 복수 시스템에서 자율 실행
- **데일리 브리핑 (음성)**: 매일 아침 음성으로 일정·메일·중요 사항 안내
- **개인화된 UI**: 사용자 업무 패턴에 맞춘 맞춤형 인터페이스
- **노코드 에이전트 빌더 (Studio)**: 비개발자도 에이전트를 설계·배포할 수 있는 시각적 인터페이스

## 경쟁 포지셔닝

### 강점
- **6종 모듈 풀스택**: 에이전트 개발(Builder/Studio) → 지식관리(Knowledge Lake) → 시스템연동(Hub) → 모델최적화(Refiner) → 모델선택(Router)까지 전 주기를 모듈화. 국내 유일의 6종 모듈형 풀스택 구조
- **MCP/A2A 조기 채택**: 글로벌 에이전트 표준 프로토콜을 조기 적용하여 기존 시스템 무수정 연동 가능. 삼성SDS와 함께 국내 양대 MCP/A2A 지원 플랫폼
- **실증된 ROI**: LG디스플레이 적용 시 일일 생산성 10% 향상, 연간 100억 원+ 비용 절감 효과 공개. 채용 업무 생산성 26% 개선
- **AI 보안 내재화 (SecureXper AI)**: 에이전트-시스템 연결 포인트 전반에 보안 솔루션을 자체 내장. 보안 우려를 선제적으로 해소
- **코히어 글로벌 협력**: 코히어와의 기술 파트너십으로 최신 에이전틱 AI 기술 빠르게 도입
- **500+ AX 프로젝트 경험**: 산업별·밸류체인별 노하우 축적으로 맞춤형 컨설팅 역량

### 약점
- **독립 ERP 미보유**: SAP 등 타사 ERP와의 연동에 의존. 더존처럼 자체 ERP 위에서 네이티브 AI를 제공하지 못함
- **중소기업 시장 부재**: 대기업·중견기업 중심 서비스로 중소기업 접근이 제한적
- **마켓플레이스 부재**: 에이전트를 제작·공유·구독하는 개방형 생태계 미구축
- **후발 출시**: 2025년 8월 공개로 더존 ONE AI(2024-04), 삼성SDS FabriX(2024-05) 대비 약 1년 후발
- **도메인 특화 에이전트 부족**: 한국 세무·회계·노동법 등 특화 에이전트는 더존 ONE AI에 비해 제한적

### 주요 경쟁사 비교
| 항목 | LG CNS AgenticWorks | 삼성SDS FabriX | 더존 ONE AI |
|------|---------------------|---------------|------------|
| 포지셔닝 | 에이전틱 AI 업무혁신 플랫폼 | AI 풀스택 기업 혁신 플랫폼 | 한국 중소기업 AI 비즈니스 플랫폼 |
| 핵심 AI | 6종 모듈 AgenticWorks + a:xink | 5종 퍼스널 에이전트 + FabriX | 도메인 특화 에이전트 + 마켓플레이스 |
| LLM | 코히어 + LG 엑사원 | 삼성 자체 LLM + GPT-4o + 오픈소스 | GPT-4o + LG 엑사원 |
| 타겟 | 대기업·중견기업 | 대기업·공공기관 | 한국 중소·중견기업 |
| 프로토콜 | MCP + A2A | MCP + A2A | 미공개 |
| 보안 | SecureXper AI 내장 | SCP 기반 보안 | 프라이빗 AI (PE) |
| 차별점 | 6종 모듈, AI 보안 내재화 | OpenAI 리셀러, 풀스택 인프라 | 자체 ERP 네이티브, 에이전트 마켓 |

## 관련 리서치

- [[samsung-sds-fabrix/samsung-sds-fabrix|삼성SDS FabriX]] — AI 풀스택 기업 혁신 플랫폼
- [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] — 한국 중소기업 ERP AI 에이전트
- [[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]] — 한국 중견기업 AI ERP

## 참고 자료

- [LG CNS 공식 사이트](https://www.lgcns.com/)
- ["똑똑한 AI 동료 만든다" LG CNS 에이전틱 AI 생태계 본격 가동 — LG](https://www.lg.co.kr/media/release/29289)
- [LG CNS, AX 역량 바탕으로 에이전틱 AI 생태계 확장 — 바이라인네트워크](https://byline.network/2025/08/82544/)
- [LG CNS unveils agentic AI to boost corporate productivity — Korea Herald](https://www.koreaherald.com/article/10561390)
- [LG CNS AgenticWorks: Full-Stack Modular Platform — AIM Research](https://aimresearch.co/market-briefs/lg-cns-agenticworks-platform-launch)
- [LG CNS, 마케팅 AI 에이전트 출시 — 머니투데이](https://www.mt.co.kr/tech/2025/11/19/2025111908591731571)
- [LG CNS, 코히어와 AI 에이전트 서비스 개발 — AI타임스](https://www.aitimes.com/news/articleView.html?idxno=168641)
- [LG CNS, 미국 클라인과 에이전틱 AI 솔루션 공동개발 — 스마트에프엔](https://www.smartfn.co.kr/news/articleView.html?idxno=130017)
- [LG CNS Debuts AI-Enhanced PerfecTwin ERP Edition — IT Tech Pulse](https://ittech-pulse.com/news/lg-cns-ai-perfectwin-erp-sapphire-2025/)
- ["기업용 종합 생성형 AI 솔루션" LG CNS DAP 젠AI — CIO](https://www.cio.com/article/3512705/)
