import markdown, re, sys, pathlib
d = pathlib.Path(sys.argv[1])
CSS = """
@page{size:A4;margin:22mm 20mm 20mm 20mm}
*{box-sizing:border-box}
body{font-family:Inter,sans-serif;color:#111;font-size:11pt;line-height:1.55;margin:0}
h1{font-family:'Inter Display',Inter;font-size:27pt;font-weight:700;letter-spacing:-.02em;line-height:1.1;margin:0 0 6px}
.by{color:#777;font-size:10pt;margin:0 0 26px}
h2{font-family:'Inter Display',Inter;font-size:19pt;font-weight:700;letter-spacing:-.015em;margin:0 0 14px;padding-bottom:10px;border-bottom:2px solid #111;break-before:page;break-after:avoid}
h2:first-of-type{break-before:auto}
h3{font-size:12.5pt;font-weight:700;margin:22px 0 8px;break-after:avoid}
p{margin:0 0 10px}
table{width:100%;border-collapse:collapse;margin:8px 0 16px;font-size:9.8pt;break-inside:avoid}
th{text-align:left;background:#111;color:#fff;font-weight:600;padding:7px 9px}
td{padding:7px 9px;border-bottom:1px solid #ddd;vertical-align:top}
tr{break-inside:avoid}
td:first-child{font-weight:600}
ol,ul{margin:0 0 12px;padding-left:22px}
li{margin:0 0 7px;break-inside:avoid}
ul.q{list-style:none;padding-left:0}
ul.q li{display:grid;grid-template-columns:20px 1fr;margin:0 0 4px}
ul.q li .box{font-size:13pt;line-height:1.2}
ul.q li .ans{grid-column:2;border-bottom:1px dotted #999;height:24px;margin-bottom:6px}
a{color:#111}
strong{font-weight:700}
"""
EXTRA={"dossier":"ul.q li .ans{display:none}ul.q li{margin:0 0 6px}pre{background:#f3f3f3;border:1px solid #ddd;border-radius:8px;padding:12px 14px;white-space:pre-wrap;font-size:9pt;line-height:1.45;break-inside:auto}code{font-family:Menlo,monospace;font-size:9pt}h2{break-before:auto;margin-top:26px}","informativa":"body{font-size:10pt;line-height:1.42}h1{font-size:22pt}h3{margin:14px 0 6px}p{margin:0 0 7px}li{margin:0 0 4px}table{margin:6px 0 10px}td,th{padding:5px 8px}"}
for name in (sys.argv[2:] or ["spiegazione", "domande", "informativa"]):
    src = (d / f"{name}.md").read_text()
    html = markdown.markdown(src, extensions=["tables", "fenced_code"])
    # checklist items -> box + answer line
    def fix_ul(m):
        inner = m.group(1)
        if "[ ]" not in inner: return m.group(0)
        inner = re.sub(r"<li>\[ \] (.*?)</li>", r'<li><span class="box">☐</span><span>\1</span><span class="ans"></span></li>', inner, flags=re.S)
        return f'<ul class="q">{inner}</ul>'
    html = re.sub(r"<ul>(.*?)</ul>", fix_ul, html, flags=re.S)
    title = re.search(r"<h1>(.*?)</h1>", html).group(1)
    (d / f"{name}.html").write_text(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}{EXTRA.get(name,"")}</style></head><body>{html}</body></html>')
print("ok")
