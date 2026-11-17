# The foundation checks

26 checks in four themes. Each one has the **principle** (why it matters, in a sentence the user can learn from), **how to test it** on the live site, what counts as a **pass**, and the **severity** used for grading.

Test on the live site, not the repo: what crawlers see is what counts. Use the repo only to find *where* a problem lives. `scripts/sweep.py` collects most of the page-level evidence in one run.

**Severity:** `critical` (3 points) breaks indexing or splits ranking credit · `important` (2) loses clicks, citations or crawl speed · `polish` (1) helps at the margin.
**Result:** `pass` (full points) · `partial` (half) · `fail` (zero) · `n/a` (left out of the grade, with the reason).

---

## Theme A: Make pages quotable

Google and AI answer engines both skim. The job is to make the answer easy to find and easy to trust.

### A1. Real meta descriptions · important
- **Principle:** The meta description is the two-line blurb under the title in Google, a free ad of about 155 characters. A description that repeats the title wastes it.
- **Test:** From the sweep, every page's `meta name="description"`.
- **Pass:** Every indexable page has one, 110–160 characters, not equal to the title, not duplicated across pages. Partial: under 10% of pages fail.

### A2. One H1, question-phrased H2s · important
- **Principle:** Headings are the outline crawlers read. Questions match how people actually search, especially in AI tools.
- **Test:** Sweep: H1 count per page. Read the H2s on the sample pages.
- **Pass:** Exactly one H1 on every page; H2s on articles are mostly questions where that reads naturally.

### A3. FAQs on guides and posts · important
- **Principle:** People ask AI full questions, and the AI looks for pages that answer that exact question. A list of real questions with direct answers is the easiest thing on a page to quote.
- **Test:** Sample articles: a visible FAQ section and matching `FAQPage` JSON-LD.
- **Pass:** Guides and posts carry 2–4 real FAQs, visible on the page, with FAQPage markup that matches the visible text.

### A4. Structured data · critical
- **Principle:** JSON-LD labels tell machines what a page is and who's behind it, so they don't have to guess.
- **Test:** Sweep: JSON-LD `@type`s per page. Check the homepage for `Organization` or `Person` with `name`, `url`, `logo` or `image`, and `sameAs` links to the real profiles.
- **Pass:** Site-wide `Organization`/`Person` and `WebSite`; `Article` or `BlogPosting` (with author and dates) on articles; `FAQPage` where FAQs show; `BreadcrumbList` on nested pages; `Product` or `SoftwareApplication` where it fits. All parse as valid JSON.

### A5. Visible author byline and updated date · important
- **Principle:** Google and AI weigh who's behind an answer and how fresh it is. Both have to be visible, not only in the markup.
- **Test:** Sample articles.
- **Pass:** A named author linked to a bio, a published date, and an updated date where the page changed.

### A6. A preview image per page · important
- **Principle:** The share card is what people see in Slack, LinkedIn and iMessage. One generic image on every page reads as noise; a card with the page's own title gets clicked.
- **Test:** Sweep: `og:image` per page, and fetch two of them.
- **Pass:** Each page has its own `og:image` (generated or set), 1200×630, with `og:title` and `og:description` that match the page, plus `twitter:card` `summary_large_image`.

### A7. Answer first · important
- **Principle:** A one- or two-sentence direct answer right under each heading is the part AI tools quote most.
- **Test:** Read the first sentence under the H1 and under 3 H2s on each sample article.
- **Pass:** The answer comes first, stands alone, and names the subject outright.

### A8. Real alt text · polish
- **Principle:** Crawlers can't see images. Alt text is how they know what a screenshot or chart shows.
- **Test:** Sweep: images without `alt`, or with alt equal to a filename.
- **Pass:** Every content image has descriptive alt text; decorative images have `alt=""`.

### A9. Short, descriptive URLs · polish
- **Principle:** A URL that says what the page is about helps readers and Google before anyone clicks.
- **Test:** The sitemap's URLs.
- **Pass:** Lowercase kebab-case words, no IDs or dates in evergreen URLs, no query strings for content.

---

## Theme B: Get found faster

A new site can wait weeks for a crawler to stumble onto it. Hand the crawlers a map, and open the door.

### B1. A sitemap with honest dates · critical
- **Principle:** The sitemap lists every page for crawlers. Accurate `lastmod` dates make them re-check pages that changed; dates that all say "today" teach them to ignore the field.
- **Test:** Fetch `/sitemap.xml` (or the one `robots.txt` names).
- **Pass:** It loads, lists every indexable page on the canonical host, leaves out noindex and redirected URLs, and `lastmod` reflects real edits.

### B2. llms.txt · important
- **Principle:** A plain-text summary of the best pages, written for AI. It's an unofficial convention that not every engine reads yet, but it takes minutes to add.
- **Test:** Fetch `/llms.txt` and `/llms-full.txt`.
- **Pass:** `llms.txt` loads as text, opens with a one-line summary of what the site is, and links the most important pages with a line each, generated from the content so it stays current. `llms-full.txt` and a Markdown mirror of each page (`/<path>.md`) count as polish on top.

### B3. Google Search Console · critical
- **Principle:** Submitting the sitemap tells Google to come and look, and Search Console is the only first-party view of what Google indexed.
- **Test:** OpenSEO `list_search_console_sites` and `get_search_console_performance` (free). Ask the user whether the sitemap is submitted and shows "Success".
- **Pass:** The property is verified for the canonical host and connected to OpenSEO, and the sitemap is submitted. This is a user task; the agent can't submit it.

### B4. Bing Webmaster Tools · important
- **Principle:** Bing's index feeds ChatGPT search and Microsoft Copilot, so this is an AI search step too.
- **Test:** Ask the user.
- **Pass:** The site is verified in Bing Webmaster Tools with the sitemap submitted (importing from Search Console is fine). A user task.

### B5. IndexNow on deploy · important
- **Principle:** IndexNow tells Bing and other engines the moment a page changes. Google doesn't use it, which is why B3 still matters.
- **Test:** Look for the key file (`/<key>.txt`) and the ping in the build or deploy code.
- **Pass:** Changed URLs are pinged automatically on each production deploy, never from local or preview builds.

### B6. AI crawlers allowed · critical
- **Principle:** `robots.txt` tells crawlers what they may read. Blocking AI bots means AI answers can't cite you.
- **Test:** Fetch `/robots.txt`. Also fetch the homepage with a GPTBot user agent and check the status isn't 403 (a firewall or bot protection can block what robots.txt allows).
- **Pass:** Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot and Google-Extended are allowed (or not mentioned under a permissive `*`), the sitemap is listed, and no firewall blocks them. If the user chose to block training bots, that's a Decision; search bots still need access.

### B7. Readable without JavaScript · critical
- **Principle:** Many AI crawlers don't run JavaScript. If the text only appears after scripts load, they see an empty page.
- **Test:** Sweep: the word count of the raw HTML (no JS) for each sample page, compared with what the page shows in a browser.
- **Pass:** The main content, headings, links and JSON-LD are in the server HTML.

### B8. Internal links · important
- **Principle:** Crawlers find pages by following links, and links show which pages matter most.
- **Test:** Sweep: internal links per page, and pages in the sitemap no other page links to (orphans).
- **Pass:** No orphans; articles link to 2–3 related pages and to the product page they support; nav and footer reach every section.

### B9. Fast and mobile-friendly · important
- **Principle:** Google measures load speed and mobile usability (Core Web Vitals). Slow pages rank lower and lose clicks.
- **Test:** PageSpeed Insights API (`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile`) for the homepage and one article. Report LCP, CLS, INP and the performance score.
- **Pass:** LCP under 2.5s, CLS under 0.1, INP under 200ms on mobile. Partial: one metric in "needs improvement".

---

## Theme C: Stop sending mixed signals

When a site disagrees with itself about its own URLs, Google discounts all of them.

### C1. One host · critical
- **Principle:** `example.com` and `www.example.com` are two sites to a search engine. When the code says one and the server the other, every link takes a redirect detour and ranking credit splits.
- **Test:** `curl -sI` both hosts and `http://`. Compare the redirect target with the host used in canonicals, `og:url`, the sitemap and internal links.
- **Pass:** One host, every other variant 301/308-redirects to it in a single hop, and every file says the same host.

### C2. Canonical tags · critical
- **Principle:** A canonical tag names the one true URL for a page. Without it, tracking links and query strings create copies that compete with the original.
- **Test:** Sweep: `link rel="canonical"` per page. Fetch one page with `?utm_source=test` and check the canonical stays clean.
- **Pass:** Every indexable page has a self-referencing, absolute canonical on the canonical host, with no query string.

### C3. Correct og:url · important
- **Principle:** `og:url` is the address a page hands to Slack, LinkedIn or iMessage. If it says the homepage everywhere, shared links point to the wrong place.
- **Test:** Sweep: `og:url` per page.
- **Pass:** `og:url` equals the page's canonical on every page.

### C4. Permanent redirects · important
- **Principle:** A permanent redirect (301 or 308) carries ranking credit to the new URL. A temporary one (302 or 307) tells Google to keep the old URL.
- **Test:** The redirect config, and `curl -sI` on moved URLs and the host variants.
- **Pass:** Every permanent move uses 301/308, with no chains longer than one hop.

### C5. Empty pages hidden · important
- **Principle:** Placeholder and "coming soon" pages make the site look thin. Keep them out of the index until they have real content.
- **Test:** Sweep: pages under ~150 words of main content; check their `robots` meta.
- **Pass:** Thin pages are `noindex` and out of the sitemap, or filled in. A soft 404 (a "not found" page that returns 200) is a fail.

---

## Theme D: Make it run itself

Set the system up once so every future page is born right.

### D1. The site is owned code · important
- **Principle:** When every page is a file in the site's own repo and every change deploys automatically, an agent can do the weekly work. A hosted builder that limits code access caps how much can be automated.
- **Test:** `site.md` → Stack and Shipping.
- **Pass:** Pages live in the repo (Markdown, MDX or code), deploys are automatic, and the generated files (sitemap, llms.txt, JSON-LD, OG images, IndexNow) come from the content, not hand edits. On a hosted builder, mark what can't be automated and score the rest.

### D2. Rules baked into the page workflow · important
- **Principle:** Fixes that live only in a one-off sweep regress. When the page template or check command enforces them, every new page is born with its description, FAQs, structured data and preview image.
- **Test:** The blog or page template, the check command in `site.md`, and the site profile.
- **Pass:** New pages get A1–A6, C2 and C3 from the template or a check that fails the build, and `site.md` lists the check command.

### D3. Tracking where visitors come from, AI included · important
- **Principle:** You can't grow a channel you can't see. AI referrals show up as `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com` and `copilot.microsoft.com`, and a "how did you hear about us" answer catches the rest.
- **Test:** Look for analytics on the site and ask the user whether AI referrers show up as their own segment. Check the signup flow for a source question or UTM capture.
- **Pass:** Analytics loads on every page, AI referrers are visible as a segment, and signups record a source.

---

## Grading

For each theme: `points earned ÷ points possible` (n/a checks left out).
- **A** ≥ 90% · **B** ≥ 80% · **C** ≥ 70% · **D** ≥ 60% · **F** below. Add `+` or `−` for the top or bottom 3 points of a band.
- **Overall:** the same formula over all checks.

Grades are directional, not a benchmark. Their job is to show where the biggest wins are and to prove a fix stuck on the re-audit.
