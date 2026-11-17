# Manual checks

Run these when the site has no check command. They cover what a check command would catch. Report each one as pass, fixed, or left (with the reason).

## Errors (fix before shipping)

- [ ] **Title** plus the brand suffix from `site.md` is 60 characters or fewer.
- [ ] **Description** is 110–160 characters.
- [ ] **Short answer** is 30–75 words.
- [ ] **Every required field** in the blog's template is filled, and no `[placeholder]` or guidance comment is left.
- [ ] **Slug** is lowercase kebab-case, 3–6 words, with no year, and no other post uses it.
- [ ] **Every internal link** points at a page in the site's list of pages that is live. None points at a draft.
- [ ] **No link** goes to a competitor's site.
- [ ] **Exactly one H1** (usually the title), and headings don't skip levels.
- [ ] **Code blocks** have a language tag.
- [ ] **Images** have alt text and exist at their paths.

## Warnings (fix unless there's a reason not to)

- [ ] At least 2 internal links to product, feature, comparison or pricing pages.
- [ ] Every H2 opens with a direct answer of 40 words or fewer.
- [ ] 2–4 FAQs, none repeating an H2.
- [ ] Word count meets the target from research, and at least 800 for how-tos, listicles and explainers.
- [ ] No competitor named outside a listicle or alternatives post.
- [ ] No "today", "as of" or "yet" in the body.
- [ ] The year is in the title only for evaluation posts, and it's the right year for today's date (it rolls over on December 1).
- [ ] The product's name appears near the point of value, not only in the closing section.

If the site would benefit from a real check command, note it for `aeo-seo-foundations`.
