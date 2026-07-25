---
name: redesign
description: redesigns copilot/architecture.md for legacy code into a target architecture.
mode: interactive
input: copilot/analysis.md, copilot/context.md, copilot/architecture.md (current, optional)
output: copilot/architecture.md (target), debt tickets via refine
allowed-tools: shell
---

# Goal
- Evolve the legacy architecture toward a clean target design.

# Phase 1 - Load
- Load `copilot/context.md`, `copilot/analysis.md` (from the `analyse` skill), and current `copilot/architecture.md` if present from the target project.

# Phase 2 - Target design
- Propose target components/modules/interfaces.
- Show migration path current -> target.
- Discuss with the user what you found, ask questions about the code, the architecture and the context. Clarify your understanding of the code, architecture, gaps, problems, code quality and so on.
- After a few questions - max 5. - ask the user if he wants to progress to phase 3 or in case you do not have more questions progress to phase 3.

# Phase 3 - Select
- Let the user pick what to keep. Simple by questions for each idea: Do not ask the user to pick between ideas, but ask for each idea if he wants to keep it or not. Do not ask the user to rate ideas by value vs effort, but do it yourself based on the discussion with the user and your understanding of the project. Add it to the question like this  "Do you want to keep this idea? yes/no/optional user input".
- Then progress to phase 4 with the selected ideas.

# Phase 4 - Apply
- Update `copilot/architecture.md` with the findings.

