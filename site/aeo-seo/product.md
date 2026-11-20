# Product

What the site sells, who it's for, and how to talk about it. Every page the skills write is aimed at the reader described here and uses only the facts this file points to.

The full brand (strategy, audience, positioning, voice, vocabulary, claims rules) is in `../BRAND.md`. This file is the short version. When the two disagree, `../BRAND.md` wins.

## What it is

AEO-SEO Skills is a free, open-source (MIT) set of agent skills that do AEO (answer engine optimization) and SEO as one job. They run in Claude Code, Codex, Cursor and any agent that reads `SKILL.md` files, and they plan topics, audit the site and write pages that rank in Google and get quoted by ChatGPT, Perplexity and Google AI Overviews.

## Who it's for

Founders and marketers at small companies who own their website and already use an AI coding agent. They can run a terminal command. They don't have an SEO team and don't want an agency. They believe AI search matters now and that their site isn't showing up in it. They're skeptical of SEO tools that guess numbers, AI content that reads like AI content, and anything that publishes without asking.

## Who it isn't for

- Agencies looking for a white-label content mill.
- Anyone who wants pages shipped without reading them.

## What makes it different

- **AEO and SEO are one job.** Every page is written answer-first, so it ranks and still makes sense when it's quoted out of context.
- **Real data, never guessed.** Search numbers come from OpenSEO and Google Search Console. If the data isn't connected, the skill stops.
- **You approve the work.** Briefs and pages wait for a yes before they ship.
- **Your context stays yours.** Everything about your site lives in an `aeo-seo/` folder in your project, and updating the skills never touches it.
- **Free and open source.** MIT licence.

## Voice

The King's Cross Labs company voice: direct, specific, proof over promise, builder to builder. The brand rules, the vocabulary table and the banned words are in `../BRAND.md` → Voice. In short: say what the skill does in one plain sentence before saying why it matters, name the real engines and tools, use short sentences, prefer colons to dashes, and use no exclamation marks.

## Where the true facts live

| Fact | Source of truth |
|---|---|
| Pricing | Free, MIT (`../../LICENSE`). There is no paid tier and no pricing on the site (`../BRAND.md` → Calls to action) |
| What's live vs. coming soon | Each skill's `status` in `../src/data/site.ts`, which must match the repo `README.md` |
| Approved claims and FAQs | The `faqs` in `../src/data/site.ts`, and `../BRAND.md` → Governance → Claims |
| What the product actually does | Each skill's `SKILL.md` in `../../skills/`, and the repo `README.md` |

## Proof you can cite

- Built by Mika Reyes at King's Cross Labs. These are the skills KCL uses every week on its own products (`../BRAND.md`).
- <!-- GitHub stars and install counts, once they're worth citing, with a date. -->
