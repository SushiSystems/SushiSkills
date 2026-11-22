# Versioning and release: tables and red flags

Read this when the original table form of the version sources or the bump rules is needed, or
when a red flag applies. The rules themselves are in `../SKILL.md`.

## One source of truth

| Stack | Source |
| --- | --- |
| C++ | `project(<Name> VERSION x.y.z)` in the root `CMakeLists.txt`; `version.hpp` is generated from it |
| Python | `version` in `pyproject.toml` |
| TypeScript | `version` in the root `package.json` |
| No build manifest (a skills or documentation repository) | The latest `## vX.Y.Z` heading in `docs/reference/CHANGELOG.md` |

## Choosing the next version

| Change since the last tag | From `v1.0.0` on | Before `v1.0.0` |
| --- | --- | --- |
| A breaking change to a public interface, file format or CLI | MAJOR | MINOR |
| New behaviour, backwards compatible (`feat`) | MINOR | PATCH |
| Wrong behaviour made right (`fix`), or `perf` | PATCH | PATCH |
| Only `refactor`, `test`, `docs`, `build`, `chore` | no release | no release |

## Red flags

- "It is only a small feature, so a patch bump is fine." → the table decides, not the size.
- "I will retag the release to include this fix." → a new PATCH.
- "The version in `package.json` and the tag can differ for now." → one source of truth.
- "The owner will notice it is time to release." → tracking is the agent's job.
- "The checkers pass, so the manual is ready." → a checker reads names and paths; a reviewer
  reads the sentences.

## Why the manual is read before a release

`check_docs_truth.py` catches a stale name or path; only a reader catches a sentence that
describes behaviour the code has lost.
