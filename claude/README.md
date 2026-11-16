# claude

`CLAUDE.md` holds the owner's instructions for every project: language, quality, the line that
opens every subagent prompt, and the model and effort per dispatch. For
documentation, source comments and planning it names the skill that holds the rule.

It is read through an import. `~/.claude/CLAUDE.md` holds one line pointing at this file:
`@<checkout>/claude/CLAUDE.md`, where `<checkout>` is the absolute path of this repository's clone
on that machine. Each machine then reads the same file.

`DISPATCH.md` holds the rules every subagent follows. It is not imported, so it costs nothing
outside a dispatch; a subagent reads it by path and proves it with the line it asks for.

`hooks/remind_doctrine.py` keeps the doctrine in front of the agent in a long session. It reads
the boundaries and defaults from `skills/sushiskills/SKILL.md` and the red flags from its
`references/red-flags.md` each time it runs, so it restates nothing. `~/.claude/settings.json`
runs it on `SessionStart` (startup, resume, clear and compact, in full), on `UserPromptSubmit`
(one line of boundary names) and on `PostToolUse` (in full every 25 tool calls).
