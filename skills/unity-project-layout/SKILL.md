---
name: unity-project-layout
description: Use when creating or reorganising a Unity project repository, adding a folder, assembly, scene, prefab or test under Assets/, or naming a C# file or namespace, in a repository.
---

# Unity repositories

A Unity repository keeps the rules of `repository-layout` and swaps only the tree and the names:
one responsibility per module, a README per module, dependencies that point one way. Why each rule
reads as it does is in `references/rationale.md`; read it when a case is not foreseen here.

## The root

```
README.md  LICENSE  NOTICE.md  AGENTS.md  CLAUDE.md  .gitignore  .editorconfig
docs/  tools/
Packages/  ProjectSettings/
Assets/
```

`docs/` and `tools/` keep their lower-case names. `Packages/`, `ProjectSettings/` and `Assets/` are
Unity's. Solution and project files, `Library/`, `Logs/`, `obj/`, `UserSettings/` and build output
are generated and ignored.

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
    Prefabs/      assets only this feature's code uses
```

Only the folders with content exist. Each code folder carries one assembly definition:
`<Company>.<Product>.<Feature>.Simulation`, `.View`, `.Editor`.

| Assembly | May reference |
| --- | --- |
| `Core` | Nothing of ours |
| `<Feature>.Simulation` | `Core` |
| `<Feature>.View` | `Core`, its own `Simulation` |
| `<Feature>.Editor` | `Core`, its own `Simulation` and `View` |
| `App` | Everything; the only assembly that sees two features |

A feature never references another feature; two features meet through an interface, an event or
a command declared in `Core`. A feature is added by creating its folder and one registration line
in `App`, and removed by deleting both.

`Simulation` references no UI, camera, input or audio type and no `ThirdParty` assembly.

## Tests

`Assets/<Product>/Tests/` mirrors `Assets/<Product>/`; `tools/testing/check_test_mirror.py`
enforces the mirror: `<path>/<Name>.cs` is tested by `Tests/<path>/<Name>Tests.cs`.

- The test class is `<Name>Tests`, one per file. `Legacy/` and `Content/` have no tests.
- Each mirrored code folder is one test assembly, `<Company>.<Product>.Tests.<Feature>.<Folder>`.
  `Simulation` and `Editor` tests run in EditMode; `View` tests run in PlayMode.
- A test assembly references what its mirrored folder references, and that folder. A test of two
  features together belongs to `App`.
- The kind of a test is an NUnit `[Category]`, never a folder. The labels are in `testing`.
- Test data sits in `Fixtures/<Name>/` and reference outputs in `Goldens/<Name>/` beside the
  test file that reads them.

## Content

One unit, weapon or map is one folder holding its data asset, prefab, model, textures, materials
and sounds. A `Models/`, `Textures/` or `ScriptableObjects/` folder that collects one file type
across many things is a defect. An asset that only one feature's code uses lives in that
feature's `Prefabs/`.

## Large files

A file above 10 MB, or a source file the build does not need, goes to `Assets/LargeFiles/`. Read
`references/large-files.md` before adding one; it holds the path, git, backup and inventory rules.

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

A file moves with its `.meta`, and a folder with its folder `.meta`, in one `git mv` each. Scenes
and prefabs are saved as text (`Force Text`) before a move.

## Common mistakes

`references/common-mistakes.md` lists the usual misplacements and their fixes; read it when
reviewing a Unity tree.
