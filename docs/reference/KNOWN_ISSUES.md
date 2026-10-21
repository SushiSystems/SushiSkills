# Known issues

Next id: KI-3

## Releases

### KI-2 The release tags exist only on this machine
- Origin: own
- Where: `docs/reference/CHANGELOG.md`
- Cause: the tags were created and never pushed
- Recognise: `git ls-remote --tags origin` lists neither `v0.1.0` nor `v0.1.1`
- Workaround: a clone has no tags; check out the release commit by its hash
- Fix: RW-4
