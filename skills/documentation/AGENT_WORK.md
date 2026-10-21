# Design documents and agent work

Read from the `documentation` skill before opening a design document or a work folder under
`docs/agent/`, or before closing a piece of work.

## One topic, one design document

- `docs/design/README.md` maps every topic to exactly one document. Before writing, look the
  topic up there. If a document exists, extend it; never open a second one on the same topic.
- A design document has the sections, the one-line status and the phase table of
  `DESIGN_FORMAT.md`. Its second line is its status, in one of four forms. Text may follow the date
  after a full stop.

  | Form | Meaning |
  | --- | --- |
  | `**Status:** Open — <where it stands>` | Intent with work left |
  | `**Status:** Shipped — <YYYY-MM-DD>` | Built as designed on that date |
  | `**Status:** Superseded — <YYYY-MM-DD> by <link>` | Replaced by another document |
  | `**Status:** Withdrawn — <YYYY-MM-DD>, <reason>` | Given up by the owner |

- A design document above its ceiling (see "Size and one home" in `SKILL.md`) is split into
  `<TOPIC>/` with a `README.md` and one file per phase, and the map is updated in the same commit.
  The `README.md` carries the status; the phase files carry none.
- `REMAINING_WORK.md` is the only backlog and `## Next` in it the only order; its format is
  `BACKLOG_FORMAT.md`. No TODO list, roadmap, journal, handover, milestone or priority file sits
  under `docs/` outside `agent/` and `archive/`. Phases live in their design document, finished
  work in the changelog, a journal or a handover in the work folder that wrote it.

## Agent work lifecycle

1. **Open.** One folder: `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/`. Before opening, check that no
   open folder already covers the work; if one does, continue it. The folder's first file
   (`SPEC.md`, else `PLAN.md`, else `REPORT.md`) carries a status line in the forms above.
2. **Work.** The folder holds at most `SPEC.md`, `PLAN.md` and `REPORT.md`. Each is rewritten
   in place as the work moves. A second review round replaces the first `REPORT.md`; it is not
   a new file. A worker records each step in the folder right after finishing it, naming the
   commit, and does not ask first or wait for the end.
3. **Close.** The orchestrator, in one commit: writes the changelog line, dates the work
   folder's status and the design status, writes the decisions the work made into its design
   document, updates `REMAINING_WORK.md`, updates the module READMEs and manual pages the work
   made false.
4. **Archive.** A work folder or a design document whose status has carried a `Shipped`,
   `Superseded` or `Withdrawn` date for 90 days moves to `docs/archive/` as it is, keeping its
   path below `docs/`. The clock reads the date in the status line, never a commit date, which a
   pass over many files would reset. `check_docs_layout.py` lists the candidates.

The manual is never archived; it is kept true.

## Who writes where

Who may write which file is the Roles table of `multi-agent-work`.

A worker whose change makes a page outside its write list false reports the page and the exact
lines. The orchestrator corrects them in the commit that closes that piece of work. Reported is
not corrected.

