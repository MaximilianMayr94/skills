---
name: init
description: creates the context.md file and asks you questiosns about the project the user can state when he is done or the ai stops asking questions.
allowed-tools: shell
---

# Goal
- Produce a high-quality `copilot/context.md`.

# Phase 1 - Scan
Scan the whole project for existing documentation, architecture, code quality, test quality, bugs, gaps, problems and contradicting information. Use this as input for the interview and the context.md. Do not assume that the existing information is correct. Also use `context.default.md` (this folder) as default input and `context.example.md` (this folder) to see how an result should look like.

# Phase 2 - Interview
Ask the user relentlessly about the project, process, quality(Testing), tech stack and also about bugs, gaps, problems and contradicting information in the existing problem to be able to create the best possible context.md. Always ask for clarification if you are not sure about something. Do not make assumptions. After a few questions - max 5. - ask the user if he wants to progress to phase 3 or in case you do not have more questions progress to phase 3. 

# Phase 3 - Create context.md

- Create `copilot/context.md` using `context.default.md` (this folder) as template.
- See `context.example.md` for a filled-out example.
- Fill every section (I–IX) from interview answers and project scan.
- The important chapter VI Context should be as detailed as a product requirements specification. Do not leave out any function that needs to be implemented, any user flow that needs to be supported.
- Sections marked "Default" in the template apply only when no project exists yet.
- Achieve a high-quality complete overview of the project so the architecture can flawlessly be created from it and the implementation can be done without further questions. The better the context.md, the better the architecture and implementation will be. So do not rush this step.
