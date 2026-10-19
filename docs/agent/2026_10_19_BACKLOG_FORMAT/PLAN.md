# Backlog format: plan

**Status:** Open — part 1 done on 2026-10-19; part 2 migrated sushilog, ten repositories left.

Runs inline (D10). Each task has one acceptance criterion and one build, the build being
`python tools/check_all.py .` in the repository the task changes. Tasks 1 to 5 change sushiskills
only and name no other repository in what they write. The migrations follow, one per repository.

## Part 1: sushiskills

### Task 1. The format and the status forms in the skills

Files:

- `skills/documentation/BACKLOG_FORMAT.md` (new): SPEC sections 2 to 4, examples naming no real
  repository.
- `skills/documentation/SKILL.md`: a "Read before" row for it.
- `skills/documentation/AGENT_WORK.md`: the four status forms, the close step setting the date,
  the archive clock, the files D13 forbids.
- `skills/debugging/SKILL.md`, "Known issues": the entry parts become a citation.
- `skills/testing/SKILL.md`, rule 5: the quarantine entry cites `Owner:` and `Fix by:`.

Acceptance: each rule of SPEC sections 2 to 4 and 6 is written in exactly one of these files, and
`check_all.py` passes.

### Task 2. `check_docs_layout.py`: status lines, archive clock, forbidden kinds

Files: `tools/documentation/check_docs_layout.py`, `tools/tests/test_check_docs_layout.py`, and
the status lines of sushiskills' own work folders, which the new rule reads.

- `rule_status_lines` accepts only the four forms, in design documents and in the first file of
  each work folder.
- `rule_archive_candidates` reads the date of a `Shipped`, `Superseded` or `Withdrawn` line;
  `_last_commit_age_days` goes if nothing else uses it.
- `rule_forbidden_kinds`, new.

Tests first: each rule has a failing case and a passing case, the clock case included (a status
dated 91 days ago is a candidate, a commit dated yesterday does not save it).

Acceptance: the new tests fail before the change and pass after, and `check_all.py` passes.

### Task 3. `check_backlog.py`

Files: `tools/documentation/check_backlog.py`, `tools/tests/test_check_backlog.py`.

The six rules and the `--report` count of SPEC section 5, on the `checking.checker` frame,
shaped like its siblings. Sibling discovery is tested with a temporary folder holding two
repositories. Not yet in `check_all.py`, since sushiskills' own files are not converted.

Acceptance: every rule has a failing and a passing test, the tests pass, and `check_all.py`
passes.

### Task 4. sushiskills on the new format

Files: `docs/design/REMAINING_WORK.md`, `docs/reference/KNOWN_ISSUES.md`,
`tools/check_all.py` (`K_CHECKERS`), `tools/README.md`, `skills/project-tools/SKILL.md` (the
checker's row and the "Backlog fact check" audit).

The fact check runs on sushiskills' own backlog first and its verdicts go into `REPORT.md`. The
"Estate programmes" section is foreign under D2; it stays, listed by `--report`, until the
repository that coordinates the programmes migrates and takes it.

Acceptance: `check_all.py` passes with `check_backlog.py` in it.

### Task 5. Close part 1

Files: `docs/reference/CHANGELOG.md`, `docs/design/REMAINING_WORK.md`, `REPORT.md`, this plan's
status.

The owner approves the commit. The shared tools reach the other repositories in their
migrations, not before.

Acceptance: `check_all.py` passes and the owner has approved the commit.

## Part 2: migrations

One task per repository, lower tiers first, so that a target exists before it is cited. The
coordinating repository goes last, because its programme entries cite everyone else's IDs:

1. sushilog
2. sushicore
3. sushiruntime
4. sushiblas
5. sushiai
6. sushidsp
7. sushiengine
8. sushitrack
9. sushiweb
10. project-mobilerts-legacy
11. sushistack

Each migration opens its own work folder in that repository,
`docs/agent/<date>_BACKLOG_MIGRATION/`, and follows SPEC section 8. Two stops for the owner per
repository:

1. The inventory in that folder's `REPORT.md`: each entry and open design document marked true,
   stale, closed or foreign; each forbidden file and where its parts go; the proposed `## Next`.
2. The commit.

A shared checker copied in may find faults that predate this work. Those go into the
repository's new backlog as entries, not into the migration.

Acceptance per repository: `check_all.py` passes there, and `check_backlog.py --report` lists no
foreign entry the owner has not accepted.

## Risks

- Large repositories can turn the inventory into a long review. sushiengine has 104 design
  documents and two backlog files of 435 and 928 lines; its inventory is split by design topic
  if one sitting cannot hold it.
- A sibling checked out on another branch resolves IDs against that branch. `--report` names the
  branch it read.
