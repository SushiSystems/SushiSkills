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

## Linking work to a design

A work folder that carries out a phase of a design says so under the status line of its first file,
one field to a line:

| Field | Holds |
| --- | --- |
| `**Implements:**` | `TOPIC#PHASE` items, separated by commas, naming phases in the topic's phase table |
| `**Designs:**` | Topics the work touches without carrying out one of their phases, separated by commas |

An audit or a tooling change that serves no design carries neither line. `check_design_topics.py`
fails an item whose topic or phase does not exist, so a renamed phase is found where the work cites it.

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
4. **Delete.** A closed work folder, and a design document that is `Superseded` or `Withdrawn`, is
   deleted: the version history keeps it, and the decisions it made are already in the topic. The
   clock reads the date in the status line, never a commit date, which a pass over many files would
   reset. `check_docs_layout.py` lists each one closed for longer than `K_CLOSED_GRACE_DAYS` in
   `tools/settings.py`: 90 days by default, 0 in a repository that deletes at close. A `Shipped`
   design document stays as the record of its decisions and their reasons; what the code now is
   belongs on the module page.

## The archive

`docs/archive/` holds frozen text and nothing new is moved into it. A repository that still tracks
one runs `tools/documentation/retire_archive.py --apply` once the repository cites nothing in it:
the tool tags the history `docs-archive-<date>`, unstages the folder and ignores it, and the
commit follows. A repository that sets `K_ARCHIVE_UNTRACKED` in `tools/settings.py` has
`check_design_topics.py` fail every line that cites the archive; each such citation is repointed to
the topic that holds the decision, or dropped. A decision that only an archived folder held is not
recovered.

The manual is never deleted; it is kept true.

## Who writes where

Who may write which file is the Roles table of `multi-agent-work`.

A worker whose change makes a page outside its write list false reports the page and the exact
lines. The orchestrator corrects them in the commit that closes that piece of work. Reported is
not corrected.

