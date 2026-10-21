# Design document format

**Status:** Shipped — 2026-10-21

## Problem

A survey of `sushiengine/docs/design` on 2026-10-21 found 111 files and 53 885 lines. 35 files
run over 600 lines and the largest reach 1 430. The 111 files hold 737 distinct `##` headings, so
no two share a layout. Most status lines are paragraphs: they list phases, commit hashes and dates,
which is what a work folder is for. A reader cannot tell from the status which document is alive.

## Decision

`docs/design/` and `docs/agent/` both stay, with sharper roles.

| | `docs/design/<TOPIC>.md` | `docs/agent/<DATE_WORK>/` |
| --- | --- | --- |
| Answers | What are we building and why this way? | What did this piece of work do and find? |
| Holds | The ruling, its reason, the shape, a phase table, open questions | Commit hashes, measurements, review findings, the working record |
| Never holds | Commit hashes, measurements, a dated narrative | A decision that outlives the work |
| Lives | As long as the topic | Until closed, then 90 days |

## Rules

1. A design document has exactly five `##` sections, in this order: `Problem`, `Decision`,
   `Design`, `Phases`, `Open questions`. Deeper headings are free.
2. The status line is one line of at most 160 characters. Progress is the phase table, not the
   status.
3. `Phases` holds one table with the columns `Id`, `Phase`, `State`. A state is `planned`,
   `building`, `built` or `withdrawn`.
4. A commit hash in a design document is a finding. The work folder holds it; the document links
   the folder.
5. The ceiling is 400 lines, down from 1 500. A split topic keeps its five sections in `README.md`.
6. Closing a work folder moves the decision it made into its design document.

## What changes

- `skills/documentation/DESIGN_FORMAT.md`: the format, in the one place it lives.
- `skills/documentation/AGENT_WORK.md`, `SKILL.md`: the ceiling, the close step and a pointer.
- `tools/documentation/check_design_format.py`: the rules for sections, status length, phase table
  and hashes. `check_docs_layout.py` takes the new ceiling.

## Not in scope

- Migrating any sibling repository. `sushiengine` has 111 documents to reshape, by agents, after
  the rule has run in one small repository.
- Judging whether a document's content is true.
