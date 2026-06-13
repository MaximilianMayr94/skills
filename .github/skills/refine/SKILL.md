---
name: refine
description: prepares implementation from architecture.md and review.md into refinement/component_*.md.
mode: interactive
input: copilot/context.md, software_requirements.md, copilot/architecture.md, copilot/review.md (optional)
output: copilot/refinement/component_*.md
allowed-tools: shell
---

# Phase 1 - Load
- Load `copilot/context.md`, `software_requirements.md`, `copilot/architecture.md` and `copilot/review.md` (if it exists).
- If the scope is not clear ask the user on what (sub)-component to focus on. Can be more then one.

# Phase 2 - refine
- Refine the component(s) into modules/units and data structures. 
- Define the test approach (TDD) and list test cases.
- Reduce duplicate code/functions as much as possible.
- Implement/define the component/functions in a simple way.

# Phase 3 - Discuss with user
- Ask the user open questions. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one. Clarify Slices. Every few questions (max. 5) ask the user if he wants to progress to phase 4 or if he wants to continue refining with more questions.

# Phase 4 - Creation
- Create `copilot/refinement/component_*.md` use the template defined in `component_.default.md`.
