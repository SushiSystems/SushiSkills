# SOLID

Read this to apply boundary 1 of `../SKILL.md`. A unit is a function, a class, a file or a
module. Other files name these rules "SOLID" or "the unit rules of `sushiskills`" and link here.

## Single responsibility

A unit has one reason to change.

Correct: `check_skill_budget.py` counts words in `rule_word_budget`; reading files is
`read_files` in `checking/source_file.py`.

Violation, and its fix:

```python
def check_budget(root):                       # violation: finds files, reads them and checks
    for path in root.rglob("SKILL.md"):
        text = path.read_text(encoding="utf-8")
        if len(text.split()) > 800:
            print(path)
# fix: collect() finds the files, read_files() reads them, rule_word_budget() checks one skill
```

## Open/closed

A unit gains a new behaviour through new code, without editing its existing code.

```python
rules = {
    "rule_word_budget": rule_word_budget,
    "rule_ceiling_follows": rule_ceiling_follows,   # a new rule is one new row
}
```

Violation: `if name == "word_budget": ... elif name == "maximum": ...` inside the runner, edited
for every new rule. Fix: move each branch into its own `rule_<what>` function and register it
in the table above.

## Liskov substitution

A unit that implements an interface can replace any other implementation of it, and callers
keep working.

```cpp
class Sink { public: virtual ~Sink() = default; virtual void write(std::string_view line) = 0; };
class FileSink final : public Sink { public: void write(std::string_view line) override; };
class MemorySink final : public Sink { public: void write(std::string_view line) override; };
```

Violation: `MemorySink::write` throws when its buffer is full, while callers of `Sink` expect
`write` to return. Fix: give `MemorySink` the same contract (drop the oldest line, or grow), or
do not make it a `Sink`.

## Interface segregation

A caller depends only on the functions it calls.

```cpp
class Reader { public: virtual ~Reader() = default; virtual std::string read() = 0; };
class Writer { public: virtual ~Writer() = default; virtual void write(std::string_view) = 0; };
void load(Reader& source);            // needs read() only
```

Violation: `void load(Storage& source);` where `Storage` declares `read`, `write`, `remove` and
`list`, so every test of `load` must implement all four. Fix: split `Storage` into `Reader` and
`Writer` and pass `load` a `Reader`.

## Dependency inversion

A unit depends on an interface, not on a concrete type.

```python
from typing import Protocol

class Sink(Protocol):
    def write(self, line: str) -> None: ...

def report(sink: Sink) -> None:     # correct: any object with write() is accepted
    sink.write("done")
```

Violation: `def report(path): FileSink(path).write(...)`, which ties `report` to the file
system. Fix: `def report(sink: Sink): sink.write(...)`; the caller passes a `FileSink`, a test
passes a `MemorySink`.

## Units of one kind have the same shape

Units that do the same kind of job are built the same way, so a reader who has read one checker
can find the rule table of any other. In this repository every checker under `tools/` has one
`rule_<what>` function per rule, each taking one collected item and yielding `Issue` values, and
one row per rule in the `rules` table of its `Checker`. `tools/skills/check_skill_budget.py`:

```python
K_CHECKER = Checker(
    description="Checks that every SKILL.md stays within the skill word budget.",
    collect=collect,
    rules={"rule_word_budget": rule_word_budget, "rule_ceiling_follows": rule_ceiling_follows},
)
```

A checker that prints its findings from a `main()` loop instead has a different shape and is a
breach.

## An unneeded dependency

A dependency is unneeded when it is an import, an include or a link edge that no code path
uses, or when the function it supplies is already supplied by an existing unit.

```python
import os                    # unneeded: nothing in the file calls os
from pathlib import Path
```

```cmake
target_link_libraries(core PRIVATE fmt)   # unneeded when no file of core includes <fmt/...>
```

It is removed. When it is the owner's (an external dependency, a module edge), it is reported
with its file instead.
