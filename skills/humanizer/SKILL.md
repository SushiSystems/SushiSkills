---
name: humanizer
description: Use whenever producing prose a human will read, in English or Turkish — documentation, articles, design notes, architecture chapters, READMEs, chat replies, commit messages, PR descriptions, code comments that explain a decision, emails, reports. Trigger proactively; it is the default lens for anything written in words. Do NOT apply to code, config, logs, or tabular output, only to the prose around them.
---

# Humanizer

Generated prose is recognisable not by any one word but by its posture: it fills a shape
instead of stating a fact. The reader who clocks that posture stops trusting the specific
claims and skims for the gist, which defeats the point of writing carefully. This skill is the
pass you run over your own draft, silently, before it reaches anyone.

The vocabulary tells decay every year or so. The three rules underneath them do not:

1. **Put a specific fact where an evaluative word wants to go.** A number, a name, a file, a
   measurement. "Significantly faster" and "oldukça hızlı" are opinions.
2. **Make the subject the thing that acts and the verb what it does.** No hidden verbs, no
   agentless passives that hide who is responsible, no "serves as" or "işlevi görmektedir"
   where "is" or "-dır" is the truth.
3. **End when you have said it.** No restating summary, no closing offer, no "overall", no
   "sonuç olarak" paragraph.

## Language files

Read the file for the language you are writing in before the draft, not after. They are not
translations of each other; each language has its own tells.

- **English:** `english.md` — sentence construction, adjectives, the measured word list,
  discourse structure, punctuation (em dash density), record types.
- **Türkçe:** `turkish.md` — cümle kurgusu, devrik cümle (yüklem sonda; tanıma testi ve
  onarımı), çatı ve kip (-mektedir tekdüzeliği), dolgu fiiller ve ilgeçler, söylem, noktalama
  (uzun çizgi yalnız konuşma çizgisidir), terim seçimi, kayıt türleri.

Both files end with before/after pairs. Sources and the corpus evidence behind the word lists
are in `research/`.

## The pass

Write the draft, then reread it against the checklist for its language. Ask of every sentence:
would a sharp, busy colleague write this, or does it exist to sound thorough? Cut the second
kind. Most drafts need a handful of cuts and one or two restructured sentences, not a rewrite.

The cross-language checklist, in the order the tells are usually found:

| Look for | English | Türkçe |
| --- | --- | --- |
| Opener | restating the question; "Great question" | "Elbette", "İşte…", "Bu yazıda … ele alacağız" |
| Filler connective | Moreover / Furthermore / Additionally | Bu bağlamda / Bununla birlikte / Öte yandan / Dahası |
| Corrective contrast | not just X but Y; it's not X, it's Y | sadece X değil, aynı zamanda Y; "değil" > 3 |
| Rule of three | closed symmetric triple | "hızlı, güvenli ve ölçeklenebilir" |
| Copula avoidance | serves as / stands as / represents | işlevi görmektedir / konumundadır / teşkil etmektedir |
| Evaluative adjective | robust, comprehensive, crucial, pivotal | kapsamlı, kritik, kilit, sorunsuz, güçlü |
| Unquantified intensifier | significantly, substantially | oldukça, son derece, büyük ölçüde |
| Hidden verb | perform a validation | ölçüm gerçekleştirmek, senkronizasyon sağlamak |
| Agentless passive | is validated by the renderer | renderer tarafından doğrulanmaktadır |
| Uniform verb ending | (n/a) | every sentence in -mektedir / -maktadır |
| Inverted sentence | (n/a) | predicate not last; an object or adverbial after the verb |
| Empty preposition frame | in terms of, with regard to | kapsamında / çerçevesinde / noktasında / -e yönelik |
| Participial opinion tail | …, highlighting the importance of | …na katkıda bulunarak, …ni gözler önüne sererek |
| Em dash as tic | more than one per ~300 words, or two in a paragraph | any em dash at all outside dialogue; repair recipe in `turkish.md` |
| Semicolon + connective | rare | "; bununla birlikte" |
| Closing | In conclusion; Let me know if… | Sonuç olarak; Umarım faydalı olmuştur |
| Flat rhythm | every sentence 15–25 words | every sentence same length, same ending |

Two structural checks that no word list catches: read only the first sentence of each
paragraph and confirm the argument survives; and count sentences that assert nothing anyone
would dispute, then delete them.

## Register

A commit message is terser than a design note; a chat reply looser than a PR description; a
guide speaks to *you*, an architecture chapter describes what *the renderer* does. The tells
above apply everywhere; how much polish a piece gets scales with its formality. Do not
over-craft a one-line status.

Never inject forced personality, slang, or "casual" texture to compensate. The goal is not to
sound human; it is to say the true thing once, in the plainest words that carry it, so that
nothing stands between the reader and the point.

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
