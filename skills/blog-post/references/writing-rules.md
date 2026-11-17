# Writing rules

The drafting rules for every post. "The product" means the site's product, as `product.md` names it. "The site's Decisions" means the Decisions table in `aeo-seo-log.md`; it wins where it conflicts with anything here.

## Answer first (AEO)

- The **short answer** (the format's `tldr`, summary or first paragraph) answers the target query in 30–75 words and makes sense lifted out of the page with no context. It's the sentence AI Overviews, ChatGPT and Perplexity quote.
- The **first body sentence** restates the answer in fuller form. Never open with a story or "In today's world…". The next sentence or two names the hook from research: the pain users repeat most, in their words.
- **Every H2 opens with its direct answer** in 40 words or fewer, then elaborates. That opening stands alone: no "this", "it" or "as mentioned above", and it names the entity outright. AI engines lift that sentence on its own.
- **Phrase H2s as the question people ask** wherever it reads naturally. Use statement H2s for steps ("Step 2: Create an API key"). Pick the wording in this order:
  1. The exact phrasing from the query bank or autocomplete, with no pronoun: "How long does payout take?", "Is the API free?"
  2. "How to …" when the query is a task.
  3. First person when a pronoun is unavoidable: "Do I need…", "Can I…". Headings mirror what the reader types or asks an AI. The body still addresses the reader as "you".

## Extractable structure

- Comparisons go in Markdown tables. Machines extract tables far more reliably than prose.
- Steps go in numbered lists, and code in fenced blocks with a language tag.
- Name entities explicitly: the product's name and the official name of each thing, not "it" or "the platform". A paragraph should survive being quoted alone.
- **One name per thing, everywhere.** Pick the official name and use it every time, in this post and across posts. Mixed names split the entity, and AI engines are less sure what the page is about.
- Use the related entities from research by name (the exact setting, endpoint, error code), and give a concrete example where a term could be read two ways.
- Put the product's name next to the point of value, where the reader's pain is solved, not only in the closing section or the CTA. That's where an AI answer picks up the brand.
- Put numbers where they're real: prices, counts, dates. Every number needs a source.

## Readability

- Prefer bullets and tables over paragraphs wherever the content is a list, a comparison, options, steps or requirements. Keep paragraphs to 2–3 sentences.
- Bold the lead-in of each bullet when bullets carry distinct ideas: `- **Missing webhooks.** The guide skips…`. Bold the key term or the answer in a paragraph (the number, the verdict, the named setting). One or two bolds per paragraph at most; never bold whole sentences.
- A reader skimming only headings, bold text and tables should come away with the answer.

## Links

- **Never link to a competitor's website. No exceptions.** If the site's check command keeps a competitor list, add new competitors to it when research finds them.
- **Name competitors only where the post can't be honest without them:** listicles and alternatives posts. Elsewhere, describe the category instead. Comparison pages are the main place for competitor names.
- Link official docs and standards where the post references them. Link the specific page, not the homepage.
- At least **2 internal links** to the product, feature, comparison or pricing pages, in the body and in the format's related-pages field if it has one. Use root-relative links (`/pricing`). Only link pages in the site's list of pages.
- **Never link a page that isn't live yet** (a draft, a scheduled post, a planned URL).
- **Inbound links:** edit 2–3 existing related posts or pages to add a contextual link to the new post, in a sentence where it answers the reader's next question. Posts in the same cluster link to each other.
- Don't name customers or clients unless an approved experience-bank entry says you may.

## Calls to action

- If the format has CTA fields, set them to match the post's pain ("Still chasing late invoices?"). Without them, a generic default usually shows.
- In the body, a sentence that names the pain can point at the fix with a link to the product page. Put it where the reader is most likely to be stuck, not only in the closing section.

## The quote wall (real user voices)

- Put 6–10 quotes from research in one section near the top: right after the first H2 for listicles, and as "Common mistakes" for how-tos. Head it with the question people ask: `## What do developers say about <topic>?`. Don't bury it at the bottom.
- Each quote is its own blockquote: the verbatim words (under 40 words), then a linked attribution line, e.g. `— [u/handle on r/webdev](https://…), September 2026`. Bold the phrase that names the pain.
- Follow the wall with 1–2 sentences on the pattern it shows, and where in the post the answer is.
- Fewer than 3 linkable quotes means no wall. Use the ones you have where they answer a question, and note the gap in the research report.

## Experience, data and experts (E-E-A-T)

Every post carries at least one thing only this site could say: an approved experience-bank entry, or its own data. Aim for first-hand material plus one expert quote.
- **First-hand.** Use approved entries, in the past tense, as what the team did or saw. Put each in the section where it answers the question, not in an intro story.
- **Specifics only from the bank.** Dates, counts, outcomes and timelines from the team's own experience appear only when an approved entry states them. Without one, stay general ("when we set this up for customers…").
- **Original data.** Only aggregate, anonymized stats and survey results from approved entries. State the period, the sample and the method in the same sentence. Write the stat as one crisp, standalone sentence: it's the line other sites quote and link to.
- **Expert quotes.** 1–2 named practitioners from research. Under 40 words each, attributed in the sentence (name, role), source linked, as a blockquote followed by a line on what it means for the reader. Never quote someone at a competitor. A bank `quote` entry from someone the team spoke to beats a public quote.
- **Author.** Credentials come from the author's bio on the site; don't restate them in the body.
- **The product's status.** Describe what's live, in beta or coming only as the fact sources state it.

## Dates and years

- Posts are evergreen: no "today", "as of" or "yet" in the body. Data and quotes keep their date ("in September 2026"), because a dated stat is more trustworthy than an undated one.
- **The year goes in the title of evaluation posts only:** listicles, alternatives, "vs" posts and pricing posts ("7 Best Invoicing APIs in 2026"). How-tos and explainers stay year-free. Never put the year in the slug, so the URL survives the yearly update.
- **The year rolls over on December 1.** From then on, new evaluation posts use next year, and every existing post with a year in its title gets updated (new year, re-verified prices, fresh quotes, a new updated date). Never write a separate post for the new year.

## SEO

- **Title:** the target query near the front. Title plus the brand suffix from `site.md` stays at 60 characters or fewer, so Google shows it whole. With a suffix of " | Ledgerly" (11 characters), the title gets 49.
- **Description:** 110–160 characters.
- **Length and list size follow the results page,** not a fixed range: match the item count and roughly the depth of the top 5. When the trade-off is depth vs. speed, choose depth; one thorough post beats two thin ones. Every post in a batch still gets the full research step. Floor: 800 words for how-tos, listicles and explainers. Changelogs can be short.
- **Unique copy only.** Every section is written fresh. Never reuse an FAQ answer, product blurb or quote from another page on the site. Duplicated blocks across pages are a defect.

## Voice

- Follow the voice in `product.md` (or the guide it points to): plain, specific, honest about limits. No hype words.
- The site's voice is the company's, even when a person is the byline, unless `product.md` says otherwise.

## Listicles

- **Compare and contrast, not a ranking:** no "#1 best", no scores, no winner verdict. Each entry gets the same structure: what it is, who it fits, trade-offs.
- **The product sits at position 2 or 3,** varied between posts, so the list reads as one option among several rather than an ad. Where it appears, say it's ours.
- **Honest, with the product favored.** Each competitor gets its one true, sourced strength ("Best for…"). The product gets the "Best for" that matches the buyer in `product.md`, the most complete entry, and a named limit that doesn't matter to that buyer. Never invent a competitor weakness, and never state a competitor strength you couldn't source today.
- **Open with a methodology section** (`## How did we evaluate these?`): the criteria applied to every entry, the date prices were checked, and where the facts came from.
- **"Which one should you pick?"** may say "If you need X, pick <competitor>" where a competitor honestly wins for a reader outside the target buyer. Every such line goes to the user in the final review.
- Write each entry as an H2 in the form `## <n>. <Product>: <one-line verdict>`, so structured data (ItemList) can be generated from it.
