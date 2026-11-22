---
name: unity-project-layout
description: Use when creating or reorganising a Unity project repository, adding a folder, assembly, scene, prefab or test under Assets/, or naming a C# file or namespace, in a repository.
---

# Unity repositories

Keeps `repository-layout`. Trees, tables, names: [layout](references/layout.md).
Why: [rationale](references/rationale.md).

- Root: `README.md LICENSE NOTICE.md AGENTS.md CLAUDE.md .gitignore .editorconfig docs/ tools/
  Packages/ ProjectSettings/ Assets/`; generated files ignored.
- `Assets/<Product>/`: `App/` (composition root), `Core/` (no feature), `Features/<Feature>/`,
  `Content/<Kind>/<Name>/` (no code), `Legacy/` (nothing new enters), `Tests/`. Beside it
  `ThirdParty/<Vendor>/` and git-ignored `LargeFiles/`. No other folder under `Assets/`, except
  a Unity special folder that must sit there or a vendored pack that hard-codes its path, named
  in the layout document.
- A feature: `README.md` plus only the folders with content: `Simulation/`, `View/`, `Editor/`,
  `Prefabs/`. Each code folder has one assembly `<Company>.<Product>.<Feature>.<Folder>`.
- References: `Core` nothing of ours; `Simulation` `Core`; `View` `Core` and its `Simulation`;
  `Editor` those three; `App` all. A feature never references another; they meet through an
  interface, event or command in `Core`. `Simulation` references no UI, camera, input, audio or
  `ThirdParty` type. Adding a feature is its folder plus one line in `App`.
- Tests mirror `Assets/<Product>/`: `<path>/<Name>.cs` is tested by `Tests/<path>/<Name>Tests.cs`;
  `Legacy/` and `Content/` have none. One test assembly per mirrored code folder,
  `<Company>.<Product>.Tests.<Feature>.<Folder>`, referencing what that folder references and
  the folder; `Simulation` and `Editor` run EditMode, `View` PlayMode; a two-feature test
  belongs to `App`. Kind is an NUnit `[Category]`, never a folder. Data in `Fixtures/<Name>/`,
  outputs in `Goldens/<Name>/`, beside the test.
- Content: one unit, weapon or map is one folder with all its assets; a folder collecting one
  file type across many things is a defect. One feature's asset lives in its `Prefabs/`.
- A file above 10 MB, or a source file the build does not need, goes to `Assets/LargeFiles/`;
  read `references/large-files.md` first.
- Names: `PascalCase` for folders, C# files (one type each), assets, scenes; namespace follows
  the folder; Unity special folders keep Unity's spelling; docs `UPPER_SNAKE_CASE.md`.
- Move a file with its `.meta`, a folder with its folder `.meta`, one `git mv` each; scenes
  and prefabs saved as text first.
- Read `references/common-mistakes.md` when reviewing a Unity tree.
