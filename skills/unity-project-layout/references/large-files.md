# Large files

Read this when adding a file above 10 MB, or a source file the build does not need, to a Unity
repository.

| Rule | Detail |
| --- | --- |
| Where | `Assets/LargeFiles/`, mirroring the path the file would have had |
| Not imported | Files Unity must not import sit under `Assets/LargeFiles/Source~/`; Unity skips a folder ending in `~` |
| Git | The folder's content is ignored; its `README.md` is tracked |
| Backup | The owner copies the folder by hand, `.meta` files included, since they hold the GUIDs |
| Inventory | `docs/reference/LARGE_FILES.md` lists every file with its size and hash, so a clone can tell what it lacks |
