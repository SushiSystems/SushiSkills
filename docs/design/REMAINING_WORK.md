# Remaining work

The single backlog of this repository.

## Checks the checkers do not make

- `check_source_comments.py` does not check that every symbol carries a `@brief`; that needs a
  C++ parser.
- `check_layering.py` reads C-family includes and CMake only, not Python imports across modules.
- `check_changelog.py` checks that an entry's verb is capitalised, not that it is past tense.
- `check_changelog.py` does not check that entries are newest first inside a section.
- `rule_links` resolves Markdown links under `docs/` only; it skips the root README, module
  READMEs and paths cited in backticks.
- `rule_module_readmes` covers `modules/<tier>/<module>/` only; a single-module repository and
  a skills repository are not checked.

## Estate programmes

The estate audit of 2026-10-05 opened five programmes. The first, rules unification, is this
repository's; the others (licence, command line, documentation and layout, code) run in the
sibling repositories and take their rules from here.
