# aeo-seo-skills

Agent skills that get your website found in Google and quoted by ChatGPT, Perplexity and Google AI Overviews. They work in Claude Code, Codex, Cursor and any agent that reads `SKILL.md` files.

SEO and AEO (answer engine optimization) are one job here. The same page has to rank in search and make sense when an AI engine lifts one paragraph out of it. Every skill writes for both: answer-first sections, real search data, sourced facts, quotes from real people, and a log of every decision so nothing gets researched or argued twice.

The skills are generic. Everything about your site lives in a small `aeo-seo/` folder in your own project: your domain, your product, your competitors, your decisions and your research. Updating the skills never touches it. You approve every brief and every page before it ships.

Built by [Mika Reyes](https://mikareyes.com) ([@its.mikareyes](https://instagram.com/its.mikareyes)) at [King's Cross Labs](https://kingscrosslabs.com). These are the skills I use to run AEO and SEO for my own products every week.

> **Status:** scaffolding. The skill folders exist; the methods are being moved in from the private versions, one skill at a time.

## Skill map

```
                     ┌──────────────────────────────────────┐
                     │        aeo-seo/  site profile        │
                     │  site · product · competitors · log  │
                     │   query bank · experience bank · …   │
                     │     (read by every skill first)      │
                     │        built by aeo-seo-setup        │
                     └──────────────────┬───────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
┌────────────────┐              ┌─────────────────┐             ┌─────────────────┐
│   Site-wide    │              │      Pages      │             │    Off-site     │
├────────────────┤              ├─────────────────┤             ├─────────────────┤
│ setup          │              │ topic-plan      │             │ forum-replies   │
│ technical-audit│              │ blog-post       │             │ link-pitches    │
│ weekly         │              │ comparison-page │             │                 │
│                │              │ feature-page    │             │                 │
│                │              │ use-case-page   │             │                 │
└───────┬────────┘              └────────┬────────┘             └────────┬────────┘
        └────────────────────────────────┼───────────────────────────────┘
                                         ▼
                     ┌──────────────────────────────────────┐
                     │   OpenSEO: Search Console, keyword   │
                     │   data, live search results (req.)   │
                     └──────────────────────────────────────┘
```

Skills hand off to each other:

```
aeo-seo-setup → aeo-seo-technical-audit → topic-plan → blog-post / comparison-page / feature-page / use-case-page
aeo-seo-weekly → picks this week's queries and the pages to update → the page skills
```

## Skills

✅ available now · 🚧 being built · 🔜 coming soon

**Site-wide**
- 🚧 [`aeo-seo-setup`](skills/aeo-seo-setup/): builds your `aeo-seo/` site profile by reading your repo and live site, interviewing you for the rest, and connecting OpenSEO.
- 🚧 [`aeo-seo-technical-audit`](skills/aeo-seo-technical-audit/): audits the live site against 26 foundation checks, delivers a graded visual HTML report (problem → principle → fix prompt), implements the fixes you pick with parallel subagents, then re-audits to prove they stuck.
- 🔜 [`aeo-seo-weekly`](skills/aeo-seo-weekly/): a weekly routine that reads Search Console, checks indexing, proposes the week's queries, and lists the pages to update.

**Pages**
- 🚧 [`topic-plan`](skills/topic-plan/): proposes a cluster of 8–12 pages from real search data, scored and ordered, linked into the pages you already have.
- 🚧 [`blog-post`](skills/blog-post/): research, brief, draft and ship one post (how-to, listicle, explainer or changelog), with approval before drafting and before publishing. Also updates existing posts.
- 🚧 [`comparison-page`](skills/comparison-page/): an "X alternative" or "you vs X" page with sourced, dated competitor facts.
- 🚧 [`feature-page`](skills/feature-page/): a page for one integration or one capability of your product, using only facts your code or docs back up.
- 🚧 [`use-case-page`](skills/use-case-page/): a page for one kind of customer, in their words, grounded in real customer evidence.

**Off-site**
- 🔜 `forum-replies`: drafts helpful replies to the forum and Reddit threads where people ask about your topic.
- 🔜 `link-pitches`: finds the lists and directories your buyers read and drafts the pitch.

## Install

### 1. Connect OpenSEO (required)

Every skill uses [OpenSEO](https://openseo.so) for real search data: your Search Console numbers, keyword volume and difficulty, and the live results for a query. The skills never guess a number, so they stop if OpenSEO isn't connected.

1. Create an account at [openseo.so](https://openseo.so) and add your site as a project. Connect Google Search Console inside it.
2. Add the MCP server to your agent. For Claude Code:

   ```bash
   claude mcp add --transport http openseo https://app.openseo.so/mcp
   ```

   For other agents, see [OpenSEO's MCP docs](https://openseo.so/docs/mcp).
3. Check it: ask your agent to run OpenSEO's `whoami`.

Paid OpenSEO calls use credits. The skills check their cache before every paid call, batch what they buy, and save every result to your `aeo-seo/` folder so nothing gets bought twice.

### 2. Install the skills

```bash
npx skills add kingscrosslabs/aeo-seo-skills
```

Install all of them or pick some. Or clone the repo and copy the skill folders into your agent's skills folder (for Claude Code, `.claude/skills/`).

### 3. Recommended tools

Each skill works without these, using a built-in fallback. They make the output better:

| Tool | What it adds | Without it |
|---|---|---|
| `last30days` | Recent, linkable quotes from Reddit, X, Hacker News and YouTube | Web search for threads |
| `exa-search` | What AI engines cite, older threads, expert sources | Your agent's built-in web search |
| `humanizer` | A rewrite pass that strips AI-writing patterns | The de-AI checklist in each skill's `references/` |
| `no-ai-slop` | A second pass that catches what's left | The same checklist, run again |

## Set up your site profile

Run `aeo-seo-setup` in your website's repo. It reads your repo and live site, asks about what it can't find, and writes:

```
aeo-seo/
├── README.md            # index: which file each skill reads
├── site.md              # domain, stack, where pages live, commands, what's auto-generated
├── product.md           # what you sell, who it's for, voice, where the true facts live
├── competitors.md       # who you compare against, with sourced, dated facts
├── aeo-seo-log.md       # Decisions table + dated log of every change
├── query-bank.md        # every query considered or targeted, with search data
├── experience-bank.md   # your own stories, data and quotes, marked approved or not
├── user-questions.md    # threads where real people ask about your topic
├── link-targets.md      # lists and directories worth pitching
└── research/            # one report per page, plus saved search results
```

- **Minimum:** `site.md`, `product.md` and `aeo-seo-log.md`. The banks start empty and fill up as you use the skills.
- **Somewhere else?** If the folder isn't at `aeo-seo/` in your project, add a line to your project's `CLAUDE.md` or `AGENTS.md`: `AEO/SEO profile: path/to/aeo-seo/README.md`.
- **More than one site?** List them in your global `CLAUDE.md` or `AGENTS.md` under `AEO/SEO sites:`, one `name: path` per line, so "write a blog post for <site>" works from anywhere.

Your profile lives in your project, not in this repo, so updating the skills never overwrites it.

## Contributing

Issues and pull requests are welcome, especially fixes where a method falls short on your kind of site.

## License

MIT
