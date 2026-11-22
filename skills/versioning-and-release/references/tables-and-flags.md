# Versioning and release: version source, commands and red flags

Read this to find the file that holds the version, to cut or report a release, or when a red flag
applies. The rules themselves are in `../SKILL.md`.

## Where the version lives

| Stack | Source |
| --- | --- |
| C++ | `project(<Name> VERSION x.y.z)` in the root `CMakeLists.txt`; `version.hpp` is generated from it |
| Python | `version` in `pyproject.toml` |
| TypeScript | `version` in the root `package.json` |
| No build manifest (a skills or documentation repository) | The latest `## vX.Y.Z` heading in `docs/reference/CHANGELOG.md` |

## Cutting a release: commands

The tag is annotated:

```
git tag -a vX.Y.Z -m "vX.Y.Z"
```

## Report form

`Next release: v0.3.3 (patch), 4 entries since v0.3.2.`

## Red flags

- "It is only a small feature, so a patch bump is fine." → the bump rules decide, not the size.
- "I will retag the release to include this fix." → a new PATCH.
- "The version in `package.json` and the tag can differ for now." → one source of truth.
- "The owner will notice it is time to release." → tracking is the agent's job.
- "The checkers pass, so the manual is ready." → a checker reads names and paths; a reviewer
  reads the sentences.

## Why the manual is read before a release

`check_docs_truth.py` catches a stale name or path; only a reader catches a sentence that
describes behaviour the code has lost.
