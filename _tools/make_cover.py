"""Render a project's overview.jpg cover from its project.json.

Usage:  python _tools/make_cover.py <project-folder> [<project-folder> ...]
        python _tools/make_cover.py --all

project.json fields:
  name, tagline, category, client, year, status, stack[], highlights[],
  shot (optional: image path relative to the project folder, shown on the right),
  fit (optional: "cover" (default) or "contain" for logos and wide banners),
  accent (optional hex colour)
"""
import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]
W, H = 1600, 900


def chrome():
    for p in CHROME_PATHS:
        if Path(p).exists():
            return p
    sys.exit("Chrome or Edge not found")


def build_html(meta, folder):
    e = html.escape
    accent = meta.get("accent", "#0f766e")
    chips = "".join(f"<span class=chip>{e(s)}</span>" for s in meta.get("stack", []))
    items = "".join(f"<li>{e(h)}</li>" for h in meta.get("highlights", [])[:5])
    facts = [x for x in (meta.get("category"), meta.get("year"), meta.get("status")) if x]
    shot = meta.get("shot")
    right = ""
    if shot and (folder / shot).exists():
        fit = meta.get("fit", "cover")
        style = f"object-fit:{fit}" + (";object-position:center;background:#e9eaee" if fit == "contain" else "")
        right = (f'<div class=shot><img style="{style}" '
                 f'src="{(folder / shot).resolve().as_uri()}"></div>')
    width_left = "760px" if right else "1360px"
    return f"""<!doctype html><meta charset=utf-8><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:'Segoe UI',Arial,sans-serif;
 background:radial-gradient(circle at 85% 15%, {accent}33, transparent 45%),linear-gradient(135deg,#0b1220,#111c2e);color:#e8edf5}}
.wrap{{display:flex;gap:56px;padding:80px 90px;height:100%;align-items:center}}
.left{{width:{width_left};display:flex;flex-direction:column;gap:26px}}
.facts{{font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:{accent};filter:brightness(1.6);font-weight:600}}
h1{{font-size:68px;line-height:1.05;font-weight:700;color:#fff}}
.tag{{font-size:27px;line-height:1.4;color:#b7c2d4}}
ul{{list-style:none;display:flex;flex-direction:column;gap:12px;font-size:22px;color:#d6deea}}
li::before{{content:'';display:inline-block;width:10px;height:10px;border-radius:50%;background:{accent};filter:brightness(1.6);margin-right:14px;vertical-align:middle}}
.chips{{display:flex;flex-wrap:wrap;gap:10px}}
.chip{{font-size:18px;padding:7px 14px;border-radius:999px;border:1px solid #ffffff2a;background:#ffffff0f;color:#e8edf5}}
.shot{{flex:1;height:640px;border-radius:18px;overflow:hidden;box-shadow:0 30px 80px #0009;border:1px solid #ffffff22;background:#fff}}
.shot img{{width:100%;height:100%;object-fit:cover;object-position:left top}}
.brand{{position:absolute;bottom:34px;left:90px;font-size:17px;color:#7d8aa0;letter-spacing:.06em}}
</style><div class=wrap><div class=left>
<div class=facts>{' &middot; '.join(e(f) for f in facts)}</div>
<h1>{e(meta['name'])}</h1><p class=tag>{e(meta.get('tagline',''))}</p>
<ul>{items}</ul><div class=chips>{chips}</div></div>{right}</div>
<div class=brand>Built by Pradip Subedi &middot; Sprasa Technical Solution</div>"""


def render(folder: Path):
    meta = json.loads((folder / "project.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "cover.html"
        png = Path(tmp) / "cover.png"
        page.write_text(build_html(meta, folder), encoding="utf-8")
        subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", f"--window-size={W},{H}",
                        f"--user-data-dir={Path(tmp) / 'profile'}",
                        f"--screenshot={png}", page.as_uri()],
                       check=True, capture_output=True, timeout=60)
        Image.open(png).convert("RGB").save(folder / "overview.jpg", quality=88, optimize=True)
    print(f"ok  {folder.name}/overview.jpg")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--all"]:
        targets = sorted(p.parent for p in ROOT.glob("*/project.json"))
    else:
        targets = [Path(a).resolve() for a in args]
    for t in targets:
        render(t)
