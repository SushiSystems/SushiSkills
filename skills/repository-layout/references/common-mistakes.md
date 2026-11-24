# Common mistakes

Read this when a file seems to have no obvious location, or when reviewing where something was put.

| Mistake | Fix |
| --- | --- |
| A `utils/` or `common/` module | Name the responsibility; split it by what each part does |
| A `testing/` or `test_support/` module for shared test code | The same: `test_runner`, `fake_audio_device`, each in the tier of what it depends on |
| A `utils.hpp` header | The same: one header per responsibility, each in the lowest module that uses it |
| Two modules of one tier sharing a header of one of them | Move the header down a tier, into a module both depend on |
| Test data beside the source | `tests/<owner>/fixtures/<name>/` |
| A `unit/`, `integration/` or `regression/` test folder | The mirror in `TESTS.md`; the kind is a label |
| A second CLI or script folder | Everything runnable goes through `cli/` or is in `tools/` |
| New top-level folder "for now" | It is not allowed; pick the location from `root.md` |
| A `samples/` or `examples/` folder in the root | `applications/examples/` |
| Test input under `assets/` | `tests/<owner>/fixtures/<name>/`; `assets/` holds what ships |
