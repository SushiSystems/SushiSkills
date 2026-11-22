# Project tools: the backlog fact check

Read this before a backlog migration, or when the owner asks for a fact check. The rules are in
`../SKILL.md`.

`check_backlog.py` sees the shape of an entry, not whether it is still true. The fact check
reads every entry of `docs/backlog/`, with its detail file, and every design document whose
status is `Open`:

1. Read the code and the files the entry names.
2. Search `git log` since the entry's last change for a commit that closed it.
3. Give one verdict: true, stale (true in part; say which part), closed, or foreign (closed by a
   commit in another repository; name it).

The verdicts go in the `REPORT.md` of the work folder that ran the check.
