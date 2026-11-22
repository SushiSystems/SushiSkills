# File formats: example and red flags

Read this when writing a new format's first file or tempted to skip a version step. `../SKILL.md` holds the rules.

## Example

```json
{
    "format_version": 3,
    "asset_id": "terrain/coast_tile",
    "tile_size_metres": 512
}
```

## Red flags

- "It is only a cache, it does not need a version." → it needs one; a stale cache is a bug.
- "I renamed the key; old files will just use the default." → a version step that maps the old key.
- "Unknown version, but it looks close enough to read." → refuse it.
