---
name: sushisystems-logging
description: Use in a Sushi Systems repository together with the logging skill, when adding or changing a log call, a front, a category, a level variable, a sink or a host join; SushiLog is the logger, and this skill holds its projects, types and calls.
---

# The Sushi Systems logger

The `logging` skill names roles; this page says who fills them. [`INTERFACE.md`](INTERFACE.md)
holds the types and calls.

## Rules

- SushiLog is the one logger: one shared library that every Sushi library links directly, never
  through another Sushi library; one queue, one thread, one sink per process. A plug-in a host may
  load twice links its static target (hidden symbols) and joins the host. Only SushiLog writes a
  record.
- The formatter is `SushiLog::text` (`format_text`): `{}` through `operator<<`, `{{` `}}`
  literal, no format specs. Precision, width, form or hex go through `fixed`, `general`,
  `scientific`, `hex`, `right`, `left`.
- Projects: SushiLog `SL`, SushiRuntime `SR`, SushiAI `SA`, SushiEngine `SE`; the level variable
  is `<PREFIX>_LOG_LEVEL`.
- A front holds its `LogProject`, its ceiling (`K_LOG_LEVEL_FLOOR` from `<PREFIX>_ENABLE_LOGGING`),
  its macros each on `SL_LOG_FRONT_AT`, and one category per module in
  `<module>_log_category.hpp`.
- A front never re-exports SushiLog: no alias of a SushiLog type, no `using` of a SushiLog name
  into the project's namespace, no function that only forwards (`sr_set_log_sink`). Code names
  `SushiLog::...` and `sl_...`; `set_log_sink` and `set_log_synchronous` act on the whole process.
- A host joins by setting SushiLog's sink to one that hands each record to its system, from C++
  or through the C interface, or by writing through `log_forward_sink()`. A plug-in with a private
  SushiLog sets its sink to the host's. Unity and a Python program join through the C interface.

Declaration example, front table, host table, record format: `references/detail.md`.
