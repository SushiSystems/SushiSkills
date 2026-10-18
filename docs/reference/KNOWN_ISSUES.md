# Known issues

Next id: KI-3

## Releases

### KI-1 The archived v0.1.0 changelog misses commits
- Origin: own
- Where: `docs/archive/changelog/v0.1.0.md`
- Cause: unknown
- Recognise: six entries for the fourteen commits before the release commit; the commits that
  added the initial skill set and the TypeScript code style have none
- Workaround: read `git log v0.1.0` for the full history
- Fix: none, the archive is frozen

### KI-2 The release tags exist only on this machine
- Origin: own
- Where: `docs/archive/changelog/v0.1.0.md`, `docs/reference/CHANGELOG.md`
- Cause: the tags were created and never pushed
- Recognise: `git ls-remote --tags origin` lists neither `v0.1.0` nor `v0.1.1`
- Workaround: a clone has no tags; check out the release commit by its hash
- Fix: RW-4
