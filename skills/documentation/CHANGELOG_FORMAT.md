# Changelog format

Read from the `documentation` skill before writing a changelog entry or cutting a release.

One file, `docs/reference/CHANGELOG.md`, grouped by release, newest first.

```
# Changelog

## Unreleased

- 2026-09-15 — matter: Reserved the neighbour list at tick start (`neighbour_list.hpp`).
- 2026-09-14 — interop: Logged every refused share (`interop_share.cpp`, `ShareGate`).

## v0.3.0 — 2026-09-01

- 2026-08-28 — render: Fixed the star field's exposure (`star.vert`, `StarPass`).
```

| Part | Rule |
| --- | --- |
| Headings | `## Unreleased` on top, then `## vX.Y.Z — YYYY-MM-DD` per release, the heading being the tag |
| Entry | `- <YYYY-MM-DD> — <scope>: <Past-tense verb> <what changed> (<where>).` |
| Scope | The commit scope, so one module's history is one search |
| Where | At most five backticked files or symbols |
| Order | Newest first inside each section |
| Length | At most 240 characters, one sentence, no nested bullet, never why |
| Breaking change | The entry names what breaks, e.g. "cli: Removed the --legacy flag" |

A change that needs more than five places is more than one entry.

**Release.** When a version ships, `## Unreleased` is renamed to `## vX.Y.Z — YYYY-MM-DD` and a
new empty `## Unreleased` opens above it. The live file keeps `Unreleased` and the latest
release; every older release section is deleted, and the tag of its release holds the file as it was.
When and how a release is cut is in `versioning-and-release`.

