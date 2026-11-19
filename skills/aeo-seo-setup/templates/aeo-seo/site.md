# Site

The facts about the website itself. The skills read this to know where pages go, how to check and ship them, and what the site already does on its own.

<!-- aeo-seo-setup fills most of this by reading the repo and the live site. Leave a comment wherever there's no answer yet. -->

## Basics

- **Domain:** <!-- The canonical host, with or without www. Example: https://www.ledgerly.dev -->
- **Brand suffix:** <!-- What the site appends to every <title>, with its spaces. Example: " | Ledgerly". The skills keep title + suffix at 60 characters or fewer -->
- **Primary goal:** <!-- What search should produce. Example: signups from non-branded search, in Google and AI answer engines -->
- **Languages and regions:** <!-- Example: English, US first -->

## Stack

- **Framework and hosting:** <!-- Example: Next.js App Router on Vercel -->
- **Repo and app folder:** <!-- Example: this repo, apps/web -->
- **Dev server:** <!-- Command and local URL. Example: `npm run dev`, http://localhost:3000 -->
- **Design system:** <!-- Where shared components live, so pages never get one-off styling. Example: src/components, shown at /design-system -->

## Where each page type lives

| Page type | URL pattern | Source file or folder | Copy this one |
|---|---|---|---|
| Blog post | <!-- /blog/<slug> --> | <!-- content/blog/<slug>.md --> | <!-- content/blog/_templates/how-to.md --> |
| Comparison page | <!-- /compare/<competitor> --> | <!-- src/app/compare/<competitor>/content.ts --> | <!-- the best existing one --> |
| Feature page | <!-- /features/<feature> --> | | |
| Use-case page | <!-- /use-cases/<slug> --> | | |

<!-- Delete rows for page types the site doesn't have yet. The page skills offer to create the first one. -->

- **List of every page:** <!-- The file the skills read for internal links. Example: src/lib/routes.ts, or the live /sitemap.xml -->
- **Authors:** <!-- Who can be bylined, where their bios live, and who writes what. Example: src/lib/authors.ts; code-heavy posts go to the CTO -->

## Commands

| Step | Command | Notes |
|---|---|---|
| Scaffold a post | <!-- npm run blog:new <type> <slug> --> | <!-- Leave empty if there's none; the skill copies the template by hand --> |
| Check a page | <!-- npm run blog:check <slug> --> | <!-- What it validates: title length, links, frontmatter --> |
| Build | <!-- npm run build --> | <!-- Anything to avoid, e.g. a build that pings IndexNow --> |

## Shipping

- **How a page goes live:** <!-- Example: blog posts push to main, which auto-deploys; every other page goes to a branch and a pull request for review -->
- **Never:** <!-- Example: never push main from someone else's branch; never link to a draft post -->
- **After deploy:** <!-- What to check. Example: the page and its .md mirror both load -->

## What the site does automatically

<!-- So the skills don't hand-edit these. Tick what exists; `aeo-seo-technical-audit` adds what's missing. -->

- [ ] Sitemap
- [ ] robots.txt
- [ ] `llms.txt` / `llms-full.txt`
- [ ] A Markdown mirror of each page (`/<path>.md`)
- [ ] JSON-LD (Article, FAQPage, BreadcrumbList, Organization)
- [ ] Open Graph and share images
- [ ] RSS
- [ ] IndexNow ping on deploy
- [ ] Canonical tags and one canonical host

## Search data

- **OpenSEO project:** <!-- Project name, as it shows in OpenSEO. The skills look up its ID with `list_projects` -->
- **Search Console property:** <!-- Example: sc-domain:ledgerly.dev -->
- **Bing Webmaster Tools:** <!-- Connected or not -->

### New domain setup checklist

<!-- One-time, by hand, for every domain. `aeo-seo-technical-audit` asks about anything unticked and fills in the dates. -->

- [ ] Verified in Google Search Console <!-- date -->
- [ ] Sitemap submitted in Google Search Console <!-- date -->
- [ ] Verified in Bing Webmaster Tools, sitemap submitted <!-- date -->
- [ ] Submitted to Brave Search (https://search.brave.com/submit-url) <!-- date -->
- [ ] IndexNow pings Bing on every production deploy <!-- date -->
- **Credit budget:** <!-- Example: about 25 credits per page and 300 per weekly batch; stop paid calls at a balance of 100 -->
