# The root README

Read this when writing or reshaping a repository's root `README.md`.

The root `README.md` is the front page: each line answers a question a cold reader has, and
everything else is a link into `docs/`. Its sections, in this order, none of them empty:

1. `# <Project>`, then one sentence: what it is and who it is for. Two CI or licence badges at
   most, on the line under the title.
2. The smallest real use: for a library, code under the example rule of "Size and one home" in
   `SKILL.md`; for a tool, the commands a user types.
3. `## Build`: the commands that build and test it, one block.
4. `## Status`: what works and what does not yet, in a few lines, linking
   `docs/backlog/README.md`.
5. `## Documentation`: a link to `docs/README.md`; `docs/CONTRIBUTING.md` for contributors.
6. `## Licence`: the licence by name, `LICENSE`, and `COMMERCIAL.md` and `NOTICE.md` where they
   exist.

A repository with no code to show, such as SushiSkills, replaces section 2 with a table of
where things are. Not on the page: a table of contents, emoji headings, a feature bullet list,
adjectives such as fast, powerful or seamless, and anything the manual already says.

`CONTRIBUTING.md` is `docs/CONTRIBUTING.md`; GitHub finds it there. `SECURITY.md` and
`CODE_OF_CONDUCT.md` sit under `.github/`, as `repository-layout` says.
