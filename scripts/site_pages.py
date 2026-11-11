"""Regenerate home, block, folder and wrapper pages for Nexus.

Run from the repo root: python3 scripts/site_pages.py
Reads ITEMS from scripts/items.py. Raw HTML lives in quartz/static/pages/<slug>.html.
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from items import ITEMS  # noqa: E402

C = ROOT / "content"
import json as _sj
SITE = _sj.loads((ROOT / "scripts" / "site.json").read_text())
BASE = SITE.get("base_path", "").rstrip("/")  # "" when the site sits at a domain root
FOM = C / "fom"
ART = "https://claude.ai/artifact/"
e = html.escape

BLOCKS = {
    1: ("Early life and foundations", "Weeks 1–4", "Tasks of a physician, the human body, early life, the well child and adolescent."),
    2: ("Screening, cancer, aging and prescribing", "Weeks 5–8", "Adult screening, cancer, aging, therapeutics and prescribing."),
    3: ("Hematology", "Weeks 9–12", "Anemia, bleeding, myeloid disorders, lymphadenopathy and lymphoid disorders."),
    4: ("Infection and immunity", "Weeks 13–15", "Fever, antibiotics, sepsis and immune dysfunction."),
}
NOTES_BLOCKS: set = set()  # no blocks carry weekly notes pages
FOLDER = {"quiz": "question-bank", "test": "practice-tests", "flow": "flowcharts"}
HEAD = {"quiz": "Question Bank", "test": "Practice Tests", "flow": "Flowcharts"}
LEAD = {
    "quiz": "One bank per week. Each plays in the page and saves progress in your browser.",
    "test": "Full-length mixed tests across the block. Sit them like the real exam.",
    "flow": "Workup maps. Start at the top and follow the results down.",
}


def fm(title, extra=""):
    return f'---\ntitle: "{title}"\n{extra}---\n\n'


def row(href, title, desc, external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return (f'<li><a class="row" href="{href}"{tgt}><span><strong>{e(title)}</strong>'
            f'<span class="desc">{e(desc)}</span></span><span class="go" aria-hidden="true">›</span></a></li>')


def rows(items):
    return '<ul class="rows">\n' + "\n".join(items) + "\n</ul>\n"


def week_key(slug):
    m = re.search(r"week-(\d+)", slug)
    return int(m.group(1)) if m else 0


by = {}
for b, slug, title, aid, _unused, kind, blurb in ITEMS:
    by.setdefault((b, kind), []).append((slug, title, aid, blurb))
for k in by:
    if k[1] == "quiz":
        by[k].sort(key=lambda x: week_key(x[0]))


def weeks(b):
    out = []
    for f in sorted((FOM / f"block-{b}").glob("week-*.md")):
        t = re.search(r'title: "(.*)"', f.read_text()).group(1)
        n = re.search(r"· (\d+) topics", f.read_text())
        desc = f"Nicole's Notes, {n.group(1)} topics" if (b in NOTES_BLOCKS and n) else "Notes coming"
        out.append((f"/fom/block-{b}/{f.stem}", t, desc))
    return out


def href(b, kind, slug=""):
    return f"/fom/block-{b}/{FOLDER[kind]}/{slug}"


# wrapper pages
for b, slug, title, aid, _unused, kind, blurb in ITEMS:
    folder = FOM / f"block-{b}" / FOLDER[kind]
    folder.mkdir(parents=True, exist_ok=True)
    btns = f'<a class="btn primary" href="/static/pages/{slug}.html" target="_blank" rel="noopener">Open full screen</a>'
    if aid:
        btns += f' <a class="btn" href="{ART}{aid}" target="_blank" rel="noopener">Open in Claude</a>'
    tag = {"quiz": "quiz", "test": "practice-test", "flow": "flowchart"}[kind]
    (folder / f"{slug}.md").write_text(
        fm(title, f"tags:\n  - block-{b}\n  - {tag}\ndescription: \"{blurb}\"\n")
        + f"{blurb}\n\n<div class=\"embed-actions\">{btns}</div>\n\n"
        + f'<iframe class="embed-page" src="/static/pages/{slug}.html" title="{e(title)}" loading="lazy"></iframe>\n'
    )

# folder index pages
for (b, kind), items in by.items():
    folder = FOM / f"block-{b}" / FOLDER[kind]
    (folder / "index.md").write_text(
        fm(HEAD[kind]) + f"{LEAD[kind]}\n\n" + rows([row(href(b, kind, s), t, d) for s, t, a, d in items]))

# block pages
for b, (name, wk, topics) in BLOCKS.items():
    d = FOM / f"block-{b}"
    body = f"{topics}\n\n"
    any_res = False
    for kind, label in [("test", "Practice tests"), ("quiz", "Question bank"), ("flow", "Flowcharts")]:
        items = by.get((b, kind))
        if items:
            any_res = True
            body += f'<h2 class="section-title">{label}</h2>\n' + rows([row(href(b, kind, s), t, dd) for s, t, a, dd in items])
    if not any_res:
        body += '<p class="empty-note">Questions and flowcharts for this block are coming soon.</p>\n'
    wk_rows = weeks(b)
    if wk_rows:
        body += '<h2 class="section-title" id="weeks">Weekly notes</h2>\n' + rows([row(h, t, dd) for h, t, dd in wk_rows])
    (d / "index.md").write_text(fm(f"Block {b} (Weeks {wk.split()[1]})", f"tags:\n  - block-{b}\n") + body)

# question bank overview
qb = "Every practice set in one place. Practice tests mix the whole block. Weekly banks go deep on one week.\n\n"
for b, (name, wk, _) in BLOCKS.items():
    t, q = by.get((b, "test"), []), by.get((b, "quiz"), [])
    qb += f'<h2 class="section-title">Block {b}: {e(name)}</h2>\n'
    if t or q:
        qb += rows([row(href(b, "test", s), tt, dd) for s, tt, a, dd in t] + [row(href(b, "quiz", s), tt, dd) for s, tt, a, dd in q])
    else:
        qb += '<p class="empty-note">No sets yet.</p>\n'
(C / "question-bank").mkdir(exist_ok=True)
(C / "question-bank" / "index.md").write_text(fm("Question Bank") + qb)

# progress page
import json as _json
QDATA = ROOT / "scripts" / "quiz" / "data"
plist = []
for b, slug, title, aid, _u, kind, blurb in ITEMS:
    f = QDATA / f"{slug}.json"
    if kind in ("quiz", "test") and f.exists():
        n = len(_json.loads(f.read_text())["questions"])
        plist.append({"b": b, "slug": slug, "title": title, "n": n, "href": ".." + href(b, kind, slug), "kind": kind})
plist.sort(key=lambda x: (x["b"], x["kind"] != "test", week_key(x["slug"]), x["slug"]))
total_all = sum(x["n"] for x in plist)
(C / "progress").mkdir(exist_ok=True)
(C / "progress" / "index.md").write_text(fm("Progress", 'description: "Your progress across every question bank and practice test."\n') + f"""Your progress across every question bank and practice test. It reads what you have answered in this browser.

<div class="prog" id="prog">
<section class="prog-hero">
<div class="prog-num"><span id="p-ans">0</span><span class="prog-of">/ {total_all}</span></div>
<p class="prog-label">questions answered</p>
<div class="prog-bar" aria-hidden="true"><span id="p-bar"></span></div>
<p class="prog-stats" id="p-stats">Start any question bank and your progress shows here.</p>
</section>
<div id="p-blocks"></div>
</div>

<script>
(function(){{
  const QUIZZES = {_json.dumps(plist)};
  const NAMES = {_json.dumps({b: n for b, (n, w, t) in BLOCKS.items()})};
  function read(slug){{
    try {{ return JSON.parse(localStorage.getItem("differential-" + slug) || "null"); }} catch(e) {{ return null; }}
  }}
  function esc(s){{ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;"); }}
  function render(){{
    const root = document.getElementById("p-blocks");
    if (!root) return;
    let ans = 0, ok = 0, total = 0, started = 0;
    const byBlock = {{}};
    for (const q of QUIZZES) {{
      const d = read(q.slug);
      let a = 0, c = 0;
      if (d && d.answers) for (const k in d.answers) {{
        const r = d.answers[k];
        if (r && r.pick !== null && r.pick !== undefined) {{ a++; if (r.ok) c++; }}
      }}
      a = Math.min(a, q.n);
      ans += a; ok += c; total += q.n; if (a) started++;
      (byBlock[q.b] = byBlock[q.b] || []).push(Object.assign({{a, c}}, q));
    }}
    document.getElementById("p-ans").textContent = ans;
    document.getElementById("p-bar").style.width = (total ? 100 * ans / total : 0) + "%";
    document.getElementById("p-stats").textContent = ans
      ? Math.round(100 * ans / total) + "% of all questions. " + ok + " correct (" + Math.round(100 * ok / ans) + "%). " + started + " of " + QUIZZES.length + " sets started."
      : "Start any question bank and your progress shows here.";
    root.innerHTML = Object.keys(byBlock).map(b => {{
      const list = byBlock[b];
      const ba = list.reduce((s, x) => s + x.a, 0), bt = list.reduce((s, x) => s + x.n, 0);
      return `<h2 class="section-title">Block ${{b}}: ${{esc(NAMES[b])}} <span class="prog-sub">${{ba}} / ${{bt}}</span></h2>
        <ul class="rows">${{list.map(x => `<li><a class="row prog-row" href="${{x.href}}"><span><strong>${{esc(x.title)}}</strong>
        <span class="prog-mini"><i style="width:${{100 * x.a / x.n}}%"></i></span>
        <span class="desc">${{x.a ? x.a + " of " + x.n + " answered, " + x.c + " correct" : x.n + " questions, not started"}}</span></span>
        <span class="prog-pct">${{Math.round(100 * x.a / x.n)}}%</span></a></li>`).join("")}}</ul>`;
    }}).join("");
  }}
  render();
  document.addEventListener("nav", render);
  window.addEventListener("storage", render);
}})();
</script>
""")

# all flowcharts, grouped by block
fc = "Workup maps for every block. Start at the top of a chart and follow the findings down.\n\n"
for b, (name, wk, _) in BLOCKS.items():
    items = by.get((b, "flow"))
    if items:
        fc += f'<h2 class="section-title">Block {b}: {e(name)}</h2>\n' + rows([row(href(b, "flow", s_), t, dd) for s_, t, a, dd in items])
(C / "flowcharts").mkdir(exist_ok=True)
(C / "flowcharts" / "index.md").write_text(fm("Flowcharts") + fc)

# FoM index
(FOM / "index.md").write_text(fm("Foundations of Medicine") + rows(
    [row(f"/fom/block-{b}/", f"Block {b}: {n}", f"{w}. {t}") for b, (n, w, t) in BLOCKS.items()]))


# home
def chip(h, n, label):
    return f'<a class="chip" href="{h}"><b>{n}</b> {label}</a>'


def plural(n, one, many):
    return one if n == 1 else many


block_rows = []
total_q = 0
for b, (name, wk, topics) in BLOCKS.items():
    chips = []
    t, q, fl = by.get((b, "test"), []), by.get((b, "quiz"), []), by.get((b, "flow"), [])
    if t:
        chips.append(chip(href(b, "test"), len(t), plural(len(t), "practice test", "practice tests")))
    if q:
        chips.append(chip(href(b, "quiz"), len(q), plural(len(q), "weekly bank", "weekly banks")))
    if fl:
        chips.append(chip(href(b, "flow"), len(fl), plural(len(fl), "flowchart", "flowcharts")))
    if b in NOTES_BLOCKS:
        chips.append(chip(f"/fom/block-{b}/#weeks", len(weeks(b)), "weeks of notes"))
    if not chips:
        chips.append('<span class="chip empty">Coming soon</span>')
    block_rows.append(
        f'<li class="block-row"><span class="block-num" aria-hidden="true">{b}</span>'
        f'<div class="block-main"><span class="weeks">{wk}</span><h3><a href="/fom/block-{b}/">{e(name)}</a></h3><p>{e(topics)}</p></div>'
        f'<div class="block-links">{"".join(chips)}</div></li>')

for b, slug, title, aid, _u, kind, blurb in ITEMS:
    m = re.match(r"(\d+) questions", blurb)
    if m:
        total_q += int(m.group(1))

recent = [
    (href(2, "flow", "cancer-workup-map"), "Cancer Workup Map", "Breast mass, screening, pathology, treatment, hereditary cancer."),
    (href(3, "flow", "myeloid-disorders-map"), "Myeloid Disorders Map", "High and low counts, MPNs, leukemias, emergencies."),
    (href(3, "flow", "hemostasis-workup-map"), "Hemostasis Workup Map", "Bleeding, platelets, VTE, anticoagulants, transfusion."),
    (href(3, "flow", "anemia-workup-map"), "Anemia Workup Map", "From CBC to diagnosis, every branch."),
]

home = fm("Nexus", 'description: "Study hub for Schulich Foundations of Medicine."\n') + f'''<section class="hero">
<h1>Nexus</h1>
<p>New questions, generated with Claude for the class of 2030</p>
<div class="hero-actions">
<a class="btn primary" href="/question-bank/">Start practising</a>
<a class="btn" href="/flowcharts/">Browse flowcharts</a>
</div>
</section>

<ul class="blocks">
{chr(10).join(block_rows)}
</ul>

<h2 class="section-title">Recently added</h2>
{rows([row(h, t, d) for h, t, d in recent])}
<p class="empty-note">Search anything from the bar at the top, or press Ctrl K.</p>
'''
(C / "index.md").write_text(home)
# Quartz rewrites root-relative links inside page content to relative paths, so content needs no prefix.
# Only the nav links (plugin config) and the Progress page's script data carry BASE.

# keep the site address in quartz.config.yaml in sync (used for metadata only)
cfg = ROOT / "quartz.config.yaml"
y = cfg.read_text()
y = re.sub(r"(\n  baseUrl: ).*", lambda m: m.group(1) + SITE["base_url"], y, count=1)
cfg.write_text(y)

print("ok", {f"B{k[0]} {k[1]}": len(v) for k, v in sorted(by.items())}, "questions:", total_q)
