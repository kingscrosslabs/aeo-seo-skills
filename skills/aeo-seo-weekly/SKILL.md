---
name: aeo-seo-weekly
description: Runs the site's weekly AEO/SEO routine: reads Search Console and Bing, checks how many new pages got indexed and sets the pace, proposes this week's queries from the query bank and fresh search data, lists the existing pages to update (including the December year rollover), and logs everything. Nothing ships until the user approves the week's queries. Use when the user says "run the weekly SEO", "weekly AEO", "this week's SEO", "AEO/SEO weekly", or when a weekly scheduled task fires.
---

# AEO/SEO Weekly

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

One run a week that turns last week's search data into this week's work: which queries to target, which pages to update, and what to fix. It proposes; the user approves; the page skills build. It can run unattended up to the approval gate.

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

## Step 2: Read the numbers

<!-- TODO -->

## Step 3: Indexing and pacing

<!-- TODO -->

## Step 4: Pages to update

<!-- TODO -->

## Step 5: Propose this week's queries (approval gate)

<!-- TODO -->

## Step 6: Hand off to the page skills

<!-- TODO -->

## Step 7: Log and report

<!-- TODO -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
