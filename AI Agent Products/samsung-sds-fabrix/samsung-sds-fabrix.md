---
type: product-profile
product_id: samsung-sds-fabrix
product_name: 삼성SDS FabriX & Brity Copilot
vendor: 삼성SDS
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
  - Korea-ERP
  - Full-Stack-AI
  - MCP
  - A2A
url: https://www.samsungsds.com/
launched: 2024-05
last_updated: 2026-02-10
status: in-progress
related:
  - "[[douzone-one-ai/douzone-one-ai|더존 ONE AI]]"
  - "[[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]]"
  - "[[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]]"
---

# 삼성SDS FabriX & Brity Copilot

## 개요

삼성SDS가 개발한 기업용 AI 풀스택 플랫폼으로, 생성형 AI 플랫폼 'FabriX(패브릭스)'와 협업 AI 솔루션 'Brity Copilot(브리티 코파일럿)'을 중심으로 ERP·CRM·SCM·MES 등 기간계 시스템과 AI 에이전트를 네이티브로 연결한다. MCP(Model Context Protocol)와 A2A(Agent-to-Agent) 프로토콜을 적용하여 다수의 AI 에이전트가 협력하며 복잡한 기업 업무를 자동으로 처리하는 에이전틱 AI 아키텍처를 구현한다. CES 2026에서 'AI 에이전트 기반 일하는 방식의 전환'을 선언하며, 약 20만 명의 사용자 기반을 확보했다.

| 항목 | 내용 |
|------|------|
| 회사 | 삼성SDS |
| 출시일 | 2024-05 (FabriX & Brity Copilot 출시), 2025-09 (REAL Summit 2025 에이전트 전략 공개) |
| 가격 | 비공개 (엔터프라이즈 구독 모델, Azure Marketplace에서도 제공) |
| 플랫폼 | Samsung Cloud Platform (SCP) + AWS/Azure/GCP/OCI 멀티클라우드 |
| 공식 사이트 | https://www.samsungsds.com/ |

## 핵심 기능

- **FabriX 생성형 AI 플랫폼**: 다양한 언어모델(삼성 자체 LLM + GPT-4o + 오픈소스)과 기업 시스템을 원활하게 연결하는 생성형 AI 플랫폼. 기업이 AI 에이전트를 제작·공유·활용할 수 있는 기반 인프라
- **5종 퍼스널 에이전트**: 브리핑(일정·메일·뉴스 종합), 인터프리팅(60개 언어 실시간 통역), 큐레이팅(맥락 기반 자료 추천), 보이스(음성 명령 업무 처리), 앤서링(부재 시 자동 응답)
- **딥 리서치 에이전트**: 내부 ERP·CRM 주요 데이터와 외부 논문·특허 데이터를 결합하여 보안성 갖춘 맞춤형 보고서를 자동 생성
- **Brity Meeting (AI 회의 솔루션)**: 95% 이상 음성 인식 정확도, 60개 이상 언어 실시간 자막 및 번역, 화자 구분 기능
- **Brity Automation (업무 자동화)**: AI 에이전트 기반 비즈니스 프로세스 자동화. RPA와 생성형 AI를 결합한 지능형 자동화
- **에이전틱 봇 (Agentic Bot)**: 입력·UI 변화에 대한 자동 대응, 지능형 문서 인식, 동적 시나리오 처리가 가능한 차세대 자동화 봇

## 아키텍처

### 기술 스택
| 구성 요소 | 설명 |
|-----------|------|
| Samsung Cloud Platform (SCP) | 삼성SDS 자체 클라우드 인프라. NVIDIA B300 GPU 통합 |
| 멀티클라우드 | AWS, Azure, GCP, OCI 등 주요 퍼블릭 클라우드 연동 |
| FabriX | 생성형 AI 플랫폼. 멀티 LLM + 기업 시스템 연동 허브 |
| LLM 엔진 | 삼성 자체 LLM + OpenAI GPT-4o + 오픈소스 모델. OpenAI ChatGPT Enterprise 국내 최초 리셀러 |
| Brity Works | 그룹웨어·협업 플랫폼 (메일, 메신저, 캘린더, 드라이브 등) |
| Brity Copilot | Brity Works 위에서 작동하는 AI 코파일럿. 퍼스널 에이전트 포함 |
| Brity Automation | RPA + 생성형 AI 기반 프로세스 자동화 |

### AI 풀스택 아키텍처
```
[Infrastructure] Samsung Cloud Platform (SCP) + 멀티클라우드
        ↓
[Platform]       FabriX (멀티 LLM + MCP + A2A)
        ↓
[Solutions]      Brity Copilot / Brity Automation / Brity Meeting
        ↓
[Integration]    ERP · CRM · SCM · MES · 그룹웨어 연동 (MCP/A2A)
```

### 에이전트 아키텍처
- **MCP (Model Context Protocol)**: LLM이 기업 내부 ERP·CRM·문서 시스템의 데이터에 안전하게 접근하는 표준 프로토콜
- **A2A (Agent-to-Agent)**: 여러 AI 에이전트 간 안전한 통신과 협업을 가능하게 하는 개방형 프로토콜
- **기존 시스템 무수정 연동**: 기업의 기간계 시스템(ERP, SCM, MES, CRM)을 수정하지 않고 AI 에이전트가 직접 연결
- **권한/인증 연계**: 사내 시스템의 권한·인증 체계를 에이전트가 그대로 활용하여 보안 유지

### 외부 파트너 에코시스템
- **OpenAI**: 국내 최초 ChatGPT Enterprise 리셀러 파트너
- **SAP**: ERP 전환 전략적 파트너십
- **Salesforce / Workday**: CRM·HR 솔루션 연동
- **Upstage**: 한국어 특화 AI 모델 협력

## UI·UX 분석

### 메인 인터페이스 구성
- **Brity Works 통합 UI**: 메일, 메신저, 캘린더, 드라이브, 화상회의가 하나의 협업 플랫폼에서 유기적으로 연결
- **AI 코파일럿 패널**: Word, Excel, PowerPoint 등 Office 문서 작업 중 AI 지원을 인라인으로 제공

### 퍼스널 에이전트 인터랙션
- **자연어 명령 → 업무 실행**: "오늘 주요 일정과 미확인 메일 브리핑해줘" 같은 자연어 입력으로 에이전트가 자동 실행
- **음성 인터페이스**: 외근·이동 중에도 음성으로 메일 확인·답장·일정 관리
- **자동 대리 응답**: 회의·집중 업무 중 동료의 질문에 에이전트가 자동 대응

### 데이터 시각화
- **딥 리서치 보고서**: ERP·CRM 데이터와 외부 데이터를 결합한 자동 생성 보고서
- **회의 자동 요약**: 화상회의 후 핵심 내용·액션 아이템 자동 정리

## 경쟁 포지셔닝

### 강점
- **AI 풀스택 역량**: 인프라(SCP) → 플랫폼(FabriX) → 솔루션(Brity) → 컨설팅까지 전 영역 자체 보유. 국내 유일의 AI 풀스택 제공자
- **MCP/A2A 표준 지원**: 글로벌 에이전트 상호운용 표준을 조기 채택하여 기존 기간계 시스템 무수정 연동 가능
- **OpenAI 공식 파트너**: 국내 유일 OpenAI 리셀러 파트너로서 최신 AI 모델 접근 우위
- **삼성 그룹사 실전 검증**: 삼성 계열사 전체 업무에 적용하여 일일 5시간 20분 업무 시간 절감 실증 (67% 감소)
- **대기업·공공 레퍼런스**: KB금융그룹, S-OIL, 서울시 등 대규모 고객 확보. 300+ 공공기관 클라우드 전환 수행
- **20만 사용자 기반**: 브리티 코파일럿 약 20만 명 사용, 절반가량이 실업무 활용

### 약점
- **중소기업 시장 부재**: 대기업·공공기관 중심 포지셔닝으로 중소기업 시장 접근이 제한적 (더존 ONE AI와 대비)
- **독립 ERP 미보유**: 자체 ERP 제품 없이 SAP·Oracle 등 타사 ERP와의 연동에 의존. ERP 네이티브 AI 대비 통합 깊이 한계
- **한국어 특화 도메인 AI**: 더존 대비 한국 세무·회계·노동법 등 도메인 특화 AI 에이전트 부족
- **마켓플레이스 부재**: 더존의 에이전트 마켓플레이스 같은 개방형 에이전트 생태계 미구축
- **가격 문턱**: 대기업·공공 타겟 솔루션으로 중견·중소기업 도입 비용 부담

### 주요 경쟁사 비교
| 항목 | 삼성SDS FabriX | 더존 ONE AI | LG CNS AgenticWorks |
|------|---------------|------------|---------------------|
| 포지셔닝 | AI 풀스택 기업 혁신 플랫폼 | 한국 중소기업 AI 비즈니스 플랫폼 | 에이전틱 AI 업무혁신 플랫폼 |
| 핵심 AI | 5종 퍼스널 에이전트 + FabriX | 도메인 특화 에이전트 + 마켓플레이스 | 6종 모듈 AgenticWorks + a:xink |
| LLM | 삼성 자체 LLM + GPT-4o + 오픈소스 | GPT-4o + LG 엑사원 | 코히어 + LG 엑사원 |
| 타겟 | 대기업·공공기관 | 한국 중소·중견기업 | 대기업·중견기업 |
| 프로토콜 | MCP + A2A | 미공개 | MCP + A2A |
| ERP 연동 | SAP/Oracle 등 타사 ERP 연동 | 자체 ERP (위하고) 네이티브 | SAP 등 타사 ERP 연동 |
| 차별점 | OpenAI 리셀러, 풀스택 인프라 | 에이전트 마켓플레이스, 프라이빗 AI | 코히어 협력, AI 보안 내재화 |

## 관련 리서치

- [[douzone-one-ai/douzone-one-ai|더존 ONE AI]] — 한국 중소기업 ERP AI 에이전트
- [[lgcns-agenticworks/lgcns-agenticworks|LG CNS AgenticWorks]] — 에이전틱 AI 업무혁신 플랫폼
- [[younglimwon-ksystem/younglimwon-ksystem|영림원 K-System]] — 한국 중견기업 AI ERP

## 참고 자료

- [삼성SDS 공식 사이트](https://www.samsungsds.com/)
- [삼성SDS "브리티 코파일럿으로 AI 개인 비서 시대 연다" — ZDNet](https://zdnet.co.kr/view/?no=20251001151603)
- [삼성SDS, AI 에이전트 기반 기업 혁신 전략 REAL Summit 2025 — 삼성SDS](https://www.samsungsds.com/kr/news/realsummit-250911.html)
- [Samsung SDS Declares AI-Agent-Driven AI Transformation at CES 2026 — Samsung SDS](https://www.samsungsds.com/en/news/ces2026-260112.html)
- [삼성SDS '패브릭스', 에이전틱AI 공략 키워드는 '맞춤형' — Bloter](https://www.bloter.net/news/articleView.html?idxno=643839)
- [삼성SDS, 생성형 AI 서비스 'FabriX 및 Brity Copilot' 출시 — 뉴스와이어](https://www.newswire.co.kr/newsRead.php?no=989024)
- [삼성SDS AI Journey — 삼성SDS 인사이트](https://www.samsungsds.com/kr/insights/samsung-sds-ai-journey.html)
- [Samsung SDS FabriX on Azure — Azure Marketplace](https://azuremarketplace.microsoft.com/ko-kr/marketplace/consulting-services/samsungsds1730787947038.samsungsds_fabrixonazure)
- [이준희 삼성SDS 대표 "신뢰할 수 있는 AI 에이전트 구현" — CIO](https://www.cio.com/article/4055460/)
