# Unity layout: trees, tables and naming in full

Trees, tables and examples for the rules in `../SKILL.md`. Read this when creating a folder, an
assembly, a test or a name.

## The root

```
README.md  LICENSE  NOTICE.md  AGENTS.md  CLAUDE.md  .gitignore  .editorconfig
docs/  tools/
Packages/  ProjectSettings/
Assets/
```

`Packages/`, `ProjectSettings/` and `Assets/` are Unity's. The generated files are solution and
project files, `Library/`, `Logs/`, `obj/`, `UserSettings/` and build output.

## Under `Assets/`

```
Assets/
    <Product>/                  everything the company wrote
        App/                    composition root: bootstrap code, scenes, game-owned settings
        Core/                   kernel and contracts; references no feature
        Features/<Feature>/     one responsibility per folder
        Content/<Kind>/<Name>/  data and art, no code
        Legacy/                 code on its way out; nothing new enters
        Tests/                  the mirror of everything above that holds code
    ThirdParty/<Vendor>/        vendored packs, outside this discipline
    LargeFiles/                 git-ignored, backed up by hand
```

The exceptions under `Assets/`: a Unity special folder that a package refuses to find anywhere
else (`Resources/`, `Plugins/`, `StreamingAssets/`, `Gizmos/`), and a vendored pack whose code
hard-codes its own `Assets/<Vendor>/` path.

## A feature

```
Features/<Feature>/
    README.md
    Simulation/   rules; runs headless
    View/         what the player sees and touches
    Editor/       editor tooling
    Prefabs/      assets only this feature's code uses
```

The assemblies are `<Company>.<Product>.<Feature>.Simulation`, `.View` and `.Editor`.

| Assembly | May reference |
| --- | --- |
| `Core` | Nothing of ours |
| `<Feature>.Simulation` | `Core` |
| `<Feature>.View` | `Core`, its own `Simulation` |
| `<Feature>.Editor` | `Core`, its own `Simulation` and `View` |
| `App` | Everything; the only assembly that sees two features |

A feature is removed by deleting its folder and its registration line in `App`.

## Tests

`tools/testing/check_test_mirror.py` enforces the mirror of `Assets/<Product>/` in `Tests/`. The
test class is `<Name>Tests`, one per file. The `[Category]` labels are in `testing`.

## Content

A unit, weapon or map folder holds its data asset, prefab, model, textures, materials and
sounds. `Models/`, `Textures/` and `ScriptableObjects/` are the folders that collect one file
type.

## Large files

`large-files.md` holds the path, git, backup and inventory detail.

## Names

| Thing | Form | Example |
| --- | --- | --- |
| Folder under `Assets/` | `PascalCase`, no space, bracket or leading underscore | `Features/Ballistics` |
| C# file | `PascalCase`, one type per file, named after it | `ProjectileFlight.cs` |
| Test file | The unit's name and `Tests` | `ProjectileFlightTests.cs` |
| Namespace | Follows the folder | `Acme.MobileRts.Ballistics.View` |
| Asset | `PascalCase` | `M1Abrams.prefab` |
| Scene | `PascalCase` | `Match.unity` |
| Unity special folder | Unity's exact spelling | `Editor`, `Resources` |
| Document under `docs/` | `UPPER_SNAKE_CASE.md` | `REPOSITORY_LAYOUT.md` |
| Module README | `README.md` | `Features/Recon/README.md` |

## Moving files

Scenes and prefabs are saved as text with the `Force Text` setting.
