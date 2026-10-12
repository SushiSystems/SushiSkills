# tools

Reference implementations of the five checkers every Sushi Systems repository carries. A
repository copies this folder whole; a rule is fixed here first and copied out.

| Path | Checks | Takes |
| --- | --- | --- |
| `common/checker.py` | Nothing itself; runs a checker's rule table and prints findings | |
| `documentation/check_source_comments.py` | C++, GLSL, TypeScript and Python: license block, file header, block ceiling, `//` and `#` runs, separators, history words, `@date` | Files or folders |
| `documentation/check_docs_layout.py` | `docs/` entries, required documents, document names, work folders, status lines, design ceiling, links under `docs/`, reachability from `docs/README.md`, READMEs under `modules/<tier>/`, archive candidates | Repository root |
| `documentation/check_changelog.py` | Headings and entry shape, releases kept live, length, one sentence, nesting, cited places | Repository root |
| `documentation/check_docs_truth.py` | The manual against the source: named symbols, cited paths, example sources, history words, page length, duplicated passages, em dashes, the allow-list | Repository root, `--source` |
| `layering/check_layering.py` | Declared tiers, upward includes, reaches into another module's `source/` | Repository root |
| `licensing/write_license_block.py` | Nothing; writes the license block of `source-comments` into every tracked source file, or lists the files that lack it with `--report` | Repository root, `--project` |
| `tests/` | Unit tests for the checker rules; run `python -m unittest discover -s tools/tests` | |

`check_docs_layout.py` reads inline Markdown links, with or without a title, wrapped over a
line or in angle brackets. It does not read reference-style links or a link around an image.

`write_license_block.py` is the one tool here that writes files. It takes its licence lines
from `check_source_comments.py`, covers `.in` templates and `.inc` fragments by the file they become, `--closed` for a closed repository, `--skip GLOB` for generated
files and `--upstream PATH=LINE;LINE` for a ported file; a later run without it keeps those lines. A `--report` run that prints nothing
proves a repository's headers are in place.

`check_docs_truth.py` reads the root `README.md`, every document under `docs/` outside
`agent/`, `archive/` and the changelog, and every `README.md` under the source folders. It
looks each name up in one index of the words of those folders; `--source FOLDER`, repeatable,
replaces the default folders. A design document is exempt from the name, path and example
rules. A source example in a manual page is followed within three lines by
``Source: `<file>` `` or `Source: not compiled`, and `--report` ends with the count of the
second kind. `docs/.docs_truth_allow` holds one regular expression per line with ` # reason`
after it, for names and paths the source cannot hold.

Every checker takes `--report` and `--rule NAME`, exits 1 on findings, 0 when clean or
reporting, 2 on a bad path. Python 3.11, standard library only.

## Per-repository settings

`K_` constants at the top of each checker. `check_layering.py` does nothing until
`K_TIER_ORDER` lists the repository's tiers, lowest first. `K_COPYRIGHT_LINE` and
`K_LICENSE_LINES` in `check_source_comments.py` hold the repository's licence lines; a closed
repository sets `K_LICENSE_LINES` to `("All rights reserved. No licence is granted.",)`.
`check_docs_truth.py` takes a repository's macro prefixes from the source unless
`K_MACRO_PREFIXES` names them, and its page ceilings from `K_LINE_CEILINGS`, which a test
compares with the table in the `documentation` skill.
