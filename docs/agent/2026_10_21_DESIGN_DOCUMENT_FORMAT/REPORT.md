# Design document format: report

**Status:** Shipped — 2026-10-21

The rule and its checker are in SushiSkills. No sibling repository is migrated; the work is
`RW-24`.

## What changed

- `skills/documentation/DESIGN_FORMAT.md`: the roles of a design document and a work folder, the
  five sections, the status line, the phase table.
- `skills/documentation/AGENT_WORK.md`, `SKILL.md`: the pointer, the close step that writes the
  work's decisions into the design document, the 400-line ceiling.
- `tools/documentation/check_design_format.py` and its test: `rule_sections`,
  `rule_status_length`, `rule_phase_table`, `rule_no_commit_hashes`, `rule_no_execution_record`.
- `check_docs_layout.py`: `K_DESIGN_LINE_CEILING` is 400.
- `check_all.py`, `tools/README.md`, `project-tools`: the eleventh checker.

`python tools/check_all.py .` reports clean.

## What the checker finds elsewhere

Read-only runs on 2026-10-21, before any sibling copies the tool:

| Repository | Format findings | Ceiling findings |
| --- | --- | --- |
| sushicore | 44 | 0 |
| sushiai | 94 | 1 |
| sushiweb | 19 | 1 |
| sushiengine | 1 177 | 51 |

The first column counts findings of `check_design_format.py`; the second counts findings of
`rule_design_ceiling`, which reads phase files as well as documents.

## Known weaknesses

- The checker sees form and two content signals, not meaning. `rule_no_commit_hashes` finds a hash
  with a digit and a letter, in a code span or bare; a hash of letters only passes.
  `rule_no_execution_record` finds a verb such as built or merged within a short span of an ISO
  date. A narrative with neither passes, and a legitimate sentence that happens to match (a
  decision that cites when a thing was merged) is a false finding. A run on `sushiengine` found 228
  such lines and 104 hashes; the first lines read were all real execution records.
- The 400-line ceiling is not tested against a document that is a table of contents for phase
  files; a split topic's README is held to the same ceiling.
- The shared tools are not copied into any sibling. A sibling that copies them fails its own check
  until it is reshaped.

## SOLID breaches and unneeded dependencies

None met. `check_design_format.py` imports `design_status.py` for the document list, as
`check_backlog.py` does.
