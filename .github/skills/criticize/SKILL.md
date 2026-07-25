---
name: criticize
description: "criticizes the project from high level down to files and updates copilot/context.md or copilot/software_requirements.md."
mode: interactive
input: copilot/context.md, copilot/software_requirements.md, copilot/architecture.md (optional), requested code/docs
output: copilot/context.md, copilot/software_requirements.md
allowed-tools: shell
---

# Phase 1 - Load
- Load `copilot/context.md`, `copilot/software_requirements.md`, `copilot/architecture.md` if present, and the parts of the codebase the user requested.

# Phase 2 - Criticize (top-down)
Analyze the loaded material and look for:
- Problems, risks, gaps, contradictions.
- Overengineering / duplication / dead parts.
- Missing tests or quality gates.

# Phase 3 - Discuss
- Ask the user open questions. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one.
- Every few questions (max. 5) ask the user if he wants to progress to phase 4 or if he wants to continue refining with more questions.
- For each question give the user a custom answer field so he can enter something else

# Phase 4 - Apply
- Ask the user to either
  - Update `copilot/context.md` / `copilot/software_requirements.md` in the target project with validated state, open issues and ideas.
  - Fix the findings directly
- Do not update unvalidated/undiscussed findings.




