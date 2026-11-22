---
name: file-formats
description: Use when defining, reading, writing or changing a persistent file format - JSON, TOML, YAML, a binary asset, a save file, a cache or a manifest - in a repository.
---

# File Formats

A file outlives the code that wrote it: every persistent format names its version, and every
reader knows what to do with each version it meets. Example and red flags:
`references/detail.md`.

## Rules

1. **Keys are `snake_case`** in JSON, TOML and YAML.
2. **Every persistent file carries `format_version`**, an integer, at top level or in a binary
   header.
3. **One module owns each format**: schema, reader, writer. Other modules go through it.
4. **Readers upgrade.** A reader accepts every older version it has shipped and upgrades in memory,
   one version step at a time, each step its own function.
5. **Readers refuse the unknown.** A newer version is rejected with a status naming both versions,
   never read as the newest known.
6. **Writers write only the current version.**
7. **A format change is breaking** for `versioning-and-release` and bumps `format_version`.

## Binary formats

- Open with a four-byte magic, `format_version`, then a byte order marker or a fixed documented
  order.
- Every field has a fixed size and alignment, written in the owning module's `README.md`.
- Never write a struct's memory directly; serialise field by field.

## Documentation

The owning module's `README.md` holds the current schema and a table of every version the code
meets today: what the reader does with it (reads, migrates, rejects) and how it differs from the
current one. The release a version shipped in is in the changelog.
