---
name: init
description: creates copilot/context.md and copilot/software_requirements.md, then asks questions until both are complete enough.
mode: interactive
input: existing project docs/code, context.default.md, software_requirements.default.md, software_requirements.example.md
output: copilot/context.md, copilot/software_requirements.md
allowed-tools: shell
---

# Phase 1 - Scan
Scan the whole project for existing documentation, architecture, code quality, test quality, bugs, gaps, problems and contradicting information. Use this as input for the interview and the generated documents. Do not assume that the existing information is correct. If the project is empty progress to phase 2 with the ``context.default.md` and `software_requirements.default.md` as input for the interview and generated documents.

# Phase 2 - Discuss
Ask the user about:
- project purpose, process, tech stack, quality and test expectations,
- product scope, actors, user flows, detailed functionality, acceptance criteria and data contracts,
- bugs, gaps, problems and contradictions in existing material.

Always ask for clarification if you are not sure about something. Do not make assumptions. After a few questions - max 5. - ask the user if he wants to progress to phase 3 or in case you do not have more questions progress to phase 3.

# Phase 3 - Create documents
- Create `copilot/context.md` in the target project using `context.default.md` (this folder) as template.
- Create `copilot/software_requirements.md` in the target project using `software_requirements.default.md` (this folder) as template.
- Fill every section from interview answers and project scan.
- Achieve a high-quality complete overview so architecture and implementation can be done without further questions. The better these documents are, the better architecture and implementation will be. Do not rush this step.
- Reference content instead of copying it.
