# Common mistakes

Read this when reviewing a Unity tree, or when a file under `Assets/` seems to have no obvious
location.

| Mistake | Fix |
| --- | --- |
| `Scripts/`, `Managers/`, `Utils/` | Name the responsibility; each part goes to the feature that owns it or to `Core` |
| `Prefabs/`, `Materials/`, `Textures/` at the top | Put the asset with the thing it belongs to |
| `(Obsolete)` or `_Old` beside live code | `Legacy/`, with a backlog entry for its deletion |
| A feature that imports another feature's namespace | Declare the contract in `Core` and wire it in `App` |
| A vendored pack edited in place | Leave `ThirdParty/` untouched; wrap it in a feature |
