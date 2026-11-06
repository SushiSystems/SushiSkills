# Licence change: spec

**Status:** Open — the open repositories are under Apache 2.0; the closed-product drafts wait for a lawyer

The owner changed the licences of Sushi Systems on 2026-11-06. The ten open repositories moved from the
PolyForm Noncommercial License 1.0.0 to the Apache License 2.0, and every version they published under
PolyForm is now under Apache 2.0 as well. That part is done and pushed. SushiEngine and Project mobileRTS
stay closed, and they gain two promises to the people who use them: a right to maintain and repair the
binary, and a sunset clause that opens the product when Sushi Systems is gone and has no successor.

This page holds the decisions and the draft clauses for those two products. The drafts are not a licence.
They go to a lawyer first, and nothing in either repository changes until the reviewed text comes back.

## Decisions

The owner made these on 2026-11-06.

1. Open repositories use the Apache License 2.0. It grants a patent licence and ends it for anyone who
   sues over the code, which protects the individual developers the code is meant for.
2. Every version published under PolyForm Noncommercial is also licensed under Apache 2.0. Nobody who
   holds an older tag is bound by the noncommercial terms.
3. SushiEngine and Project mobileRTS stay proprietary. Whoever lawfully holds their binary may maintain
   and repair it, without a right to take the code into anything else.
4. Both products carry a sunset clause. When Sushi Systems ceases to exist and it is confirmed that it
   has no successor, the product is released to the public.
5. On sunset, SushiEngine is released under the Mozilla Public License 2.0. A changed engine file stays
   open, so no company can take the engine, close it and sell it, and a game made with the engine may
   still use any licence and be sold.
6. On sunset, Project mobileRTS releases its code under the Mozilla Public License 2.0 and the art, sound
   and music Sushi Systems owns under Creative Commons BY-NC-SA 4.0. Players and modders may use and
   change the assets; nobody may sell them.

## Why the clauses are shaped this way

**The grant is made now, not at sunset.** When a company is dissolved or goes bankrupt, its intellectual
property passes to a liquidator or to creditors, who may sell it to the highest bidder. A promise to open
the code "later" can be lost in that sale. A licence granted today to the public, irrevocable and taking
effect on a stated condition, binds whoever later acquires the rights. The draft is written that way.

**The product goes to everyone, not to one party.** A single heir, person or company can itself be bought.
A public release under MPL-2.0 cannot be taken back. A non-profit may be named as steward of the code, but
the licence does not depend on it.

**The source must exist on the day.** A licence to code nobody can reach is worth nothing. The source and
its build instructions are deposited with an escrow agent or a named trustee, refreshed at each release,
and the trustee publishes them when the condition is met. The trustee also confirms the condition.

**Repair rights start from the law and go further.** In the EU, Directive 2009/24/EC, Articles 5(1) and 6,
already lets a lawful user correct errors and decompile for interoperability, and a contract cannot take
that away. The draft names these rights plainly and adds the ones the law leaves out: sharing a patch, and
running a game's servers when the official ones close.

**A game dies when its servers close.** For Project mobileRTS the repair right includes running community
servers, and Sushi Systems publishes what those servers need before it shuts its own.

## Draft clauses

The two products share the definitions and the sunset clause. The repair grant differs only where the
game has servers.

### Definitions

- **Licensor**: Sushi Systems and Mustafa Garip, the holders of the copyright in the Product.
- **Product**: SushiEngine or Project mobileRTS, as the licence names it, in the form the Licensor
  distributes it.
- **Binary**: the Product in executable or object form, with its data files.
- **Lawful Holder**: anyone who obtained a copy of the Binary from the Licensor or with its permission.
- **Repair Purpose**: finding and correcting a defect; keeping the Product working on hardware, an
  operating system, a driver or a service that changes; fixing a security weakness; removing or replacing
  a dependency on a service the Licensor no longer runs.
- **Repair Patch**: a file that changes a copy of the Binary for a Repair Purpose and holds no more of the
  Binary than it needs to find the place it changes.

### Right to maintain and repair

1. The Licensor grants every Lawful Holder a worldwide, royalty-free, non-exclusive licence, for as long
   as they hold the copy, to run, study, debug, decompile and disassemble the Binary, and to change their
   own copy, for a Repair Purpose.
2. A Lawful Holder may make Repair Patches and share them, free of charge or for a fee, with anyone, for
   use on copies other Lawful Holders hold.
3. This licence does not permit:
   - distributing the Binary, or a substantial part of it, outside a Repair Patch;
   - using code, structure or information obtained under it in any other product, including an engine or
     a game that competes with the Product;
   - removing a copyright, licence or attribution notice;
   - using a trademark of the Licensor, or presenting a Repair Patch as made or approved by the Licensor.
4. The Licensor will not use a technical protection measure, or a law that protects one, against an act
   this licence permits.
5. Nothing here limits a right the Lawful Holder has under the law that applies to them.

### Community servers (Project mobileRTS only)

6. A Lawful Holder may run servers for the game and let other Lawful Holders connect to them. A server may
   ask players for money only to cover what it costs to run.
7. At least 90 days before the Licensor stops running the official servers, it publishes the server
   software in Binary form, or a description of the protocol complete enough to write a compatible
   server, under the terms of clauses 1 to 5.

### Sunset

8. **Sunset Event.** A Sunset Event happens when both of these are true:
   - the Licensor has been dissolved, struck off or liquidated, or has carried on no business for twelve
     months in a row; and
   - no successor has taken over the rights in the Product and gone on distributing or supporting it,
     as the Trustee confirms after a public notice of six months asking any successor to come forward.
   The Licensor may also cause a Sunset Event at any time by a written declaration that it has ended the
   Product.
9. **Grant.** The Licensor grants, today, irrevocably and to everyone, a licence that takes effect on the
   Sunset Event:
   - for SushiEngine: its source code, under the Mozilla Public License 2.0;
   - for Project mobileRTS: its source code under the Mozilla Public License 2.0, and the art, sound and
     music the Licensor owns under Creative Commons Attribution-NonCommercial-ShareAlike 4.0.
   Third-party parts keep their own licences and are not covered.
10. **Binding on successors.** This grant binds every assignee, acquirer, liquidator, administrator and
    creditor of the Licensor. Any transfer of rights in the Product is made subject to it.
11. **Deposit.** The Licensor deposits the source code, the owned assets and the build instructions of
    each release with the Trustee, at the latest 30 days after the release.
12. **Trustee.** The Trustee is a person or organisation the Licensor names in writing, with a substitute.
    On a Sunset Event the Trustee publishes the deposit in a public place with clause 9's licences.
13. **No trademark.** The sunset licence grants no right to the Licensor's names or marks. Released code
    may not be called SushiEngine or Project mobileRTS without permission.

## Questions for the lawyer

1. Is a licence granted today to the public, taking effect on a condition, valid and enforceable under
   Turkish law (FSEK) without each licensee accepting it, and does it bind a buyer in a bankruptcy or
   liquidation under the İİK?
2. Does Mustafa Garip need to sign as a holder beside Sushi Systems, and what happens to his share on
   his death? Should his will name the Trustee?
3. Which trustee form fits best: a commercial source-code escrow agent, a foundation (vakıf), or named
   people with substitutes? Who confirms the Sunset Event, and how is a false confirmation prevented?
4. Do clauses 1 to 5 agree with FSEK Article 38 and with the EU directive where the Product is sold in
   the EU, and does clause 4 need narrower wording?
5. Do the App Store and Google Play terms allow a custom licence with these clauses for Project
   mobileRTS, or must it sit beside the store's standard licence?
6. Do Unity's terms limit releasing the game's own code and assets under clause 9? Unity itself and Asset
   Store packages are never released, and the draft excludes them.
7. Is "only to cover what it costs to run" in clause 6 clear enough to enforce, or should a community
   server be free of charge?
8. In clause 2, should a fee for a Repair Patch be allowed, or should patches be free?

## What follows the review

1. The reviewed text becomes the `LICENSE` of SushiEngine and of Project mobileRTS, and the licence the
   game's store pages and SushiHub's binary installs show.
2. The owner names the Trustee and sets up the deposit.
3. The `sushisystems-licence` skill gains the closed products' licence rows, and the closed licence block
   names `LICENSE` in place of "No licence is granted".
4. The brand skill says what copy may claim about these two products.
