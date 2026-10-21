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

The pattern across them: ownership or audience decides the grouping, a stable identifier survives moves,
and indexes are generated from metadata instead of kept by hand.

## Options

Two placement rules that derive the tree from the code were measured on `sushiengine` and both fail.

- **Mirror the module tree**, or place a design at the common parent of the code it governs. Of 71
  topics, 50 land at the repository root when every cited unit counts, and 20 to 35 when only the main
  ones do. Designs cut across modules, so no rule of this kind gives them a home below the root.
- **Group by the first word of the name.** The 71 names have 48 different first words, most of them
  used once, so the folders would be singletons. Names were not chosen for this.

A hand-written list of subject areas fits the topics, but it fits one repository: another repository
has other subjects, and each new subject is a decision about the tree. That is the management cost
the owner named.

**A. Fixed folders by subject.** Rejected for the reason above.

**B. Flat storage, metadata for every cut, generated views.** Described below.

**C. Keep the flat tree and generate only the topic map.** Cheaper than B, and it leaves records,
citations and the module link as they are.

## Recommendation: B

The tree stops carrying meaning. It exists to keep folders small and paths stable. Every way a reader
wants to cut the designs, by subject, by module, by status, by owner, is a generated view of
metadata. A new subject is then a new tag value: no folder moves, no citation changes, and nothing to
decide about the tree.

1. **Storage.** `docs/design/<TOPIC>/`, one folder per topic, as it is today. Shipped, superseded and
   withdrawn topics leave for the archive after 90 days, so the folder holds live designs only. If a
   repository still passes the entry ceiling, the checker names the overflow rule, which is
   mechanical and needs no judgement: topics older than a cut-off year move under
   `docs/design/<year>/<TOPIC>/`, written by the tool with the citations repaired. Nothing in the
   tree is chosen by an author.
2. **Metadata under the status line**, one field per line, checked: `**Tags:**` (free words; the
   subject), `**Modules:**` (module paths the topic governs, each must exist) and `**Record:**`
   (see 4). The status line keeps its 160-character limit and its four forms.
3. **Generated views.** A tool writes, from the metadata, the topic map of `docs/design/README.md`,
   one page per tag, one per status, and a `Designs` block in every module README between generation
   markers. CI verifies that the generated text is current. Nobody edits a row by hand, so parallel
   sessions stop colliding, and a tag nobody has used before simply appears as a new page. A tag used
   once is listed so that near-duplicates (`render`, `rendering`) can be merged by editing one word.
4. **The record lives with its design.** A topic's execution record, today a work folder named
   `<date>_<TOPIC>_RECORD`, becomes `<TOPIC>/RECORD.md`. The record is exempt from the no-dates and
   no-hashes rules and from the reachable-from-index rule, is not counted in the topic's pages, and
   moves to the archive together with its design. Work that does not belong to one design (an audit,
   a review, a tooling change) stays in `docs/agent/` and names the designs it touched in a
   `**Designs:**` line, which the tool reads to build the other direction of the link. This is the
   owner's idea of 2026-10-21, kept in part: 63 record folders opened on one day are why the earlier
   answer, that the two should stay apart, no longer holds for per-design records.
5. **Bounded folders.** A ceiling of entries per folder, checked as the 400-line ceiling is, in
   `docs/design/`, `docs/agent/` and each archive folder. The archive shards by year and month with the
   same tool.
6. **Stable references.** A citation names the topic, and a tool resolves a bare `<TOPIC>` to its
   path. A move is one generated rewrite, not a hand repair, and the resolver reports any citation it
   cannot place.

Everything above is independent of the repository: the tool reads the layout from `tools/settings.py`
and needs no list of subjects.

## Risks

- Browsing the folder tree no longer tells a reader what a topic is about. The generated indexes do,
  and they sit one click from `docs/README.md`. If the owner wants the tree itself to carry the
  subject, a hand-written area list is the price, and it stays one repository's list.
- The generated blocks in module README files are the first generated text in them. A checker must
  tell a hand edit inside the markers from a stale block.
- Adding metadata to 71 topics and folding 63 records is one more migration of the kind just
  finished. It should be run once, by the tool of point 6.
- The rule change lives in SushiSkills, so every repository follows it: the `documentation` skill,
  `check_docs_layout.py`, `check_design_format.py` and a new generator change together.

## Open questions

1. Is a tree that carries no meaning acceptable, with tags and generated views doing the work?
2. Is the record folder inside the topic acceptable, given that it relaxes the no-dates rule for one
   named file?
3. The entry ceiling per folder: 40, 60 or 100?
4. Which repository is the pilot? It should be small, have real design documents and not be
   `sushiengine`; the choice decides whether the tool is proved generic.

## Phases

| Id | Phase | State |
| --- | --- | --- |
| D0 | Research and options, this document. | built |
| D1 | The owner chooses an option and answers the open questions. | planned |
| D2 | Rules and tools in SushiSkills: metadata fields, entry ceiling, generator and resolver, with tests. | planned |
| D3 | Pilot on a small repository: add the metadata, generate the views, fold the records. | planned |
| D4 | The remaining repositories follow, smallest first, `sushiengine` last. | planned |
