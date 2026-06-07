# Review

> Example: CLI note-taking app.

## Summary
- Core works, but persistence lacks error handling and tests.

## Findings
| # | Severity | Location | Problem | Suggestion | -> Ticket |
|---|----------|----------|---------|------------|-----------|
| 1 | High | FileRepository.cpp | corrupt file crashes load | skip + warn | debt_0001 |
| 2 | Medium | NoteService | no input validation | reject empty text | debt_0002 |
| 3 | Low | CLI Renderer | duplicated format code | extract helper | debt_0003 |

## Gaps & contradictions
- No tests for `search` edge cases.
- architecture.md mentions encryption, code has none.

## Suggested architecture/refinement changes
- Mark encryption as future scope or remove from architecture.md.

