---
name: update
description: updates copilot/context.md based on user ideas or project changes.
mode: interactive
input: copilot/context.md, user changes, project changes
output: copilot/context.md
allowed-tools: shell
---

# Goal
- Keep `context.md` in sync with the real project state.

# Phase 1 - Load
- Load `copilot/context.md` from the target project (see init skill for section layout).

# Phase 2 - Interview
- Ask the user relentlessly about changes and new ideas: new/removed features, tech, quality, bugs, gaps, contradictions.
- After a few questions - max 5. - ask the user if he wants to progress to phase 3 or in case you do not have more questions progress to phase 3.

# Phase 3 - Apply
- Update affected sections only (I-IX, see init skill).
- Remove outdated info, mark open questions.

```mermaid
flowchart LR
  P[Project state] --> D{Diff vs context.md}
  U[User input] --> D
  D --> C[context.md updated]
```

