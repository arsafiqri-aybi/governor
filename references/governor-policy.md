# Governor policy

Optimize for the least unnecessary total resource that still produces an accepted result. Do not collapse tokens, latency, tool calls, context, retries, money, quota, and human review into one invented score.

Complexity, risk, and uncertainty are different. A simple high-consequence calculation may need deterministic tools and strong verification; a difficult low-risk analysis may need deeper reasoning but no external action.

## Control loop

1. Read current state and required gates.
2. Diagnose the bottleneck.
3. Choose one resource intervention inside the allowed envelope.
4. Execute and observe.
5. Verify the property that was failing.
6. Continue, stop success, change strategy, or request re-plan.

Governor may adjust context, retrieval depth, valid reuse/cache, reasoning effort inside the allowed range, optional verification, retry timing, and pre-authorized model/tool alternatives.

Governor must preserve the user goal, hard constraints, mandatory acceptance criteria, permission boundaries, capability floors, required verifier channels, and dependency integrity.

## Retry and side effects

Retry only after a material condition changes. For a side-effecting operation with unknown outcome, inspect resulting state before trying again.

Routine technical re-planning already authorized by the user may proceed without repetitive confirmation. A genuinely new permission, cost boundary, or irreversible action must be surfaced according to host rules.

## Evidence discipline

UNKNOWN is not zero. NOT_RUN is not FAIL. Conflicting evidence is not averaged into truth. A routing rule remains a heuristic until supported by comparable tasks, holdout evidence, and preserved critical gates.

Do not claim savings, success probability, or optimality from a small smoke test.
