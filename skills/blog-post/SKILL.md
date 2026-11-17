---
name: blog-post
description: Researches, briefs, drafts and ships one SEO- and AEO-optimized blog post (how-to, listicle, explainer or changelog) on the user's site, with approval before drafting and before publishing. Uses real search data from OpenSEO, verbatim linked quotes from real users, first-hand experience from the site profile, and answer-first sections AI engines can quote. Also updates existing posts. Use when the user says "write a blog post", "blog post about <topic>", "SEO post", "AEO post", "update this post", "refresh this post", or names a query they want to rank for. Not for picking topics (use topic-plan) or comparison pages (use comparison-page).
---

# Blog Post

Writes one blog post that can rank in Google and be quoted by AI answer engines, from research to a live page. It works one post at a time and stops for approval twice: on the brief, and before publishing. It doesn't pick which posts to write (that's `topic-plan`) and doesn't make comparison pages (that's `comparison-page`).

**The idea behind every rule below:** a page earns a ranking only when it holds something a language model couldn't write from a prompt. Search data decides what to build and how to shape it. Real people's words, the site's own experience, and facts checked today give the post its substance. A post that could be rebuilt from training data has no reason to rank.

**References in this skill:**
- `references/openseo-credits.md`: which OpenSEO calls cost credits, the cache, and the budget rules. Follow it for every paid call.
- `references/writing-rules.md`: the drafting rules (answer-first, structure, links, quotes, E-E-A-T, listicles, titles and years). Read it before Step 5.
- `references/manual-checks.md`: the checks to run by hand when the site has no check command.
- `references/de-ai-checklist.md`: the fallback when `humanizer` or `no-ai-slop` isn't installed.

## Step 1: Load the site profile

Before doing anything, load the site's AEO/SEO profile.

1. **Find it.** Check the project's CLAUDE.md or AGENTS.md for a line starting `AEO/SEO profile:` and use that path. Otherwise use `aeo-seo/README.md` in the current project. If the user names a site you're not in, check their global CLAUDE.md or AGENTS.md for an `AEO/SEO sites:` list and use that site's path.
2. **Read the index.** Open the profile's `README.md` and read the files it lists for every task: at minimum `site.md`, `product.md`, and the Decisions table plus the last two weeks of `aeo-seo-log.md`. Open the other files (banks, competitors, research) only when this task needs them.
3. **Respect what's settled.** If a decision in the log rules out this work, or the log shows it's already done, stop and say so instead of redoing it. Decisions win over this skill when they conflict.
4. **Check OpenSEO.** Run `whoami` on the OpenSEO MCP. If it isn't connected, stop and point the user to the OpenSEO setup in this repo's README. Never guess search volumes or rankings.
5. **No profile?** Stop and offer two choices: run `aeo-seo-setup` (recommended), or point to where the profile lives.

Never state a fact about the product that isn't in one of the fact sources `product.md` lists. If the work needs one that isn't there, ask, or leave a clearly marked `[placeholder]`.

**For this skill, also read:**
- `site.md` → the Blog post row of "Where each page type lives", the Commands, Shipping, Authors and "What the site does automatically".
- The blog's own README or template, if `site.md` points to one. It sets the post format: which fields exist (short answer, description, CTA, related pages, author, draft flag, dates) and what they're called.
- `query-bank.md`, `experience-bank.md`, `user-questions.md`, and `research/` for this topic.

If `site.md` has no Blog post row, the site has no blog yet. Say so and stop: the post needs a home first. Offer to work out the URL pattern, file format and template with the user (and `aeo-seo-technical-audit` for the sitemap and structured data), then add the row to `site.md`.

## Step 2: Intake

Establish these. Ask only for what the request and the profile don't already make clear:

1. **Topic and angle:** what the post is about, and the one thing it argues or teaches.
2. **Type:**
   - `how-to`: a task, step by step. High-intent queries ("how to send an invoice via API").
   - `listicle`: a set of options. The queries AI engines answer most often ("best invoicing APIs").
   - `explainer`: what a term means and why it matters. Top of funnel ("what is dunning").
   - `changelog`: a launch or a new capability. Can be short.
3. **Target query:** the exact phrase a person types into Google or asks an AI engine.
4. **The page it supports:** the product, feature, comparison or pricing page this post should send readers to. Pick it from the site's list of pages (`site.md`).
5. **Author:** decide it yourself from the rules in `site.md` → Authors. If there are none, use the site's default author and say so.

Check the target query in `query-bank.md`:
- If another page already targets it, stop and tell the user. An update to that page is usually the better move.
- Otherwise set it to `targeted: <slug>`, and mark the cluster queries the post will cover as H2s or FAQs `answered-by: <slug>`. Add any query that isn't in the bank yet.

## Step 3: Research

No approval needed. Just do it, following `references/openseo-credits.md` for every paid call: cache first, batch, write back. Search data comes first, because it can change the plan or stop it.

**A. Search data**
- **Already ranking?** Run `get_search_console_performance` (free) for the target query and its close variants, with dimensions `['query','page']`. If one of the site's pages sits at positions 5–20 for it, update that page instead (see [Updating an existing post](#updating-an-existing-post)) and tell the user.
- **Real numbers.** Get volume, KD and CPC for the target query and its modifier family in one `get_keyword_metrics` call: `best <topic>`, `<topic> free`, `<topic> pricing`, `<topic> api`, `<topic> alternatives`, `<a> vs <b>`, plus question forms. Confirm the target query, or swap in a variant with more demand or lower difficulty.
- **Read the live results like an editor** (`get_serp_results` for the target query, depth 20):
  - **Format:** what kind of page ranks (a list, a guide, a product page)? Match it. Don't fight the results page.
  - **List length and depth:** how many items the ranking lists carry, and roughly how long the top 5 pages are. That sets the item count and word target.
  - **AI Overview:** if one shows, the short answer and the first body sentence must be quotable on their own.
  - **People Also Ask:** record the questions. They're the first source for FAQs and question H2s.
  - **Who ranks, and where they're weak:** stale dates, no pricing, no real user voices, no code. Those gaps are the angle.
  - Use `exa-search` (or web search) for what AI engines cite, and note whether any result names the product.
- **Overlap with the site's own pages.** If another page on the site is close to this topic, fetch its query's results in the same batch and compare the two top-10 URL sets:
  - **Under ~30% shared URLs:** build both. The new post doesn't use the sibling's query in its title or H1, and the two link to each other.
  - **30% or more:** don't build. Update the existing page and tell the user.

**B. What real people say** (the quotes are what nobody else has)
- Start with `user-questions.md`. Then run `last30days` on the topic with several phrasings: the topic itself, `<topic> pricing`, `alternative to <x>`, `switching from <x>`, `how do you <task>`. For anything older, or if `last30days` isn't installed, use `exa-search` or web search with `site:reddit.com` or `site:news.ycombinator.com`.
- Pick **6–10 verbatim quotes** that fit the type:

  | Type | Quotes to look for |
  |---|---|
  | listicle | Complaints about the incumbent (price, gaps, complexity) and "what do you use for X" recommendations |
  | how-to | Failed attempts and error messages people hit. These become "Common mistakes" |
  | explainer | How practitioners actually use the term |
  | changelog | The requests and complaints the launch answers |

- **Every quote needs a working public link** to the exact post or comment. Open it and check the words match exactly. No link, or no exact match, means no quote. Use `…` for cuts and `[brackets]` for substitutions. Never paraphrase and present it as a quote.
- Prefer quotes that name a specific pain: a dollar figure, a missing feature, hours lost. Dedupe by author. Outside listicles, skip quotes that name a competitor.
- **Find the hook:** the pain that repeats most across the quotes becomes the opening angle, in the users' own words.
- **Fan-out questions:** People Also Ask first, then 5–8 in total, including ones an AI engine would also answer ("…vs…", "how much…", "is it free…", "do I need…"). These become H2s and FAQs.
- Log new threads in `user-questions.md` in its format.

**C. Facts, experience and experts**
- **Competitor facts.** Any claim about a competitor (price, limits, features) cites a source URL fetched today. Check `competitors.md` first; if a fact there is older than 90 days or contradicts what you find, update it.
- **Products in a listicle.** For each one, fetch the official pricing page and docs today. Record the entry price, what's gated behind which tier, its one true strength ("Best for…"), 2–3 strengths, 2–3 limits, and the source URLs.
- **The site's own experience and data.** Read the topic's section of `experience-bank.md` and pick the `approved` entries that fit. If there are none, note what a good entry would be (a story, a stat someone could pull, a survey question). Those become questions for the user in the brief.
- **Expert quotes.** Find 1–2 named practitioners who said something specific about the topic: platform developer advocates, maintainers of well-known libraries, engineers writing about their own build. Each needs a real name, a role, a public source URL and a date. Skip anonymous accounts, anyone at a competitor, and anything you can't open and read in full.
- **Recent data.** A dated, sourced number that sharpens the post (a changelog, a policy change, a published study), taken from the primary source, not a blog quoting it.
- **Related entities.** From the top results and the official docs, list the specific things a complete answer names: endpoints, settings, error codes, limits, standards, adjacent tools. Naming them is what makes a post read as the authority, to Google and to AI engines.

**D. Save the research report** to `research/<slug>.md` in the profile:
- the keyword table (keyword, volume, KD, CPC, intent, date)
- the notes on the results page, and the overlap verdict
- the quote shortlist (quote, author, platform, URL, date, theme)
- the product and competitor facts, with sources
- the decisions (target query, format, list length, word target, title)
- the OpenSEO credits spent

Updates and future posts start from this file.

## Step 4: Brief (approval gate)

Present the brief in chat:

```
Title: ≤ 60 characters minus the brand suffix's length (site.md), target query near the front
Target query: with volume, KD and the date measured
Type, and the format the results page rewards: list length and word target from the top 5
Already ranking? Overlap verdict: the Search Console result; sibling pages checked and % shared URLs
Hook: the most repeated user pain, quoted
Quote wall: n quotes, with platforms (the full list is in the research report)
Angle, in one sentence: what this post says that the top 5 results don't
Short answer draft (30–75 words): answers the query outright and names the product
H2 plan: question-phrased where natural
FAQs (2–4): the fan-out questions that didn't become H2s
Internal links: 2+ pages on the site, each from the site's list of pages
Inbound links: the 2–3 existing posts or pages I'll edit to link here
Author: who, and why
OpenSEO credits spent: n (or "0, reused cache from <date>")
First-hand: the experience-bank entries I'll use (or "none yet", plus the question I'd ask)
Original data: the stat or survey result, with its date and method (or "none")
Expert quotes: name, role, source URL, the line
Facts I'll use: each with its source
Facts I need from you: anything not in the fact sources
```

Wait for approval or edits. Don't draft before this.

## Step 5: Draft

Read `references/writing-rules.md` first. It holds every drafting rule; the ones that most often go wrong are summed up here.

1. **Create the file** with the scaffold command from `site.md` → Commands. If there's none, copy the template `site.md` names for the blog (or the best existing post of the same type) to the blog's source folder.
2. **Slug:** the target query in kebab-case, 3–6 words, no stop-word padding, no year: `send-invoice-via-api`, not `how-to-send-an-invoice-via-the-api-in-2026`.
3. **Fill it in.** Replace every `[placeholder]` and delete every guidance comment. Leave the post as a draft (the format's draft flag, or unpublished in the CMS) until Step 8.
4. **Use the site's components.** A post is content inside the site's blog template. Never add raw HTML or one-off styling. If the post needs a visual the format can't express, stop and ask; it belongs in the site's shared components (`site.md` → Design system), not inside the post.

The rules in short:
- **Answer first.** The short answer answers the query in 30–75 words and makes sense lifted out of the page. The first body sentence restates it in fuller form, and every H2 opens with its own direct answer in 40 words or fewer.
- **Extractable.** Comparisons in tables, steps in numbered lists, code in fenced blocks. Name entities outright and use one name per thing.
- **Readable.** Bullets and tables over paragraphs, paragraphs of 2–3 sentences, bold lead-ins and key terms. A reader skimming headings, bold and tables gets the answer.
- **Links.** Never link a competitor's site. Link specific official doc pages. At least 2 internal links to product, feature, comparison or pricing pages. Never link a page that isn't live yet.
- **Proof.** At least one thing only this site could say (an approved experience-bank entry or its own data), a quote wall of real user voices, and an expert quote where one exists.
- **Titles.** Title plus the brand suffix stays at 60 characters or fewer. The year goes in the title of evaluation posts only, rolls over on December 1, and never goes in the slug.
- **Listicles.** Compare and contrast, no ranking. The product sits at position 2 or 3, says it's ours, and every competitor gets its one true, sourced strength.
- **Unique.** Every section is written fresh for this post. Length and list size follow the results page, with an 800-word floor for how-tos, listicles and explainers.

## Step 6: Check and preview

1. **Run the site's check command** (`site.md` → Commands) on the post. Errors must be fixed. Warnings are an editorial checklist: fix them unless there's a reason not to, and say which you left and why. If the site has no check command, run `references/manual-checks.md` instead.
2. **De-AI the text**, in this order, over the body, short answer and FAQ answers. Every draft goes through both:
   1. `humanizer`: the rewrite pass. Apply its edits, except keep the bold lead-ins, bold key terms, bullets and tables from the writing rules. Those are format, not AI tells.
   2. `no-ai-slop`: the detect pass on the humanized text. Fix everything it flags. If a fix would change a fact or a question-phrased heading, keep the fact and the question and rephrase around them.

   If either tool isn't installed, run `references/de-ai-checklist.md` for that pass and say so.
3. **Re-run the check** after both passes. Rewrites can push the short answer out of range or break a link.
4. **No links to unpublished pages.** List every post or page still in draft and confirm the new post links to none of them. A link to a draft can break the production build. If the site has a build command, run it.
5. **Every external link opens.** Run `curl -sIL -o /dev/null -w '%{http_code} %{url_effective}\n' <url>` on each external URL, quote links included. Drop or replace anything that isn't a 200 on the intended page. Reddit and X can block curl; open those in the browser instead.
6. **Quotes are verbatim.** Re-read each quoted source and confirm the words match.
7. **No duplicated copy.** Take 3–4 distinctive sentences (a product blurb, an FAQ answer, a quote) and `grep -rF` each across the site's content and page folders. Any hit outside this post gets rewritten.
8. **Preview.** Start the dev server from `site.md`, open the post, and screenshot the top of the page.

## Step 7: Final review (approval gate)

Show the user:
- the preview screenshot and the local URL
- the check result
- confirmation that both de-AI passes ran, with a line on what each changed
- the E-E-A-T line: which experience-bank entries, data, expert quotes and user quotes the post uses, and the author
- the search line: target query with volume and KD, the format and length decision and why, and the OpenSEO credits spent
- **Needs your call:** one batched list of every open item, each with a recommendation:
  - each "If you need X, pick <competitor>" line
  - each competitor name kept in the body, and why
  - facts still unverified
  - stale or contradictory facts found on other pages of the site during research
  - any rule bent, and why

When `aeo-seo-weekly` runs this skill in a batch, it collects this list for the user instead of stopping here. A post whose open items would change what it says stays a draft until the user answers.

Wait for explicit approval to publish.

## Step 8: Ship

On approval:

1. **Publish the post:** clear the draft flag and set the published date to today.
2. **Run the check again.** Zero errors.
3. **Log it** under today's date in `aeo-seo-log.md` (create the date heading if it's missing, newest on top):
   `- [change] Published /<blog path>/<slug>, targeting "<target query>". Supports <page>.`
   Add a `[decision]` line for any editorial call the user made at the gates that future posts should follow, and copy standing decisions into the Decisions table.
4. **Update the banks:** add `<slug>` to the `used in:` list of every experience-bank entry the post uses, and make sure the query bank statuses from Step 2 are saved.
5. **Ship it the way `site.md` → Shipping says** (a push, a pull request, a CMS publish). Stage only what this skill touched: the post, its research report and new search-results files, the log, the banks, and the posts edited for inbound links. Other changes in the working tree may be someone else's work in progress.
6. **After the deploy,** run the checks `site.md` lists under "After deploy", at minimum that the live URL loads.
7. **Report** what shipped, with the live URL. Suggest requesting indexing in Google Search Console's URL Inspection if the site has no IndexNow ping, or for faster Google pickup.

## Updating an existing post

Update instead of writing a new post when:
- research shows the site already ranks at positions 5–20 for the target query, or a new topic shares 30% or more of its top-10 results with an existing page
- a fact the post states has changed (a price, a feature going live, a limit)
- it's the December 1 rollover and the post has a year in its title (`aeo-seo-weekly` runs these in the first week of December)

How:
1. **Start from `research/<slug>.md`.** Re-run Step 3 for what has aged: search data (the cache windows still apply), product and competitor facts, quotes. Always re-fetch prices.
2. **Keep the URL and the published date.** Set the updated date to today. Change the year in the title if it has one. Never write a separate post for the new year; it would compete with this one for the same results.
3. **Replace stale or dead quotes** with fresh ones, and update the research report.
4. **Diff old against new.** The post should be more specific (newer numbers, more answered questions, sharper quotes), not just longer. If it only grew, cut.
5. Show the diff and the reason for each change, and get a yes (the same gate as Step 7).
6. Run Step 6's checks, add `- [change] Updated /<blog path>/<slug>: <what changed>` to `aeo-seo-log.md`, and ship as in Step 8.

A visible "Updated" date is a freshness signal, but don't touch a post just to bump the date.

## Quality check

Before showing the final review, confirm:
- The target query is marked `targeted: <slug>` in the query bank, and no other page targets it.
- Every product fact traces to a fact source in `product.md`, and every competitor fact to a URL fetched today.
- Every quote opens at its link and matches word for word.
- The short answer is 30–75 words and stands alone; every H2 opens with a direct answer of 40 words or fewer.
- Title plus brand suffix is 60 characters or fewer; the description is 110–160 characters.
- No link to a competitor's site, and no link to an unpublished page.
- At least 2 internal links out, and 2–3 existing pages edited to link in.
- At least one approved experience-bank entry or own-data point, or the gap is flagged in "Needs your call".
- Both de-AI passes ran.
- The research report is saved, and every paid OpenSEO call is in the research log.

## Related skills

- `topic-plan`: decides which posts to write and in what order. Run it first when the user asks what to write about.
- `comparison-page`: for "<product> vs <competitor>" and "<competitor> alternative" pages.
- `aeo-seo-weekly`: runs this skill in batches and decides which posts need an update.
- `aeo-seo-technical-audit`: for site-wide gaps the post exposes (no structured data, no sitemap entry, no `llms.txt`).
- `aeo-seo-setup`: builds the site profile this skill reads.
