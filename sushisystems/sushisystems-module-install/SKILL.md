---
name: sushisystems-module-install
description: Use in a Sushi Systems repository together with the module-install skill, for SushiHub, the sushi-module.toml manifest, the dependency declaration, the catalog and the two install headings.
---

# Module install at Sushi Systems

The `module-install` skill names the roles; this page names the tool or file for each role here. The workspace tool
is SushiHub; the shared tooling library is `sushicore`.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Workspace tool | SushiHub: `hub add` and `hub install` bring a module and its dependencies into a workspace, `hub link` adopts an existing checkout |
| Marker files, variable | `.sushistack`, `workspace.toml`, `SUSHISTACK_HOME`, `~/.sushisystems` |
| Shared tooling library | `sushicore`, pinned in the module's `cli/pyproject.toml` |
| Manifest | `sushi-module.toml` at the root: name (equal to its folder), alias, distribution, repository. Format: SushiStack `docs/reference/MODULE_MANIFEST.md` |
| Dependency declaration | `cli/sushistack.deps.toml`: `[module] depends_on` and `cli`, each Sushi library's pin as `[sushisystems.<name>]`, the third-party ports. Search order: `sushisystems-dependencies` |
| Module CLI | `cli/`, installable with `pip`, scripts `<alias>` and `<name>` |
| Build path variables | `<NAME>_DIR`, `CMAKE_PREFIX_PATH` or `VCPKG_ROOT`, passed by the CLI |
| Catalog | SushiStack `cli/sushihub/catalog.toml`: clone URL, directory and alias behind `hub add <module>` |

## Pages

Headings `Standalone` and `With SushiHub`. `With SushiHub` lists `hub add <module>`,
`hub install-cli <module>` and, for an existing checkout, `hub link <module> <path>`, then states
that a standalone checkout can be linked without changes. `Standalone` installs the CLI with the `sushicore`
source it resolves from.

## Boundary 1 grep and check

A grep of a module's code, CMake, CLI, tests and CI for `hub`, `.sushistack` and `workspace.toml`
finds only a comment or a page that names the workspace-tool route.
`tools/documentation/check_module_install.py` checks the elements, both headings, machine paths
and SushiHub in code.
