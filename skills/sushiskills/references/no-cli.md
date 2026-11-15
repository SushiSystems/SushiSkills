# Not every project has a CLI

Read this when the repository has no CLI of its own and a rule names `<cli>`.

A CLI is for a complex project: several modules, its own toolchain, a runtime search path to set up.
A web application driven by its package manager, or a Unity project driven by the editor, does not
need one, and none is built for it. The rules that name `<cli>` then read as follows:

- Build, test and run go through the project's own scripts (`npm run`, the editor), and nothing is
  called behind them.
- The backlog and the design are read with the module form of the same commands, which the tooling
  role of the company layer names.
- The checkers under `tools/` run directly.
- A Unity project follows `unity-project-layout` for its tree and does not carry the C++ and Python
  module rules that assume a CLI.

Adding a CLI to a project that has none is the owner's decision.
