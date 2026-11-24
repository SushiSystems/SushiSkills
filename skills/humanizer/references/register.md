# Humanizer: register and rationale

Read this when a draft feels off, or to choose a register. The rules are in `../SKILL.md`.

## Why

Generated prose is recognisable not by any one word but by its pattern: it follows an expected
form instead of stating a fact. A reader who notices that pattern stops trusting the specific
claims and skims for the gist, so the careful writing is wasted. The vocabulary
tells go out of date every year or so; the three rules underneath them do not. "Significantly faster"
and "oldukça hızlı" are opinions, so rule 1 asks for the number.

## Language files

The files are not translations of each other; each language and register has its own tells.

| File | Language | Register |
| --- | --- | --- |
| `generic_english.md` | English | Default: documentation, commits, PRs, design notes, chat replies |
| `plain_english.md` | English | CEFR B1–B2, international readers, plain and natural |
| `hood_english.md` | English | Informal street and internet English |
| `generic_turkish.md` | Türkçe | Varsayılan: belge, commit, PR, tasarım notu, sohbet yanıtı |
| `hood_turkish.md` | Türkçe | Sokak, argo ve internet Türkçesi |

Every file ends with before/after pairs. Sources and the corpus evidence behind the word lists
are in `research/`, one sources file per register.

## The pass

Write the draft, then reread it against the checklist for its language. Most drafts need a
few cuts and one or two restructured sentences, not a rewrite. `checklist.md` lists the
tells (openers, filler connectives, copula avoidance, em dashes, closings and the rest); read it
with the language file on the first draft of a session. The two structural checks catch what no
word list does.

## Register

A commit message is terser than a design note; a chat reply looser than a PR description; a
guide speaks to *you*, an architecture chapter describes what *the renderer* does. The tells
apply everywhere. The hood registers exist for when informal speech is the job, and their own
files say how to do it without mockery. The goal is not to sound human; it is to say the true thing
once, in the plainest words that state it, so that the reader gets the point without extra words.

## Uncertainty

Qualifiers added to every sentence read as evasion; confident claims about unchecked
things read as lying. Both are failures of the same rule.
