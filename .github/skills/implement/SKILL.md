---
name: implement
description: implements tickets from copilot/tickets following architecture, refinement and quality rules.
mode: non-interactive
input: copilot/tickets/####.md, copilot/context.md, copilot/architecture.md, copilot/refinement.md
output: code, tests, updated ticket status, copilot/tickets/kanban.md (optional)
allowed-tools: shell
---

# Goal
- SDLC phase 4 (Implementation, Agile). Non-interactive: do not ask, follow the documents.
- Implement open tickets, code + tests, until quality gates pass.

```mermaid
flowchart LR
  refine --> implement --> review --> refine
```

# Phase 1 - Load
- Always load `copilot/context.md` from the target project first, then `copilot/architecture.md` and `copilot/refinement.md`.
- Implement the given ticket. If no ticket was given, look for the lowest not-done ticket.

# Phase 2 - Implement (per ticket)
```mermaid
flowchart LR
  T[Ticket Todo] --> S[Set InProgress]
  S --> TDD[Write tests]
  TDD --> Impl[Implement]
  Impl --> Q{Quality gates pass?}
  Q -->|no| Impl
  Q -->|yes| D[Set Done]
  Q -->|blocked| F[Set Failed + note]
```
- Follow TDD: write tests from the ticket first.
- Reuse code, keep it small and simple (context.md rules).

# Phase 3 - Verify gates
- per `context.md` III/V
- Fix failures before finishing. If unfixable: set ticket `Failed` + note reason.

# Phase 4 - Update board
- Run `scripts/kanban.py` only if present in the target project.
