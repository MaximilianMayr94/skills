---
name: verify
description: verifies the project against context.md and architecture.md, writes copilot/verify.md.
mode: non-interactive
input: copilot/context.md, copilot/architecture.md, copilot/refinement.md, source code
output: copilot/verify.md
allowed-tools: shell
---

# Phase 1 - Load
- load `copilot/context.md`, `software_requirements.md`, `copilot/architecture.md` and all refinement documents.

# Phase 2 - Verify
- Map each requirement/component to evidence (test, code, gate result).
- Run quality gates (build, lint, tests) and record results.
- Do not assume ambiguous or untestable requirements. Record them as open verification issues. And write them as tests for the user to do.

# Phase 3 - Write verify.md
- Use `verify.default.md` (this folder);
- Give a pass/fail per requirement + overall verdict.
- Write a testlist for open cases for the user.
- List deviations and suggested architecture/refinement changes.

