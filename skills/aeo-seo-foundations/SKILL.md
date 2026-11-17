---
name: aeo-seo-foundations
description: Audits the live site against 26 foundation checks for Google and AI answer engines (quotable pages, getting found faster, consistent URLs, and a setup that runs itself), grades each theme, and delivers a visual HTML report that teaches the principle behind every issue and gives a ready-to-run fix prompt. After the user picks fixes, implements them in parallel with subagents on a branch, then re-audits the live site to prove they stuck. Use when the user says "AEO audit", "SEO audit", "audit my site", "technical SEO", "AEO foundations", "set up llms.txt", "schema markup", "make my site readable by AI", "re-audit", or when aeo-seo-setup finds gaps.
---

# AEO/SEO Foundations

Makes the whole site easy to crawl, index, trust and quote, once, so every page the other skills write inherits it. It runs in three passes: a **plan-only audit** with a visual HTML report, **implementation** by parallel subagents once the user picks the fixes, and a **re-audit** of the live site to prove the fixes stuck. It fixes site code, templates and site-wide sweeps (missing descriptions, alt text, headings). It doesn't write new pages or plan topics; those are `blog-post` and `topic-plan`.

**The idea behind the method:**
- **Audit before you touch anything.** You can't fix what you can't see, and the user should agree with the plan before code changes.
- **Teach, don't just list.** Every finding is problem → principle → prompt: what's wrong and where, why it matters, and the exact prompt that fixes it. A checklist that says "fix metadata" teaches nothing.
- **Fix in parallel, coordinate centrally.** Independent fixes run as separate subagents, one thread per package, so the user can answer each one's questions. The main agent keeps them from colliding.
- **Verify on the live site.** The repo says what should happen; the production HTML says what did. The re-audit is how you know.
- **Bake it in.** A fix that isn't enforced by the template or a check regresses on the next page.

**References in this skill:**
- `references/checks.md`: the 26 checks, each with its principle, test, pass bar and severity, plus the grading formula.
- `references/report-template.html`: the report's HTML and styles. Copy it and fill it in.
- `references/fix-brief.md`: the brief every implementation subagent gets.
- `scripts/sweep.py`: crawls the sitemap and collects the page-level evidence (titles, descriptions, canonicals, `og:*`, H1s, JSON-LD types, alt text, word counts, internal links).

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

**For this skill, also read:**
- `site.md` → Basics (the canonical host), Stack, "Where each page type lives", Commands, Shipping, "What the site does automatically", and Search data.
- `research/audits/`: the last report, if there is one. A run with an earlier report is a re-audit (see [Re-auditing](#re-auditing)).

## Step 2: Scope

Confirm three things in one message:
1. **Mode:** audit only (the default), audit and fix, or re-audit against the last report.
2. **Access:** the live URL is enough for the audit. Fixes need the site's repo open in this session. On a hosted builder with no code access, the report still lands, and its prompts become a hand-off list.
3. **Sample:** the pages to audit in depth. Default: the homepage, the best example of each page type in `site.md`, and the 5 pages with the most impressions in the last 28 days (`get_search_console_performance` with dimension `page`, free). The sweep covers every URL in the sitemap for the page-level checks.

## Step 3: Gather the evidence

No approval needed. Read only; change nothing. Save raw evidence to `research/audits/<YYYY-MM-DD>/` in the profile so the re-audit can diff against it.

1. **Crawl files and host.** Fetch `/robots.txt`, `/sitemap.xml` (and any sitemap index), `/llms.txt`, `/llms-full.txt`, and the homepage's `.md` mirror if the site has one. Run `curl -sIL` on `http://` and `https://` for the bare and `www` hosts and record each hop and status code.
2. **Sweep the pages.** Run `python3 scripts/sweep.py <sitemap URL> --out research/audits/<date>/sweep.json` (it caps at 300 URLs by default; pass `--limit` to change it). It fetches the raw HTML the way a non-JS crawler would. If Python isn't available, collect the same fields with `curl` for the sample pages and say the sweep was partial.
3. **Read the sample pages** in full: the raw HTML and the rendered page (open it in the browser). Note headings, the first sentence under each, FAQs, the byline and dates, and anything that only appears after JavaScript.
4. **AI crawler access.** Fetch the homepage with `-A "GPTBot"` and `-A "ClaudeBot"` and record the status.
5. **Speed.** Call the PageSpeed Insights API for the homepage and one article, mobile strategy.
6. **Search data (free calls only).** `get_search_console_performance` for the last 28 days (totals, top pages, top queries), and `inspect_urls` on the sample pages if it's available, for indexing status. Don't run paid OpenSEO calls in this skill; if a paid site audit would help, say what it costs and ask first.
7. **The repo, to locate problems.** For each failing check, find the file that causes it: the layout or head component, the metadata helpers, the sitemap and robots generators, the redirect config, the content folder. Record the path; the report and the fix packages need it.
8. **Ask the user** what you can't see: Search Console sitemap status, Bing Webmaster Tools, and how analytics shows AI referrers.

## Step 4: Grade and write the findings

Score every check in `references/checks.md` as pass, partial, fail or n/a, then compute the theme grades and the overall grade with its formula.

Write one finding per failed or partial check. Merge checks that share a cause (one broken layout file can fail C2, C3 and A6) into one finding that lists all their IDs. Each finding has:
- **Title:** the problem in plain words, with a number where there is one ("About 250 pages use their title as the meta description").
- **Severity** from the check, and the **theme**.
- **Evidence:** the live URLs or sweep counts that prove it, and the file in the repo where it lives.
- **Principle:** why it matters, in two or three sentences someone new to SEO would understand. Teach the idea, so the user can spot the next one alone.
- **Fix prompt:** a copy-paste prompt that would fix it in this repo. It names the files, says what done looks like, and says how to verify on the live site.
- **Effort:** S (under an hour), M (half a day) or L (more).
- **Owner:** `agent` (code in the repo) or `user` (an account task: Search Console, Bing Webmaster Tools, analytics settings, a DNS change).

Then write two more sections:
- **What's already good:** the passes worth keeping, in one line each, so the user knows what not to break.
- **Rules for new pages:** the page-level rules this site keeps failing (descriptions, FAQs, alt text, answer-first openings, internal links), written so they can go into the site's page template or check command. These are what the D2 fix bakes in.

## Step 5: Build the report (approval gate)

1. Copy `references/report-template.html` to `research/audits/foundations-<YYYY-MM-DD>.html` in the profile and fill it in, following the comments in the template: the header, the scorecards, the mental model, the findings grouped by severity, what's good, the rules for new pages, and the action plan.
2. **Action plan:** every finding in one table, ordered by severity, then effort. Group the agent-owned rows into **fix packages** (see Step 6) and show which package each row belongs to. User-owned rows go in their own "Your to-dos" list with the exact steps.
3. Remove every template comment and example, and check the page renders in light and dark mode at phone width.
4. Open the report in the browser for the user, then summarize in chat: the overall and theme grades, the 3–5 findings that matter most, the packages, and the user's to-dos.
5. **Ask which packages to implement.** Recommend the critical ones first. In audit-only mode, stop here.

Log it in `aeo-seo-log.md` under today's date: `- [research] Foundations audit: overall <grade> (A <g>, B <g>, C <g>, D <g>). Report: research/audits/foundations-<date>.html.`

## Step 6: Implement with subagents

Only the packages the user approved.

1. **Branch.** Create one branch for the batch from the default branch, as `site.md` → Shipping describes (`aeo-seo-foundations-<date>` unless the site has a naming rule). Never work on the default branch.
2. **Plan the packages so no two touch the same file.** A package is one or more findings that share files. The usual split:

   | Package | Typical findings | Typical files |
   |---|---|---|
   | Head and metadata | C2, C3, A1 template, A6, A4 site-wide | The layout or head component, the metadata helper |
   | Structured data | A4 per page type, A3 markup, A5 | The JSON-LD helpers, the article template |
   | Crawl files | B1, B2, B5, B6 | The sitemap, robots, llms.txt and IndexNow generators, the build config |
   | Host and redirects | C1, C4 | The redirect config, the hosting config, hardcoded hosts |
   | Content sweep | A1 backfill, A2, A7, A8, C5 | The content folder; split by folder if it's large |
   | Measurement | D3 | Analytics setup, the signup form |

   Two findings that need the same file go in the same package, or run one after the other. Say which packages run in parallel and which wait.
3. **Dispatch.** Start one subagent per package with the agent's subagent tool, all parallel packages in one message. Give each the brief from `references/fix-brief.md`, filled in: its findings with their evidence and fix prompts, the files it may change, the files it must not change, the site's check and build commands, and what done looks like. Subagents don't commit, push or deploy. If the agent has no subagent tool, run the packages one at a time yourself, in the same order.
4. **Coordinate.** Answer each subagent's questions or pass them to the user. If one needs a file another package owns, hold it until that package finishes, then hand it the updated file.
5. **Integrate.** When every package reports back, review each diff against its brief. Run the site's check and build commands on the whole branch, start the dev server, and check the affected pages' HTML locally (canonicals, `og:*`, JSON-LD parses, the sitemap and llms.txt render).
6. **Commit** each package as its own commit on the branch, with the finding IDs in the message, so any one can be reverted alone.

## Step 7: Final review and ship (approval gate)

Show the user:
- each package: what changed, the files, and the finding IDs it closes
- the check and build results, and anything that still fails
- anything a subagent couldn't finish, and why
- the user's to-dos from the report, still open

Wait for explicit approval. Then ship the way `site.md` → Shipping says (usually a pull request for site code). After the deploy, go to Step 8.

## Step 8: Re-audit the live site

Run Steps 3 and 4 again on production, and write a follow-up report from the same template:
- Before and after grades for each theme and overall.
- **Verified on the live site:** each fixed finding, with the URL and the evidence that it's live (the canonical in the production HTML, the sitemap entry, the JSON-LD type).
- **Still open:** findings not fixed, and any regressions.
- Save it as `research/audits/foundations-<YYYY-MM-DD>-followup.html`.

Then close the loop:
- Tick what's now automatic in `site.md` → "What the site does automatically", and add the check command to `site.md` → Commands if the D2 fix added one.
- Log `- [change] Foundations fixes live: <finding IDs>. Overall <before> → <after>.` and add a `[decision]` and a Decisions table row for any standing choice the user made (for example, blocking training bots).
- Search Console shows the effect in 1–4 weeks. Suggest a `[baseline]` entry with today's 28-day numbers to compare against.

## Re-auditing

Re-run the audit after any big batch of new pages, after a redesign or a framework upgrade, and at least once a quarter. `aeo-seo-weekly` flags when one is due.

When `research/audits/` holds an earlier report:
1. Read it and its evidence folder first.
2. Run Steps 3–4 in full. Don't trust earlier passes; regressions are the point.
3. In the new report, mark each finding `new`, `still open` or `regressed`, and show the grade change per theme.

## Quality check

Before showing the report:
- Every check in `references/checks.md` has a result, and every n/a has a reason.
- Every finding has evidence from the live site, not only from the repo.
- Every agent-owned finding has a file path and a fix prompt that names it; every user-owned one has exact steps.
- No two fix packages share a file.
- The grades match the formula.
- The report opens, has no template comments left, and reads in light and dark mode at phone width.
- No paid OpenSEO call ran without the user's OK.

Before shipping fixes:
- The check and build commands pass on the branch.
- Each package is its own commit with its finding IDs.
- Nothing was committed to the default branch or deployed without the user's yes.

## Related skills

- `aeo-seo-setup`: builds the site profile this skill reads. Run it first.
- `blog-post`, `comparison-page`, `feature-page`, `use-case-page`: write new pages that inherit these foundations.
- `topic-plan`: the next step once the foundations are sound.
- `aeo-seo-weekly`: the weekly routine; it flags when a re-audit is due.
