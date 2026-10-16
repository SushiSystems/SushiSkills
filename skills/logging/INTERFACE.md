# Logger interface

Every Sushi logger offers this interface, in its project's namespace and with its project's
export macro, so that any two of them, or one and a host, join the same way. `SKILL.md` holds
the rules; this page holds the types and what each call does.

## Values

```cpp
enum class LogLevel : std::uint8_t { Trace = 0, Debug = 1, Info = 2, Warn = 3, Error = 4, Fatal = 5, Off = 6 };

class LogProject
{
public:
    constexpr LogProject(std::string_view name, std::string_view level_variable) noexcept;
    constexpr std::string_view name() const noexcept;
    constexpr std::string_view level_variable() const noexcept;
};

class LogCategory
{
public:
    constexpr LogCategory(LogProject project, std::string_view module) noexcept;
    constexpr LogProject project() const noexcept;
    constexpr std::string_view module() const noexcept;
};

constexpr LogCategory make_log_category(LogProject project, std::string_view module) noexcept;
```

Source: not compiled

The numbers of `LogLevel` are part of the C interface below and never change. A project and a
category hold views of string literals, so both are `constexpr` and live for the whole process.

## Record

```cpp
struct LogRecord
{
    LogLevel level;
    std::string_view project;
    std::string_view module;
    std::string_view file;
    std::uint32_t line;
    std::uint32_t thread;
    std::int64_t time_ns;
    std::string_view message;
    std::string_view text;
};
```

Source: not compiled

| Field | Holds |
| --- | --- |
| `file`, `line` | The call site; `file` is the file name without its folders |
| `thread` | The sending logger's number for the calling thread |
| `time_ns` | System clock time of the call, in nanoseconds since the Unix epoch |
| `message` | The formatted message alone |
| `text` | The whole line of `SKILL.md`'s "Record" |

Every view is valid only during the sink call.

## Calls

| Call | Does |
| --- | --- |
| `void set_log_level(LogProject, LogLevel)` | Sets every category of one project |
| `LogLevel log_level(LogProject)` | Returns the level of a project's categories that no module setting overrides |
| `void set_log_level(LogCategory, LogLevel)` | Sets one category |
| `LogLevel log_level(LogCategory)` | Returns one category's level |
| `using LogSink = Delegate<void(const LogRecord&), 48>` | The callable that receives each record |
| `void set_log_sink(LogSink)` | Replaces the sink; an empty sink restores stderr |
| `void set_log_synchronous(bool)` | `true` waits for the queue, then delivers each record on the calling thread |
| `LogSink log_forward_sink()` | Returns a sink that enters another logger's record into this logger's queue |

A project's level variable is read the first time one of its categories is used.

## Forwarding

A record entering through `log_forward_sink()` passes no level gate of the receiver, because the
sender has already applied its own. The receiver keeps `time_ns`, ignores the sender's `thread`
and `text`, numbers the calling thread and writes the line itself, and queues the record as if
the call had been made to it.

Joining a sender to a receiver is two calls on the sender, made at start-up:

```cpp
SushiDSP::set_log_synchronous(true);
SushiDSP::set_log_sink(SushiRuntime::log_forward_sink());
```

Source: not compiled

The receiver is never destroyed, so a sender may forward during process exit.

## Compile-time ceiling

A front computes the ceiling of `SKILL.md`'s "Two gates" in its own translation unit, from
`NDEBUG` and its `<PREFIX>_ENABLE_LOGGING`, through a function with internal linkage
(`static constexpr`). An `inline` function whose body reads `NDEBUG` would differ between
translation units and break the one-definition rule.

## C interface

A host outside C++ joins through one C call per logger, named with the project's lowercase
prefix.

```c
typedef struct SushiLogRecord
{
    uint32_t size;
    uint8_t level;
    const char* project;  size_t project_size;
    const char* module;   size_t module_size;
    const char* file;     size_t file_size;
    uint32_t line;
    uint32_t thread;
    int64_t time_ns;
    const char* message;  size_t message_size;
    const char* text;     size_t text_size;
} SushiLogRecord;

typedef void (*SushiLogSinkFunction)(const SushiLogRecord* record, void* user);

void sr_set_log_sink(SushiLogSinkFunction function, void* user);
void sr_set_log_synchronous(int synchronous);
```

Source: not compiled

`size` is `sizeof(SushiLogRecord)` of the logger that filled it; a later version only adds
fields at the end, and a host reads only the fields its own `size` covers. Strings are not
NUL-terminated. A null `function` restores stderr. The function must not throw or unwind into
the logger.
