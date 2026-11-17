#!/usr/bin/env python3
"""Sweep a site's pages and collect page-level SEO/AEO evidence.

Fetches each URL's raw HTML the way a crawler that doesn't run JavaScript sees it,
and records the fields the foundation checks need. Standard library only.

Usage:
    python3 sweep.py https://www.example.com/sitemap.xml --out sweep.json [--limit 300]
    python3 sweep.py --urls https://example.com/,https://example.com/pricing --out sweep.json
    python3 sweep.py --urls urls.txt --out sweep.json

Options:
    --urls FILE_OR_LIST       Sweep these URLs instead of a sitemap (a file with one URL
                              per line, or a comma-separated list). If the sitemap is
                              missing or empty, the sweep falls back to the homepage and
                              the internal links on it.
    --extra-host URL          Fetch a URL on a second host (an app or sign-in subdomain)
                              and record its status, robots meta, X-Robots-Tag and whether
                              that host's robots.txt blocks it. Repeatable.
    --previous-sitemap FILE   An older sitemap (file path or URL). Every old URL is
                              followed; any that ends in a 4xx is listed in the summary.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

UA = "Mozilla/5.0 (compatible; aeo-seo-technical-audit-sweep/1.1)"
DEAD_END_MAX_LINKS = 2


def fetch(url, timeout=20):
    """Return (status, final_url, headers, body). 4xx/5xx come back as a status, not an exception."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.geturl(), resp.headers, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, e.geturl() or url, e.headers, body


def site_key(netloc):
    """www.example.com and example.com count as the same site."""
    host = netloc.lower()
    return host[4:] if host.startswith("www.") else host


def norm(url):
    """Compare URLs on site, path and query; ignore scheme, www, fragment and trailing slash."""
    u = urlparse(url)
    path = u.path.rstrip("/") or "/"
    return site_key(u.netloc) + path + (("?" + u.query) if u.query else "")


def parse_sitemap(body):
    """Return [(loc, lastmod or "")] for a urlset, or the child sitemap locs for an index."""
    entries = []
    for block in re.findall(r"<url>(.*?)</url>", body, re.S):
        loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", block)
        if loc:
            lastmod = re.search(r"<lastmod>\s*([^<\s]+)\s*</lastmod>", block)
            entries.append((loc.group(1), lastmod.group(1) if lastmod else ""))
    if not entries:  # sitemap index, or a urlset written without <url> wrappers
        entries = [(loc, "") for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)]
    return entries


def sitemap_entries(url, limit, seen=None):
    """Return {url: lastmod}, following sitemap indexes. Empty if the sitemap can't be read."""
    seen = seen if seen is not None else set()
    if url in seen or limit <= 0:
        return {}
    seen.add(url)
    try:
        status, _, _, body = fetch(url)
    except Exception as e:  # noqa: BLE001 - a missing sitemap is evidence, not a crash
        print(f"Sitemap {url}: {e}", file=sys.stderr)
        return {}
    if status >= 400:
        print(f"Sitemap {url}: HTTP {status}", file=sys.stderr)
        return {}
    out = {}
    if "<sitemapindex" in body:
        for child, _ in parse_sitemap(body):
            out.update(sitemap_entries(child, limit - len(out), seen))
            if len(out) >= limit:
                break
    else:
        for loc, lastmod in parse_sitemap(body):
            out.setdefault(loc, lastmod)
    return dict(list(out.items())[:limit])


class Page(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.title = ""
        self.titles_seen = 0
        self.meta, self.meta_all = {}, {}
        self.links, self.links_all = {}, {}
        self.h1 = self.h2 = 0
        self.h2_text, self.jsonld, self.imgs_no_alt, self.imgs = [], [], 0, 0
        self.internal_links = set()
        self.text_words = 0
        self._in = None
        self._buf = ""
        self._skip = 0
        self._svg = 0
        self._in_head = False
        self._seen_body = False

    def _keep(self, first, every, key, value):
        every.setdefault(key, []).append(value)
        first.setdefault(key, value)  # the first tag wins, as most crawlers read it

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "head":
            self._in_head = True
        elif tag == "body":
            self._in_head, self._seen_body = False, True
        elif tag == "svg":
            self._svg += 1
        if tag in ("script", "style", "noscript"):
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in, self._buf = "jsonld", ""
            else:
                self._skip += 1
        elif tag == "title":
            # Only the document title: inside <head> (or before <body> when there's no <head>), never inside <svg>.
            if self._svg == 0 and (self._in_head or not self._seen_body):
                self.titles_seen += 1
                if self.titles_seen == 1:
                    self._in, self._buf = "title", ""
        elif tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
            self._in, self._buf = "h2", ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self._keep(self.meta, self.meta_all, key, a.get("content", ""))
        elif tag == "link" and a.get("rel"):
            self._keep(self.links, self.links_all, a["rel"].lower(), a.get("href", ""))
        elif tag == "img":
            self.imgs += 1
            alt = (a.get("alt") or "").strip()
            src = a.get("src") or ""
            stem = src.split("?")[0].rsplit("/", 1)[-1].rsplit(".", 1)[0].lower()
            looks_like_file = bool(re.search(r"\.(png|jpe?g|webp|gif|svg|avif)$", alt.lower())) or (alt and " " not in alt and alt.lower() == stem and ("-" in alt or "_" in alt))
            if a.get("alt") is None or looks_like_file:
                self.imgs_no_alt += 1
        elif tag == "a" and a.get("href"):
            href = urljoin(self.base, a["href"]).split("#")[0]
            u = urlparse(href)
            if u.scheme in ("http", "https") and site_key(u.netloc) == site_key(urlparse(self.base).netloc):
                self.internal_links.add(href)

    def handle_endtag(self, tag):
        if tag == "head":
            self._in_head = False
        elif tag == "svg":
            self._svg = max(0, self._svg - 1)
        if tag in ("style", "noscript") or (tag == "script" and self._in != "jsonld"):
            self._skip = max(0, self._skip - 1)
        elif tag == "script" and self._in == "jsonld":
            self.jsonld.append(self._buf)
            self._in = None
        elif tag == "title" and self._in == "title":
            self.title, self._in = self._buf.strip(), None
        elif tag == "h2" and self._in == "h2":
            self.h2_text.append(self._buf.strip().rstrip("#¶§🔗 ").strip())
            self._in = None

    def handle_data(self, data):
        if self._in:
            self._buf += data
        if not self._skip and self._in != "jsonld":
            self.text_words += len(data.split())


def jsonld_types(blocks):
    types, errors = [], 0
    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if t:
                types.extend(t if isinstance(t, list) else [t])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    for b in blocks:
        try:
            walk(json.loads(b))
        except ValueError:
            errors += 1
    return sorted(set(types)), errors


def parse_page(url):
    """Fetch and parse one URL. Returns (status, final_url, headers, Page) or raises."""
    status, final, headers, html = fetch(url)
    p = Page(final)
    p.feed(html)
    return status, final, headers, p


def sweep_page(url, lastmod=None):
    try:
        status, final, headers, p = parse_page(url)
    except Exception as e:  # noqa: BLE001 - record any fetch failure as evidence
        return {"url": url, "error": str(e)}, set()
    types, bad = jsonld_types(p.jsonld)
    desc = p.meta.get("description", "")
    self_keys = {norm(url), norm(final)}
    out_links = sorted(h for h in p.internal_links if norm(h) not in self_keys)
    page = {
        "url": url,
        "status": status,
        "final_url": final,
        "redirected": final.rstrip("/") != url.rstrip("/"),
        "x_robots_tag": headers.get("X-Robots-Tag", "") if headers else "",
        "title": p.title,
        "title_len": len(p.title),
        "title_tags_in_head": p.titles_seen,
        "description": desc,
        "description_len": len(desc),
        "description_equals_title": bool(desc) and desc.strip() == p.title.strip(),
        "canonical": p.links.get("canonical", ""),
        "robots": p.meta.get("robots", ""),
        "og_url": p.meta.get("og:url", ""),
        "og_title": p.meta.get("og:title", ""),
        "og_description": p.meta.get("og:description", ""),
        "og_image": p.meta.get("og:image", ""),
        "twitter": {k: v for k, v in p.meta.items() if k.startswith("twitter:")},
        "twitter_card": p.meta.get("twitter:card", ""),
        "duplicate_tags": {k: v for k, v in {**p.meta_all, **{"link:" + r: h for r, h in p.links_all.items()}}.items() if len(v) > 1},
        "h1_count": p.h1,
        "h2": p.h2_text[:20],
        "h2_questions": sum(1 for h in p.h2_text if h.endswith("?")),
        "jsonld_types": types,
        "jsonld_parse_errors": bad,
        "images": p.imgs,
        "images_missing_alt": p.imgs_no_alt,
        "raw_html_words": p.text_words,
        "internal_links_out": len(out_links),
        "internal_links": out_links,
    }
    if lastmod is not None:
        page["sitemap_lastmod"] = lastmod
    return page, p.internal_links


def check_extra_host(url):
    """Status, robots meta, X-Robots-Tag and robots.txt for a URL on another host (e.g. an app subdomain)."""
    try:
        status, final, headers, p = parse_page(url)
    except Exception as e:  # noqa: BLE001
        return {"url": url, "error": str(e)}
    robots_meta = p.meta.get("robots", "")
    x_robots = headers.get("X-Robots-Tag", "") if headers else ""
    blocked = None
    u = urlparse(final)
    try:
        r_status, _, _, r_body = fetch(f"{u.scheme}://{u.netloc}/robots.txt")
        if r_status < 400:
            rp = RobotFileParser()
            rp.parse(r_body.splitlines())
            blocked = not rp.can_fetch("Googlebot", final)
        else:
            blocked = False
    except Exception:  # noqa: BLE001
        pass
    return {
        "url": url,
        "status": status,
        "final_url": final,
        "robots": robots_meta,
        "x_robots_tag": x_robots,
        "blocked_by_robots_txt": blocked,
        "indexable": status < 400 and "noindex" not in (robots_meta + " " + x_robots).lower() and not blocked,
    }


def check_previous_sitemap(source, limit):
    """Follow every URL in an older sitemap; return the ones that now end in a 4xx."""
    if os.path.isfile(source):
        with open(source) as f:
            urls = [loc for loc, _ in parse_sitemap(f.read())]
    else:
        urls = list(sitemap_entries(source, limit))
    bad = []
    for i, u in enumerate(urls[:limit], 1):
        print(f"[previous {i}/{min(len(urls), limit)}] {u}", file=sys.stderr)
        try:
            status, final, _, _ = fetch(u)
        except Exception as e:  # noqa: BLE001
            bad.append({"url": u, "error": str(e)})
            continue
        if 400 <= status < 500:
            bad.append({"url": u, "final_url": final, "status": status, "redirected": final.rstrip("/") != u.rstrip("/")})
    return len(urls[:limit]), bad


def read_url_list(arg):
    if os.path.isfile(arg):
        with open(arg) as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return [u.strip() for u in arg.split(",") if u.strip()]


def summarize(pages):
    ok = [p for p in pages if "error" not in p]
    descs = Counter(p["description"] for p in ok if p["description"])
    ogimg = Counter(p["og_image"] for p in ok if p["og_image"])
    linked = set()
    for p in ok:
        linked.update(norm(h) for h in p["internal_links"])
    summary = {
        "pages": len(pages),
        "errors": len(pages) - len(ok),
        "non_200": sum(1 for p in ok if p["status"] != 200),
        "redirected": sum(1 for p in ok if p["redirected"]),
        "missing_description": sum(1 for p in ok if not p["description"]),
        "description_equals_title": sum(1 for p in ok if p["description_equals_title"]),
        "description_out_of_range": sum(1 for p in ok if p["description"] and not 110 <= p["description_len"] <= 160),
        "duplicate_descriptions": sum(n for n in descs.values() if n > 1),
        "missing_canonical": sum(1 for p in ok if not p["canonical"]),
        "canonical_not_self": sum(1 for p in ok if p["canonical"] and p["canonical"].rstrip("/") != p["final_url"].split("?")[0].rstrip("/")),
        "og_url_not_canonical": sum(1 for p in ok if p["og_url"] and p["canonical"] and p["og_url"].rstrip("/") != p["canonical"].rstrip("/")),
        "missing_og_image": sum(1 for p in ok if not p["og_image"]),
        "missing_og_description": sum(1 for p in ok if not p["og_description"]),
        "missing_twitter_card": sum(1 for p in ok if not p["twitter_card"]),
        "most_shared_og_image": ogimg.most_common(1)[0] if ogimg else None,
        "pages_with_duplicate_tags": [p["url"] for p in ok if p["duplicate_tags"]],
        "h1_not_one": sum(1 for p in ok if p["h1_count"] != 1),
        "no_jsonld": sum(1 for p in ok if not p["jsonld_types"]),
        "jsonld_parse_errors": sum(p["jsonld_parse_errors"] for p in ok),
        "images_missing_alt": sum(p["images_missing_alt"] for p in ok),
        "thin_under_150_words": [p["url"] for p in ok if p["raw_html_words"] < 150],
        "noindex": [p["url"] for p in ok if "noindex" in (p["robots"] + " " + p["x_robots_tag"]).lower()],
        "x_robots_tag": {p["url"]: p["x_robots_tag"] for p in ok if p["x_robots_tag"]},
        "orphans": [p["url"] for p in ok if norm(p["url"]) not in linked and norm(p["final_url"]) not in linked],
        "dead_end_pages": [p["url"] for p in ok if p["internal_links_out"] <= DEAD_END_MAX_LINKS],
    }
    with_lastmod_field = [p for p in ok if "sitemap_lastmod" in p]
    if with_lastmod_field:
        summary["missing_lastmod"] = sum(1 for p in with_lastmod_field if not p["sitemap_lastmod"])
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sitemap", nargs="?", help="sitemap URL (optional with --urls)")
    ap.add_argument("--out", default="sweep.json")
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--urls", help="file with one URL per line, or a comma-separated list")
    ap.add_argument("--extra-host", action="append", default=[], metavar="URL")
    ap.add_argument("--previous-sitemap", metavar="FILE")
    args = ap.parse_args()
    if not args.sitemap and not args.urls:
        ap.error("give a sitemap URL or --urls")

    lastmods, source = {}, None
    if args.urls:
        urls = read_url_list(args.urls)[: args.limit]
        source = "url list"
    else:
        lastmods = sitemap_entries(args.sitemap, args.limit)
        urls = list(lastmods)
        source = "sitemap"
        if not urls:
            u = urlparse(args.sitemap)
            home = f"{u.scheme}://{u.netloc}/"
            print(f"No URLs in the sitemap; falling back to {home} and its internal links.", file=sys.stderr)
            source = "homepage and its links (sitemap missing or empty)"
            urls = [home]
    if not urls:
        sys.exit("No URLs to sweep.")

    pages, done = [], set()
    queue = list(urls)
    fallback = source.startswith("homepage")
    while queue and len(pages) < args.limit:
        u = queue.pop(0)
        if norm(u) in done:
            continue
        done.add(norm(u))
        print(f"[{len(pages) + 1}/{len(queue) + len(pages) + 1}] {u}", file=sys.stderr)
        page, links = sweep_page(u, lastmods.get(u) if source == "sitemap" else None)
        pages.append(page)
        if fallback and len(pages) == 1:
            queue += sorted(h for h in links if norm(h) not in done)

    result = {"source": source, "sitemap": args.sitemap, "summary": summarize(pages), "pages": pages}
    if args.extra_host:
        result["extra_hosts"] = [check_extra_host(u) for u in args.extra_host]
        result["summary"]["extra_hosts_indexable"] = [e["url"] for e in result["extra_hosts"] if e.get("indexable")]
    if args.previous_sitemap:
        checked, bad = check_previous_sitemap(args.previous_sitemap, args.limit)
        result["summary"]["previous_sitemap_urls_checked"] = checked
        result["summary"]["redirects_to_4xx"] = bad
    with open(args.out, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
