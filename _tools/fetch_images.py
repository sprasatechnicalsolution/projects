"""Download images from a GitHub repo into a showcase folder as JPG.

Usage: python _tools/fetch_images.py <owner/repo> <repo-path> <dest-folder> [name ...]
Without names, every png/jpg in <repo-path> is fetched. Needs the gh CLI to be logged in.
"""
import io
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

from PIL import Image

IMG = (".png", ".jpg", ".jpeg")


def gh_token():
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


def api(url, token, raw=False):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.raw" if raw else "application/vnd.github+json",
    })
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def main(repo, path, dest, names):
    token = gh_token()
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    base = f"https://api.github.com/repos/{repo}/contents/{path.strip('/')}".rstrip("/")
    listing = json.loads(api(base, token))
    for item in listing:
        name = item["name"]
        if item["type"] != "file" or not name.lower().endswith(IMG):
            continue
        if names and name not in names:
            continue
        data = api(item["url"].split("?")[0], token, raw=True)
        img = Image.open(io.BytesIO(data))
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
            bg = Image.new("RGB", img.size, "white")
            bg.paste(img, mask=img.split()[-1])
            img = bg
        img = img.convert("RGB")
        if img.width > 2000:
            img = img.resize((2000, round(img.height * 2000 / img.width)), Image.LANCZOS)
        out = dest / (Path(name).stem + ".jpg")
        img.save(out, quality=85, optimize=True)
        print(f"ok  {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], set(sys.argv[4:]))
