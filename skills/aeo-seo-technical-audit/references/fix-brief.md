# Fix package brief

Fill this in for each subagent. It's the only context the subagent gets, so keep the evidence and file paths concrete. Delete the guidance in angle brackets.

```markdown
You're fixing one package of findings from an AEO/SEO technical audit of <domain>.
The repo is at <path>, on the branch <branch>. Work only on that branch.

## Your package: <package name>

<For each finding:>
### <ID(s)> · <title>
- Evidence: <live URLs, sweep counts, what the production HTML shows now>
- Where it lives: <file paths>
- Principle: <one or two sentences, from the report>
- Fix: <the fix prompt from the report>

## Files
- You may change: <paths or globs>
- Don't change: <files other packages own, and anything outside this list>. If you need one, stop and say which file and why.

## Rules
- The canonical host is <host>. Every URL you write uses it.
- Never link to a competitor's site.
- Use the site's existing helpers and components; don't add a new library without asking.
- Don't commit, push or deploy. Leave the changes in the working tree.

## Done means
- <What's true when it's fixed, per finding, e.g. "every page's HTML has a self-referencing canonical on <host> with no query string".>
- `<check command>` and `<build command>` pass.
- Checked locally: <how, e.g. "run <dev command>, curl three pages and confirm the canonical and og:url">.

## Report back
1. Each finding ID: fixed, partly fixed (what's left), or not fixed (why).
2. The files you changed.
3. Anything you noticed outside your package. Don't fix it.
4. Questions for the user, if any.
```
