---
name: architect
description: defines the software architecture from copilot/context.md into copilot/architecture.md.
mode: interactive
input: copilot/context.md
output: copilot/architecture.md
allowed-tools: shell
---

# Goal
- SDLC phase 2 (Architecture, V-Model). Interactive.
- Translate functionality from `context.md` into a component-based architecture.
- Greenfield: from `context.md`. Legacy: use `analyse` + `redesign` instead.

# Phase 1 - Load
- Always load `copilot/context.md` from the target project first (targets, functionality, tech stack, quality).

# Phase 2 - Group functionality
- Group functions into components (see `context.md` glossary). If a component is too large, create sub-components.
- Define interfaces between them (in case of protocols or header classes).

```mermaid
flowchart TB
  ctx[context.md functionality] --> comp[Components]
  comp --> mod[Modules]
  mod --> unit[Units]
```

# Phase 3 - Discuss with user
- Ask the user open questions to widen the solution space. Discuss with the user question by question refine ideas and generate new ones. Do not ask all questions at once, but one by one, discuss each question and its answer before moving to the next one. Every few questions ask the user if he wants to progress to phase 4 or if he wants to continue refining the architecture with more questions.

# Phase 4 - Write architecture.md
- Use `architecture.default.md` (this folder) as template; see `architecture.example.md`.
- Keep interfaces explicit.

