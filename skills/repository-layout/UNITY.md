# Unity repositories

Unity fixes part of the tree and its community reads PascalCase, so a Unity repository keeps the
rules of `SKILL.md` and swaps the tree and the names. Everything not named here is unchanged:
one responsibility per module, a README per module, dependencies that point one way.

## The root

```
README.md  LICENSE  NOTICE.md  AGENTS.md  CLAUDE.md  .gitignore  .editorconfig
docs/  tools/
Packages/  ProjectSettings/
Assets/
```

`docs/` and `tools/` keep their lower-case names, because the checkers look for them.
`Packages/`, `ProjectSettings/` and `Assets/` are Unity's. Solution and project files, `Library/`,
`Logs/`, `obj/`, `UserSettings/` and build output are generated and ignored.

## Under `Assets/`

```
Assets/
    <Product>/                  everything the company wrote
        App/                    composition root: bootstrap code, scenes, game-owned settings
        Core/                   kernel and contracts; references no feature
        Features/<Feature>/     one responsibility per folder
        Content/<Kind>/<Name>/  data and art, no code
        Legacy/                 code on its way out; nothing new enters
    ThirdParty/<Vendor>/        vendored packs, outside this discipline
    LargeFiles/                 git-ignored, backed up by hand
```

No other folder directly under `Assets/`, with two exceptions: a Unity special folder that a
package refuses to find anywhere else (`Resources/`, `Plugins/`, `StreamingAssets/`, `Gizmos/`),
and a vendored pack whose code hard-codes its own `Assets/<Vendor>/` path. The second kind stays
where it demands and the repository's layout document names it.

## A feature

```
Features/<Feature>/
    README.md
    Simulation/   rules; runs headless
    View/         what the player sees and touches
    Editor/       editor tooling
    Tests/
    Prefabs/      assets only this feature's code uses
```

Only the folders with content exist. Each code folder carries one assembly definition:
`<Company>.<Product>.<Feature>.Simulation`, `.View`, `.Editor`, `.Tests`.

| Assembly | May reference |
| --- | --- |
| `Core` | Nothing of ours |
| `<Feature>.Simulation` | `Core` |
| `<Feature>.View` | `Core`, its own `Simulation` |
| `<Feature>.Editor` | `Core`, its own `Simulation` and `View` |
| `App` | Everything; it is the only assembly that sees two features |

A feature never references another feature. Two features meet through an interface, an event or
a command declared in `Core`. A feature is added by creating its folder and one registration
line in `App`, and removed by deleting both. If adding one requires editing another feature, the
boundary is wrong.

`Simulation` references no UI, camera, input or audio type and no `ThirdParty` assembly.

## Content

Content is addressed by what it is, not by its file type. One unit, weapon or map is one folder
holding its data asset, prefab, model, textures, materials and sounds. Adding the tenth unit adds
a folder; deleting a unit deletes one. A `Models/`, `Textures/` or `ScriptableObjects/` folder
that collects one file type across many things is a defect.

An asset that only one feature's code uses lives in that feature's `Prefabs/`.

## Large files

| Rule | Detail |
| --- | --- |
| What goes in | Any file above 10 MB, and any source file the build does not need |
| Where | `Assets/LargeFiles/`, mirroring the path the file would have had |
| Not imported | Files Unity must not import sit under `Assets/LargeFiles/Source~/`; Unity skips a folder ending in `~` |
| Git | The folder's content is ignored; its `README.md` is tracked |
| Backup | The owner copies the folder by hand, `.meta` files included, since they hold the GUIDs |
| Inventory | `docs/reference/LARGE_FILES.md` lists every file with its size and hash, so a clone can tell what it lacks |

## Names

| Thing | Form | Example |
| --- | --- | --- |
| Folder under `Assets/` | `PascalCase`, no space, bracket or leading underscore | `Features/Ballistics` |
| C# file | `PascalCase`, one type per file, named after it | `ProjectileFlight.cs` |
| Namespace | Follows the folder | `SushiSystems.MobileRTS.Ballistics.View` |
| Asset | `PascalCase` | `M1Abrams.prefab` |
| Scene | `PascalCase` | `Match.unity` |
| Unity special folder | Unity's exact spelling | `Editor`, `Resources` |
| Document under `docs/` | `UPPER_SNAKE_CASE.md` | `REPOSITORY_LAYOUT.md` |
| Module README | `README.md` | `Features/Recon/README.md` |

## Moving files

A file moves with its `.meta`, and a folder with its folder `.meta`, in one `git mv` each. The
GUID lives in the `.meta`; a file that arrives without it loses every reference to it. Scenes and
prefabs are saved as text (`Force Text`) before a move, so the result can be diffed.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `Scripts/`, `Managers/`, `Utils/` | Name the responsibility; each part goes to the feature that owns it or to `Core` |
| `Prefabs/`, `Materials/`, `Textures/` at the top | Put the asset with the thing it belongs to |
| `(Obsolete)` or `_Old` beside live code | `Legacy/`, with a backlog item for its deletion |
| A feature that imports another feature's namespace | Declare the contract in `Core` and wire it in `App` |
| A vendored pack edited in place | Leave `ThirdParty/` untouched; wrap it in a feature |
