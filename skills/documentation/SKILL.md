---
name: documentation
description: Use when creating, editing, moving or archiving any file under docs/ or a module README in a Sushi Systems repository, when adding, renaming or removing a public name, a signature, a header path, a CLI command or a behaviour a page may describe, when recording a spec, plan, report, design decision, backlog item or changelog entry, or when unsure where a written fact belongs.
---

# Documentation

Documentation is split by what it records, and each kind has exactly one home. A fact in two
places is a fact that will disagree with itself. The failure this skill prevents is the soup:
many agents, each writing correct files in slightly different places, until nobody can find
the current truth.

## The tree

```
docs/
    README.md                     manual index; reaches every document outside agent/ and archive/
    CONTRIBUTING.md               what must be documented, how a change lands
    DOCUMENTATION_STYLE_GUIDE.md
    publish.toml                  what the repository publishes to docs.sushisystems.io
    .docs_truth_allow             names the manual may write that the source cannot hold
    getting_started/  architecture/  guides/
    reference/
        CHANGELOG.md  GLOSSARY.md  KNOWN_ISSUES.md
    design/
        README.md                 topic -> design document map
        REMAINING_WORK.md         the single backlog
        <TOPIC>/README.md         live intent of one topic, with a status line; pages beside it
        _REVISION/<TOPIC>/        a topic the owner set aside for revision; see DESIGN_FORMAT.md
    agent/
        <YYYY_MM_DD>_<WORK_NAME>/ one folder per piece of agent work
            SPEC.md  PLAN.md  REPORT.md
    archive/                      frozen, only in a repository that has not retired it; see AGENT_WORK.md
<module>/README.md                the module's own facts, beside the code
<folder>/<file>.md                one file's facts, beside it, when its README would pass the ceiling
```

No other folder under `docs/`. No other file names inside a work folder.

Required in every repository: `README.md`, `CONTRIBUTING.md`, `DOCUMENTATION_STYLE_GUIDE.md`,
the three files under `reference/` and the two under `design/`. The other folders appear when
they have content.

## Placement

Ask in order, stop at the first yes.

1. Is it a fact about one module? → that module's `README.md`.
2. Was it written by an agent while doing a piece of work? → that work's folder in `docs/agent/`.
3. Is it intent with an open phase? → `docs/design/<TOPIC>/README.md`.
4. Is it about work that is finished? → nowhere: it is deleted when its decisions are in the topic;
   version history keeps it.
5. Otherwise → the manual: `getting_started/`, `architecture/`, `guides/` or `reference/`.

## The root README

The root `README.md` is the front page: each line answers a question a cold reader has, and
everything else is a link into `docs/`. Its sections, in this order, none of them empty:

1. `# <Project>`, then one sentence: what it is and who it is for. Two CI or licence badges at
   most, on the line under the title.
2. The smallest real use: for a library, code under the example rule of "Size and one home";
   for a tool, the commands a user types.
3. `## Build`: the commands that build and test it, one block.
4. `## Status`: what works and what does not yet, in a few lines, linking
   `docs/design/REMAINING_WORK.md`.
5. `## Documentation`: a link to `docs/README.md`; `docs/CONTRIBUTING.md` for contributors.
6. `## Licence`: the licence by name, `LICENSE`, and `COMMERCIAL.md` and `NOTICE.md` where they
   exist.

A repository with no code to show, such as SushiSkills, replaces section 2 with a table of
where things are. Not on the page: a table of contents, emoji headings, a feature bullet list,
adjectives such as fast, powerful or seamless, and anything the manual already says.

`CONTRIBUTING.md` is `docs/CONTRIBUTING.md`; GitHub finds it there. `SECURITY.md` and
`CODE_OF_CONDUCT.md` sit under `.github/`, as `repository-layout` says.

## Read before

| Task | File in this folder |
| --- | --- |
| Opening or extending a design document, opening or closing a work folder under `docs/agent/` | `AGENT_WORK.md` |
| Writing or reshaping a design document: its sections, status line and phase table | `DESIGN_FORMAT.md` |
| Writing a changelog entry or moving a release section | `CHANGELOG_FORMAT.md` |
| Writing or closing an entry in `REMAINING_WORK.md` or `KNOWN_ISSUES.md` | `BACKLOG_FORMAT.md` |

## Names

- Files: `UPPER_SNAKE_CASE.md`. Work folders: `YYYY_MM_DD_UPPER_SNAKE_CASE`.
- Every link and cited path resolves. Example paths are in code spans, never live links.

## Keeping the manual true

A manual page that stops being true is a defect in the change that made it false. The code,
its module README, the manual pages that describe it, its design status and its changelog line
land in one commit.

The manual is the root `README.md`, every document under `docs/` outside `agent/`, `archive/`
and the changelog, and every `.md` page under the source folders: each `README.md`, and each page
named after the file it describes (`test_tensor.md` beside `test_tensor.cpp`), which its folder's
README links.

- A change that adds, renames or removes a public name, a signature, a header path, a CLI
  command or a behaviour a page describes searches the manual for the old name,
  `git grep -n <old name> -- '*.md'`, and corrects every hit in that commit.
- Architecture and guide pages are part of every change. They are never a stage at the end of a
  plan.
- `tools/documentation/check_docs_truth.py` enforces what a tool can: every name and path a page
  writes in code exists in the source, and every example comes from a file. A sentence that
  describes behaviour the code has lost is caught only by a reader. A design document states
  intent, so its names are not looked up.
- A name the source cannot hold, such as a third-party type or a target the build generates,
  goes in `docs/.docs_truth_allow`: one regular expression per line, ` # reason` after it. An
  entry without a reason, or one that excuses nothing, is a finding.

### Editing is replacing

- The old paragraph is deleted, never kept beside the new one. Git keeps it.
- A page says what is. It does not say `previously`, `no longer`, `used to`, `was renamed`,
  `formerly`, `as of v`, `new in v`, `up to v` or `deprecated since`. What changed is in the
  changelog; a defect that still bites is in `KNOWN_ISSUES.md`.
- When a section's subject is gone, the section goes, heading included.

### Size and one home

| Page | Ceiling | Above it |
| --- | --- | --- |
| Root `README.md` | 120 lines | Move the detail into the manual and link it |
| Manual page | 600 lines | Split by subject into pages the index links |
| Module README | 800 lines | Move each part to the README of the folder it describes, or to a page beside the file it describes |
| Design document | 400 lines | Pages beside its `README.md`, one per phase |

- One fact, one home. A paragraph of 300 characters or more that a second page repeats becomes
  one sentence and a link there.
- A page is written for the reader who arrives cold: what the thing is, how to use it, then the
  detail.
- A source example in a manual page is taken from a file the build compiles, and a line within
  three lines after it cites that file: ``Source: `applications/examples/quickstart.cpp` ``.
  Every line of the example is a line of that file; `// ...` marks an omission.
- An example no file can back carries `Source: not compiled`. `--report` counts those; drive the
  count down.
- No em dash in the prose of a page; `humanizer` gives the repair. The changelog entry and the
  design status line keep theirs.

## Red flags

- "I will write a quick note in a new file so the next agent sees it." → the work folder.
- "This review deserves its own file." → replace `REPORT.md`.
- "This topic is slightly different from the existing design document." → extend it.
- "I will update the changelog at the end of the week." → it is part of the commit.
- "`docs/` is outside my write list, so I reported it." → `AGENT_WORK.md`, on a reported page.
- "The manual is a later stage of the plan." → the page is part of the change that made it false.
- "The module README is updated, that is enough." → `git grep` the name over `README.md` and
  `docs/`; every hit belongs to this change.
- "I will add a note that this changed." → replace the text; the changelog holds the change.
- "I will keep the old paragraph in case." → delete it; git keeps it.
- "The page is long because the subject is large." → a subject that large is more than one page.
