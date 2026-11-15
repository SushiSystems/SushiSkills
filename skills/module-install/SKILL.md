---
name: module-install
description: Use when a module's way of being obtained, set up, built and recognised changes - its README install section, its setup, doctor or link command, its manifest, its dependency declaration, a remedy message - or when asked whether a repository works with and without its workspace tool.
---

# Module install

A module has two equal ways in, neither built on the other. A module that works on one and not the
other is unfinished.

- **Standalone.** A person clones the module and the siblings it genuinely needs, and builds, tests
  and runs it from its own CLI and pages, with no workspace tool installed.
- **With the workspace tool.** The tool brings the module and its dependencies into a workspace and
  adopts an existing checkout, the same one the standalone person has.

The workspace tool reads what the module declares; it holds nothing the module needs to run.

`tools/documentation/check_module_install.py` checks the elements, both headings, machine paths
and the workspace tool in code; its messages carry the detail.

## Boundaries

1. **No module needs the workspace tool.** Not its code, build files, CLI, tests or CI. A grep of
   those for the tool's name, its marker files and its workspace variable finds only a comment or
   a page that names the second way in.
2. **No machine path in a committed file.** No drive path, home directory or workspace layout in a
   preset, config, example or page command. A path comes from an environment variable, the CLI or
   a relative location.
3. **The tooling the CLI pins is published.** The pinned version of the shared tooling library
   installs from a public index on a clean machine; an unpublished pin breaks the standalone way
   at its first command.
4. **A module declares itself.** Its manifest and dependency declaration are enough for the
   workspace tool to recognise, provision and link the checkout. The tool has no special case for
   a module; a catalog entry only lets it clone the module by name.
5. **Both ways are written in every module**, under the same two headings, in the elements below.

## The elements

Every module carries a manifest, a dependency declaration, a module CLI (`setup`, `doctor`,
`build`, `test`, `run`, `link`, working without the workspace tool), build files that take every
outside path from a variable the CLI hands them and download nothing but test frameworks, a
catalog entry, install pages, and a bare-clone lane in CI. What each provides, the order of the
`Standalone` page and the three questions for checking a module are in
`references/elements-and-checking.md`; read it when adding or reviewing an element or auditing a
module.

## The install pages

The module README's build section and its install page carry the same two headings, `Standalone`
and `With <workspace tool>`. `Standalone` gives the prerequisites, the clones, the CLI install and
`setup`, `build`, `test`; the second gives the tool's add, install and link commands and states
that the standalone checkout links unchanged. A page names the file that holds a version and never
copies the version into prose.

## Defaults

The reason behind each default is in `references/elements-and-checking.md`.

1. **A remedy names the module's own command.**
   **Rule:** a message that tells the person how to fix a missing tool or checkout says the
   module's `setup` or `doctor`, never the workspace tool's install.
   **Not when:** the message is printed by the workspace tool itself.
2. **The workspace layout is read by the CLI, not by the build files.**
   **Rule:** the CLI resolves the workspace variable, the marker file and the sibling folder search,
   and hands the build the result as a path variable.
   **Not when:** the module has no CLI yet.
3. **One place per version fact.**
   **Rule:** a pin lives in the CLI's package file or the dependency declaration. The notice file
   is the one prose copy a rule requires; every other page names the file.
   **Not when:** a changelog line records a version that was true on its date.
4. **The bare-clone lane runs on both operating systems the module supports.**
   **Rule:** it is a job of its own, so a red result names the standalone way.
   **Not when:** the module builds on one operating system only.

## Red flags

- "The CI installs the siblings by hand, so the bare clone must work." → add the lane.
- "Everybody uses the workspace tool, so the page starts there." → both headings, equal.
- "The preset only needs my compiler path." → no machine path in a committed file.
- "The version is in the README so it is easy to find." → name the file.
