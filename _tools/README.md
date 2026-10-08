# Adding a project to the portfolio

Three steps. Run them from `C:\xampp\htdocs\projects`.

## 1. Create the folder

```
python _tools/add_project.py new hotel-booking-site
```

Use a short lowercase name with dashes. This creates:

```
hotel-booking-site/
  README.md        page clients read, with TODO markers to replace
  project.json     data for the cover image and the project list
  screenshots/     put your images here
```

## 2. Fill it in

**Screenshots:** put them in `screenshots/` named in order: `01-home.jpg`, `02-booking.jpg` and so on. PNG is fine; it is converted to JPG automatically and large images are compressed.

To capture a running site automatically, use `node _tools/shoot.js jobs.json` (see the top of `shoot.js` for the format).

**README.md:** replace every `TODO`. Keep the same order as the other projects:
title and one-line description → facts table → the client's problem → what we built (one heading and screenshot per feature) → technology.

**project.json:**

| Field | What to write |
|---|---|
| `name` | Project name |
| `tagline` | One or two sentences, shown on the cover |
| `summary` | Short line shown in the main project list |
| `section` | Where it is listed: `client`, `software`, `education`, `media`, `design`, `websites`, `open-source` or `engineering` |
| `source` | Local htdocs folder / GitHub repo it came from (kept in hidden notes, not shown to clients) |
| `category`, `client`, `year`, `status` | Shown on the cover |
| `stack` | Technologies, shown as chips on the cover |
| `highlights` | Up to five short feature lines for the cover |
| `shot` | Screenshot shown on the right of the cover (remove the line for a text-only cover) |
| `accent` | Cover colour, e.g. `#0f766e` |

## 3. Publish

```
python _tools/add_project.py publish hotel-booking-site
```

This will:

1. Stop and list anything missing (leftover TODOs, missing screenshots)
2. Compress screenshots and make `overview.jpg`
3. Add the project to the right section of the main `README.md`
4. Commit, and push to GitHub as **sprasatechnicalsolution** (your normal gh account is switched back afterwards)

Add `--no-push` to commit without pushing.

Changed an existing project? Edit its files and run `publish` again. It updates the cover and the list row, then commits it as "Update ...".

## Other tools

| Command | Does |
|---|---|
| `python _tools/make_cover.py --all` | Rebuild every cover image |
| `python _tools/fetch_images.py <owner/repo> <path> <dest>` | Download images from a GitHub repo as JPG |
| `node _tools/shoot.js jobs.json` | Screenshot running sites with Playwright |
| `python _tools/add_project.py sections` | List the section keys |
