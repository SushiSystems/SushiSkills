# Backlog and design tool: report

**Implements:** the plan beside this report, waves 0 to 6.

The plan ran inline in one session. Nothing was pushed: every commit and tag below is local.

## What was built

sushicore 0.10.0 added the `backlog` and `design` command groups and `sushicore.citations`;
0.10.1 and 0.10.2 fixed four faults the moves found. The three tags are local.

| Commit | Repository | What |
| --- | --- | --- |
| `99082b8` | sushicore | The two groups, the citation rewriter, their tests and reference pages |
| `dd5f433` | sushicore | Its own backlog moved with `backlog import` |
| `ba97b51` | sushicore | v0.10.0 |
| `2519694` | sushicore | `import` rewrites Markdown pages only and lists the code that names a retired file |
| `d073811` | sushicore | A topic under `_REVISION/` owns no module; `--json` prints ASCII |
| `31e4355` | sushicore | v0.10.1 |
| `4557b96` | sushicore | `import` rebases the relative links of the prose it moves into a detail file |
| `c99e96c` | sushicore | v0.10.2 |
| `a088495` | SushiSkills | The backlog store in the `documentation` skill, the checkers as calls into sushicore |
| `e473a65`, `93182ef` | SushiSkills | Two checker fixes the moves found |

The sushicore suite passed with 1449 tests and one skip at v0.10.0. The design and backlog tests
passed again at v0.10.2, and `check_all` is clean in both repositories.

## The moves

Each repository was moved with `backlog import`, given the SushiSkills checkers, and checked with
`check_all`. A repository whose branch was in use by another session was moved on a new branch,
`docs/backlog-store`, in a separate worktree, and the branch was left for the owner to merge.

| Repository | Where | Entries (work, issues) | `check_all` after |
| --- | --- | --- | --- |
| sushiweb | main, `8d90f7d4`, `185fe4dd` | 102, 25 | the two failures it had before |
| sushilog | main, `fa52635` | 12, 3 | clean |
| sushiprofiler | main, `439543a` | 18, 1 | clean |
| sushitrack | main, `52264b2` | 17, 2 | clean |
| sushistack | main, `0639d95` | 51, 13 | the five failures it had before, and `check_module_install` (RW-57) |
| sushidsp | main, `6cbc9cfd` | 73, 19 | `check_test_mirror` (RW-79) |
| project-mobilerts | main, `63a2a95d0`, `2337843ae` | 132, 6 | the test mirror, probe and deck findings (RW-145) |
| sushiruntime | `docs/backlog-store`, `07823694` | 69, 13 | clean |
| sushiblas | `docs/backlog-store`, `aa91e969` | 115, 19 | clean |
| sushiai | `docs/backlog-store`, `bb3eba6f` | 115, 4 | clean |
| sushiengine | `docs/backlog-store`, `93e27ba63` | 193, 20 | 14 of the 15 checkers that failed before; `check_backlog` now passes |

A failure after a move that was not there before comes from a shared checker the copy brought,
not from the move; each has a work entry in that repository's backlog.

In project-mobilerts only `docs/`, `tools/` and the module READMEs were committed; the Unity
assets that were changed in the working tree were left as they were.

## Design decisions taken under the delegation

- sushiruntime: `PHYSICS_SUBSTRATE_REQUIREMENTS` is a page of `LAYERED_EXECUTION`, which owns the
  scheduler both named.
- sushiai: `PROFILING` keeps the modules it instruments and no other topic names; the graph and
  the programs stay with `GRAPH_CAPABILITIES` and `LAYERED_EXECUTION`.
- project-mobilerts: every topic was given its folder, an `**About:**` line and a `**Modules:**`
  line naming its `Assets/MobileRTS/Features/` folder; `BALANCE` and `REPOSITORY_LAYOUT` name
  none.
- sushiengine: `VOLUMETRIC_CLOUDS` is a page of `ATMOSPHERE_SYSTEM`. Each of the 37 shared modules
  was given to the topic that builds it. The six programme topics (`COUPLED_PLANET`,
  `ROAD_TO_PROJECTFS`, `SOLID_DOMAIN`, `SOLID_RENDER_AND_ASSET`, `RENDER_OPTIMIZATION`,
  `UNIFIED_HAZARD_MODEL`) name none, since each spans modules other topics own. The editor and
  the five core render modules (`render`, `render_passes`, `render_device`, `render_resources`,
  `render_scene`) have no owning topic; `AMBIENT_OCCLUSION` owns its own folder inside
  `render_passes`. Topics under `_REVISION/` own nothing until they are rewritten.

## Left for the owner

- Merge `docs/backlog-store` in sushiruntime, sushiblas, sushiai and sushiengine.
- Push the commits and the tags `v0.10.0`, `v0.10.1` and `v0.10.2` of sushicore. The CI of every other
  repository installs `sushicore[typer]>=0.10.0` from PyPI, so it fails until the tag push
  publishes the release.
- `sushiruntime-cli` 0.4.0 pins `sushicore==0.9.2` and `sushilog-cli` 0.1.0 pins
  `sushicore==0.9.0`; pip reports both conflicts on every install of sushicore 0.10.
- sushiengine has 66 backlog areas from its old sections; `backlog area merge` folds them.
- Whether the editor and the core render modules of sushiengine get one owning topic each.
