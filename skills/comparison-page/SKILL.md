---
name: comparison-page
description: Writes or updates a comparison page on the user's site: "<competitor> alternative" or "<product> vs <competitor>". Researches the queries and AI prompts people use, re-fetches and dates every competitor claim, shows only the dimensions where the user's product is actually stronger, puts where the competitor fits in a "Stay with <X> if you" box, and adds question-form sections, quotable answers, a comparison table, FAQs and schema. Use when the user says "comparison page", "compare page", "<competitor> alternative page", "<X> vs <Y> page", or "refresh the compare pages". Not for listicles comparing several tools (use blog-post).
---

# Comparison Page

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

One page per competitor that wins "<competitor> alternative" and "<competitor> vs <product>" searches and is the page AI engines quote when someone asks for an alternative. Every competitor fact is sourced and dated, and the page never links to the competitor.

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

## Step 2: Intake

<!-- TODO -->

## Step 3: Target queries

<!-- TODO -->

## Step 4: Source and verify

<!-- TODO -->

## Step 5: Page plan (approval gate)

<!-- TODO -->

## Step 6: Draft

<!-- TODO -->

## Step 7: Check and preview

<!-- TODO -->

## Step 8: Final review (approval gate)

<!-- TODO -->

## Step 9: Ship

<!-- TODO -->

## Updating an existing comparison page

<!-- TODO: when to update instead of writing a new page (already ranking at positions 5–20, a fact changed, 30%+ overlap with a new topic, the December year rollover for titles with a year), and how: start from research/<slug>.md, re-check facts and quotes, set the updated date, log it. -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
