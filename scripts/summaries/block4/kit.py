"""Building blocks for the Block 4 study guides.

Every function returns an HTML string. Content files (w13.py, w14.py, w15.py)
compose these. <b> marks a phrase Nicole bolded (shown highlighted).
<strong> is plain emphasis.
"""
import html as _h
import re

esc = _h.escape


def P(*xs):
    return "".join(f"<p>{x}</p>" for x in xs)


def UL(*xs):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"


def OL(*xs):
    return '<ol class="steps">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"


def topic(title, *parts, src=""):
    """One readable section with a heading and a source line."""
    sid = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", title).lower()).strip("-")
    s = f'<p class="srcline">{src}</p>' if src else ""
    return f'<section class="topic" id="{{tab}}-{sid}" data-title="{esc(re.sub(r"<[^>]+>", "", title))}"><h3>{title}</h3>{"".join(parts)}{s}</section>'


def callout(kind, body, title=None):
    """kind: key (must know), trap (exam trap), clin (clinical pearl), why (why it matters)."""
    t = title or {"key": "Must know", "trap": "Exam trap", "clin": "Clinical pearl", "why": "Why it matters"}[kind]
    return f'<div class="call {kind}"><p class="ct">{t}</p>{body}</div>'


def flow(*steps, caption=None, down=False):
    """Steps with arrows. Each step is a title or (title, detail)."""
    out = []
    for s in steps:
        t, d = (s, "") if isinstance(s, str) else s
        out.append(f'<div class="step"><p class="st">{t}</p>{f"<p class=sd>{d}</p>" if d else ""}</div>')
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    cls = " down" if down else (" many" if len(steps) > 4 else "")
    if cls == " many":
        out = [o.replace('<p class="st">', f'<p class="st"><span class="sn">{i+1}</span>', 1) for i, o in enumerate(out)]
    return f'<figure class="dia"><div class="flow{cls}">{"".join(out)}</div>{cap}</figure>'


def chain(*items, caption=None):
    """A compact one-line sequence, e.g. taxonomic ranks."""
    body = '<span class="ca" aria-hidden="true">›</span>'.join(f'<span class="ci">{x}</span>' for x in items)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia"><p class="chain">{body}</p>{cap}</figure>'


def cols(*panels, caption=None):
    """Side by side comparison. Each panel is (title, body_html)."""
    out = "".join(f'<div class="col"><p class="colh">{t}</p>{b}</div>' for t, b in panels)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia"><div class="cols n{len(panels)}">{out}</div>{cap}</figure>'


def tree(root, branches, caption=None):
    """A classification tree. branches: list of (label, [leaf, ...]) or (label, html)."""
    def node(label, kids):
        if isinstance(kids, str):
            return f'<li><span class="tn">{label}</span><p class="tleaf">{kids}</p></li>'
        inner = "".join(f'<li><span class="tl">{k}</span></li>' for k in kids)
        return f'<li><span class="tn">{label}</span><ul>{inner}</ul></li>'
    body = "".join(node(l, k) for l, k in branches)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia"><div class="tree"><p class="troot">{root}</p><ul class="tb">{body}</ul></div>{cap}</figure>'


def table(head, *rows, cls=""):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    cls = (cls + f" c{len(head)}").strip()
    return f'<div class="tw {cls}"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def grid(head, *rows, caption=None, key="Y = covers · S = some or selected · blank = no"):
    """Coverage grid. Cells: Y (yes), S (some), N or "" (no), or any other text."""
    def cell(c):
        m = {"Y": ('cy', "Yes"), "S": ('cs', "Some"), "N": ('cn', "No"), "": ('cn', "")}
        if c in m:
            cl, lab = m[c]
            return f'<td class="{cl}">{lab}</td>'
        return f"<td>{c}</td>"
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + f"<td>{row[0]}</td>" + "".join(cell(c) for c in row[1:]) + "</tr>" for row in rows)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia"><div class="tw grid c{len(head)}"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>{cap}</figure>'


def scale(title, bands, caption=None):
    """A horizontal band scale, e.g. S / I / R. bands: (label, range, tone)."""
    b = "".join(f'<div class="band {tone}"><p class="bl">{l}</p><p class="br">{r}</p></div>' for l, r, tone in bands)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia"><p class="dt">{title}</p><div class="scale">{b}</div>{cap}</figure>'


def svg(markup, caption=None, label=""):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="dia svgd" role="img" aria-label="{esc(label)}">{markup}{cap}</figure>'


def fig(src, caption):
    return (f'<figure class="pic"><a href="b4figs/{src}" target="_blank" rel="noopener"><img src="b4figs/{src}" loading="lazy" alt="{esc(caption)}"></a>'
            f'<figcaption>{caption} (tap to enlarge)</figcaption></figure>')


CSS = r"""
:root{--bg:#f6f5f2;--surface:#fff;--ink:#16191d;--muted:#4b525c;--faint:#69717c;--line:#dcd9d2;--soft:#efede8;
  --c:#9a5a06;--cbg:#f8eedd;--hl:#fbe1ad;--c2:#245b9a;--c2bg:#e7eef8;--ok:#2f6b3f;--okbg:#e5f1e7;--bad:#9b3426;--badbg:#f7e6e2;
  --font:"Atkinson Hyperlegible Next","Segoe UI",system-ui,-apple-system,sans-serif}
:root[data-theme="dark"]{--bg:#141518;--surface:#1c1e22;--ink:#eceef1;--muted:#b6bcc6;--faint:#8e96a2;--line:#353a42;--soft:#24272c;
  --c:#e3a548;--cbg:#2b2211;--hl:#5b4113;--c2:#93b9ec;--c2bg:#172231;--ok:#8fcf9d;--okbg:#18271b;--bad:#ee9a8b;--badbg:#2e1a16;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:17px;line-height:1.6;
  padding:20px max(16px,env(safe-area-inset-right,0px)) 64px max(16px,env(safe-area-inset-left,0px))}
.wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:18px}
h1,h2,h3,p,ul,ol,figure{margin:0}
header h1{font-size:clamp(25px,4.2vw,32px);line-height:1.15;letter-spacing:-.01em}
header .lede{color:var(--muted);margin-top:8px;max-width:62ch}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:10px;font-size:14px;color:var(--muted)}
details.lectures{font-size:14px;color:var(--muted);margin-top:8px}
details.lectures summary{cursor:pointer;font-weight:700}
details.lectures ul{margin-top:4px;padding-left:20px}
.bar{position:sticky;top:0;z-index:5;background:var(--bg);padding:8px 0 10px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:8px}
.search{display:flex;gap:8px;align-items:center}
.search input{flex:1;min-width:0;font:inherit;font-size:15px;padding:8px 12px;border:1.5px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.search input:focus{outline:2px solid var(--c);outline-offset:1px;border-color:var(--c)}
.count{font-size:13px;color:var(--faint);white-space:nowrap}
.tabs{display:flex;flex-wrap:wrap;gap:6px}
.tabs button{font:inherit;font-size:14px;font-weight:700;color:var(--muted);background:var(--surface);border:1.5px solid var(--line);border-radius:6px;padding:5px 11px;cursor:pointer;line-height:1.3}
.tabs button[aria-selected="true"]{color:var(--c);border-color:var(--c);background:var(--cbg)}
button:focus-visible,summary:focus-visible,a:focus-visible{outline:2px solid var(--c);outline-offset:2px}
.panel{display:flex;flex-direction:column;gap:22px}.panel[hidden]{display:none}
.phead h2{font-size:26px;line-height:1.2;color:var(--c)}
.phead .plede{color:var(--muted);margin-top:4px;max-width:62ch}
.toc{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:14.5px;margin-top:10px;padding-left:0;list-style:none}
.toc a{color:var(--ink);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px}
.toc a:hover{text-decoration-color:var(--c)}
.topic{display:flex;flex-direction:column;gap:12px;scroll-margin-top:120px}
.topic h3{font-size:20px;line-height:1.3;padding-top:14px;border-top:1px solid var(--line)}
.topic p{max-width:68ch}
.topic ul,.topic ol{padding-left:22px;display:flex;flex-direction:column;gap:5px;max-width:68ch}
ol.steps{counter-reset:s;list-style:none;padding-left:0}
ol.steps li{counter-increment:s;position:relative;padding-left:34px}
ol.steps li::before{content:counter(s);position:absolute;left:0;top:1px;width:24px;height:24px;border-radius:50%;background:var(--cbg);color:var(--c);font-weight:700;font-size:13.5px;display:grid;place-items:center}
b{font-weight:700;background:linear-gradient(transparent 58%,var(--hl) 58%);padding:0 1px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
strong{font-weight:700}
th b,.colh b,.st b,.ct b,.tn b{background:none}
.srcline{font-size:12.5px;color:var(--faint)}
.call{border-radius:8px;padding:11px 14px;display:flex;flex-direction:column;gap:6px;font-size:16px;border-left:4px solid}
.call .ct{font-size:13px;font-weight:700;letter-spacing:.01em}
.call ul{gap:3px}
.call.key{background:var(--cbg);border-color:var(--c)}.call.key .ct{color:var(--c)}
.call.trap{background:var(--badbg);border-color:var(--bad)}.call.trap .ct{color:var(--bad)}
.call.clin{background:var(--c2bg);border-color:var(--c2)}.call.clin .ct{color:var(--c2)}
.call.why{background:var(--okbg);border-color:var(--ok)}.call.why .ct{color:var(--ok)}
figure.dia{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:10px}
figure.dia figcaption,figure.pic figcaption{font-size:13px;color:var(--faint)}
.dt{font-weight:700;font-size:15px}
.flow{display:flex;align-items:stretch;gap:26px;flex-wrap:wrap}
.flow .step{flex:1 1 120px;position:relative;background:var(--soft);border-radius:8px;padding:9px 11px;min-width:0}
.flow .step:not(:last-child)::after{content:"";position:absolute;right:-19px;top:50%;width:12px;height:12px;border-top:2.5px solid var(--c);border-right:2.5px solid var(--c);transform:translateY(-50%) rotate(45deg)}
.flow .st{font-weight:700;font-size:15px;line-height:1.3}
.flow .sd{font-size:14px;color:var(--muted);line-height:1.45;margin-top:3px}
.flow.many{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.flow.many .step::after{display:none}
.sn{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--cbg);color:var(--c);font-size:12px;margin-right:6px;vertical-align:1px}
.chain{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;font-weight:700;font-size:15px}
.chain .ci{background:var(--soft);border-radius:6px;padding:4px 10px}.chain .ca{color:var(--c);font-size:20px;line-height:1}
.flow.down{flex-direction:column;gap:22px}
.flow.down .step{flex:none}
.flow.down .step:not(:last-child)::after{right:auto;left:50%;top:auto;bottom:-17px;transform:translateX(-50%) rotate(135deg)}
.cols{display:grid;gap:10px}
.cols.n2{grid-template-columns:1fr 1fr}.cols.n3{grid-template-columns:repeat(3,1fr)}.cols.n4{grid-template-columns:repeat(2,1fr)}
.col{background:var(--soft);border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.5;display:flex;flex-direction:column;gap:5px;min-width:0}
.col .colh{font-weight:700;font-size:15.5px;color:var(--c);line-height:1.3}
.col ul{padding-left:18px;gap:2px}
.tree .troot{font-weight:700;text-align:center;background:var(--cbg);color:var(--c);border-radius:8px;padding:6px 10px;width:fit-content;margin:0 auto 10px;max-width:100%}
.tree ul.tb{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;max-width:none}
.tree ul.tb>li{background:var(--soft);border-radius:8px;padding:8px 10px;border-top:3px solid var(--c)}
.tree .tn{font-weight:700;font-size:15px;display:block;line-height:1.3}
.tree ul.tb ul{list-style:none;padding:0;margin-top:5px;display:flex;flex-direction:column;gap:2px;font-size:14px}
.tree ul.tb ul li{padding-left:12px;position:relative;line-height:1.4}
.tree ul.tb ul li::before{content:"";position:absolute;left:0;top:.6em;width:6px;height:1.5px;background:var(--faint)}
.tree .tleaf{font-size:14px;color:var(--muted);margin-top:4px;line-height:1.45}
.scale{display:flex;border-radius:8px;overflow:hidden}
.band{flex:1;padding:8px 10px;text-align:center}
.band .bl{font-weight:700;font-size:15px}.band .br{font-size:14px}
.band.ok{background:var(--okbg);color:var(--ok)}.band.mid{background:var(--cbg);color:var(--c)}.band.bad{background:var(--badbg);color:var(--bad)}.band.n{background:var(--soft)}
.svgd svg{width:100%;height:auto;display:block;max-height:340px}
.svgd text{font-family:var(--font);fill:var(--ink)}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
.tw table{border-collapse:collapse;width:100%;font-size:14.5px;line-height:1.45;min-width:480px}
.tw th,.tw td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
.tw tbody tr:last-child td{border-bottom:0}
.tw th{background:var(--soft);font-weight:700}
.tw td:first-child{font-weight:700}
.tw.plain td:first-child{font-weight:400}
.tw.grid{border:0;background:none}
.tw.grid td.cy,.tw.grid td.cs,.tw.grid td.cn{text-align:center;font-weight:700;font-size:13px}
.tw.grid td.cy{background:var(--okbg);color:var(--ok)}.tw.grid td.cs{background:var(--cbg);color:var(--c)}.tw.grid td.cn{color:var(--faint)}
.tw.grid th:not(:first-child){text-align:center}
.legend5{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;list-style:none;padding:0;margin:0;max-width:none}
.legend5 li{display:flex;gap:8px;align-items:flex-start;font-size:15px;line-height:1.45}
.legend5 .n{flex:none;width:24px;height:24px;border-radius:50%;background:var(--c);color:#fff;font-weight:700;font-size:13px;display:grid;place-items:center;margin-top:1px}
.lesions{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.les{background:var(--soft);border-radius:8px;padding:6px 6px 8px;text-align:center}.les svg{width:100%;height:auto;display:block}
.les .lh{font-weight:700;font-size:15px}.les .ls{font-size:13px;color:var(--muted)}
figure.pic{text-align:center}
figure.pic img{max-width:100%;height:auto;border-radius:8px;border:1px solid var(--line);background:#fff}
details.nn{background:var(--surface);border:1px solid var(--line);border-radius:10px}
details.nn>summary{cursor:pointer;padding:12px 14px;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:10px}
details.nn>summary::-webkit-details-marker{display:none}
details.nn>summary .sub{font-weight:400;font-size:14px;color:var(--faint)}
details.nn>summary::after{content:"Show";font-size:13px;color:var(--c);border:1.5px solid var(--c);border-radius:5px;padding:0 6px;height:fit-content;flex:none}
details.nn[open]>summary::after{content:"Hide"}
.nnbody{padding:0 14px 14px;display:flex;flex-direction:column;gap:14px}
.ncard{border-top:1px solid var(--line);padding-top:10px;display:flex;flex-direction:column;gap:8px;font-size:15.5px}
.ncard h4{margin:0;font-size:16px}.ncard h4 .src{font-weight:400;font-size:12.5px;color:var(--faint);margin-left:6px}
.ncard ul{padding-left:20px;display:flex;flex-direction:column;gap:3px;margin:0}
.ncard li.sub{margin-left:18px;list-style:circle}
.ncard .cap{font-size:13.5px;font-weight:700;color:var(--muted)}
.ncard figure img{max-width:100%;height:auto;border-radius:6px;border:1px solid var(--line);background:#fff}
.ncard figure{text-align:center}.ncard figcaption{font-size:12.5px;color:var(--faint)}
.recall{background:var(--surface);border:1px dashed var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.recall h3{font-size:17px}.recall .hint{font-size:14px;color:var(--muted)}
.qa{border-top:1px solid var(--line);padding-top:8px}
.qa button{font:inherit;font-size:15.5px;text-align:left;width:100%;color:var(--ink);background:none;border:0;padding:0;cursor:pointer;display:flex;gap:10px;align-items:flex-start}
.qa button::before{content:"Show";flex:none;font-size:12px;font-weight:700;color:var(--c);border:1.5px solid var(--c);border-radius:5px;padding:1px 6px;margin-top:3px}
.qa button[aria-expanded="true"]::before{content:"Hide"}
.qa .ans{margin-top:6px;padding:8px 10px;background:var(--cbg);border-radius:6px;font-size:15.5px}
.qa .ans[hidden]{display:none}
body.searching .recall,body.searching .toc,body.searching .plede{display:none}
body.searching .panel{display:flex !important}
.hidden{display:none !important}
@media (max-width:620px){
  body{font-size:16.5px}
  .tabs{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin:0 -16px;padding:0 16px 2px;-webkit-overflow-scrolling:touch}
  .tabs::-webkit-scrollbar{display:none}.tabs button{flex:none}
  .flow:not(.many){flex-direction:column;gap:22px}.flow .step{flex:none}.flow.many{grid-template-columns:1fr 1fr}
  .tw.c2 table,.tw.c3 table{min-width:0}
  .tw.grid table{min-width:0;font-size:12.5px;table-layout:fixed}.tw.grid th,.tw.grid td{padding:5px 3px}.tw.grid th:first-child,.tw.grid td:first-child{width:28%}
  .flow .step:not(:last-child)::after{right:auto;left:50%;top:auto;bottom:-17px;transform:translateX(-50%) rotate(135deg)}
  .cols.n2,.cols.n3,.cols.n4{grid-template-columns:1fr}
  .tw table{min-width:440px}
  .scale{flex-direction:column}
  .lesions{grid-template-columns:1fr 1fr}
}
"""
