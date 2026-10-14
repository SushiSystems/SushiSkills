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
        <TOPIC>.md                live intent, each with a status line
    agent/
        <YYYY_MM_DD>_<WORK_NAME>/ one folder per piece of agent work
            SPEC.md  PLAN.md  REPORT.md
    archive/                      frozen; a folder is moved in whole, then never edited
<module>/README.md                the module's own facts, beside the code
```

No other folder under `docs/`. No other file names inside a work folder.

Required in every repository: `README.md`, `CONTRIBUTING.md`, `DOCUMENTATION_STYLE_GUIDE.md`,
the three files under `reference/` and the two under `design/`. The other folders appear when
they have content.

## Placement

Ask in order, stop at the first yes.

1. Is it a fact about one module? → that module's `README.md`.
2. Was it written by an agent while doing a piece of work? → that work's folder in `docs/agent/`.
3. Is it intent with an open phase? → `docs/design/<TOPIC>.md`.
4. Is it about work that is finished and untouched for 90 days? → `docs/archive/`.
5. Otherwise → the manual: `getting_started/`, `architecture/`, `guides/` or `reference/`.

## Read before

| Task | File in this folder |
| --- | --- |
| Opening or extending a design document, opening or closing a work folder under `docs/agent/` | `AGENT_WORK.md` |
| Writing a changelog entry or moving a release section | `CHANGELOG_FORMAT.md` |

## Names

- Files: `UPPER_SNAKE_CASE.md`. Work folders: `YYYY_MM_DD_UPPER_SNAKE_CASE`.
- Every link and cited path resolves. Example paths are in code spans, never live links.

## Keeping the manual true

A manual page that stops being true is a defect in the change that made it false. The code,
its module README, the manual pages that describe it, its design status and its changelog line
land in one commit.

The manual is the root `README.md`, every document under `docs/` outside `agent/`, `archive/`
and the changelog, and every `README.md` under the source folders.

- A change that adds, renames or removes a public name, a signature, a header path, a CLI
  command or a behaviour a page describes searches the manual for the old name,
  `git grep -n <old name> -- README.md docs '*README.md'`, and corrects every hit in that commit.
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
| Root `README.md` | 300 lines | Move the detail into the manual and link it |
| Manual page | 600 lines | Split by subject into pages the index links |
| Module README | 800 lines | Move each part to the README of the folder it describes |
| Design document | 1 500 lines | Split into `<TOPIC>/`, one file per phase |

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
