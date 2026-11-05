"""Generate home, block, folder and wrapper pages for Differential."""
import pathlib, re, html

SPD = pathlib.Path("/tmp/claude-0/-home-claude/e23cfabf-ba8c-5f49-b0f6-18fc202068a5/scratchpad")
src = (SPD / "restructure.py").read_text()
ns = {"pathlib": pathlib}
exec(src[src.index("SP = "):src.index("STATIC =")], ns)
ITEMS = ns["ITEMS"]

C = pathlib.Path("/home/claude/med-notes/content")
FOM = C / "fom"
ART = "https://claude.ai/artifact/"

BLOCKS = {
    1: ("Early life and foundations", "Weeks 1–4", "Tasks of a physician, the human body, early life, the well child and adolescent."),
    2: ("Screening, cancer, aging and prescribing", "Weeks 5–8", "Adult screening, cancer, aging, therapeutics and prescribing."),
    3: ("Hematology", "Weeks 9–12", "Anemia, bleeding, myeloid disorders, lymphadenopathy and lymphoid disorders."),
    4: ("Infection and immunity", "Weeks 13–15", "Fever, antibiotics, sepsis and immune dysfunction."),
}
NOTES_BLOCKS = {3, 4}
e = html.escape


def fm(title, extra=""):
    return f'---\ntitle: "{title}"\n{extra}---\n\n'


def row(href, title, desc, external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return (f'<li><a class="row" href="{href}"{tgt}><span><strong>{e(title)}</strong>'
            f'<span class="desc">{e(desc)}</span></span><span class="go" aria-hidden="true">›</span></a></li>')


def rows(items):
    return '<ul class="rows">\n' + "\n".join(items) + "\n</ul>\n"


by = {}
for b, slug, title, aid, _src, kind, blurb in ITEMS:
    by.setdefault((b, kind), []).append((slug, title, aid, blurb))


def weeks(b):
    out = []
    for f in sorted((FOM / f"block-{b}").glob("week-*.md")):
        t = re.search(r'title: "(.*)"', f.read_text()).group(1)
        n = re.search(r"· (\d+) topics", f.read_text())
        desc = f"Nicole's Notes, {n.group(1)} topics" if (b in NOTES_BLOCKS and n) else "Notes coming"
        out.append((f"/fom/block-{b}/{f.stem}", t, desc))
    return out


# ---- wrapper pages for quizzes and flowcharts ----
for b, slug, title, aid, _src, kind, blurb in ITEMS:
    folder = FOM / f"block-{b}" / ("question-bank" if kind == "quiz" else "flowcharts")
    btns = f'<a class="btn primary" href="/static/pages/{slug}.html" target="_blank" rel="noopener">Open full screen</a>'
    if aid:
        label = "Open in Claude to save answers" if kind == "quiz" else "Open in Claude"
        btns += f' <a class="btn" href="{ART}{aid}" target="_blank" rel="noopener">{label}</a>'
    tag = "quiz" if kind == "quiz" else "flowchart"
    (folder / f"{slug}.md").write_text(
        fm(title, f"tags:\n  - block-{b}\n  - {tag}\ndescription: \"{blurb}\"\n")
        + f"{blurb}\n\n<div class=\"embed-actions\">{btns}</div>\n\n"
        + f'<iframe class="embed-page" src="/static/pages/{slug}.html" title="{e(title)}" loading="lazy"></iframe>\n'
    )

# ---- folder index pages ----
for (b, kind), items in by.items():
    folder = FOM / f"block-{b}" / ("question-bank" if kind == "quiz" else "flowcharts")
    head = "Question Bank" if kind == "quiz" else "Flowcharts"
    lead = ("Practice sets for this block. Each one plays in the page." if kind == "quiz"
            else "Workup maps. Start at the top and follow the results down.")
    lst = [row(f"/fom/block-{b}/{folder.name}/{s}", t, d) for s, t, a, d in items]
    if b == 3 and kind == "flow":
        lst.append(row(ART + "DffUNGsPBXLhosvg7YgRRi", "Approach to Microcytic Anemia", "Written guide. Opens in Claude.", True))
    (folder / "index.md").write_text(fm(head) + f"{lead}\n\n" + rows(lst))

# ---- block pages ----
for b, (name, wk, topics) in BLOCKS.items():
    d = FOM / f"block-{b}"
    body = f"{topics}\n\n"
    q = by.get((b, "quiz"))
    fl = by.get((b, "flow"))
    if q:
        body += f'<h2 class="section-title">Question bank</h2>\n' + rows(
            [row(f"/fom/block-{b}/question-bank/{s}", t, dd) for s, t, a, dd in q])
    if fl:
        lst = [row(f"/fom/block-{b}/flowcharts/{s}", t, dd) for s, t, a, dd in fl]
        if b == 3:
            lst.append(row(ART + "DffUNGsPBXLhosvg7YgRRi", "Approach to Microcytic Anemia", "Written guide. Opens in Claude.", True))
        body += f'<h2 class="section-title">Flowcharts</h2>\n' + rows(lst)
    if not q and not fl:
        body += '<p class="empty-note">No quizzes or flowcharts yet. Ask Claude to build a set for this block.</p>\n'
    body += f'<h2 class="section-title" id="weeks">Weeks</h2>\n' + rows([row(h, t, dd) for h, t, dd in weeks(b)])
    (d / "index.md").write_text(fm(f"Block {b} (Weeks {wk.split()[1]})", f"tags:\n  - block-{b}\n") + body)

# ---- question bank overview ----
qb = "Every practice set in one place, grouped by block.\n\n"
for b, (name, wk, _) in BLOCKS.items():
    q = by.get((b, "quiz"))
    qb += f'<h2 class="section-title">Block {b}: {e(name)}</h2>\n'
    qb += rows([row(f"/fom/block-{b}/question-bank/{s}", t, dd) for s, t, a, dd in q]) if q else '<p class="empty-note">No sets yet.</p>\n'
(C / "question-bank" / "index.md").write_text(fm("Question Bank") + qb)

# ---- FoM index ----
(FOM / "index.md").write_text(fm("Foundations of Medicine") + rows(
    [row(f"/fom/block-{b}/", f"Block {b}: {n}", f"{w}. {t}") for b, (n, w, t) in BLOCKS.items()]))

# ---- home ----
def chip(href, n, label):
    return f'<a class="chip" href="{href}"><b>{n}</b> {label}</a>'

block_rows = []
for b, (name, wk, topics) in BLOCKS.items():
    chips = []
    q, fl = by.get((b, "quiz"), []), by.get((b, "flow"), [])
    if q:
        chips.append(chip(f"/fom/block-{b}/question-bank/", len(q), "quizzes" if len(q) > 1 else "quiz"))
    if fl:
        chips.append(chip(f"/fom/block-{b}/flowcharts/", len(fl), "flowcharts"))
    if b in NOTES_BLOCKS:
        chips.append(chip(f"/fom/block-{b}/#weeks", len(weeks(b)), "weeks of notes"))
    if not chips:
        chips.append('<span class="chip empty">Coming soon</span>')
    block_rows.append(
        f'<li class="block-row"><span class="block-num" aria-hidden="true">{b}</span>'
        f'<div class="block-main"><span class="weeks">{wk}</span><h3><a href="/fom/block-{b}/">{e(name)}</a></h3><p>{e(topics)}</p></div>'
        f'<div class="block-links">{"".join(chips)}</div></li>')

recent = [
    ("/fom/block-3/flowcharts/hemostasis-workup-map", "Hemostasis Workup Map", "Bleeding, platelets, VTE, anticoagulants, transfusion."),
    ("/fom/block-3/flowcharts/anemia-workup-map", "Anemia Workup Map", "From CBC to diagnosis, every branch."),
    ("/fom/block-3/question-bank/bleeding-block-drill", "Bleeding Block Drill", "Week 10 practice set."),
    ("/fom/block-2/question-bank/block-2-mock-exam", "Block 2 Mock Exam", "40 questions on the predicted blueprint."),
]

home = fm("Differential", 'description: "Study hub for Schulich Foundations of Medicine."\n') + f'''<section class="hero">
<h1>Differential</h1>
<p>Practice questions, workup maps and notes for Schulich Foundations of Medicine. Built by a student, for the years after.</p>
<div class="hero-actions">
<a class="btn primary" href="/question-bank/">Start practising</a>
<a class="btn" href="/fom/block-3/flowcharts/">Browse flowcharts</a>
</div>
</section>

<ul class="blocks">
{chr(10).join(block_rows)}
</ul>

<h2 class="section-title">Recently added</h2>
{rows([row(h, t, d) for h, t, d in recent])}
<p class="empty-note">Search anything from the sidebar, or press Ctrl K. Facts come from Nicole's Notes and course quizzes. Check details against your lecture slides.</p>
'''
(C / "index.md").write_text(home)
print("ok", {k: len(v) for k, v in by.items()})
