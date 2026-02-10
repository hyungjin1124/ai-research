---
type: product-profile
product_id: oracle-digital-assistant
product_name: Oracle Digital Assistant
vendor: Oracle
category: Enterprise
tags:
  - AI-Agent
  - Enterprise
  - ERP-Integrated
url: https://www.oracle.com/chatbots/
launched: 2018-10
last_updated: 2026-02-09
status: in-progress
related:
  - "[[엔터프라이즈 AI 서비스 비교 분석]]"
  - "[[리서치 목표 및 벤치마크 대상]]"
---

# Oracle Digital Assistant

## 개요

Oracle이 개발한 대화형 AI 플랫폼으로, Oracle Cloud 에코시스템(ERP, HCM, SCM, CX, PeopleSoft) 전반에 걸쳐 챗봇 및 AI 에이전트를 제공한다. 2018년 출시로 엔터프라이즈 AI 에이전트 제품군 중 가장 긴 역사를 가지며, Skills 기반 모듈형 아키텍처가 핵심이다. 하나의 Digital Assistant가 여러 개의 Skills(개별 봇)을 호스팅하여 다양한 업무 도메인을 단일 대화 인터페이스에서 처리한다. Visual Flow Designer를 통한 로코드 대화 설계, 자체 NLU(Natural Language Understanding) 엔진, 35개 이상의 Oracle Cloud 사전 구축 Skills, 그리고 2025년부터 LLM 블록을 통한 GenAI 통합을 지원한다. 멀티채널 배포(Web, Mobile, Slack, Teams, WhatsApp, 음성)와 다국어 Zero-shot NLU를 갖추어, Oracle Cloud 고객을 위한 통합 대화형 인터페이스로 포지셔닝하고 있다.

| 항목 | 내용 |
|------|------|
| 회사 | Oracle |
| 출시일 | 2018-10 (ODA), 2024+ (LLM/GenAI 통합) |
| 가격 | 세션 기반 과금: 1,000 Sessions 단위, 최소 시간당 250 Requests 소비 (세부 단가 비공개, Oracle Cloud 가격표 참조) |
| 플랫폼 | Web, Mobile, Slack, Microsoft Teams, WhatsApp, 음성 (Oracle Cloud Infrastructure 기반) |
| 공식 사이트 | https://www.oracle.com/chatbots/ |

## 핵심 기능

- **Skills 기반 모듈형 아키텍처**: 각 Skills은 특정 업무 도메인(ERP, HCM, SCM, CX)에 특화된 독립 봇으로, 하나의 Digital Assistant가 복수의 Skills을 호스팅. 사용자 발화에서 의도(Intent)를 파악하여 적절한 Skill로 자동 라우팅. Skill Store에서 사전 구축 Skills을 검색·설치 가능
- **Visual Flow Designer**: YAML 기반 레거시 디자이너를 대체하는 로코드 비주얼 대화 설계 도구. 캔버스 위에 상태(State) 타일을 배치하고 연결선으로 대화 흐름을 설계. 모듈형 재사용 가능한 플로우를 분리 설계할 수 있어 복잡한 대화 시나리오를 관리 가능
- **LLM 블록 통합 (GenAI)**: Invoke Large Language Model 컴포넌트를 통해 대화 흐름 내에서 REST 호출로 LLM에 접근. Oracle GenAI, Cohere, Meta 등 다양한 LLM을 호출 가능. 중앙 집중형 프롬프트 관리로, Flow Designer를 수정하지 않고도 프롬프트를 일괄 업데이트
- **Multi-Agent 아키텍처**: ODA를 오케스트레이터로 활용하여 복수의 AI 에이전트를 관리. 에이전트가 도구(Tools), 지식 베이스(Knowledge Base), 다른 에이전트를 자율적으로 호출하는 Supervisor 패턴 지원. 단순 구조부터 복잡한 계층형 에이전트 구조까지 확장 가능
- **35+ 사전 구축 Skills**: Oracle Cloud ERP, SCM, HCM, CX, PeopleSoft용 사전 구축 AI 기반 트랜잭션 Skills 제공. 경비 승인, 구매 요청, 직원 셀프서비스, 고객 서비스 등 즉시 배포 가능한 대화형 워크플로우
- **Zero-shot 다국어 NLU**: 아랍어, 네덜란드어, 영어, 프랑스어, 독일어, 이탈리아어, 포르투갈어, 스페인어를 네이티브 지원. 추가 학습 데이터 없이 다국어 의도 인식 수행
- **이벤트 기반 워크플로우 자동화**: AI 에이전트가 ODA 내부 또는 외부 워크플로우 엔진의 워크플로우를 트리거·관리. HR, IT, 고객 지원 프로세스에서 동적이고 반응형인 이벤트 기반 자동화 제공

## 아키텍처

### Skills 기반 구조
| 구성 요소 | 역할 |
|-----------|------|
| Digital Assistant | 사용자 대화 진입점. 복수 Skills을 호스팅하고 Intent 기반 라우팅 수행 |
| Skills | 특정 도메인 업무를 처리하는 독립 봇 (ERP Skill, HCM Skill, SCM Skill 등) |
| Visual Flow Designer | 대화 흐름을 시각적으로 설계하는 로코드 캔버스 도구 |
| NLU Engine | Intent 인식, Entity 추출, 컨텍스트 관리를 수행하는 자연어 이해 엔진 |
| LLM Block | GenAI 기능을 대화 흐름에 주입하는 REST 기반 LLM 호출 컴포넌트 |

### NLU 처리 파이프라인
1. **Intent Resolution**: 사용자 발화에서 의도를 파악하여 해당 Skill로 라우팅. 신뢰도 점수(Confidence Score) 기반 판단
2. **Entity Extraction**: 트랜잭션 세부 정보(날짜, 금액, 직원명 등)를 자연어 입력에서 추출
3. **Context Handling**: 멀티턴 대화에서 이전 발화 컨텍스트를 유지하여 복잡한 요청을 단계적으로 처리
4. **Composite Bag Resolution**: 복합 엔터티(여러 필드로 구성된 데이터)를 대화를 통해 점진적으로 수집
5. **UnresolvedIntent Trigger**: 의도를 파악할 수 없는 경우 폴백 처리 또는 LLM 블록으로 전환

### Multi-Agent 아키텍처
- **Simple Agent**: 단일 LLM 블록 + 도구 호출로 구성된 기본 에이전트
- **Supervisor Agent**: 상위 에이전트가 하위 에이전트 팀을 관리하며, 사용자 요청에 따라 적절한 하위 에이전트에 태스크를 위임
- **도구 통합**: REST API, 데이터베이스, 외부 클라우드 서비스를 에이전트의 도구(Tool)로 등록하여 자율적으로 호출
- **지식 베이스 연동**: RAG(Retrieval Augmented Generation) 패턴으로 문서·FAQ를 검색하여 LLM 응답의 정확도 향상

### Oracle Cloud 에코시스템 통합
- **Oracle Cloud ERP**: 경비 보고서 제출, 구매 요청 승인, 계정 조회, 결산 지원
- **Oracle Cloud HCM**: 직원 셀프서비스(휴가 신청, 급여 명세 조회, 복리후생), 온보딩 안내
- **Oracle Cloud SCM**: 재고 조회, 주문 추적, GPS 기반 운송 모니터링
- **Oracle Cloud CX**: 고객 문의 자동 응답, 케이스 생성, 서비스 요청 라우팅
- **Oracle PeopleSoft**: 레거시 PeopleSoft 시스템 연동용 사전 구축 Skills 제공
- **Oracle Integration Cloud**: 서드파티 시스템과의 REST/SOAP 기반 통합 허브

### 멀티채널 배포
- Web Chat Widget (커스터마이즈 가능)
- Mobile SDK (iOS, Android)
- Microsoft Teams, Slack 네이티브 커넥터
- WhatsApp Business, Facebook Messenger
- 음성 채널 (IVR 연동)
- Oracle Service Cloud 임베딩

## UI·UX 분석

### 메인 인터페이스 구성
- **Skills 기반 대화 인터페이스**: 사용자가 자연어로 질의하면, Digital Assistant가 적절한 Skill을 자동 선택하여 응답. 복수 도메인(ERP, HR, CX)을 단일 대화 창에서 처리
- **Visual Flow Designer (관리자용)**: 캔버스 기반 드래그 앤 드롭 대화 설계 도구. 상태 타일 간 연결선으로 대화 분기·반복·조건을 시각화. 레거시 YAML 방식 대비 직관성과 재사용성이 크게 향상
- **Skill Store (저장소)**: 사전 구축 Skills과 커스텀 Skills을 검색·설치·관리하는 카탈로그 인터페이스

### 대화형 UI 패턴
- **Intent-Entity Recognition**: 사용자 발화에서 의도와 핵심 데이터를 자동 추출하여 구조화된 트랜잭션으로 변환
- **멀티턴 대화**: 복잡한 프로세스(경비 보고서 작성, 채용 요청)를 여러 턴에 걸쳐 필요한 정보를 점진적으로 수집
- **컨텍스트 기반 응답**: 이전 대화 내용을 기반으로 후속 질문에 자동 응답. 도메인 간 컨텍스트 전환도 처리

### Human-in-the-Loop 패턴
- **Expense Approval Workflows**: AI가 경비 보고서를 자동 분류·검증한 후, 승인권자에게 검토 요청. 영수증 사진 첨부 및 정책 준수 여부 자동 점검
- **Receipt Photo + Review**: 사용자가 영수증 사진을 업로드하면 AI가 OCR로 데이터를 추출하고, 인간이 확인·수정
- **Policy Compliance Check**: AI가 트랜잭션을 자동 분석하여 정책 위반 항목을 플래그하고, 관리자에게 검토 요청

### 데이터 시각화
- **Oracle Cloud ERP Dashboards**: ERP 데이터를 대화 컨텍스트에서 직접 대시보드 형태로 표시. 계정 잔액, 예산 현황, 구매 내역 등
- **GPS Tracking (Transportation)**: SCM 연동으로 운송 현황을 실시간 GPS 추적으로 시각화
- **Account Reconciliation Views**: 계정 대사(Reconciliation) 결과를 테이블·요약 카드로 표시
- **Dialog Flow Canvas**: 관리자가 대화 흐름의 상태 전이를 시각적으로 모니터링

## 경쟁 포지셔닝

### 강점
- **Oracle Cloud 네이티브 통합의 깊이**: ERP, HCM, SCM, CX, PeopleSoft 전 제품군에 걸쳐 35개 이상의 사전 구축 Skills 제공. Oracle Cloud 고객은 별도 개발 없이 즉시 대화형 AI를 업무에 적용 가능
- **Skills 기반 모듈형 설계**: 도메인별 독립 Skills을 조합하는 구조로, 필요한 업무 영역만 선택적으로 AI를 적용할 수 있어 단계적 도입에 유리. 재사용 가능한 플로우 모듈로 유지보수 효율 향상
- **Visual Flow Designer 성숙도**: 비주얼 캔버스 기반 로코드 대화 설계 도구가 충분히 성숙하여, 비개발자도 복잡한 대화 시나리오를 설계·수정 가능. Point-and-click 방식으로 진입 장벽 낮음
- **Zero-shot 다국어 NLU**: 8개 언어를 추가 학습 데이터 없이 네이티브 지원. 글로벌 기업의 다국어 서비스 배포에 강점
- **LLM 유연성**: LLM 블록을 통해 Oracle GenAI, Cohere, Meta 등 다양한 LLM을 대화 흐름 내에서 호출 가능. 중앙 프롬프트 관리로 운영 편의성 확보
- **Multi-Agent Supervisor 패턴**: ODA를 오케스트레이터로 활용한 계층형 멀티 에이전트 구조 지원으로, 복잡한 엔터프라이즈 자동화 시나리오에 대응

### 약점
- **MCP/A2A 프로토콜 미지원**: Workday(MCP+A2A), Google(A2A)과 달리 개방형 에이전트 간 통신 프로토콜을 채택하지 않음. Oracle 에코시스템 외부와의 에이전트 상호운용성이 제한적
- **Agentic AI 후발 주자**: 2018년 출시의 긴 역사에도 불구하고, LLM/GenAI 통합은 2024-2025년에 추가된 비교적 최신 기능. ServiceNow(AI Agent Orchestrator), Salesforce(Atlas Engine) 대비 Agentic AI 전략 발표가 늦음
- **Generative UI 부재**: 응답 포맷이 텍스트·카드·버튼 중심의 전통적 챗봇 UI. Google Gemini의 Dynamic View나 Salesforce의 인터랙티브 에이전트 UI 대비 제한적
- **독립적 AI 브랜딩 약세**: ServiceNow(Now Assist), Salesforce(Agentforce), SAP(Joule), Workday(Illuminate) 등 경쟁사 대비 AI 브랜드 인지도가 낮음. Oracle AI 전략이 OCI GenAI 서비스, Database AI 등으로 분산
- **Oracle Cloud 종속성**: 사전 구축 Skills이 Oracle Cloud 제품군에 최적화되어, 비 Oracle 환경에서의 활용은 커스텀 개발이 필요

### 주요 경쟁사 비교
| 항목 | Oracle Digital Assistant | ServiceNow Now Assist | SAP Joule | Workday Assistant |
|------|------------------------|----------------------|-----------|------------------|
| 핵심 도메인 | ERP, HCM, SCM, CX | ITSM, CSM, HRSD | ERP, HCM, SCM, Procurement | HR, Finance |
| 아키텍처 | Skills 기반 모듈형 + Multi-Agent | Skills -> Agents -> Orchestrator | Scenario/Knowledge Catalog | ASOR (에이전트를 직원처럼 관리) |
| 대화 설계 도구 | Visual Flow Designer (캔버스) | AI Agent Studio (자연어) | Joule Studio | Workday Build + Flowise |
| LLM 전략 | LLM Block (Oracle GenAI, Cohere, Meta 등) | 자체 모델 + 외부 LLM | SAP 자체 + 다중 파운데이션 모델 | 서드파티 LLM 의존 |
| 사전 구축 자산 | 35+ Oracle Cloud Skills | 도메인별 OOB Skills | 80% 트랜잭션 커버리지 | HR 6종 + Finance 5종 |
| 프로토콜 | REST/SOAP, Oracle Integration Cloud | REST API, 전용 커넥터 | Microsoft 365 Copilot 양방향 | MCP + A2A (네이티브) |
| 다국어 NLU | Zero-shot 8개 언어 네이티브 | Dynamic Translation | SAP Translation Hub | 다국어 지원 제한적 |
| 멀티채널 | Web, Mobile, Teams, Slack, WhatsApp, 음성 | Web, Mobile, Teams, Slack, 음성 | SAP 임베딩 | Web, Mobile, Slack |
| 가격 모델 | 세션 기반 과금 | 시트 기반 + Assist 토큰 | SAP 라이선스 번들 | Flex Credits |

## 관련 리서치

- [[엔터프라이즈 AI 서비스 비교 분석]] -- 크로스 제품 UI/UX 비교 테이블에서 Oracle Digital Assistant 관련 분석 참조
- [[리서치 목표 및 벤치마크 대상]] -- 엔터프라이즈 AI 에이전트 벤치마크 대상 목록

## 참고 자료

- [Oracle Digital Assistant 공식 사이트](https://www.oracle.com/chatbots/)
- [Oracle Digital Assistant 공식 문서](https://docs.oracle.com/en-us/iaas/digital-assistant/doc/overview-digital-assistants-and-skills.html)
- [Visual Flow Designer 가이드](https://docs.oracle.com/en-us/iaas/digital-assistant/doc/get-started-visual-flow-designer.html)
- [LLM Integration 문서](https://docs.oracle.com/en/cloud/paas/digital-assistant/use-chatbot/llm-blocks-skills.html)
- [Multi-Agent 아키텍처 가이드](https://docs.oracle.com/en/solutions/build-multi-agent-with-oda/index.html)
- [Oracle Digital Assistant HCM Skill 튜토리얼](https://docs.oracle.com/en/cloud/paas/digital-assistant/tutorial-hcm/)
- [Oracle Cloud Fusion 글로벌 가격표 (2026-01)](https://www.oracle.com/a/ocom/docs/corporate/pricing/oracle-fusion-cloud-global-price-list.pdf)
- [Oracle Cloud 가격표](https://www.oracle.com/cloud/price-list/)
- [Oracle Blog: OCI GenAI Agents](https://blogs.oracle.com/cloud-infrastructure/post/behind-the-scenes-with-generative-ai-agents)
- [Oracle Blog: Empower Your Business Conversations with ODA](https://blogs.oracle.com/developers/empower-your-business-conversations-discover-the-oracle-digital-assistant-advantage-and-capabilities)
- [Oracle Digital Assistant for Oracle Fusion (GenAI 통합)](https://bitmapbytes.com/your-new-generative-digital-assistant-designed-for-oracle-fusion/)
- [Oracle Digital Assistant - Skill Development Deep Dive (Rittman Mead)](https://www.rittmanmead.com/blog/2023/11/oracle-digital-assistant-deep-dive-into-skill-development-part-1/)
