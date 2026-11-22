---
name: module-install
description: Use when a module's way of being obtained, set up, built and recognised changes - its README install section, its setup, doctor or link command, its manifest, its dependency declaration, a remedy message - or when asked whether a repository works with and without its workspace tool.
---

# Module install

Two equal ways in, neither built on the other; a module on only one is unfinished.
**Standalone:** clone the module and its siblings; build, test, run from its own CLI, no
workspace tool. **With the tool:** it brings module and dependencies into a workspace and adopts
the same checkout. `tools/documentation/check_module_install.py` checks it.

## Boundaries

1. **No module needs the workspace tool** in code, build, CLI, tests or CI: a grep of those for its
   name, marker files and variable finds only a comment or page naming the second way.
2. **No machine path in a committed file** (drive, home, workspace layout); paths come from an
   environment variable, the CLI or a relative path.
3. **The tooling the CLI pins is published**: it installs from a public index on a clean machine.
4. **A module declares itself.** Manifest and dependency declaration let the tool recognise,
   provision and link it, no special case; a catalog entry only lets it clone by name.
5. **Both ways are written in every module**, under the headings `Standalone` and
   `With <workspace tool>`, in the README build section and the install page.

## Elements

Each module carries a manifest, dependency declaration, module CLI, build files, catalog entry,
install pages and a bare-clone CI lane. A page names the file holding a version, never copies it.
What each provides, the pages, the audit: `references/elements-and-checking.md`; red flags:
`references/red-flags.md`.

## Defaults

1. **A remedy names the module's own command** (`setup`, `doctor`), never the tool's install.
   **Not when:** the tool itself prints it.
2. **The CLI reads the workspace layout** (variable, marker file, sibling search) and hands the
   build a path variable. **Not when:** no CLI yet.
3. **One place per version fact**: the CLI's package file or the dependency declaration; the
   notice file is the one required prose copy. **Not when:** a changelog line records a version
   true on its date.
4. **The bare-clone lane is its own job on every supported operating system**, so red names the
   standalone way. **Not when:** the module builds on one operating system only.
