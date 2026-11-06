# SushiSkills

The engineering discipline shared by every Sushi Systems repository, written as skills that any
AI coding agent, or any person, can load. It fixes how a repository is laid out, how code is
named and formatted, how source is commented, what is logged, where documentation lives, how
parallel agents stay out of each other's files, and how commits read.

The aim is maintenance cost. A reader who knows one repository already knows the next one.

## Where things are

| Path | Holds |
| --- | --- |
| `skills/` | One folder per rule set; the table of skills is in `skills/README.md` |
| `claude/` | The owner's global instructions; see `claude/README.md` |
| `tools/` | The checkers every repository copies; see `tools/README.md` |
| `docs/` | The manual, starting at [`docs/README.md`](docs/README.md) |

To install the skills, read [`docs/getting_started/INSTALL.md`](docs/getting_started/INSTALL.md).

## Third-party skills

`third_party/superpowers/` holds the MIT-licensed superpowers skill library, unchanged. Its
`README.md` names the version and the licence. Where it disagrees with a Sushi Systems skill, the
Sushi Systems skill wins.

## Licence

Open source under the Apache License 2.0; see `LICENSE`. Third-party material keeps its own
licence; see `NOTICE.md`.

v0.2.0 up to the commit before this licence change was published under the PolyForm Noncommercial
License 1.0.0. Those versions stay available under it, and their code is under Apache 2.0 here.
