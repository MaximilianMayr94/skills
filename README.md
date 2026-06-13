# Skills from a Software Engineering Manager

Hi, I am Maximilian. I work on LLM management, process, quality and automation. This repository contains public meta files for Copilot-style agents. They can be copied into new projects or legacy-code projects.

[![YouTube Channel](https://img.shields.io/badge/YouTube-SoftMax--v5t-red?logo=youtube)](https://www.youtube.com/@SoftMax-v5t)

Use Mermaid-capable Markdown rendering. Do not replace diagrams with ASCII art.

## VAgile process

```mermaid
flowchart TB
    subgraph VM_TOP["V-Model · whole project"]
        direction TB
        D["1. Definition<br/>(init, brainstorm, criticize)"]
        A["2. Architecture<br/>(architect)"]
    end

    subgraph AGILE["Agile · modular / per increment"]
        direction TB
        R["3. Refinement<br/>(refine, ticket_prep)"]
        I["4. Implementation<br/>(implement)"]
        V["5. Review<br/>(review)"]
    end

    subgraph VM_BOT["V-Model · whole project"]
        direction TB
        VER["6. Verification<br/>(verify)"]
    end

    D --> A --> R --> I --> V --> VER
    V -. "rework module" .-> R
    V -. "feedback" .-> A
    VER -. "fails requirements" .-> A
    VER -. "fails requirements" .-> D
    R -. "gaps / contradictions" .-> A
    V -. "next module / iterate" .-> R

    classDef vmodel fill:#cde4ff,stroke:#2b6cb0,color:#000;
    classDef agile fill:#d8f5d0,stroke:#38a169,color:#000;
    class D,A,VER vmodel;
    class R,I,V agile;
```

## Skill map

| Skill         | Mode            | Purpose                                                  | Main output                                              |
|---------------|-----------------|----------------------------------------------------------|----------------------------------------------------------|
| `init`        | interactive     | Scan/interview and create project source-of-truth docs.  | `copilot/context.md`, `copilot/software_requirements.md` |
| `brainstorm`  | interactive     | Explore, rate and validate ideas with the user.          | updated `context.md` / `software_requirements.md`        |
| `criticize`   | interactive     | Find gaps, contradictions, risks and overengineering.    | updated `context.md` / `software_requirements.md`        |
| `architect`   | interactive     | Group functionality into components and interfaces.      | `copilot/architecture.md`                                |
| `analyse`     | interactive     | Reverse-engineer existing legacy code. Refactoring.      | `copilot/analysis.md`                                    |
| `redesign`    | interactive     | Convert legacy findings into target architecture.        | `copilot/architecture.md`                                |
| `refine`      | interactive     | Detail components into modules, units, data and tests.   | `copilot/refinement/component_*.md`                      |
| `ticket_prep` | interactive     | Split refined work into vertical implementation tickets. | `copilot/tickets/####.md`, `kanban.md`                   |
| `implement`   | non-interactive | Implement tickets and verify acceptance criteria.        | code, tests, ticket status, `kanban.md`                  |
| `review`      | non-interactive | Review code/changes against docs and quality rules.      | `copilot/review/review_*.md`                             |
| `verify`      | non-interactive | Verify requirements/components against evidence.         | `copilot/verify.md`                                      |

## Target project artifacts

| File                                | Purpose                                                  |
|-------------------------------------|----------------------------------------------------------|
| `copilot/context.md`                | project description, tech stack, quality rules, glossary |
| `copilot/software_requirements.md`  | requirements + behavior source of truth                  |
| `copilot/architecture.md`           | components, functionality, interfaces, diagrams          |
| `copilot/analysis.md`               | legacy architecture + risks                              |
| `copilot/refinement/component_*.md` | modules, units, data, tests                              |
| `copilot/tickets/####.md`           | implementation tickets                                   |
| `copilot/tickets/kanban.md`         | generated board                                          |
| `copilot/review/review_*.md`        | ranked findings                                          |
| `copilot/verify.md`                 | evidence, verdict, open tests                            |  
| `scripts/kanban.py`                 | generates the ticket board from tickets                  |

### Example kanban output format:

```mermaid
---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
  Debt
    a[Old Architecture]@{ ticket: d0001, assigned: 'core', priority: 'High' }
  Todo
    a[Implement Buildsystem]@{ ticket: 0001, assigned: 'buildsystem', priority: 'High' }
  InProgress
    a[Creating Documents]@{ ticket: 0003, assigned: 'core', priority: 'Low' }
  Done
    a[Remove Old files]@{ ticket: 0004, assigned: 'none', priority: 'Very Low' }
  Failed
    a[Remove src]@{ ticket: 0005, assigned: 'core', priority: 'Very High' }
```

## Changes

- 13.06.2026 - Updated README to match current `copilot-instructions.md` and all skill metadata.
- 09.06.2026 - Split `context.md` into `context.md` + `software_requirements.md`; removed example files; removed update and quality skills; finalized SDLC.
