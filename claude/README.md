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
clear and compact), the second, one line of boundary names, on `UserPromptSubmit`. No hook runs
Python, writes a file or fires on a tool call.

`hooks/remind_doctrine.py write` builds both files from the boundaries and defaults in
`skills/sushiskills/SKILL.md` and the red flags in its `references/red-flags.md`. Its test fails
when a file no longer matches the skill, so `tools/check_all.py` catches a stale reminder.
