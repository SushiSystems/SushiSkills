# Git workflow rationale

Read when you need the reason behind a rule of `git-workflow`.

## Branches

| Work | Where |
| --- | --- |
| Everyday work | Directly on `main` |
| Risky or multi-day work | `feature/<snake_case_name>`, merged back within days |
| Release fix for an old version | Not a branch; the next PATCH on `main` (see `versioning-and-release`) |

A feature branch is rebased onto `main` before it merges, and deleted after.

## Conflicts

A conflict is resolved by reading both sides and keeping both intents. When the intents
contradict, the agent stops and asks. Never resolve by taking one side wholesale to make the
conflict go away.

## Shared working tree

Nothing tells an agent when another session edits the same checkout.

- A bare `git commit` takes the whole index, and another session's `git add` lands in the same
  index. Hence `git commit -o <path>...`.
- `-o` names only files git knows, so a new file is staged with `git add` first.
- `storage-discipline` forbids worktrees.
