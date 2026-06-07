# Skills from a Software Engineering Manager

Hi, I am Maximilian. I am currently working on LLM management, processes, quality and automation. This repository contains my latest public meta files (skills). They are made for Copilot, but you can adapt them to other tools and models.

I created these skills so they can be copied into current projects, from new ideas to legacy code. They focus on a simple and effective process while keeping LLM automation in mind. I will keep updating this repository with new skills and improvements.

If you are interested into the details of these skills and my thought process behind it check out my Youtube channel:  [![YouTube Channel](https://img.shields.io/badge/YouTube-SoftMax--v5t-red?logo=youtube)](https://www.youtube.com/@SoftMax-v5t)

## Mermaid
Install a Mermaid plugin if diagrams are not supported natively. Do not let the LLM create ASCII diagrams.

## Overview - Meta-Files
Note: Most skills are interactive and might require user input while executing. `implement`, `review` and `verify` are non-interactive services.

```mermaid
flowchart TB
  
    %% First line emphasized: bold. Descriptions smaller and grey.
    CF["<b>.github/copilot-instructions.md</b><br/><span style='font-size:10px;color:#888'>basic LLM interaction guidelines</span>"]
    
    subgraph General[General]
      G1["<b>init</b><br/><span style='font-size:10px;color:#888'>Create context.md</span>"]
      G2["<b>update</b><br/><span style='font-size:10px;color:#888'>Update context.md</span>"]
      G3["<b>quality</b><br/><span style='font-size:10px;color:#888'>Add/Update Quality requirements to context.md</span>"]
      G4["<b>brainstorm</b><br/><span style='font-size:10px;color:#888'>Brainstorm Ideas<br/>-> update context.md</span>"]
      G5["<b>criticize</b><br/><span style='font-size:10px;color:#888'>Criticize from project to files <br/>-> update context.md</span>"]
    end

    subgraph Process[Process]
      P1["<b> </b><br/><span style='font-size:10px;color:#888'>Defines SW Architecture - Groups Functions<br/>context.md -> architecture.md</span>"]
      P2["<b>refine</b><br/><span style='font-size:10px;color:#888'>Prepare Implementation<br/>architecture.md & review.md -> tickets/*</span>"]
      P3["<b>implement</b><br/><span style='font-size:10px;color:#888'>Implement Tickets</span>"]
      P4["<b>review</b><br/><span style='font-size:10px;color:#888'>Review Software<br/>* -> review.md</span>"]
      P5["<b>verify</b><br/><span style='font-size:10px;color:#888'>Verify Project against architecture and context</span>"]
    end

    subgraph LegacyCode[Module: LegacyCode]
      L1["<b>analyse</b><br/><span style='font-size:10px;color:#888'>Creates/updates analysis.md from legacy code + review.md</span>"]
      L2["<b>redesign</b><br/><span style='font-size:10px;color:#888'>Redesigns architecture.md</span>"]
    end
```

## Overview - Repository-Files


```mermaid
flowchart TB

    subgraph copilot[copilot]
        C1["<b>copilot/context.md</b><br/><span style='font-size:10px;color:#888'>Basic non functional information + Quality expectation + Basic LLM guidelines</span>"]
        C2["<b>copilot/architecture.md</b><br/><span style='font-size:10px;color:#888'>Highlevel Software Architecture<br/>Functionality split in Components + Interfaces and flowcharts</span>"]
        C3["<b>copilot/refinement.md</b><br/><span style='font-size:10px;color:#888'>Current idea of the implementation</span>"]
        C9["<b>copilot/review.md</b><br/><span style='font-size:10px;color:#888'>Review of the current state of the software</span>"]
        C10["<b>copilot/verify.md</b><br/><span style='font-size:10px;color:#888'>Final verification result</span>"]
    end

    subgraph tickets[copilot/tickets]
        C4["<b>copilot/tickets/kanban.md</b><br/><span style='font-size:10px;color:#888'>Kanban overview of all tickets</span>"]
        C5["<b>copilot/tickets/####.md</b><br/><span style='font-size:10px;color:#888'>Ticket to implement</span>"]
        C8["<b>copilot/tickets/debt_####.md</b><br/><span style='font-size:10px;color:#888'>Technical debt ticket</span>"]
    end
```

### Mermaid kanban example

Optional helper: `scripts/kanban.py` can generate this Mermaid overview from all tickets. Agents should execute it after `implement`/`refine` only when the script exists in the target project.

```mermaid
---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
  Debt
    a[Old Architecture]@{ ticket: d0001, assigned: 'core', priority: 'High' }
    a[Old Architecture]@{ ticket: d0002, assigned: 'utils', priority: 'High' }
  Todo
    a[Implement Buildsystem]@{ ticket: 0001, assigned: 'buildsystem', priority: 'High' }
    a[Implement corestructure]@{ ticket: 0002, assigned: 'core', priority: 'High' }
  InProgress
    a[Creating Documents]@{ ticket: 0003, assigned: 'core', priority: 'Low' }
  Done
    a[Remove Old files]@{ ticket: 0004, assigned: 'none', priority: 'Very Low' }
  Failed
    a[Remove src]@{ ticket: 0005, assigned: 'core', priority: 'Very High' }

```