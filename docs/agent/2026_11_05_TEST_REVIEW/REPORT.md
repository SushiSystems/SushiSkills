# Test review: report

**Status:** Open — every test has a verdict; the plan's jobs are next

Every test in the repository has a verdict from `skills/testing/REVIEWING.md`, reviewed on 2026-11-05 as
part of J15 (`docs/agent/2026_11_03_INDUSTRIAL_TESTING/`). The review read the code and ran nothing. Each
record names the files it read. The shared checkers' tests are reviewed here once; every other
repository holds copies of them.

## What the review found

The checker tests are in good shape: 618 of 732 are kept. The split into a pure core and a file-walking
shell (J1 to J4) left most rules testable on strings. The non-keep verdicts come from four places:

- Names joining two results with "and" that can break apart (39 splits).
- Loops over case or rule tables in a test body, which become parametrised rows.
- Small tests that patch process-wide settings: `K_BUDGET` in `test_budget`, the settings and
  `K_LICENCE` in `test_licence`.
- Tests that patch the repository's own functions: `test_check_all` (three tests on `_run_all`) and
  `test_check_backlog` (`tooling_bridge._import`, `check_backlog.load`).

## Defects and gaps the review found

- `tools/testing/test_budget.py` has a `test_` name and holds no test.
- `apply_settings` logic runs only through files.
- `check_design_format` and `check_design_topics` hand four rules to the installed sushicore;
  `ValidDocumentTest` passes when sushicore is absent.
- Rules with no test: `check_source_comments` `rule_file_header`, `rule_block_ceiling`,
  `rule_separators`, `rule_history`; `check_docs_layout` `rule_document_names`, `rule_work_folders`,
  `rule_design_ceiling`, `rule_module_readmes`; `check_layering` `rule_private_reach`.
- `copy_shared_tools.py` writes the files upstream holds and never removes one upstream dropped. Every
  other repository still holds `tools/testing/check_test_additions.py` and its test, which phase B
  removed here.

## Pages of the testing skill the review found unclear

- `REVIEWING.md` question 4: "at a larger size" means this test is the larger copy. The brief said so;
  the page does not.
- `SKILL.md` gives no size for a death test. The brief ruled medium until the owner rules.
- The order of question 1 and question 4 when a test of the forbidden kind is the copy in the unit's
  own file.
- Question 4 does not decide when both copies sit in one module and neither is in the unit's own test
  file (project-mobilerts `PosturePacksIntoAByte` and `PackedRulesKeepTheirValues`).
- Whether a fixture closure over a port, or a hand-built value of a plain data type, is a stand-in. The
  brief ruled that a value is not; the closure is open (sushiweb).
- A Unity GameObject, scene or frame and the size it gives. The brief ruled medium until the owner rules.

## Decisions

The owner delegated these decisions on 2026-11-05. Each ruling below is final for the plan; its reason follows it.

1. The four design rules live in sushicore, which owns the design format through its design commands. The checkers here call them, and `ValidDocumentTest` fails, not passes, when sushicore is absent.
2. Every ruling of this review that the testing skill does not state is written into `SKILL.md` and `REVIEWING.md` in T1: death tests and the allocation trap are medium; named epsilon constants are not typed tolerances; compile checks are not tests; a loop that only steps time is straight-line; a Unity GameObject in EditMode is small, while a scene or a frame is medium; a fixture closure over a port is a stand-in, a plain value is not; the rules for two copies of one promise; the scoped SushiLog sink in small tests.
3. The M1 record that asked for a seam passing the upstream values in is met by the existing `missing_settings(text)`, which already takes text: an M job changes no production code when a public function already reaches the promise.
4. Where an M2 record asked to stop patching a setting or a function of the repository and no parameter reached the promise, the seam is a keyword-only parameter whose default keeps the command's behaviour: `check_all.main` and `run_plan` take `run`, `check_backlog.rule_backlog` takes `load_module`, `check_source_comments.collect` and `write_license_block.main` take `licence`, `write_license_block.pending` takes `year`, `known_findings.main` takes `run_plan`, and `test_budget.evaluate` and `main` take `budget`.
5. The add "history: commits_since returns the commits it has when git cannot read the range" contradicts the function's documented contract, which stops with a message. The test keeps the contract: `commits_since` stops with a message.

## Dispatches

dispatch: J15 review, 4 chunks — haiku high, 1 round each, passed, rung 1
dispatch: M2 slice A, copy_shared_tools, test_budget, test_times_settings — sonnet medium, 30 tool calls, passed, rung 1
dispatch: M2 slice B, licence, write_license_block, known_findings, facts — sonnet medium, 22 tool calls, passed with 7 records left for a seam, rung 1
dispatch: M2 slice C, check_all, docs_follow, design_views, citation_files, layering, design_format, backlog_trailer, backlog, design_topics — sonnet medium, 44 tool calls, passed, rung 1
dispatch: M2 slice D, nineteen mechanical files — haiku high, 101 tool calls, passed, rung 1
dispatch: M2 slice E, the seams slice B left — sonnet medium, 72 tool calls over two rounds, passed after its report was sent back for skipping DISPATCH rules 1 and 2, rung 1

## Totals

| Tests | Keep | Rewrite | Resize | Split | Merge | Delete | Characterize | Add |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 732 | 618 | 44 | 16 | 39 | 7 | 8 | 0 | 26 |

Kept as they stand: 618 of 732 (84%).

## Verdicts by question

| Verdict | Question | What it means | Tests |
| --- | --- | --- | --- |
| split | 3 | no single promise | 39 |
| rewrite | 1 | a forbidden kind | 26 |
| resize | 8 | wrong size | 16 |
| rewrite | 7 | a long-test sign | 13 |
| merge | 4 | a duplicate | 7 |
| delete | 4 | a duplicate | 6 |
| rewrite | 2 | cannot fail | 4 |

## Modules

| Module | Files | Tests | Keep | Rewrite | Resize | Split | Merge | Delete | Characterize |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tools` | 47 | 724 | 617 | 43 | 15 | 36 | 5 | 8 | 0 |
| `sushisystems` | 1 | 8 | 1 | 1 | 1 | 3 | 2 | 0 | 0 |

## Records

One line per test: `file::test | verdict | question | reason | files read`.

### `sushisystems/sushisystems-tooling/tests/test_apply_settings.py`

```
ApplySettingsTest.test_appends_every_constant_the_file_lacks_and_keeps_the_rest | split | 3 | apply_to_settings appends; apply_to_settings leaves existing lines; apply_to_settings does not add a defined constant. One name, three promises | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py; tools/settings.py
ApplySettingsTest.test_the_result_is_a_python_file_with_the_values_intact | keep | 9 | apply_to_settings round-trip row. Bytes reaching a file are a boundary, so medium is the smallest size that sees the promise; oracle is tools/settings.py (K_TOOLING_PACKAGE at line 28) and the headings in apply_settings.py | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py; tools/settings.py
ApplySettingsTest.test_a_second_run_adds_nothing | resize | 8 | apply_to_settings idempotence row. The decision on values (which names are missing) reaches the file through the upstream import in missing_settings; seam: pass the upstream values and the text in | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py; tools/settings.py
ApplySettingsTest.test_the_claude_block_gets_the_alias_and_is_written_once | split | 3 | apply_to_claude keeps existing text ahead of the block; claude_block replaces <alias>; apply_to_claude returns False when present (the second call is a second action) | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py; sushisystems/sushisystems-tooling/CLAUDE_TEMPLATE.md
ApplySettingsTest.test_a_repository_without_a_claude_file_gets_one | merge | 4 | apply_to_claude creates-file row; the same promise with alias None is checked by test_a_repository_without_a_cli_gets_the_module_form_of_the_commands, which reads the file it creates. Merge into one table over alias "sx" and None | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py
ApplySettingsTest.test_the_alias_comes_from_the_manifest | rewrite | 7 | Two calls of alias_of with a state change between them (the manifest is unlinked); the check between two actions is a sign for question 7. Rewrite as the alias_of rows: returns the alias; returns None when the manifest is missing | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py
ApplySettingsTest.test_a_repository_without_a_cli_gets_the_module_form_of_the_commands | merge | 4 | claude_block no-alias row; the same promise with alias "sx" is checked by test_the_claude_block_gets_the_alias_and_is_written_once. Merge into one table over alias "sx" and None | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py; sushisystems/sushisystems-tooling/CLAUDE_TEMPLATE.md
ApplySettingsTest.test_the_command_needs_a_settings_file_and_no_alias | split | 3 | main returns 2 with a message when no tools/settings.py; main returns 0 when settings are present. Two actions whose outcomes can break apart | sushisystems/sushisystems-tooling/tests/test_apply_settings.py; sushisystems/sushisystems-tooling/apply_settings.py
```

### `tools/tests/test_added_tests.py`

```
TestAddedCases.test_names_the_cases_a_commit_adds | keep | 9 | added: a case whose name is new in the test files is listed | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_a_case_moved_between_files_adds_nothing | keep | 9 | added: a case moved between files adds nothing | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_a_renamed_suite_and_an_edited_body_add_nothing_but_a_new_name_with_a_new_body_does | split | 3 | split into (a) added: a renamed suite or an edited body adds nothing and (b) added: a new name with a new body is listed | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_a_copy_under_a_new_name_counts_because_the_original_stays | keep | 9 | added: a copy under a new name is listed | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_a_benchmark_and_a_file_outside_the_test_folders_add_nothing | split | 3 | split into (a) added: a benchmark case adds nothing and (b) added: only files under the test folders are listed | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_a_removed_case_is_not_an_addition | keep | 9 | added: a removed case is not an addition | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_the_first_program_of_a_folder_is_free_and_the_second_is_named | split | 3 | split into (a) added: the first program of a folder is free and (b) added: a second program in a folder is named | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCases.test_two_programs_in_a_new_build_file_are_named | keep | 9 | added: two programs in a new build file are both named | tools/tests/test_added_tests.py; tools/testing/added_tests.py
TestAddedCommand.test_the_list_prints_each_commit_that_adds_something | keep | 9 | added (command): the list prints each commit that adds a case | tools/tests/test_added_tests.py; tools/testing/added_tests.py
```

### `tools/tests/test_case_reader.py`

```
CppCasesTest.test_reads_name_size_span_and_assertions | keep | 9 | reader C++: name, size, span and assertion count of a case | tools/tests/test_case_reader.py; tools/testing/case_reader.py
CppCasesTest.test_a_commented_or_quoted_assertion_does_not_count | keep | 9 | reader C++: a commented or quoted assertion is not counted | tools/tests/test_case_reader.py; tools/testing/case_reader.py
CppCasesTest.test_braces_in_strings_and_raw_strings_do_not_end_the_body | keep | 9 | reader C++: braces in strings and raw strings do not end the body | tools/tests/test_case_reader.py; tools/testing/case_reader.py
CppCasesTest.test_a_helper_named_expect_or_assert_counts | keep | 9 | reader C++: a helper named expect or assert counts, another name does not | tools/tests/test_case_reader.py; tools/testing/case_reader.py
CppCasesTest.test_finds_literal_assertions_and_sleeps_by_line | keep | 9 | reader C++: literal assertions and sleeps are found by line | tools/tests/test_case_reader.py; tools/testing/case_reader.py
CppCasesTest.test_knows_a_benchmark_and_an_unsized_suite | split | 3 | split into (a) reader C++: a benchmark suite has size benchmark and (b) reader C++: an unsized fixture has none | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_reads_asserts_raises_and_helpers | keep | 9 | reader Python: asserts, raises and helpers are counted | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_a_test_that_only_prints_asserts_nothing | keep | 9 | reader Python: a test that only prints has no assertion | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_finds_a_literal_assert_and_a_sleep | merge | 4 | reader Python: literal assertions and sleeps are found by line; merge into CppCasesTest.test_finds_literal_assertions_and_sleeps_by_line, the same promise read by another reader with another input | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_size_comes_from_the_function_then_the_class_then_the_file | keep | 9 | reader Python: size comes from the function, then the class, then the file | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_reads_a_testcase_subclass_whatever_its_name | keep | 9 | reader Python: a unittest subclass is read whatever its name | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_a_class_size_attribute_beats_the_file_size | keep | 9 | reader Python: a class size attribute beats the file size | tools/tests/test_case_reader.py; tools/testing/case_reader.py
PythonCasesTest.test_size_comes_from_a_module_size_constant | keep | 9 | reader Python: a module size constant sizes the tests | tools/tests/test_case_reader.py; tools/testing/case_reader.py
TypeScriptCasesTest.test_reads_the_size_of_the_describe_above_and_its_assertions | keep | 9 | reader TypeScript: describe gives the size, assertions and span | tools/tests/test_case_reader.py; tools/testing/case_reader.py
TypeScriptCasesTest.test_a_template_string_with_braces_does_not_end_the_body | keep | 9 | reader TypeScript: braces in a template string do not end the body | tools/tests/test_case_reader.py; tools/testing/case_reader.py
TypeScriptCasesTest.test_finds_a_literal_expectation_and_a_timer | merge | 4 | reader TypeScript: literal expectations and timers are found by line; merge into CppCasesTest.test_finds_literal_assertions_and_sleeps_by_line, the same promise read by another reader | tools/tests/test_case_reader.py; tools/testing/case_reader.py
OtherFilesTest.test_a_markdown_file_has_no_cases | keep | 9 | reader: a markdown file has no cases | tools/tests/test_case_reader.py; tools/testing/case_reader.py
```

### `tools/tests/test_changed_lines.py`

```
TestChangedLinesParse.test_names_the_edited_and_the_added_lines_only | keep | 9 | changed lines: edited and added lines are named, deleted lines are not | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
TestChangedLinesParse.test_a_pure_deletion_adds_no_line | keep | 9 | changed lines: a pure deletion adds no line | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
TestChangedLinesParse.test_an_untracked_file_counts_every_line | keep | 9 | changed lines: an untracked file counts every line | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
TestChangedLinesParse.test_a_deleted_file_adds_no_line | keep | 9 | changed lines: a deleted file adds no line | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
TestChangedLinesParse.test_an_unknown_base_stops_with_a_message | rewrite | 2 | changed lines: an unknown base stops with a message; the test asserts SystemExit only, so the message is unchecked and no other test checks it | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
TestChangedLinesShell.test_a_commit_after_the_base_and_an_untracked_file_are_both_named | split | 3 | split into (a) changed lines: a commit after the base is named by its added lines and (b) changed lines: an untracked file in a repository is named | tools/tests/test_changed_lines.py; tools/testing/changed_lines.py
```

### `tools/tests/test_check_agnostic.py`

```
ProductTermsTest.test_product_name_is_reported_with_its_line | keep | 9 | agnostic: a product name is reported with its line | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_allowed_name_is_not_reported | keep | 9 | agnostic: an allowed name is not reported | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_company_tool_and_identity_are_reported_by_their_own_rule | split | 3 | split into (a) agnostic: a company tool name is reported and (b) agnostic: an identity is reported | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_technology_name_is_reported_outside_the_exempt_folders | keep | 9 | agnostic: a technology name is reported outside the exempt folders | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_exempt_folder_still_answers_to_the_other_rules | keep | 9 | agnostic: an exempt folder still answers to the other rules | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_leading_hash_header_of_a_script_is_not_read | keep | 9 | agnostic: the leading hash header of a script is not read | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ProductTermsTest.test_a_line_with_the_allow_mark_is_not_read | keep | 9 | agnostic: a line with the allow mark is not read | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
MachinePathTest.test_machine_paths_are_reported | keep | 9 | agnostic: a drive path or user folder is reported | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
MachinePathTest.test_urls_and_prose_about_paths_are_not_machine_paths | keep | 9 | agnostic: URLs and prose about paths are not machine paths | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
MachinePathTest.test_an_escape_sequence_in_a_string_is_not_a_machine_path | keep | 9 | agnostic: an escape sequence in a string is not a machine path | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
CheckedFilesTest.test_the_settings_file_is_not_read | keep | 9 | agnostic: the settings file is not read | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
CheckedFilesTest.test_files_outside_the_checked_folders_are_not_read | keep | 9 | agnostic: files outside the checked folders are not read | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
CheckedFilesTest.test_no_checked_folder_means_nothing_is_checked | keep | 9 | agnostic: no checked folder means nothing is checked | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
CheckedFilesTest.test_a_checked_text_file_is_read | keep | 9 | agnostic: a checked text file is read and an image is not | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
TermsFileTest.test_missing_terms_file_is_one_issue_and_silences_the_term_rules | split | 3 | split into (a) agnostic: a missing terms file is one issue and (b) agnostic: a missing terms file silences the term rules | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
TermsFileTest.test_unreadable_terms_line_is_reported_with_its_number | keep | 9 | agnostic: an unreadable terms line is reported with its number | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
TermsFileTest.test_a_pattern_that_does_not_compile_is_reported | keep | 9 | agnostic: a pattern that does not compile is reported | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
ShellTest.test_cli_reads_the_text_files_of_the_checked_folders_only | keep | 9 | agnostic (command): the checked folders are read and the product name is reported | tools/tests/test_check_agnostic.py; tools/layering/check_agnostic.py; tools/checking/checker.py
```

### `tools/tests/test_check_all.py`

```
OwnCheckerNamesTest.test_names_a_checker_the_shared_list_does_not_name | keep | 9 | check_all: a checker the shared list does not name is an own checker | tools/tests/test_check_all.py; tools/check_all.py
OwnCheckerNamesTest.test_drops_a_test_helper_and_a_checker_under_tests | keep | 9 | check_all: test helpers and checkers under tests are dropped | tools/tests/test_check_all.py; tools/check_all.py
PlanChecksTest.test_shared_checkers_run_first_then_own_then_suites | keep | 9 | check_all: shared checkers run first, own ones next, suites last | tools/tests/test_check_all.py; tools/check_all.py
PlanChecksTest.test_each_checker_runs_with_the_interpreter_and_the_root | keep | 9 | check_all: each checker runs with the interpreter and the root | tools/tests/test_check_all.py; tools/check_all.py
PlanChecksTest.test_suite_runs_unittest_discover_on_its_folder | keep | 9 | check_all: a suite runs unittest discover on its folder | tools/tests/test_check_all.py; tools/check_all.py
PlanChecksTest.test_no_folder_that_exists_means_no_suite | delete | 2 | check_all: a plan with no suite folder has no suite; plan_checks never checks existence (that is _read_suite_folders, covered by ShellTest.test_lists_only_the_test_folders_that_exist), so this test passes with the existence filter removed | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_clean_run_counts_checkers_not_suites_and_exits_zero | split | 3 | split into (a) check_all: a clean run counts checkers, not suites and (b) check_all: a clean run exits zero | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_failed_check_prints_its_trimmed_output_and_is_named | keep | 9 | check_all: a failed check prints its trimmed output and is named | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_several_failures_keep_the_order_of_the_checks | keep | 9 | check_all: several failures keep the order of the checks | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_known_findings_end_the_clean_line | keep | 9 | check_all: known findings end the clean line | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_orphans_fail_under_the_baseline_file_name | keep | 9 | check_all: orphan baseline entries fail under the baseline file name | tools/tests/test_check_all.py; tools/check_all.py
ReportTest.test_orphans_follow_the_failed_checks | keep | 9 | check_all: orphans follow the failed checks | tools/tests/test_check_all.py; tools/check_all.py
JudgedTest.test_no_entries_return_the_results_as_they_are | keep | 9 | check_all: a baseline with no entries leaves results unchanged | tools/tests/test_check_all.py; tools/check_all.py
EnvironmentTest.test_drops_every_variable_that_points_git_at_a_repository | keep | 9 | check_all: the suite environment drops git repository variables | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_finds_a_checker_the_shared_list_does_not_name | keep | 9 | check_all: an own checker found on disk is named | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_runs_each_command_and_returns_its_exit_code_in_order | keep | 9 | check_all: each command runs and its exit code returns in order | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_lists_only_the_test_folders_that_exist | keep | 9 | check_all: only the test folders that exist are listed | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_main_returns_one_when_a_check_fails | rewrite | 1 | check_all: main returns one when a check fails; the test replaces check_all._run_all, a function the repository owns (forbidden kind), and no other test checks main exit code; rewrite with a real failing command | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_a_baseline_makes_a_red_checker_pass_and_the_clean_line_counts_it | rewrite | 1 | check_all: a baseline makes a red checker pass; the test replaces the own function _run_all (forbidden kind) and states two outcomes, the pass and the clean line; rewrite with a real failing check and split the clean-line count | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_a_baseline_entry_for_no_checker_fails | rewrite | 1 | check_all: a baseline entry naming no checker fails main; the test replaces the own function _run_all with a lambda (forbidden kind); main exit code for an orphan entry is checked nowhere else; rewrite with a real run | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_a_broken_baseline_file_returns_one | keep | 9 | check_all: a broken baseline file returns one | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_a_closed_backlog_id_fails_when_the_root_lists_its_open_ones | keep | 9 | check_all: a closed backlog ID fails when open IDs are listed | tools/tests/test_check_all.py; tools/check_all.py
ShellTest.test_reads_a_non_ascii_finding | keep | 9 | check_all: a non-ASCII finding is read as UTF-8 | tools/tests/test_check_all.py; tools/check_all.py
```

### `tools/tests/test_check_backlog.py`

```
RegistrationTest.test_names_the_one_rule | resize | 8 | backlog: the checker has one rule, rule_backlog; no file is read, so small suffices and the medium tag comes only from the module-level K_TEST_SIZE | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
WithoutBacklogTest.test_reports_nothing_without_a_store_or_a_retired_file | rewrite | 1 | backlog: a repository with no store or retired file reports nothing; the test patches the own function tooling_bridge._import (forbidden kind) and never asserts that the package is not asked for | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
MissingToolingTest.test_reports_once_that_the_rules_could_not_run | rewrite | 1 | backlog: a missing tooling package is reported once with package and version; the test patches documentation.check_backlog.load, a function the repository owns (forbidden kind) | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
MissingToolingTest.test_names_the_missing_setting_when_no_package_is_configured | keep | 9 | backlog: a missing package setting is named in the message; it patches a settings constant, not a function | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
DelegationTest.test_reports_a_retired_file | keep | 9 | backlog: a retired file is sent to backlog import | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
DelegationTest.test_reports_nothing_for_a_store_the_tool_wrote | keep | 9 | backlog: a store the tool wrote checks clean | tools/tests/test_check_backlog.py; tools/documentation/check_backlog.py; tools/documentation/tooling_bridge.py
```

### `tools/tests/test_check_backlog_trailer.py`

```
TrailerProblemsTest.test_a_message_without_the_line_is_refused | keep | 9 | trailer: a message without a Backlog line is refused | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_an_open_id_passes | merge | 4 | trailer: an open ID passes; merge into TrailerProblemsTest.test_several_ids_pass_when_each_is_open, the same promise with another input | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_several_ids_pass_when_each_is_open | keep | 9 | trailer: several IDs pass when each is open | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_an_id_that_is_not_open_is_refused | keep | 9 | trailer: an ID that is not open is refused and named | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_text_that_is_no_id_is_refused | keep | 9 | trailer: text that is no ID is refused | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_none_needs_a_reason | keep | 9 | trailer: none needs a reason in brackets | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_the_shape_of_an_id_is_the_pattern_given | keep | 9 | trailer: the shape of an ID is the pattern given | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_the_pattern_must_match_the_whole_item | keep | 9 | trailer: the pattern must match the whole item | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerProblemsTest.test_the_last_line_counts | keep | 9 | trailer: the last Backlog line counts | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_reads_the_rows_of_a_backlog_table | keep | 9 | trailer: ids_in reads the rows of a backlog table | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_an_id_open_at_the_parent_or_in_the_commit_passes | delete | 2 | trailer: an ID open at the parent or added in the commit passes; the body checks only a known ID in a message, so the in-commit and parent halves of the name are not exercised and the body would still pass if they broke; the promise is covered by RepositoryTest.test_a_commit_that_closes_its_entry_and_one_that_adds_an_entry_both_pass | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_a_commit_without_the_line_is_reported_on_its_short_hash | keep | 9 | trailer: a commit without the line is reported on its short hash | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_an_id_closed_before_the_commit_is_refused | keep | 9 | trailer: an ID closed before the commit is refused | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_the_rule_judges_the_id_by_the_pattern_of_the_commit | keep | 9 | trailer: the commit IDs are judged by the pattern given | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_nothing_is_checked_without_a_base | keep | 9 | trailer: nothing is checked without a base | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
TrailerRuleTest.test_registers_one_rule | keep | 9 | trailer: the checker registers one rule, rule_trailer | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_reads_the_rows_on_disk_and_at_a_revision | keep | 9 | trailer: open IDs are read on disk and at a revision | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_a_folder_without_a_backlog_holds_no_ids | keep | 9 | trailer: a folder without a backlog holds no IDs | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_a_commit_that_names_an_entry_closed_earlier_is_refused | keep | 9 | trailer: a commit naming an entry closed earlier is refused; the only test that reads the git history at this size, so it stays beside the small one | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_a_commit_that_closes_its_entry_and_one_that_adds_an_entry_both_pass | split | 3 | split into (a) trailer: a commit that closes an entry passes and (b) trailer: a commit that adds an entry passes | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_a_commit_without_the_line_is_reported_with_its_hash | keep | 9 | trailer: a commit without the line is reported with its hash | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
RepositoryTest.test_a_history_that_cannot_be_read_stops_the_check | keep | 9 | trailer: a history that cannot be read stops the check | tools/tests/test_check_backlog_trailer.py; tools/commits/check_backlog_trailer.py
```

### `tools/tests/test_check_changelog.py`

```
RuleTest.test_each_case_fires_exactly_its_rules | rewrite | 7 | changelog: each case fires exactly its rules; the body loops over the case table, so each case becomes one row of a parametrised test | tools/tests/test_check_changelog.py; tools/documentation/check_changelog.py
RuleTest.test_a_release_heading_with_trailing_spaces_is_a_release | keep | 9 | changelog: a release heading with trailing spaces is a release | tools/tests/test_check_changelog.py; tools/documentation/check_changelog.py
RuleTest.test_a_bullet_inside_a_code_fence_is_not_an_entry | keep | 9 | changelog: a bullet inside a code fence is not an entry | tools/tests/test_check_changelog.py; tools/documentation/check_changelog.py
RuleTest.test_an_entry_carries_the_line_it_is_on | keep | 9 | changelog: an entry carries the line it is on | tools/tests/test_check_changelog.py; tools/documentation/check_changelog.py
ShellTest.test_each_case_fires_exactly_its_rules_on_disk | rewrite | 7 | changelog (command): each case read from disk fires its rules; the body loops over the case table and repeats RuleTest on disk; keep one case on disk for the read path | tools/tests/test_check_changelog.py; tools/documentation/check_changelog.py
```

### `tools/tests/test_check_design_format.py`

```
RegistrationTest.test_names_every_rule | resize | 8 | design format: the five rules are registered by name; no file is read, so small suffices and the medium tag comes from the module-level K_TEST_SIZE | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ValidDocumentTest.test_reports_nothing | rewrite | 7 | design format: a valid document passes every rule; the body loops over the rule table, and the test passes vacuously when the tooling package is absent (no skip; the four non-section rules yield nothing without it); one row per rule with a guard that the package loads | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ValidDocumentTest.test_leaves_the_indexes_and_phase_files_alone | rewrite | 7 | design format: index, design map and phase files are skipped; the body loops over the rule table and passes vacuously without the tooling package; one row per rule | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ValidDocumentTest.test_reads_the_readme_of_a_split_topic | keep | 9 | design format: a split topic README is read as its document | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
SectionsTest.test_reports_a_foreign_section_and_a_missing_one | keep | 9 | design format: a foreign or missing section is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
SectionsTest.test_reports_the_wrong_order | keep | 9 | design format: sections out of order are reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
SectionsTest.test_ignores_a_heading_inside_a_fence | keep | 9 | design format: a fenced heading is not a section | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
StatusLengthTest.test_reports_a_long_status | keep | 9 | design format: a status over 160 characters is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
StatusLengthTest.test_accepts_a_status_at_the_ceiling | keep | 9 | design format: a status of 160 characters is accepted | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
PhaseTableTest.test_reports_other_columns | keep | 9 | design format: a phase header other than Id, Phase, State is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
PhaseTableTest.test_reports_an_unknown_state | keep | 9 | design format: a phase state outside the four is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
PhaseTableTest.test_reports_a_section_with_neither_table_nor_none | keep | 9 | design format: a section with neither a table nor None is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
PhaseTableTest.test_accepts_none | keep | 9 | design format: a section that says None is accepted | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
CommitHashTest.test_reports_a_hash_and_a_range | keep | 9 | design format: a commit hash or a range is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
CommitHashTest.test_reports_a_bare_hash | keep | 9 | design format: a bare hash in prose is reported | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
CommitHashTest.test_leaves_a_word_and_a_number_alone | keep | 9 | design format: a word or a long number is not a hash | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ExecutionRecordTest.test_reports_a_verb_beside_a_date_in_either_order | keep | 9 | design format: a verb beside a date is an execution record | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ExecutionRecordTest.test_leaves_a_ruling_and_the_status_alone | keep | 9 | design format: a ruling or the status line is not a record | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
ExecutionRecordTest.test_ignores_a_fenced_example | keep | 9 | design format: a fenced example is not a record | tools/tests/test_check_design_format.py; tools/documentation/check_design_format.py; tools/documentation/tooling_bridge.py
```

### `tools/tests/test_check_design_topics.py`

```
RegistrationTest.test_names_every_rule | keep | 9 | design topics: the ten rules are registered by name | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
GlossaryTest.test_is_silent_when_not_asked | keep | 9 | design topics: a glossary term is required per topic when asked, silent otherwise | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
GlossaryTest.test_reports_a_topic_the_glossary_lacks | keep | 9 | design topics: a topic the glossary lacks is reported on its first line | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
GlossaryTest.test_reports_every_topic_when_there_is_no_glossary | keep | 9 | design topics: every topic is reported when there is no glossary | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
GlossaryTest.test_reads_a_table_cell_and_a_heading_with_separators | keep | 9 | design topics: a glossary table cell or a heading with separators matches a topic | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
GlossaryTest.test_does_not_match_inside_a_longer_word | keep | 9 | design topics: a term does not match inside a longer word | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
FolderCeilingTest.test_is_off_at_zero | keep | 9 | design topics: a ceiling of zero is off | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
FolderCeilingTest.test_reports_a_folder_over_the_ceiling | keep | 9 | design topics: a folder over its ceiling is reported | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ArchiveCitationTest.test_is_silent_while_the_archive_is_tracked | keep | 9 | design topics: archive citations are silent while the archive is tracked | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ArchiveCitationTest.test_reports_each_line_that_cites_the_archive | keep | 9 | design topics: each line citing an untracked archive is reported | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ArchiveCitationTest.test_does_not_read_the_archive_itself | keep | 9 | design topics: the archive itself is not read | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ViewsTest.test_reports_a_stale_block | keep | 9 | design topics: a stale generated block is reported | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ViewsTest.test_leaves_a_file_without_markers_alone | keep | 9 | design topics: a file without markers is left alone | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ViewsTest.test_asks_for_the_topic_map_when_topics_are_required | keep | 9 | design topics: a topic map is required when topics are required | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ShellTest.test_reports_a_module_two_topics_name | keep | 9 | design topics: a module named by two topics is reported; rule_module_owner is delegated to the tooling package, so the bridge contract is what this test holds | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
ShellTest.test_reports_nothing_for_valid_files_with_every_rule_on | rewrite | 7 | design topics: valid files pass every rule on disk; the body loops over the rule table; one row per rule | tools/tests/test_check_design_topics.py; tools/documentation/check_design_topics.py; tools/documentation/tooling_bridge.py
```

### `tools/tests/test_check_docs_layout.py`

```
RequiredEntriesTest.test_is_registered | keep | 9 | docs layout: the checker registers the required-entry and reachability rules | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
RequiredEntriesTest.test_reports_every_missing_document | keep | 9 | docs layout: every missing required document is reported | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
RequiredEntriesTest.test_accepts_a_complete_tree | keep | 9 | docs layout: a complete tree passes the required-entry rule | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_follows_links_through_an_index | keep | 9 | docs layout: links through an index reach a document, anchor included | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_follows_a_link_that_climbs_out_of_its_folder | keep | 9 | docs layout: a link through .. reaches its normalised target | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_reports_an_orphan | keep | 9 | docs layout: an unlinked document is reported as an orphan | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_ignores_links_in_code | keep | 9 | docs layout: a link inside code does not reach its target | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_exempts_work_folders_and_archive | keep | 9 | docs layout: agent folders and the archive are exempt from reachability | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_reads_titled_wrapped_bracketed_and_queried_links | keep | 9 | docs layout: titled, wrapped, bracketed, queried and encoded link targets are read | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_reports_a_broken_titled_link_on_its_line | keep | 9 | docs layout: a broken titled link is reported on the line it starts | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_does_not_reach_through_a_file_outside_docs | keep | 9 | docs layout: a root README link does not reach through a file outside docs | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_does_not_reach_through_a_work_folder | keep | 9 | docs layout: a work folder link does not reach the guide it names | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ReachabilityTest.test_is_silent_without_an_index | keep | 9 | docs layout: reachability is silent without an index | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
DocsEntriesTest.test_accepts_the_publish_list | keep | 9 | docs layout: docs accepts the publish list and reports other loose files | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
DocsEntriesTest.test_accepts_the_docs_truth_allow_list | keep | 9 | docs layout: docs accepts the docs_truth allow list | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
LinkAnchorsTest.test_accepts_a_heading_slug_and_a_label | keep | 9 | docs layout: a heading slug, a repeated slug and a label resolve | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
LinkAnchorsTest.test_reports_an_anchor_no_heading_has | keep | 9 | docs layout: an anchor no heading has is reported on the link line | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
LinkAnchorsTest.test_ignores_a_heading_inside_a_fence | keep | 9 | docs layout: a heading inside a fence gives no anchor | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
StatusLinesTest.test_accepts_the_four_forms | keep | 9 | docs layout: the four status forms are accepted | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
StatusLinesTest.test_reports_prose_and_an_undated_closed_status | keep | 9 | docs layout: a prose or undated closed status is reported | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
StatusLinesTest.test_reads_the_first_file_of_a_work_folder | keep | 9 | docs layout: a work folder is read through SPEC first, then REPORT | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ClosedWorkTest.test_counts_from_the_status_date | keep | 9 | docs layout: closed work is listed once its grace has passed, counted from the status date | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ClosedWorkTest.test_keeps_a_shipped_design_and_deletes_a_shipped_work_folder | split | 3 | split into (a) docs layout: a shipped design is kept and (b) docs layout: a shipped work folder is listed | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ClosedWorkTest.test_a_grace_of_zero_lists_work_closed_today | keep | 9 | docs layout: a grace of zero lists work closed today | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ForbiddenKindsTest.test_reports_each_kind_outside_agent_and_archive | keep | 9 | docs layout: forbidden kinds are reported outside agent and archive | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ForbiddenKindsTest.test_accepts_a_design_document | keep | 9 | docs layout: a design document and the backlog are accepted | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ShellTest.test_leaves_out_a_folder_git_ignores | keep | 9 | docs layout (shell): a loose docs entry git ignores is not reported | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ShellTest.test_a_fresh_commit_does_not_reset_the_clock | keep | 9 | docs layout (shell): the clock counts from the status date across a commit | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
ShellTest.test_command_line_names_each_missing_document | keep | 9 | docs layout (command): each missing required document is named | tools/tests/test_check_docs_layout.py; tools/documentation/check_docs_layout.py
```

### `tools/tests/test_check_docs_truth.py`

```
RuleTableTest.test_registers_every_rule | keep | 9 | docs truth: every rule is registered under its own name | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
NamedSymbolsTest.test_reports_each_shape_of_absent_name | keep | 9 | docs truth: an absent qualified name, call, type, snake name, constant or macro is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
NamedSymbolsTest.test_accepts_names_the_source_holds | keep | 9 | docs truth: names the source holds, standard library names and paths are accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
NamedSymbolsTest.test_reads_a_source_block_without_its_own_names | keep | 9 | docs truth: a source block reports absent calls, not the names it declares | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
NamedSymbolsTest.test_leaves_a_design_document_to_its_intent | keep | 9 | docs truth: a design document is not checked for names the source lacks | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
NamedSymbolsTest.test_accepts_an_allowed_name | keep | 9 | docs truth: a name matched by an allow-list pattern is accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
CitedPathsTest.test_reports_a_missing_path | keep | 9 | docs truth: a cited path that is missing is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
CitedPathsTest.test_accepts_existing_and_foreign_paths | keep | 9 | docs truth: existing and foreign cited paths are accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
CitedPathsTest.test_resolves_a_module_readme_path_beside_it | keep | 9 | docs truth: a module README path resolves beside the README | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
CitedPathsTest.test_reads_a_page_beside_a_test_file | keep | 9 | docs truth: a page beside a test file is read | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ExampleSourceTest.test_reports_an_uncited_and_a_drifted_example | keep | 9 | docs truth: an uncited example and a drifted example are reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ExampleSourceTest.test_accepts_a_cited_excerpt_and_a_marked_block | keep | 9 | docs truth: a cited excerpt and a marked block are accepted and unverified examples counted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ExampleSourceTest.test_exempts_a_module_readme | keep | 9 | docs truth: a module README is exempt from example citation | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
HistoryWordsTest.test_reports_each_history_phrase | keep | 9 | docs truth: each history phrase is reported on its line | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
HistoryWordsTest.test_accepts_present_tense_code_quotes_and_known_issues | keep | 9 | docs truth: present tense, code quotes and known issues are accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
PageLengthTest.test_reports_a_page_one_line_above_its_ceiling | keep | 9 | docs truth: a page one line over its ceiling is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
PageLengthTest.test_accepts_a_page_at_its_ceiling_and_leaves_design_to_its_checker | keep | 9 | docs truth: a page at its ceiling is accepted and design documents are left to their checker | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
DuplicatedPassagesTest.test_reports_the_second_copy_whatever_its_wrapping | keep | 9 | docs truth: a second copy of a long passage is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
DuplicatedPassagesTest.test_reports_a_rule_restated_in_a_second_skill | keep | 9 | docs truth: a rule restated in a second skill is reported and research notes are skipped | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
DuplicatedPassagesTest.test_accepts_a_short_repeat_and_a_repeated_code_block | keep | 9 | docs truth: a short repeat and a repeated code block are accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
DuplicatedPassagesTest.test_accepts_a_generated_block_in_two_module_readmes | keep | 9 | docs truth: a generated block in two module READMEs is accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
EmDashTest.test_reports_an_em_dash_in_prose | keep | 9 | docs truth: an em dash in prose is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
EmDashTest.test_accepts_code_the_status_line_and_the_changelog | keep | 9 | docs truth: an em dash in code, a status line or the changelog is accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
AllowListTest.test_reports_a_bare_a_broken_and_an_unused_entry | keep | 9 | docs truth: a bare, broken or unused allow-list entry is reported | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
AllowListTest.test_accepts_a_reasoned_entry_in_use_and_comment_lines | keep | 9 | docs truth: a reasoned, used allow-list entry and comments are accepted | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ShellTest.test_source_option_replaces_the_default_folders | keep | 9 | docs truth (command): the source option replaces the default source folders | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ShellTest.test_checks_a_page_given_by_path | keep | 9 | docs truth (command): a page given by path is checked | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ShellTest.test_report_counts_the_unverified_examples | keep | 9 | docs truth (command): the report counts unverified examples | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py
ShellTest.test_ceilings_match_the_documentation_skill | keep | 9 | docs truth: the four ceilings match the table in the documentation skill | tools/tests/test_check_docs_truth.py; tools/documentation/check_docs_truth.py; skills/documentation/SKILL.md
```

### `tools/tests/test_check_layering.py`

```
RuleUpwardIncludesTest.test_reports_an_include_of_a_higher_module | keep | 9 | layering: an include of a higher module is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleUpwardIncludesTest.test_ignores_another_project_with_a_module_of_the_same_name | keep | 9 | layering: another project with a same-named module is ignored | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleUpwardIncludesTest.test_reports_an_upward_include_in_a_module_test | keep | 9 | layering: an upward include in a module test is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleUpwardIncludesTest.test_allows_a_test_to_include_an_umbrella | keep | 9 | layering: a test may include an umbrella | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleUpwardIncludesTest.test_resolves_the_tier_form_and_a_root_umbrella | keep | 9 | layering: the tier form and a root umbrella include path resolve | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredTiersTest.test_reports_an_empty_order_and_an_undeclared_tier | split | 3 | split into (a) layering: an empty tier order is reported and (b) layering: an undeclared tier is reported by name | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredTiersTest.test_reports_a_domain_tier_missing_from_the_order_without_crashing_on_a_declared_one | keep | 9 | layering: a domain tier missing from the order is reported without a crash | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleCrossDomainIncludesTest.test_reports_one_domain_including_another_and_allows_a_lower_tier | split | 3 | split into (a) layering: one domain including another is reported and (b) layering: a domain includes a lower tier and that is allowed | tools/tests/test_check_layering.py; tools/layering/check_layering.py
DomainNameResolutionTest.test_a_bare_name_means_the_module_outside_the_domains | keep | 9 | layering: a bare build name means the module outside the domains | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleSameTierIncludesTest.test_reports_an_edge_that_is_not_listed | keep | 9 | layering: a same-tier edge that is not listed is reported and a listed one is not | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleSameTierIncludesTest.test_lets_an_umbrella_include_its_tier | keep | 9 | layering: an umbrella may include its own tier | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_reports_an_include_the_build_file_does_not_list | keep | 9 | layering: an include the build file does not list is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_reports_a_listed_module_nothing_includes | keep | 9 | layering: a listed module that nothing includes is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_a_further_private_keyword_declares_a_source_include | keep | 9 | layering: a further private keyword declares a source include | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_an_include_of_a_generated_header_uses_a_module_with_no_include_tree | keep | 9 | layering: a generated header uses the module that generates it | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_reads_same_tier_edges_from_the_build_file | keep | 9 | layering: same-tier edges are read from the build file | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_resolves_a_tier_qualified_name_and_keeps_same_named_modules_apart | keep | 9 | layering: a tier-qualified name resolves and same-named modules stay apart | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_reports_an_installed_header_that_includes_an_internal_module | keep | 9 | layering: an installed header including an internal module is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
BuildDeclarationTest.test_skips_the_build_rules_when_no_function_is_named | keep | 9 | layering: build rules are skipped when no module function is named | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_reports_a_plain_add_library_with_its_file_and_line | keep | 9 | layering: a plain add_library is reported with its file and line | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_reports_any_case_and_any_compiled_type | keep | 9 | layering: any case and any compiled library type is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_ignores_a_target_that_compiles_nothing | keep | 9 | layering: a target that compiles nothing is ignored | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_reports_a_build_file_below_the_module_folder | keep | 9 | layering: a build file below the module folder is reported | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_ignores_the_module_function_a_comment_and_a_longer_name | keep | 9 | layering: the module function, a comment and a longer name are ignored | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleDeclaredLibrariesTest.test_is_silent_when_the_layout_names_no_module_function | keep | 9 | layering: the rule is silent when the layout names no module function | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleRestrictedIncludesTest.test_include_outside_the_door_is_refused | keep | 9 | layering: an include outside its door is refused | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleRestrictedIncludesTest.test_reports_the_file_and_line_of_the_include | keep | 9 | layering: a refused include is reported with its file and line | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleRestrictedIncludesTest.test_reads_applications_and_tests_as_well_as_modules | keep | 9 | layering: applications and tests are read as well as modules | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleRestrictedIncludesTest.test_allows_the_listed_paths_and_a_file_name_prefix | keep | 9 | layering: listed paths and a file-name prefix are allowed | tools/tests/test_check_layering.py; tools/layering/check_layering.py
RuleRestrictedIncludesTest.test_ignores_another_include_and_a_layout_with_no_door | split | 3 | split into (a) and (b) of layering: other includes and a layout with no door are ignored | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_names_the_door_module_when_the_includer_does_not_list_it | keep | 9 | layering: the door module is named when the includer does not list it | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_accepts_the_door_module_when_listed | keep | 9 | layering: the door module is accepted when listed | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_accepts_a_linked_provider_in_any_case | keep | 9 | layering: a linked provider is accepted in any case | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_ignores_a_provider_of_another_root | keep | 9 | layering: a provider of another root is ignored | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_names_nothing_when_the_door_module_is_absent | keep | 9 | layering: nothing is named when the door module is absent | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_leaves_an_include_of_another_root_alone | keep | 9 | layering: an include of another root is left alone | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ForeignRootTest.test_leaves_a_bare_root_name_alone | keep | 9 | layering: a bare root name is left alone | tools/tests/test_check_layering.py; tools/layering/check_layering.py
ShellTest.test_cli_reads_the_module_tree_and_reports_each_finding | keep | 9 | layering (command): the module tree is read and each finding printed | tools/tests/test_check_layering.py; tools/layering/check_layering.py
```

### `tools/tests/test_check_logging.py`

```
ConsoleOutputTest.test_reports_console_writes_outside_comments_and_allowed_paths | keep | 9 | logging: console writes outside comments and allowed paths are reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
SwallowedErrorTest.test_reports_an_empty_catch_and_an_except_that_only_passes | keep | 9 | logging: an empty catch and an except that only passes are reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
CategoryCallTest.test_reports_a_call_without_a_category | keep | 9 | logging: a log call without a category is reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
CategoryCallTest.test_reports_a_call_under_another_modules_category | keep | 9 | logging: a call under another module category is reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
CategoryCallTest.test_no_prefix_turns_the_cpp_call_rules_off | keep | 9 | logging: no prefix turns the C++ call rules off | tools/tests/test_check_logging.py; tools/logs/check_logging.py
CategoryHeaderTest.test_reports_a_module_that_logs_without_its_category_header | keep | 9 | logging: a module that logs without its category header is reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
PythonLoggerTest.test_reports_root_named_and_fstring_python_logging | keep | 9 | logging: root, named and f-string Python logging is reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
FrontReexportTest.test_reports_a_front_that_re_exports_the_logger | keep | 9 | logging: a front that re-exports the logger names or forwards to them is reported | tools/tests/test_check_logging.py; tools/logs/check_logging.py
ShellTest.test_cli_reads_the_source_folders_and_reports_each_finding | keep | 9 | logging (command): the source folders are read and tests and console paths skipped | tools/tests/test_check_logging.py; tools/logs/check_logging.py
```

### `tools/tests/test_check_module_install.py`

```
RuleTest.test_each_case_fires_exactly_its_rules | rewrite | 7 | module install: each case fires exactly its rules; the body loops over the case table, one row per case | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
RuleTest.test_an_issue_names_the_line_it_is_on | keep | 9 | module install: an issue names the line it is on | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_each_case_fires_exactly_its_rules_on_disk | rewrite | 7 | module install: each case fires exactly its rules on disk; the body loops over the case table and repeats RuleTest on disk; keep one case on disk for the read path | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_a_repository_that_is_not_a_module_is_skipped | keep | 9 | module install: a folder that is not a module is skipped | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_a_repository_whose_settings_name_no_manifest_is_skipped | keep | 9 | module install: settings that name no manifest skip the folder | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_only_git_tracked_files_are_read_inside_a_repository | keep | 9 | module install: only git-tracked config files are read inside a repository | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_without_git_every_config_file_is_read | keep | 9 | module install: without git every config file is read | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
ShellTest.test_collect_returns_what_read_modules_returns | keep | 9 | module install: collect returns what read_modules returns | tools/tests/test_check_module_install.py; tools/documentation/check_module_install.py
```

### `tools/tests/test_check_probes.py`

```
TestProbeRules.test_reports_a_probes_folder_outside_applications | keep | 9 | probes: a probes folder outside applications/probes is reported | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeRules.test_reports_a_probe_that_uses_a_test_framework | keep | 9 | probes: a probe that uses a test framework is reported | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeRules.test_reports_a_probe_added_to_the_test_runner | keep | 9 | probes: a probe added to the test runner is reported | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeRules.test_reports_a_probe_named_after_another | keep | 9 | probes: a probe named after another probe is reported | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeRules.test_reports_a_probe_the_readme_does_not_name | keep | 9 | probes: a probe the README does not name is reported | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeRules.test_applies_the_same_rules_to_scenario_benchmarks | keep | 9 | probes: scenario benchmarks follow the same rules | tools/tests/test_check_probes.py; tools/testing/check_probes.py
TestProbeCommand.test_command_reports_each_rule_with_its_line_and_exits_non_zero | keep | 9 | probes (command): each rule is printed with its line and the exit code is non-zero | tools/tests/test_check_probes.py; tools/testing/check_probes.py
```

### `tools/tests/test_check_source_comments.py`

```
RuleTableTest.test_registers_the_license_block_rule | keep | 9 | source comments: the license block rule is registered under its name | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_boxed_block | keep | 9 | source comments: a boxed block opens a C-family header | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_python_block | keep | 9 | source comments: the hash form opens a Python file | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_block_after_shebang | merge | 4 | source comments: a block after a shebang is accepted; merge into LicenseBlockTest.test_accepts_block_after_coding_line, the same promise with another first line | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_block_after_coding_line | keep | 9 | source comments: a block after a source encoding line is accepted | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_block_behind_a_byte_order_mark | keep | 9 | source comments: a block behind a byte order mark is accepted | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_accepts_upstream_lines | keep | 9 | source comments: upstream notice lines are accepted beside the own lines | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_demands_own_lines_beside_upstream_lines | keep | 9 | source comments: a ported file with only the upstream notice reports the missing own lines | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_a_box_without_the_project_section | keep | 9 | source comments: a box without the project section is reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_missing_block | keep | 9 | source comments: a file that opens with code is reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_wrong_file_name | keep | 9 | source comments: a block that names another file is reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_old_block | keep | 9 | source comments: an old holder and an old licence are reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_second_licence_beside_the_right_one | keep | 9 | source comments: a second licence beside the right one is reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
LicenseBlockTest.test_reports_reserved_rights_beside_a_grant | keep | 9 | source comments: reserved rights beside a grant are reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
PythonCommentTest.test_hash_lines_inside_a_string_are_not_comments | keep | 9 | source comments: hash lines inside a string are not comments | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
PythonCommentTest.test_a_real_run_of_comments_is_still_reported | keep | 9 | source comments: a run of comment lines is reported on its first line | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
PythonCommentTest.test_a_file_that_does_not_tokenize_falls_back_to_the_line_test | keep | 9 | source comments: a file that does not tokenise falls back to the line test | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
DateTagTest.test_reports_both_spellings_in_a_ray_tracing_shader | keep | 9 | source comments: both spellings of the date tag are reported in a shader | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
CommandLineTest.test_accepts_a_byte_order_mark_on_disk | keep | 9 | source comments (shell): a byte order mark on disk is accepted | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
CommandLineTest.test_reports_both_spellings_in_a_ray_tracing_shader_on_disk | keep | 9 | source comments (command): the date tag in a ray-tracing shader is reported | tools/tests/test_check_source_comments.py; tools/documentation/check_source_comments.py
```

### `tools/tests/test_check_test_mirror.py`

```
TestMultiModule.test_a_header_without_its_test_is_reported | keep | 9 | test mirror: a header without its test is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_a_test_with_no_header_is_reported | keep | 9 | test mirror: a test with no header or source is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_a_kind_folder_is_reported | keep | 9 | test mirror: a kind folder under tests is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_an_include_path_with_the_tier_mirrors_like_one_without | keep | 9 | test mirror: an include path with the tier mirrors like one without | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_a_folder_of_aspect_files_stands_for_the_unit_test | keep | 9 | test mirror: a folder of aspect files stands for the unit test | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_a_unit_with_both_a_test_file_and_a_folder_is_reported | keep | 9 | test mirror: a unit with both a test file and a folder is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMultiModule.test_data_folders_and_the_package_test_are_allowed | keep | 9 | test mirror: data folders and the package test are allowed | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestPrivateInclude.test_a_public_include_is_clean | keep | 9 | test mirror: a public include is clean | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestPrivateInclude.test_a_private_header_by_name_is_reported | keep | 9 | test mirror: a private header included by name is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestPrivateInclude.test_a_path_through_source_is_reported | keep | 9 | test mirror: a path through source is reported | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestPrivateInclude.test_a_helper_beside_the_test_is_not_private | keep | 9 | test mirror: a helper beside the test is not private | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestLanguagesAndApplications.test_python_mirrors_each_source_file_below_its_package | keep | 9 | test mirror: Python sources mirror below their package | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestLanguagesAndApplications.test_typescript_mirrors_each_source_file_of_a_module | keep | 9 | test mirror: TypeScript sources mirror per module | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestLanguagesAndApplications.test_an_application_mirrors_to_tests_applications | keep | 9 | test mirror: an application mirrors to tests/applications | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestUnity.test_an_untested_script_is_reported_and_legacy_and_vendors_are_not | keep | 9 | test mirror: an untested Unity script is reported and legacy and vendor folders are not | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestUnity.test_a_kind_folder_and_its_test_are_reported | keep | 9 | test mirror: a kind folder and its test are reported in a Unity project | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestSingleModule.test_a_mirrored_tree_is_clean | keep | 9 | test mirror: a mirrored single-module tree is clean | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestSingleModule.test_a_test_in_the_wrong_area_is_reported_twice | rewrite | 7 | test mirror: a test in the wrong area gives three findings; the name says twice while the body asserts three findings, so the name states no promise the body checks; rename to the three-finding promise | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMirrorCommand.test_command_reports_each_rule_on_a_layered_tree_with_its_line | keep | 9 | test mirror (command): each rule is printed with its line on a layered tree | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
TestMirrorCommand.test_command_reports_an_untested_script_of_a_unity_project | delete | 4 | test mirror (command): an untested Unity script is printed with its expected test; the same promise as TestUnity.test_an_untested_script_is_reported_and_legacy_and_vendors_are_not at a larger size, and the printed format is held by test_command_reports_each_rule_on_a_layered_tree_with_its_line; delete | tools/tests/test_check_test_mirror.py; tools/testing/check_test_mirror.py
```

### `tools/tests/test_check_test_sizes.py`

```
TestSizesRuleTest.test_cpp_rule_reports_an_unsized_suite_in_a_test_file_only | keep | 9 | test sizes: a C++ suite without a size in a test file is reported | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_python_rule_accepts_every_test_when_the_file_mark_sizes_it | keep | 9 | test sizes: a file mark sizes every Python test | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_python_rule_accepts_every_test_when_the_size_constant_sizes_it | merge | 4 | test sizes: a size constant sizes every Python test; merge into TestSizesRuleTest.test_python_rule_accepts_every_test_when_the_file_mark_sizes_it, the same promise by another mechanism | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_python_rule_reports_an_unsized_testcase_subclass_whatever_its_name | keep | 9 | test sizes: a unittest subclass without a size is reported whatever its name | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_python_rule_accepts_a_class_size_attribute | keep | 9 | test sizes: a class size attribute sizes its tests | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_python_rule_reports_a_test_when_file_and_test_carry_no_size | keep | 9 | test sizes: a Python test with no size in its file or itself is reported | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_typescript_rule_reports_an_unsized_describe_in_a_test_file_only | keep | 9 | test sizes: a TypeScript describe without a size is reported in test files only | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_csharp_rule_reports_a_fixture_without_a_size_category | keep | 9 | test sizes: a C# fixture without a size category is reported | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesRuleTest.test_every_rule_skips_a_benchmark_suite | rewrite | 7 | test sizes: benchmark suites are skipped by every rule; the body is a comprehension over the four rules; one row per rule | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
TestSizesShellTest.test_command_reads_every_test_folder_at_any_depth_and_nothing_outside | keep | 9 | test sizes (command): every test folder at any depth is read and nothing outside | tools/tests/test_check_test_sizes.py; tools/testing/check_test_sizes.py
```

### `tools/tests/test_check_test_value.py`

```
TestValueRules.test_reports_a_cpp_case_without_an_assertion_and_keeps_one_with_a_helper | keep | 9 | test value: a C++ case without an assertion is reported and a helper assertion counts | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_a_benchmark_case_is_left_alone | keep | 9 | test value: a benchmark case is left alone | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_python_and_typescript_cases_without_an_assertion | keep | 9 | test value: Python and TypeScript cases without an assertion are reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_an_assertion_on_a_literal | keep | 9 | test value: an assertion on a literal is reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_succeed_is_a_literal_assertion | keep | 9 | test value: SUCCEED is a literal assertion and not a missing one | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_counts_a_compile_time_check_a_no_throw_check_and_a_project_macro_as_assertions | keep | 9 | test value: compile-time, no-throw and project macro checks count as assertions | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_a_sleep_in_a_case_of_any_size | keep | 9 | test value: a sleep in a case of any size is reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_a_case_that_only_succeeds_checks_at_compile_time_or_checks_no_throw | keep | 9 | test value: a case that only succeeds, checks at compile time or checks no-throw is reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_a_typed_tolerance_and_keeps_a_derived_one | keep | 9 | test value: a typed tolerance is reported and a derived one is kept | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_reports_a_small_case_that_reaches_a_thread_a_file_or_the_clock | keep | 9 | test value: a small case that reaches a thread, a file or the clock is reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueRules.test_judges_only_a_case_with_a_changed_line | keep | 9 | test value: only a case with a changed line is judged | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueCommand.test_the_command_reports_a_case_written_after_the_base_commit | keep | 9 | test value (command): a case written after the base commit is reported | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
TestValueCommand.test_the_command_checks_nothing_in_a_repository_that_sets_no_base_commit | keep | 9 | test value (command): nothing is checked without a base commit | tools/tests/test_check_test_value.py; tools/testing/check_test_value.py; tools/tests/repo_builder.py
```

### `tools/tests/test_check_workflows.py`

```
DuplicateKeyTest.test_reports_a_key_written_twice_in_one_step | keep | 9 | workflows: a key written twice in one mapping is reported on its line | tools/tests/test_check_workflows.py; tools/ci/check_workflows.py
DuplicateKeyTest.test_the_same_key_in_separate_steps_and_jobs_is_not_a_duplicate | keep | 9 | workflows: the same key in separate steps and jobs is not a duplicate | tools/tests/test_check_workflows.py; tools/ci/check_workflows.py
DuplicateKeyTest.test_a_block_scalar_body_and_a_comment_are_not_keys | keep | 9 | workflows: a block scalar body and a comment are not keys | tools/tests/test_check_workflows.py; tools/ci/check_workflows.py
ShellTest.test_cli_reads_the_workflow_files_of_the_folder_only | keep | 9 | workflows (command): workflow files of the folder are read and no other file | tools/tests/test_check_workflows.py; tools/ci/check_workflows.py
```

### `tools/tests/test_checker.py`

```
CheckerTest.test_lists_its_rules_one_a_line | keep | 9 | checker: --list-rules prints each rule name on its own line | tools/tests/test_checker.py; tools/checking/checker.py
```

### `tools/tests/test_citation_files.py`

```
IsCitableTest.test_accepts_the_manual_and_the_source | rewrite | 7 | citation files: a manual page, a source file and a top-level tool file are citable; the body loops over names; one row per name | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
IsCitableTest.test_refuses_the_archive_and_the_shared_tools | rewrite | 7 | citation files: the archive and the shared tools are refused; the body loops over names; one row per name | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
IsCitableTest.test_refuses_a_skipped_folder_at_any_depth | rewrite | 7 | citation files: vendored, build and git folders are refused at any depth; the body loops over names; one row per name | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
IsCitableTest.test_refuses_an_extension_no_citation_uses | keep | 9 | citation files: an image and an extensionless file are refused | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
IsCitableTest.test_matches_the_archive_folder_by_name_not_by_prefix | keep | 9 | citation files: the archive folder is matched by name, not by prefix | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
ArchiveCitationLinesTest.test_numbers_each_line_that_cites_the_archive_from_one | keep | 9 | citation files: archive citation lines are numbered from one | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
ArchiveCitationLinesTest.test_is_empty_when_no_line_cites_the_archive | keep | 9 | citation files: text that cites no archive line gives an empty list | tools/tests/test_citation_files.py; tools/documentation/citation_files.py
```

### `tools/tests/test_commit_msg.py`

```
MessageTest.test_git_comment_lines_are_removed | keep | 9 | commit_msg: strip_comments drops the lines that start with git's comment mark | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
MessageTest.test_a_hash_inside_a_line_stays | keep | 9 | commit_msg: strip_comments keeps a mark that sits inside a line | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
MessageTest.test_a_message_that_opens_with_merge_is_a_merge | keep | 9 | commit_msg: is_merge is true only for messages that open with "Merge " | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
UsageTest.test_wants_exactly_one_argument | keep | 9 | commit_msg: main takes exactly one argument and otherwise prints the usage line and returns 1 | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_a_commit_with_an_open_id_and_nothing_staged_that_a_page_describes_passes | keep | 9 | commit_msg: a message whose Backlog ID is open and that stages no unpaged described change passes | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py; tools/documentation/docs_follow.py
CommitProblemsTest.test_a_message_without_the_line_is_refused | keep | 9 | commit_msg: a message without a Backlog line is refused | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_an_id_that_is_not_open_is_refused | keep | 9 | commit_msg: a Backlog ID that is not open is refused | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_the_shape_of_an_id_is_the_pattern_given | keep | 9 | commit_msg: a Backlog ID must match the pattern it is given | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_nothing_is_required_of_the_line_when_no_base_is_set | keep | 9 | commit_msg: no Backlog line is required when no base is set | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_a_staged_change_without_its_page_is_refused | keep | 9 | commit_msg: a staged change of a described file without its page is refused | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py; tools/documentation/docs_follow.py
CommitProblemsTest.test_the_page_staged_with_the_change_passes | keep | 9 | commit_msg: a page staged with its change passes | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py; tools/documentation/docs_follow.py
CommitProblemsTest.test_a_docs_line_waives_the_page | delete | 4 | duplicate of tools/tests/test_docs_follow.py::TestExplicitRule::test_a_docs_line_with_a_reason_satisfies_the_rule, the same promise at the same size in another file (docs_follow: a Docs line with a reason satisfies the rule for the page it names) | tools/tests/test_commit_msg.py; tools/tests/test_docs_follow.py; tools/hooks/commit_msg.py; tools/documentation/docs_follow.py
CommitProblemsTest.test_the_page_is_judged_even_when_no_line_is_required | keep | 9 | commit_msg: a page is judged even when no Backlog line is required | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_the_faults_of_the_line_come_before_the_faults_of_the_pages | keep | 9 | commit_msg: line faults are listed before page faults | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
CommitProblemsTest.test_each_problem_is_printed_on_a_line_of_its_own | keep | 9 | commit_msg: each refusal is printed on a line of its own with the refused prefix | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py
HookTest.test_refuses_and_accepts_by_what_is_staged_and_what_the_backlog_holds | split | 3 | several promises on one repository: commit_msg: the hook refuses a staged change without its page, accepts a Backlog line with an open ID and a staged page, refuses a message without the line, and accepts a merge; split into one test each | tools/tests/test_commit_msg.py; tools/hooks/commit_msg.py; tools/commits/check_backlog_trailer.py; tools/documentation/docs_follow.py
```

### `tools/tests/test_copy_shared_tools.py`

```
MergedTest.test_a_python_file_keeps_the_repository_header | resize | 8 | copy_shared_tools: merged keeps the repository header of a Python file; the function takes text, so the test is small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
MergedTest.test_a_new_python_file_takes_the_upstream_header | resize | 8 | copy_shared_tools: merged gives a new Python file the upstream header; pure text, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
MergedTest.test_another_file_is_copied_as_it_is | resize | 8 | copy_shared_tools: merged copies any other file as upstream has it; pure text, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_changed_shared_file_is_pending | keep | 9 | copy_shared_tools: pending lists the shared files a copy would write | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_copy_writes_shared_files_and_keeps_settings_and_local_tools | split | 3 | copy_shared_tools: copy writes the shared files, keeps settings, keeps local tools; split into one test each | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_missing_settings_are_written_from_upstream | keep | 9 | copy_shared_tools: a missing settings file is written from upstream | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_an_older_upstream_version_is_an_upgrade_not_a_local_edit | keep | 9 | copy_shared_tools: an older upstream version of a file is an upgrade, not a local edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_text_no_upstream_version_held_is_a_local_edit | keep | 9 | copy_shared_tools: a text no upstream version held is a local edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_copy_refuses_a_local_edit_and_writes_nothing | keep | 9 | copy_shared_tools: copy refuses a local edit and writes nothing | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_force_overwrites_a_local_edit | keep | 9 | copy_shared_tools: force overwrites a local edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_file_the_repository_lacks_is_never_a_local_edit | keep | 9 | copy_shared_tools: a file the repository lacks is never a local edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_crlf_newlines_alone_are_not_a_local_edit | keep | 9 | copy_shared_tools: CRLF newlines alone are not a local edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_an_upstream_without_a_commit_knows_no_text | keep | 9 | copy_shared_tools: an upstream with no commit knows no text | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_an_uncommitted_edit_is_not_copied_and_the_committed_text_is | keep | 9 | copy_shared_tools: copy uses the committed text of upstream, not an uncommitted edit | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_an_untracked_upstream_file_is_not_shared | keep | 9 | copy_shared_tools: shared_files lists only committed upstream tools files | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_the_command_names_uncommitted_upstream_files | keep | 9 | copy_shared_tools: the command names the uncommitted upstream files it copies from HEAD | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_the_command_reports_a_local_edit_and_refuses_to_copy_it | split | 3 | copy_shared_tools: the command reports a local edit and refuses to copy it; split into the report and the refusal | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
CopyTest.test_a_kept_file_is_left_alone_and_the_rest_is_copied | split | 3 | copy_shared_tools: --keep leaves a named file alone; the rest is copied; split into two tests | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
OtherSourceBlockTest.test_a_closed_repository_gets_its_own_box_and_a_second_copy_finds_no_difference | split | 3 | copy_shared_tools: a closed repository gets its own licence box in a non-Python shared file; a second copy finds no difference; split into two tests | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
OtherSourceBlockTest.test_a_repository_without_settings_gets_the_upstream_text | keep | 9 | copy_shared_tools: a repository without settings gets the upstream licence text | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
SmallDecisionTest.test_the_year_is_the_first_copyright_row_found | resize | 8 | copy_shared_tools: first_year is the first copyright row found; a literal function, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
SmallDecisionTest.test_the_year_falls_back_to_this_year | resize | 8 | copy_shared_tools: first_year falls back to this year when no row is found; pure, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
SmallDecisionTest.test_no_uncommitted_path_gives_no_notice | resize | 8 | copy_shared_tools: uncommitted_notice is empty for no path; pure, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
SmallDecisionTest.test_the_notice_names_every_path | resize | 8 | copy_shared_tools: uncommitted_notice names every uncommitted path; pure, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
NewFileHeaderTest.test_a_new_python_file_takes_the_template_header_with_its_own_name | resize | 8 | copy_shared_tools: a new shared Python file takes the template header with its own name; pure text, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
NewFileHeaderTest.test_without_a_template_the_upstream_header_stays | resize | 8 | copy_shared_tools: without a template the upstream header stays; pure text, so small | tools/tests/test_copy_shared_tools.py; tools/checking/copy_shared_tools.py
```

### `tools/tests/test_design_status.py`

```
FirstLineTest.test_skips_the_title_and_blank_lines | keep | 9 | design_status: first_content_line returns the number and text of the first non-empty line after the title | tools/tests/test_design_status.py; tools/documentation/design_status.py
FirstLineTest.test_returns_an_empty_line_when_the_document_has_none | keep | 9 | design_status: first_content_line returns line 1 with no text when nothing follows the title | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_reads_an_open_status | keep | 9 | design_status: parse_status reads an Open status as known and open with no close date | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_reads_a_shipped_status_and_its_date_before_a_full_stop | keep | 9 | design_status: parse_status reads a Shipped date that may be followed by a sentence | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_reads_a_superseded_status_by_its_successor | keep | 9 | design_status: parse_status reads a Superseded date and marks it not shipped | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_reads_a_withdrawn_status_with_its_reason | keep | 9 | design_status: parse_status reads a Withdrawn date with its reason | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_rejects_a_date_that_does_not_exist | keep | 9 | design_status: parse_status calls a shipped status with an impossible date unknown | tools/tests/test_design_status.py; tools/documentation/design_status.py
StatusFormTest.test_rejects_a_status_in_none_of_the_forms | keep | 9 | design_status: parse_status calls any other first line unknown, and an empty document too | tools/tests/test_design_status.py; tools/documentation/design_status.py
BodyTest.test_leaves_out_a_fenced_block | keep | 9 | design_status: body_lines leaves out the lines of a fenced block | tools/tests/test_design_status.py; tools/documentation/design_status.py
BodyTest.test_names_each_section_heading_with_its_line | keep | 9 | design_status: section_names lists each level-two heading with its line, not a heading inside a fence | tools/tests/test_design_status.py; tools/documentation/design_status.py
BodyTest.test_returns_the_lines_under_one_section_only | keep | 9 | design_status: section_body returns the lines under the named heading up to the next | tools/tests/test_design_status.py; tools/documentation/design_status.py
BodyTest.test_splits_a_table_row_into_trimmed_cells | keep | 9 | design_status: table_cells splits a row into trimmed cells | tools/tests/test_design_status.py; tools/documentation/design_status.py
ListingTest.test_lists_the_entries_directly_inside_a_folder_sorted | keep | 9 | design_status: children lists the entries directly inside a folder, sorted | tools/tests/test_design_status.py; tools/documentation/design_status.py
ListingTest.test_counts_a_split_topic_readme_and_the_topics_under_revision | keep | 9 | design_status: design_documents counts loose documents, split topic READMEs and revision READMEs, not indexes | tools/tests/test_design_status.py; tools/documentation/design_status.py
ListingTest.test_pairs_each_work_folder_with_its_first_status_file | keep | 9 | design_status: status_documents pairs each work folder with its SPEC.md, else its PLAN.md | tools/tests/test_design_status.py; tools/documentation/design_status.py
ListingTest.test_work_folders_lists_every_entry_under_agent | keep | 9 | design_status: work_folders lists every entry under docs/agent, sorted | tools/tests/test_design_status.py; tools/documentation/design_status.py
ListingTest.test_knows_a_topic_under_revision_by_its_path | keep | 9 | design_status: is_under_revision is true for a path inside the revision folder | tools/tests/test_design_status.py; tools/documentation/design_status.py
```

### `tools/tests/test_design_views.py`

```
RenderTest.test_renders_the_topic_map | keep | 9 | design_views: render_topic_map lists each topic with its link, state and About line | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_marks_a_topic_under_revision | keep | 9 | design_views: a topic under revision is listed with its link there and the state Revision | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_says_when_a_topic_has_no_about_line | keep | 9 | design_views: a topic with no About line says No description | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_lists_the_topics_of_a_module | keep | 9 | design_views: render_module_designs lists the topics whose Modules line names the module | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_lists_only_open_work_that_names_the_topic | keep | 9 | design_views: render_topic_work lists only open work that names the topic | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_says_when_no_work_is_open | keep | 9 | design_views: render_topic_work says No open work when none names the topic | tools/tests/test_design_views.py; tools/documentation/design_views.py
RenderTest.test_names_the_topic_map_the_module_and_the_work_blocks | keep | 9 | design_views: expected_blocks names the topic map, the module block and the work block | tools/tests/test_design_views.py; tools/documentation/design_views.py
BlockTest.test_returns_none_without_markers | keep | 9 | design_views: read_block returns None for a text without markers | tools/tests/test_design_views.py; tools/documentation/design_views.py
BlockTest.test_writes_between_the_markers_and_keeps_the_rest | split | 3 | design_views: write_block replaces only the lines between the markers, and a second write changes nothing; split into two tests | tools/tests/test_design_views.py; tools/documentation/design_views.py
BlockTest.test_leaves_a_text_without_markers_as_it_was | keep | 9 | design_views: write_block leaves a text without the block as it was | tools/tests/test_design_views.py; tools/documentation/design_views.py
BlockTest.test_inserts_empty_blocks | split | 3 | design_views: insert_block adds an empty block under its heading once, and puts the Work block at the end of the Phases section; split into two tests | tools/tests/test_design_views.py; tools/documentation/design_views.py
GeneratorTest.test_initialises_then_fills_every_block | keep | 9 | generate_design_views: init adds the markers and fills every block | tools/tests/test_design_views.py; tools/documentation/generate_design_views.py
GeneratorTest.test_check_reports_a_stale_block_and_writes_nothing | split | 3 | generate_design_views: check exits one on a stale block and writes nothing; the write then repairs it; split into the check, the untouched file and the repair | tools/tests/test_design_views.py; tools/documentation/generate_design_views.py
GeneratorTest.test_leaves_a_file_without_markers_alone | keep | 9 | generate_design_views: a README without markers is left alone unless initialised | tools/tests/test_design_views.py; tools/documentation/generate_design_views.py
```

### `tools/tests/test_docs_follow.py`

```
TestParsing.test_the_describes_line_lists_its_code_spans | keep | 9 | docs_follow: describes_of returns the code spans of a Describes line near the head of a page | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestParsing.test_a_describes_line_below_the_head_of_the_page_is_ignored | keep | 9 | docs_follow: describes_of ignores a Describes line below the head of a page | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestParsing.test_the_status_listing_names_renames_with_both_paths | keep | 9 | docs_follow: parse_changes reads a rename with both its old and new path | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestParsing.test_a_page_is_acknowledged_with_a_reason_only | keep | 9 | docs_follow: acknowledged reads a Docs line only when it gives a reason | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestParsing.test_none_with_a_reason_waives_every_page | keep | 9 | docs_follow: Docs none with a reason waives every page, and without a reason it does not | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_changed_described_file_without_its_page_is_a_problem | keep | 9 | docs_follow: a described file changed without its page is a problem | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_the_page_in_the_same_commit_satisfies_the_rule | keep | 9 | docs_follow: a page changed in the same commit satisfies the rule | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_docs_line_with_a_reason_satisfies_the_rule | keep | 9 | docs_follow: a Docs line with a reason satisfies the rule for the page it names | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_waiver_with_a_reason_satisfies_every_page | keep | 9 | docs_follow: a waiver with a reason satisfies every page | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_docs_line_names_one_page_and_leaves_the_others_reported | keep | 9 | docs_follow: a page that names one page leaves the other pages reported | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_described_folder_covers_the_files_below_it | keep | 9 | docs_follow: a described folder covers the files below it | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_renamed_described_file_is_a_problem | keep | 9 | docs_follow: a renamed or removed described file is a problem | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_removed_described_file_is_a_problem | keep | 9 | docs_follow: a renamed or removed described file is a problem | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestExplicitRule.test_a_file_nobody_describes_is_free | keep | 9 | docs_follow: a file no page describes is free | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_a_new_entry_needs_the_readme | keep | 9 | docs_follow: a new entry of a folder that a README lists needs that README in the same commit | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_a_new_folder_is_one_new_entry | keep | 9 | docs_follow: a new folder is one new entry | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_a_file_inside_an_existing_entry_is_free | keep | 9 | docs_follow: a file inside an existing entry is free, and so is an edit of an existing file | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_an_edit_of_an_existing_file_is_free | keep | 9 | docs_follow: a file inside an existing entry is free, and so is an edit of an existing file | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_removing_an_entry_needs_the_readme | keep | 9 | docs_follow: removing an entry needs its README, and removing one file of a folder that stays is free | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_removing_one_file_of_a_folder_that_stays_is_free | keep | 9 | docs_follow: removing an entry needs its README, and removing one file of a folder that stays is free | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_the_readme_in_the_same_commit_satisfies_the_rule | keep | 9 | docs_follow: a README changed in the same commit satisfies the README rule | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestReadmeRule.test_work_folders_and_the_backlog_are_not_followed | rewrite | 2 | docs_follow: work folders under docs/agent and the backlog are not followed; the body tests only a work folder, so the backlog half would still pass if broken; name and body need to agree, with a backlog case added | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestFactRule.test_a_page_following_a_changed_fact_is_a_problem | keep | 9 | docs_follow: a page following a fact is a problem when the fact's text changes in the commit | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestFactRule.test_a_page_following_an_unchanged_fact_is_free | keep | 9 | docs_follow: a page following a fact whose text does not change is free | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestPages.test_only_markdown_outside_the_ignored_folders_is_followed | keep | 9 | docs_follow: only markdown outside the ignored folders is a followed page | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestRepository.test_nothing_is_read_without_a_base | keep | 9 | check_docs_follow: nothing is read without a base | tools/tests/test_docs_follow.py; tools/documentation/check_docs_follow.py
TestRepository.test_only_the_commits_after_the_base_are_read | keep | 9 | check_docs_follow: only the commits after the base are read, oldest first | tools/tests/test_docs_follow.py; tools/documentation/check_docs_follow.py
TestRepository.test_refuses_a_staged_change_that_leaves_its_page_behind | delete | 4 | duplicate of tools/tests/test_commit_msg.py::CommitProblemsTest::test_a_staged_change_without_its_page_is_refused, the same promise at a smaller size in another file | tools/tests/test_docs_follow.py; tools/tests/test_commit_msg.py; tools/documentation/docs_follow.py
TestRepository.test_accepts_the_page_staged_with_it | delete | 4 | duplicate of tools/tests/test_commit_msg.py::CommitProblemsTest::test_the_page_staged_with_the_change_passes, the same promise at a smaller size in another file | tools/tests/test_docs_follow.py; tools/tests/test_commit_msg.py; tools/documentation/docs_follow.py
TestRepository.test_accepts_a_docs_line | delete | 4 | duplicate of tools/tests/test_docs_follow.py::TestExplicitRule::test_a_docs_line_with_a_reason_satisfies_the_rule, the same promise at a smaller size in the same file | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestRepository.test_a_new_entry_is_seen_in_the_index | keep | 9 | docs_follow: a new entry of a folder that a README lists is seen in the staged index | tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py; tools/hooks/commit_msg.py
```

### `tools/tests/test_drop_retired_citations.py`

```
PhraseTest.test_names_a_spec_by_its_file | keep | 9 | drop_retired_citations: phrase names a spec by its file, without date and extension, with its kind | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
PhraseTest.test_names_a_work_file_by_its_folder | keep | 9 | drop_retired_citations: phrase names a work file by its folder | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
PhraseTest.test_names_a_readme_by_its_folder | keep | 9 | drop_retired_citations: phrase names a README by its folder | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
PhraseTest.test_says_the_article_once | keep | 9 | drop_retired_citations: phrase says the article once | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
PhraseTest.test_falls_back_to_document | keep | 9 | drop_retired_citations: phrase falls back to document for a file in an unknown folder | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
RelativeLinkTest.test_replaces_a_sibling_topic_link_given_the_retired_folder | keep | 9 | drop_retired_citations: drop_text rewrites a sibling topic link when its folder is retired and leaves a live one | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
RelativeLinkTest.test_leaves_relative_links_alone_without_the_retired_folders | keep | 9 | drop_retired_citations: drop_text leaves relative links alone without the retired folders | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_replaces_a_code_span_and_keeps_the_section | keep | 9 | drop_retired_citations: drop_text replaces a path in a code span and keeps the section mark | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_replaces_a_bare_path_in_a_comment | keep | 9 | drop_retired_citations: drop_text replaces a bare path in a source comment | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_keeps_the_text_of_a_link | keep | 9 | drop_retired_citations: drop_text turns a link into its text and drops its anchor | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_replaces_a_link_whose_text_is_the_path | keep | 9 | drop_retired_citations: drop_text gives the phrase for a link whose text is the path | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_reads_a_path_reached_from_a_module | keep | 9 | drop_retired_citations: drop_text replaces a path written with leading parent folders and docs/ | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_replaces_a_retired_work_folder | keep | 9 | drop_retired_citations: drop_text replaces a citation of a retired work folder's file | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
DropTest.test_leaves_other_paths_alone | keep | 9 | drop_retired_citations: drop_text leaves citations of live documents and folders alone | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
RunTest.test_a_dry_run_lists_and_writes_nothing | keep | 9 | drop_retired_citations: run without apply lists the drops and writes nothing | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
RunTest.test_apply_writes_outside_the_archive_only | keep | 9 | drop_retired_citations: run --apply writes outside the archive and leaves the archive as it was | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
RunTest.test_the_command_exits_one_for_a_dry_run_that_finds_something | split | 3 | drop_retired_citations: main exits one while a citation remains without --apply and zero once replaced; split into the dry run, the apply and the dry run after it | tools/tests/test_drop_retired_citations.py; tools/documentation/drop_retired_citations.py
```

### `tools/tests/test_facts.py`

```
TestParsing.test_a_fact_has_its_id_lines_and_body | keep | 9 | facts: parse gives a fact its id, its marker lines and its body | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_multi_line_fact_keeps_every_line_of_its_body | keep | 9 | facts: a multi-line fact keeps every line of its body | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_an_empty_fact_has_an_empty_body | keep | 9 | facts: an empty fact has an empty body | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_quote_is_found | keep | 9 | facts: a quote is found by its id | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_follow_mark_is_found_with_its_line | keep | 9 | facts: a follow mark is found with its line | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_follow_mark_inside_a_fact_is_body_text | keep | 9 | facts: a follow mark inside a fact is body text | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_well_formed_page_has_no_faults | keep | 9 | facts: a well-formed page has no faults | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_fact_never_closed_is_a_fault | keep | 9 | facts: a fact that is never closed is a fault | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_an_end_without_its_beginning_is_a_fault | keep | 9 | facts: an end marker without its beginning is a fault | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_an_end_with_another_id_is_a_fault | keep | 9 | facts: an end marker with another id is a fault | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_quote_end_that_closes_a_fact_is_a_fault | keep | 9 | facts: a quote end that closes a fact is a fault | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_a_marker_inside_another_block_is_a_fault | keep | 9 | facts: a marker inside another block is a fault | tools/tests/test_facts.py; tools/documentation/facts.py
TestParsing.test_crlf_text_is_read_the_same_as_lf | keep | 9 | facts: CRLF text is read the same as LF text | tools/tests/test_facts.py; tools/documentation/facts.py
TestRegeneration.test_regenerate_replaces_only_the_quote_bodies | keep | 9 | facts: regenerate replaces only the body of each quote | tools/tests/test_facts.py; tools/documentation/facts.py
TestRegeneration.test_regenerate_keeps_crlf_and_unknown_quotes | rewrite | 2 | facts: regenerate keeps CRLF text and leaves a quote whose fact is unknown alone; with an empty home nothing is rewritten, so a CRLF rewrite that breaks the line endings would not fail; the test needs a CRLF quote that is replaced | tools/tests/test_facts.py; tools/documentation/facts.py
TestRegeneration.test_regenerate_rewrites_every_stale_quote_of_a_page | keep | 9 | facts: regenerate rewrites every stale quote of a page | tools/tests/test_facts.py; tools/documentation/facts.py
TestRegeneration.test_an_empty_home_empties_the_quote | keep | 9 | facts: an empty home empties its quote | tools/tests/test_facts.py; tools/documentation/facts.py
TestRegeneration.test_a_multi_line_home_replaces_the_body_with_all_its_lines | keep | 9 | facts: a multi-line home fills the quote with all its lines | tools/tests/test_facts.py; tools/documentation/facts.py
TestRules.test_a_current_quote_passes_every_rule | keep | 9 | check_docs_facts: a current quote passes every rule | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_stale_quote_names_its_home_and_the_command | keep | 9 | check_docs_facts: a stale quote names its home and the apply command | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_quote_whose_fact_has_no_home_is_left_to_the_existence_rule | keep | 9 | check_docs_facts: a quote whose fact has no home is left to the existence rule | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_two_homes_for_one_id_are_refused | keep | 9 | check_docs_facts: two homes for one id are refused | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_one_id_twice_on_one_page_is_refused | keep | 9 | check_docs_facts: one id twice on one page is refused | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_quote_or_follow_of_a_missing_fact_is_refused | keep | 9 | check_docs_facts: a quote or follow of a missing fact is refused | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_follow_of_a_missing_fact_names_the_fact | keep | 9 | check_docs_facts: a follow of a missing fact names the fact | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_home_on_the_quoting_page_satisfies_the_quote | keep | 9 | check_docs_facts: a home on the quoting page satisfies the quote | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_faulty_markers_are_reported | keep | 9 | check_docs_facts: faulty markers are reported | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_marker_fault_is_reported_on_its_line | keep | 9 | check_docs_facts: a marker fault is reported on its line | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_the_first_home_of_an_id_is_the_one_kept | keep | 9 | check_docs_facts: the first home of an id is the one kept | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestRules.test_a_quote_is_not_a_home | keep | 9 | check_docs_facts: a quote is not a home | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestCitations.test_citations_list_quotes_and_follows_in_page_order | keep | 9 | facts_cli: citations list quotes and follows in page order | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestCitations.test_every_quote_of_a_fact_is_listed | keep | 9 | facts_cli: every quote of a fact is listed | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestCitations.test_citations_skip_the_quotes_of_other_facts | keep | 9 | facts_cli: citations skip the quotes of other facts | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestCitations.test_an_uncited_fact_has_no_citations | keep | 9 | facts_cli: an uncited fact has no citations | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestPlanApply.test_a_stale_quote_is_planned_with_its_new_text | keep | 9 | facts_cli: plan_apply plans a stale quote with its new text | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestPlanApply.test_pages_with_current_quotes_are_not_planned | keep | 9 | facts_cli: pages with current quotes are not planned | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestPlanApply.test_planning_a_planned_text_again_plans_nothing | keep | 9 | facts_cli: planning a planned text again plans nothing | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestPlanApply.test_planned_pages_keep_their_order | keep | 9 | facts_cli: planned pages keep their order | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestPageSelection.test_build_folders_are_skipped | keep | 9 | check_docs_facts: build, third-party and dependency folders are skipped | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestPageSelection.test_third_party_and_dependency_folders_are_skipped | keep | 9 | check_docs_facts: build, third-party and dependency folders are skipped | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestPageSelection.test_ordinary_folders_are_checked | keep | 9 | check_docs_facts: ordinary folders are checked | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestPageSelection.test_page_paths_are_relative_and_posix | keep | 9 | check_docs_facts: page paths are relative and POSIX | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestTreeOnDisk.test_cited_by_lists_every_quote_and_follow | keep | 9 | facts_cli: cited-by lists every quote and follow of a fact | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestTreeOnDisk.test_where_and_list_name_the_home | split | 3 | facts_cli: where and list name the home of a fact; split into where and list | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestTreeOnDisk.test_an_unknown_id_is_an_error | keep | 9 | facts_cli: an unknown fact id is an error | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestTreeOnDisk.test_apply_rewrites_a_stale_quote_and_a_second_run_writes_nothing | split | 3 | facts_cli: apply rewrites a stale quote; a second apply writes nothing; split into two tests | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestTreeOnDisk.test_apply_refuses_a_stale_page_that_is_not_utf8_and_writes_nothing | keep | 9 | facts_cli: apply refuses a stale page that is not UTF-8 and writes nothing | tools/tests/test_facts.py; tools/documentation/facts_cli.py
TestTreeOnDisk.test_the_checker_passes_a_clean_tree_and_names_a_stale_quote | split | 3 | check_docs_facts: the checker passes a clean tree and names a stale quote; split into the clean pass and the stale finding | tools/tests/test_facts.py; tools/documentation/check_docs_facts.py
TestTreeOnDisk.test_changing_a_fact_lists_the_page_that_follows_it | delete | 4 | duplicate of tools/tests/test_docs_follow.py::TestFactRule::test_a_page_following_a_changed_fact_is_a_problem, the same promise at a smaller size in another file | tools/tests/test_facts.py; tools/tests/test_docs_follow.py; tools/documentation/docs_follow.py
TestTreeOnDisk.test_the_followers_page_in_the_commit_satisfies_the_rule | keep | 9 | docs_follow: a page that follows a fact is satisfied by the same commit changing it | tools/tests/test_facts.py; tools/documentation/docs_follow.py
TestTreeOnDisk.test_a_docs_line_satisfies_the_rule | keep | 9 | docs_follow: a Docs line satisfies the fact rule | tools/tests/test_facts.py; tools/documentation/docs_follow.py
TestTreeOnDisk.test_editing_text_outside_the_fact_is_free | keep | 9 | docs_follow: editing text outside a fact is free | tools/tests/test_facts.py; tools/documentation/docs_follow.py
```

### `tools/tests/test_fold_design_topics.py`

```
FoldPlanTest.test_names_the_readme_of_a_folder_named_after_the_document | keep | 9 | fold_design_topics: folded_name is the README of a folder named after the document | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldPlanTest.test_keeps_the_dots_inside_the_name | keep | 9 | fold_design_topics: folded_name keeps the dots inside the name | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldPlanTest.test_plans_one_move_per_document | keep | 9 | fold_design_topics: plan gives one move per loose document | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
LooseDocumentsTest.test_skips_the_indexes_and_the_folders | keep | 9 | fold_design_topics: loose_documents lists only the topic documents directly in docs/design | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
RelinkTest.test_keeps_a_link_to_the_same_file_and_leaves_external_ones | keep | 9 | fold_design_topics: relink keeps a link to the same file and leaves external links alone | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
RelinkTest.test_a_link_into_the_moved_folder_stays_within_it | rewrite | 2 | fold_design_topics: relink makes a link to a sibling of a moved folder reach that sibling from the new folder; the name says a link into the moved folder, the body tests a link out of it, so the name's promise is not tested | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldTest.test_a_dry_run_changes_nothing | keep | 9 | fold_design_topics: fold changes nothing on a dry run | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldTest.test_apply_moves_each_document_into_its_folder | keep | 9 | fold_design_topics: fold moves each document into its folder and keeps the indexes | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldTest.test_apply_rewrites_links_out_of_the_moved_file_and_into_it | keep | 9 | fold_design_topics: fold rewrites the links out of, into and to the moved file | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldTest.test_a_folder_reached_through_a_short_name_keeps_its_links_relative | keep | 9 | fold_design_topics: fold of a repository reached by another spelling keeps its links relative | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
FoldTest.test_the_command_exits_one_only_for_a_dry_run_with_work | split | 3 | fold_design_topics: fold exits one for a dry run that has work and zero after folding; split into the dry run and the apply | tools/tests/test_fold_design_topics.py; tools/documentation/fold_design_topics.py
```

### `tools/tests/test_history.py`

```
ParseLogTest.test_each_record_becomes_a_commit_in_listing_order | keep | 9 | history: parse_log yields each commit in listing order with its hash, parent and message | tools/tests/test_history.py; tools/commits/history.py
ParseLogTest.test_a_commit_without_a_parent_is_left_out | keep | 9 | history: parse_log leaves out a commit that has no parent | tools/tests/test_history.py; tools/commits/history.py
ParseLogTest.test_an_empty_listing_holds_no_commit | keep | 9 | history: parse_log of an empty listing holds no commit | tools/tests/test_history.py; tools/commits/history.py
ParseLogTest.test_the_whole_message_is_kept_with_one_closing_newline | keep | 9 | history: a commit message keeps every line with one closing newline | tools/tests/test_history.py; tools/commits/history.py
ParseLogTest.test_a_message_may_hold_the_field_mark | keep | 9 | history: a commit message may hold the field mark | tools/tests/test_history.py; tools/commits/history.py
ParseBlobStreamTest.test_each_object_is_read_by_its_size | keep | 9 | history: parse_blob_stream reads each object by its size | tools/tests/test_history.py; tools/commits/history.py
ParseBlobStreamTest.test_an_object_git_does_not_hold_is_left_out_and_the_next_is_read | keep | 9 | history: parse_blob_stream leaves out an object git does not hold and reads the next | tools/tests/test_history.py; tools/commits/history.py
ParseBlobStreamTest.test_bytes_that_are_not_utf8_are_replaced | keep | 9 | history: parse_blob_stream replaces bytes that are not UTF-8 | tools/tests/test_history.py; tools/commits/history.py
ParseBlobStreamTest.test_no_output_holds_no_text | keep | 9 | history: parse_blob_stream of no output holds no text | tools/tests/test_history.py; tools/commits/history.py
HistoryTest.test_the_commits_after_a_base_come_oldest_first_with_parent_and_whole_message | split | 3 | history: commits_since returns the commits after a base oldest first, and gives each its parent and its whole message; split into order, parent and message | tools/tests/test_history.py; tools/commits/history.py; tools/tests/repo_builder.py
HistoryTest.test_a_blob_is_read_by_its_hash_and_an_unknown_hash_is_left_out | split | 3 | history: blob_texts reads a blob by its hash and leaves out an unknown one; split into the read and the unknown hash | tools/tests/test_history.py; tools/commits/history.py; tools/tests/repo_builder.py
```

### `tools/tests/test_ignored_paths.py`

```
IgnoredPathsTest.test_an_ignored_folder_is_dropped | keep | 9 | ignored_paths: drop_ignored drops a path below a git-ignored folder | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py
IgnoredPathsTest.test_a_folder_linked_to_somewhere_outside_the_repository_is_still_dropped | keep | 9 | ignored_paths: drop_ignored drops a path below a folder linked from outside the repository | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py
IgnoredPathsTest.test_every_path_is_kept_outside_a_repository | keep | 9 | ignored_paths: drop_ignored keeps every path outside a repository | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py
IgnoredPathsTest.test_an_ignored_folder_is_named_once | keep | 9 | ignored_paths: ignored_folders names each ignored folder once | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py
IgnoredPathsTest.test_no_folder_is_ignored_outside_a_repository | keep | 9 | ignored_paths: ignored_folders is empty outside a repository | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py
IgnoredPathsTest.test_the_comment_checker_does_not_read_an_ignored_file | keep | 9 | check_source_comments: collect does not read a path git ignores | tools/tests/test_ignored_paths.py; tools/checking/ignored_paths.py; tools/documentation/check_source_comments.py
```

### `tools/tests/test_install_hooks.py`

```
InstallDecisionTest.test_the_command_sets_the_hooks_path_of_the_given_repository | keep | 9 | install_hooks: hooks_path_command sets core.hooksPath of the given repository | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py
InstallDecisionTest.test_the_root_is_the_first_argument_or_the_current_folder | keep | 9 | install_hooks: root_of is the first argument, or the current folder when there is none | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py
InstallDecisionTest.test_an_accepted_path_reports_on_stdout_and_exits_clean | keep | 9 | install_hooks: an accepted path reports on stdout and exits zero | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py
InstallDecisionTest.test_a_refused_path_reports_on_stderr_and_fails | keep | 9 | install_hooks: a refused path reports on stderr and exits one | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py
InstallTest.test_sets_the_hooks_path_and_reports_it | split | 3 | install_hooks: install sets core.hooksPath of a repository, and main reports it; split into install and main | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py; tools/tests/repo_builder.py
InstallTest.test_reports_a_folder_that_is_no_repository | keep | 9 | install_hooks: main reports a folder that is no repository | tools/tests/test_install_hooks.py; tools/hooks/install_hooks.py
```

### `tools/tests/test_job_table.py`

```
JobTableTest.test_good_table_yields_its_jobs_in_order | keep | 9 | job_table: read_jobs yields the rows of a good table in order, with their files and waits | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_bad_status_is_reported_with_its_line | keep | 9 | job_table: read_jobs reports a status outside todo, running, done and failed, with its line | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_repeated_id_is_reported | keep | 9 | job_table: read_jobs reports a repeated job id | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_row_with_a_missing_cell_is_reported | keep | 9 | job_table: read_jobs reports a row with a missing cell | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_missing_column_in_the_header_is_reported | keep | 9 | job_table: read_jobs reports a header that lacks a column | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_document_without_the_table_is_reported | keep | 9 | job_table: read_jobs reports a document without the table | tools/tests/test_job_table.py; tools/routing/job_table.py
JobTableTest.test_only_the_table_under_the_heading_is_read | keep | 9 | job_table: read_jobs reads only the table under the Jobs heading | tools/tests/test_job_table.py; tools/routing/job_table.py
```

### `tools/tests/test_known_findings.py`

```
ParseOutputTest.test_reads_path_rule_and_keeps_the_line | keep | 9 | known_findings: parse_output splits finding lines from the other lines | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseOutputTest.test_a_traceback_and_a_usage_line_are_other_lines | keep | 9 | known_findings: parse_output keeps a traceback and a usage line as other lines | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseOutputTest.test_a_path_with_folders_and_a_message_with_colons | keep | 9 | known_findings: parse_output reads a path with folders and a message with colons | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseOutputTest.test_an_indented_line_is_no_finding | keep | 9 | known_findings: parse_output reads an indented line as no finding | tools/tests/test_known_findings.py; tools/checking/known_findings.py
CountGroupsTest.test_counts_per_rule_and_path | keep | 9 | known_findings: count_groups counts the findings of each rule and path | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_no_entry_for_the_checker_returns_it_unchanged | keep | 9 | known_findings: apply_baseline returns the output of a checker with no entry unchanged | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_exactly_covered_findings_pass_although_the_checker_exited_one | keep | 9 | known_findings: apply_baseline passes exactly the covered findings even when the checker exited one | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_more_than_allowed_prints_every_line_of_the_group | keep | 9 | known_findings: apply_baseline prints every line of a group that is over its allowance | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_a_group_with_no_entry_prints_its_lines_and_the_covered_group_stays_quiet | keep | 9 | known_findings: apply_baseline prints the lines of an uncovered group and keeps a covered group quiet | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_fewer_than_allowed_says_the_finding_shrank | keep | 9 | known_findings: apply_baseline says a finding shrank when fewer are found than allowed | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_an_entry_found_never_says_gone_even_when_the_checker_exited_zero | keep | 9 | known_findings: apply_baseline says an entry is gone when none is found | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_another_line_makes_nothing_covered | keep | 9 | known_findings: apply_baseline covers nothing when another line is printed | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_an_exit_code_of_two_is_never_covered | keep | 9 | known_findings: apply_baseline never covers exit code two | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_a_backlog_id_that_does_not_match_fails_a_covered_checker | keep | 9 | known_findings: apply_baseline fails a covered checker whose backlog ID does not match | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ApplyBaselineTest.test_a_bad_backlog_id_fails_a_checker_that_exited_zero_with_other_lines | keep | 9 | known_findings: apply_baseline fails a checker that exits zero with other lines and a bad backlog ID | tools/tests/test_known_findings.py; tools/checking/known_findings.py
EntryProblemsTest.test_a_matching_id_with_no_open_list_passes | keep | 9 | known_findings: entry_problems accepts a matching ID when no open list is given | tools/tests/test_known_findings.py; tools/checking/known_findings.py
EntryProblemsTest.test_an_id_outside_the_open_list_is_closed | keep | 9 | known_findings: entry_problems refuses an ID outside the open list | tools/tests/test_known_findings.py; tools/checking/known_findings.py
EntryProblemsTest.test_an_open_id_passes | keep | 9 | known_findings: entry_problems passes an open ID | tools/tests/test_known_findings.py; tools/checking/known_findings.py
EntryProblemsTest.test_the_pattern_must_match_the_whole_id | keep | 9 | known_findings: the backlog pattern must match the whole ID | tools/tests/test_known_findings.py; tools/checking/known_findings.py
SummaryTest.test_no_entries_add_nothing | keep | 9 | known_findings: summary is empty for no entries | tools/tests/test_known_findings.py; tools/checking/known_findings.py
SummaryTest.test_counts_findings_and_entries | keep | 9 | known_findings: summary counts the findings and the entries | tools/tests/test_known_findings.py; tools/checking/known_findings.py
SummaryTest.test_one_of_each_is_singular | keep | 9 | known_findings: summary uses the singular for one finding and one entry | tools/tests/test_known_findings.py; tools/checking/known_findings.py
SummaryTest.test_names_the_entry_whose_checker_is_not_planned | keep | 9 | known_findings: orphan_lines names an entry whose checker is not planned | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_reads_each_field | keep | 9 | known_findings: parse_entries reads each field of an entry | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_no_table_is_no_entry | keep | 9 | known_findings: parse_entries reads no table as no entry | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_a_missing_field_is_an_error | keep | 9 | known_findings: parse_entries refuses an entry with a missing field | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_a_count_below_one_or_not_an_integer_is_an_error | keep | 9 | known_findings: parse_entries refuses a count below one or not an integer | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_a_table_that_is_no_table_is_an_error | keep | 9 | known_findings: parse_entries refuses a table that is not a table | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_finding_must_be_a_list | keep | 9 | known_findings: parse_entries refuses a finding list that is not a list | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ParseEntriesTest.test_a_repeated_group_is_an_error | keep | 9 | known_findings: parse_entries refuses a repeated group | tools/tests/test_known_findings.py; tools/checking/known_findings.py
RenderBaselineTest.test_one_sorted_entry_per_group_that_reads_back | keep | 9 | known_findings: render_baseline writes one sorted entry per group and reads back | tools/tests/test_known_findings.py; tools/checking/known_findings.py
RenderBaselineTest.test_quotes_and_backslashes_in_a_path_survive | keep | 9 | known_findings: render_baseline survives quotes and backslashes in a path | tools/tests/test_known_findings.py; tools/checking/known_findings.py
RenderBaselineTest.test_a_non_ascii_path_is_written_as_it_is | keep | 9 | known_findings: render_baseline writes a non-ASCII path as it is | tools/tests/test_known_findings.py; tools/checking/known_findings.py
RenderBaselineTest.test_no_findings_render_empty | keep | 9 | known_findings: render_baseline renders no findings as empty text | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ShellTest.test_an_absent_file_is_an_empty_baseline | keep | 9 | known_findings: read_baseline reads an absent file as an empty baseline | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ShellTest.test_write_refuses_an_existing_file_unless_replace_and_writes_lf | split | 3 | known_findings: write_baseline refuses an existing file unless replace is given, and writes LF endings; split into refusal and LF | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ShellTest.test_a_file_that_is_not_toml_is_an_error | keep | 9 | known_findings: read_baseline refuses a file that is not TOML | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ShellTest.test_the_writer_writes_what_the_checkers_print_and_reads_back | rewrite | 1 | known_findings: the writer writes the baseline of what the checkers print; the test replaces check_all.run_plan, a function the repository owns, so the promise is only checked through a stub; rewrite main to take the checker results as values and test that seam | tools/tests/test_known_findings.py; tools/checking/known_findings.py; tools/check_all.py
ShellTest.test_the_writer_reports_a_checker_that_prints_more_than_findings | rewrite | 1 | known_findings: the writer reports a checker that prints more than findings as not covered; the test replaces check_all.run_plan, a function the repository owns, and this is the only test of the message; rewrite as in the writer test | tools/tests/test_known_findings.py; tools/checking/known_findings.py; tools/check_all.py
ShellTest.test_the_writer_reports_a_note_after_a_zero_exit_and_a_silent_failure | rewrite | 1 | known_findings: the writer reports a note after a zero exit and a silent failure as not covered; the test replaces check_all.run_plan, a function the repository owns, and this is the only test of the message; rewrite as in the writer test | tools/tests/test_known_findings.py; tools/checking/known_findings.py; tools/check_all.py
ShellTest.test_the_command_needs_both_write_and_backlog | resize | 8 | known_findings: the command needs both --write and --backlog; argparse exits before any file or checker is read, so the test is small | tools/tests/test_known_findings.py; tools/checking/known_findings.py
ShellTest.test_the_writer_rejects_a_backlog_id_that_does_not_match | resize | 8 | known_findings: the writer rejects a backlog ID that does not match; main returns before any checker runs or any file is written, so the test is small | tools/tests/test_known_findings.py; tools/checking/known_findings.py
```

### `tools/tests/test_licence.py`

```
LicenceTest.test_reads_every_value_from_the_settings | rewrite | 1 | licence: from_module reads every value of a settings module into the licence; the test patches the process-wide settings module of a small test; from_module takes the module as an argument, so pass a namespace | tools/tests/test_licence.py; tools/documentation/licence.py
LicenceTest.test_a_closed_repository_takes_the_closed_rows | rewrite | 1 | licence: closed settings take the closed rows; the test patches the process-wide settings module of a small test; pass a closed namespace to from_module | tools/tests/test_licence.py; tools/documentation/licence.py
LicenceTest.test_settings_that_do_not_set_closed_take_the_open_rows | keep | 9 | licence: from_module takes the open rows unless the settings set closed | tools/tests/test_licence.py; tools/documentation/licence.py
LicenceTest.test_settings_without_a_holder_describe_no_licence | rewrite | 1 | licence: settings without a holder describe no licence; the test patches the process-wide settings module of a small test; pass a namespace without a holder to from_module | tools/tests/test_licence.py; tools/documentation/licence.py
LicenceTest.test_the_reserved_pattern_names_the_company_only_when_there_is_one | rewrite | 1 | licence: the reserved pattern names the company only when the settings name one; the test patches the process-wide settings module of a small test; pass the namespaces to from_module | tools/tests/test_licence.py; tools/documentation/licence.py
LicenceTest.test_the_checker_stops_when_no_licence_is_configured | rewrite | 1 | check_source_comments.collect stops when no licence is configured; the test patches the process-wide K_LICENCE of a small test; pass the licence to collect as a value | tools/tests/test_licence.py; tools/documentation/check_source_comments.py
LicenceTest.test_the_writer_stops_when_no_licence_is_configured | rewrite | 1 | write_license_block main stops with the unset message when no licence is configured; the test patches the process-wide K_LICENCE of a small test; pass the licence as a value | tools/tests/test_licence.py; tools/licensing/write_license_block.py; tools/documentation/licence.py
```

### `tools/tests/test_mutate_diff.py`

```
TestCore.test_parse_changed_lines_reads_added_ranges_and_skips_deletions | keep | 9 | mutate_diff: parse_changed_lines gives the added lines of each file and skips deletions | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_is_mutable_path_rejects_tests_and_other_languages | keep | 9 | mutate_diff: is_mutable_path accepts Python source outside the tests folders only | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_picks_one_mutation_per_kind | keep | 9 | mutate_diff: mutate_line makes one mutation per kind of the table | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_produces_the_mutated_text | keep | 9 | mutate_diff: mutate_line produces the mutated text | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_prefers_the_comparison_over_later_kinds | keep | 9 | mutate_diff: mutate_line prefers a comparison over the later kinds | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_keeps_non_ascii_text_before_the_span | keep | 9 | mutate_diff: mutate_line keeps non-ASCII text before the span | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_skips_what_proof_of_value_skips | keep | 9 | mutate_diff: mutate_line skips logging, capacity and docstring text | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_skips_a_return_of_none_and_a_broken_source | keep | 9 | mutate_diff: mutate_line returns no mutation when nothing applies | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_mutate_line_covers_a_continuation_line_of_a_statement | keep | 9 | mutate_diff: mutate_line covers a continuation line of a statement | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_apply_mutation_replaces_only_the_named_span | keep | 9 | mutate_diff: apply_mutation replaces only the named span | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_module_names_lists_every_suffix_and_drops_init | keep | 9 | mutate_diff: module_names lists the dotted names longest first and drops __init__ | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_imports_any_reads_each_import_form | keep | 9 | mutate_diff: imports_any reads each import form | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestCore.test_format_lines_follow_the_output_contract | keep | 9 | mutate_diff: format_result and format_summary follow the output contract | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestShell.test_main_reports_one_killed_and_one_survived_mutant | keep | 9 | mutate_diff: a run reports each mutant killed or survived and leaves the file as it was | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
TestShell.test_main_fails_with_a_reason_outside_a_repository | keep | 9 | mutate_diff: main fails with a reason outside a repository | tools/tests/test_mutate_diff.py; tools/testing/mutate_diff.py
```

### `tools/tests/test_next_jobs.py`

```
PlanReportTest.test_prints_the_ready_jobs_and_exits_zero | keep | 9 | next_jobs: plan_report prints the ready jobs and exits zero | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
PlanReportTest.test_exits_one_when_jobs_remain_and_none_is_ready | keep | 9 | next_jobs: plan_report exits one when jobs remain and none is ready | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
PlanReportTest.test_exits_two_when_every_job_is_done | keep | 9 | next_jobs: plan_report exits two when every job is done | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
PlanReportTest.test_exits_three_on_a_malformed_table_and_names_the_line | keep | 9 | next_jobs: plan_report exits three on a malformed table and names the line | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
PlanReportTest.test_exits_three_on_a_cycle | keep | 9 | next_jobs: plan_report exits three on a cycle | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
MainTest.test_main_reads_the_plan_file_and_prints_its_ids | keep | 9 | next_jobs: main reads the plan file and prints the ids of the ready jobs | tools/tests/test_next_jobs.py; tools/routing/next_jobs.py
```

### `tools/tests/test_ready_jobs.py`

```
ReadyJobsTest.test_blocked_job_is_skipped_for_a_later_ready_one | keep | 9 | ready_jobs: a blocked job is skipped for a later ready one | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_job_after_a_done_dependency_is_ready | keep | 9 | ready_jobs: a job after a done dependency is ready | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_failed_dependency_blocks_the_jobs_behind_it | keep | 9 | ready_jobs: a failed dependency blocks the jobs behind it | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_file_inside_a_running_jobs_folder_is_held | keep | 9 | ready_jobs: a file inside a running job's folder is held | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_file_above_a_running_jobs_file_is_held | keep | 9 | ready_jobs: a file above a running job's file is held | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_two_ready_jobs_sharing_a_file_are_not_both_picked | keep | 9 | ready_jobs: two ready jobs sharing a file are not both picked | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_count_limits_the_picks_in_list_order | keep | 9 | ready_jobs: the count limits the picks in list order | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_no_free_subagent_picks_nothing | keep | 9 | ready_jobs: no free subagent picks nothing | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_cycle_is_reported | keep | 9 | ready_jobs: a cycle is reported | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_unknown_dependency_is_reported | keep | 9 | ready_jobs: an unknown dependency is reported | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
ReadyJobsTest.test_acyclic_graph_has_no_faults | keep | 9 | ready_jobs: an acyclic graph has no faults | tools/tests/test_ready_jobs.py; tools/routing/ready_jobs.py
```

### `tools/tests/test_repair_design_citations.py`

```
RelativeNameTest.test_climbs_out_of_a_sibling_folder | keep | 9 | repair_design_citations: relative_name climbs out of a sibling folder then walks down | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RelativeNameTest.test_names_a_file_in_the_same_folder_bare | keep | 9 | repair_design_citations: relative_name gives a bare name for a file in the same folder | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RelativeNameTest.test_climbs_before_it_walks_down_when_the_paths_part_at_the_first_folder | keep | 9 | repair_design_citations: relative_name climbs first when the paths part at the first folder | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RelativeNameTest.test_gives_a_dot_for_the_folder_itself | keep | 9 | repair_design_citations: relative_name gives a dot for the folder itself | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RelativeNameTest.test_counts_each_folder_of_the_revision_path | keep | 9 | repair_design_citations: relative_name counts each folder of the revision path | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
ScanTest.test_skips_a_file_with_no_design_citation | keep | 9 | repair_design_citations: is_scanned skips a file that never names design | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
ScanTest.test_reads_a_file_under_design_and_a_file_that_names_design | keep | 9 | repair_design_citations: is_scanned reads a design file and any file that names design | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
ScanTest.test_reads_every_file_when_a_move_is_given | keep | 9 | repair_design_citations: is_scanned reads every file when a move is given | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_points_a_file_citation_at_the_folder_that_replaced_it | keep | 9 | repair_design_citations: repair_text points a file citation at the folder that replaced it | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_points_a_folder_citation_at_the_file_that_replaced_it | keep | 9 | repair_design_citations: repair_text points a folder citation at the file that replaced it | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_reports_a_page_the_topic_does_not_have | keep | 9 | repair_design_citations: repair_text reports a page the topic does not have | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_reports_a_topic_that_does_not_exist | keep | 9 | repair_design_citations: repair_text reports a topic that does not exist | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_leaves_a_citation_that_resolves_alone | keep | 9 | repair_design_citations: repair_text leaves a citation that resolves alone | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_repairs_a_path_that_starts_at_design | keep | 9 | repair_design_citations: repair_text repairs a path that starts at design and keeps the form written | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_rewrites_a_path_and_a_link_to_the_new_file | keep | 9 | repair_design_citations: repair_text rewrites a moved path and a link to it, keeping the anchor | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_leaves_other_files_of_the_topic_alone | keep | 9 | repair_design_citations: repair_text leaves other files of the topic alone | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_points_a_citation_at_the_topic_under_revision | keep | 9 | repair_design_citations: repair_text points a citation at the topic under revision | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_reads_the_links_of_a_moved_page_from_its_former_place | keep | 9 | repair_design_citations: repair_text reads the links of a moved page from its former place | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RepairTextTest.test_reads_the_links_of_a_page_that_left_the_revision_folder | keep | 9 | repair_design_citations: repair_text reads the links of a page that left the revision folder | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_apply_writes_the_repaired_citations_to_disk | keep | 9 | repair_design_citations: run --apply writes the repaired citations to disk | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_writes_nothing_without_apply | keep | 9 | repair_design_citations: run without apply writes nothing | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_leaves_the_archive_alone | keep | 9 | repair_design_citations: run leaves the archive and the citations that resolve alone | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_leaves_the_fixtures_of_the_checker_tests_alone | keep | 9 | repair_design_citations: run leaves the fixtures of the checker tests alone | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_the_command_reads_each_move_pair | keep | 9 | repair_design_citations: the command reads each move pair | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
RunTest.test_exits_one_only_for_a_citation_it_cannot_place | split | 3 | repair_design_citations: the command exits one only for a citation it cannot place; split into the zero exit after a repair and the one exit for an unplaced citation | tools/tests/test_repair_design_citations.py; tools/documentation/repair_design_citations.py
```

### `tools/tests/test_retire_archive.py`

```
TagNameTest.test_names_the_tag_by_the_day | keep | 9 | retire_archive: tag_name puts the ISO day after the tag prefix | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
IgnoreLineTest.test_adds_the_line_to_an_empty_file | keep | 9 | retire_archive: with_ignore_line adds the archive line to an empty file | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
IgnoreLineTest.test_appends_the_line_after_the_existing_ones | keep | 9 | retire_archive: with_ignore_line appends the archive line after the existing ones | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
IgnoreLineTest.test_writes_nothing_when_the_archive_is_already_ignored | keep | 9 | retire_archive: with_ignore_line returns None when the archive is already ignored | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
PlanTest.test_reports_nothing_to_retire_when_no_archive_file_is_tracked | keep | 9 | retire_archive: plan reports nothing to retire when no archive file is tracked | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
PlanTest.test_lists_each_citation_and_blocks | keep | 9 | retire_archive: plan lists each citation and blocks the retirement | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
PlanTest.test_a_dry_run_names_the_plan_and_acts_on_nothing | keep | 9 | retire_archive: a dry run names the plan and acts on nothing | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
PlanTest.test_apply_acts_and_says_what_was_staged | keep | 9 | retire_archive: apply acts and says what was staged | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
RetireTest.test_a_dry_run_changes_nothing | keep | 9 | retire_archive: a dry run changes nothing | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
RetireTest.test_apply_tags_unstages_and_ignores_and_keeps_the_files | split | 3 | retire_archive: apply tags, unstages, ignores and keeps the files; split into the tag, the unstage, the ignore line and the kept files | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
RetireTest.test_refuses_while_something_cites_the_archive | keep | 9 | retire_archive: the command refuses while a citation of the archive remains and stages nothing | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
RetireTest.test_is_quiet_when_the_archive_is_already_gone | keep | 9 | retire_archive: the command is quiet when the archive is already gone | tools/tests/test_retire_archive.py; tools/documentation/retire_archive.py
```

### `tools/tests/test_summarize_dispatches.py`

```
SummarizeDispatchesTest.test_reads_only_dispatch_lines | keep | 9 | summarize_dispatches: parse reads only the dispatch lines | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
SummarizeDispatchesTest.test_a_line_without_a_rung_is_on_the_first | keep | 9 | summarize_dispatches: a dispatch line without a rung is on the first rung | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
SummarizeDispatchesTest.test_totals_per_model_and_effort | keep | 9 | summarize_dispatches: summarize totals runs, passes, turns and escalations per model and effort | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
SummarizeDispatchesTest.test_table_names_the_columns_then_one_row_per_seat | keep | 9 | summarize_dispatches: the summary table names its columns, then one row per seat | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
SummarizeDispatchesTest.test_no_dispatch_line_in_any_report_says_so | keep | 9 | summarize_dispatches: no dispatch line in any report says so | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
ReportsOnDiskTest.test_main_sums_only_the_reports_under_agent_and_archive | keep | 9 | summarize_dispatches: main sums only the reports under docs/agent and docs/archive | tools/tests/test_summarize_dispatches.py; tools/routing/summarize_dispatches.py
```

### `tools/tests/test_test_budget.py`

```
TestReadingAndNames.test_reads_times_and_leaves_out_a_skipped_test | keep | 9 | test_budget: parse_junit reads each test time and leaves out skipped tests | tools/tests/test_test_budget.py; tools/testing/test_budget.py
TestReadingAndNames.test_refuses_a_file_with_a_doctype_or_an_entity | keep | 9 | test_budget: parse_junit refuses a file with a DOCTYPE or an ENTITY | tools/tests/test_test_budget.py; tools/testing/test_budget.py
TestReadingAndNames.test_finds_the_suite_and_size_of_a_plain_and_a_parametrised_name | keep | 9 | test_budget: suite_and_size finds the suite and size of a plain and a parametrised name | tools/tests/test_test_budget.py; tools/testing/test_budget.py
TestReadingAndNames.test_reads_the_exemption_table | keep | 9 | test_budget: parse_exemptions reads the exempt table | tools/tests/test_test_budget.py; tools/testing/test_budget.py
TestReadingAndNames.test_reads_the_program_map | keep | 9 | test_budget: parse_programs reads the program map | tools/tests/test_test_budget.py; tools/testing/test_budget.py
TestReadingAndNames.test_the_shape_counts_a_case_by_its_name_or_its_size_property | rewrite | 1 | test_budget: the shape line counts a case by its name or its size property; the test reaches the limits through judge(), which patches the process-wide K_BUDGET of a small test; pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_run_inside_every_limit_has_no_finding | rewrite | 1 | test_budget: evaluate finds nothing for a run inside every limit; the test patches the process-wide K_BUDGET of a small test through judge(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_large_test_has_no_time_limit_and_counts_in_the_shape | rewrite | 1 | test_budget: evaluate leaves a large test out of the time limits and counts it in the shape; the test patches K_BUDGET of a small test through judge(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_test_over_its_limit_is_named_for_a_rerun_and_judged_by_the_rerun | rewrite | 1 | test_budget: evaluate names a test over its limit for a rerun and judges it by the rerun; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_module_small_total_is_printed_and_never_a_finding | rewrite | 1 | test_budget: evaluate prints the small total of a module and never makes it a finding; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_the_default_run_is_judged_by_wall_time_when_given | rewrite | 1 | test_budget: evaluate judges a default run by wall time when it is given; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_partial_run_judges_no_whole_run_limit | rewrite | 1 | test_budget: evaluate judges no whole-run limit of a partial run; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_an_exempt_test_is_left_out_and_a_stale_exemption_is_a_finding | rewrite | 1 | test_budget: evaluate leaves an exempt test out and reports a stale exemption; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_an_exemption_needs_an_open_backlog_id | rewrite | 1 | test_budget: evaluate needs an open backlog ID for an exemption; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestEvaluate.test_a_run_that_did_not_rebuild_says_so_and_a_count_is_printed | rewrite | 1 | test_budget: evaluate says a run that did not rebuild and prints the count of added cases; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestRendering.test_prints_the_rerun_line_and_exits_clean_without_gate | rewrite | 1 | test_budget: render prints the rerun line and the run exits clean without a gate; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestRendering.test_gate_exits_one_on_a_finding_and_a_run_that_did_not_rebuild_never_gates | rewrite | 1 | test_budget: exit_code fails a gated rebuilt run with a finding, and never a run that did not rebuild; the test patches K_BUDGET of a small test through run(); pass the limits to evaluate | tools/tests/test_test_budget.py; tools/testing/test_budget.py; settings.py
TestMainCommand.test_reads_the_junit_and_the_program_map_and_gates_the_run | keep | 9 | test_budget: the command reads the JUnit file and the program map and gates the run | tools/tests/test_test_budget.py; tools/testing/test_budget.py
```

### `tools/tests/test_test_times_settings.py`

```
TestTimesSettingsTest.test_the_skill_table_matches_the_settings | keep | 9 | settings: the Time table of the testing skill matches K_TEST_TIMES | tools/tests/test_test_times_settings.py; tools/settings.py; skills/testing/SKILL.md
TestTimesSettingsTest.test_reads_milliseconds_seconds_and_a_thousands_space_only_under_the_heading | resize | 8 | settings: read_times reads milliseconds, seconds and thousands spaces only under the Time heading; the function takes text, so the test is small | tools/tests/test_test_times_settings.py; tools/settings.py
TestTimesSettingsTest.test_names_each_key_that_differs | resize | 8 | settings: differences names each key whose value differs; pure text and values, so small | tools/tests/test_test_times_settings.py; tools/settings.py
TestTimesSettingsTest.test_every_row_of_the_table_has_a_constant | keep | 9 | settings: every row of the Time table has a settings constant | tools/tests/test_test_times_settings.py; tools/settings.py
```

### `tools/tests/test_tolerance_header.py`

```
ToleranceHeaderTest.test_the_self_check_compiles_and_every_promise_holds | split | 3 | tolerance: the C++ self-check of tolerance.hpp compiles and each promise of the header holds; one test names one promise, so split the self-check into one check per promise | tools/tests/test_tolerance_header.py; tools/testing/support/tolerance.hpp
```

### `tools/tests/test_write_license_block.py`

```
RewriteTest.test_replaces_an_old_box | keep | 9 | write_license_block: rewrite replaces an old boxed licence block and keeps the file block one blank line below | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_replaces_a_box_without_copyright | keep | 9 | write_license_block: rewrite replaces a boxed block that names no holder | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_replaces_a_slash_block | keep | 9 | write_license_block: rewrite replaces a leading slash-comment block that holds a copyright line | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_inserts_above_a_file_block | keep | 9 | write_license_block: rewrite inserts the block above a file block | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_a_leading_comment_that_is_no_licence | keep | 9 | write_license_block: rewrite keeps a leading comment that is not a licence | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_replaces_old_hash_lines | keep | 9 | write_license_block: rewrite replaces old hash lines and leaves the docstring below | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_shebang_and_encoding_lines_first | keep | 9 | write_license_block: rewrite keeps a shebang and an encoding line above the block | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_inserts_above_a_docstring | keep | 9 | write_license_block: rewrite inserts the block above a module docstring | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_an_ordinary_leading_comment | keep | 9 | write_license_block: rewrite keeps an ordinary leading comment of a CMake file one blank line below the block | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_writes_an_empty_file | keep | 9 | write_license_block: rewrite writes the block alone into an empty file | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_newline_style_and_byte_order_mark | split | 3 | write_license_block: rewrite keeps CRLF newlines and a leading byte order mark; split into the newline style and the byte order mark | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_is_idempotent | keep | 9 | write_license_block: rewrite changes nothing on a second run for every opening | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_writes_the_closed_lines | keep | 9 | write_license_block: rewrite writes the reserved-rights lines and no grant in a closed repository | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py; tools/documentation/licence.py
RewriteTest.test_appends_upstream_lines | keep | 9 | write_license_block: rewrite appends a ported file's upstream notice below the repository's lines | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_upstream_lines_on_a_plain_rerun | split | 3 | write_license_block: rewrite keeps a ported file's upstream rows on a plain rerun; split into the rerun and the replacement by a newly named upstream | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_drops_foreign_rows_of_an_old_block | keep | 9 | write_license_block: rewrite carries nothing over from an old block that lacks this repository's licence lines | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_keeps_upstream_rows_of_the_narrow_box | keep | 9 | write_license_block: rewrite keeps the upstream rows of the narrow box the writer produced before | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_reads_templates_and_include_fragments_as_c_family | keep | 9 | write_license_block: is_source gives templates and include fragments the block of the file they become | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_replaces_an_indented_old_box | keep | 9 | write_license_block: rewrite replaces an old boxed block whose rows are indented | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_widens_the_box_for_a_long_line | keep | 9 | write_license_block: rewrite widens the box for a long line and keeps every row the same width | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RewriteTest.test_uses_the_year_it_is_given | keep | 9 | write_license_block: rewrite writes the year it is given into the copyright line | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
ParseFirstYearsTest.test_first_year_follows_a_rename | keep | 9 | write_license_block: parse_first_years dates a renamed file from the commit that first added it | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
PlanChangesTest.test_plans_only_the_candidates_whose_text_would_change | keep | 9 | write_license_block: plan_changes plans only the candidates whose text would change | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RepositoryTest.test_report_writes_nothing_and_run_converges | split | 3 | write_license_block: the report writes nothing, the run writes once, and the report then passes; split into the report, the write and the converged report | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RepositoryTest.test_writes_a_file_that_is_staged_and_not_yet_committed | rewrite | 8 | write_license_block: a file staged and not yet committed gets its block dated this year; the expected year is read from the real clock with date.today(), and the writer reads the same clock inside pending, so the test depends on wall-clock time; pass the year to pending and test with a fixed year | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RepositoryTest.test_skips_a_tracked_file_deleted_from_the_working_tree | keep | 9 | write_license_block: a tracked file deleted from the working tree is skipped | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py
RepositoryTest.test_output_passes_the_checker | keep | 9 | write_license_block: the output passes the license block rule of the checker | tools/tests/test_write_license_block.py; tools/licensing/write_license_block.py; tools/documentation/check_source_comments.py
```

## Adds

Promises a header or a port states that no test checks: `unit: promise | oracle | size`.

```
claude_block: raises ValueError naming the template when it holds no block | spec, a template without a block | small
apply_to_claude: leaves a CLAUDE.md that has the heading byte for byte unchanged | byte comparison before and after | medium
alias_of: returns None when the manifest has no alias line | spec | small
main: prints the names added and whether the block was written | captured stdout against the file state | medium
main: --alias overrides the manifest alias | spec | medium
missing_settings: a name that only prefixes a defined name, or sits in a comment, is still missing | spec | small
source comments: a file opens with its @file block or its module docstring | in memory: a file with and without the block | small
source comments: a symbol comment block longer than the ceiling is reported | in memory: a long block and a short one | small
source comments: a separator line inside a comment outside the licence is reported | in memory: a separator inside a comment and inside the licence | small
source comments: a TODO-style tag or history word inside a comment is reported | in memory: a comment holding a tag and a clean comment | small
docs layout: a live document not named in UPPER_SNAKE_CASE is reported | in memory: a mixed-case document name | small
docs layout: a malformed work folder or a foreign file inside a work folder is reported | in memory: a bad folder name and a foreign file | small
docs layout: a design document longer than the design ceiling is reported | in memory: a document one line over the ceiling | small
docs layout: a module folder without README.md is reported | in memory: a module folder with and without a README | small
layering: an include or build line that reaches another module's source/ is reported | in memory: an include of a sibling's source folder | small
design topics: rule_modules_exist, rule_modules_required, rule_topic_folder and rule_work_references report the tooling package findings; delegated, so the promise belongs to the package and this repository holds only the bridge contract | disk through the tooling bridge with the package installed | medium
history: git returns None when a git command fails | real repository with a failing command | medium
history: commits_since leaves out merge commits | real repository with a merge commit in the range | medium
history: commits_since returns the commits it has when git cannot read the range | real repository with an unknown base | medium
copy_shared_tools: shared_files lists the community files of upstream | committed upstream holding .github community files | medium
design_status: read_tree reads the docs tree and the module READMEs into values | real temporary tree | medium
design_views: state_of names a shipped, superseded or withdrawn topic by its status word | literal text | small
design_views: modules_with_designs lists each module that a topic names once, in order | literal text | small
fold_design_topics: relink leaves an absolute path or a scheme link alone | literal text | small
licence: copyright_line matches the copyright row of the holder in any year and no other | literal text | small
write_license_block: main exits two and names the form when --upstream is malformed | contract on stderr and exit code | small
```
