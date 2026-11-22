# A sibling library as a dependency

Read this when a repository links a sibling library of the same organisation: when declaring
or moving its pin, when wiring how the build finds it, or when `setup` or `doctor` handles it.

A repository builds on its own, with or without a workspace: whoever clones only a library gets
what it depends on through the repository's own `setup`, without the workspace tool.

1. The repository's dependency declaration lists each sibling library it links and pins it with a
   release tag and the library's full commit hash.
2. The build finds it in this order, the CLI and the build files alike, and stops at the first
   that exists:
   1. a path variable, set by the person or the CLI;
   2. the sibling checkout beside the repository;
   3. the copy `setup` fetched at the pinned version, which it refuses when the commit differs
      from the pin.
3. The build never downloads; it only reads the path the CLI hands it.
4. `doctor` reports a sibling whose commit differs from the pin, and which of the three it used.
5. Moving a pin is an upgrade (`../SKILL.md`, "Upgrading and removing"). Every repository
   pinning a library moves together, and the library's CI builds and tests each repository that
   pins it before a release.
6. A workspace tool takes over what a repository set up on its own. The toolchains `setup`
   installed sit in a machine root the tool reads too, so nothing is fetched twice, and the tool
   adopts a checkout the person made. The workspace sibling then wins the search above.

When `setup` cannot fetch, it says in one message what it tried to fetch, from where, and how to
hand it a checkout through the path variable. Two pins of one library in one dependency chain at
different versions are an error `doctor` names, with both pinning repositories.
