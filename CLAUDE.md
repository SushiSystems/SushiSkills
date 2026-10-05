# Agent instructions

This repository holds the Sushi Systems skills. It follows them itself.

Load before working here: `sushiskills`, `documentation`, `humanizer`, `commits`,
`source-comments`, `python-code-style`, `project-tools`.

A rule lives in one file; see `docs/CONTRIBUTING.md` before changing one.

Check before reporting work as finished:

```
python tools/documentation/check_source_comments.py .
python tools/documentation/check_docs_layout.py .
python tools/documentation/check_changelog.py .
python tools/layering/check_layering.py .
python -m unittest discover -s tools/tests
```
