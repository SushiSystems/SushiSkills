# KI-2 The release tags exist only on this machine

The row of this entry is in `docs/backlog/RELEASES.md`. This file holds what did not fit the row.

- Origin: own
- Where: `docs/reference/CHANGELOG.md`
- Cause: the tags were created and never pushed
- Recognise: `git ls-remote --tags origin` lists neither `v0.1.0` nor `v0.1.1`
- Workaround: a clone has no tags; check out the release commit by its hash
- Fix: RW-4
