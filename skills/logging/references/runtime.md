# Logging: levels, records, sinks and hosts

Read this when you set a level from the environment or in code, write or replace a sink, read a
record's fields, or join the logger to a host's own logging system. The rules are in
`../SKILL.md`.

## Levels, with examples

| Level | Example |
| --- | --- |
| `TRACE` | Every node visited in one graph pass |
| `DEBUG` | Chosen memory tier and its size |
| `INFO` | Device opened, world loaded, 1842 assets cooked |
| `WARN` | Share refused, falling back to a host copy |
| `ERROR` | Asset file unreadable |
| `FATAL` | Device lost with no recovery path |

## Setting the level

Each project's `<PREFIX>_LOG_LEVEL` sets the levels of that project's categories at the first
log call, and touches no other project's. It takes a level for all of them, then any number of
`module=level` pairs, in any case:

```
AC_LOG_LEVEL=off
BX_LOG_LEVEL=warn,autograd=trace
```

These two lines silence one project and follow one module of another, in the same process. A
value the logger cannot read is reported once on stderr, and that project's levels stay at
`WARN`. In code, `set_log_level(project, level)` sets one project and
`set_log_level(category, level)` sets one category. A call made before the first log call wins
over the environment.

## Record

Example of a record:

```
[12:04:31.207] [WARN] [acme.memory] [t3] [usm_allocator.cpp:88] share refused for 64 MiB on device 1; falling back to a host copy
```

The fields are local time to the millisecond, the level, the project and module of the
category, the thread and the file and line of the call. The thread is a small number the logger
gives each thread on its first record, so one thread's records can be followed through the log.
The sink receives every field apart, so a program can send one project's records to their own
file and a host can file each field where its own logging system keeps it.

## Sink

| Rule | Detail |
| --- | --- |
| Default | One write per record, flushed |
| Replacing | `set_log_sink(sink)`; an empty sink restores stderr |
| Thread | Applications deliver from one logger thread. Tests switch to synchronous delivery, which first waits for the queue, so records arrive in order |
| Queue | Bounded. A record that finds it full is dropped and counted, and the next record delivered is preceded by a `WARN` naming how many were dropped |
| Failure | A sink that throws loses nothing: the logger writes the exception and the record to stderr |
| `FATAL` | Delivered on the calling thread after the queue is drained, then flushed, before the process ends |
| Exit | The logger is never destroyed, so a call is valid during static initialisation and process exit. At static destruction it stops its thread and delivers what is queued. A process ended without static destruction loses its queue |

## Meeting another logger

A process can hold a logging system besides the logger: the host's own, as in a game engine, a
Python program or a game with a logging library, or a plug-in's private copy of the logger. The
program joins them at start-up, before its first log call, so one of them writes everything.

| Host | Join |
| --- | --- |
| Its own logging system, in C++ | It sets the logger's sink to one that hands each record to its system |
| Its own logging system, outside C++ | The same, through the logger's C interface |
| A host that wants its records in the logger's stream | It writes them through the logger's forwarding sink |
| A plug-in with a private logger | The plug-in sets its sink to the host's, as either row above |

A sink that belongs to a host is delivered on the calling thread, so the host sees records in
the order they were made.

## Python

| Part | Rule |
| --- | --- |
| Levels | `TRACE` is registered as level 5 and `FATAL` is `CRITICAL` |
| Configuration | `<PREFIX>_LOG_LEVEL` is read the same way as above |
| Record | The same line |
