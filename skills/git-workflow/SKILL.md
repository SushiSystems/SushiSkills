---
name: git-workflow
description: Use when creating a branch, merging, pushing, rebasing, resolving a conflict, or deciding where a piece of work should live in git, in a repository.
---

# Git Workflow

One line of history per repository. Work reaches `main` in small commits; nothing leaves the
machine without the owner. Commit messages follow `commits`. Why: `references/rationale.md`.

## Branches

Everyday work goes directly on `main`. Risky or multi-day work goes on
`feature/<snake_case_name>`, merged back within days, rebased onto `main` first and deleted
after. A release fix for an old version is no branch; it is the next PATCH on `main`
(`versioning-and-release`).

## Forbidden

- Force push to any shared branch.
- Rewriting commits that have been pushed.
- Moving or deleting a tag.
- `--no-verify` or skipping signing.

## Pushing

The agent commits; the owner pushes, or the agent pushes when the owner says so for that push.
Approval for one push does not carry to the next.

## Conflicts

Read both sides and keep both intents. When they contradict, stop and ask. Never take one side
wholesale to make a conflict go away.

## Shared working tree

Another session may be editing the same checkout. These hold always:

- Stage by path, and only your own hunks in shared files. Never `git add -A`, `git add .` or
  `git commit -a`.
- Commit with the paths: `git commit -o <path>...`. Stage a new file with `git add` first.
- Check `git diff --cached --stat` before every commit and unstage what is not yours.
- No `git stash`. No worktree (`storage-discipline`).
- Never discard changes you did not make.
