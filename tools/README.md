# tools

Reference implementations of the twelve checkers every repository carries. A rule is
fixed here first and copied out with `checking/copy_shared_tools.py`; which files that copies and
which it keeps is in the `project-tools` skill.

| Path | Checks | Takes |
| --- | --- | --- |
| `check_all.py` | Nothing itself; runs the twelve checkers, then the repository's own `<area>/check_<what>.py` files and the tests, and prints only what failed | Repository root |
| `checking/checker.py` | Nothing itself; runs a checker's rule table and prints findings | |
| `checking/copy_shared_tools.py` | Nothing; copies these files, `.github/CODE_OF_CONDUCT.md` and `.github/SECURITY.md` into a repository, keeping its license blocks, `settings.py`, this README and its own tools, or lists the files that differ with `--report` | Repository root, `--from` |
| `settings.py` | Nothing; holds the settings that differ between repositories | |
| `checking/ignored_paths.py` | Nothing itself; names the files and folders git ignores, which no checker reads | |
| `documentation/check_source_comments.py` | C++, GLSL, TypeScript and Python: license block, file header, block ceiling, `//` and `#` runs, separators, history words, `@date` | Files or folders |
| `documentation/check_docs_layout.py` | `docs/` entries, required documents, document names, work folders, status lines in the four forms, design ceiling, links under `docs/`, reachability from `docs/README.md`, READMEs under `modules/<tier>/`, closed work past its grace by the date in the status line, roadmap, journal, handover, milestone, priority and to-do files | Repository root |
| `documentation/check_changelog.py` | Headings and entry shape, releases kept live, length, one sentence, nesting, cited places | Repository root |
| `documentation/check_backlog.py` | `docs/backlog/` through the tooling package's `backlog check`: the store's shape, values, IDs, paths, references here and in siblings checked out beside the repository, pins, the index, a work entry for every open design topic, and the retired backlog files | Repository root |
| `documentation/check_design_format.py` | Design documents, through the tooling package's `design check`: the five sections in order, a status line of at most 160 characters, the phase table and its states, no commit hash, no line that dates built or merged work | Repository root |
| `documentation/check_design_topics.py` | Design topics: through the tooling package's `design check`, a `Modules` line on every topic, its modules exist, each module named by one topic, no loose document, and the topics and phases a work folder names in `Implements` and `Designs` exist; then the generated views and the opt-in rules for a glossary entry on every topic and for the entry ceiling of `docs/design` and `docs/agent` | Repository root |
| `documentation/check_module_install.py` | A module against `module-install`: the manifest, the dependency declaration and the install page exist, the page has the headings the settings name, no machine path in a committed config or code file, no workspace tool command or variable in code, build files or a workflow; a repository whose settings name no manifest is skipped | Repository root |
| `layering/check_agnostic.py` | The folders `K_AGNOSTIC_PATHS` names: no product, company tool, identity or machine path the terms file lists, no engine, vendor or device name outside the folders `K_TECHNOLOGY_EXEMPT` names; a line with `agnostic: allow` is left out | Repository root |
| `documentation/check_docs_follow.py` | Each commit after `K_DOCS_FOLLOW_SINCE` updates the pages whose `**Describes:**` line, or whose README folder, it changes, or carries a `Docs: <page> unchanged (<reason>)` line | Repository root |
| `documentation/docs_follow.py` | Nothing itself; finds the pages a change leaves behind, for the checker and the commit-msg hook | |
| `commits/history.py` | Nothing itself; reads the commits after a base for the checkers that judge each commit | |
| `commits/check_backlog_trailer.py` | Each commit after `K_TRAILER_SINCE` ends with `Backlog: <ID>` for an entry open in its parent or in itself, or `Backlog: none (<reason>)` | Repository root |
| `hooks/install_hooks.py` | Nothing; sets `core.hooksPath` to `tools/hooks` so every clone runs the same hooks | Repository root |
| `hooks/commit_msg.py` | Nothing; the check the `hooks/commit-msg` hook runs on a message before the commit exists | Message file |
| `hooks/pre-commit` | Nothing itself; runs `check_all.py` before a commit is made | |
| `documentation/generate_design_views.py` | Writes the topic map, the Designs block of each module README and the work block of each topic between their markers; `--init` adds the markers, `--check` writes nothing and fails a stale block | Repository root |
| `documentation/repair_design_citations.py` | Rewrites each citation of a design document that moved between one file and a folder with a `README.md` in the manual and the source, and reports the ones it cannot place; `--move OLD NEW` rewrites the citations of a file that was moved or merged; nothing is written without `--apply` | Repository root |
| `documentation/retire_archive.py` | Tags the history that holds the archive folder, unstages it and ignores it, once nothing cites it; nothing is changed without `--apply` | Repository root |
| `documentation/fold_design_topics.py` | Gives each design document that sits loose in `docs/design` a folder of its own with the document as its `README.md`, and rewrites the links out of it and every citation of it; nothing is changed without `--apply` | Repository root |
| `documentation/drop_retired_citations.py` | Replaces each citation of a file under a retired folder, such as the archive folder or a deleted work folder, with a phrase naming it and the version history; a link becomes its text; nothing is written without `--apply` | Repository root, `--prefix` |
| `documentation/citation_files.py` | Nothing itself; lists the files that can cite a document and the lines that cite the archive | |
| `documentation/design_views.py` | Nothing itself; renders the three generated views and reads and writes the blocks | |
| `documentation/design_topics.py` | Nothing itself; reads a topic's name, metadata lines and phase ids and the links work folders make to them | |
| `documentation/tooling_bridge.py` | Nothing itself; loads the `backlog` and `design` modules of the package `K_TOOLING_PACKAGE` names, installed or from a checkout beside the repository, for the checkers that run their rules | |
| `documentation/licence.py` | Nothing itself; reads the holder, the addresses and the licence text from `settings.py` for the license block checker and writer | |
| `documentation/design_status.py` | Nothing itself; finds the design documents and work folders and reads their status lines | |
| `documentation/check_docs_truth.py` | The manual against the source: named symbols, cited paths, example sources, history words, page length, duplicated passages, em dashes, the allow-list | Repository root, `--source` |
| `layering/check_layering.py` | Declared tiers and domains, upward includes from a module or its tests, cross-domain and unlisted same-tier includes, reaches into another module's `source/`, dependencies the build file lists, internal headers in installed ones | Repository root |
| `testing/check_test_mirror.py` | `tests/` mirrors the source: one `test_<name>` file per header or source file (`<name>.test.ts` in TypeScript), no test without a unit, no folder without a counterpart, no test that includes a header under `source/`; in a Unity repository, `Assets/<Product>/Tests/` with `<Name>Tests.cs` | Repository root |
| `testing/check_test_sizes.py` | Every test names its size in its source: a `Small_`, `Medium_` or `Large_` C++ suite, a size mark on a pytest file, class or function, a `small:` TypeScript `describe` | Repository root |
| `testing/check_probes.py` | Folders named as probes or benchmarks outside `applications/probes/` and `applications/benchmarks/`, such a program using a test framework or added to the test runner, one named after another of its kind, one its README does not list | Repository root |
| `logs/check_logging.py` | Console writes outside the paths `settings.py` allows, empty `catch` and `except: pass`, C++ log calls without their module's category, a logging module without `<module>_log_category.hpp`, Python root-logger, named-logger and f-string records | Repository root |
| `ci/check_workflows.py` | The files under `.github/workflows/`: a mapping key written twice in one block, which GitHub rejects before any job starts and a YAML library accepts | Repository root |
| `licensing/write_license_block.py` | Nothing; writes the license block of `source-comments` into every tracked source file, or lists the files that lack it with `--report` | Repository root, `--project` |
| `routing/summarize_dispatches.py` | Nothing; sums the dispatch lines of every `REPORT.md` per model and effort, for `model-routing` | Repository root |
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

`settings.py` holds them. `check_layering.py` does nothing until `K_TIER_ORDER` lists the
repository's tiers, lowest first. `K_DOMAIN_TIERS` names the tiers that share a rank and never
include each other. `K_MODULE_FUNCTION` names the CMake function that declares a module; when it
is set, the dependencies its `K_PUBLIC_DEPENDS` and `K_PRIVATE_DEPENDS` keywords list, and those of any keyword in
`K_PRIVATE_DEPENDS_ALSO` as private ones, are checked
against the includes and are the allowed edges between modules of one tier, and a module marked
`K_INTERNAL_MARK` may not be included by an installed header. Without the function,
`K_SAME_TIER_EDGES` lists each `(includer, included)` pair of one tier. `K_CLOSED` makes
`check_source_comments.py` expect the closed licence lines. `check_docs_truth.py` takes a
repository's macro prefixes from the source unless `K_MACRO_PREFIXES` names them.

`K_TOOLING_PACKAGE`, `K_TOOLING_MINIMUM_VERSION` and `K_TOOLING_SIBLING_SOURCE` name the package the backlog and design checkers run; with none set they report that they cannot run. `K_LICENSE_HOLDER`, `K_LICENSE_COMPANY`, `K_LICENSE_SITE` and the four `K_LICENSE_*_LINES` tuples describe the licence block; with no holder set the license block checker and writer stop with a message. `K_MODULE_MANIFEST`, `K_MODULE_DEPENDENCY_FILE`, `K_MODULE_INSTALL_PAGE`, `K_MODULE_HEADINGS` and `K_MODULE_WORKSPACE_READ` describe a module for `check_module_install.py`, which skips a repository that sets no manifest. `K_LOGGER_NAMESPACE`, `K_LOGGER_C_PREFIX` and `K_LOGGER_MACRO_PREFIX` name the shared logger for the re-export rule of `check_logging.py`. `K_AGNOSTIC_PATHS`, `K_AGNOSTIC_TERMS` and `K_TECHNOLOGY_EXEMPT` set what `check_agnostic.py` reads. `K_EXTRA_TEST_FOLDERS` lists folders of tests, below the root, that `check_all.py` runs after its own. `K_DOCS_FOLLOW_SINCE` names the commit after which `check_docs_follow.py` and the hook require the pages to follow, and `K_DOCS_FOLLOW_IGNORED` the folders no README follows. `K_TRAILER_SINCE` names the commit after which `check_backlog_trailer.py` and the `commit-msg` hook require a `Backlog:` line, and `K_BACKLOG_ID_PATTERN` the shape of an ID; with no commit set, neither checks anything.

Every other `K_` constant sits at the top of its checker and is the same in every repository.
`K_LINE_CEILINGS` in `check_docs_truth.py` is compared by a test with the table in the
`documentation` skill.
