# PROJECT_NAME - Context

## I. Project description
- Summarize the project in a few sentences.
- Prefer a mermaid diagram over plain text.

## II. Tech stack
- C++ 20
- cmakelists.txt with cmake presets
- GoogleTest
- clang-format and clang-tidy
- development platform: windows 11

## III. Quality requirements
- Always execute clang-format, clang-tidy, all tests, all build-targets before finishing your tasks and tickets. If any of these fails, fix the problems before finishing your task. If you are not able to fix the problems, ask the user for help.
- Write long-term maintainable code. This includes a well-designed architecture, tests and clean code.
- Keep the software small and simple, go for simple solutions.
- Do not create duplicate code, reuse as much as possible.

## IV. Overview of filestructure
- src: Contains all source code
- rsc: Contains all resources, i.e. images, diagrams, icons and so on
- test: Contains all tests, organized in the same way as src
- copilot: Contains generated documents, i.e. tickets, documents
- scripts: Contains all scripts, i.e. for the workflow, buildsystem, automatic checks, and so on
- install: contains per cmake Preset a finished executable, including all dependencies, ready to be executed on the target system. This is the output of the build system.

## V. Test requirements
- Test framework gtest
- Write tests before writing the implementation (TDD)
- Write tests for each bug/ticket that you implement/fix (Regression tests)
- For each test use a versatile test selection based on failure expectations. Also include standards such as low limit, high limit, outside of limits, empty, full, and so on.

## VI. Architecture
- Define software with high cohesion and low coupling.
- Hide lots of functionality behind interfaces. So less dependencies.
- Keep architecture simple
- Split the software into high level components - which are massive parts of the software. If the software is huge you can define sub-components and so on.
- Modules and units are part of refinement and implementation.

## VII. Appendix
- Links to resources relevant for the project.

## VIII. Glossary
Words with special meaning in this project. Standard glossary to extend:
- WORD: meaning
- ...

## IX. Abbreviations
- Abbreviations and their meaning relevant for the project.

