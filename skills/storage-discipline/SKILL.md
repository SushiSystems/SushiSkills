---
name: storage-discipline
description: Use when about to write files outside the repository's source tree, in a scratchpad or temp directory, to capture command output, copy or back up files, compile a scratch binary, install a package, download data, or before reporting a session finished, in a repository.
---

# Storage discipline

Every byte a session writes is a byte it owes back. Why, red flags: `references/detail.md`.

## No worktrees, no second build trees

- Never open a git worktree, for yourself or a subagent (`isolation: "worktree"` included).
- Never configure a build tree beside the owner's; a baseline or bisect runs in the existing
  tree, or ask.
- Ask first, every time, with size and purpose, before copying, moving into place or extracting
  anything over 1 GB, temporary or not.

## Scratch

- Scratch goes in the harness's scratchpad only: never `/tmp`, `%TEMP%` root, the home directory
  or the repository root. Files are small text.
- A scratchpad stays under 100 MB; a file over 10 MB needs a one-sentence reason.
- Never in scratch: build output (objects, executables, libraries, trees, precompiled headers,
  coverage); copies of the repository, a module, a dependency or a build directory; virtual
  environments, models, datasets, archives, installers; backups of git-held files.
- Build through the CLI into the owner's build directory. A binary only to test an idea is not
  built: read the code, or ask.

## Capturing output

- Bound every capture at the source (`| tail -n 200`, `| head -n 200`, `| grep`); never redirect
  a whole build or test log to a file.
- Bound a background command the same; start none with unpredictable output.
- One file per purpose, overwritten: no `notes_v2.txt`.

## Before anything large

Ask before any action that writes over 1 GB or leaves over 200 MB (download, model,
dataset, full copy, global install), stating size and purpose. Install no package for one
command; use existing environments; add no cache, virtual or conda one unasked.

## Cleaning up

- Delete what you created once done with it; never what you did not.
- Before reporting finished, measure the scratchpad (`du -sh`, or the sum of
  `Get-ChildItem -Recurse -File` lengths) and state it. Over budget: empty it, say what went.
- List old session folders and caches found on disk, with sizes; deleting them waits.

## Delegation

A subagent inherits nothing: `claude/DISPATCH.md` rule 7 sends it here, and `claude/CLAUDE.md`
"Delegation" returns a report without the scratchpad size.
