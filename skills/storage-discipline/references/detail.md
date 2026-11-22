# Storage discipline: why, and the red flags

Read this when a rule in `../SKILL.md` looks too strict for the case at hand, or when a thought from the list below turns up. `../SKILL.md` holds the rules.

## Why

Disk is not free. SSDs and RAM are expensive, and an agent session that leaves tens of
gigabytes behind costs the owner real money. The rule is the same as for cycles: engineer it once carefully, run it a thousand times
cheaply.

## Red flags

- "I'll compile it here just to check." → read the code, or hand it to the owner.
- "I'll keep the full log in case I need it." → keep the failing lines.
- "A copy is safer than editing in place." → git is the safety.
- "The temp folder gets cleaned eventually." → it does not; Windows never empties it.
- "It is only a few hundred megabytes." → five sessions make a hundred gigabytes.
- "A worktree keeps the main tree clean." → no worktree; work in the tree there is.
- "I need a baseline build to compare." → ask the owner; never a second tree.

## Notes

- `git show <rev>:<path>` is the backup of a file git already holds.
- Scratch holds a script, a diff, a trimmed log, a number.
- On Windows the scratchpad size is the sum of the `Get-ChildItem -Recurse -File` lengths.
