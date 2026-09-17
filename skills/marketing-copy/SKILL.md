---
name: marketing-copy
description: Use when writing, editing or reviewing any text that sells or presents a Sushi Systems company, product or person to outsiders, in English or Turkish - a website hero, an about or team page, a product page, a pitch deck, an investor email, a press release, a social post, a store listing. Load humanizer as well; this skill adds what marketing needs on top of it.
---

# Marketing Copy

Marketing copy that sounds generated is banned. Readers who believe a brand's copy was written
by a model trust the brand less and recommend it less, whatever the copy's quality (sources in
`research/english_sources.md`). Investors read pitches for a living and spot the pattern fastest.
The damage is worse for a young company: it has no reputation to absorb it.

`humanizer` already removes the general tells of generated prose. This skill covers what goes
wrong only when the text is trying to sell: slogans, decorative jargon, vision without evidence,
invented scenes.

## The ban

Copy containing any of these does not ship.

1. **Slogan rhythm.** Three short declaratives in a row ("We build. We simulate. We deliver."),
   closed triples of adjectives, an imperative stack ("Explore. Create. Discover.").
2. **Jargon as decoration.** A standard, an algorithm or a library named for a reader who cannot
   know what it buys them. WGS84 on a hero means something to a handful of engineers and
   nothing to an investor.
3. **Claims with nothing to picture.** "Real scale", "next generation", "limitless", "seamless",
   "yenilikçi", "sınırları zorlayan". If the reader cannot see what happens, it says nothing.
4. **The swap test fails.** Replace the product's name with a competitor's. If the sentence is
   still true, delete it.
5. **Invented facts or scenes.** A number, a customer, a benchmark or a demo scene the owner did
   not supply. Write `[number]` and ask.
6. **Superlatives with no comparison.** "Best", "most advanced", "world-class", "en gelişmiş".
7. **Vision standing alone.** The vision is kept whole and never shrunk, but it never appears
   without a verified fact on the same screen.
8. **Openness as a slogan.** "Anyone can read the code" stands in for a link to the code.

## How to write it instead

1. **Find the one true thing a non-specialist can picture.** "In SushiEngine you can travel from
   Pluto to Mercury in milliseconds" needs no background. It comes from the owner, is true, and
   can be shown in a video. A hero is built on a fact like this, never on a phrase.
2. **Put the evidence next to the claim.** A large claim is allowed when a fact sits beside it:
   a number with a unit, a date, a video, a link. Readers anchor on what they see first, so the
   first screen carries both.
3. **Give numbers a referent.** "12 metres of wingspan, 27 hours in the air" (Baykar) works
   because the reader knows what a metre and an hour feel like. A unit only an engineer knows
   needs a translation or a different page.
4. **Name people and dates.** First person, founders by name, what each built, since when. A
   dated timeline of what shipped says more than any adjective.
5. **Say what is not done.** "Designed, not yet built" beside the thing that is built makes both
   believable. Two-sided messages raise credibility; one-sided hype lowers it.
6. **Write for the reader who does not know.** The writer cannot unknow what they know, so they
   overestimate what the reader shares. Read the draft as the least technical person the page
   is for. Technical depth belongs on pages written for engineers, and even there each term is
   explained once.
7. **One category first.** Name the one thing the company is. Other lines of work appear as
   evidence for it, not as equal headlines.

## Language files

Read the file for the language before drafting. Each lists that language's marketing clichés and
ends with before and after pairs.

| File | Language |
| --- | --- |
| `english.md` | English |
| `turkish.md` | Türkçe |

## The pass

After `humanizer`'s pass, ask of every sentence:

- Can a smart non-engineer repeat it to a friend correctly?
- Does it survive the swap test?
- Would deleting it lose a fact, or only a mood?
- Is every fact in it one the owner supplied or a source confirms?
- Is there a fact on the same screen as every large claim?
- Would an engineer at a rival company nod, or wince?

## Red flags

- "This needs a punchier closing line."
- "A technical term here will sound credible."
- "I'll write a plausible number and they can fix it."
- "Three short sentences give it rhythm."
- "The vision is inspiring enough on its own."
