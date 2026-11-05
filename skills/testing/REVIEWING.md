# Reviewing tests

How the promises of a unit are found, what a good test and a bad one look like, and how a review
gives every existing test one verdict. Two reviewers who follow this page on the same test reach the
same verdict; where they do not, the page is wrong and is fixed.

## Finding the promises

The promise list of a unit is derived, not recalled, so that two people derive the same list. Work
from the public header or the module's public names, with the code closed.

1. **Contracts first.** For each public function, write what its documentation or its types
   guarantee: the result for valid input (postcondition), the error for invalid input
   (precondition), and what holds after every call (invariant). Each is a promise.
2. **Categories.** For each parameter and each condition of the state it runs in, list the
   categories of value that the contract treats differently: empty and not, aliased and not,
   finite and NaN, on the device and on the host. Combinations the contract rules out are dropped.
3. **Boundaries.** At each limit, take the value on it and the one just off it: 200 and 199 for
   `score >= 200`. A count takes zero, one and many.
4. **Properties.** Name the property shape that fits the unit, if one does: round trip, invariant,
   comparison with an independent oracle, metamorphic relation, idempotence. A property replaces a
   table of examples over the same promise.
5. **Between units.** A promise that two units make together, such as a writer and its reader, is
   listed once, on the unit that owns the format.

Each promise is one row:

```
<unit>: <promise as a sentence> | <oracle> | <size>
tensor_shape: a negative extent is rejected with InvalidShape | contract | small
gemm: beta zero ignores NaN in C | contract | small
gemm (device): the kernel matches the host reference within tolerance | host reference | medium
```

A row with no test is a gap. A test with no row is a candidate for deletion.

## A good test and a bad one

```cpp
TEST(Small_Gemm, BetaZeroIgnoresNanInC)
{
    // Given C filled with NaN, which beta zero must not read.
    Matrix<float> a = Matrix<float>::identity(2);
    Matrix<float> b = {{1.0f, 2.0f}, {3.0f, 4.0f}};
    Matrix<float> c = Matrix<float>::filled(2, 2, kNan);

    // When C is overwritten with beta zero.
    gemm(a, b, c, /*alpha=*/1.0f, /*beta=*/0.0f);

    // Then C holds A times B and no NaN.
    expect_matrix_eq(c, b);
}
```

One promise, named as a sentence. The oracle is the contract: with A the identity, the result is
B, which anyone can check by hand. It runs on the host in microseconds. It kills the mutant that
reads C when beta is zero, and it survives any rewrite of how `gemm` is computed.

```cpp
TEST(Medium_Gemm, SimpleGemm)
{
    Device device;                              // a device made in the test
    Queue queue(device);
    for (int n : {1, 7, 64, 513})               // a loop instead of rows
    {
        auto a = random_matrix(n, n);           // unseeded input
        auto b = random_matrix(n, n);
        auto c = random_matrix(n, n);
        gemm(queue, a, b, c, 1.0f, 0.5f);
        queue.wait();
        EXPECT_NEAR(c(0, 0), c(0, 0), 1e-5);    // compared with itself, bare tolerance
        print(c);                               // printing as if it checked something
    }
    std::this_thread::sleep_for(10ms);          // waiting for nothing
}
```

The name says no promise, so no reviewer can tell what it protects. It makes a device, loops, draws
unseeded input, compares a value with itself under a typed epsilon, prints, and sleeps. No mutant of
`gemm` makes it fail, and it costs the device start-up on every run. Its verdict is delete; if the
device promise has no other test, the host-reference test in the rows above replaces it.

## Signs of a long test

Each sign is countable. A sign sends the test to the questions below; it is not a verdict by itself.
A sign about size is answered at question 8, every other sign at question 7.

| Sign | Points at |
| --- | --- |
| More than one action under test, or a check between two actions | Two tests |
| The name needs "and", or names a feature rather than a promise (`Simple`, `Basic`, `Works`, `Full`, `Smoke`) | No stated promise |
| Setup longer than the action and the checks together | A missing builder, or a test at the wrong size |
| Assertions about different results of different calls | Several promises in one test |
| A loop over sizes or inputs in the body | Rows |
| A device, file, thread or clock in a test of logic: logic is anything decided on values, including what a thread computes; handing a value between threads, a kernel matching its host reference and bytes reaching a file are boundaries | Question 8 |
| A fixture field this test does not use | A general fixture that hides the cause |
| A test slower than its size's limit | Question 8 |

No published study gives a line count for a test, and this page gives none.

## The verdict

"Elsewhere" and "another test" mean any test of the same module. The reviewer reads the whole test
file, searches the module's other test files for the unit's name, so that sibling tests are seen, and the test's fixture, its
helpers and the public code it calls; a question
the test alone cannot answer is answered from them, never guessed. The questions are asked in this
order, and the first answer that gives a verdict ends the review of that test.

| # | Question | If the answer is | Verdict |
| --- | --- | --- | --- |
| 1 | Is it one of the forbidden kinds of `SKILL.md`? | yes, and its promise is tested elsewhere or it states none | **delete**, naming the kind |
| | | yes, and it is the only test of a real promise, or the copy in the unit's own test file | **rewrite**, naming the kind |
| 2 | Would it fail if its promise broke? | no | **delete**, or **rewrite** when its promise has no other test |
| 3 | Can its promise be said as one sentence from the name and body? | no, there is none | **delete** |
| | | no, there are several | **split**, one test per promise |
| 4 | Does another test check the same promise? | yes, and this one is the larger copy, or sits outside the unit's own test file while the other is in it | **delete** this one |
| | | yes, and neither is in the unit's own test file | **rewrite** the fuller one into the unit's own test file, **delete** the other |
| | | yes, with other inputs | **merge** them into rows |
| 5 | Would it fail when only the inside of the unit changes? | yes | **rewrite** against the public promise |
| 6 | Is its oracle the code under test, or a value pasted from its output? | yes | **rewrite** with a named oracle, or **characterize** with a backlog entry |
| 7 | Does a sign other than a size sign remain? | yes | **rewrite** |
| 8 | Is its size the smallest that sees the promise? A decision made on values is seen small. A test that reaches it through a process-wide instance, a device, a file, a thread or a clock is not the smallest, also when the public code offers no other door: that door is the missing seam | no | **resize**, building the seam first when only a larger size can see logic |
| | Does it touch only what its size allows, and leave nothing behind? | no, and the size is right | **rewrite** |
| 9 | None of the above | | **keep** |

Each promise row with no test after the review gets one: **add**.

## The record

Every reviewed test gets one line in the work folder's report:

```
<file>::<test> | <verdict> | <question #> | <promise row, or the reason> | <files read>
tests/test_gemm.cpp::Medium_Gemm.SimpleGemm | delete | 1 | sleep; self-comparison; device in a logic test | tests/test_gemm.cpp
```

A verdict at question 2, 4, 5 or 8 names the files that answer it: the sibling tests for 4, the
public code for 2, 5 and 8. A record without them is sent back.

A worker applies the verdicts. A deletion carries its question and reason, as `SKILL.md` asks.

## Measuring agreement

Studies find that people judging the same tests disagree about half the time, so agreement is
measured, not assumed. Before a repository's review starts, two reviewers who see only this page and
`SKILL.md` give verdicts on the same sample of its tests, at least twenty from different modules.
Each test where the two verdicts differ is read against this page: the page is made clear where it
allowed both answers, and the sample is run again until the verdicts agree.
