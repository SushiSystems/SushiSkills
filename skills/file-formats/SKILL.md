---
name: file-formats
description: Use when defining, reading, writing or changing a persistent file format - JSON, TOML, YAML, a binary asset, a save file, a cache or a manifest - in a Sushi Systems repository.
---

# File Formats

A file outlives the code that wrote it. Every persistent format says which version it is, and
every reader knows what to do with every version it meets.

## Rules

1. **Keys are `snake_case`** in JSON, TOML and YAML.
2. **Every persistent file carries `format_version`**, an integer, at its top level or in its
   binary header.
3. **One module owns each format**: it defines the schema, the reader and the writer. Other
   modules go through it.
4. **Readers upgrade.** A reader accepts every older version it has ever shipped and upgrades it
   in memory, one version step at a time, each step its own function.
5. **Readers refuse the unknown.** A version newer than the reader knows is rejected with a status
   naming both versions; it is never read as the newest known one.
6. **Writers write only the current version.**
7. **A change to a format is breaking** for `versioning-and-release`, and bumps `format_version`.

## Binary formats

- Open with a four-byte magic, then `format_version`, then a byte order marker or a fixed,
  documented byte order.
- Every field has a fixed size and alignment written in the owning module's `README.md`.
- Never write a struct's memory directly; serialise field by field.

## Documentation

The owning module's `README.md` holds the current schema and a table of versions: each version,
the release it shipped in, and what changed.

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
