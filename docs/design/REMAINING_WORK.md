# Remaining work

Next id: RW-26

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

### RW-19 Name the licence of the shared code of conduct text
- State: decision
- Done when: `NOTICE.md` names the licence of the Contributor Covenant text that
  `.github/CODE_OF_CONDUCT.md` adapts, or the owner replaces the text

Every repository copies the file from here. Four pages of the Covenant read on 2026-10-09 state
no licence for its text.

## Checkers

### RW-5 Check that every symbol carries a `@brief`
- State: open
- Done when: `check_source_comments.py` reports a C++ symbol without `@brief`

The file block is checked today; a symbol needs a C++ parser.

### RW-6 Read Python imports across modules in the layering check
- State: open
- Done when: `check_layering.py` reports a Python import that crosses a module boundary the
  layering forbids


### RW-21 Read TypeScript imports in the layering check
- State: open
- Done when: `check_layering.py` reports a TypeScript import that crosses a boundary the
  repository's tier order forbids

A TypeScript repository holds its package split in `architecture.test.ts` files today.


### RW-22 Read C# in the comment, licence and layering checks
- State: open
- Done when: `check_source_comments.py` and `write_license_block.py` read `.cs` files, and
  `check_layering.py` reads a Unity tree's assembly definitions

A Unity repository relies on its assembly definitions alone to stop a reference between
features.
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

### RW-20 Let the test mirror checker skip listed units
- State: open
- Done when: `check_test_mirror.py` skips the units a repository lists in `tools/settings.py` and
  fails on a listed unit that has gained a test

One repository keeps this as a local edit of the shared checker, with the list in a text file;
the copy would drop it.

## Documentation

### RW-25 Make the documentation tree scale
- State: open
- Done when: a pilot repository other than `sushiengine` keeps its designs as topics with generated
  views, closes agent work by deleting it, and has an untracked archive, with its `check_all` green
- Source: `docs/agent/2026_10_21_DOCS_SCALABILITY/SPEC.md`

The archive rule of RW-1 goes away with the untracked archive, so RW-1 is decided by this entry's
phase D4 and not before.
