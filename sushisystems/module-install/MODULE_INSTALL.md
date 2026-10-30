# Module install at Sushi Systems

The `module-install` skill names the roles: the workspace tool, the manifest, the dependency
declaration, the shared tooling library, the catalog. This page says who fills each role at Sushi
Systems. The workspace tool is SushiHub, and the shared tooling library is `sushicore`.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Workspace tool | SushiHub: `hub add` and `hub install` bring a module and its dependencies into a workspace, `hub link` adopts a checkout that exists |
| Its marker files and variable | `.sushistack`, `workspace.toml`, `SUSHISTACK_HOME`, `~/.sushisystems` |
| Shared tooling library | `sushicore`, pinned in the module's `cli/pyproject.toml` |
| Manifest | `sushi-module.toml` at the root: the module's name (equal to its folder), alias, distribution and repository. Format: SushiStack `docs/reference/MODULE_MANIFEST.md` |
| Dependency declaration | `cli/sushistack.deps.toml`: `[module] depends_on` and `cli`, the pins of each Sushi library as `[sushisystems.<name>]`, and the third-party ports. The search order for a Sushi library is in `../dependencies/DEPENDENCIES.md` |
| Module CLI | `cli/`, installable with `pip`, scripts `<alias>` and `<name>` |
| Build path variables | `<NAME>_DIR`, `CMAKE_PREFIX_PATH` or `VCPKG_ROOT`, handed by the CLI |
| Catalog | SushiStack `cli/sushihub/catalog.toml`: the clone URL, directory and alias behind `hub add <module>` |

## Pages

The headings are `Standalone` and `With SushiHub`. `With SushiHub` lists `hub add <module>`,
`hub install-cli <module>`, and `hub link <module> <path>` for a checkout that exists, then states
that the standalone checkout links without any change to it. `Standalone` installs the CLI with the
`sushicore` source it resolves from.

## The grep of boundary 1

A grep of a module's code, CMake, CLI, tests and CI for `hub`, `.sushistack` and `workspace.toml`
finds only a comment or a page that names the second way in.

## Checking

`tools/documentation/check_module_install.py` checks the elements, both headings, no machine path
and no SushiHub in code.
