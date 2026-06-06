# Review

> Example: CLI note-taking app.

## Summary
- Core works, but persistence lacks error handling and tests.

## Findings
| # | Severity | Location | Problem | Suggestion | -> Ticket |
|---|----------|----------|---------|------------|-----------|
| 1 | High | FileRepository.cpp | corrupt file crashes load | skip + warn | dept_0001 |
| 2 | Medium | NoteService | no input validation | reject empty text | dept_0002 |
| 3 | Low | CLI Renderer | duplicated format code | extract helper | dept_0003 |

## Gaps & contradictions
- No tests for `search` edge cases.
- architecture.md mentions encryption, code has none.

## Suggested architecture/refinement changes
- Mark encryption as future scope or remove from architecture.md.

