---
name: review
description: reviews the software and writes findings into copilot/review.md.
mode: non-interactive
input: copilot/context.md, copilot/software_requirements.md, copilot/architecture.md, copilot/refinement/*.md, source code
output: copilot/review/review_*.md
allowed-tools: shell
---

# Phase 1 - Load
- Load ``copilot/context.md``, ``copilot/software_requirements.md``, ``copilot/architecture.md``
- Load necessary files from tickets and refinement - if context is unclear ask the user what to review
- Scan source, tests, quality config.

# Phase 2 - Review
- Focus on the Code and the Changes
- Check if the functions are implemented as defined compared to the project or given scope.
- Check for: correctness, consistency, gaps, duplication, missing tests, doc/code mismatch. Per `context.md`.

# Phase 3 - Write review.md
- Write `copilot/review/review_*.md` use `review.default.md`.
- Rank findings by severity. Each finding: location, problem, suggestion.
- Mark items that should become dept tickets (not needed to fix to progress to ``6. Verification``).
