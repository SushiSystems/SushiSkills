---
name: versioning-and-release
description: Use when changing a version number, tagging, cutting or proposing a release, when the Unreleased changelog section has grown, when a change breaks a public interface, or when asked whether a repository is ready to release, in a repository.
---

# Versioning and Release

Semantic Versioning 2.0.0, releases named `vMAJOR.MINOR.PATCH`. The agent always knows the next
version and says so when a release is due; the owner approves every tag and push. Read
`references/tables-and-flags.md` for the source and bump tables and the red flags.

## One source of truth

The version lives in one place; every other copy is generated or checked against it. C++:
`project(<Name> VERSION x.y.z)` in the root `CMakeLists.txt`. Python: `pyproject.toml`.
TypeScript: root `package.json`. No manifest: the latest `## vX.Y.Z` heading in
`docs/reference/CHANGELOG.md`. The tag is `v` plus that number, and the changelog heading is the tag.

## Choosing the next version

Read `## Unreleased` and the commit subjects since the last tag; take the highest bump any demands.

- Breaking change to a public interface, file format or CLI: MAJOR; before `v1.0.0`, MINOR.
- `feat`: MINOR; before `v1.0.0`, PATCH.
- `fix` or `perf`: PATCH.
- Only `refactor`, `test`, `docs`, `build`, `chore`: no release.
- A breaking commit is marked `feat(scope)!: ...`; its entry says what breaks (`commits`).
- `v1.0.0` is the owner's decision alone, never reached by counting bumps.
- Pre-releases take a suffix, `v0.4.0-rc.1`. No build metadata.

## Tracking

1. After each commit that adds a changelog entry, compute the next version. For a breaking
   entry, search the manual for every changed name and fix the hits in that commit
   (`documentation`).
2. When closing work, report: `Next release: v0.3.3 (patch), 4 entries since v0.3.2.`
3. Propose a release when an `Unreleased` entry is breaking; a design phase moved to shipped; a
   `fix` corrects behaviour a user of the last release can hit; `Unreleased` holds 15 or more
   entries; or 30 days passed since the last tag with a `feat` or `fix`.
4. A proposal names the version, the bump reason and the driving entries, then waits.

## Cutting a release

After the owner approves, in order:

1. Run every checker under `tools/` and the full test suite through the project CLI; a finding or
   failure stops the release. Then a reviewer who did not write the manual reads it start to
   finish against the code; a false sentence stops the release.
2. Set the version in the source of truth.
3. Close `## Unreleased` as `CHANGELOG_FORMAT.md` in `documentation` says.
4. Update every design status and manual page naming the version.
5. Commit only those files: `chore(release): vX.Y.Z`.
6. Tag it: `git tag -a vX.Y.Z -m "vX.Y.Z"`.
7. Report commit and tag. Push only when the owner says so.

## After a release

`Unreleased` is empty. A defect in a released version is fixed on the main line and released as
the next PATCH. Tags are never moved or deleted.
