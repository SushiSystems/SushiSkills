# Dispatch block

You are a subagent. These rules hold for this whole task, on top of the task itself.

1. Invoke the `sushiskills` skill and follow its doctrine: the boundaries, SOLID first, without
   exception; the defaults unless their "not when" line applies.
2. Before writing any prose (a comment that explains, a commit message, a report, a reply),
   invoke the `humanizer` skill and apply its rules in the language of the prose.
3. Do not start any process that runs `se`, `cmake`, `ninja` or `ctest`, in the foreground or
   the background, and do not write or edit any build configuration file.
4. Write only to the files the task lists and to the work folder under `docs/agent/`.
5. Report what was done and what was not. Paste the output of every verification you claim.
6. Before reporting, syntax-check what you wrote without building: C++ through
   `compile_commands.json` with `clang -fsyntax-only`, GLSL through `shader_compiler.exe`.
   Paste the command and its output.
7. Write scratch only to the scratchpad, never binaries or copies, under 100 MB; delete what you
   made and report the scratchpad size (`storage-discipline` skill).

The first line of your report is exactly:

`dispatch block read: amber-kettle-7`

A report without that line is returned unread.
