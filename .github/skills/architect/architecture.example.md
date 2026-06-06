# Software Architecture

> Example: simple CLI note-taking app (C++20).

## 1. Overview
- Store, list and search plain-text notes from the command line.

```mermaid
flowchart TB
  CLI[CLI] --> Core[NoteCore]
  Core --> Store[Storage]
```

## 2. Components

### CLI
- Responsibility: parse args, render output.
- Modules: ArgParser, Renderer
- Interfaces: required `NoteService`

### NoteCore
- Responsibility: business logic for notes.
- Modules: NoteService, Search
- Interfaces: provided `NoteService`; required `NoteRepository`

### Storage
- Responsibility: persist notes on disk.
- Modules: FileRepository
- Interfaces: provided `NoteRepository`

```mermaid
classDiagram
  class NoteService {
    +add(text) Note
    +list() vector~Note~
    +search(query) vector~Note~
  }
  class NoteRepository {
    +save(Note)
    +loadAll() vector~Note~
  }
  NoteService --> NoteRepository
```

## 4. Interfaces
| Interface | Provider | Consumer | Purpose |
|-----------|----------|----------|---------|
| NoteService | NoteCore | CLI | note operations |
| NoteRepository | Storage | NoteCore | persistence |

## 5. Data / Flow

```mermaid
sequenceDiagram
  participant U as User
  participant C as CLI
  participant S as NoteService
  participant R as FileRepository
  U->>C: notes add "buy milk"
  C->>S: add("buy milk")
  S->>R: save(note)
  R-->>S: ok
  S-->>C: Note
  C-->>U: "Note #3 added"
```

## 6. Cross-cutting
- Errors: exceptions mapped to exit codes.
- Config: notes dir via `NOTES_DIR` env var.

## 7. Open questions
- Encryption needed? (TBD)

