---
name: module-install
description: Use when a module's way of being obtained, set up, built and recognised changes - its README install section, its setup, doctor or link command, its manifest, its dependency declaration, a remedy message - or when asked whether a repository works with and without its workspace tool.
---

# Module install

A module has two ways in, and they are equal. Neither is built on the other, and a module that
works on one and not the other is unfinished.

- **Standalone.** A person clones the module, and the sibling repositories it genuinely needs,
  and gets a working build, test run and run from the module's own CLI and own pages. The
  workspace tool is not installed.
- **With the workspace tool.** It brings the module and its dependencies into a workspace and
  adopts a checkout that already exists. The checkout is the same one the standalone person has.

The workspace tool is a convenience over what a module already does for itself. It reads what the
module declares; it holds nothing the module needs to run.

## Boundaries

1. **No module needs the workspace tool.** Not its code, build files, CLI, tests or CI. A grep of
   those for the tool's name, its marker files and its workspace variable finds only a comment or
   a page that names the second way in.
2. **No machine path in a committed file.** A preset, a config, an example, a command in a page:
   none holds a drive path, a home directory or a workspace layout. A path comes from an
   environment variable, the CLI or a relative location.
3. **The tooling the CLI pins is published.** A module's CLI pins a version of its shared tooling
   library that a clean machine installs from a public index. A pin to an unpublished version
   makes the standalone way fail at its first command.
4. **A module declares itself.** A manifest and a dependency declaration are enough for the
   workspace tool to recognise, provision and link the checkout. The tool has no special case for
   a module, and a catalog entry is only what lets it clone the module by name.
5. **Both ways are written in every module**, under the same two headings, in the elements below.

## The elements

Each module carries all of these. The right column is what the element gives the person, and what
the other way in reads from it.

| Element | What it provides |
| --- | --- |
| Manifest | The module's name (equal to its folder), alias, distribution and repository, so the workspace tool recognises a checkout it never cloned |
| Dependency declaration | The modules it depends on, the pin of each as a release tag, and the third-party ports. The CLI provisions from it; the workspace tool aggregates it |
| Module CLI | Installable with the language's package tool. `setup` provisions the toolchain and libraries the declaration names, `doctor` reports what is missing, and `build`, `test`, `run` and `link` do what they say. It works with the workspace tool absent |
| Build files | A configure that takes every outside path from a variable the CLI hands it. It downloads nothing but test frameworks |
| Catalog entry | The clone URL, directory and alias behind the tool's add command |
| Install pages | The two ways in, in order, with the prerequisites each needs |
| Bare-clone lane | One job in the module's CI that proves the standalone way: checkout, install the CLI, set up, build, test, without the workspace tool or its variable |

## The install pages

The module README's build section and its install page carry the same two headings, `Standalone`
and `With <workspace tool>`, so a person moving between modules finds them in the same place.

`Standalone` lists, in order:

1. Prerequisites the module cannot install for itself: the operating system, the language runtime,
   Git, a compiler only if `setup` does not provision one.
2. The clones: the module and each sibling it needs, side by side, named with their URLs.
3. Installing the CLI, with the source of the tooling library it resolves from.
4. The module's `setup`, `build` and `test`.

The second heading lists the tool's add and install commands, and its link command for a checkout
that exists, then states that the standalone checkout links without any change to it.

A page names the file that holds a version and never copies the version into prose.

## Defaults

1. **A remedy names the module's own command.**
   **Rule:** a message that tells the person how to fix a missing tool or checkout says the
   module's `setup` or `doctor`, never the workspace tool's install.
   **Why:** the module's command works on both ways in; the tool's does not exist on one.
   **Not when:** the message is printed by the workspace tool itself.
2. **The workspace layout is read by the CLI, not by the build files.**
   **Rule:** the workspace variable, the marker file and the sibling folder search are resolved in
   the CLI, which hands the build the result as a path variable.
   **Why:** one place knows how a workspace is laid out; a layout change then edits one file.
   **Not when:** the module has no CLI yet.
3. **One place per version fact.**
   **Rule:** a pin lives in the CLI's package file or the dependency declaration. The notice file
   is the one prose copy a rule requires; every other page names the file.
   **Why:** the same version written in four pages was wrong in three of them.
   **Not when:** a changelog line records a version that was true on its date.
4. **The bare-clone lane runs on both operating systems the module supports.**
   **Rule:** it is a job of its own, so a red result names the standalone way.
   **Why:** a pipeline that installs sibling checkouts by hand passes while a fresh clone fails.
   **Not when:** the module builds on one operating system only.

## Checking a module

Three questions, each answered with a file and a line, and each ending in done, partial or
missing.

1. **Standalone, in code.** From a bare clone with no workspace tool, do the CLI and the build
   provision and build? What do they still read from the tool, its variable, its marker file, a
   per-user folder or a sibling path?
2. **With the workspace tool, in code.** Does the manifest read, does the declaration parse, is
   there a catalog entry, does the tool find the CLI's scripts, does the CLI's link command adopt
   the checkout?
3. **In the pages.** Do the install pages carry both headings, with the prerequisites, and does
   any page, hint string or example assume one way?

## Red flags

- "The CI installs the siblings by hand, so the bare clone must work." → add the lane.
- "Everybody uses the workspace tool, so the page starts there." → both headings, equal.
- "The preset only needs my compiler path." → no machine path in a committed file.
- "The version is in the README so it is easy to find." → name the file.
