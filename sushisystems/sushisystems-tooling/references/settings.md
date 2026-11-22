# Settings of a Sushi repository

Read when you set or check `tools/settings.py` of a Sushi repository. `tools/README.md` says
what each constant does.

| Constant | Value |
| --- | --- |
| `K_TOOLING_PACKAGE` | `"sushicore"` |
| `K_TOOLING_MINIMUM_VERSION` | the sushicore release the repository's CLI pins |
| `K_TOOLING_SIBLING_SOURCE` | `"sushicore/source"` |
| `K_LICENSE_HOLDER` | `"Mustafa Garip & Sushi Systems"` |
| `K_LICENSE_COMPANY` | `"Sushi Systems"` |
| `K_LICENSE_SITE` | `"https://sushisystems.io"` |
| `K_LICENSE_OPEN_LINES`, `K_LICENSE_CLOSED_LINES`, `K_LICENSE_OPEN_BOX_LINES`, `K_LICENSE_CLOSED_BOX_LINES` | the rows of the `sushisystems-licence` skill |
| `K_MODULE_MANIFEST` | `"sushi-module.toml"` in a module, empty elsewhere |
| `K_MODULE_DEPENDENCY_FILE` | `"cli/sushistack.deps.toml"` |
| `K_MODULE_HEADINGS` | `("## Standalone", "## With SushiHub")` |
| `K_MODULE_WORKSPACE_READ` | the pattern of the hub commands, `SUSHISTACK_HOME`, `.sushistack` and `workspace.toml` |
| `K_LOGGER_NAMESPACE`, `K_LOGGER_C_PREFIX`, `K_LOGGER_MACRO_PREFIX` | `"SushiLog"`, `"sl_"`, `"SL"` in every repository except SushiLog |
