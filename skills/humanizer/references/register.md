# Humanizer: register, rationale and red flags

Read this when a draft feels off, or to choose a register. The rules are in `../SKILL.md`.

## Why

Generated prose is recognisable not by any one word but by its posture: it fills a shape
instead of stating a fact. The reader who clocks that posture stops trusting the specific
claims and skims for the gist, which defeats the point of writing carefully. The vocabulary
tells decay every year or so; the three rules underneath them do not. "Significantly faster"
and "oldukça hızlı" are opinions, so rule 1 asks for the number.

## Language files

Read the file for the language and register you are writing in before the draft, not after.
They are not translations of each other; each language and register has its own tells. The
generic file is the default. Use another register only when the owner or the task asks for it.

| File | Language | Register |
| --- | --- | --- |
| `generic_english.md` | English | Default: documentation, commits, PRs, design notes, chat replies |
| `plain_english.md` | English | CEFR B1–B2, international readers, plain and organic |
| `hood_english.md` | English | Informal street and internet English |
| `generic_turkish.md` | Türkçe | Varsayılan: belge, commit, PR, tasarım notu, sohbet yanıtı |
| `hood_turkish.md` | Türkçe | Sokak, argo ve internet Türkçesi |

Every file ends with before/after pairs. Sources and the corpus evidence behind the word lists
are in `research/`, one sources file per register.

## The pass

Write the draft, then reread it against the checklist for its language. Most drafts need a
handful of cuts and one or two restructured sentences, not a rewrite. Run every draft against the
cross-language checklist of tells (openers, filler connectives, copula avoidance, em dashes,
closings and the rest) in `checklist.md`; read it with the language file on the first draft of a
session. Two structural checks that no word list catches: read only the first sentence of each
paragraph and confirm the argument survives; and count sentences that assert nothing anyone would
dispute, then delete them.

## Register

A commit message is terser than a design note; a chat reply looser than a PR description; a
guide speaks to *you*, an architecture chapter describes what *the renderer* does. The tells
apply everywhere; how much polish a piece gets scales with its formality. Do not over-craft a
one-line status.

In the generic registers, never inject forced personality, slang, or "casual" texture to
compensate. The hood registers exist for when informal speech is the job, and their own files
say how to do it without caricature. The goal is not to sound human; it is to say the true thing
once, in the plainest words that carry it, so that nothing stands between the reader and the point.

## Uncertainty

Assert what you verified. Name what you did not, once, where it applies, with what would
resolve it. Qualifiers sprinkled over every sentence read as evasion; confident claims about
unchecked things read as lying. Both are failures of the same rule.

## Red flags

If you notice yourself thinking any of these, stop and run the pass:

- "This connector makes it flow better."
- "A third item would round out the list."
- "I'll soften this with 'may' so I'm not wrong."
- "The reader might not realise this is important, so I'll say it's crucial."
- "A dash here reads more elegant." (In Turkish, a dash here reads as machine translation.)
- "A summary paragraph would be thorough."
