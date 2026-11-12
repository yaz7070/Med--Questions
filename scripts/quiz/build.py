"""Build every quiz page from scripts/quiz/template.html and scripts/quiz/data/*.json.

Run from the repo root: python3 scripts/quiz/build.py
Data file shape: {"title", "context", "questions": [{c, p, o, a, e, l}], "objectives": {id: text}}
Output: quartz/static/pages/<slug>.html
"""
import html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
QDIR = ROOT / "scripts" / "quiz"
OUT = ROOT / "quartz" / "static" / "pages"
TEMPLATE = (QDIR / "template.html").read_text()
sys.path.insert(0, str(ROOT / "scripts"))
from items import ITEMS  # noqa: E402
BLOCK = {it[1]: it[0] for it in ITEMS}  # slug -> block number, sets the quiz colour


def js(v):
    # keep "</script>" out of inline data
    return json.dumps(v, ensure_ascii=False).replace("</", "<\\/")


def build(path):
    d = json.loads(path.read_text())
    qs = d["questions"]
    for n, q in enumerate(qs, 1):
        assert {"c", "p", "o", "a", "e", "l"} <= q.keys(), f"{path.name} q{n} missing fields"
        assert 0 <= q["a"] < len(q["o"]), f"{path.name} q{n} bad answer index"
    page = (TEMPLATE
            .replace("__TITLE__", html.escape(d["title"]))
            .replace("__CONTEXT__", html.escape(d["context"]))
            .replace("__KEY__", "differential-" + path.stem)
            .replace("__BLOCK__", str(BLOCK.get(path.stem, 1)))
            .replace("__QUESTIONS__", js(qs))
            .replace("__OBJECTIVES__", js(d.get("objectives", {}))))
    (OUT / f"{path.stem}.html").write_text(page)
    return len(qs)


if __name__ == "__main__":
    files = [QDIR / "data" / f"{a}.json" for a in sys.argv[1:]] or sorted((QDIR / "data").glob("*.json"))
    for f in files:
        print(f.stem, build(f))
