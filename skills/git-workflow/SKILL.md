---
name: git-workflow
description: Use when creating a branch, merging, pushing, rebasing, resolving a conflict, or deciding where a piece of work should live in git, in a Sushi Systems repository.
---

# Git Workflow

One line of history per repository. Work reaches `main` in small commits; nothing leaves the
machine without the owner.

## Branches

| Work | Where |
| --- | --- |
| Everyday work | Directly on `main` |
| Risky or multi-day work | `feature/<snake_case_name>`, merged back within days |
| Release fix for an old version | Not a branch; the next PATCH on `main` (see `versioning-and-release`) |

A feature branch is rebased onto `main` before it merges, and deleted after.

## Forbidden

- Force push to any shared branch.
- Rewriting commits that have been pushed.
- Moving or deleting a tag.
- `git worktree`, `git stash` and `git add -A` or `git add .` when another session may share the
  working tree.
- `--no-verify` or skipping signing.

## Pushing

The agent commits; the owner pushes, or the agent pushes when the owner says so for that push.
Approval for one push does not carry to the next.

## Conflicts

A conflict is resolved by reading both sides and keeping both intents. When the intents
contradict, the agent stops and asks. Never resolve by taking one side wholesale to make the
conflict go away.

## Shared working tree

Another session may be editing the same checkout.

- Stage by path, and only your own hunks in shared files.
- Check `git diff --cached --stat` before every commit and unstage anything that is not yours.
- Never discard changes you did not make.

Commit messages follow `commits`.
