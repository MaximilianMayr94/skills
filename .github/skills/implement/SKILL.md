---
name: implement
description: implements tickets from copilot/tickets following architecture, refinement and quality rules.
mode: non-interactive
input: copilot/tickets/####.md, copilot/context.md, copilot/software_requirements.md, copilot/architecture.md, copilot/refinement/*.md
output: code, tests, updated ticket status, copilot/tickets/kanban.md (optional)
allowed-tools: shell
---

# Phase 1 - Load
- load `copilot/context.md`, `copilot/software_requirements.md`, `copilot/architecture.md` and necessary `copilot/refinement/*.md`.
- Implement the given ticket. If no ticket was given, look for the lowest not-done ticket.

# Phase 2 - Implement (per ticket)
- Follow the tickets instructions 
- Follow the quality guidelines of `context.md`
- Reuse code, keep it small and simple (context.md rules)

# Phase 3 - Verify acceptance criteria
- Execute each acceptance criterion and verify it.
- Fix failures before finishing. If unfixable: set ticket `Failed` + note reason.

# Phase 4 - Update board
- Run `scripts/kanban.py`
