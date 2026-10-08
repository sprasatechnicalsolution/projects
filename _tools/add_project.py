"""Add a new project to the portfolio, or publish changes to an existing one.

Usage:
  python _tools/add_project.py new <folder-name>          Create the folder with a README and project.json to fill in
  python _tools/add_project.py publish <folder-name>      Check, make the cover, list it in README.md, commit and push
  python _tools/add_project.py publish <folder-name> --no-push
  python _tools/add_project.py sections                   Show the section keys for "section" in project.json

Pushes go to github.com/sprasatechnicalsolution/projects as the sprasatechnicalsolution account;
the active gh account is switched back afterwards. Commits use the local git author.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PUSH_ACCOUNT = "sprasatechnicalsolution"
MAX_SHOT_BYTES = 600_000

# key -> heading in README.md
SECTIONS = {
    "client": "Client projects: business, booking and e-commerce",
    "software": "Business software and products",
    "education": "Education",
    "media": "News and media",
    "design": "Design and marketing",
    "websites": "Company and personal websites",
    "open-source": "Open-source tools",
    "engineering": "Engineering and research",
}

README_TEMPLATE = """# {name}

**TODO one-line description of what was built and for whom**

![{name} overview](overview.jpg)

| | |
|---|---|
| **Client** | TODO client name, what they do, town |
| **Type** | TODO e.g. Website + booking system |
| **Year** | {year} |
| **Status** | TODO e.g. Live / Complete / In development |
| **Platform** | TODO e.g. Web (desktop and mobile) |

## The client's problem

TODO two or three sentences: how they worked before and what was going wrong.

## What we built

TODO one sentence on the overall solution.

### TODO first feature
TODO what it does for the client, in plain words.

![TODO](screenshots/01-home.jpg)

### TODO next features, two screenshots side by side
TODO description.

| TODO | TODO |
|---|---|
| ![TODO](screenshots/02-TODO.jpg) | ![TODO](screenshots/03-TODO.jpg) |

## Technology

TODO e.g. Laravel, MySQL, Tailwind CSS, eSewa

---

**Built by Pradip Subedi · Sprasa Technical Solution**
Need something similar? [Get in touch](../README.md#contact).
"""


def project_json_template(name, year):
    return {
        "name": name,
        "tagline": "TODO one or two sentences for the cover image",
        "summary": "TODO short line for the project list in README.md",
        "section": "TODO one of: " + ", ".join(SECTIONS),
        "source": "TODO local htdocs folder / GitHub repo it came from",
        "category": "TODO e.g. Website + Booking",
        "client": "TODO",
        "year": year,
        "status": "TODO",
        "stack": ["TODO"],
        "highlights": ["TODO up to five short feature lines"],
        "shot": "screenshots/01-home.jpg",
        "accent": "#0f766e",
    }


def run(*cmd, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"failed: {' '.join(cmd)}\n{r.stdout}{r.stderr}")
    return r


def new(slug):
    folder = ROOT / slug
    if folder.exists():
        sys.exit(f"{slug}/ already exists. Edit it, then run: publish {slug}")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        sys.exit("Use a lowercase folder name with dashes, e.g. hotel-booking-site")
    name = slug.replace("-", " ").title()
    year = str(__import__("datetime").date.today().year)
    (folder / "screenshots").mkdir(parents=True)
    (folder / "README.md").write_text(README_TEMPLATE.format(name=name, year=year), encoding="utf-8")
    (folder / "project.json").write_text(
        json.dumps(project_json_template(name, year), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Created {slug}/ with README.md, project.json and screenshots/\n"
          f"1. Put screenshots in {slug}/screenshots/ (01-home.jpg, 02-....jpg)\n"
          f"2. Replace every TODO in README.md and project.json\n"
          f"3. python _tools/add_project.py publish {slug}")


def check(folder, meta):
    problems = []
    for f in ("README.md", "project.json"):
        if "TODO" in (folder / f).read_text(encoding="utf-8"):
            problems.append(f"{f} still has TODO placeholders")
    readme = (folder / "README.md").read_text(encoding="utf-8")
    for ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)|<img src=\"([^\"]+)\"", readme):
        ref = ref[0] or ref[1]
        if ref != "overview.jpg" and not ref.startswith("http") and not (folder / ref).exists():
            problems.append(f"README.md shows {ref}, which does not exist")
    shot = meta.get("shot")
    if shot and not (folder / shot).exists():
        problems.append(f'project.json "shot" points to {shot}, which does not exist')
    for k in ("name", "tagline", "category", "year", "status"):
        if not meta.get(k):
            problems.append(f'project.json needs "{k}"')
    return problems


def shrink_screenshots(folder):
    """Convert PNGs to JPG and recompress large images, so the repo stays light."""
    shots = folder / "screenshots"
    if not shots.is_dir():
        return
    for p in sorted(shots.iterdir()):
        if p.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        if p.suffix.lower() == ".jpg" and p.stat().st_size <= MAX_SHOT_BYTES:
            continue
        im = Image.open(p).convert("RGB")
        if im.width > 1600:
            im = im.resize((1600, round(im.height * 1600 / im.width)))
        out = p.with_suffix(".jpg")
        im.save(out, quality=82, optimize=True)
        if out != p:
            p.unlink()
            for f in ("README.md", "project.json"):
                doc = folder / f
                doc.write_text(doc.read_text(encoding="utf-8").replace(
                    f"screenshots/{p.name}", f"screenshots/{out.name}"), encoding="utf-8")
            print(f"converted {p.name} -> {out.name}")
        else:
            print(f"compressed {p.name}")


def list_row(slug, meta):
    return (f'| <img src="{slug}/overview.jpg" width="160"> | [{meta["name"]}]({slug}/) '
            f'| {meta["summary"]} |')


def update_index(slug, meta):
    path = ROOT / "README.md"
    lines = path.read_text(encoding="utf-8").split("\n")
    existing = next((i for i, l in enumerate(lines) if f"]({slug}/)" in l and l.startswith("| <img")), None)
    summary = meta.get("summary", "")
    if existing is not None:
        if summary:
            lines[existing] = list_row(slug, meta)
    else:
        heading = SECTIONS.get(meta.get("section", ""))
        if not heading:
            sys.exit(f'project.json "section" must be one of: {", ".join(SECTIONS)}')
        if not summary:
            sys.exit('project.json needs "summary" (the short line shown in the project list)')
        start = lines.index(f"### {heading}")
        i = start + 1
        while not lines[i].startswith("|"):
            i += 1
        while i < len(lines) and lines[i].startswith("|"):
            i += 1
        lines.insert(i, list_row(slug, meta))

    source = meta.get("source")
    if source and not any(l.strip().startswith(f"{slug} ") for l in lines):
        notes_end = next(i for i, l in enumerate(lines) if l.startswith("- Not showcased:"))
        lines.insert(notes_end, f"  {slug:<33} <- {source}")
    path.write_text("\n".join(lines), encoding="utf-8")


def active_gh_account():
    out = run("gh", "auth", "status", check=False)
    text = out.stdout + out.stderr
    for m in re.finditer(r"account (\S+).*?Active account: (true|false)", text, re.S):
        if m.group(2) == "true":
            return m.group(1)
    return None


def push():
    before = active_gh_account()
    if before != PUSH_ACCOUNT:
        run("gh", "auth", "switch", "-u", PUSH_ACCOUNT)
    try:
        r = run("git", "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
                "push", "origin", "main", check=False)
        print((r.stdout + r.stderr).strip())
        if r.returncode:
            sys.exit("push failed; the commit is saved locally, run publish again to retry")
    finally:
        if before and before != PUSH_ACCOUNT:
            run("gh", "auth", "switch", "-u", before)


def publish(slug, do_push=True):
    folder = ROOT / slug
    if not (folder / "project.json").exists():
        sys.exit(f"{slug}/project.json not found. Start with: new {slug}")
    meta = json.loads((folder / "project.json").read_text(encoding="utf-8"))
    problems = check(folder, meta)
    if problems:
        sys.exit("Fix these first:\n- " + "\n- ".join(problems))

    shrink_screenshots(folder)
    meta = json.loads((folder / "project.json").read_text(encoding="utf-8"))
    run(sys.executable, str(ROOT / "_tools" / "make_cover.py"), str(folder))
    print(f"ok  {slug}/overview.jpg")
    update_index(slug, meta)

    is_new = not run("git", "ls-files", f"{slug}/README.md").stdout.strip()
    run("git", "add", "--", slug, "README.md")
    if not run("git", "diff", "--cached", "--quiet", check=False).returncode:
        print("Nothing changed since the last publish.")
    else:
        run("git", "commit", "-m", f"{'Add' if is_new else 'Update'} {meta['name']}")
        print(run("git", "log", "--oneline", "-1").stdout.strip())
    if do_push:
        push()
        print(f"Live at https://github.com/{PUSH_ACCOUNT}/projects/tree/main/{slug}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["new"] and len(a) == 2:
        new(a[1])
    elif a[:1] == ["publish"] and len(a) in (2, 3):
        publish(a[1], do_push="--no-push" not in a)
    elif a == ["sections"]:
        for k, v in SECTIONS.items():
            print(f"{k:<12} {v}")
    else:
        sys.exit(__doc__)
