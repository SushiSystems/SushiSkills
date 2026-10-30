# The backlog and design block of a repository's CLAUDE.md

Every Sushi repository's `CLAUDE.md` carries this block, with `<alias>` replaced by the CLI of the
repository (`se`, `sd`, `sr`). It gives the order of work as commands, not as a pointer to a file.

```
## Backlog and design

1. Session start: `<alias> backlog next`. Take what it gives.
2. A defect or limitation turns up: `<alias> backlog add issue ...` or `<alias> backlog add work ...`
   at once.
3. Before changing a module: `<alias> design owner <path>`.
4. Finishing: `<alias> backlog close <ID>` in the same commit, and the changelog line it prints.
   The commit message ends with `Backlog: <ID>`, or `Backlog: none (<reason>)`.
5. Once per clone: `python tools/hooks/install_hooks.py`.

State is read with these commands. It is never read from a markdown file or the git log.
```
