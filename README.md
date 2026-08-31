# dmv.is-a.dev

Personal site for Divija MV. One static HTML file, no framework, no build step,
no dependencies. Cloudflare Pages serves this directory as-is.

Adapted from Meng To's MIT-licensed **Sketchbook** landing page
([MengTo/threeui](https://github.com/MengTo/threeui)). See `LICENSE`.

```
index.html          the entire site: markup + inline <style> + inline <script>
plates.json         single source of truth for the 18 sketchbook plates
build.py            syncs plates.json -> the PAGES array in index.html
divija-mv.pdf       resume, served at /divija-mv.pdf
assets/             fonts, paper/botanical art, og image
assets/plates/      SOURCE photographs (compositor input; not served to visitors)
assets/spreads/     COMPOSED book spreads (what the site actually shows)
deploy/dmv.json     the is-a.dev record to submit (see Domain below)
writing/            reserved; blog posts land here as plain .html
```

## Local preview

```bash
python3 -m http.server 4173
```

Then open <http://localhost:4173>. There is nothing to install or compile.

## How the sketchbook works

The template's page-turn engine treats each plate as **one image of a whole open
book** and slices it as CSS backgrounds for the halves and the 18-strip curl.
So the notes on the right-hand page are *rendered into* the spread image rather
than being live DOM text.

That is why `assets/spreads/NN.jpg` exists: each is a 1760x1100 composite of
paper + the photograph on the left page + the notes on the right page.

The note text is still on the page as real, selectable, indexable text — the
Plates index below the book carries every note, and on small screens (where the
book is too small to read) that index is the primary way to read them.

## Rebuilding

**After editing text only** (titles, places, notes in `plates.json`):

1. `python3 build.py` — updates the plate list in `index.html`
2. Re-compose the spreads (below), because the notes are baked into the images

**Re-composing the spreads** needs a browser, since the compositor is a web page:

1. Serve the directory (`python3 -m http.server 4173`)
2. Open `.work/compose.html`, which stacks six spreads at a time
3. Screenshot full-page, then crop each 2668x1668 tile and scale to 1760x1100:
   ```bash
   ffmpeg -i sheet.png -vf "crop=2668:1668:0:$((k*1668)),scale=1760:1100" -q:v 4 assets/spreads/NN.jpg
   ```

**Replacing a photograph**: drop the new file over `assets/plates/NN.jpg`
(keep the filename), re-compose that spread. No code change.

## Deploy

Cloudflare Pages, connected to this repo. **No build command; output directory `/`.**
Every push to `main` deploys.

## Domain

`dmv.is-a.dev`, free, via a pull request to
[is-a-dev/register](https://github.com/is-a-dev/register).

1. Put the Pages subdomain into `deploy/dmv.json` (replace the placeholder)
2. Fork the register repo, add the file as `domains/dmv.json`, open the PR
   **yourself** — their README says AI-generated pull requests get closed and
   the author blocked
3. `is-a.dev` is on the Public Suffix List, so the custom domain **cannot** be
   added from the Pages dashboard. Use the Cloudflare API, or the GUI helper
   linked from <https://docs.is-a.dev/guides/cloudflare-pages/>

## Writing

The nav slot is reserved. Posts are hand-written HTML at `writing/<slug>.html`,
reusing the paper styling, and listed in the `#writing` index. When that gets
tedious (roughly the fifth post), move to a generator — the HTML files can be
regenerated from markdown without changing anything else.
