---
name: versioning-and-release
description: Use when changing a version number, tagging, cutting or proposing a release, when the Unreleased changelog section has grown, when a change breaks a public interface, or when asked whether a repository is ready to release, in a repository.
---

# Versioning and Release

Semantic Versioning 2.0.0, tags `vMAJOR.MINOR.PATCH`. The agent always knows the next version;
the owner approves every tag and push. Source table, commands, excuses:
`references/tables-and-excuses.md`.

## One source of truth

One place holds the version; other copies are generated or checked against it. Which file, per
stack: the reference. The tag is `v` plus that number.

## Choosing the next version

Take the highest bump that `## Unreleased` or a commit since the last tag requires.

- Breaking change to a public interface, file format or CLI: MAJOR; before `v1.0.0`, MINOR.
- `feat`: MINOR; before `v1.0.0`, PATCH. `fix` or `perf`: PATCH.
- Only `refactor`, `test`, `docs`, `build`, `chore`: no release.
- A breaking commit and its entry follow `commits`.
- `v1.0.0` is the owner's decision, never reached by counting bumps.
- Pre-releases take a suffix (`v0.4.0-rc.1`); no build metadata.

## Tracking

1. After each commit adding a changelog entry, compute the next version; for a breaking entry
   fix every manual hit for a changed name in that commit (`documentation`).
2. When closing work, report the next version, its bump and the entry count (form in the reference).
3. Propose a release when an `Unreleased` entry is breaking; a design phase shipped; a `fix`
   corrects behaviour users of the last release can hit; `Unreleased` holds 15 or more; or 30
   days passed since the last tag with a `feat` or `fix`. The proposal names the version,
   the bump reason and the entries behind it, then waits.

## Cutting a release

After the owner approves, in order: run every checker under `tools/` and the full test suite
through the project CLI; have a reviewer who did not write the manual check it against the code
(a failure or a false sentence stops the release); set the version in its source; close
`## Unreleased` per `CHANGELOG_FORMAT.md` (`documentation`); update every design status and
manual page naming the version; commit only those files as `chore(release): vX.Y.Z`; tag it;
report commit and tag; push only when the owner says so.

A defect in a released version is fixed on `main` and released as the next PATCH. Tags
are never moved or deleted.
