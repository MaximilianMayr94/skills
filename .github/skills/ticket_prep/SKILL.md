---
name: ticket_prep
description: creates ticket out of context, architecture, review, given prompt...
mode: interactive
input: copilot/context.md, software_requirements.md, copilot/architecture.md, copilot/refinement/*.md, copilot/review.md (optional)
output: copilot/tickets/####.md, copilot/tickets/kanban.md
allowed-tools: shell
---

# Phase 1 - Load
- Load `copilot/context.md`, `software_requirements.md`, `copilot/architecture.md`, required components from ``copilot/refinement/`` and `copilot/review.md` (if it exists).
- If the scope is not clear ask the user on what slice/review/bug to focus on. Can be more then one.

# Phase 2 - vertical slicing
- Split the implementation (the tickets) in vertical slicing

# Phase 3 - Discuss with user
- Propose to the user the vertical slices and ask for feedback or different ideas. In case of very small implementation there is no need for slicing (<=5 tickets)
- Ask the user open questions. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one. Clarify Slices. Every few questions (max. 5) ask the user if he wants to progress to phase 4 or if he wants to continue refining with more questions.

# Phase 4 - Creation
- Create `copilot/tickets/####.md` use the template defined in `ticket.default.md`
- Ticket numbering: linear in order of execution
- Execute the `scripts/kanban.py` script to create the `copilot/tickets/kanban.md` file
