---
name: module-install
description: Use when a Sushi Systems module's way of being obtained, set up, built and recognised changes - its README install section, `setup`, `doctor` or `link`, `sushi-module.toml`, the dependency fragment, the SushiHub catalog entry, a remedy message - or when asked whether a repository works with and without SushiHub.
---

# Module install

A module has two ways in, and they are equal. Neither is built on the other, and a module that
works on one and not the other is unfinished.

- **Standalone.** A person clones the module, and the sibling repositories it genuinely needs,
  and gets a working build, test run and run from the module's own CLI and own pages. SushiHub
  is not installed.
- **With SushiHub.** `hub add` and `hub install` bring the module and its dependencies into a
  workspace, and `hub link` adopts a checkout that already exists. The checkout is the same
  one the standalone person has.

SushiHub is a convenience over what a module already does for itself. It reads what the module
declares; it holds nothing the module needs to run.

## Boundaries

1. **No module needs SushiHub.** Not its code, CMake, CLI, tests or CI. A grep of those for
   `hub`, `.sushistack` and `workspace.toml` finds only a comment or a page that names the
   second way in.
2. **No machine path in a committed file.** A preset, a config, an example, a command in a page:
   none holds `D:/...`, a home directory or a workspace layout. A path comes from an environment
   variable, the CLI or a relative location.
3. **The core the CLI pins is published.** A module's `cli/pyproject.toml` pins a `sushicore`
   version that a clean machine installs from its index. A pin to an unpublished version makes
   the standalone way fail at its first command.
4. **A module declares itself.** `sushi-module.toml` and the dependency fragment are enough for
   SushiHub to recognise, provision and link the checkout. SushiHub has no special case for a
   module, and a catalog entry is only what lets `hub add` clone it by name.
5. **Both ways are written in every module**, under the same two headings, in the elements below.

## The elements

Each module carries all of these. The right column is what the element gives the person, and
what the other way in reads from it.

| Element | Where | What it provides |
| --- | --- | --- |
| Manifest | `sushi-module.toml` at the root | The module's name (equal to its folder), alias, distribution and repository, so SushiHub recognises a checkout it never cloned. Format: SushiStack `docs/reference/MODULE_MANIFEST.md` |
| Dependency fragment | `cli/sushistack.deps.toml` | `[module] depends_on` and `cli`, the pins of each Sushi library as `[sushisystems.<name>]`, and the third-party ports. The CLI provisions from it; SushiHub aggregates it. The search order for a Sushi library is in `dependencies`, "A Sushi library as a dependency" |
| Module CLI | `cli/`, installable with `pip`, scripts `<alias>` and `<name>` | `setup` (provisions the toolchain and libraries the fragment names), `doctor` (reports what is missing), `build`, `test`, `run`, `link` and `unlink`. It works with SushiHub absent |
| Build files | `CMakeLists.txt`, `cmake/`, presets | A configure that takes every outside path from `<NAME>_DIR`, `CMAKE_PREFIX_PATH` or `VCPKG_ROOT`, handed by the CLI. It downloads nothing but test frameworks |
| Catalog entry | SushiStack `cli/sushihub/catalog.toml` | The clone URL, directory and alias behind `hub add <module>` |
| Install pages | the module `README.md` "Install" and `docs/getting_started/INSTALL.md` | The two ways in, in order, with the prerequisites each needs |
| Bare-clone lane | one job in the module's CI | Proof that the standalone way works: checkout, install the CLI, `<alias> setup`, build, test, with no `hub` and no `SUSHISTACK_HOME` |

## The install pages

Both pages carry the same two headings, `Standalone` and `With SushiHub`, so a person moving
between modules finds them in the same place.

`Standalone` lists, in order:

1. Prerequisites the module cannot install for itself: the operating system, Python, Git, a
   compiler only if `setup` does not provision one.
2. The clones: the module and each sibling it needs, side by side, named with their URLs.
3. Installing the CLI, with the `sushicore` source it resolves from.
4. `<alias> setup`, `<alias> build`, `<alias> test`.

`With SushiHub` lists `hub add <module>`, `hub install-cli <module>`, and `hub link <module>
<path>` for a checkout that exists, then states that the standalone checkout links without any
change to it.

A page names the file that holds a version, such as `cli/pyproject.toml`, and never copies the
version into prose.

## Defaults

1. **A remedy names the module's own command.**
   **Rule:** a message that tells the person how to fix a missing tool or checkout says `<alias>
   setup` or `<alias> doctor`, never `hub install`.
   **Why:** the module's command works on both ways in; `hub install` does not exist on one.
   **Not when:** the message is printed by SushiHub itself.
2. **The workspace layout is read by the CLI, not by CMake.**
   **Rule:** `SUSHISTACK_HOME`, `.sushistack` and the sibling folder search are resolved in the
   CLI, which hands CMake the result as `<NAME>_DIR`.
   **Why:** one place knows how a workspace is laid out; a layout change then edits one file.
   **Not when:** the module has no CLI yet.
3. **One place per version fact.**
   **Rule:** a pin lives in `cli/pyproject.toml` or `cli/sushistack.deps.toml`. `NOTICE.md` is
   the one prose copy a rule requires; every other page names the file.
   **Why:** the same version written in four pages was wrong in three of them.
   **Not when:** a changelog line records a version that was true on its date.
4. **The bare-clone lane runs on both operating systems the module supports.**
   **Rule:** it is a job of its own, so a red result names the standalone way.
   **Why:** a pipeline that installs sibling checkouts by hand passes while a fresh clone fails.
   **Not when:** the module builds on one operating system only.

## Checking a module

Three questions, each answered with a file and a line, and each ending in done, partial or
missing.

1. **Standalone, in code.** From a bare clone with no `hub`, do the CLI and CMake provision and
   build? What do they still read from `hub`, `SUSHISTACK_HOME`, a `.sushistack` marker,
   `~/.sushisystems` or a sibling path?
2. **With SushiHub, in code.** Does the manifest read, does the fragment parse, is there a
   catalog entry, does `hub install-cli` find the scripts, does `<alias> link` adopt the
   checkout?
3. **In the pages.** Do the install pages carry both headings, with the prerequisites, and does
   any page, hint string or example assume one way?

## Red flags

- "The CI installs the siblings by hand, so the bare clone must work." → add the lane.
- "Everybody uses `hub`, so the page starts there." → both headings, equal.
- "The preset only needs my compiler path." → no machine path in a committed file.
- "The version is in the README so it is easy to find." → name the file.
