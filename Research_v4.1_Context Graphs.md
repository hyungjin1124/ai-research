## Ontology와 Knowledge Graph
---
#### Ontology
![[Pasted image 20260129171011.png]]

#### Knowledge Graph
![[Pasted image 20260129171036.png]]

```
ontology + data = knowledge graph
```

## Context Graph의 정의 및 개념
---
전통적 Triple 기반 Knowledge Graph의 한계를 극복하고, 지식의 맥락 정보(시간, 공간, 출처 등)를 통합한 확장된 지식 표현 구조

```
Context Graph (CG) = Knowledge Graph (KG) + Contextual Information

* 출처: Xu et al. (2024)의 연구
``` 

Contextual Information:
- **Temporal Context**: 시간 유효성 (time validity)
- **Spatial Context**: 지리적 위치 (geographic location)
- **Provenance Context**: 출처 정보 (source provenance)
- **Confidence Context**: 신뢰도 점수 (confidence scores)

#### Triple 구조와 확장

- 기본 Triple
	```
	<Subject, Predicate, Object>
	```
- Context Graph Triple
	```
	<Subject, Predicate, Object, Context>
	
	* Context  = {temporal, spatial, provenance, confidence, reasoning_trace}
	```
- Knowledge Graph vs Context Graph
	- Konwledge Graph
		```
		(Alice, works_at, TechCorp)
		```
	- Context Graph
		```
(Alice, works_at, TechCorp) {
		  since: "2020-01-15",
		  source: "HR_database",
		  confidence: 0.98,
		  verified_by: "annual_review_2024",
		  decision_trace: "promoted_from_VP_role"
}
		```

## Context Graph Demo
---
https://context-graph-demo.vercel.app/

### 워크플로우: 신용 한도 증액

사용자가 다음과 같이 질문했을 때 일어나는 일입니다:

> "Jessica Norris의 신용 한도 증액을 승인해야 할까요? 그녀는 $25,000 한도 증액을 요청하고 있습니다."

AI 에이전트는 즉시 컨텍스트 그래프 쿼리를 시작합니다:

**1단계: 고객 검색 (search_customer)**  
에이전트는 Jessica Norris를 찾고 그녀의 전체 프로필로 그래프 시각화를 채웁니다:

- 위험 점수: 0.419 (중상위)
- 계좌: 2개 — 트레이딩 계좌($258,695, 중간위험등급) 및 마진계좌($17,756, 높은위험등급)
- 고용주: Anderson Group (위험 등급 "C", 예멘 소재)
- 최근 거래: 보류 중인 여러 해외 송금을 포함한 20개 이상의 거래

**2단계: 결정 이력 (get_customer_decisions)**  
컨텍스트 그래프는 중요한 과거 결정들을 드러냅니다:

- **2025년 4월 사기 거절:** 거래 차단됨. 알려진 사기 유형 FT-8291과 패턴 일치. 
	- 속도 이상: 29분 내 14건의 거래. 
	- 지리적 이상: IP 위치와 계좌 주소 불일치. 
	- 위험 요소: new_device, round_amount, high_amount, after_hours. 
	- 신뢰도 점수: 78.8%
    
- **2025년 2월 규정 준수 거절:** after_hours 및 round_amount를 포함한 위험 요소로 표준 검토 완료.
    
- **2024년 4월 규정 준수 거절:** round_amount 플래그로 인한 또 다른 거절.
    

**3단계: 선례 검색 (find_precedents)**  
에이전트는 하이브리드 벡터 검색 — 의미적 유사성(텍스트 임베딩)과 구조적 유사성(FastRP 그래프 임베딩)의 결합 — 을 사용하여 유사한 신용 한도 결정을 검색합니다.

**4단계: 정책 조회 (get_policy)**  
"고액 거래 검토" 및 "KYC 갱신 정책"과 같은 적용 가능한 정책을 검색합니다.

**에이전트의 추천:**  
컨텍스트 그래프 분석을 바탕으로 에이전트는 다음을 반환합니다:
```
⚠️ 추천: 거절 또는 고위급 검토를 위한 에스컬레이션
핵심 위험 요소:
	- 속도 체크 실패가 포함된 과거 사기 플래그 (2025년 4월)
	- 기록상의 다수 규정 준수 거절
	- 고위험 등급 마진 계좌
	- 국가 위험도가 높은 고용주
  
문서화된 사기 사건과 규정 준수 패턴을 고려할 때, 거절하거나 추가 실사 요구사항과 함께 에스컬레이션할 것을 권장합니다.
```


그래프 시각화는 31개의 노드와 30개의 관계를 보여줍니다 — Jessica의 계좌, 거래, 과거 결정, 그 결정을 내린 직원, 적용된 정책을 포함한 그녀의 전체 맥락입니다.

에이전트는 단순히 신용 점수만 확인한 것이 아닙니다. 전체 결정 이력을 추적하고, 과거 사건들 간의 인과 관계를 이해했으며, 조직 내 지식에 기반한 추천을 내렸습니다.

## 코나아이 시나리오 비교
---

사용자 질문: "지난 분기 A고객 매출이 왜 30% 하락했나요?"
#### Knowledge Graph

![[Pasted image 20260127130228.png]]
![[Pasted image 20260127130257.png]]


쿼리 결과
``` cypher
MATCH (c:Customer {name: "고객A"})-[r:has_revenue]->(rev) 
WHERE rev.quarter 
IN ["Q3", "Q4"] RETURN c, rev
```

AI 응답
```
고객A의 Q3 매출은 5억원, Q4 매출은 3.5억원으로 30% 하락했습니다.
담당자는 김영업이며, 제조업 분야의 연간계약 고객입니다.
```

한계점
- ❌ "왜" 하락했는지 설명 불가 
- ❌ 관련된 의사결정 이력 없음 
- ❌ 예외 상황이나 맥락 정보 부재

#### Context Graph

<엔티티 레이어>
![[Pasted image 20260128173525.png]]

<이벤트 레이어>
![[Pasted image 20260128145843.png]]

<인과관계 그래프>
![[Pasted image 20260128174713.png]]

<Agent 응답>
![[Pasted image 20260128174242.png]]

<의사결정 레이어> - 전자결재 연동 필요
![[Pasted image 20260129150607.png]]

#### Context Graph 핵심 기능 달성 여부

```
Context Graph의 핵심 = Decision Traces (의사결정 이력 + 근거)
                                ↓
                    결재이력 테이블이 없으면 구성 불가
                                ↓
              "왜(Why)" 설명 불가 → Context Graph 핵심 가치 미달성
```

#### AI 응답 비교

| 시나리오                               | AI 응답 예시                                     |
| ---------------------------------- | -------------------------------------------- |
| **Knowledge Graph**                | "Q3 5억원, Q4 3.5억원으로 30% 하락했습니다"              |
| **Context Graph (ERP)**            | "납기지연 후 부품A 중심 수주 급감으로 30% 하락"               |
| **Context Graph <br>(ERP + 전자결재)** | "납기지연 → 클레임 → 단가인하 거절(박상무, 원가율 미충족)로 30% 하락" |

