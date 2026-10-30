# Checkers

## Remaining work

| ID | Pri | State | Title | Done when | Blocked by | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RW-5 | P2 | open | Check that every symbol carries a `@brief` | `check_source_comments.py` reports a C++ symbol without `@brief` |  |  | 2026-10-19 |
| RW-6 | P2 | open | Read Python imports across modules in the layering check | `check_layering.py` reports a Python import that crosses a module boundary the layering forbids |  |  | 2026-10-19 |
| RW-7 | P2 | open | Check that a changelog entry's verb is past tense | `check_changelog.py` reports an entry whose verb is not in the past tense |  |  | 2026-10-19 |
| RW-8 | P2 | open | Check that changelog entries run newest first | `check_changelog.py` reports an entry dated after the one above it |  |  | 2026-10-19 |
| RW-9 | P2 | open | Resolve links outside `docs/` | `rule_links` checks the root README, module READMEs and paths cited in backticks |  |  | 2026-10-19 |
| RW-10 | P2 | open | Check module READMEs in every layout | `rule_module_readmes` checks a single-module repository and a skills repository |  |  | 2026-10-19 |
| RW-11 | P2 | open | Check the licence block of shell and CMake files | `rule_license_block` reads `.sh` and `.cmake` files |  |  | 2026-10-19 |
| RW-12 | P2 | open | Tell a second personal copyright line from an upstream notice | `rule_license_block` reports a second copyright line that is not an upstream notice |  |  | 2026-10-19 |
| RW-13 | P2 | open | Read reference-style links and links around an image | `rule_links` and `rule_reachable_from_index` follow both kinds |  |  | 2026-10-19 |
| RW-16 | P2 | open | Copy the shared rows of `tools/README.md` with the shared tools | `copy_shared_tools.py` writes the rows of the shared tools into a repository's `tools/README.md` and keeps the rows of its own tools |  |  | 2026-10-19 |
| RW-17 | P2 | open | Report a setting the shared tools read that `settings.py` lacks | `copy_shared_tools.py` names each `K_` setting the copied tools import that the repository's `tools/settings.py` does not define, with SushiSkills' default |  |  | 2026-10-19 |
| RW-18 | P2 | open | Refuse a changelog without its title and `## Unreleased` | `check_changelog.py` reports a `CHANGELOG.md` that lacks `# Changelog` or `## Unreleased` |  |  | 2026-10-19 |
| RW-20 | P2 | open | Let the test mirror checker skip listed units | `check_test_mirror.py` skips the units a repository lists in `tools/settings.py` and fails on a listed unit that has gained a test |  |  | 2026-10-19 |
| RW-21 | P2 | open | Read TypeScript imports in the layering check | `check_layering.py` reports a TypeScript import that crosses a boundary the repository's tier order forbids |  |  | 2026-10-19 |
| RW-22 | P2 | open | Read C# in the comment, licence and layering checks | `check_source_comments.py` and `write_license_block.py` read `.cs` files, and `check_layering.py` reads a Unity tree's assembly definitions |  |  | 2026-10-19 |

## Known issues

| ID | Origin | Symptom | Workaround | Fix | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- |
