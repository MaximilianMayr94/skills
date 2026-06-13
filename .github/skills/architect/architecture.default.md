# PROJECT_NAME - Software Requirements

## Overview
- Very short overview of purpose and functionality of the software. One or two sentences.
- High-level component diagram.

```mermaid
flowchart TB
  C1[Component A] --> C2[Component B]
```

## Components
For each component repeat:

### <Component Name>
- Responsibility: <what it does>

#### Interface
- <provided / required>

```mermaid
classDiagram
  class Unit {
    +interfaceMethod()
  }
```

## Data / Flow
- Key flows as sequence diagrams.

```mermaid
sequenceDiagram
  participant A
  participant B
  A->>B: request()
  B-->>A: response()
```


