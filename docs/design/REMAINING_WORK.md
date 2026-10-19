# Remaining work

Next id: RW-19

## Decisions waiting for the owner

### RW-1 Decide whether the archive clock gates a push
- State: decision
- Done when: the owner has kept `rule_archive_candidates` in the gate of `ci.yml`, or moved it
  to `--report`

The rule reads the date in a work folder's status line. From 2027-01-04 a push fails on the
oldest work folder until it is archived.

### RW-2 Decide whether contributions from outside are accepted
- State: decision
- Done when: the owner has named a contributor agreement, or ruled contributions out

### RW-3 Decide where C++ tests live
- State: decision
- Done when: the owner has kept the `tests/` mirror, or moved C++ tests into their module at
  `modules/<tier>/<module>/tests/`

Under study since 2026-10-16. The owner wants the mirror used longer first, so every case is
known. Cases so far: a test that spans several modules, a second target inside a module folder,
a shader twin, a test that reaches a private header.

### RW-4 Decide whether the release tags are pushed
- State: decision
- Done when: `v0.1.0` and `v0.1.1` are on the remote, or the owner has ruled them local

## Checkers

### RW-5 Check that every symbol carries a `@brief`
- State: open
- Done when: `check_source_comments.py` reports a C++ symbol without `@brief`

The file block is checked today; a symbol needs a C++ parser.

### RW-6 Read Python imports across modules in the layering check
- State: open
- Done when: `check_layering.py` reports a Python import that crosses a module boundary the
  layering forbids

### RW-7 Check that a changelog entry's verb is past tense
- State: open
- Done when: `check_changelog.py` reports an entry whose verb is not in the past tense

### RW-8 Check that changelog entries run newest first
- State: open
- Done when: `check_changelog.py` reports an entry dated after the one above it

### RW-9 Resolve links outside `docs/`
- State: open
- Done when: `rule_links` checks the root README, module READMEs and paths cited in backticks

### RW-10 Check module READMEs in every layout
- State: open
- Done when: `rule_module_readmes` checks a single-module repository and a skills repository

It covers `modules/<tier>/<module>/` only.

### RW-11 Check the licence block of shell and CMake files
- State: open
- Done when: `rule_license_block` reads `.sh` and `.cmake` files

These files get the `#` block from `write_license_block.py` and are proven by its `--report`.

### RW-12 Tell a second personal copyright line from an upstream notice
- State: open
- Done when: `rule_license_block` reports a second copyright line that is not an upstream notice

It rejects only lines that name Sushi Systems or state a licence.

### RW-13 Read reference-style links and links around an image
- State: open
- Done when: `rule_links` and `rule_reachable_from_index` follow both kinds

### RW-16 Copy the shared rows of `tools/README.md` with the shared tools
- State: open
- Done when: `copy_shared_tools.py` writes the rows of the shared tools into a repository's
  `tools/README.md` and keeps the rows of its own tools

Each repository keeps its `tools/README.md`, so the rows naming the shared tools are copied by
hand and fall behind: the first migration found one still naming nine checkers.

### RW-17 Report a setting the shared tools read that `settings.py` lacks
- State: open
- Done when: `copy_shared_tools.py` names each `K_` setting the copied tools import that the
  repository's `tools/settings.py` does not define, with SushiSkills' default

The copy keeps `settings.py`, so a new setting breaks the checker that reads it: the second
migration found `check_layering.py` failing on `K_PRIVATE_DEPENDS_ALSO`.

### RW-18 Refuse a changelog without its title and `## Unreleased`
- State: open
- Done when: `check_changelog.py` reports a `CHANGELOG.md` that lacks `# Changelog` or
  `## Unreleased`

Two commits in one repository wrote the changelog as their own entry alone and 413 lines were
lost; the checker passed, since it reads entries and the one entry left was well formed.

## Estate

### RW-14 Migrate every estate repository to the backlog format
- State: open
- Done when: `check_all.py`, with `check_backlog.py` in it, passes in every estate repository
- Source: `docs/agent/2026_10_19_BACKLOG_FORMAT/PLAN.md` §2

Part 2 of the plan gives the order and the steps. The work lands in the other repositories, so
this entry moves with RW-15 to the repository that coordinates them.

### RW-15 Hand the estate programmes to the repository that coordinates them
- State: open
- Done when: the coordinating repository's backlog holds the programmes and this entry is deleted
- Source: `docs/agent/2026_10_05_ESTATE_AUDIT/REPORT.md`

The estate audit of 2026-10-05 opened five programmes: rules unification, which is this
repository's and has shipped, then licence, command line, documentation and layout, and code,
which run in the other repositories and take their rules from here.
