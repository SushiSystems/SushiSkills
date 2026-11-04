---
name: sushisystems-specific
description: Use in every Sushi Systems repository, loaded with sushiskills before any work, for the products, tools, licence, brand and install scheme that belong to Sushi Systems alone and that the sushiskills doctrine leaves out; it names the Sushi skill to load beside each doctrine skill.
---

# Sushi Systems specific

The `sushiskills` doctrine names no product, company or machine. The Sushi Systems layer holds what
it leaves out: the things true of Sushi Systems and of no other organisation. It extends the
doctrine's rules and never replaces one.

## Loading

In a Sushi Systems repository this skill is loaded with `sushiskills`, before any work. Each
doctrine skill the task loads then brings the Sushi skill its row below names, loaded in the same
step. A subagent does the same, since its dispatch sends it to the repository's `CLAUDE.md`.

| Doctrine skill | Sushi skill | What it fills |
| --- | --- | --- |
| `backlog`, `design`, `project-tools`, `build-throughput`, `versioning-and-release` | `sushisystems-tooling` | `sushicore` as the tooling library, the backlog and design commands with and without a module CLI, `tools/settings.py`, the `CLAUDE.md` block |
| `testing`, `continuous-integration` | `sushisystems-testing` | The test command, the CTest call, the time reader, the tolerance helper, the machine of the `large` tier |
| `logging` | `sushisystems-logging` | SushiLog, its projects and fronts, and its types and calls in `INTERFACE.md` |
| `module-install` | `sushisystems-module-install` | SushiHub, the manifest, the dependency declaration, the catalog, the install headings |
| `dependencies`, `api-stability` | `sushisystems-dependencies` | Pinning, finding and upgrading a Sushi library; the logger's runtime file |
| `source-comments` | `sushisystems-licence` | The holder, the licence and the licence block in each language |
| `marketing-copy` | `sushisystems-brand` | How copy names a Sushi product's licence |

## The direction of the dependency

The Sushi skills depend on the doctrine. The doctrine names none of them, and
`tools/layering/check_agnostic.py` fails when a doctrine file does. A fact about Sushi Systems is
written once, in the Sushi skill of its subject. A rule that any organisation could follow is
written in the doctrine. `terms.txt` beside this file lists the names the doctrine must not carry;
the checker reads it.
