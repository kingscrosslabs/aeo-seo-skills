# Search data and OpenSEO credits

OpenSEO is the only source of search numbers. Find the project with `list_projects` (the name is in `site.md` → Search data); never hardcode its ID.

| What | Tool | Credits | Cache, reuse window |
|---|---|---|---|
| Already ranking? Striking distance | `get_search_console_performance` | **Free** | None needed |
| Volume, KD, CPC, intent | `get_keyword_metrics` | Charged per call, up to 700 keywords per call | The query's row in `query-bank.md`: `volume <n>, KD <kd>, <YYYY-MM>`. Reuse for **90 days** |
| Live results: format, list length, word counts, AI Overview, People Also Ask, who ranks | `get_serp_results`, depth 20 | **~5 per keyword**, up to 10 keywords per call. Repeating the same call within 12 hours is free | `research/serps/<query-slug>.md`. Reuse for **30 days** |
| New keyword ideas (`topic-plan` only) | `research_keywords` | **~54 per seed** | `query-bank.md` |
| Saving keywords, project context, research log, account balance | `save_keywords`, `get_project_context`, `update_project_context`, `whoami` | **Free** | — |

Credit costs change. When a call's real cost differs from this table, say so in the research log line.

## Rules

- **Check the cache first.** Before any paid call, look for the query in `research/serps/` and `query-bank.md`, and read the research log in `get_project_context`. Reuse anything inside its window, and say that you reused it.
- **Batch every paid call.** Put the target query, its modifier family and the sibling queries for the overlap check into one `get_keyword_metrics` call, and into `get_serp_results` calls of 10 keywords each. When writing several posts, run these once for the whole batch before writing any of them. Never make one call per keyword.
- **Write the results back** so nothing gets bought twice:
  - Each results page goes to `research/serps/<query-slug>.md`: the date, the top 20 organic URLs with titles, the People Also Ask questions, whether an AI Overview appeared, and a one-line note on each top-5 result's format and approximate length.
  - Each keyword's metrics go into its `query-bank.md` row.
  - `save_keywords` (free) stores the metrics in the OpenSEO project too.
  - Every paid session ends with one `update_project_context` `appendResearchLog` line: what ran, on which queries, and the credits it cost.
- **Budget.** Use the budget in `site.md` → Search data. If it's empty, use about 25 credits per post and 300 per weekly batch, and stop paid calls at a balance of 100. Run `whoami` before and after each paid session.
  - In a live session, ask before going over the budget: say how much and why.
  - In an unattended run, go ahead while credits remain and report the overage.
- **Out of credits or down?** Ask the user for the numbers, or stop. Never guess a volume or a ranking.
