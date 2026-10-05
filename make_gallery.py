#!/usr/bin/env python3
"""Regenerate index.html: a gallery of every outputs/YYYY-MM-DD batch, newest first.
Run from the repo root after adding a new weekly folder. No dependencies."""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "outputs")
weeks = sorted([d for d in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, d))], reverse=True)

cards = []
for w in weeks:
    files = sorted(os.listdir(os.path.join(OUT, w)))
    imgs = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png")) and f != "contact_sheet.jpg"]
    vids = [f for f in files if f.lower().endswith(".mp4")]
    items = []
    for f in imgs:
        p = f"outputs/{w}/{f}"
        items.append(f'<a class="card" href="{p}" download><img loading="lazy" src="{p}"><span>{html.escape(f)}</span></a>')
    for f in vids:
        p = f"outputs/{w}/{f}"
        items.append(f'<div class="card"><video controls preload="metadata" src="{p}"></video>'
                     f'<a href="{p}" download><span>{html.escape(f)} (download)</span></a></div>')
    cards.append(f'<section><h2>{w}</h2><div class="grid">{"".join(items)}</div></section>')

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>DLBLP - Weekly Ad Creatives</title>
<style>
  body {{ margin:0; font-family: Georgia, serif; background:#faf6ef; color:#30261e; }}
  header {{ padding:36px 20px 10px; text-align:center; }}
  header h1 {{ margin:0; font-size:clamp(22px,4vw,34px); }}
  header p {{ color:#8a7a64; margin:8px 0 0; }}
  section {{ max-width:1200px; margin:0 auto; padding:18px 16px; }}
  h2 {{ border-bottom:2px solid #e3d8c4; padding-bottom:8px; color:#3d5444; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(210px,1fr)); gap:14px; }}
  .card {{ background:#fff; border:1px solid #e8dfd0; border-radius:10px; overflow:hidden;
           text-decoration:none; color:#30261e; display:block; }}
  .card img, .card video {{ width:100%; display:block; aspect-ratio:4/5; object-fit:cover; background:#eee; }}
  .card video {{ aspect-ratio:9/16; }}
  .card span {{ display:block; font-size:12px; padding:8px 10px; font-family:Helvetica,Arial,sans-serif; }}
  footer {{ text-align:center; color:#a5947c; padding:30px; font-size:13px; }}
</style></head><body>
<header><h1>De la Bobiță la Pepene - Weekly Ad Creatives</h1>
<p>Click any image to download the full-resolution file. New batch every Sunday.</p></header>
{"".join(cards)}
<footer>delabobitalapepene.ro - internal creative drop</footer>
</body></html>"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page)
print(f"gallery ok - {len(weeks)} week(s)")
