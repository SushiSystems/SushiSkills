# Module install: elements, pages and checking

Read this when adding or reviewing one of a module's install elements, writing its install pages,
or answering whether a repository works with and without its workspace tool. The rules themselves
are in `../SKILL.md`.

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

`Standalone` lists, in order:

1. Prerequisites the module cannot install for itself: the operating system, the language runtime,
   Git, a compiler only if `setup` does not provision one.
2. The clones: the module and each sibling it needs, side by side, named with their URLs.
3. Installing the CLI, with the source of the tooling library it resolves from.
4. The module's `setup`, `build` and `test`.

The second heading lists the tool's add and install commands, and its link command for a checkout
that exists, then states that the standalone checkout links without any change to it.

## Why the defaults hold

1. A remedy names the module's own command because that command works on both ways in; the
   tool's does not exist on one.
2. The CLI reads the workspace layout so that one place knows how a workspace is laid out; a
   layout change then edits one file.
3. One place per version fact, because the same version written in four pages was wrong in three
   of them.
4. The bare-clone lane is a job of its own because a pipeline that installs sibling checkouts by
   hand passes while a fresh clone fails.

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
