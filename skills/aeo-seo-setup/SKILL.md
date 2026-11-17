---
name: aeo-seo-setup
description: Builds or updates the site's AEO/SEO profile (an aeo-seo/ folder in the website's repo), the files every AEO/SEO skill reads first - the website, the product, competitors, standing decisions, and the banks of queries, first-hand experience, user questions, link targets and research. Reads the repo and the live site, connects the OpenSEO project and Search Console, links docs the user already has instead of copying them, and interviews only for what's missing. Shows every file for approval and never overwrites without a diff. Use when the user says "set up AEO", "set up SEO", "AEO/SEO setup", "set up my site for the SEO skills", "onboard my website", "create my aeo-seo folder", or when another AEO/SEO skill reports that no site profile exists.
---

# AEO/SEO Setup

Builds the `aeo-seo/` folder that every other skill in this repo reads before doing anything: what the site is, how its pages get made and shipped, what the product is and who it's for, who it competes with, what's already been decided, and the research so far. Most of it comes from reading the repo and the live site; the user only answers what those can't. This skill doesn't fix the site or write pages: missing site-wide pieces (sitemap, `llms.txt`, JSON-LD) go to `aeo-seo-technical-audit`, and the first pages come from `topic-plan`.

**The finished folder:**

```
aeo-seo/
├── README.md            # index: which file each skill reads
├── site.md              # domain, stack, page locations, commands, shipping, what's automatic, search data
├── product.md           # what it is, who it's for and not for, differentiators, voice, fact sources
├── competitors.md       # sourced, dated competitor facts
├── aeo-seo-log.md       # Decisions table + dated log
├── query-bank.md        # queries considered or targeted, with search data
├── experience-bank.md   # first-hand stories, data, quotes (approved or pending)
├── user-questions.md    # real questions from forums and Reddit
├── link-targets.md      # places worth pitching
└── research/            # one report per page + serps/ cache
```

**Minimum for the other skills to run:** `site.md`, `product.md` and `aeo-seo-log.md`. The banks can start empty.

## Where the templates are

Every file is written from the templates in this skill's `templates/aeo-seo/` folder, so they install with the skill. If that folder is missing, read them from GitHub (`kingscrosslabs/aeo-seo-skills`, folder `skills/aeo-seo-setup/templates/aeo-seo/`).

Keep each template's headings and order. Replace the guidance comments with real answers. Leave a comment in place wherever there's no answer yet, and delete the fictional examples once a section has real content.

**The overwrite rule, for this whole skill:** never change an existing file without first showing a diff and getting a yes. Linked files outside the `aeo-seo/` folder are read-only.

## Step 1: Check what exists

1. **Find the profile.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:`. Otherwise check for `aeo-seo/README.md` in the project.
2. **If you find one,** read its README and every file it lists, then report in a few lines: which minimum files exist, which sections still hold template comments, which banks have entries, and anything the README links to that you couldn't open. Offer: **fill the gaps** (recommended), **update one file**, or **start over in a new folder**. Never rebuild an existing profile in place.
3. **If you find nothing,** confirm this is the website's repo (or ask where it is) and where the folder should go. Default: `aeo-seo/` at the project root, or next to the site's content folder in a monorepo.

## Step 2: Connect OpenSEO

OpenSEO is required. Without it the other skills stop.

1. Run `whoami`. If the MCP isn't connected, stop and give the user the setup steps from this repo's README.
2. Run `list_projects` and find the project for this domain. If there isn't one, offer to create it with `create_project`.
3. Check Search Console with `list_search_console_sites`. If the project has no property, help the user pick one and connect it with `set_search_console_site`.
4. Read `get_project_context`. Anything already there (goal, positioning, competitors, key pages) is a starting answer, not something to ask again.

All of these calls are free. Don't run paid research in this skill.

## Step 3: Read the repo and the live site

Fill as much of `site.md` as you can before asking anything. Say what you found and where.

- **Stack:** framework, hosting, app folder, dev server command and port (from `package.json`, config files, deploy config).
- **Page types:** find the blog, comparison, feature and use-case pages, if any. For each, record the URL pattern, the source file or folder, and the best existing page to copy.
- **Commands:** any scripts to scaffold or check content, and any build step with side effects (a postbuild ping, a deploy).
- **Shipping:** how changes go live (push to main, pull requests, a CMS), from the README, CI config or git history.
- **What's automatic:** fetch the live site's `/sitemap.xml`, `/robots.txt`, `/llms.txt` and one page's HTML, and tick each item in the checklist that exists. Note the canonical host (www or not) from the redirects.
- **Fact sources:** files that hold pricing, live features, approved claims and docs. These go in `product.md` → "Where the true facts live".

## Step 4: Link what already exists

Ask once: "Do you already have docs that cover any of this?" Positioning or strategy docs, a brand or voice guide, a competitor file, a keyword sheet, an existing SEO log.

For each one, add a row to the README's "Files that live somewhere else" table instead of copying it. Create a file in `aeo-seo/` only for what's still missing.

## Step 5: Interview for the gaps

Run the rounds in `references/interview.md`, two or three questions at a time, skipping anything Steps 2–4 already answered (say which). Use the user's own words in the files.

## Step 6: Seed the log and the query bank

Free data only:
- `get_search_console_performance` for the last 28 days. Add a `[baseline]` entry to `aeo-seo-log.md`: impressions, clicks, average position, pages indexed if known.
- The top queries the site already gets impressions for go into `query-bank.md` with source `search-console`, grouped into clusters.
- Every choice the user made in the interview that should hold over time (audiences to skip, queries to avoid, how pages ship) goes into the Decisions table with today's date.

## Step 7: Write and approve

Show each file before writing it, the minimum three first. On approval, write it. For files that already exist, show a diff.

If the folder isn't at `aeo-seo/` in the project root, add `AEO/SEO profile: <path>/README.md` to the project's CLAUDE.md or AGENTS.md (show the line first).

If the user runs more than one site, offer to add this one to an `AEO/SEO sites:` list in their global CLAUDE.md or AGENTS.md (`<name>: <path to README.md>`).

## Quality check

Before calling it done:
- `site.md`, `product.md` and `aeo-seo-log.md` exist, with no template comments left in Basics, "What it is", "Who it's for" and "Where the true facts live".
- Every linked file opens.
- The OpenSEO project and Search Console property are named in `site.md`.
- No fact in `product.md` came from you rather than the user or a source file.

## Related skills

- `aeo-seo-technical-audit`: next, when the "What the site does automatically" checklist has gaps.
- `topic-plan`: next, to pick the first cluster of pages.
- `aeo-seo-weekly`: once pages are live, the weekly routine.
