# Installing

Clone the repository, then link it into each agent. A linked install stays on the revision
that is checked out; a copied one goes stale.

| Agent | Step |
| --- | --- |
| Claude Code | Symlink each folder under `skills/` into `~/.claude/skills/`, and `sushisystems/sushisystems-specific` beside them |
| Codex, Gemini CLI, Copilot CLI | Symlink each folder under `skills/` into `~/.agents/skills/`, and `sushisystems/sushisystems-specific` beside them |
| Any other agent | Point it at `skills/sushiskills/SKILL.md` from the repository's `AGENTS.md`; that file names the others |

## Global instructions

Make `~/.claude/CLAUDE.md` a single import line pointing at `claude/CLAUDE.md`; the exact line
per platform is in [`claude/README.md`](../../claude/README.md).

## Hooks

In a clone of a repository that carries `tools/hooks/`, run `python tools/hooks/install_hooks.py`
once. Git then runs `check_all.py` before each commit and refuses a message without its
`Backlog:` line.

## What a linked install runs

A symlinked install reads the working tree. An uncommitted edit to a skill is
live the moment it is saved, and a half-finished one is live too. Commit rule changes before
leaving them.

## Inside a Sushi Systems repository

`AGENTS.md` and `CLAUDE.md` at the repository root name the skills that repository follows.
