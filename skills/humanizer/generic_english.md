# English

The rules below come from the classic style authorities (Strunk, Orwell, Williams, Zinsser,
Pinker), the institutional guides (GOV.UK, Microsoft, Google developer docs, digital.gov), the
corpus studies of LLM vocabulary (Kobak et al. 2024, Liang et al. 2024, Juzek & Ward 2025) and
the Wikipedia "Signs of AI writing" catalogue. Sources are in `research/generic_english_sources.md`.

Three rules subsume most of the rest. If you keep nothing else, keep these:

1. **Put a specific fact where an evaluative word wants to go.** "significantly faster" is an
   opinion; "14 ms to 3 ms at p99" is a fact.
2. **Make the subject the thing that acts, and the verb what it does.** "Validation of the set
   is performed by the renderer" hides both; "the renderer validates the set" shows both.
3. **End when you have said it.** No summary that restates, no closing offer, no "overall".

## Sentence construction

- **Old before new.** Start a sentence with what the reader already holds; end it with the new
  thing. The last word of a sentence is its stressed position; put the word that matters there.
  Not "A 40% cut in frame time results from barrier batching, which landed last week" but
  "Barrier batching landed last week. It cut frame time by 40%."
- **Verbs, not nominalizations.** `initialization of` → `initializes`; `perform a validation` →
  `validate`; `make a decision` → `decide`. A hidden verb takes a helper verb with it
  (`perform`, `conduct`, `carry out`, `achieve`), and both go.
- **`is` and `has` are fine.** Corpus work measured a 10% drop in `is`/`are` in 2023 academic
  prose as LLMs replaced them with `serves as`, `stands as`, `represents`, `functions as`,
  `boasts`, `features`, `offers`. When the true verb is `is`, write `is`.
- **Passive is a tool, not a fault.** Use it when the agent is unknown or irrelevant, or when
  the patient is the topic that carries old information forward ("The set is validated at
  submission" in a paragraph about the set). Never use it to hide an accountable actor.
- **Sentence length varies on purpose.** Stylometry measures burstiness; generated prose is
  flat. If a paragraph runs 15–25 words per sentence throughout, break it. A four-word sentence
  after a thirty-word one is a human choosing where the weight goes.
- **Connectives carry logic or they go.** `but`, `so`, `because`, `then` say how one sentence
  follows another. `Moreover`, `Furthermore`, `Additionally`, `In addition` only claim that it
  does. If you cannot replace one with `and` or delete it, the sentences do not follow, and
  that is the actual problem.
- **Real parallelism only.** Coordinate items in matching grammatical form. Do not pad a pair
  into a triple; the third item is usually invented.
- **Sentences over ~25 words get a second look.** GOV.UK breaks them. Not a hard cap, but a
  long sentence should be long because it holds one long thought, not three short ones.

## Adjectives and adverbs

- An adjective earns its place by narrowing the set. `robust, comprehensive error handling` narrows
  nothing; `a retry loop with exponential backoff` is the noun the adjectives were standing in for.
  Prefer the specific noun to adjective + generic noun.
- Cut the adverb the verb already contains: `blare loudly`, `clench tightly`, `carefully
  validate`.
- Unquantified intensifiers are claims without evidence: `significantly`, `substantially`,
  `dramatically`, `considerably`, `greatly`. Each becomes a number or is deleted.
- Zinsser's qualifiers whittle trust: `very`, `quite`, `rather`, `a bit`, `sort of`, `somewhat`,
  `in a sense`, `pretty much`. Delete.
- `simple`, `easy`, `just`, `straightforward` about a task: Google bans them. The reader who
  finds it hard now also feels stupid.

## Vocabulary

Vocabulary tells decay; Wikipedia versions its list every twelve to eighteen months. Treat these
as symptoms of the underlying fault (filling a shape instead of stating a fact), not as a
regex.

**Measured excess (corpus ratios in Kobak 2024, Juzek & Ward 2025):** delve, underscore(s),
showcase/showcasing, crucial, pivotal, intricate, meticulous, tapestry, testament, interplay,
garner, bolster, enduring, vibrant, comprehensive, insights, notably, particularly, additionally,
align with, foster, enhance, highlighting, emphasizing, groundbreaking, boast, landscape, realm,
robust, seamless, leverage, harness, unlock, elevate, multifaceted, nuanced, myriad, plethora,
game-changer, potential (as a noun crutch), findings.

**GOV.UK replacements:** agenda→plan, deliver→make/provide, deploy→use, facilitate→name the
action, foster→encourage, impact→affect, key→important, leverage→use, robust→well thought out,
streamline→simplify, tackle→solve, transform→state the change, utilise→use, initiate→start,
empower→allow, collaborate→work with. Metaphor-as-verb: drive, hub, portal, ring-fence.

**Stock phrases:** it's important to note that; it's worth mentioning; note that (as an opener);
in today's fast-paced world; in the ever-evolving landscape of; plays a crucial/pivotal/key
role; serves as a testament to; stands as; whether you're a X or a Y; from X to Y (as a sweep);
generally speaking; to some extent; it could be argued that; at the end of the day; let's dive
in; in conclusion; overall; to summarize.

**Participial opinion tails.** A fact followed by `, highlighting…`, `, underscoring…`,
`, ensuring…`, `, reflecting…`, `, contributing to…`, `, demonstrating…`. The tail attaches an
unattributed judgment to the fact. Cut the tail or make it its own sentence with its own
subject.

**Vague attribution.** "Experts argue", "industry reports suggest", "observers have noted",
"it is widely recognised". Name the source or make the claim yourself.

## Discourse structure

These survive any vocabulary substitution, so they matter more than the word list.

- **Lead with the answer.** Do not restate the question. Do not signpost ("In this section we
  will examine…"). Examine it.
- **No corrective contrast.** `not just X but Y`, `it's not X, it's Y`, `X rather than Y` all
  pretend the reader held a wrong belief the sentence now overturns. Once per document is a
  rhetorical choice; twice is a template.
- **No false balance.** "While X has advantages, it also has drawbacks" is true of everything.
  Name the specific trade and who pays it.
- **Lists are lumpy.** Two items, or five, or four of unequal weight. A list of exactly three
  matched items, repeatedly, is the rule of three imposed on material that did not come in
  threes.
- **Paragraphs vary in length**, and a heading marks a real division. A heading per paragraph
  is decoration. Bold-header bullets (`**Term:** explanation`, down a whole list) are the
  listicle shape; write the paragraph instead.
- **The closing paragraph earns its place** with a decision, a next step or a caveat not yet
  stated. Otherwise stop at the last substantive sentence. Never "Let me know if you'd like me
  to expand on this" in a document.
- **Uncertainty is asymmetric.** Assert what you verified. Name what you did not, once, where it
  applies, with what would resolve it: "Not measured on the 3080 Ti; the golden run would settle
  it." Diffuse qualifiers on every sentence read as evasion; confident claims about things
  unchecked read as lying. Both are wrong.
- **No praise of the question**, no thanks for asking, no "excellent point".

## Punctuation

- **Em dash.** Human density is roughly 1–3 per thousand words; ChatGPT runs 8–15. The tell is
  not the mark but its repeated function: the appended hedge ("good approach — though limited")
  and the appended second clause ("does A — and also B"). Repair with a comma, a full stop, a
  parenthesis or a restructure. For a short piece the page count is useless; use this instead:
  at most one dash per ~300 words, and never two in one paragraph. Which repair depends on what
  the dash was doing: an aside → paired commas; an appended clause → full stop and a new
  sentence; a list or example introduction → colon; a single stressed word → colon or move it
  to the end of the sentence.
- **Colon** when the second half delivers what the first promised. Not before every list.
- **Semicolon** joins two independent clauses whose relation is closer than a full stop implies.
  Fine, underused; not a substitute for a full stop.
- **Oxford comma**: use it (Microsoft, Chicago).
- **Scare quotes** twice in a document means you are hedging on vocabulary instead of choosing
  it.
- **No exclamation marks** in documentation (Google). **No emoji** as formatting. **Bold** for
  the term being defined, not for the sentence you think is important; if it is important, put
  it first.
- Title case belongs to titles of works. Headings are sentence case.

## Record types

**Commit message** (Beams; Linux kernel). Subject line ≤ 50 characters, imperative, capitalised,
no trailing full stop; it must complete "If applied, this commit will ___". Blank line. Body
wrapped at 72, saying what and why, never how; the diff says how. One problem per commit. A
performance claim carries its number and its trade-off. The kernel's phrasing rule: write "as
if giving orders to the codebase", so `make xyzzy do frotz`, never `this patch makes`.

**PR description.** What changed; why it had to; what the reviewer should look at hardest; how
it was verified (the actual command, the actual output); what is knowingly left undone. The last
item is where honesty is cheapest and most valuable.

**API doc comment** (Go, Rust). A complete sentence beginning with the symbol's own name:
`Quote returns a double-quoted literal representing s.` "Reports whether", not "returns true
if". State errors, panics and the invariants the caller upholds, in their own sections, at the
place they bind. An example shows why you would call it, not that it can be called.

**Architecture decision record** (Nygard). Title is an imperative verb phrase ("Choose Postgres
for the ledger"). Context, decision, consequences. One decision per record. Append-only, dated;
supersede rather than edit, because the value is what was believed at the time.

**Design note / architecture chapter.** Declarative present tense. The tree as it is. Name the
type, the file, the number. History goes to the changelog.

**Chat reply.** Answer first. Register looser, rules identical. Length proportional to the
question.

## Before and after

> Before: It's important to note that the new caching layer significantly improves performance
> across a wide range of scenarios, serving as a robust foundation for future work.
> After: The cache cuts material resolve from 11 ms to 0.4 ms per frame at 5,000 entities.
> Nothing else depends on it yet.

> Before: The renderer not only handles barriers automatically — it also ensures correctness,
> ultimately reducing the burden on pass authors.
> After: The graph inserts barriers from each pass's declared reads and writes. A pass author
> declares those and nothing else.

> Before: Moreover, the readback is invalidated. Additionally, the meter is updated to reflect
> the current state.
> After: The readback is invalidated in the same call, so the meter shows the frame's real
> exposure instead of last frame's.
