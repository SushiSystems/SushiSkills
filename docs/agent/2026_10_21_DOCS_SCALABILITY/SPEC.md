# Documentation that scales

**Status:** Open — research done on 2026-10-21; the owner has not yet chosen between the options below

## Problem

The module tree and the test tree scale: a new module adds a folder in a fixed place, and a checker
says when a test has no home. `docs/` does not. Measured on `sushiengine` on 2026-10-21, four months
after its first commit:

| Measure | Value |
| --- | --- |
| Design topics | 71, in one folder; `docs/design` has 73 entries |
| Work folders in `docs/agent` | 83, in one folder; 63 of them were opened on one day, one per reshaped design |
| Markdown files added to `docs/` per month | 42 to 136 in agent work alone, since August |
| Citations of a design document by path | 1 963, over 183 distinct paths |
| Citations rewritten by one reshape of the corpus | more than 600 |
| Modules a design topic cites | 1 module: 3 topics; 2 to 3: 14; 4 to 8: 22; 9 or more: 30 |
| Modules that no design topic cites | 30 of 122 |

Four costs follow.

1. **One flat folder per kind.** A topic list read by eye stops working somewhere past 150 entries.
   `docs/design/README.md` is edited by hand, one row per topic, and every agent that adds a topic
   touches it, so it is also where parallel sessions collide.
2. **Paths are identities.** A design document is cited by its path, so moving or splitting one costs
   a repair pass over the whole repository. The format migration did this once; it will be needed
   again each time the shape changes.
3. **Records outnumber designs.** Each design reshaped to the format left one work folder of dated
   record. The record belongs to one design and nothing else, yet it lives apart, ages on its own
   clock and doubles the folder count.
4. **A document cannot be reached from the code it governs.** Nothing says which designs apply to a
   module, and 30 modules have none. A reader of a module README does not learn that a 6 000-line
   design owns its behaviour.

## What other projects do

Evidence from the web search of 2026-10-21 is marked (web); the rest is from memory and not yet
re-verified.

- **Linux kernel documentation** grew into a top level its own maintainer calls a mess, and has been
  reorganised by audience. Architecture documents moved into `Documentation/arch` so that they match
  the source tree. The hand-maintained `00-INDEX` files were deleted in 2018. (web)
- **Architecture decision records** are append-only and numbered. One team keeps a single global
  sequence for the whole repository and tags each record with an area, because decisions that span
  tiers are easier to find in one place; a superseded record points to its replacement and is
  never rewritten. Index generation from the records' links is common tooling. (web)
- **Kubernetes enhancement proposals** are grouped by the owning special interest group, not by code
  path, and carry a machine-readable metadata file so that dashboards and release tooling read status
  without parsing prose. The layout was not confirmed by the search; check the `kubernetes/enhancements`
  repository before relying on it.

The pattern across them: ownership or audience decides the tree, a stable identifier survives moves,
and indexes are generated from metadata instead of kept by hand.

## Options

**A. Mirror the module tree.** `docs/design/<layer>/<module>/<TOPIC>/`, checked like the test mirror.
Rejected on the measurement: only 3 of 71 topics touch one module, and 30 touch nine or more. A mirror
would force a single home on a document that has many, and a module rename would move documents and
break citations.

**B. Shard by area, describe by metadata, generate the indexes.** Described below.

**C. Keep the flat tree and generate only the topic map.** Cheap, and it fixes the collision on
`docs/design/README.md`. It does not bound any folder, and it leaves the path-as-identity cost.

## Recommendation: B

1. **Areas.** `docs/design/<area>/<TOPIC>/`, with the area one of a short fixed list that follows the
   module layers: `foundation`, `domain`, `asset`, `world`, `presentation`, `applications`, `tooling`
   and `cross` for documents about the whole engine. A topic gets its area once, from the layer of the
   module that owns its behaviour, and does not move when the code moves. Most areas then hold tens
   of topics, not hundreds.
2. **Metadata under the status line**, one field per line, checked: `**Area:**`, `**Modules:** ` (the
   module paths the topic governs, each of which must exist), and `**Record:**` (see 4). The status
   line keeps its 160-character limit and its four forms.
3. **Generated indexes.** The topic map of `docs/design/README.md`, one index per area, and a
   `Designs` block in every module README between generation markers are written by a tool from the
   metadata and verified by the same tool in CI. Nobody edits a row by hand, so sessions no longer
   collide. `check_design_backlog_coverage` keeps reading the generated map.
4. **The record lives with its design.** A topic's execution record, today a work folder named
   `<date>_<TOPIC>_RECORD`, becomes `<TOPIC>/RECORD.md` or `<TOPIC>/record/`. The record is exempt from
   the no-dates and no-hashes rules and from the reachable-from-index rule, is not counted in the
   topic's pages, and moves to the archive together with its design 90 days after `Shipped`. Work that
   does not belong to one design (an audit, a review, a tooling change) stays in `docs/agent/` and
   names the designs it touched in a `**Designs:**` line, which the tool reads to build the other
   direction of the link. This is the owner's idea of 2026-10-21, kept in part: the numbers above are
   why the earlier answer, that the two should stay apart, no longer holds for per-design records.
5. **Bounded folders.** A ceiling of entries per folder, checked as the 400-line ceiling is, forces a
   shard at the moment a folder grows, in `docs/design/<area>/`, `docs/agent/` and the archive. The
   archive shards by year and month.
6. **Stable references.** A citation names the topic, `docs/design/<area>/<TOPIC>/`, and a tool
   resolves a bare `<TOPIC>` to its path. A move of a topic between areas is then one generated
   rewrite, not a hand repair, and the resolver reports any citation it cannot place.

## Risks

- Choosing the area is a judgement. Mitigated by the fixed list and by `cross` as the answer when
  two areas fit.
- The generated blocks in module README files are the first generated text in them. A checker must
  tell a hand edit inside the markers from a stale block.
- Moving 71 topics and rewriting about 2 000 citations is one more migration of the kind just
  finished. It should run once, with the tool of point 6, not by hand.
- The rule change lives in SushiSkills, so every sibling repository follows it; the `documentation`
  skill, `check_docs_layout.py`, `check_design_format.py` and a new generator change together.

## Open questions

1. Is the area list right: eight values, taken from the layers? A repository with other layers
   defines its own list in `tools/settings.py`.
2. Is the record folder inside the topic acceptable, given that it relaxes the no-dates rule for one
   named file?
3. The entry ceiling per folder: 40, 60 or 100?
4. Does the owner want the migration of `sushiengine` to be the pilot, with the tools written first
   in SushiSkills and run there before the other repositories?

## Phases

| Id | Phase | State |
| --- | --- | --- |
| D0 | Research and options, this document. | built |
| D1 | The owner chooses an option and answers the open questions. | planned |
| D2 | Rules and tools in SushiSkills: metadata fields, entry ceiling, generator and resolver, with tests. | planned |
| D3 | Pilot on `sushiengine`: move the topics into areas, generate the indexes, fold the records. | planned |
| D4 | The remaining repositories follow, smallest first. | planned |
