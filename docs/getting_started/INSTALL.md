# Installing

Clone the repository, then link it into each agent. Linking, not copying, keeps every machine
on the revision that is checked out.

| Agent | Step |
| --- | --- |
| Claude Code | Symlink each folder under `skills/` into `~/.claude/skills/` |
| Codex, Gemini CLI, Copilot CLI | Symlink each folder under `skills/` into `~/.agents/skills/` |
| Any other agent | Point it at `skills/sushiskills/SKILL.md` from the repository's `AGENTS.md`; that file names the others |

## Global instructions

Make `~/.claude/CLAUDE.md` a single import line pointing at `claude/CLAUDE.md`; the exact line
per platform is in [`claude/README.md`](../../claude/README.md).

## What a linked install runs

A symlinked install reads the working tree, not a commit. An uncommitted edit to a skill is
live the moment it is saved, and a half-finished one is live too. Commit rule changes before
leaving them.

## Inside a Sushi Systems repository

`AGENTS.md` and `CLAUDE.md` at the repository root name the skills that repository follows.
