"""End-to-end test of abhinemani.com's AI-agent setup, run against the live site.

Checks llms.txt, llms-full.txt, the Markdown sidecars (_plugins/agent_ready.rb),
the agent skills index, robots.txt and sitemaps, and the Cloudflare rules that
serve Markdown to clients sending `Accept: text/markdown`. It crawls every URL in
sitemap.xml three ways (the .md sibling, Accept: text/markdown, a browser Accept),
so a run takes a minute or two. Exits non-zero if any check fails.

Run with: python3 scripts/agent_test.py [site-url]
Standard library only. Behind a TLS-inspecting proxy, set SSL_CERT_FILE.
"""
import hashlib, json, random, re, ssl, sys, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://abhinemani.com").rstrip("/")
CTX = ssl.create_default_context()
BROWSER = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
results = []  # (section, name, ok, detail)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(urllib.request.HTTPSHandler(context=CTX))
OPENER_NR = urllib.request.build_opener(urllib.request.HTTPSHandler(context=CTX), NoRedirect)


def get(path, accept=None, ua="agent-test/1.0", method="GET", follow=True, bust=True):
    url = path if path.startswith("http") else SITE + path
    if bust:
        url += ("&" if "?" in url else "?") + f"cb={random.randrange(10**9)}"
    req = urllib.request.Request(url, method=method, headers={"User-Agent": ua})
    if accept:
        req.add_header("Accept", accept)
    try:
        r = (OPENER if follow else OPENER_NR).open(req, timeout=30)
        return r.status, r.headers, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, {}, str(e)


def check(section, name, ok, detail=""):
    results.append((section, name, bool(ok), detail))


def ctype(h):
    return (h.get("content-type") or "") if h else ""


# ---------------------------------------------------------------- llms.txt
S = "llms.txt"
st, h, llms = get("/llms.txt")
check(S, "/llms.txt returns 200 text/plain", st == 200 and "text/plain" in ctype(h), f"{st} {ctype(h)}")
check(S, "starts with H1 + blockquote summary (llmstxt.org shape)", llms.startswith("# Abhi Nemani") and "\n> " in llms[:400])
check(S, "no unrendered Liquid", "{{" not in llms and "{%" not in llms)
for sec in ["## Key pages", "## Essays", "## Public Innovation Academy", "## Portfolio case studies", "## Blog posts", "## Optional"]:
    check(S, f"has section '{sec}'", sec in llms)
links = re.findall(r"\]\((https?://[^)\s]+)\)", llms)
check(S, "links are absolute on abhinemani.com", links and all(l.startswith(SITE) for l in links), f"{len(links)} links")
check(S, "no duplicate links", len(links) == len(set(links)), f"{len(links) - len(set(links))} dupes")
empty_titles = re.findall(r"- \[\s*\]\(", llms)
check(S, "no empty link titles", not empty_titles, f"{len(empty_titles)} empty")
ent = re.findall(r"&(#x?[0-9a-f]+|amp|quot|lt|gt);", llms, re.I)
check(S, "no leftover HTML entities in titles", not ent, ", ".join(sorted(set(ent)))[:120])


def probe_link(u):
    st, h, body = get(u)
    return u, st, ctype(h), body


with ThreadPoolExecutor(12) as ex:
    probed = list(ex.map(probe_link, links))
bad = [(u, st) for u, st, _, _ in probed if st != 200]
check(S, f"all {len(links)} linked pages return 200", not bad, "; ".join(f"{u} {s}" for u, s in bad[:8]))
md_links = [p for p in probed if p[0].endswith(".md")]
badmd = [u for u, st, ct, b in md_links if st == 200 and ("text/markdown" not in ct or not b.startswith("# "))]
check(S, f"all {len(md_links)} .md links are text/markdown starting with '# '", not badmd, "; ".join(badmd[:5]))

# ---------------------------------------------------------------- sidecar quality
S = "Markdown sidecars"
for u, st, ct, body in md_links:
    if st != 200:
        continue
    probs = []
    if re.search(r"<script\b|<style\b", body, re.I): probs.append("script/style")
    if re.search(r"<!--", body): probs.append("html comment")
    if re.search(r"\{\{|\{%", body): probs.append("liquid")
    if re.search(r"\]\(/(?!/)", body): probs.append("relative link")
    m = re.search(r"^URL: (\S+)", body, re.M)
    if not m: probs.append("no URL line")
    elif not m.group(1).startswith(SITE): probs.append("URL line off-site")
    elif u.rsplit(".md", 1)[0] + "/" != m.group(1): probs.append(f"URL line {m.group(1)} != page")
    if "\n---\n" not in body[:1500]: probs.append("no meta separator")
    if probs:
        results.append((S, f"clean sidecar {u[len(SITE):]}", False, ", ".join(probs)))
n_bad = sum(1 for r in results if r[0] == S and not r[2])
check(S, f"{len(md_links)} linked sidecars are clean (no script/style/comments/Liquid/relative links, correct URL line)", n_bad == 0, f"{n_bad} with issues")
st, h, trust = get("/blog/2026/09/21/Trust.md")
check(S, "Trust.md has title, Published date, Author", trust.startswith("# We don't trust local government anymore.") and "Published: 2026-09-21" in trust and "Author:" in trust)
check(S, "Trust.md strips interactive chart code", "<script" not in trust and "d3." not in trust)
check(S, "Trust.md: no leftover <figure>/<div>/<span>", not re.search(r"<(figure|div|span|canvas|svg)\b", trust, re.I))
charts = re.findall(r"^\*\*Chart: .+", trust, re.M)
check(S, "Trust.md: all 5 charts rendered as '**Chart:**' text", len(charts) == 5, f"{len(charts)} found")
check(S, "Trust.md: chart summary carries the data", "54% to 41%" in trust and "10% to 42%" in trust)

# Site-wide Markdown hygiene, fixed by commits #7-#9
leftover, ents, local, iframes = [], [], [], []
for u, st, ct, body in md_links:
    if st != 200:
        continue
    p = u[len(SITE):]
    if re.search(r"<(div|span|section|figure|form|iframe|canvas|svg|input|button|a|strong|b|em|i|p|br|hr|img|ul|ol|li|h[1-6]|blockquote)\b", body, re.I): leftover.append(p)
    if re.search(r"&(mdash|ndash|minus|colon|nbsp|hellip|[lr]squo|[lr]dquo|amp|quot|#\d+|#x[0-9a-f]+);", body, re.I): ents.append(p)
    if "localhost" in body: local.append(p)
    iframes += re.findall(r"^Embedded (?:video|slides|PDF|content): \S+", body, re.M)
check(S, f"no HTML tags at all (layout, embeds, links, emphasis, lists, quotes…) in {len(md_links)} sidecars", not leftover, "; ".join(leftover[:8]))
check(S, "no undecoded HTML entities in sidecars", not ents, "; ".join(ents[:8]))
check(S, "no localhost links in sidecars", not local, "; ".join(local))
check(S, "embeds converted to 'Embedded …: <url>' lines", len(iframes) > 0, f"{len(iframes)} embeds")
total_md = sum(len(b) for _, st, _, b in md_links if st == 200)
check(S, "sidecar corpus size", True, f"{total_md:,} chars across {len(md_links)} sidecars")

# ---------------------------------------------------------------- llms-full.txt
S = "llms-full.txt"
st, h, full = get("/llms-full.txt")
check(S, "/llms-full.txt returns 200", st == 200, f"{st} {ctype(h)} {len(full):,} chars")
check(S, "is text/plain", "text/plain" in ctype(h), ctype(h))
n_docs = len(re.findall(r"^URL: ", full, re.M))
check(S, "contains every sidecar linked from llms.txt", n_docs >= len(md_links), f"{n_docs} docs vs {len(md_links)} sidecar links")
dates = re.findall(r"^Published: (\d{4}-\d\d-\d\d)", full, re.M)
check(S, "posts ordered newest first", dates == sorted(dates, reverse=True), f"{len(dates)} dated posts")
check(S, "no script/style/Liquid leaked", not re.search(r"<script\b|<style\b|\{\{|\{%", full, re.I))
check(S, "em dashes are real characters, none left as entities", "&mdash;" not in full and "&#8212;" not in full, f"{full.count('—')} dashes")

# ---------------------------------------------------------------- Agent skills
S = "Agent skills"
st, h, idx = get("/.well-known/agent-skills/index.json")
check(S, "index.json returns 200 application/json", st == 200 and "json" in ctype(h), f"{st} {ctype(h)}")
try:
    index = json.loads(idx)
except Exception as e:
    index = {}
    check(S, "index.json parses", False, str(e))
check(S, "declares discovery schema 0.2.0", index.get("$schema", "").endswith("/discovery/0.2.0/schema.json"), index.get("$schema"))
skills = index.get("skills", [])
check(S, "lists both skills", {s.get("name") for s in skills} == {"cite-abhi-nemani", "govtech-market-sizing"}, [s.get("name") for s in skills])
for s in skills:
    n = s.get("name")
    check(S, f"{n}: has type/description/url/digest", all(s.get(k) for k in ("type", "description", "url", "digest")) and s["type"] == "skill-md")
    req = urllib.request.Request(SITE + s["url"] + f"?cb={random.randrange(10**9)}", headers={"User-Agent": "agent-test/1.0"})
    raw = OPENER.open(req, timeout=30).read()
    check(S, f"{n}: SKILL.md sha256 matches index digest", s["digest"] == "sha256:" + hashlib.sha256(raw).hexdigest())
    txt = raw.decode()
    fm = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    check(S, f"{n}: front matter name matches folder", fm and re.search(rf"^name:\s*{re.escape(n)}\s*$", fm.group(1), re.M))
    check(S, f"{n}: description in index matches front matter", fm and s["description"] in fm.group(1))
    urls = re.findall(r"https://abhinemani\.com[^\s)>\"'`]*", txt)
    deadl = [u for u in set(urls) if get(u.rstrip(".,"))[0] != 200]
    check(S, f"{n}: all {len(set(urls))} abhinemani.com links resolve", not deadl, ", ".join(deadl))

# ---------------------------------------------------------------- robots / sitemaps
S = "robots.txt & sitemaps"
st, h, robots = get("/robots.txt")
check(S, "robots.txt 200", st == 200)
for bot in ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended"]:
    check(S, f"allows {bot}", re.search(rf"User-agent: {bot}\nAllow: /\n", robots))
check(S, "no Disallow rules", "Disallow" not in robots)
sms = re.findall(r"^Sitemap: (\S+)", robots, re.M)
check(S, "lists sitemap.xml and sitemap-projects.xml", len(sms) == 2, sms)
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_urls = []
for sm in sms:
    st, h, x = get(sm)
    try:
        locs = [e.text.strip() for e in ET.fromstring(x).findall(".//s:loc", ns)]
        check(S, f"{sm.rsplit('/', 1)[1]} is valid XML", True, f"{len(locs)} URLs")
        sitemap_urls += locs
    except Exception as e:
        check(S, f"{sm.rsplit('/', 1)[1]} is valid XML", False, str(e))
check(S, "sitemap-projects lists /govtech-market/", SITE + "/govtech-market/" in sitemap_urls)
check(S, "llms.txt not in sitemap (sitemap: false)", SITE + "/llms.txt" not in sitemap_urls)

# ---------------------------------------------------------------- crawl: every sitemap URL
S = "Full sitemap crawl"
page_urls = sorted({u for u in sitemap_urls if u.startswith(SITE) and u.endswith("/")})


def crawl(u):
    path = u[len(SITE):]
    md_path = "/index.md" if path == "/" else path.rstrip("/") + ".md"
    st_md, h_md, b_md = get(md_path)
    st_neg, h_neg, b_neg = get(path, accept="text/markdown")
    st_html, h_html, b_html = get(path, accept=BROWSER)
    return path, (st_md, ctype(h_md), b_md[:200]), (st_neg, ctype(h_neg), b_neg[:200], h_neg), (st_html, ctype(h_html), b_html, h_html)


with ThreadPoolExecutor(12) as ex:
    crawled = list(ex.map(crawl, page_urls))
gm = "/govtech-market/"
fails = {"sibling": [], "neg": [], "match": [], "html": [], "alt": [], "headtags": [], "vary": [], "link": []}
for path, md, neg, html in crawled:
    if path != gm and not (md[0] == 200 and "text/markdown" in md[1] and md[2].startswith("# ")):
        fails["sibling"].append(f"{path} {md[0]}")
    if path == gm:
        if neg[0] != 200: fails["neg"].append(f"{path} {neg[0]}")
    elif not (neg[0] == 200 and "text/markdown" in neg[1] and neg[2].startswith("# ")):
        fails["neg"].append(f"{path} {neg[0]} {neg[1]}")
    elif md[0] == 200 and neg[2] != md[2]:
        fails["match"].append(path)
    if not (html[0] == 200 and "text/html" in html[1]):
        fails["html"].append(f"{path} {html[0]} {html[1]}")
        continue
    if path != gm:
        if 'rel="llms-txt"' not in html[2] or 'rel="agent-skills"' not in html[2]:
            fails["headtags"].append(path)
        alt = re.search(r'<link rel="alternate" type="text/markdown"[^>]*href="([^"]+)"', html[2])
        if alt:
            if get(alt.group(1))[0] != 200: fails["alt"].append(f"{path} -> {alt.group(1)}")
    for hh, lbl in ((html[3], "html"), (neg[3], "md")):
        if "Accept" not in (hh.get_all("vary") or []) and "accept" not in ",".join(hh.get_all("vary") or []).lower():
            fails["vary"].append(f"{path} ({lbl})")
        lk = ",".join(hh.get_all("link") or [])
        if 'rel="llms-txt"' not in lk or 'rel="agent-skills"' not in lk:
            fails["link"].append(f"{path} ({lbl})")
n = len(crawled)
alts = sum(1 for _, _, _, html in crawled if re.search(r'type="text/markdown"', html[2] or ""))
check(S, f"every one of {n - 1} pages has a .md sibling (200, text/markdown, '# ' heading)", not fails["sibling"], "; ".join(fails["sibling"][:8]))
check(S, f"Accept: text/markdown returns Markdown on all {n} pages (govtech-market: 200 HTML)", not fails["neg"], "; ".join(fails["neg"][:8]))
check(S, "negotiated Markdown is identical to the .md sibling", not fails["match"], "; ".join(fails["match"][:8]))
check(S, f"browser Accept still returns HTML on all {n} pages", not fails["html"], "; ".join(fails["html"][:8]))
check(S, "every Jekyll page advertises llms-txt and agent-skills in <head>", not fails["headtags"], "; ".join(fails["headtags"][:8]))
check(S, f"<link rel=alternate type=text/markdown> resolves on all {alts} pages that have one", not fails["alt"], "; ".join(fails["alt"][:8]))
check(S, "Vary: Accept on every HTML and Markdown response", not fails["vary"], "; ".join(fails["vary"][:8]))
check(S, "Link header (llms-txt, agent-skills) on every HTML and Markdown response", not fails["link"], "; ".join(fails["link"][:8]))

# ---------------------------------------------------------------- Cloudflare negotiation edge cases
S = "Cloudflare negotiation edge cases"
T = "/blog/2026/09/21/Trust/"
for acc, want_md in [
    ("text/markdown", True),
    ("TEXT/MARKDOWN", True),
    ("text/markdown, text/html;q=0.9", True),
    ("text/html;q=0.9, text/markdown", True),
    ("text/markdown;charset=utf-8", True),
    (BROWSER, False),
    ("*/*", False),
    (None, False),
    ("application/json", False),
]:
    st, h, b = get(T, accept=acc)
    is_md = "text/markdown" in ctype(h)
    check(S, f"Accept {acc!r} -> {'Markdown' if want_md else 'HTML'}", st == 200 and is_md == want_md, f"{st} {ctype(h)}")
st, h, b = get(T + "?utm_source=test", accept="text/markdown", bust=False)
check(S, "query string kept on rewrite", st == 200 and b.startswith("# We don't trust"), f"{st}")
st, h, b = get(T, accept="text/markdown", method="HEAD")
check(S, "HEAD with Accept: text/markdown", st == 200 and "text/markdown" in ctype(h), f"{st} {ctype(h)}")
st, h, b = get("/blog/2026/09/21/Trust", accept="text/markdown")
check(S, "no-trailing-slash URL lands on Markdown after redirect", st == 200 and "text/markdown" in ctype(h), f"{st} {ctype(h)}")
st, h, b = get("/blog/2026/09/21/Trust.md", accept="text/markdown")
check(S, "direct .md request not double-rewritten", st == 200 and b.startswith("# We don't"), f"{st}")
st, h, b = get("/this-page-does-not-exist/", accept="text/markdown")
check(S, "missing page still 404s (no false 200)", st == 404, f"{st}")
st, h, b = get("/govtech-market/", accept="text/markdown")
check(S, "/govtech-market/ excluded from rewrite: 200 HTML", st == 200 and "text/html" in ctype(h), f"{st} {ctype(h)}")
for p in ["/feed.xml", "/llms.txt", "/.well-known/agent-skills/index.json", "/sitemap.xml"]:
    st, h, b = get(p, accept="text/markdown")
    check(S, f"{p} unaffected by Accept: text/markdown", st == 200 and "text/markdown" not in ctype(h), f"{st} {ctype(h)}")
for p in ["/feed.xml", "/.well-known/agent-skills/index.json", "/robots.txt"]:
    st, h, b = get(p)
    check(S, f"no agent Link/Vary header on non-HTML {p}", not (h.get_all("link") or []), ctype(h))
st, h, b = get(T, accept=BROWSER)
lk = h.get_all("link") or []
check(S, "Link header not duplicated", len([x for x in lk if "llms-txt" in x]) == 1, lk)
check(S, "HTML still not cached at edge (no Vary/cache mixups)", (h.get("cf-cache-status") or "") in ("DYNAMIC", ""), h.get("cf-cache-status"))
st, h, b = get(T, accept="text/markdown")
check(S, "Markdown not cached at edge", (h.get("cf-cache-status") or "") in ("DYNAMIC", "", "BYPASS"), h.get("cf-cache-status"))

# ---------------------------------------------------------------- AI crawler access
S = "AI crawler access (no bot blocking)"
for name, ua in [
    ("GPTBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.2; +https://openai.com/gptbot"),
    ("ClaudeBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)"),
    ("Claude-User", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)"),
    ("PerplexityBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)"),
    ("ChatGPT-User", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot"),
]:
    st1, h1, _ = get("/llms.txt", ua=ua)
    st2, h2, _ = get(T, ua=ua, accept="text/markdown")
    check(S, f"{name}: llms.txt and Markdown page both 200", st1 == 200 and st2 == 200 and "text/markdown" in ctype(h2), f"{st1}/{st2}")

# ---------------------------------------------------------------- report
out = []
cur = None
for sec, name, ok, det in results:
    if sec != cur:
        out.append(f"\n## {sec}")
        cur = sec
    out.append(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{det}]" if det not in ("", None, True) else ""))
passed = sum(r[2] for r in results)
out.append(f"\nTOTAL: {passed}/{len(results)} passed, {len(results) - passed} failed")
print("\n".join(out))
sys.exit(0 if passed == len(results) else 1)
