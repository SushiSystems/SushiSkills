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

## Migration progress

Recorded after each repository, by `RW-24`.

| Repository | State | Commit | Notes |
| --- | --- | --- | --- |
| sushiskills | done | `115d3ef`, `25737bc` | No design document to reshape |
| sushilog | done | `32b9f59` | No design document; shared tools copied whole |
| sushiweb | done | `887716b9` | `SOCIAL_APP.md` became a topic folder of seven pages; 62 source files repointed; only the design checker and the ceiling copied, as the other shared tools raise licence findings that predate this work |
| sushicore | done | `348ddd8` | Three documents reshaped in place; the GPU run evidence moved to `docs/agent/2026_10_14_GPU_TOOLKIT_SELECTION/REPORT.md`; shared tools copied whole |
| sushiai | done | `96a162c` | Seven documents reshaped; `GRAPH_CAPABILITIES.md` (1117 lines) became a topic folder of five pages; phase states read from each document's own status line and from the status of the work folders it names, so the owner should confirm them; the plan's source commits moved to `docs/agent/2026_10_21_GRAPH_CAPABILITIES_SOURCES/`; shared tools copied whole |
| sushitrack | done | `ed9d79e` | One document reshaped in place; the phase states read from its own status line, so the owner should confirm them; shared tools copied whole |
| sushiblas | done | `45a5a52` | Four documents reshaped; the module split and GPU run evidence moved to two work folders; the build states are read from each document's own status text, so the owner should confirm them; shared tools copied whole |
| sushihub | done | `c3e8fd2` | The checkout is `sushistack/`, whose remote is SushiHub. Three documents reshaped; the landing records of the decoupling waves moved to a work folder; only the design checker, its test and the ceiling copied, as the other shared tools predate this work |
| sushiruntime | done | `f134019` | Five documents reshaped; the engine backbone plan and the substrate plan became topic folders; phase states for WP-0 to WP-3, WP-6 and WP-DOCS are the last recorded reading and WP-7 is contradictory between two documents, so the owner should confirm them; shared tools copied whole |
| sushidsp | done | `1efc691` | Five documents reshaped; the SushiDSP design became a topic folder; dated phase records, hashes and measurements moved to four work folders; phase states read from the documents' own text, so the owner should confirm them; the design checker, its test, the ceiling and `check_all.py` copied |
| project-mobilerts | done | `ccdab09c2` | The git checkout is `project-mobilerts-legacy/`; `project-mobilerts/` is a Plastic SCM Unity project with no `docs/`. Thirteen documents reshaped, three of them topic folders; phase states derived from each document's status and tables, so the owner should confirm them; the closed licence header of the repository kept on the copied tools |
| sushifx, sushistack, IpekWeb, MAYAGAWeb, SerkanGaripWeb | not applicable | | No design documents, or no `docs/` tree |
| sushiengine | open | | 1 177 findings, 51 above the ceiling; last |

## How to continue

For a session on another machine. Work from sibling checkouts of the repositories, side by side
with this one; take no clone path from this page.

1. Read `SPEC.md` for the format and `skills/documentation/DESIGN_FORMAT.md` for the rule.
2. Pick the next open repository from the table above, smallest first, `sushiengine` last.
3. Measure it: `python tools/documentation/check_design_format.py ../<repo> --report` and
   `python tools/documentation/check_docs_layout.py ../<repo> --rule rule_design_ceiling`.
4. Check the repository's tools against this one with
   `python tools/checking/copy_shared_tools.py ../<repo> --from . --report`. When the report lists
   only the four design format files, copy the whole set. When it lists many, copy only
   `check_design_format.py`, its test and `check_docs_layout.py`, as sushiweb did: the full copy
   raises licence findings in `check_source_comments.py` that predate this work. sushidsp,
   sushiengine and sushistack were behind in the known issues scope work for the same reason.
5. Reshape each design document into the five sections, one repository per commit. Keep the
   section titles other files cite (search `git grep` for the document's name). Split a document
   above 400 lines into `<TOPIC>/` with a README and one page per part. Move dated evidence and
   hashes to a work folder `REPORT.md`.
6. Close the repository with its checkers, the tools README row, the changelog line and
   `python tools/check_all.py .` (or its own checkers when it has no `check_all.py`).
7. Write the repository's row in the table above and update `RW-24` before the next repository.

The phase states in the migrated documents are read from each document's own status line and
from the status of the work folders it names. They are not verified against the code; the owner
confirms them.

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
