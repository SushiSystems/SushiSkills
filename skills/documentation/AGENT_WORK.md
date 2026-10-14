# Design documents and agent work

Read from the `documentation` skill before opening a design document or a work folder under
`docs/agent/`, or before closing a piece of work.

## One topic, one design document

- `docs/design/README.md` maps every topic to exactly one document. Before writing, look the
  topic up there. If a document exists, extend it; never open a second one on the same topic.
- Every design document's second line is its status:
  `**Status:** Open — phase 2 of 4` or `**Status:** Shipped`.
- A design document above its ceiling (see "Size and one home" in `SKILL.md`) is split into
  `<TOPIC>/` with a `README.md` and one file per phase, and the map is updated in the same commit.
- `REMAINING_WORK.md` is the only backlog. No TODO lists anywhere else.

## Agent work lifecycle

1. **Open.** One folder: `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/`. Before opening, check that no
   open folder already covers the work; if one does, continue it.
2. **Work.** The folder holds at most `SPEC.md`, `PLAN.md` and `REPORT.md`. Each is rewritten
   in place as the work moves. A second review round replaces the first `REPORT.md`; it is not
   a new file.
3. **Close.** The orchestrator, in one commit: writes the changelog line, updates the design
   status and `REMAINING_WORK.md`, updates the module READMEs and manual pages the work made
   false.
4. **Archive.** A work folder or a shipped design document with no commit for 90 days moves to
   `docs/archive/` as it is, keeping its path below `docs/`. `check_docs_layout.py` lists the
   candidates.

The manual is never archived; it is kept true.

## Who writes where

Who may write which file is the Roles table of `multi-agent-work`.

A worker whose change makes a page outside its write list false reports the page and the exact
lines. The orchestrator corrects them in the commit that closes that piece of work. Reported is
not corrected.

