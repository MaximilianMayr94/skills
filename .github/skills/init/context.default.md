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

## VI. Context
- Detailed description: targets, stories, user flows, requirements, ideas, state.
- Use as much mermaid as possible.

## VII. Appendix
- Links to resources relevant for the project.

## VIII. Glossary
Words with special meaning in this project. Standard glossary to extend:
- Software Design: Defines components, their included functionality and the interfaces.
- Software Architecture: Defines the implementation of all modules, units of a component in detail (i.e. mostly class diagrams)
- Component: Highest level of abstraction of functionality. A component can be divided into sub-components and sub-sub-components if needed, but this is only for extremely big projects. A component contains modules and the component unit (named after the component). Components are not necessarily software-relevant; they are groups of functionality. (I.e. component "User Management" could contain module "Authentication", which contains units "WebDav", "OAuth", "LDAP" and so on.)
- Module: Groups units that belong together and share common interfaces. A module can also have a unit that is named after the module.
- Unit: A unit is a .h and a .c/cpp file that mostly contains a class.
- Interface: An interface are the functions that are needed to interact with a Component/Module/Unit. Interfaces can be functions of a class, an abstract/virtual class and even static global functions.
- Test driven development (TDD): First implement tests that will cover all functionality that is followed to implement.
- Regression test: First write a test that shows the bug, then implement the fix for the test and thus solving the bug.
- Technical debt: Tasks that are not related to project functionality but aim for general improvements, i.e. refactoring, improving the architecture, improving the process, and so on.

## IX. Abbreviations
- Abbreviations and their meaning relevant for the project.

