---
name: init
description: creates basic files to setup this project for further and enhanced work.
allowed-tools: shell
---

basic files: copilot/context.md

# Phase 1 - Interview

This skill creates the basic files and basic content. Check the existing project and files. Then ask the user relentlessly about the project, process, quality(Testing), tech stack and also about bugs, gaps, problems and contradicting information in the existing problem to be able to create the best possible context.md. Always ask for clarification if you are not sure about something. Do not make assumptions.

## Phase 2 - context.md

Create the file context.md The following sections should be created. Use this file as input for the content of context.md there might be answered questions.

### I. Project description
Summarize the project in a few sentences. Try to write mermaid diagrams instead of writing too much plain text.

### II. Tech stack
Default in case project not exists:
- C++ 20
- cmakelists.txt with cmake presets
- GoogleTest
- clang-format and clang-tidy
- development platform: windows 11

### III. Quality requirements
Default in case project not exists:
- Always execute clang-format, clang-tidy, all tests, all build-targets before finishing your tasks and tickets. If any of these fails, fix the problems before finishing your task. If you are not able to fix the problems, ask the user for help.
- Write long-term maintainable code. This includes a well-designed architecture, tests and clean code.
- Keep the software small and simple, go for simple solutions.
- Do not create duplicate code,  reuse as much as possible.

### IV: Overview of filestructure
Default in case project not exists:
- src: Contains all source code
- rsc: Contains all resources, i.e. images, diagrams, icons and so on
- test: Contains all tests, organized in the same way as src
- copilot: Contains generated documents, i.e. tickets, documents
- scripts: Contains all scripts, i.e. for the workflow, buildsystem, automatic checks, and so on
- install: contains per cmake Preset a finished executable, including all dependencies, ready to be executed on the target system. This is the output of the build system.

### V. Test requirements
Default in case project not exists:
- Test framework
- Write tests before writing the implementation (TDD)
- Write tests for each bug that you find (Regression tests)
- For each test use a highly versatile test selection based on failure expections. Also include the standards (low limit, high limit, outside of limits, empty, full, and so on).

### VI. Context
Write an detailed description of the project. Its targets, stories, user flows, requirements, ideas, state. Try to use as much mermaid diagrams as possible.

### VII. Appendix
Write down links to resources that are relevant for the project

### VIII - Glossary.md
Write down words and their definition that have special context in this project and are necessary to understand the documents of this projects.
standard glossary to extend:
- Software Design: Defines components, their included functionality and the interfaces.
- Software Architecture: Defines the implementation of all modules, units of a component in detail (i.e. mostly class diagrams)
- Component: Highest level of abstraction of functionality. A component can be divided into sub-components and sub-sub-components if needed but this is only for extremly big projects. A Component contains modules and the component unit (named after the component). Components do not necessary be software relevant, its just a group of functionality. (I.e. Component "User Management" could contain modules "Authentication", which contains Units "WebDav", "OAuth", "LDAP" and so on.)
- Module: Groups units that belong together and share common interfaces. A module can also have a unit that is named after the module.
- Unit: A unit is a .h and a .c/cpp file that mostly contains a class.
- Interface: An interface are the functions that are needed to interact with a Component/Module/Unit. Interfaces can be functions of a class, an abstract/virtual class and even static global functions.
- Test driven development (TDD): First implement tests that will cover all functionality that is followed to implement.
- Regression test: First write a test that shows the bug, then implement the fix for the test and thus solving the bug.
- Dept: Tasks that are not related to the functionality of the project but aim for general improvements, i.e. refactoring, improving the architecture, improving the process, and so on.

### IX - Abbreviations
Write down abbreviations and their meaning that are relevant for the project.