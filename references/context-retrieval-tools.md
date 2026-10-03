# Context, retrieval, tools, and reuse

Build active context from the latest control state, current contract/node, relevant accepted artifacts, targeted evidence, and ephemeral tool output.

## Preserve

- goal and hard constraints;
- exact values, negations, and exceptions;
- accepted decisions;
- blockers and unresolved material uncertainty;
- gate definitions/status;
- provenance and source dates;
- dependency versions;
- last-known-good checkpoints.

## Compress or archive

Superseded alternatives, redundant logs, duplicate evidence, stale exploratory dialogue, and raw tool output that no longer affects the next decision. Keep recoverable source material outside active context when audit value remains.

## Retrieval

Search when missing or changing information could materially affect the result. Define the evidence question first. Prefer authoritative/primary sources, track date/version, and inspect contradictions.

Stop retrieval when required claims are supported and no concrete material gap remains. Re-open retrieval if execution exposes a new information deficit.

## Tools

Use deterministic tools for properties they can actually prove: calculators for arithmetic, parsers for structure, execution/tests for behavior, screenshots/rendering for visual artifacts, authoritative sources for current facts, external state inspection for side effects.

A successful tool response is not always proof of the final external effect.

## Reuse and cache

Reuse only when semantic fit, dependency versions, freshness, permission scope, and quality status still match. Invalidate only affected cached artifacts when state changes.

Never treat another user's secrets or private results as shared cache.
