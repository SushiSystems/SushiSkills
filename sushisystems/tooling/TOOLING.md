# Tooling at Sushi Systems

The doctrine's tooling skills name roles: the shared tooling library, the backlog tool, the design
tool. This page says who fills each role at Sushi Systems.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Shared tooling library | `sushicore` |
| Backlog tool | `sushicore`'s `backlog` commands: `<cli> backlog ...` in a repository with a module CLI, `python -m sushicore.backlog ...` in one without. Reference: sushicore's `docs/reference/BACKLOG.md` |
| Design tool | `sushicore`'s `design` commands, run the same two ways. Reference: sushicore's `docs/reference/DESIGN.md` |
| Build machinery | From sushicore: `build_tree`, `build_admission`, `build_gate`, `build_report` |
| Module manifest | `sushi-module.toml` |
| The shared checkers' source | the SushiSkills checkout: `python tools/checking/copy_shared_tools.py ROOT --from <the SushiSkills checkout>` |
| Documentation host | `docs.sushisystems.io`, named by `docs/publish.toml` |

## The settings of a Sushi repository

`tools/settings.py` of a Sushi repository sets these constants. `tools/README.md` says what each does.

| Constant | Value |
| --- | --- |
| `K_TOOLING_PACKAGE` | `"sushicore"` |
| `K_TOOLING_MINIMUM_VERSION` | the sushicore release the repository's CLI pins |
| `K_TOOLING_SIBLING_SOURCE` | `"sushicore/source"` |
| `K_LICENSE_HOLDER` | `"Mustafa Garip & Sushi Systems"` |
| `K_LICENSE_COMPANY` | `"Sushi Systems"` |
| `K_LICENSE_SITE` | `"https://sushisystems.io"` |
| `K_LICENSE_OPEN_LINES`, `K_LICENSE_CLOSED_LINES`, `K_LICENSE_OPEN_BOX_LINES`, `K_LICENSE_CLOSED_BOX_LINES` | the rows of `../licence/LICENCE.md` |
| `K_MODULE_MANIFEST` | `"sushi-module.toml"` in a module, empty elsewhere |
| `K_MODULE_DEPENDENCY_FILE` | `"cli/sushistack.deps.toml"` |
| `K_MODULE_HEADINGS` | `("## Standalone", "## With SushiHub")` |
| `K_MODULE_WORKSPACE_READ` | the pattern of the hub commands, `SUSHISTACK_HOME`, `.sushistack` and `workspace.toml` |
| `K_LOGGER_NAMESPACE`, `K_LOGGER_C_PREFIX`, `K_LOGGER_MACRO_PREFIX` | `"SushiLog"`, `"sl_"`, `"SL"` in every repository except SushiLog |

SushiSkills' own `tools/settings.py` is the reference copy.
