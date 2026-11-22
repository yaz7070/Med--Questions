"""Turn Nicole's Notes PDF pages (Block 4) into cards with bold preserved.

Output: cards.json, a list of {page, heading, html, text, bold}. A card starts at
each standalone bold heading line. Tables come from pdfplumber, with empty spacer
columns dropped and bold words marked with <b>.
"""
import json, re, html, sys, collections, pathlib
import pdfplumber

PDF = "/mnt/user-data/uploads/Nicole_s_Notes_FoM_Summative__1_.pdf"
FIRST, LAST = 119, 160
BULLETS = ("•", "-", "o ", "", "▪", "")


def isbold(w):
    return "Bold" in w["fontname"]


def words_to_html(ws):
    """Join words, wrapping runs of bold words in <b>."""
    out, run, bold = [], [], None
    for w in ws:
        b = isbold(w)
        if bold is None or b == bold:
            run.append(w["text"])
        else:
            out.append((bold, " ".join(run))); run = [w["text"]]
        bold = b
    if run:
        out.append((bold, " ".join(run)))
    s = ""
    for b, t in out:
        t = html.escape(t)
        s += (f"<b>{t}</b>" if b else t) + " "
    s = s.strip()
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    s = re.sub(r"\(\s+", "(", s)
    s = s.replace("</b> <b>", " ")
    return s


def cell_html(page, bbox):
    x0, top, x1, bottom = bbox
    ws = [w for w in page.extract_words(extra_attrs=["fontname"], use_text_flow=False)
          if w["x0"] >= x0 - 1 and w["x1"] <= x1 + 1 and w["top"] >= top - 1 and w["bottom"] <= bottom + 1]
    # keep reading order: group into lines
    ws.sort(key=lambda w: (round(w["top"] / 3), w["x0"]))
    lines = collections.OrderedDict()
    for w in ws:
        lines.setdefault(round(w["top"] / 3), []).append(w)
    return "<br>".join(words_to_html(v) for v in lines.values())


def table_html(page, t):
    rows = t.rows
    grid, boxes = [], []
    for r in rows:
        grid.append([cell_html(page, c) if c else "" for c in r.cells])
        boxes.append(list(r.cells))
    if not grid:
        return ""
    ncol = max(len(r) for r in grid)
    for r in grid:
        r += [""] * (ncol - len(r))
    for r in boxes:
        r += [None] * (ncol - len(r))
    body = grid[1:] if len(grid) > 1 else grid
    keep = [j for j in range(ncol) if any(r[j].strip() for r in body)] or list(range(ncol))
    # x-centre of each kept column, from body cells
    centre = {}
    for j in keep:
        xs = [((b[j][0] + b[j][2]) / 2) for b in boxes[1:] if b[j]]
        centre[j] = sum(xs) / len(xs) if xs else None
    # move text sitting in a spacer column (often a merged header cell) to the nearest kept column
    for i, r in enumerate(grid):
        for j in range(ncol):
            if j in keep or not r[j].strip() or not boxes[i][j]:
                continue
            cx = (boxes[i][j][0] + boxes[i][j][2]) / 2
            cands = [k for k in keep if centre[k] is not None and not r[k].strip()]
            if cands:
                k = min(cands, key=lambda k: abs(centre[k] - cx))
                r[k], r[j] = r[j], ""
    grid = [[r[j] for j in keep] for r in grid]
    grid = [r for r in grid if any(c.strip() for c in r)]
    h = '<div class="tw"><table>'
    for i, r in enumerate(grid):
        tag = "th" if i == 0 and all(("<b>" in c or not c) for c in r) else "td"
        h += "<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in r) + "</tr>"
    return h + "</table></div>"


MD = pathlib.Path("/mnt/skills/plugins/nicoles-notes/references/notes_block4.md").read_text().split("\n")[5:1790]
HEADINGS = {l.strip() for l in MD if re.fullmatch(r"[A-Z][A-Za-z0-9 ,()/&:'’+-]{3,60}", l.strip())}
norm = lambda s: re.sub(r"\s+", " ", s).strip()

cards = []
cur = None
pending_bullet = False


def new_card(page, heading):
    global cur
    cur = {"page": page, "heading": heading, "parts": []}
    cards.append(cur)


with pdfplumber.open(PDF) as pdf:
    for pn in range(FIRST, LAST + 1):
        page = pdf.pages[pn - 1]
        tables = page.find_tables()
        tboxes = [t.bbox for t in tables]
        items = []  # (top, kind, payload)
        for t in tables:
            items.append((t.bbox[1], "table", t))
        for k, im in enumerate(page.images):
            bb = (max(im["x0"], 0), max(im["top"], 0), min(im["x1"], page.width), min(im["bottom"], page.height))
            if (bb[2] - bb[0]) < 60 or (bb[3] - bb[1]) < 40:
                continue
            items.append((bb[1], "image", (bb, f"p{pn}_{k}")))
        ws = page.extract_words(extra_attrs=["fontname", "size"], use_text_flow=False)
        ws = [w for w in ws if not any(b[0] - 1 <= w["x0"] and w["x1"] <= b[2] + 1 and b[1] - 1 <= w["top"] and w["bottom"] <= b[3] + 1 for b in tboxes)]
        lines = collections.OrderedDict()
        for w in sorted(ws, key=lambda w: (round(w["top"] / 3), w["x0"])):
            lines.setdefault(round(w["top"] / 3), []).append(w)
        for k, v in lines.items():
            items.append((v[0]["top"], "line", v))
        items.sort(key=lambda x: x[0])
        for top, kind, payload in items:
            if kind == "image":
                bb, name = payload
                img = page.crop(bb).to_image(resolution=160).original.convert("RGB")
                img.save(str(pathlib.Path(__file__).parent / "figs" / f"{name}.webp"), "WEBP", quality=80)
                if cur is None:
                    new_card(pn, "Untitled")
                cur["parts"].append(("table", f'<figure><img src="FIGDIR/{name}.webp" alt="Figure from Nicole\'s Notes, page {pn}" loading="lazy"></figure>'))
                continue
            if kind == "table":
                if cur is None:
                    new_card(pn, "Untitled")
                cur["parts"].append(("table", table_html(page, payload)))
                continue
            v = payload
            text = " ".join(w["text"] for w in v).strip()
            if re.fullmatch(r"\d{1,3}", text) or text.startswith("Week 1") and ":" in text and pn in (119, 131, 143) or set(text) <= set("_ "):
                continue
            x0 = v[0]["x0"]
            first = v[0]["text"]
            if text in ("•", "-", "o", "▪", "", ""):
                pending_bullet = True
                continue
            is_bullet = pending_bullet or first in ("•", "-", "o", "▪", "", "") or first.startswith(("•", "-"))
            pending_bullet = False
            if not is_bullet and norm(text) in HEADINGS and x0 < 45:
                new_card(pn, norm(text))
                continue
            if cur is None:
                new_card(pn, "Untitled")
            body = words_to_html(v)
            if is_bullet:
                body = re.sub(r"^(<b>)?\s*[•▪]\s*", r"\1", body)
                lvl = 2 if first.startswith("-") or first == "o" or x0 > 60 else 1
                cur["parts"].append(("li%d" % lvl, body))
            elif cur["parts"] and cur["parts"][-1][0].startswith("li") and x0 > 45:
                k, b = cur["parts"][-1]
                cur["parts"][-1] = (k, b + " " + body)
            else:
                cur["parts"].append(("p", body))

# Render each card's parts to HTML
out = []
for c in cards:
    h, inlist = "", None
    for k, b in c["parts"]:
        if k.startswith("li"):
            if inlist is None:
                h += "<ul>"; inlist = 1
            cls = ' class="sub"' if k == "li2" else ""
            h += f"<li{cls}>{b}</li>"
        else:
            if inlist:
                h += "</ul>"; inlist = None
            h += b if k == "table" else f"<p>{b}</p>"
    if inlist:
        h += "</ul>"
    text = re.sub(r"<[^>]+>", " ", h)
    bold = re.findall(r"<b>(.*?)</b>", h)
    out.append({"page": c["page"], "heading": c["heading"], "html": h, "text": html.unescape(text), "bold": [html.unescape(x) for x in bold]})

json.dump(out, open(pathlib.Path(__file__).parent / "cards.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "cards")
for i, c in enumerate(out):
    print(i, c["page"], c["heading"][:60], len(c["html"]))
