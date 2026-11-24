# Storage discipline: why, and the excuses

Read this when a rule in `../SKILL.md` looks too strict for the case at hand, or when an excuse from the list below comes to mind. `../SKILL.md` holds the rules.

## Why

Disk space costs money. SSDs and RAM are expensive, and an agent session that leaves tens of
gigabytes behind costs the owner real money. The rule is the same as for processor time: design it
once, carefully, so that each of the thousand later runs is cheap.

## Excuses

- "I'll compile it here just to check." → read the code, or hand it to the owner.
- "I'll keep the full log in case I need it." → keep the failing lines.
- "A copy is safer than editing in place." → git keeps the previous version.
- "The temp folder gets cleaned eventually." → it does not; Windows never empties it.
- "It is only a few hundred megabytes." → five sessions make a hundred gigabytes.
- "A worktree keeps the main tree clean." → no worktree; work in the tree there is.
- "I need a baseline build to compare." → ask the owner; never a second tree.
- "I'll redirect the whole test log to a file and grep it later." → pipe the command through `grep` or `tail`; the log is never written.
- "The installer is needed once." → ask the owner; a download of any size waits, and an installer is never kept in scratch.
- "A notes file helps the next session." → write the finding in the report or with `backlog add`; no notes file.
- "Python caches make reruns faster." → run Python with `PYTHONDONTWRITEBYTECODE=1` and pytest with `-p no:cacheprovider`; no cache stays in a tree.
- "The scratchpad is the harness's, so it cleans itself." → it does not; empty it before reporting finished.

## Notes

- `git show <rev>:<path>` prints the previous version of a file git already holds.
- Scratch holds a script, a diff, a trimmed log, a number.
- Measure the scratchpad with `du -sh`, or on Windows with the sum of the `Get-ChildItem -Recurse -File` lengths.
- The harness sets `PYTHONDONTWRITEBYTECODE=1` and `PYTEST_ADDOPTS=-p no:cacheprovider` in `env` of `~/.claude/settings.json` (`claude/README.md`); the rule in `../SKILL.md` applies wherever the harness does not set them.
