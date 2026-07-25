---
name: brainstorm
description: brainstorms ideas with the user and feeds validated results back into copilot/context.md or copilot/software_requirements.md.
mode: interactive
input: copilot/context.md, copilot/software_requirements.md
output: copilot/context.md, copilot/software_requirements.md
allowed-tools: shell
---

# Phase 1 - Load
- Load `copilot/context.md` and `copilot/software_requirements.md` from the target project for targets, state, constraints and product behavior.

# Phase 2 - Diverge
- Create multiple new ideas like a storm (features, approaches, simplifications) that are going to improve the project.
- Challenge assumptions, offer alternatives.

# Phase 3 - Discuss with the user
- Ask the user open questions. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one.
- Every few questions (max. 5) ask the user if he wants to progress to phase 4 or if he wants to continue refining with more questions.
- For each question give the user a custom answer field so he can enter something else

# Phase 4 - Apply
- Ask the user to either
    - Update `copilot/context.md` / `copilot/software_requirements.md` in the target project with validated state, open issues and ideas.
    - Fix the findings directly
- Do not update unvalidated/undiscussed findings.





























