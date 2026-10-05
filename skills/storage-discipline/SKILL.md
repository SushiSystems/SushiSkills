---
name: storage-discipline
description: Use when about to write files outside the repository's source tree, in a scratchpad or temp directory, to capture command output, copy or back up files, compile a scratch binary, install a package, download data, or before reporting a session finished, in a Sushi Systems repository.
---

# Storage discipline

Disk is not free. An agent session that leaves tens of gigabytes behind costs the owner real
money on every SSD. Every byte a session writes is a byte it owes back, and the rule is the same
as for cycles: engineer it once carefully, run it a thousand times cheaply.

## Where scratch lives

- Scratch goes in the scratchpad directory the harness names, and nowhere else. Never `/tmp`,
  `%TEMP%` root, the home directory or the repository root.
- A scratch file is small text: a script, a diff, a trimmed log, a number. Nothing else.
- One session's scratchpad stays under 100 MB. A single file over 10 MB needs a reason you can
  state in one sentence.

## Never written to scratch

- Object files, executables, libraries, build trees, precompiled headers, coverage data.
- Copies of the repository, of a module, of a dependency, or of a build directory.
- Virtual environments, downloaded models, datasets, archives, installers.
- Backups of files git already holds. `git show <rev>:<path>` is the backup.

A build goes through the project's own CLI into the project's own build directory, which the
owner manages. A binary that exists only to test one idea is not built; read the code, or ask
the owner to run the build.

## Capturing output

- Bound every capture at the source: `| tail -n 200`, `| head -n 200`, `| grep <pattern>`.
- Never redirect a whole build or test log to a file. Keep the failing lines.
- A background command writes its output to the scratchpad too. Bound it the same way, and do
  not start one whose output you cannot predict.
- Overwrite one file per purpose. `notes.txt` is edited; `notes_v2.txt` and `notes_final.txt`
  are not created.

## Before anything large

Stop and ask the owner before an action that will write more than 1 GB or leave more than 200 MB
behind: a download, a model, a dataset, a full copy, a package install into a global location.
State the size you expect and what it is for.

Do not install packages to run one command once. Use the environments that already exist, and
never add a new package cache, virtual environment or conda environment without asking.

## Cleaning up

- Delete what you created when its purpose is over, not at the end of the session. Delete only
  what you created; another session's folder is not yours.
- Before reporting a task finished, measure the scratchpad and state the result in the report:
  `du -sh <scratchpad>` (Bash) or the sum of `Get-ChildItem -Recurse -File` lengths
  (PowerShell).
- If the scratchpad is over budget, empty it before reporting, then say what was removed.
- Old session folders and caches you find already on disk are listed to the owner with their
  sizes. Mass deletion of them waits for the owner's word.

## Delegation

A subagent does not inherit this rule. Line 7 of the dispatch block carries it, and the
evidence rule beside the block sends back a report without the scratchpad size. The block is in
`claude/CLAUDE.md`, section "Delegation".

## Red flags

- "I'll compile it here just to check." → read the code, or hand it to the owner.
- "I'll keep the full log in case I need it." → keep the failing lines.
- "A copy is safer than editing in place." → git is the safety.
- "The temp folder gets cleaned eventually." → it does not; Windows never empties it.
- "It is only a few hundred megabytes." → five sessions make a hundred gigabytes.
