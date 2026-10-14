# Private headers, header-only and internal modules

Read from the `repository-layout` skill before placing a header no consumer includes, or declaring
a header-only or an internal module.

A header that nothing outside the module includes is private and lives under `source/`, beside the
code that uses it. A private tree of headers, such as a library's kernels, is a folder under
`source/`, never a top-level folder.

A module whose code is all templates and inline functions has no `source/` folder. It is declared
as a header-only target, it still names every module it includes, and it carries the test that
includes each of its headers first and alone (see `TESTS.md`).

A header that another module of the same repository includes, and a consumer must not, cannot stay
under `source/`: module rule 3 in `SKILL.md` forbids the reach. It goes to the `include/` tree of
an internal module. An internal module is marked so in its `CMakeLists.txt`, its headers are never
installed, and its README says so in the first paragraph. A module's `include/` root is installed
whole or not at all, so headers of both kinds are two modules.
