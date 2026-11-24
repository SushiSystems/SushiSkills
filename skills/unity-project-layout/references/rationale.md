# Why the Unity rules read as they do

Read this when a case the rules did not foresee has to be judged by their purpose.

- **Only the tree and the names change, not the rules.** Unity fixes part of the tree and its
  community writes PascalCase, so a Unity repository follows every rule of `repository-layout`
  and changes only the tree and the names.
- **`docs/` and `tools/` stay lower-case** because the checkers look for them by that name.
- **Tests are under `Assets/`** because Unity compiles only what is under `Assets/` or
  `Packages/`.
- **EditMode and PlayMode tests are separate assemblies** because Unity requires the two modes in
  separate assemblies; the split falls where the code already splits, `Simulation` and `Editor`
  against `View`.
- **The test class is `<Name>Tests`** because that is how C# names a test fixture.
- **A test of two features belongs to `App`** because `App` is the only assembly that references both.
- **Content goes by what it is.** Adding the tenth vehicle adds one folder and deleting a vehicle deletes
  one; a folder per file type puts the assets of one vehicle in many folders.
- **A feature is added with its folder and one line in `App`.** If adding one requires editing
  another feature, the boundary is wrong.
- **A file moves with its `.meta`** because the GUID is stored in the `.meta`; a file that arrives
  without it loses every reference to it. Scenes and prefabs are saved as text so the move can be
  diffed.
