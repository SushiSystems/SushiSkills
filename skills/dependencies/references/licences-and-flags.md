# Dependencies: licence table and red flags

Read this when a licence question comes up, or when a red flag applies. The other rules are in
`../SKILL.md`.

## Licences

| Licence | Decision |
| --- | --- |
| MIT, BSD, Apache-2.0, Zlib, ISC, public domain | Accepted |
| A repository of the same organisation, under its own licence | Accepted |
| LGPL | Only linked dynamically, and only after asking |
| GPL, AGPL, SSPL | Rejected |
| Third-party non-commercial, source-available, field-of-use limits | Rejected |
| Vendor SDK licences that require marks, notices to the vendor, or restrict redistribution | Rejected |

## Red flags

- "It is header-only, so it is not really a dependency." → it is.
- "The licence is probably MIT." → read it.
- "It is simpler to expose its type in our header." → wrap it.
