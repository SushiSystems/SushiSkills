# API stability: excuses

Read this when you think a change to a public surface is harmless. The rules themselves are in
`../SKILL.md`.

## Excuses

- "Nobody outside this module calls it." → check the repositories above before calling it private.
- "I will keep the old function as well, just in case." → deprecate and forward, then remove.
- "Point the dependency at main until the release is out." → release first.
