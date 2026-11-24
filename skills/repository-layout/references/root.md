# The root

Read this when adding, moving or questioning an entry in a repository's root.

```
README.md  LICENSE  NOTICE.md  COMMERCIAL.md  CMakeLists.txt  CMakePresets.json  AGENTS.md
CLAUDE.md  <manifest>  .clang-format  .editorconfig  .gitignore  .gitattributes
.config/  .github/  cmake/  cli/  tools/  modules/  tests/  applications/  assets/  third_party/
docs/
```

| Entry | Holds |
| --- | --- |
| `README.md` | The repository's first document; its shape is in `documentation`, section "The root README" |
| `NOTICE.md` | Third-party components, ported files and redistributed binaries; see `dependencies` |
| `COMMERCIAL.md` | How a company obtains a commercial licence; absent from a closed repository |
| `CMakeLists.txt` | `project()`, options and `add_subdirectory`; no logic |
| `CMakePresets.json` | The configure presets, when the project has them; CMake reads them from the root only |
| `AGENTS.md`, `CLAUDE.md` | Agent instructions and skill declarations; names the skills the repository follows |
| the module manifest | The file the workspace tool reads from the root; `module-install` names its contents |
| `.config/` | Configuration a flag or a key can point a tool at, such as `doxygen/Doxyfile` and `docker/Dockerfile`; its `README.md` has one row per file, naming the tool and the call site that passes the path |
| `.github/` | The files GitHub finds by their path: workflows, templates, `SECURITY.md` and `CODE_OF_CONDUCT.md`; the last two are the shared tooling library's, copied unchanged by its sync command and edited only there |
| `cmake/` | Every CMake function and the tier order table |
| `cli/` | The project CLI package, with its own `pyproject.toml` |
| `tools/` | Manual checkers; see `project-tools` |
| `modules/` | Source, one tree per module |
| `include/`, `source/` | Source of a one-module repository, in place of `modules/` |
| `tests/` | Every test, in a tree that mirrors the source; see `TESTS.md` |
| `applications/` | Executables, one folder each; example programs under `applications/examples/`, probes under `applications/probes/`, scenario benchmarks under `applications/benchmarks/`; which kind a program is comes from `testing` |
| `assets/` | Content an application loads at run time and the package ships; absent when there is none |
| `third_party/` | Vendored code, outside this discipline |
| `docs/` | Everything written in prose; see `documentation` |

Forbidden in the root: `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`,
`CODE_OF_CONDUCT.md`, `Doxyfile`, build output, object files, scratch files. Each has its location in the table above.

`pyproject.toml` is in the root only when the repository is a Python package: pip, uv and
pytest look for it there. In any other repository the CLI's own is under `cli/`.

A dotfile stays in the root only when its tool looks for it nowhere else: clang-format and
EditorConfig search the folders from the edited file up to the root, and git reads `.gitignore` and `.gitattributes`
for the folder they are in. A file a flag can redirect goes to `.config/`.

A repository that holds skills and no modules has `skills/` and `claude/` in place of `cmake/`,
`cli/`, `modules/`, `tests/` and `applications/`. Each skill folder is a module whose `SKILL.md`
is its README. Skills for one organisation alone go in a folder named for it, beside `skills/` and
never inside it, one folder per skill.
