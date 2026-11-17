---
name: blog-post
description: Researches, briefs, drafts and ships one SEO- and AEO-optimized blog post (how-to, listicle, explainer or changelog) on the user's site, with approval before drafting and before publishing. Uses real search data from OpenSEO, verbatim linked quotes from real users, first-hand experience from the site profile, and answer-first sections AI engines can quote. Also updates existing posts. Use when the user says "write a blog post", "blog post about <topic>", "SEO post", "AEO post", "update this post", "refresh this post", or names a query they want to rank for. Not for picking topics (use topic-plan) or comparison pages (use comparison-page).
---

# Blog Post

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

Writes one blog post that can rank in Google and be quoted by AI answer engines, from research to a live page. It works one post at a time and stops for approval twice: on the brief, and before publishing. It doesn't pick which posts to write (that's `topic-plan`) and doesn't make comparison pages (that's `comparison-page`).

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

## Step 4: Brief (approval gate)

<!-- TODO -->

## Step 5: Draft

<!-- TODO -->

## Step 6: Check and preview

<!-- TODO -->

## Step 7: Final review (approval gate)

<!-- TODO -->

## Step 8: Ship

<!-- TODO -->

## Updating an existing post

<!-- TODO: when to update instead of writing a new page (already ranking at positions 5–20, a fact changed, 30%+ overlap with a new topic, the December year rollover for titles with a year), and how: start from research/<slug>.md, re-check facts and quotes, set the updated date, log it. -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
