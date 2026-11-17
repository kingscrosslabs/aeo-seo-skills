# Conventions for aeo-seo-skills

How every skill in this repo is built. Read this before adding or editing a skill.

## The two layers

| Layer | Lives in | Holds | Changes when |
|---|---|---|---|
| **Method** | This repo, inside each skill | The steps, approval gates, research rules, AEO and SEO writing rules, quality checks. The same for every site. | Someone finds a better way to do the job, on any site |
| **Site profile** | The user's project, in `aeo-seo/` (built by `aeo-seo-setup`) | Facts about the website and the product, competitors, standing decisions, and the banks (queries, experience, user questions, link targets, research) | The site, the product or a decision changes |

A skill never hardcodes anything about one site: no domain, brand name, folder path, command, price or competitor. If a step needs one of those, it reads it from the profile. If the profile doesn't have it, the skill asks and offers to add it.

**Precedence:** the site's **Decisions** table (in `aeo-seo-log.md`) wins over the method when they conflict. Everything else in the method holds on every site. When a site keeps needing a rule the method doesn't have, add it to the method instead of repeating the decision on each site.

## Layout

```
skills/<skill>/
├── SKILL.md
├── references/      # long tables, checklists, templates and examples the SKILL.md points to
└── scripts/         # optional: small standard-library scripts the skill runs (no installs)
```

`aeo-seo-setup` also has `templates/aeo-seo/`: the blank profile files it copies into a project.

Flat layout: every skill is one folder under `skills/`, because agents only find skills one level down.

**Names:** `aeo-seo-` for skills that work on the whole site (`aeo-seo-setup`, `aeo-seo-weekly`, `aeo-seo-foundations`). Page skills use plain names for the page they make (`blog-post`, `comparison-page`).

**Shared references.** Skills install one at a time, so each skill carries its own copy of any reference it needs (for example `references/de-ai-checklist.md`). Never point at another skill's folder.

## SKILL.md shape

1. Frontmatter: `name` (same as the folder) and `description`. The description says what the skill makes, when to use it, and the phrases that should trigger it. Written for "the user", never a named person.
2. A one-paragraph intro: what the skill produces, and what it doesn't do (point to the sibling skill instead).
3. `## Step 1: Load the site profile`, copied verbatim from below.
4. The method steps, approval gates included. Gate 1 comes before drafting and gate 2 before shipping.
5. `## Updating an existing page` (page skills only): when to update instead of writing a new page, and how.
6. `## Quality check` before showing anything.
7. `## Related skills`, naming skills in this repo only.

Keep SKILL.md under about 400 lines. Move long tables, frameworks and examples into `references/`.

## Step 1 block (verbatim)

```markdown
## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.
```

## Tools

| Tool | Status | What the skills use it for | Fallback when missing |
|---|---|---|---|
| [OpenSEO](https://openseo.so) MCP | **Required** | Search Console data, keyword volume and difficulty, live search results, keyword ideas, the research log | None. The skill stops and points to the README setup |
| `last30days` | Recommended | Recent, linkable quotes from Reddit, X, Hacker News and YouTube | Web search with `site:reddit.com` / `site:news.ycombinator.com`. Every quote still needs a working link |
| `exa-search` | Recommended | What AI engines cite, older threads, expert sources | The agent's built-in web search |
| `humanizer` | Recommended | Rewrite pass that strips AI-writing patterns | The skill's `references/de-ai-checklist.md`, applied by hand |
| `no-ai-slop` | Recommended | Detect pass on the rewritten draft | The same checklist, run a second time as a detect-only pass |

When a skill uses a recommended tool, it says so in one line, and says which fallback it used when the tool isn't installed.

**OpenSEO credits.** Every page skill follows the same rules: check the cache (`query-bank.md`, `research/serps/`, the OpenSEO research log) before any paid call; batch paid calls; write every result back so nothing is bought twice; end each paid session with one research-log line saying what ran and what it cost. Budgets live in the site's `site.md`.

## Writing rules for skills

- Plain, specific, no hype words. The site's voice comes from `product.md`, never from the skill.
- Every number, price and competitor claim needs a source fetched today.
- Never link to a competitor's site (a method rule on every site).

## Private-data rule

Never in this repo:
- A path into a private brain or notes repo, Notion IDs or URLs, Slack, Linear, issue keys, OpenSEO project IDs.
- Facts about a specific product or site, used as the user's own (they belong in that site's profile). A product may appear in a clearly labeled example.
- References to skills that aren't in this repo, except the recommended tools above.

Run this before every commit:

```bash
grep -rniE 'notion\.(so|com)|app\.notion|projectId|company-brain|KIN-[0-9]+|tryadeli' skills/ README.md
```

Each hit is either removed or is a deliberate, labeled example.

## Approval gates

Skills that publish or change a live site never ship without the user's explicit go-ahead at gate 2. Skills that spend OpenSEO credits say what they'll spend before a large batch.
