# skills

Each folder is one rule set. Its `SKILL.md` opens with front matter holding a `name`, equal to
the folder name, and a `description` that starts with "Use when" and says when to load it. An
agent reads the descriptions first and loads a skill only when its task matches.

| Skill | Covers |
| --- | --- |
| `sushiskills` | The doctrine and a map to every other skill; load it first |
| `humanizer` | Prose in English and Turkish: documents, comments, commits, replies. Five registers: generic, plain B1–B2 English, informal English and Turkish |
| `marketing-copy` | Copy that presents the company to outsiders, in English and Turkish: the ban on AI-style marketing and how to write it instead |
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
| `testing` | What each change must test, bug fix order, determinism, golden files |
| `dependencies` | Licences, where libraries come from, keeping them private |
| `api-stability` | Public surfaces, deprecation, exports, cross-repository upgrades |
| `performance` | Hot path defaults, measured optimisation, benchmarks |
| `debugging` | Known issues first, temporary instrumentation, root causes |
| `file-formats` | `snake_case` keys, `format_version`, upgrading readers |
| `git-workflow` | `main` and short branches, pushing, conflicts, shared trees |
| `continuous-integration` | What CI runs on Windows and Linux, red builds |
| `platform-portability` | Platform adapters, export macros, paths and text |
| `storage-discipline` | Scratchpad budget, no binaries or copies in scratch, bounded output capture, cleanup before reporting |

`humanizer` and `marketing-copy` carry one file per language and register beside `SKILL.md`,
and a `research/` folder with the sources those files cite.

A skill stays one rule set. A new concern is a new folder, not a new section in an existing one.
