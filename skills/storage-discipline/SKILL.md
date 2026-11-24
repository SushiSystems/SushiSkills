---
name: storage-discipline
description: Use when about to write files outside the repository's source tree, in a scratchpad or temp directory, to capture command output, copy or back up files, compile a scratch binary, install a package, download data, or before reporting a session finished, in a repository.
---

# Storage discipline

A session deletes every scratch file it created before it ends. Why: `references/detail.md`.

## No worktrees, no second build trees

- Never open a git worktree, for yourself or a subagent (`isolation: "worktree"` included).
- Never configure a build tree beside the owner's; a baseline or bisect runs in the existing tree, or ask.

## Scratch

- Scratch goes in the harness's scratchpad only, never `/tmp`, `%TEMP%` root, the home directory
  or the repository root.
- A scratchpad stays under 20 MB; no file is over 1 MB.
- Never in scratch: build output; copies of the repository, a module, a dependency or a build
  directory; virtual environments, models, datasets, archives, installers, downloads; backups of
  git-held files.
- Build through the CLI into the owner's build directory. A binary only to test an idea is not
  built: read the code, or ask.

## Capturing output

- Bound every capture at the source (`| tail -n 200`, `| head -n 200`, `| grep`); never redirect
  a whole build or test log to a file. No capture exceeds 1 MB.
- Bound a background command the same; start none with unpredictable output.

## Files the task does not name

- Create no note, plan, summary, report, backup or `_v2` copy; one file per purpose, overwritten.
  Findings go in the report, the backlog or a `docs/agent/` folder.
- Run Python with `PYTHONDONTWRITEBYTECODE=1` and pytest with `-p no:cacheprovider`; leave no
  `__pycache__`, `.pytest_cache` or other tool cache in a tree.

## Before anything large

A download of any size waits for the owner. Ask first, with size and purpose, before anything that
writes over 1 GB, leaves over 200 MB (model, dataset, full copy, global install) or copies, moves
or extracts over 1 GB, temporary or not. Install no package for one command; use existing
environments; add no cache, virtual or conda environment unasked.

## Cleaning up

- Delete what you created once done with it; never what you did not.
- Before reporting finished, delete every file you created in scratch, measure the scratchpad
  and state its size.
- List old session folders and caches found on disk, with sizes; deleting them waits.
