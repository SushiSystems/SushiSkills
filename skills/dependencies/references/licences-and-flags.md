# Dependencies: licence table and red flags

Read this when a licence question comes up in table form, or when a red flag applies. The rules
themselves are in `../SKILL.md`.

## Why a dependency is a decision

Every dependency is a permanent cost: its licence, its build, its bugs, its upgrades. Adding one
is the owner's decision; the skill says what the agent brings to that decision and how an
accepted dependency is wired.

## Licences

| Licence | Decision |
| --- | --- |
| MIT, BSD, Apache-2.0, Zlib, ISC, public domain | Accepted |
| A repository of the same organisation, under its own licence | Accepted |
| LGPL | Only linked dynamically, and only after asking |
| GPL, AGPL, SSPL | Rejected |
| Third-party non-commercial, source-available, field-of-use limits | Rejected |
| Vendor SDK licences that require marks, notices to the vendor, or restrict redistribution | Rejected |

A dependency's own dependencies are held to the same table.

## Red flags

- "It is header-only, so it is not really a dependency." → it is.
- "The licence is probably MIT." → read it.
- "It is simpler to expose its type in our header." → wrap it.
