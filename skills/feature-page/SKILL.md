---
name: feature-page
description: 'Writes or updates a feature page on the user''s site: one page for one integration ("<platform> API", "<tool> integration") or one capability of the product. Checks every claim against the code or docs, drafts answer paragraphs, feature cards and FAQs, wires the page in, previews it, and hands off for review. Use when the user says "feature page", "product page", "integration page", "capability page", or "page for <feature>". Not for use-case pages (use use-case-page) or comparison pages (use comparison-page).'
---

# Feature Page

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

Tells a buyer exactly what the product does for one integration or one capability, using only facts the code or docs already back. It doesn't write pages about kinds of customers (that's `use-case-page`).

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

## Step 3: Research

<!-- TODO -->

## Step 4: Outline (approval gate)

<!-- TODO -->

## Step 5: Draft

<!-- TODO -->

## Step 6: Check and preview

<!-- TODO -->

## Step 7: Final review (approval gate)

<!-- TODO -->

## Step 8: Ship

<!-- TODO -->

## Updating an existing feature page

<!-- TODO: when to update instead of writing a new page (already ranking at positions 5–20, a fact changed, 30%+ overlap with a new topic, the December year rollover for titles with a year), and how: start from research/<slug>.md, re-check facts and quotes, set the updated date, log it. -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
