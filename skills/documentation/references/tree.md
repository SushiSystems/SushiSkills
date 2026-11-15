# The documentation tree

Read this when creating a repository's `docs/` skeleton, adding a folder or file under `docs/`, or
when `tools/documentation/check_docs_layout.py` reports an entry, a name or a missing file.

```
docs/
    README.md                     manual index; reaches every document outside agent/ and archive/
    CONTRIBUTING.md               what must be documented, how a change lands
    DOCUMENTATION_STYLE_GUIDE.md
    publish.toml                  what the repository publishes to its documentation host
    .docs_truth_allow             names the manual may write that the source cannot hold
    getting_started/  architecture/  guides/
    reference/
        CHANGELOG.md  GLOSSARY.md
    backlog/                      remaining work and known issues, written by the backlog commands
        README.md  backlog.toml  ids.toml  <AREA>.md  detail/<ID>.md
    design/
        README.md                 topic -> design document map
        <TOPIC>/README.md         live intent of one topic, with a status line; pages beside it
        _REVISION/<TOPIC>/        a topic the owner set aside for revision; see DESIGN_FORMAT.md
    agent/
        <YYYY_MM_DD>_<WORK_NAME>/ one folder per piece of agent work
            SPEC.md  PLAN.md  REPORT.md
    archive/                      frozen, only in a repository that has not retired it; see AGENT_WORK.md
<module>/README.md                the module's own facts, beside the code
<folder>/<file>.md                one file's facts, beside it, when its README would pass the ceiling
```

No other folder under `docs/`. No other file names inside a work folder.

Required in every repository: `README.md`, `CONTRIBUTING.md`, `DOCUMENTATION_STYLE_GUIDE.md`,
the two files under `reference/`, `design/README.md`, and `backlog/README.md` with
`backlog/backlog.toml`, which `backlog area add` writes. The other folders appear when they have
content.

## Names

- Files: `UPPER_SNAKE_CASE.md`. Work folders: `YYYY_MM_DD_UPPER_SNAKE_CASE`.
- Every link and cited path resolves. Example paths are in code spans, never live links.
