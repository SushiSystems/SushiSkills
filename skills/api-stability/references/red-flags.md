# API stability: red flags

Read this when a change to a public surface feels harmless. The rules themselves are in
`../SKILL.md`.

- "Nobody outside this module calls it." → check the repositories above before calling it private.
- "I will keep the old function as well, just in case." → deprecate and forward, then remove.
- "Point the dependency at main until the release is out." → release first.
