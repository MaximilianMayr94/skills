---
name: analyse
description: reverse-engineers architecture.md and review.md from existing legacy code.
mode: interactive
input: existing source code, copilot/context.md, copilot/architecture.md, copilot/review.md
output: copilot/analysis.md
allowed-tools: shell
---

# Goal
- Recover the real architecture from the code that was requested by the user and capture its properties.

# Phase 1 - Load
- Load `copilot/context.md` from the target project and `copilot/architecture.md` if present.
- Scan the requested part of the codebase: entry points, modules, dependencies.
- Reconstruct architecture
- Record smells, risks, dead code, coupling, missing tests.

# Phase 2 - Discuss
- Discuss with the user what you found, ask questions about the code, the architecture and the context. Clarify your understanding of the code, architecture, gaps, problems, code quality and so on.
- After a few questions - max 5. - ask the user if he wants to progress to phase 3 or in case you do not have more questions progress to phase 3.

# Phase 3 - Write analysis.md
- Write `copilot/analysis.md` using `analysis.default.md` (this folder) as template.
- See `analysis.example.md` for a filled-out example.
- Structure:
  - Architecture: reconstructed components, functionality and interfaces. Use diagrams/flowcharts.
  - Code Quality: smells, risks, dead code, coupling, missing tests. Bullet points + concrete examples.
  - Identified Gaps and Problems: gaps and contradictions in code vs. context/architecture. Bullet points + examples.

