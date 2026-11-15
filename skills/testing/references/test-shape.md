# Testing: what a test is and the forbidden kinds

Read this when writing or reviewing a test, to check its shape against the definition and the
forbidden kinds. The rules are in `../SKILL.md`; `../REVIEWING.md` turns them into verdicts.

## Why tests matter

A test is the only part of the code that says what the code promises. When someone changes the
engine a year from now, the tests are what tell them whether they broke it. A good test fails
exactly when a promise is broken, says which one, and costs milliseconds. A bad test fails for no
reason, passes when the code is wrong, or costs seconds, and every one of those teaches the people
who run it to stop reading test results. A suite of ten thousand tests nobody trusts is worth less
than a suite of five hundred everyone does. Write the test that a reviewer would be sorry to lose,
and no other.

## What a test is

A test checks one promise of a public interface, against a named oracle, at the smallest size that
can see the promise, and fails when the promise is broken.

- **Promise.** A behaviour, not a function: what the unit guarantees to do with given inputs in a
  given state. One function holds several promises, and one promise can span several functions. The
  promises of a unit are found by the procedure in `../REVIEWING.md`, not recalled.
- **One when.** The test sets up a state, does one thing, and checks what that one thing promised:
  given, when, then. A second action is a second test. The name states the promise as a sentence,
  `GemmWithBetaZeroIgnoresNanInC`, not `SimpleGemm`. An "and" joining two results that can break
  apart is two tests; one that states a single outcome, such as `RefusesAndLeavesNothingBehind` for an
  all-or-nothing refusal, is one. A name
  that cannot say which defect it catches means there is no test. It starts with the unit it tests,
  so a failing name leads to its file.
- **Oracle.** Where the expected value comes from. It never comes from running the code under test.
  `oracles.md` lists the kinds.
- **Can fail, for the right reason.** It fails when the promise breaks: a new test kills at least one
  mutant of the code it tests, or reproduces the defect its commit fixes. It does not fail when only
  the inside of the unit changes; a test that breaks on a refactor checks how, not what.
- **Public interface.** Private details are not tested directly. A private function that seems to
  need its own test is a brick that wants its own module.
- **Straight line.** No `if`, loop or `try` in the body outside a row table, including a loop that only
  builds the input or the expected value; a row table or a builder named for what it builds holds it. A loop that only advances simulated time, with
  no check inside it, is a helper named for it, such as `run_for(ticks)`, and the call is straight. Setup may repeat
  between tests when that lets a reader see cause and effect without opening a helper.

Every test answers five questions, and an empty answer is a verdict: which promise, which oracle,
which defect it catches, why this size, and why it is not a row of a sibling. `../REVIEWING.md`
turns the answers into the verdicts a review gives.

A helper that asserts is named `expect_*` or `assert_*` (`expect*` or `assert*` in TypeScript), so a
checker can tell an assertion from a call. A project macro counts when its name opens with `EXPECT`
or `ASSERT`.

## Forbidden tests

Never written. The rework of an old suite deletes or rewrites each one it meets.

| Kind | Example |
| --- | --- |
| No assertion, or only `SUCCEED()`, a `static_assert` run as a test, `EXPECT_NO_THROW` around code that cannot throw | `flush(); SUCCEED();` |
| An assertion on a literal, or a value compared with itself | `EXPECT_TRUE(true)` |
| Printing or logging in place of asserting | `print(result)` |
| A sleep or a wall-clock wait, to synchronise or to prove that something did not happen | `std::this_thread::sleep_for(50ms)` |
| A bare tolerance literal in any comparison with a tolerance, whatever the types compared | `EXPECT_NEAR(a, b, 1e-5)` |
| A `small` test that reaches what its size forbids | a device queue in `Small_` |
| A private header, a `Detail::` symbol or a `_private` name | `#include ".../source/x.hpp"` |
| Control flow in a test body, outside a row table | `if (device) { EXPECT_... }` |
| A mock, stub or replacement of a type or function the repository owns, made by the test or by a fixture it uses, including a fixture closure that implements a port by hand | mocking the module's own class, patching its own `run_tests` |
| A test of trivial code: a getter, a default value, a constant, a log category, a version string | `EXPECT_EQ(kCategory, "Blas")` |
| A change detector: asserting how the code works rather than what it promises | asserting the order of internal calls |
| An expected value pasted from the code's current output | a golden array nobody derived |
| The same promise again at a larger size or in another file | `SimpleAxpy` beside the reference axpy test |

A value of a plain data type built by hand is not a stand-in; a builder named for it is preferred. A
`static_assert` check is not a test: it sits in a compile-only translation unit, `compile_<name>.cpp`
beside the unit's test file, that the build compiles and the test runner never lists. A header with no
runtime promise has that file in place of a test file.

An expected value pasted from current output is allowed only in a test whose suite opens with
`Characterization_`, written to pin behaviour before a refactor, with a backlog entry that removes it. In
C++ its size follows the word: `Characterization_Medium_ThreadExit`.
