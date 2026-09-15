# SushiSystemsProgramming

The engineering discipline shared by every Sushi Systems repository, written as skills that any
AI coding agent, or any person, can load. It fixes how a repository is laid out, how code is
named and formatted, how source is commented, what is logged, where documentation lives, how
parallel agents stay out of each other's files, and how commits read.

The aim is maintenance cost. A reader who knows one repository already knows the next one.

## Skills

Each skill is one rule set in its own folder under `skills/`, with a `SKILL.md` that opens with
a `name` and a `description` saying when to load it.

| Skill | Covers |
| --- | --- |
| `sushisystemsprogramming` | The doctrine and a map to every other skill; load it first |
| `humanizer` | Prose in English and Turkish: documents, comments, commits, replies |
| `repository-layout` | The root, single-module and multi-module trees, module rules |
| `cpp-code-style` | C++ formatting, naming, files, includes, class shape, errors |
| `python-code-style` | Python layout, formatting, naming, class shape, errors, logging, tests |
| `typescript-code-style` | TypeScript layout, brace symmetry, naming, class shape, errors, tests |
| `source-comments` | License block, Doxygen file and symbol blocks, docstrings, what is forbidden |
| `logging` | Categories, levels, what is and is not logged, silent failures |
| `documentation` | The `docs/` tree, placement, design documents, agent work lifecycle, archive |
| `multi-agent-work` | Orchestrator and workers, wave planning, dispatch, accepting reports |
| `commits` | Commit subject grammar, body, staging |
| `versioning-and-release` | Semantic versions, `vX.Y.Z` tags, when a release is due, how it is cut |
| `project-tools` | The four checkers every repository carries and their shared contract |

## Using the skills

**Claude Code.** Link or copy each folder under `skills/` into `~/.claude/skills/`.

**Codex, Gemini CLI, Copilot CLI.** Link or copy them into `~/.agents/skills/`, which these
tools read.

**Any other agent.** Point it at `skills/sushisystemsprogramming/SKILL.md` from the repository's
`AGENTS.md`; that file names the others.

Inside a Sushi Systems repository, the root `AGENTS.md` and `CLAUDE.md` are one line each,
pointing at `docs/CLAUDE.md`, which names the skills the repository follows.

## Changing a rule

A rule changes here first, in its own skill, and every repository follows it from then on. A
skill stays one rule set: a new concern is a new folder, not a new section in an existing one.

## License

Apache License 2.0. See `LICENSE`.
