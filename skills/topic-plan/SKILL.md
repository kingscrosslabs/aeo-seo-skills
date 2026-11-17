---
name: topic-plan
description: Proposes the next cluster of 8–12 pages for the user's site from real search data: what to write, the target query for each, which existing page it supports, and the order to ship them. Pulls Search Console and keyword data from OpenSEO in one batch, checks the query bank and user questions so nothing is planned twice, and records the approved plan as a decision. Use when the user says "what should we write about", "plan topics", "topic cluster", "content plan for SEO", "keyword plan", or "what pages should we build". Not for writing the pages (use blog-post and the other page skills).
---

# Topic Plan

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

Turns search data, the query bank and real user questions into a short, ordered plan of pages that link into each other. It writes nothing on the site. Each approved row is handed to the page skill that builds it.

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

## Step 2: Map what exists

<!-- TODO -->

## Step 3: Find candidates

<!-- TODO -->

## Step 4: Pull search data (one batch)

<!-- TODO -->

## Step 5: Propose the plan (approval gate)

<!-- TODO -->

## Step 6: Record the plan

<!-- TODO -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
