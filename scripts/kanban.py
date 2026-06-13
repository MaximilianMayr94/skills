#!/usr/bin/env python3
"""Generate copilot/tickets/kanban.md (Mermaid kanban) from all ticket files.

- Reads every ticket `*.md` in `copilot/tickets/` (and `copilot/tickets/done/`).
- Parses State / Assigned to / Priority / Title from the ticket header.
- Writes a Mermaid `kanban` overview to `copilot/tickets/kanban.md`.
- Moves all `Done` tickets into `copilot/tickets/done/`.

Ticket format (see .github/skills/ticket_prep/ticket.default.md):
    # Ticket #### - Title
    - **State:** Dept | Open | InProgress | Done | Failed
    - **Assigned to:** <component/module>
    - **Priority:** Very Low | Low | Medium | High | Very High
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path

# State value -> kanban column.
STATE_TO_COLUMN = {
    "dept": "Debt",
    "debt": "Debt",
    "open": "Todo",
    "todo": "Todo",
    "inprogress": "InProgress",
    "done": "Done",
    "failed": "Failed",
}

# Column render order.
COLUMN_ORDER = ["Debt", "Todo", "InProgress", "Done", "Failed"]

TICKETS_DIR = Path(__file__).resolve().parent.parent / "copilot" / "tickets"
DONE_DIR = TICKETS_DIR / "done"
KANBAN_FILE = TICKETS_DIR / "kanban.md"

KANBAN_HEADER = """---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
"""


@dataclass
class Ticket:
    path: Path
    ticket_id: str
    title: str
    state: str
    column: str
    assigned: str
    priority: str


def _field(pattern: str, text: str, default: str = "") -> str:
    """Return first capture group of `pattern` in `text` or `default`."""
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else default


def parse_ticket(path: Path) -> Ticket | None:
    """Parse a single ticket file. Returns None if it is not a ticket."""
    text = path.read_text(encoding="utf-8")

    header = re.search(r"^#\s*Ticket\s+(\S+)\s*-\s*(.+)$", text, re.MULTILINE)
    if not header:
        return None

    raw_id, title = header.group(1).strip(), header.group(2).strip()

    state = _field(r"\*\*State:\*\*\s*([^\n,]+)", text, "Open")
    assigned = _field(r"\*\*Assigned to:\*\*\s*([^\n]+)", text, "none")
    priority = _field(r"\*\*Priority:\*\*\s*([^\n,]+)", text, "Medium")

    column = STATE_TO_COLUMN.get(state.lower().strip(), "Todo")

    ticket_id = re.sub(r"\D", "", raw_id) or raw_id

    return Ticket(
        path=path,
        ticket_id=ticket_id,
        title=title,
        state=state,
        column=column,
        assigned=assigned or "none",
        priority=priority or "Medium",
    )


def collect_tickets() -> list[Ticket]:
    """Read all ticket files from the tickets dir and the done subfolder."""
    files: list[Path] = []
    for directory in (TICKETS_DIR, DONE_DIR):
        if directory.exists():
            files.extend(
                p for p in directory.glob("*.md") if p.name != KANBAN_FILE.name
            )

    tickets: list[Ticket] = []
    for path in sorted(files):
        ticket = parse_ticket(path)
        if ticket:
            tickets.append(ticket)
    return tickets


def render_kanban(tickets: list[Ticket]) -> str:
    """Render the Mermaid kanban markdown from parsed tickets."""
    lines = ["# Kanban", "", "```mermaid", KANBAN_HEADER.rstrip("\n")]

    by_column: dict[str, list[Ticket]] = {col: [] for col in COLUMN_ORDER}
    for ticket in tickets:
        by_column.setdefault(ticket.column, []).append(ticket)

    for column in COLUMN_ORDER:
        column_tickets = by_column.get(column, [])
        if not column_tickets:
            continue
        lines.append(f"  {column}")
        for ticket in column_tickets:
            lines.append(
                f"    a[{ticket.title}]@{{ ticket: {ticket.ticket_id}, "
                f"assigned: '{ticket.assigned}', priority: '{ticket.priority}' }}"
            )

    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def move_done_tickets(tickets: list[Ticket]) -> list[Path]:
    """Move all Done tickets into the done/ folder. Returns moved paths."""
    moved: list[Path] = []
    for ticket in tickets:
        if ticket.column != "Done":
            continue
        if ticket.path.parent == DONE_DIR:
            continue
        DONE_DIR.mkdir(parents=True, exist_ok=True)
        target = DONE_DIR / ticket.path.name
        shutil.move(str(ticket.path), str(target))
        ticket.path = target
        moved.append(target)
    return moved


def main() -> None:
    if not TICKETS_DIR.exists():
        raise SystemExit(f"Tickets folder not found: {TICKETS_DIR}")

    tickets = collect_tickets()
    KANBAN_FILE.write_text(render_kanban(tickets), encoding="utf-8")
    moved = move_done_tickets(tickets)

    print(f"Parsed {len(tickets)} ticket(s).")
    print(f"Wrote {KANBAN_FILE}")
    print(f"Moved {len(moved)} done ticket(s) to {DONE_DIR}")


if __name__ == "__main__":
    main()

