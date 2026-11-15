# Why the Unity rules read as they do

Read this when a case the rules did not foresee has to be judged by their purpose.

- **The tree is swapped, not the rules.** Unity fixes part of the tree and its community reads
  PascalCase, so a Unity repository keeps `repository-layout` and changes only the tree and the
  names.
- **`docs/` and `tools/` stay lower-case** because the checkers look for them by that name.
- **Tests sit under `Assets/`** because Unity compiles only what sits under `Assets/` or
  `Packages/`.
- **EditMode and PlayMode tests are separate assemblies** because Unity requires the two modes in
  separate assemblies; the split falls where the code already splits, `Simulation` and `Editor`
  against `View`.
- **The test class is `<Name>Tests`** because that is how C# names a test fixture.
- **A test of two features belongs to `App`** because `App` is the only assembly that sees both.
- **Content goes by what it is.** Adding the tenth unit adds a folder and deleting a unit deletes
  one; a folder per file type spreads one thing over many folders.
- **A feature is added with its folder and one line in `App`.** If adding one requires editing
  another feature, the boundary is wrong.
- **A file moves with its `.meta`** because the GUID lives in the `.meta`; a file that arrives
  without it loses every reference to it. Scenes and prefabs are saved as text so the move can be
  diffed.
