# tools

Reference implementations of the four checkers every Sushi Systems repository carries. A
repository copies this folder whole; a rule is fixed here first and copied out.

| Path | Checks | Takes |
| --- | --- | --- |
| `common/checker.py` | Nothing itself; runs a checker's rule table and prints findings | |
| `documentation/check_source_comments.py` | C++, GLSL, TypeScript and Python: license block, file header, block ceiling, `//` and `#` runs, separators, history words, `@date` | Files or folders |
| `documentation/check_docs_layout.py` | `docs/` entries, document names, work folders, status lines, design ceiling, links, module READMEs, archive candidates | Repository root |
| `documentation/check_changelog.py` | Headings and entry shape, releases kept live, length, one sentence, nesting, cited places | Repository root |
| `layering/check_layering.py` | Declared tiers, upward includes, reaches into another module's `source/` | Repository root |
| `tests/` | Unit tests for the checker rules; run `python -m unittest discover -s tools/tests` | |

Every checker takes `--report` and `--rule NAME`, exits 1 on findings, 0 when clean or
reporting, 2 on a bad path. Python 3.11, standard library only.

## Per-repository settings

`K_` constants at the top of each checker. `check_layering.py` does nothing until
`K_TIER_ORDER` lists the repository's tiers, lowest first. `K_COPYRIGHT_LINE` and
`K_LICENSE_LINES` in `check_source_comments.py` hold the repository's licence lines; a closed
repository sets `K_LICENSE_LINES` to `("All rights reserved. No licence is granted.",)`.

## Not checked

- That every symbol carries a `@brief`: needs a C++ parser.
- Python imports across modules: `check_layering.py` reads C-family includes and CMake only.
- That a changelog verb is past tense: only that it is capitalised.
- That changelog entries are newest first inside a section.
