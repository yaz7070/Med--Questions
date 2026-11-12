"""Regenerate the home page, block pages and quiz or flowchart wrapper pages for Nexus.

Run from the repo root: python3 scripts/site_pages.py
Reads ITEMS from scripts/items.py. Raw HTML lives in quartz/static/pages/<slug>.html.

Site map: Home lists the four blocks with progress. Each block page lists its weekly
banks, practice tests and flowcharts with progress on every row. Each quiz or flowchart
has one wrapper page that embeds it. There are no other pages.
"""
import html, json, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from items import ITEMS  # noqa: E402

C = ROOT / "content"
SITE = json.loads((ROOT / "scripts" / "site.json").read_text())
FOM = C / "fom"
QDATA = ROOT / "scripts" / "quiz" / "data"
e = html.escape

BLOCKS = {
    1: ("Early life and foundations", "Weeks 1 to 4", "Tasks of a physician, the human body, early life, the well child and adolescent."),
    2: ("Screening, cancer, aging and prescribing", "Weeks 5 to 8", "Adult screening, cancer, aging, therapeutics and prescribing."),
    3: ("Hematology", "Weeks 9 to 12", "Anemia, bleeding, myeloid disorders, lymphadenopathy and lymphoid disorders."),
    4: ("Infection and immunity", "Weeks 13 to 15", "Fever, antibiotics, sepsis and immune dysfunction."),
}
FOLDER = {"quiz": "question-bank", "test": "practice-tests", "flow": "flowcharts"}
SECTIONS = [("quiz", "Weekly question banks"), ("test", "Practice tests"), ("flow", "Flowcharts")]


def fm(title, extra=""):
    return f'---\ntitle: "{title}"\n{extra}---\n\n'


def week_key(slug):
    m = re.search(r"week-(\d+)", slug)
    return int(m.group(1)) if m else 0


def href(b, kind, slug=""):
    return f"/fom/block-{b}/{FOLDER[kind]}/{slug}"


def qcount(slug):
    f = QDATA / f"{slug}.json"
    return len(json.loads(f.read_text())["questions"]) if f.exists() else 0


def short_name(b, kind, slug, title):
    """Row label inside a block page. The block and section already say the rest."""
    if kind == "quiz":
        return f"Week {week_key(slug)}"
    return re.sub(rf"^Block {b} ", "", title)


def topics(kind, blurb):
    """Blurb without the question count or a repeated week label."""
    t = re.sub(r"^\d+ questions\.?\s*", "", blurb)
    t = re.sub(r"^Week \d+, ", "", t)
    m = re.match(r"across (Weeks \d+ to \d+)\.", t)
    if m:
        return f"Mixed questions from {m.group(1)}, exam style."
    return t[:1].upper() + t[1:]


by = {}
for b, slug, title, aid, _unused, kind, blurb in ITEMS:
    by.setdefault((b, kind), []).append((slug, title, blurb))
for k in by:
    by[k].sort(key=lambda x: (week_key(x[0]), x[0]))

# Every scored set, for the progress script.
QUIZZES = []
for b in BLOCKS:
    for kind in ("quiz", "test"):
        for slug, title, blurb in by.get((b, kind), []):
            QUIZZES.append({"s": slug, "n": qcount(slug), "b": b, "t": title, "h": href(b, kind, slug).lstrip("/")})

# Progress script. Reads what each quiz saved in this browser ("differential-<slug>")
# and fills rows, block totals and the Continue link. Keep it free of blank lines.
PROG_JS = """<script>
(function(){
  const Q = __Q__;
  function stat(q){
    let d = null;
    try { d = JSON.parse(localStorage.getItem("differential-" + q.s) || "null"); } catch(e) {}
    let a = 0, c = 0;
    if (d && d.answers) for (const k in d.answers) {
      const r = d.answers[k];
      if (r && r.pick !== null && r.pick !== undefined) { a++; if (r.ok) c++; }
    }
    return {a: Math.min(a, q.n), c: c, u: (d && d.updatedAt) || ""};
  }
  function each(sel, fn){ document.querySelectorAll(sel).forEach(fn); }
  function run(){
    const sums = {all: {a: 0, n: 0}};
    let last = null;
    for (const q of Q) {
      const s = stat(q);
      sums[q.b] = sums[q.b] || {a: 0, n: 0};
      sums[q.b].a += s.a; sums[q.b].n += q.n; sums.all.a += s.a; sums.all.n += q.n;
      if (s.a && s.a < q.n && (!last || s.u > last.u)) last = {q: q, u: s.u};
      const row = document.querySelector('[data-quiz="' + q.s + '"]');
      if (!row) continue;
      q.href = row.getAttribute("href");
      row.querySelector(".pg-txt").textContent = !s.a ? q.n + " questions"
        : s.a < q.n ? s.a + " of " + q.n + " answered"
        : s.c + " of " + q.n + " correct";
      row.querySelector(".pg-bar i").style.width = (100 * s.a / q.n) + "%";
      row.querySelector(".set-go").textContent = !s.a ? "Start" : s.a < q.n ? "Continue" : "Review";
      row.classList.toggle("done", s.a >= q.n);
    }
    for (const k in sums) {
      const v = sums[k];
      each('[data-sum="' + k + '"]', el => { el.textContent = v.a ? v.a + " of " + v.n + " questions answered" : v.n + " questions, none answered yet"; });
      each('[data-sum-bar="' + k + '"]', el => { el.style.width = (v.n ? 100 * v.a / v.n : 0) + "%"; });
    }
    const el = document.getElementById("resume");
    if (el && last) { el.hidden = false; el.textContent = "Continue " + last.q.t; el.setAttribute("href", last.q.href || last.q.h); el.dataset.b = last.q.b; }
  }
  run();
  window.addEventListener("storage", run);
  window.addEventListener("pageshow", run);
})();
</script>
"""


def prog_js(block=None):
    q = [x for x in QUIZZES if block is None or x["b"] == block]
    return PROG_JS.replace("__Q__", json.dumps(q))


def moved(label, target):
    """A stub for an address that used to be a page. It forwards to where the content now lives."""
    return (fm("Moved")
            + f'<p class="moved">This page moved. <a href="{target}">Go to {label}</a>.</p>\n\n'
            + '<script>(function(){var a=document.querySelector(".moved a");if(a)location.replace(a.href);})();</script>\n')


# ---------- clear generated pages that no longer exist ----------
for old in ("question-bank", "flowcharts", "progress"):
    shutil.rmtree(C / old, ignore_errors=True)
(FOM / "index.md").unlink(missing_ok=True)
for b in BLOCKS:
    for folder in FOLDER.values():
        d = FOM / f"block-{b}" / folder
        if d.exists():
            for f in d.glob("*.md"):
                f.unlink()

# ---------- wrapper pages: one slim line, then the quiz or flowchart ----------
for b, slug, title, aid, _unused, kind, blurb in ITEMS:
    folder = FOM / f"block-{b}" / FOLDER[kind]
    folder.mkdir(parents=True, exist_ok=True)
    tag = {"quiz": "quiz", "test": "practice-test", "flow": "flowchart"}[kind]
    (folder / f"{slug}.md").write_text(
        fm(title, f"tags:\n  - block-{b}\n  - {tag}\ndescription: \"{blurb}\"\n")
        + f'<p class="embed-bar"><a href="/fom/block-{b}/">Block {b}</a><span class="sep" aria-hidden="true">/</span>'
        + f'<span class="here">{e(title)}</span>'
        + f'<a class="full" href="/static/pages/{slug}.html" target="_blank" rel="noopener">Open full screen</a></p>\n\n'
        + f'<iframe class="embed-page" src="/static/pages/{slug}.html" title="{e(title)}"></iframe>\n'
    )


# ---------- block pages ----------
def set_row(b, kind, slug, title, blurb):
    name, desc = short_name(b, kind, slug, title), topics(kind, blurb)
    if kind == "flow":
        return (f'<li><a class="set flow" href="{href(b, kind, slug)}"><span class="set-name">{e(name)}</span>'
                f'<span class="set-desc">{e(desc)}</span><span class="set-go">Open</span></a></li>')
    n = qcount(slug)
    return (f'<li><a class="set" href="{href(b, kind, slug)}" data-quiz="{slug}"><span class="set-name">{e(name)}</span>'
            f'<span class="set-desc">{e(desc)}</span>'
            f'<span class="set-pg"><span class="pg-txt">{n} questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span>'
            f'<span class="set-go">Start</span></a></li>')


for b, (name, wk, about) in BLOCKS.items():
    d = FOM / f"block-{b}"
    d.mkdir(parents=True, exist_ok=True)
    body = f'<p class="block-about">{wk}. {e(about)}</p>\n\n'
    has_sets = any(by.get((b, k)) for k in ("quiz", "test"))
    if has_sets:
        body += (f'<p class="block-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="{b}"></i></span>'
                 f'<span data-sum="{b}"></span><a id="resume" class="resume" hidden></a></p>\n\n')
    any_res = False
    for kind, label in SECTIONS:
        items = by.get((b, kind))
        if items:
            any_res = True
            body += f'<h2 class="section-title">{label}</h2>\n<ul class="sets">\n' + "\n".join(
                set_row(b, kind, s, t, bl) for s, t, bl in items) + "\n</ul>\n\n"
    if not any_res:
        body += '<p class="empty-note">Nothing here yet. Question banks and flowcharts for this block are on the way.</p>\n'
    if has_sets:
        body += prog_js(b)
    (d / "index.md").write_text(fm(f"Block {b}: {name}", f"tags:\n  - block-{b}\ndescription: \"{wk}. {about}\"\n") + body)
    # Old folder addresses (block-N/question-bank/ and so on) forward to the block page.
    for folder in FOLDER.values():
        if (d / folder).exists():
            (d / folder / "index.md").write_text(moved(f"Block {b}", f"/fom/block-{b}/"))
(FOM / "index.md").write_text(moved("the home page", "/"))
for old in ("question-bank", "flowcharts", "progress"):
    (C / old).mkdir(exist_ok=True)
    (C / old / "index.md").write_text(moved("the home page", "/"))

# ---------- home ----------
def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


rows = []
for b, (name, wk, about) in BLOCKS.items():
    q, t, fl = by.get((b, "quiz"), []), by.get((b, "test"), []), by.get((b, "flow"), [])
    has = [plural(len(q), "weekly bank", "weekly banks")] if q else []
    if t:
        has.append(plural(len(t), "practice test", "practice tests"))
    if fl:
        has.append(plural(len(fl), "flowchart", "flowcharts"))
    if q or t:
        pg = (f'<span class="block-pg"><span data-sum="{b}"></span>'
              f'<span class="pg-bar" aria-hidden="true"><i data-sum-bar="{b}"></i></span></span>')
    else:
        pg = '<span class="block-pg"><span>Coming soon</span></span>'
    rows.append(
        f'<li><a class="block" data-b="{b}" href="/fom/block-{b}/"><span class="block-tag">Block {b}</span>'
        f'<span class="block-main"><strong>{e(name)}</strong><span>{wk}{". " + ", ".join(has) if has else ""}</span></span>{pg}</a></li>')

total_q = sum(x["n"] for x in QUIZZES)
home = fm("Nexus", 'description: "Practice questions and flowcharts for Schulich Foundations of Medicine."\n') + f'''<section class="home-top">
<h1>Nexus</h1>
<p class="lede">New questions, generated with Claude for the class of 2030</p>
<p class="home-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="all"></i></span><span data-sum="all"></span><a id="resume" class="resume" hidden></a></p>
</section>

<ul class="blocks">
{chr(10).join(rows)}
</ul>

{prog_js()}'''
(C / "index.md").write_text(home)

# keep the site address in quartz.config.yaml in sync (used for metadata only)
cfg = ROOT / "quartz.config.yaml"
y = cfg.read_text()
y = re.sub(r"(\n  baseUrl: ).*", lambda m: m.group(1) + SITE["base_url"], y, count=1)
cfg.write_text(y)

print("ok", {f"B{k[0]} {k[1]}": len(v) for k, v in sorted(by.items())}, "questions:", total_q)
