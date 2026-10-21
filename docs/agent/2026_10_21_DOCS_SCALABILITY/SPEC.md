# Documentation that scales

**Status:** Open — decisions taken on 2026-10-21; tools built; sushidsp pilot done; the other repositories follow

## Problem

The module tree and the test tree scale: a new module adds a folder in a fixed place, and a checker
says when a test has no home. `docs/` does not. Measured on `sushiengine` on 2026-10-21, four months
after its first commit.

| Measure | Value |
| --- | --- |
| Design topics | 71 in one folder; 8 of them are `MATTER_*`, 4 `CLOUD_*`, 3 `PHYSICS_*` |
| Work folders in `docs/agent` | 83 in one folder; 63 opened on one day, one per reshaped design |
| Citations of a design by path | 1 963 over 183 paths; one reshape repaired more than 600 |
| Modules a design topic cites | 1: 3 topics; 2 to 3: 14; 4 to 8: 22; 9 or more: 30 |
| Where designs would sit if placed by the code they govern | 50 of 71 at the repository root |
| Code | 30.9 MB, 650 000 lines |
| Markdown | 24.7 MB, 397 000 lines, 80% of the code by size |
| of which `docs/archive` and `docs/agent` | 14.2 MB, 57% of all Markdown |
| of which live documents | 10.5 MB, 34% of the code |
| Citations into `docs/archive` from outside it | 675 in 273 files, 128 of them source files |
| Gate of the repository's own `check_all` | red before this work: three checkers fail |

Six costs follow.

1. **One flat folder per kind**, and a topic map edited by hand, so parallel sessions collide on it.
2. **Paths are identities.** Moving a document costs a repair pass over the repository.
3. **One subject, many files.** Each new idea became a new design file, so the same noun is spread
   over eight documents, and one subject can be described twice under two names.
4. **History outweighs the living text.** More than half of the Markdown is closed work that nobody
   maintains, and every search and every checker reads it.
5. **Shared hot files.** The changelog, the backlog and the topic map are edited by every session.
6. **A red gate protects nothing.** A checker that fails on a clean tree is not read.

### What other projects do

- **Python.** A PEP whose work is done becomes `Final` and is marked as a historical document; the
  canonical text moves to the reference. [PEP 683](https://peps.python.org/pep-0683/) shows the banner.
- **Rust.** An accepted RFC is not changed in substance; a substantial change is a new RFC with a
  note on the old one. The community discussion asks for the reference to become the truth once a
  feature is stable. ([RFC README](https://rust-lang.github.io/rfcs/introduction.html),
  [Life after an RFC](https://internals.rust-lang.org/t/life-after-an-rfc/4126))
- **Documentation kinds.** [Diátaxis](https://canonical.com/blog/diataxis-a-new-foundation-for-canonical-documentation)
  keeps tutorials, how-to guides, reference and explanation apart.
- **Reference from code, owners and a review cadence** keep the living layer true.
  ([GitBook](https://www.gitbook.com/blog/keep-technical-documentation-accurate),
  [Heavybit](https://www.heavybit.com/library/article/who-owns-the-documentation-and-why-it-should-be-the-robots))
- **Plans and reports** usually live in the pull request or the issue, not in the product tree. This
  is experience, not checked by the search.
- **Kubernetes enhancement proposals** group by owning group and keep a metadata file; not confirmed.
- **Linux** reorganised a documentation top level its maintainer called a mess, and deleted its
  hand-kept index files.

The pattern: a design is a decision record that ends; the living truth is the reference and the
module page; indexes are generated; history lives in version control.

## Decision

The owner decided on 2026-10-21:

1. **The unit is the topic**, a name that is a module (`AUDIO`, `ECS`) or a subject that spans modules
   (`WEATHER`). Each topic has one home. A new idea about an existing topic is a page and a phase in
   it, never a new top-level document. A subject that two documents describe becomes one topic.
   Topic names are the entries of the glossary.
2. **Agent work keeps its date and its plan, and does not repeat.** A work folder holds only the
   difference and names the topic phase it carries out. When it closes, its decisions move into the
   topic and the folder is deleted; version control, the changelog line and the topic keep the rest.
3. **`docs/archive/` is untracked.** It is ignored by version control and its history stays in the
   repository under a tag.
4. **A design graduates.** When every phase of a topic is built, its decisions and their reasons stay
   as a short record, what the code now is moves to the module page and the manual, and the narrative
   of how it got there is deleted.
5. **Storage is flat and carries no taxonomy.** Every cut a reader wants is a generated view.
6. **Tools that write many files are safe.** They write through a temporary file, refuse to shrink a
   file past a set share, and take a copy first.
7. **The changelog is written as fragments** and joined at release.
8. **The gate is made green before a rule is added** to it.

Rejected, with the measurement: fixed folders by subject (fit one repository only), a mirror of the
module tree or a home at the common parent of the governed code (50 of 71 at the root), grouping by
the first word of the name (48 different first words for 71 names), subject tags, and the record kept
inside the topic.

## Design

**Topic folder.** `docs/design/<TOPIC>/README.md` holds the five sections of the design format, with
the phase table of the whole topic. The README is the index and the contract; each sub-design is a
page with its own status. Phase ids carry the sub-design as a prefix (`MATTER-DEVICE-D3`). The page
list in a README is generated, not typed.

**Metadata** under the status line, one field per line, checked:

- `**Modules:**` the module paths the topic governs; each must exist.
- Nothing else is required. A topic's phases are the contract, and work reaches them by id.

**Generated views.** One tool writes, from the metadata and the phase tables: the topic map of
`docs/design/README.md`, a page per module, a page per status, the `Designs` block between markers in
every module README, and for each topic a work list built from the folders whose `Implements:` names
one of its phases. CI checks that the generated text is current. A glossary entry for every topic is
checked.

**Resolver.** A citation names a topic and, when it needs one, a phase or a page. A tool resolves it
to the path and reports a citation it cannot place. A move is a generated rewrite.

**Agent work.** `SPEC.md` starts with `Implements: <TOPIC> <phase>` (or `Designs:` for work that
touches several, or nothing for an audit). At close the orchestrator writes the decisions into the
topic, sets the phase state, writes the changelog fragment, deletes the folder and updates the backlog.
A phase marked `built` may name its evidence, an existing test or command, which a checker verifies.

**Archive.** `docs/archive/` is in `.gitignore`. The closing step no longer moves a folder there; it
deletes it. The existing contents get a tag, `docs-archive-<date>`, and are removed from the index. A
live document or a source comment may not cite an archive path; each of the 675 existing citations is
repointed to the topic that holds the decision, or dropped, before the removal.

**Volume.** `check_all` reports the share of live documentation to code, as information and with no
limit. A module README states what the module is and how to use it and links the generated reference
for signatures. How much of the module Markdown restates signatures is measured before the rule is
written.

**Folder ceiling.** A checked limit of entries per folder in `docs/design` and `docs/agent`. Proposed:
60.

**Order.** The tools and the resolver come before any merge of topics, so that no citation is
repaired by hand.

## Phases

| Id | Phase | State |
| --- | --- | --- |
| D0 | Research and options, this document. | built |
| D1 | The owner decides the unit, the lifecycle and the archive. | built |
| D2 | The gate of the pilot repository is green. | built |
| D3 | The resolver, the generated views, `Implements:` and the glossary check, with tests, in SushiSkills. | built |
| D4 | The lifecycle rules and tools: delete at close, the archive retired and uncited, with tests, in SushiSkills. | built |
| D5 | Safe writing for the bulk tools, and changelog fragments. | planned |
| D6 | Pilot on `sushidsp`: metadata, views, topic merges, the archive citations repointed and the archive retired. | built |
| D7 | The other repositories follow, smallest first, `sushiengine` last. | planned |
| D8 | Phase evidence, the size ceiling that makes a shipped design graduate, the module README dedup rule and the volume report. | planned |

## Open questions

None. The owner delegated the rest on 2026-10-21 and the choices are these.

1. **Pilot: `sushidsp`.** 13 design documents, 57 archive files and 21 work folders on 713 source files:
   small enough to finish, large enough to merge topics and repoint archive citations for real. Its
   tree was clean and its gate green on 2026-10-21.
2. **Folder ceiling: 60** entries in `docs/design` and in `docs/agent`.
3. **Topic merges** are proposed by a table from shared name prefixes and shared modules and applied by
   the orchestrator; a merge keeps every section as a page.
4. **A decision held only by an archived folder is lost** and is not recovered; the version history
   keeps the text.
