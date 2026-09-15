# Plain English

This register is English for a reader whose English is good but not native: CEFR B1 to B2, often
reading through a translation tool, often in a hurry. The rules come from the Council of Europe
CEFR Companion Volume, Cambridge's English Grammar and Vocabulary Profiles, Nation's vocabulary
coverage research, ASD-STE100 Simplified Technical English, ISO 24495-1, the European
Commission's *How to write clearly*, GOV.UK, Kohl's *Global English Style Guide*, and the
Crossley and McNamara studies of simplified texts. Sources are in
`research/plain_english_sources.md`.

Plain English sits on top of `generic_english.md`. Every rule there still holds; this file adds
the rules for a reader who stops at words and structures a native reader passes without noticing.

The hard part is that the result must not read like a graded reader. The CEFR describes a B2
reader as someone who reads "with a large degree of independence". That reader is an adult
engineer, not a child. Research on simplified texts shows that cutting every sentence short and
removing every connective makes text *harder*: the reader loses the links that say why one fact
follows another. Keep the logic; remove the obstacles.

Three rules subsume most of the rest:

1. **Use the common word, and use it every time.** Pick the word a B1 reader knows, give each
   concept one term, and never swap it for a synonym to avoid repetition. "The cache… the store…
   the buffer" is three things to a reader who is translating.
2. **One idea per sentence, but keep the word that joins the ideas.** Split a sentence that holds
   two claims. Keep `because`, `so`, `but`, `if`, `after`, `instead`, which carry meaning a
   translation tool can map.
3. **Say it literally.** No idiom, no sports or war metaphor, no cultural joke, no phrasal verb
   with a hidden meaning. If the words do not mean what they say one by one, rewrite.

## Grammar: what a B1–B2 reader handles

The left column lists structures learners usually meet by B2. A B2 reader
recognises most of the left side and some of the right; a translation engine handles the left
side far better than the right. Use the left. Use the right only where the alternative is clumsy.

| Use (B1–B2) | Avoid (C1 and above, or a known MT failure) | Rewrite |
| --- | --- | --- |
| Present, past, future simple; present perfect | Future perfect continuous; tense stacked for nuance | "will have been running for" → "has run for … by then" |
| `can`, `must`, `should`, `might` | `ought to`, `needn't`, `shall` (except in a spec), `would` as politeness | "You needn't restart" → "You do not need to restart" |
| First and second conditionals with `if` | Inverted conditional: "Should it fail", "Had we known"; mixed conditionals | "Should the build fail" → "If the build fails" |
| Active voice; passive when the actor is unknown | Passive with no actor that hides who acts; `get` passive | "It was decided" → "The team decided" |
| Full relative clause: "the file that the tool writes" | Reduced relative: "the file written"; dropped `that`: "the file the tool writes" | Keep `that`/`which` and the verb |
| Two sentences, or `and`/`but`/`because` | Participle clause: "Having built the set, the pass…"; absolute: "The set built, …" | "After the pass builds the set, it…" |
| Plain subject–verb–object | Cleft for emphasis: "What matters is…", "It is the cache that…" | "The cache matters" |
| Normal word order | Negative inversion: "Never has…", "Not only does…", "Little did…" | "The tool has never…" |
| Positive statement | Negative question: "Doesn't it work?"; double negative: "not uncommon" | "Does it work?"; "common" |
| Short noun phrase, one modifier | Noun stacks: "render graph barrier insertion policy" | "the policy for inserting barriers in the render graph" |
| `-ing` form as a clear noun: "Testing takes an hour" | `-ing` form that could be adjective or verb: "Loading files can fail" | "Files can fail to load" / "The load step can fail" |
| Explicit subject in every clause | Ellipsis: "Works on Linux; not tested on Windows" in prose | "It works on Linux. We did not test it on Windows" |
| `for example`, `that is` | `e.g.`, `i.e.`, `viz.`, `cf.`, `etc.` in running text | Write the words |

Contractions: `don't`, `it's` and `can't` are fine in chat and email; they read friendly and B1
readers know them. In documentation and anything likely to be machine translated, write the full
form.

## Vocabulary

**Frequency.** Nation's research shows a reader needs about 95% of the words in a text to follow
it and about 98% to read it with ease. For a B1–B2 reader that means almost every word should
come from the most frequent 2,000–3,000 word families (the Oxford 3000, the New General Service
List). Technical terms are the exception: the reader knows `buffer`, `thread`, `commit` better
than `nonetheless`. Spend your uncommon words on the domain, not on style.

**Latinate formal words → common words.** Most of these are C1 in the English Vocabulary
Profile, and they carry no extra meaning here.

| Instead of | Write |
| --- | --- |
| utilise, leverage, employ | use |
| commence, initiate | start |
| terminate | stop, end |
| subsequently | then, later |
| prior to | before |
| in order to | to |
| approximately | about |
| sufficient | enough |
| facilitate | help, make possible (or name the action) |
| ascertain | find out, check |
| endeavour | try |
| nonetheless, notwithstanding | but, still |
| whereby | where, by which (or split the sentence) |
| aforementioned | this, that, the (name it again) |

**One term per concept.** Define the term the first time, then repeat it exactly. STE gives
every approved word one meaning and one part of speech; you do not need STE's word list, but
take its discipline. Do not use one word for two things either: `run` as "execute", "a test
run" and "the loop runs out" in one page is three meanings.

**Ambiguous words.** Some common words mean opposite things in different places. Kohl and the EU
guide flag these:

| Word | Problem | Write |
| --- | --- | --- |
| sanction | "allow" and "punish" | approve / penalty |
| table (a motion) | UK "discuss now", US "postpone" | discuss / postpone |
| moot | "open to debate" and "no longer relevant" | open question / no longer relevant |
| once | "one time" and "after" | after, when |
| since | "because" and "from that time" | because / from |
| while | "during" and "although" | during / although |
| as | "because", "when", "like" | because / when / like |
| should | advice or expectation | must / we expect |
| billion | older UK usage 10¹² | the number, or "thousand million" |

**False friends.** Many readers translate from a European language or Turkish. Words that look
familiar can mislead: `actual` (means *real*, not *current*), `eventually` (means *in the end*,
not *possibly*), `sympathetic` (means *feeling sorry*, not *likeable*), `control` (in EU usage
often *check/inspect*), `assist` (in French and Spanish readers' ears *attend*). When you need
the meaning that the false friend suggests, use the unambiguous word: `current`, `possibly`,
`check`.

**Phrasal verbs.** A phrasal verb whose meaning is not the sum of its parts is an idiom. It
confuses readers and MT engines. Replace it with a single verb when the single verb is also
common:

| Phrasal verb | Single verb |
| --- | --- |
| find out | discover, learn (keep *find out* in chat) |
| put off | delay, postpone |
| carry out | do, run |
| come up with | create, suggest |
| figure out | understand, solve |
| look into | investigate, check |
| get rid of | remove |
| run into (a problem) | have, see ("we saw an error") |
| turn down | refuse, reject |
| bring up | mention, raise |
| go over | review |
| point out | show, note |
| set off | start, trigger |
| back up (support) | support |

Keep the phrasal verb when it is the normal word, the single verb is rarer or more formal, and
the meaning is literal or standard in the field: `set up`, `log in`, `sign up`, `back up` (data),
`shut down`, `start up`, `look up` (a value), `pick up` (a change), `roll back`, `check out` (a
branch), `clean up`, `turn on`/`turn off`, `go back`, `find out` in a friendly email. Replacing
these with `configure`, `authenticate`, `deactivate` or `ascertain` makes the text colder and
often harder. When you keep one, keep the parts together: "set up the server", not "set the
server up" (Kohl).

## Sentence length and rhythm

- **Target an average of 15–20 words**, with most sentences between 8 and 25. STE caps procedural
  sentences at 20 words and descriptive sentences at 25; treat those as limits, not targets.
- **Vary the length.** A text where every sentence is 9 words is choppy: the reader must build
  every link alone, and it sounds like a machine or a children's book. Mix an 18-word sentence
  that explains with a 7-word sentence that states the result.
- **The not-choppy test.** Read two neighbouring short sentences. If a native writer would join
  them with `because`, `so`, `but` or `which`, join them. "The cache is cold. The first frame is
  slow." → "The first frame is slow because the cache is cold."
- **One instruction per sentence** in steps. Put the condition first: "If the build fails, run
  `se clean`", not "Run `se clean` if the build fails".
- **Paragraphs of two to five sentences.** STE caps a descriptive paragraph at six.
- Readability formulas (Flesch–Kincaid and similar) count only word and sentence length. A text
  can score well and still be hard: idioms, pronouns and missing connectives are invisible to
  them. Use them as a warning light, never as proof.

## Idioms, metaphors and cultural references

Say what happens, in the literal words. Humour, sports and war metaphors, pop culture and local
references do not survive translation and exclude readers who did not grow up with them.

| Instead of | Write |
| --- | --- |
| a ballpark figure | a rough estimate |
| out of the box | by default, without changes |
| on the same page | agree, have the same information |
| low-hanging fruit | the easy changes, the quick fixes |
| move the needle | make a measurable difference (give the number) |
| hit the ground running | start work immediately |
| a home run / a slam dunk | a clear success |
| touch base, circle back | talk again, reply later |
| under the hood | internally, in the implementation |
| a silver bullet | a single fix for everything |
| bite the bullet | accept the cost |
| kill two birds with one stone | solve both problems with one change |
| the elephant in the room | the problem nobody mentions (name it) |
| it's not rocket science | (delete; it is also patronising) |
| pain point | problem |
| deep dive | detailed look |

Standard technical metaphors that are now literal terms stay: `bug`, `thread`, `pipeline`,
`garbage collection`, `hot path`, `cache hit`. The test is whether a dictionary of the field
lists the word with that meaning.

## International conventions

- **Dates.** Write `16 September 2026` in prose, or ISO `2026-09-16` in technical text. Never
  `09/10/26`: it means different days in the US and in Europe.
- **Times.** 24-hour clock with the time zone: `14:00 UTC`.
- **Numbers.** Digits for all measurements and for numbers from 10 upward. Use a comma for
  thousands and a full stop for decimals, and say which convention you use if the document is
  for a region that swaps them. Avoid `a couple of`, `a handful`, `dozens`: give the number.
- **Units.** SI units with a space: `12 ms`, `4 GB`, `20 °C`. Do not rely on `feet`, `pounds`,
  `Fahrenheit` without the SI value.
- **Spelling.** Choose US or UK spelling for the document and keep it. Mixing `colour` and
  `color` makes a reader wonder if they are different words.
- **Money.** ISO code before the amount: `EUR 40`, `USD 1,200`.
- **Abbreviations.** Spell out the first use: "render hardware interface (RHI)". Drop Latin
  abbreviations in running text.
- **Names and titles.** No `Mr/Mrs` guesses, no `Dear Sir`. Use the person's name as they write
  it.

## Cohesion

Simplification studies found that learners understand texts best when the links between ideas
stay visible. Elaborated texts (the original plus added explanation) help comprehension about as
well as simplified ones, and they keep the natural language the reader will meet later.

- **Keep connectives that carry logic:** `because`, `so`, `but`, `however`, `if`, `unless`,
  `after`, `before`, `instead`, `for example`. These are B1 words and MT handles them well.
- **Cut connectives that only decorate** (`moreover`, `furthermore`, `additionally`), exactly as in
  `generic_english.md`.
- **Repeat the noun when a pronoun could point to two things.** "The pass writes the image to the
  buffer, then it is cleared" → "…then the buffer is cleared". Repetition is a feature here, not a
  style fault.
- **Avoid `this` alone as a subject.** "This causes a stall" after a paragraph with three
  candidates → "This extra copy causes a stall".
- **Keep `that` after `say`, `think`, `show`, `mean`.** "The log shows that the lock was held" is
  easier to parse than "The log shows the lock was held".
- **Put the known thing first**, the new thing last (old before new, from `generic_english.md`).
  It matters more for a reader who processes each sentence slowly.

## Tone: organic, not graded

A plain text still sounds like a person. The failures below are how "simple mode" goes wrong,
especially in generated text:

- **Patronising.** "Don't worry!", "It's easy!", "Simply click…", "As you may know". Treat the
  reader as a colleague who reads a second language.
- **Over-explaining.** Defining `file` or `button`. Explain the domain term the reader may not
  know; trust the rest.
- **The repeated explainer.** "This means that…" or "In other words…" after every sentence. If the
  first sentence needed a rewrite, rewrite it.
- **Bullet spam.** Turning every paragraph into bullets to look simple. Bullets remove the
  connectives, which is the part the reader needed. Use bullets for real lists and steps.
- **Word-limit robot.** Every sentence the same short length, no `because`, no `but`, articles
  dropped ("Click button. Open file."). That is telegram style, not plain English.
- **Exclamation and emoji** to sound friendly. Friendliness in plain English comes from `you`,
  `we`, a direct answer and a thank you where one is due.
- **Globish flattening.** A 1,500-word ceiling forces paraphrases like "the machine that makes
  cold" for `refrigerator`. A common specific word beats a circle of basic words.

Use `you` and `we`. Use present tense. Write the way a fluent colleague explains something to a
smart new team member from another country.

## Record types

**Documentation.** Imperative for steps, present tense for descriptions. One term per concept,
defined on first use; a glossary link for anything domain-specific. Numbered steps, one action
each, condition before action. No contractions.

**Email.** Put the request or the answer in the first two sentences. Give the deadline as a
date with a time zone. One topic per email. Contractions are fine. Close with a concrete next
step or with the name, not "Please do not hesitate to reach out".

**Chat reply.** Answer first. Short is fine; telegram is not: keep articles and the verb.
Contractions and common phrasal verbs (`find out`, `look at`) are fine.

**UI text.** Verb first on buttons: `Save changes`, `Delete file`. No idioms, no humour in error
messages. An error says what happened and what to do: "The file is too large. The limit is
20 MB." Keep strings whole: do not build a sentence from pieces, because translators and MT
cannot reorder them.

**Commit message and PR description.** The rules in `generic_english.md` hold. Plain English adds:
common verbs in the subject (`Fix`, `Add`, `Remove`, `Move`, not `Rectify`, `Introduce`,
`Excise`); no noun stacks; spell out the abbreviation the reviewer may not share.

## How it layers with the generic rules

Run `generic_english.md` first: it removes the generated posture. Then run this file: it
removes the obstacles for a non-native reader. Where they meet:

- Both cut `moreover`, `robust`, `leverage`, and hidden verbs.
- Generic English allows a four-word sentence after a thirty-word one; plain English keeps that
  variety but caps the long one at about 25 words.
- Generic English lets you pick the precise uncommon word; plain English asks whether a common
  word is as precise, and uses it if so.
- Generic English warns against repeated words as flat rhythm; plain English repeats the noun
  on purpose when a pronoun would be unclear. Repetition of a term wins; repetition of a
  sentence shape still loses.

## Before and after

C1 native to organic B1–B2:

> Before: Should the nightly job fall over again, we'll need to circle back and figure out
> whether it's the cache that's the culprit, since the numbers we got last week were pretty
> ballpark.
> After: If the nightly job fails again, we need to check whether the cache causes it. Last
> week's numbers were only rough estimates, so they cannot answer that yet.

> Before: Having migrated the shaders, the team was able to get rid of the legacy path, not
> only cutting build times but also freeing up a sizeable chunk of disk.
> After: After the team moved the shaders, they removed the old code path. Builds now take
> 6 minutes instead of 9, and the build folder uses 3 GB less disk space.

> Before: It's the lock, not the allocator, that's been holding things up.
> After: The lock causes the delay. The allocator does not.

Robotic simple to organic:

> Before: The tool is fast. The tool uses a cache. The cache is on disk. This means that the
> tool is fast. Don't worry, it's easy!
> After: The tool is fast because it keeps a cache on disk and reuses it on the next run.

> Before: Click button. File opens. Check file. Save file.
> After: Click **Open**. When the file opens, check the values in the first table, then click
> **Save**.

> Before: Memory is a place where the computer keeps things. The program uses a lot of it. In
> other words, the program needs a lot of memory.
> After: The program needs about 8 GB of memory for a large scene. On a machine with less, it
> starts to swap and slows down.
