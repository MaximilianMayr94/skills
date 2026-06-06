# Ticket 0001

- **Title:** Implement FileRepository
- **Type:** feature
- **Assigned:** storage
- **Priority:** High
- **Status:** Todo
- **Depends on:** none

## Goal
- Persist and load notes from disk via `NoteRepository`.

## Scope
- In: `src/storage/FileRepository.{h,cpp}`, `test/storage/`
- Out: encryption, indexing

## Acceptance criteria
- [ ] `save(Note)` writes a note file
- [ ] `loadAll()` returns all stored notes
- [ ] corrupt file is skipped with a logged warning

## Tests (TDD)
- empty dir -> empty vector
- save then loadAll -> one note
- many notes round-trip
- corrupt file -> skipped

## Notes
- See architecture.md §2 Storage, refinement.md §2 Storage.

