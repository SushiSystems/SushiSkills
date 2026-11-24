---
name: module-install
description: Use when a module's way of being obtained, set up, built and recognised changes - its README install section, its setup, doctor or link command, its manifest, its dependency declaration, a remedy message - or when asked whether a repository works with and without its workspace tool.
---

# Module install

Two equal install methods, neither requiring the other; one alone is unfinished.
**Standalone:** clone the module and its siblings; build, test and run from its own CLI with no
workspace tool. **With the tool:** it clones module and dependencies into a workspace and
registers the same checkout the standalone method uses.

## Boundaries

1. **No module needs the workspace tool** in code, build, CLI, tests or CI: a grep of those for
   its name, marker files and variable finds only a comment or page naming the other method.
2. **No machine path in a committed file** (drive, home, workspace layout); use an environment
   variable, the CLI or a relative path.
3. **The tooling the CLI pins is published**: installable from a public index on a clean machine.
4. **A module declares its identity and dependencies.** Manifest and dependency declaration let
   the tool recognise, provision and link it with no special case; a catalog entry only lets it
   clone by name.
5. **Both methods are written in every module**, under the headings `Standalone` and
   `With <workspace tool>`, in the README build section and the install page.

## Elements

Each module carries every element `references/elements-and-checking.md` lists, and that file
gives what each provides, the pages, the audit, its checker and what a sibling is. A page names
the file holding a version, never copies it. Excuses: `references/excuses.md`.

## Defaults

1. **A remedy names the module's own command** (`setup`, `doctor`), never the tool's install.
   **Not when:** the tool itself prints it.
2. **The CLI reads the workspace layout** (variable, marker file, sibling search) and passes the
   build a path variable. **Not when:** no CLI yet.
3. **One location per version fact**: the CLI's package file or the dependency declaration; the
   notice file is the one required prose copy. **Not when:** a changelog line records a version
   true on its date.
4. **The bare-clone build is a separate CI job on every supported operating system**, so a failure
   names the standalone method. **Not when:** the module builds on one operating system only.
