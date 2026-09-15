---
name: versioning-and-release
description: Use when changing a version number, tagging, cutting or proposing a release, when the Unreleased changelog section has grown, when a change breaks a public interface, or when asked whether a repository is ready to release, in a Sushi Systems repository.
---

# Versioning and Release

Every repository follows Semantic Versioning 2.0.0 and names releases `vMAJOR.MINOR.PATCH`,
for example `v0.3.2`. The agent keeps track of what the next version is at all times and says
so when a release is due; the owner approves every tag and every push.

## One source of truth

The version lives in one place per repository and every other copy is generated or checked
against it.

| Stack | Source |
| --- | --- |
| C++ | `project(<Name> VERSION x.y.z)` in the root `CMakeLists.txt`; `version.hpp` is generated from it |
| Python | `version` in `pyproject.toml` |
| TypeScript | `version` in the root `package.json` |

The tag is `v` plus that number. The changelog heading is the tag.

## Choosing the next version

Read the entries under `## Unreleased` and the commit subjects since the last tag, then take the
highest bump any of them demands.

| Change since the last tag | From `v1.0.0` on | Before `v1.0.0` |
| --- | --- | --- |
| A breaking change to a public interface, file format or CLI | MAJOR | MINOR |
| New behaviour, backwards compatible (`feat`) | MINOR | PATCH |
| Wrong behaviour made right (`fix`), or `perf` | PATCH | PATCH |
| Only `refactor`, `test`, `docs`, `build`, `chore` | no release | no release |

- A breaking commit is marked in its subject, `feat(scope)!: ...`, and its changelog entry says
  what breaks (see `commits`).
- `v1.0.0` is the owner's decision alone. It is never reached by counting bumps.
- Pre-releases carry a suffix: `v0.4.0-rc.1`. Build metadata is not used.

## Tracking

The agent keeps the release state current without being asked.

1. After every commit that adds a changelog entry, compute the next version from the table
   above.
2. When closing a piece of work, report one line: `Next release: v0.3.3 (patch), 4 entries
   since v0.3.2.`
3. Propose a release when any of these holds:
   - an entry under `Unreleased` is a breaking change;
   - a design document's phase moved to shipped;
   - a `fix` corrects behaviour a user of the last release can hit;
   - `Unreleased` holds 15 or more entries, or 30 days have passed since the last tag with at
     least one `feat` or `fix`.
4. A proposal names the version, the bump reason and the entries that drive it, and waits for
   the owner.

## Cutting a release

Once the owner approves, in this order:

1. Run every checker under `tools/` and the full test suite through the project CLI. A finding
   or a failure stops the release.
2. Set the version in the source of truth.
3. In the changelog, rename `## Unreleased` to `## vX.Y.Z — YYYY-MM-DD`, open a new empty
   `## Unreleased` above it, and move every older release section to
   `docs/archive/changelog/vA.B.C.md`.
4. Update every design status and manual page that names the version.
5. Commit only those files: `chore(release): vX.Y.Z`.
6. Tag that commit with an annotated tag: `git tag -a vX.Y.Z -m "vX.Y.Z"`.
7. Report the commit and the tag. Push only when the owner says so.

## After a release

- `Unreleased` is empty and the next version is back to "no release".
- A defect found in a released version is fixed on the main line and released as the next PATCH.
  Tags are never moved or deleted.

## Red flags

- "It is only a small feature, so a patch bump is fine." → the table decides, not the size.
- "I will retag the release to include this fix." → a new PATCH.
- "The version in `package.json` and the tag can differ for now." → one source of truth.
- "The owner will notice it is time to release." → tracking is the agent's job.
