"""Blank Block 1-2 notes, add question banks and Block 3 flowcharts."""
import pathlib, re, shutil

SP = pathlib.Path("/tmp/claude-0/-home-claude/e23cfabf-ba8c-5f49-b0f6-18fc202068a5/scratchpad/artifact-files")
ATT = pathlib.Path("/mnt/user-data/attachments/e23cfabf-ba8c-5f49-b0f6-18fc202068a5")
C = pathlib.Path("/home/claude/med-notes/content")
FOM = C / "fom"
ART = "https://claude.ai/artifact/"

# (block, slug, title, artifact id, local dir prefix or attachment, kind, blurb)
ITEMS = [
    (1, "week-1-practice-quiz", "Week 1 Practice Quiz", "VPjPRBCvTmftCBT9QR5DKv", "e5ec5df5", "quiz", "20 questions. Ethics, physician roles, prevention, evidence."),
    (1, "week-2-practice-quiz", "Week 2 Practice Quiz", "4v7CK3hW8xQV2KS3E3XEvK", "1fb5a752", "quiz", "40 questions. Tissues, physiology, NMJ, imaging."),
    (1, "week-2-review-50", "Week 2 Review: 50 Questions", "7T7zRerwx1CjhSW3MpmMqP", "343c7a4f", "quiz", "50 questions by topic."),
    (1, "week-2-case-based-review", "Week 2 Case-Based Review", "LGHPwKNxzZAc3WXBR1MzwT", "9bffe528", "quiz", "Six clinical cases, DSSG style."),
    (1, "week-2-unfolding-case-review", "Week 2 Unfolding Case Review", "LXEso5vMTFzsFeyxEXQXV1", "9e167fb6", "quiz", "Cases that unfold between questions."),
    (1, "week-2-nmj-practice", "Week 2 NMJ Practice", "AeaLQaa2TrACZJvWQoURdK", "4e214f83", "quiz", "Neuromuscular junction physiology."),
    (1, "week-3-practice-chart", "Week 3 Practice Chart", "A4zc5htCyfsNKP9om6DKCX", "4970fac0", "quiz", "Genetics, screening, development, nutrition."),
    (1, "week-3-case-based", "Week 3 Case-Based Practice", "VdYskbXvUfZfxNFjMNudQg", "e7da4d48", "quiz", "Early life, vignette style."),
    (1, "week-4-case-based", "Week 4 Case-Based Practice", "Q7VgzyMm8AMRuuFFmssn7L", "bb2a5519", "quiz", "Immunology, ADHD, adolescents."),
    (1, "week-4-advanced-set-2", "Week 4 Advanced Practice (Set 2)", "BfFq3FssjeXLewk1gE1nMP", "5652c9c0", "quiz", "Harder Week 4 set."),
    (1, "weeks-1-4-comprehensive", "Weeks 1 to 4: Comprehensive", "8AwwiS7NaQc3XaqiaRDE2G", "3a13864b", "quiz", "50 questions across the block."),
    (1, "weeks-1-4-set-2", "Weeks 1 to 4: Set 2", "PsYxoAbyaf3oxFAhaWwFD1", "b937efb1", "quiz", "50 questions, objectives-aligned."),
    (1, "weeks-1-4-set-3", "Weeks 1 to 4: Set 3", "Y27c9PYNcieBU6yhPYv3vK", "fb331d00", "quiz", "50 questions, Weeks 3 and 4 emphasis."),
    (2, "block-2-quiz", "Block 2 Quiz", "YQmuorEbgHXpqAPhMNn9Ec", "fe5d150d", "quiz", "50 questions, Weeks 5 to 8."),
    (2, "block-2-set-2", "Block 2 Set 2", "VfLxVQkeYdGCJXhQvPv4AB", "e81a71cb", "quiz", "50 questions on untested objectives."),
    (2, "block-2-mock-exam", "Block 2 Mock Exam", "Ker2ZpZUjFWorocc423MK9", "970d3ab5", "quiz", "40 questions on the predicted blueprint."),
    (2, "block-2-review-set", "Block 2 Review Set", "EpGFfYr32CnPFPgZY7nru2", "6fe028df", "quiz", "30 questions from your mock exam misses."),
    (2, "spinal-pathways-quiz", "Spinal Pathways Quiz", "StADuqo4uUhYRng9jw88WE", "d1991518", "quiz", "20 questions. Tracts and lesion localization."),
    (2, "brain-pathways-quiz", "Brain Pathways Quiz", "HeXHwam6kHBSmT8EEGRn9t", "86cf67fd", "quiz", "20 questions. Visual, motor, cortical pathways."),
    (3, "bleeding-block-drill", "Bleeding Block Drill", "35vqwJy7vMUiXUQzqrAcMD", "10e26f4d", "quiz", "Week 10 bleeding and coagulation."),
    (3, "anemia-workup-map", "Anemia Workup Map", None, ATT / "1434b94a-Anemia_Workup_Map.html", "flow", "Full Week 9 workup from CBC to diagnosis."),
    (3, "hemostasis-workup-map", "Hemostasis Workup Map", None, ATT / "488c6756-Hemostasis_Workup_Map.html", "flow", "Week 10: bleeding, platelets, VTE, anticoagulants, transfusion."),
    (3, "anemia-speedrun", "Anemia Speedrun", "9vndtWA2dspPkAoVuoTofs", "484ba73c", "flow", "One-page quick version."),
    (3, "anemia-differential-flowchart", "Anemia Differential Flowchart", "2yNnYTwgJX41Rz6Y4cvBdY", "0ff83724", "flow", "Differential by MCV."),
    (3, "microcytic-anemia-map", "Microcytic Anemia Map", "NJyT6TWovMZGPMisGQjQQT", "ac92582c", "flow", "Microcytic branch in detail."),
]

STATIC = pathlib.Path("/home/claude/med-notes/quartz/static/pages")  # raw html lives here, copied as assets
if STATIC.exists():
    shutil.rmtree(STATIC)
STATIC.mkdir(parents=True)

# 1. blank Block 1 and 2 week pages (keep title and tags)
for b in (1, 2):
    for f in sorted((FOM / f"block-{b}").glob("week-*.md")):
        fm = re.match(r"^---\n.*?\n---\n", f.read_text(), re.S).group(0)
        f.write_text(fm)

# 2. wrapper pages
groups = {}
for b, slug, title, aid, src, kind, blurb in ITEMS:
    srcfile = src if isinstance(src, pathlib.Path) else next(SP.glob(src + "*/index.html"))
    shutil.copy(srcfile, STATIC / f"{slug}.html")
    folder = FOM / f"block-{b}" / ("question-bank" if kind == "quiz" else "flowcharts")
    folder.mkdir(exist_ok=True)
    tag = "quiz" if kind == "quiz" else "flowchart"
    links = f'<a class="embed-open" href="/static-pages/{slug}.html" target="_blank">Open full screen ↗</a>'
    if aid:
        extra = " (saves your answers)" if kind == "quiz" else ""
        links += f' · <a href="{ART}{aid}" target="_blank">Open in Claude{extra} ↗</a>'
    page = (
        "---\n"
        f'title: "{title}"\n'
        f"tags:\n  - block-{b}\n  - {tag}\n"
        f'description: "{blurb}"\n'
        "---\n\n"
        f"{blurb}\n\n"
        f"{links}\n\n"
        f'<iframe class="embed-page" src="/static-pages/{slug}.html" title="{title}" loading="lazy"></iframe>\n'
    )
    (folder / f"{slug}.md").write_text(page)
    groups.setdefault((b, kind), []).append((slug, title, blurb))

# 3. folder index pages
names = {1: "Block 1", 2: "Block 2", 3: "Block 3", 4: "Block 4"}
for (b, kind), rows in groups.items():
    folder = FOM / f"block-{b}" / ("question-bank" if kind == "quiz" else "flowcharts")
    head = "Question Bank" if kind == "quiz" else "Flowcharts"
    body = "\n".join(f"| [[{folder.relative_to(C)}/{s}\\|{t}]] | {d} |" for s, t, d in rows)
    (folder / "index.md").write_text(
        f'---\ntitle: "{names[b]} {head}"\n---\n\n| {"Quiz" if kind=="quiz" else "Map"} | What it covers |\n|---|---|\n{body}\n'
    )

# 4. block index pages
blocknames = {1: "Block 1: Early Life and Foundations", 2: "Block 2: Screening, Cancer, Aging, Prescribing",
              3: "Block 3: Hematology", 4: "Block 4: Infection and Immunity"}
for b in range(1, 5):
    d = FOM / f"block-{b}"
    lines = [f'---\ntitle: "{blocknames[b]}"\ntags:\n  - block-{b}\n---\n']
    if (d / "question-bank").exists():
        lines.append(f"## Question Bank\n\n[[fom/block-{b}/question-bank/index|All {names[b]} quizzes]] ({len(groups[(b,'quiz')])})\n")
    if (d / "flowcharts").exists():
        lines.append(f"## Flowcharts\n\n[[fom/block-{b}/flowcharts/index|All {names[b]} flowcharts]] ({len(groups[(b,'flow')])})\n")
    weeks = sorted(d.glob("week-*.md"))
    wl = []
    for f in weeks:
        t = re.search(r'title: "(.*)"', f.read_text()).group(1)
        wl.append(f"- [[fom/block-{b}/{f.stem}|{t}]]")
    lines.append(("## Weeks\n\n" if b >= 3 else "## Weeks (notes coming)\n\n") + "\n".join(wl) + "\n")
    (d / "index.md").write_text("\n".join(lines))

# 5. top-level question bank overview
qb = ["---\ntitle: Question Bank\n---\n", "Every practice set, by block. Each page plays the quiz in place. Use \"Open in Claude\" to keep your answers saved.\n"]
for b in range(1, 5):
    rows = groups.get((b, "quiz"))
    if not rows:
        qb.append(f"## {names[b]}\n\nNone yet.\n")
        continue
    qb.append(f"## {names[b]}\n\n| Quiz | What it covers |\n|---|---|\n" + "\n".join(
        f"| [[fom/block-{b}/question-bank/{s}\\|{t}]] | {d} |" for s, t, d in rows) + "\n")
(C / "question-bank" / "index.md").write_text("\n".join(qb))
print({k: len(v) for k, v in groups.items()})
