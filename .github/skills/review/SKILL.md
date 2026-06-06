---
name: review
description: reviews the software and writes findings into copilot/review.md.
allowed-tools: shell
---

input: copilot/context.md, copilot/architecture.md, copilot/refinement.md, source code
output: copilot/review.md

# Goal
- SDLC phase 5 (Review, Agile). Non-interactive.
- Find problems, bugs, gaps and contradictions; suggest architecture/refinement changes.

```mermaid
flowchart LR
  refine --> implement --> review --> refine
```

# Phase 1 - Load
- Always load `copilot/context.md` first, then `architecture.md`, `refinement.md`.
- Scan source, tests, quality config.

# Phase 2 - Review
```mermaid
flowchart TB
  R[Requirements] --> A[Architecture]
  A --> C[Code]
  C --> T[Tests]
  T --> Q[Quality gates]
```
Check per level: correctness, consistency, gaps, duplication, missing tests, doc/code mismatch. Per `context.md`.

# Phase 3 - Write review.md
- Use `review.default.md` (this folder); see `review.example.md`.
- Rank findings by severity. Each finding: location, problem, suggestion.
- Mark items that should become `dept_####` tickets (Not needed to fix to progress).
