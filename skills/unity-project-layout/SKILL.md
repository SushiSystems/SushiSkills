---
name: unity-project-layout
description: Use when creating or reorganising a Unity project repository, adding a folder, assembly, scene, prefab or test under Assets/, or naming a C# file or namespace, in a repository.
---

# Unity repositories

Follows `repository-layout`; only the tree and the names differ. See [layout](references/layout.md),
[rationale](references/rationale.md), [common-mistakes](references/common-mistakes.md).

- Root: `README.md LICENSE NOTICE.md AGENTS.md CLAUDE.md .gitignore .editorconfig docs/ tools/
  Packages/ ProjectSettings/ Assets/`; generated files ignored.
- `Assets/<Product>/`: `App/`, `Core/`, `Features/<Feature>/`, `Content/<Kind>/<Name>/` (no code),
  `Legacy/` (code to delete; add none), `Tests/`. Beside it `ThirdParty/<Vendor>/`, git-ignored `LargeFiles/`. No other folder under `Assets/`, except
  a Unity special folder or vendored pack that must be there, named in the layout document.
- A feature: `README.md` plus the folders with content: `Simulation/`, `View/`, `Editor/`, `Prefabs/`. Each code folder has an assembly `<Company>.<Product>.<Feature>.<Folder>`.
- References: `Core` none of ours; `Simulation` `Core`; `View` `Core`, own `Simulation`;
  `Editor` those; `App` all. A feature never references another; they communicate through an
  interface, event or command in `Core`. `Simulation` references no UI, camera, input, audio or `ThirdParty` type. A feature is its folder plus one `App` line.
- Tests mirror `Assets/<Product>/`: `<path>/<Name>.cs` has `Tests/<path>/<Name>Tests.cs`;
  `Legacy/` and `Content/` have none. One test assembly per mirrored code folder,
  `<Company>.<Product>.Tests.<Feature>.<Folder>`, referencing that folder and its references; `Simulation` and `Editor` run EditMode, `View` PlayMode; a two-feature test is `App`'s. Kind is an NUnit `[Category]`, not a folder. Data `Fixtures/<Name>/`, outputs `Goldens/<Name>/`,
  beside the test.
- Content: one game character, vehicle, weapon or map is one folder with all its assets; a folder per file type is a defect. A feature's own asset is in its `Prefabs/`.
- A file above 10 MB, or a source file the build does not need, goes to `Assets/LargeFiles/`
  ([large-files](references/large-files.md)).
- Names: `PascalCase` folders, C# files (one type each), assets, scenes; namespace follows the
  folder; Unity special folders keep Unity's spelling; docs `UPPER_SNAKE_CASE.md`.
- Moving files: [layout](references/layout.md).
