---
name: aeo-seo-foundations
description: Audits and fixes the site-wide pieces search engines and AI engines need: sitemap, robots.txt, llms.txt and llms-full.txt, a Markdown mirror of each page, JSON-LD (Organization, Article, FAQPage, BreadcrumbList), canonical host and tags, Open Graph images, and an IndexNow ping on deploy. Checks the live site, reports what's missing, and implements fixes on a branch for review. Use when the user says "AEO foundations", "technical SEO", "set up llms.txt", "make my site readable by AI", "schema markup", or when aeo-seo-setup finds gaps.
---

# AEO/SEO Foundations

> **Draft scaffold.** The method for this skill is being moved in. Sections marked TODO are empty.

Makes the whole site easy to crawl, index and quote, once, so every page the other skills write inherits it. It changes site code, not page copy.

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

## Step 2: Audit the live site

<!-- TODO -->

## Step 3: Report and plan (approval gate)

<!-- TODO -->

## Step 4: Implement

<!-- TODO -->

## Step 5: Check

<!-- TODO -->

## Step 6: Ship

<!-- TODO -->

## Quality check

<!-- TODO -->

## Related skills

<!-- TODO: skills in this repo only -->
