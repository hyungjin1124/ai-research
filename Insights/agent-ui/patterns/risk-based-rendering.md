---
type: insight-synthesis
topic_id: risk-based-rendering
topic_name: "위험도 기반 동적 UI 렌더링"
category: agent-ui
document_level: specific
parent_broad:
  - hitl-approval-patterns
catalog_components:
  - approval_rejection
  - confirmation_dialog
tags:
  - insight
  - agent-ui
  - pattern
  - risk
  - dynamic-rendering
  - trust
status: draft
confidence: high
last_updated: "2026-02-15"
source_products: []
source_files: []
auto_update:
  enabled: true
  keywords: []
  feeds: []
  review_trigger:
    mode: "auto"
    threshold: 3
    priority_override: true
relevant_roles:
  - frontend_agent
---

# 위험도 기반 동적 UI 렌더링

## TL;DR

- Claude Code의 3-tier permission (Allow Once / Session / Always)은 user trust level에 따른 UI 변형의 모범 사례 [^1]
- Claude Cowork는 operation type (read/write/delete)에 따라 차등 UI 제공 (read=auto, write=ask, delete=warning) [^2]
- Salesforce Atlas는 confidence score < threshold 자동 escalate → supervisor flow로 dynamic 경로 결정 [^3]
- Microsoft Copilot의 sidecar actions는 data-modifying operation에만 confirmation 요구 [^4]
- Risk classification engine이 static tiers를 dynamic confidence scoring으로 진화하는 추세 [^5]
- KonaI-Agent는 AdminView permission matrix + riskLevel props로 static risk tier 우선 구현, v2에서 confidence-scoring 고도화

## Overview

위험도 기반 동적 UI 렌더링은 Agent action의 risk level에 따라 사용자에게 제시하는 UI 형태를 동적으로 결정하는 패턴이다. 핵심 개념:

1. **Risk Classification**: Action type + resource scope + data sensitivity → risk score (0-100)
2. **Escalation Routing**: Risk score threshold에 따라 다른 interaction flow (auto-execute / toast / inline card / modal warning / supervisor escalate)
3. **Permission Tier Integration**: User의 historical approval pattern 학습 → "이 사용자는 이 action type을 항상 approve" → auto-skip ask

PPT scenario에서 "슬라이드 생성"은 low-risk (draft, revertible), "최종 outline 승인"은 medium-risk (commitment), "모든 이미지 자동 다운로드"는 high-risk (storage + bandwidth)에 분류된다.

## 경쟁사 구현 분석

| Product | Risk Tier 방식 | Classification Method | UI Rendering | Escalation |
|---------|---------------|---------------------|-----------|-|
| Claude Code | Static: Allow Once / Session / Always | User choice at ask time | Modal dialog (3-option) | Permission rule → canUseTool callback |
| Claude Cowork | Static: read / write / delete | Operation type | read=silent, write=ask, delete=warning | Tool type filtering |
| Salesforce Atlas | Dynamic: confidence % | Confidence score from LLM | High conf=silent, Med=ask, Low=escalate | Supervisor approval workflow |
| ServiceNow Now Assist | Proactive triggers | Risk-assessed rules | Notification + action buttons | Virtual agent escalate |
| Microsoft Copilot | Dynamic: operation impact | Data-modifying vs read-only | Sidecar action + optional confirmation | System-level authorization |

### Claude Code: Static Permission Tiers [^1]

Risk Classification (Simple):
- Tool call detected
- Check settings.json (allow rules)
- Check deny rules (block rules)
- Check ask rules (permission dialog)

UI per Risk:
- Allow rule matched → execute silently, maybe toast notification
- Ask rule matched → modal dialog, 3 options (Allow Once / Allow Session / Always)
- Deny rule matched → blocked, error message

**왜 이 방식인가**: Tier가 static하면 predictable. User가 "file delete는 항상 ask" 패턴을 학습하면, 매번 ask되는 게 expected.

참고: [Configure permissions - Claude Code Docs](https://code.claude.com/docs/en/permissions), [Understanding Claude Code Permissions and Security Settings](https://www.petefreitag.com/blog/claude-code-permissions/)

### Claude Cowork: Operation-Type Classification [^2]

Operation Classification:
- READ (fs.readFile, db.query): Risk = low → Auto-execute, silent log
- WRITE (fs.writeFile, db.update): Risk = medium → Ask user, single modal
- DELETE (fs.deleteFile, db.drop): Risk = high → Warning dialog, prominent deny button

**왜 이 방식인가**: Operation type은 deterministic (read/write/delete 중 하나). "이거 delete 작업이니까 ask" 원칙이 명확.

참고: [Configure permissions - Claude API Docs](https://platform.claude.com/docs/en/agent-sdk/permissions)

### Salesforce Atlas: Confidence-Based Escalation [^3]

Dynamic Risk Scoring:
- confidence > 95% → auto-execute
- 70% < confidence < 95% → ask
- confidence < 70% → escalate

Escalation Examples:
- Pricing change (sensitive) → Supervisor approval
- Refund (financial) → Finance team approval
- Account deletion (irreversible) → Legal check

**왜 이 방식인가**: 신뢰도가 작업마다 다르다. "customer name update"는 high confidence, "customer lifetime value prediction"은 low confidence. Confidence-based escalation은 "정말 sure할 때만 execute, 애매하면 ask, 확신 없으면 human 맡김."

참고: [How the Atlas Reasoning Engine Powers Agentforce](https://www.salesforce.com/agentforce/what-is-a-reasoning-engine/atlas/), [Inside Agentforce: Revealing the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)

### ServiceNow: Proactive Risk-Based Notifications [^4]

Genius Results + Risk Triggers:
- Sentiment-based: Negative sentiment detected → escalate to supervisor
- Confidence-based: Low confidence answer → flag with "uncertain" label
- Rule-based: Legal/sensitive request → route to compliance team

**왜 이 방식인가**: Reactive (user가 문제 겪을 때 react) 대신 proactive (위험 감지 시 미리 warn).

## 패턴 분류 및 트레이드오프

### Risk Classification Patterns

1. **Static Risk Tier** (Claude Code)
   - Classification: User's explicit choice (Allow Once / Session / Always)
   - Updating: Manual (via settings.json or re-ask)

2. **Operation-Type Based** (Claude Cowork)
   - Classification: read/write/delete category
   - Updating: New tool type added → automatic classification

3. **Confidence-Score Based** (Salesforce Atlas)
   - Classification: LLM outputs confidence % per action
   - Updating: Real-time per action generation

4. **Operation Impact Analysis** (Microsoft)
   - Classification: {read-only, write, delete} + {scope, data sensitivity}
   - Updating: Rules + real-time analysis

5. **Proactive Rule-Based** (ServiceNow)
   - Classification: Predefined rules (sentiment, keywords, patterns)
   - Updating: Rule engine, can be dynamic

### Trade-off Summary

| Dimension | Static Tier | Op-Type | Confidence | Impact-Based | Proactive Rules |
|-----------|------------|--------|-----------|------------|-----------------|
| Implementation Cost | 낮음 | 낮음 | 높음 | 중간 | 중간 |
| Adaptive (learns context) | 낮음 | 낮음 | 높음 | 중간 | 중간 |
| User Control | 높음 | 낮음 | 중간 | 중간 | 낮음 |
| Escalation Accuracy | 중간 | 중간 | 높음 | 좋음 | 중간 |

## KonaI-Agent 적용 전략

### 현재 코드베이스 상황

| 항목 | 현재 상태 | 문제점 |
|------|---------|-------|
| **AdminView** | Role-based permission matrix | 개별 action risk level 없음 |
| **useSlideOutlineHITL** | Approve/reject/modify 로직 | 모든 action이 같은 level |
| **dialog.tsx** | Radix dialog base | 시각적 risk indicator 없음 |
| **usePPTScenario** | Scenario with hooks | Scenario type별 risk 분류 안 됨 |
| **Brand color #FF3C42** | 사용 중 | 중성적 사용만 함 |

### 권장 설계: Static Op-Type + Confidence-Ready Architecture

**Phase 1: Action Risk Classification (Static)**

actionTypes.ts:
```
enum ActionType {
  GENERATE_OUTLINE = 'generate_outline',
  APPROVE_OUTLINE = 'approve_outline',
  MODIFY_OUTLINE = 'modify_outline',
  REGENERATE_SLIDES = 'regenerate_slides',
  READ_ARTIFACT = 'read_artifact',
  WRITE_ARTIFACT = 'write_artifact',
  DELETE_ARTIFACT = 'delete_artifact',
}

enum RiskLevel {
  LOW = 'low',       // generate_outline, read_artifact
  MEDIUM = 'medium', // approve_outline, modify_outline
  HIGH = 'high',     // delete_artifact, regenerate with major changes
}
```

**Phase 2: Dynamic UI Rendering per Risk Level**

- LOW: Toast notification (auto-proceed option, cancel button)
- MEDIUM: Inline card (approve/reject/modify buttons, #FF3C42 border-left)
- HIGH: Modal dialog (warning, #FF3C42 CTA, require explicit confirm)

**Phase 3: AdminView Extension (Risk Rule Override)**

Permission Matrix v2:
- Columns: [User Role] [Action Type] [Default Risk] [Override?] [Permission]
- Override checkbox: 특정 role에 대해 permission override 가능

## Acceptance Criteria

### Functional Criteria

1. **Action Risk Classification**
   - ACTION_RISK_MAP으로 모든 action type 매핑
   - New action 추가 시 risk level assign 필수
   - Override mechanism: AdminView에서 role/user별 risk 조정 가능

2. **Risk-Based UI Rendering**
   - LOW: Toast (5초 auto-dismiss, cancel button)
   - MEDIUM: Inline card (border-left #FF3C42, approve/reject/modify)
   - HIGH: Modal (dark overlay, centered, #FF3C42 CTA)

3. **AdminView Permission Matrix Update**
   - Risk level column 추가 (read-only, default from ACTION_RISK_MAP)
   - Override checkbox: 특정 role에 대해 permission override 가능
   - Save & apply: runtime에 반영

4. **Audit Trail**
   - 모든 risk-based decision log (approve/reject/override)
   - Admin dashboard에서 "high-risk action history" 조회 가능

## Key Considerations

1. **Risk Scoring Calibration**: "Medium이 정말 적절한가" user research 필요. 너무 many mediums (frequent asks) → fatigue, 너무 many highs (over-alert) → false positive.

2. **Context-Aware Risk** (v2 consideration): 같은 action이라도 context에 따라 risk 달라짐. v2: user profile + action context → confidence score.

3. **Cross-Action Coordination**: "A action approve + B action reject"의 조합이 inconsistent하면?
   - MVP: 각 action 독립적 (no coordination)
   - v2: "previous action state" consider

4. **Permission Tier + Risk Level 우선순위**:
   - Option A: Risk로 override ("high-risk니까 always ask")
   - Option B: Permission tier 우선 ("user가 allow for session 선택했으니 proceed")
   - Decision: B + warning toast

5. **Confidence-Score Migration Path** (v2):
   - Phase 1 (current): Static risk tier
   - Phase 2 (v2): Confidence score from Claude alongside action
   - Phase 3 (v3): Confidence + user historical pattern

## Recent Updates

| 날짜 | 변경사항 | 영향 범위 |
|------|---------|---------|
| 2026-02-15 | Claude Code static permission tiers 분석 | Phase 1 foundation |
| 2026-02-15 | Claude Cowork op-type classification 검토 | ACTION_RISK_MAP 아키텍처 |
| 2026-02-15 | Salesforce confidence-based escalation 분석 | v2 migration path 문서화 |

## References

### External

- [Configure permissions - Claude Code Docs](https://code.claude.com/docs/en/permissions)
- [Understanding Claude Code Permissions and Security Settings](https://www.petefreitag.com/blog/claude-code-permissions/)
- [Configure permissions - Claude API Docs](https://platform.claude.com/docs/en/agent-sdk/permissions)
- [How the Atlas Reasoning Engine Powers Agentforce](https://www.salesforce.com/agentforce/what-is-a-reasoning-engine/atlas/)
- [Inside Agentforce: Revealing the Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/)

[^1]: Claude Code의 3-tier는 user가 "지금은 한 번만", "이 세션은 계속", "항상"을 명시적으로 선택 가능.
[^2]: Claude Cowork의 op-type은 deterministic 분류로, rule configuration의 복잡도 낮음.
[^3]: Salesforce의 confidence scoring은 실제 LLM uncertainty를 활용하여, context-adaptive escalation 가능.
[^4]: ServiceNow는 "side effect 있나"라는 단순한 기준으로 distraction 최소화.
[^5]: 산업 동향은 static → dynamic + proactive로 진화 중. KonaI-Agent는 MVP static, v2+ confidence-based로 계획.
