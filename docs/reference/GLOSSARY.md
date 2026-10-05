# Glossary

| Word | Meaning |
| --- | --- |
| Brick | A unit with one responsibility that can be detached, re-attached and rebuilt without touching its neighbours |
| Skill | One rule set in its own folder under `skills/`, loaded by an agent when its task matches the description |
| Checker | A script under `tools/` that reads a repository and reports where it breaks a skill; it never rewrites a file |
| Rule | One function in a checker, named `rule_<what>`, registered in the checker's table |
| Work folder | `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/`, holding the `SPEC.md`, `PLAN.md` and `REPORT.md` of one piece of agent work |
| Orchestrator | The session that plans, dispatches, reviews and commits a piece of work |
| Worker | An agent given one task, one file set and one acceptance criterion by the orchestrator |
| Dispatch block | The numbered lines in `claude/CLAUDE.md` that open every worker's prompt verbatim |
| Tier | A layer in a repository's module order; a module may depend only on tiers below its own |
