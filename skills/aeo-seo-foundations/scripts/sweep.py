#!/usr/bin/env python3
"""Sweep a site's sitemap and collect page-level SEO/AEO evidence.

Fetches each URL's raw HTML the way a crawler that doesn't run JavaScript sees it,
and records the fields the foundation checks need. Standard library only.

Usage:
    python3 sweep.py https://www.example.com/sitemap.xml --out sweep.json [--limit 300]
"""
import argparse
import json
import re
import sys
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (compatible; aeo-seo-foundations-sweep/1.0)"


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.geturl(), resp.read().decode("utf-8", errors="replace")


def sitemap_urls(url, limit, seen=None):
    seen = seen or set()
    if url in seen:
        return []
    seen.add(url)
    _, _, body = fetch(url)
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)
    if "<sitemapindex" in body:
        out = []
        for child in locs:
            out += sitemap_urls(child, limit - len(out), seen)
            if len(out) >= limit:
                break
        return out[:limit]
    return locs[:limit]


class Page(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.title, self.meta, self.links = "", {}, {}
        self.h1 = self.h2 = 0
        self.h2_text, self.jsonld, self.imgs_no_alt, self.imgs = [], [], 0, 0
        self.internal_links = set()
        self.text_words = 0
        self._in = None
        self._buf = ""
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript"):
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in, self._buf = "jsonld", ""
            else:
                self._skip += 1
        elif tag == "title":
            self._in, self._buf = "title", ""
        elif tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
            self._in, self._buf = "h2", ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link" and a.get("rel"):
            self.links[a["rel"].lower()] = a.get("href", "")
        elif tag == "img":
            self.imgs += 1
            alt = (a.get("alt") or "").strip()
            src = a.get("src") or ""
            if a.get("alt") is None or (alt and alt.lower() in src.lower()):
                self.imgs_no_alt += 1
        elif tag == "a" and a.get("href"):
            href = urljoin(self.base, a["href"]).split("#")[0]
            if urlparse(href).netloc == urlparse(self.base).netloc:
                self.internal_links.add(href.rstrip("/"))

    def handle_endtag(self, tag):
        if tag in ("style", "noscript") or (tag == "script" and self._in != "jsonld"):
            self._skip = max(0, self._skip - 1)
        elif tag == "script" and self._in == "jsonld":
            self.jsonld.append(self._buf)
            self._in = None
        elif tag == "title" and self._in == "title":
            self.title, self._in = self._buf.strip(), None
        elif tag == "h2" and self._in == "h2":
            self.h2_text.append(self._buf.strip())
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


def sweep_page(url):
    try:
        status, final, html = fetch(url)
    except Exception as e:  # noqa: BLE001 - record any fetch failure as evidence
        return {"url": url, "error": str(e)}
    p = Page(final)
    p.feed(html)
    types, bad = jsonld_types(p.jsonld)
    desc = p.meta.get("description", "")
    return {
        "url": url,
        "status": status,
        "final_url": final,
        "redirected": final.rstrip("/") != url.rstrip("/"),
        "title": p.title,
        "title_len": len(p.title),
        "description": desc,
        "description_len": len(desc),
        "description_equals_title": bool(desc) and desc.strip() == p.title.strip(),
        "canonical": p.links.get("canonical", ""),
        "robots": p.meta.get("robots", ""),
        "og_url": p.meta.get("og:url", ""),
        "og_title": p.meta.get("og:title", ""),
        "og_image": p.meta.get("og:image", ""),
        "twitter_card": p.meta.get("twitter:card", ""),
        "h1_count": p.h1,
        "h2": p.h2_text[:20],
        "h2_questions": sum(1 for h in p.h2_text if h.endswith("?")),
        "jsonld_types": types,
        "jsonld_parse_errors": bad,
        "images": p.imgs,
        "images_missing_alt": p.imgs_no_alt,
        "raw_html_words": p.text_words,
        "internal_links_out": sorted(p.internal_links),
    }


def summarize(pages):
    ok = [p for p in pages if "error" not in p]
    descs = Counter(p["description"] for p in ok if p["description"])
    ogimg = Counter(p["og_image"] for p in ok if p["og_image"])
    linked = set()
    for p in ok:
        linked.update(p["internal_links_out"])
    return {
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
        "most_shared_og_image": ogimg.most_common(1)[0] if ogimg else None,
        "h1_not_one": sum(1 for p in ok if p["h1_count"] != 1),
        "no_jsonld": sum(1 for p in ok if not p["jsonld_types"]),
        "jsonld_parse_errors": sum(p["jsonld_parse_errors"] for p in ok),
        "images_missing_alt": sum(p["images_missing_alt"] for p in ok),
        "thin_under_150_words": [p["url"] for p in ok if p["raw_html_words"] < 150],
        "noindex": [p["url"] for p in ok if "noindex" in p["robots"].lower()],
        "orphans": [p["url"] for p in ok if p["url"].rstrip("/") not in linked],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sitemap")
    ap.add_argument("--out", default="sweep.json")
    ap.add_argument("--limit", type=int, default=300)
    args = ap.parse_args()

    urls = sitemap_urls(args.sitemap, args.limit)
    if not urls:
        sys.exit("No URLs found in the sitemap.")
    pages = []
    for i, u in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {u}", file=sys.stderr)
        pages.append(sweep_page(u))
    result = {"sitemap": args.sitemap, "summary": summarize(pages), "pages": pages}
    with open(args.out, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
