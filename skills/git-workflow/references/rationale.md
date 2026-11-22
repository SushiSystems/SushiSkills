# Git workflow rationale

Read when you need the reason behind a rule of `git-workflow`.

## Branches

One line of history stays readable; a feature branch merged back within days has no time to drift from `main`. A release fix is no branch because `main` carries one line of versions.

## Conflicts

Taking one side wholesale drops the other author's intent without a decision.

## Shared working tree

Nothing tells an agent when another session edits the same checkout.

- A bare `git commit` takes the whole index, and another session's `git add` lands in the same
  index. Hence `git commit -o <path>...`.
- `-o` names only files git knows, so a new file is staged with `git add` first.
