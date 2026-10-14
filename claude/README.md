# claude

`CLAUDE.md` holds the owner's instructions for every project: language, quality, the line that
opens every subagent prompt, and the model and effort per dispatch. For
documentation, source comments and planning it names the skill that holds the rule.

It is read through an import. `~/.claude/CLAUDE.md` holds one line pointing at this file:
`@D:/Projects/sushiskills/claude/CLAUDE.md` on Windows, `@~/Projects/sushiskills/claude/CLAUDE.md`
on Linux, adjusted to where the repository is cloned. Each machine then reads the same file.

`DISPATCH.md` holds the rules every subagent follows. It is not imported, so it costs nothing
outside a dispatch; a subagent reads it by path and proves it with the line it asks for.
