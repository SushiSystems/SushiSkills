# Project tools: the checkers and the shared copy

Read this when you need to know what one checker enforces, when you write or change a checker,
or when you copy the shared tools into a repository or set up its known findings. The rules are
in `../SKILL.md`.

## What each checker enforces

| Checker | Enforces |
| --- | --- |
| `tools/documentation/check_source_comments.py` | Every rule in `source-comments` |
| `tools/documentation/check_docs_layout.py` | The tree, required documents, names, work folder contents, status lines, broken links and anchors, reachability from the index, closed work past its grace and the forbidden kinds of file from `documentation` |
| `tools/documentation/check_changelog.py` | One line, 240 characters, one sentence, no nesting |
| `tools/documentation/check_backlog.py` | `BACKLOG_FORMAT.md` in `documentation`, through the backlog tool's `backlog check`: the store's shape, values, IDs, paths, references, pins, the index, and a backlog entry for every open design topic |
| `tools/documentation/check_design_format.py` | `DESIGN_FORMAT.md` in `documentation`, through the design tool's `design check`: the five sections in order, the status length, the phase table and its states, no commit hash, no dated record of work |
| `tools/documentation/check_design_topics.py` | `DESIGN_FORMAT.md` and `AGENT_WORK.md` in `documentation`: through the design tool's `design check`, the `Modules` line on every topic, the modules exist, each module owned by one topic, no loose document, and the topics and phases a work folder names exist; then the generated views and the opt-in rules for a glossary entry per topic and the folder maximum |
| `tools/documentation/check_module_install.py` | `module-install`: the elements of a module, both install headings, no machine path, no workspace tool in code |
| `tools/documentation/check_docs_truth.py` | The manual against the source, from `documentation`: every name and path a page writes in code exists, every example cites the file it is taken from, no history words, the page maximums, no paragraph in two pages, no em dash in prose, a reason on every allow-list entry |
| `tools/layering/check_layering.py` | Module dependencies follow the declared tier order; no module includes or links against another module's private `source/` |
| `tools/testing/check_test_mirror.py` | `tests/` mirrors the public headers, from `repository-layout` |
| `tools/testing/check_test_sizes.py` | Every test writes its size in its source, from `testing` |
| `tools/testing/check_test_value.py` | Every test case written after `K_TEST_VALUE_SINCE` is none of the forbidden kinds, from `testing` |
| `tools/testing/check_test_odr.py` | C++ test sources define no type twice at namespace scope, use no suite name with and without a fixture, and name no test with a character outside `[A-Za-z0-9_]`, from `testing` |
| `tools/testing/check_probes.py` | Probes and scenario benchmarks are in `applications/probes/` and `applications/benchmarks/`, use no test framework, stay out of the test runner, carry a name of their own and are listed, from `testing` and `performance` |
| `tools/logs/check_logging.py` | Log calls carry their module's category, library code writes no console output and hides no failure, from `logging` |
| `tools/commits/check_backlog_trailer.py` | The `Backlog:` line of `commits`: each commit after `K_TRAILER_SINCE` names an entry open in its parent or in itself, or says `none (<reason>)` |
| `tools/hooks/commit_msg.py` | At commit time, beside that line: an open work entry whose `Source` the commit changes is closed or named, and the commit opens at most three entries on the files it changes, from `backlog` |
| `tools/documentation/check_docs_facts.py` | "Facts with one location" in `documentation`: the markers pair, each id has one location, every quote and follow names a fact, and every quote holds its fact's text exactly |
| `tools/documentation/check_docs_follow.py` | "Pages follow what they describe" in `documentation`: each commit after `K_DOCS_FOLLOW_SINCE` updates the pages that describe what it changes, or says why not with a `Docs:` line |
| `tools/layering/check_agnostic.py` | The folders `K_AGNOSTIC_PATHS` names hold no product, company tool, identity, machine path or technology name that the terms file lists; it checks nothing in a repository that names no folder |
| `tools/ci/check_workflows.py` | The workflow files GitHub would refuse before a job starts, from `continuous-integration` |

## A rule written out

```python
def rule_block_ceiling(lines: list[str]) -> Iterator[Finding]:
    """Yields a finding for each comment block longer than eight lines."""
```

Nothing else in the checker changes.

## The shared copy in detail

The sync command of the shared tooling library copies the shared files as one release tag holds
them, never a branch or a working tree, and writes `tools/shared_tools.lock`: the tag, its
commit and a hash per file. Its check mode lists each file that differs from the lock and exits 1.
The tag is the library release the repository's CLI pins, so the tools and the library move
together.

- It runs from the library's package, never from a repository's copy, so a fix to the copier
  applies on the run that brings it.
- A shared file whose text no upstream version ever held is a local edit: the copy refuses,
  writes nothing and names the file, and `--force` overwrites it. Move the edit upstream first,
  or drop it.
- A file the repository holds that the library shared once and no longer holds is named as
  removed upstream. The copy never deletes it; the repository removes it in its own commit.

## Known findings in detail

`check_all.py` passes the findings an entry of `known_findings.toml` allows. It fails:

- a finding no entry allows;
- a group found fewer times than its entry says;
- an entry found no more;
- an entry whose ID is not open.

`python tools/checking/known_findings.py ROOT --write --backlog <ID>`
writes the list from the findings of the moment, once, when the tools arrive, and refuses to
overwrite one.
