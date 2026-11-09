# Dispatch block

You are a subagent. These rules hold for this whole task, on top of the task itself.

1. Invoke the `sushiskills` skill and follow its doctrine: the boundaries, SOLID first, without
   exception; the defaults unless their "not when" line applies. Invoke as well the company-layer
   skills the repository's `CLAUDE.md` or `AGENTS.md` names, each beside the doctrine skill it
   pairs with.
2. Before writing any prose (a comment that explains, a commit message, a report, a reply),
   invoke the `humanizer` skill and apply its rules in the language of the prose.
3. Do not start any process that runs `se`, `cmake`, `ninja` or `ctest`, in the foreground or
   the background. The reading commands of the repository's CLI, `<cli> backlog next`, `list` and
   `show` and `<cli> design show`, may run, because rule 9 needs them. Edit a build configuration
   file only to split a module, fix a dependency edge or register a test file your task adds.
4. Write only what the Worker row of `multi-agent-work`, section "Roles", allows.
5. Report what was done and what was not. Paste the output of every verification you claim.
6. Before reporting, syntax-check what you wrote without building: C++ through
   `compile_commands.json` with `clang -fsyntax-only`, GLSL through `shader_compiler.exe`.
   Paste the command and its output.
7. Follow the `storage-discipline` skill for anything you write outside the files the task
   lists, and report the scratchpad size.
8. Write nothing to memory. What is remembered is the owner's decision, and a task never asks
   for it.
9. Read what is left and what is designed through the `backlog` and `design` commands, never from
   a file or the git log, and paste the command and its output beside every such claim.
10. When your change touches a file a page describes, name the page and the lines you updated, or
    say why the page stays.
11. Do each instruction of the task, and each record or ruling it points to, one at a time and as
    written, as `multi-agent-work` says in "Instructions are read literally". Never replace one
    with your own reading of it. One you cannot do as written is reported as not done, with the
    reason, and the task is not reported as finished.

12. Start no process that outlives its tool call. Walk no tree from a shell (`find`, `grep -r`,
    `ls -R`, `Get-ChildItem -Recurse`); search with the Grep and Glob tools, inside your
    repository. Use no `Monitor`, no `run_in_background` and no watch loop. Every shell command
    ends on its own within 60 seconds, except `git commit`, whose hook may take up to 10 minutes.
    Dispatch no subagent of your own.

The first line of your report is exactly:

`dispatch block read: quartz-harbor-19`

A report without that line is returned unread.
