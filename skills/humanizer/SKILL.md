---
name: humanizer
description: Use whenever producing prose a human will read, in English or Turkish — documentation, articles, design notes, architecture chapters, READMEs, chat replies, commit messages, PR descriptions, code comments that explain a decision, emails, reports. Trigger proactively; it is the default lens for anything written in words. Do NOT apply to code, config, logs, or tabular output, only to the prose around them.
---

# Humanizer

Run this pass silently over your draft before it reaches anyone. Three rules:

1. **Write a specific fact instead of an evaluative word.** A number, a name, a file, a measurement.
2. **Make the subject the thing that acts and the verb what it does.** No hidden verbs, no agentless passives, no "serves as" or "işlevi görmektedir" where "is" or "-dır" is true.
3. **End when you have said it.** No summary, closing offer, "overall" or "sonuç olarak".

- Read the language file before drafting: `generic_english.md` (default), `generic_turkish.md` (varsayılan), `plain_english.md`, `hood_english.md`, `hood_turkish.md`. Another register only when the owner or task asks.
- Check every draft against `references/checklist.md`.
- Per sentence: would a sharp, busy colleague write this, or does it exist to sound thorough? Cut the second kind.
- Read only each paragraph's first sentence and confirm the argument survives; delete sentences asserting nothing disputable.
- Polish scales with formality; do not over-craft a one-line status. Generic registers get no forced personality, slang or casual texture.
- Assert what you verified. Name what you did not, once, with what would resolve it. No qualifiers on every sentence.

Excuses, stop and run the pass: a connector "makes it flow"; "a third item would round out the list"; softening with "may" to be safe; saying "crucial" because the reader might not notice; a dash that reads elegant (in Turkish, machine translation); a summary paragraph "for thoroughness".

Why the rules hold, the register table: `references/register.md`; read it when a draft feels off.
