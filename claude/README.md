# claude

`CLAUDE.md` holds the owner's instructions for every project: language, quality, the line that
opens every subagent prompt, and the model and effort per dispatch. For
documentation, source comments and planning it names the skill that holds the rule.

It is read through an import. `~/.claude/CLAUDE.md` holds one line pointing at this file:
`@<checkout>/claude/CLAUDE.md`, where `<checkout>` is the absolute path of this repository's clone
on that machine. Each machine then reads the same file.

`DISPATCH.md` holds the rules every subagent follows. It is not imported, so it costs nothing
outside a dispatch; a subagent reads it by path and proves it with the line it asks for.

`hooks/session_start.txt` and `hooks/prompt_submit.txt` keep the doctrine in front of the agent.
`~/.claude/settings.json` prints them with `cat`: the first on `SessionStart` (startup, resume,
clear and compact), the second on `UserPromptSubmit`. No hook runs Python, writes a file or fires
on a tool call.

- `session_start.txt` holds five files verbatim, each under a line naming its path: the
  `sushiskills` `SKILL.md`, its `references/solid.md`, `skill-map.md` and `excuses.md`, and the
  `storage-discipline` `SKILL.md`. The agent reads every rule and every "Not when" line as
  written, with no summary between it and the rule.
- `prompt_submit.txt` is one line: the names of the boundaries, the headings of the storage rules
  and the instruction to load the skill the skill map names for the task.

`hooks/remind_doctrine.py write` builds both files from those skills. Its test fails when a file
no longer matches them, so the check command catches a stale reminder. Run `write` after any
change to one of the five files, and start a new session to read the result.

## Environment of the harness

`~/.claude/settings.json` sets two variables in `env`, so that no command the agent runs leaves a
cache in a repository:

- `PYTHONDONTWRITEBYTECODE=1` stops Python from writing `__pycache__` folders and `.pyc` files.
- `PYTEST_ADDOPTS=-p no:cacheprovider` stops pytest from writing a `.pytest_cache` folder.
