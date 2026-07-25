---
name: refinement
description: prepares implementation from architecture.md and review.md into refinement/component_*.md.
mode: interactive
input: copilot/context.md, software_requirements.md, copilot/architecture.md, copilot/review.md (optional)
output: copilot/refinement/component_*.md, copilot/refinement/interface_*.md
allowed-tools: shell
---

# Phase 1 - Load
- Load `copilot/context.md`, `software_requirements.md`, `copilot/architecture.md` and `copilot/review.md` (if it exists).
- If the scope is not clear ask the user on what (sub)-component or interface to focus on. Can be more then one.

# Phase 2 - refine
- Refine the component(s) into modules/units and data structures. Or if it is an interface into its groups/messages and arguments/fields.
- Reduce duplicate code/functions as much as possible.
- Define the component/functions in a simple way.
- Ignore how it will be implemented (Slicing)

# Phase 3 - Discuss with user
- Ask the user open questions. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one. 
- Every few questions (max. 5) ask the user if he wants to progress to phase 4 or if he wants to continue refining with more questions.
- For each question give the user a custom answer field so he can enter something else

# Phase 4 - Creation
- if a component: Create `copilot/refinement/component_*.md` use the template defined in `component_.default.md`.
- if a interface: Create `copilot/refinement/interface_*.md` use the template defined in `interface_.default.md`.
