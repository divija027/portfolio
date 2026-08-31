# What's left for you

## 0. Provenance
_(Confirmed: `r/SoloTravel_India` post `1lsvcyl`,
u/insane_dark_07, is Divija's own account.)_

## 1. Convert the 18 photos to ink-and-watercolour
Nothing on this Mac can do this (no ImageMagick, Pillow, torch, or image API
key), and no filter chain reproduces Meng To's plates anyway — they're clean
ink linework over watercolour wash.

Run each of `assets/plates/01.jpg` … `18.jpg` through an AI image tool
(ChatGPT, Gemini, Krea, Photoshop neural filters). Prompt:

> Redraw this photograph as a loose ink-and-watercolour sketchbook plate.
> Fine dark ink linework for the structure, soft transparent watercolour
> washes for tone, muted palette, generous untouched white paper, visible
> paper grain, edges fading out rather than filling the frame. Keep the
> composition and subject exactly. No text, no border, no signature.

Reference to match: <https://threeui.com/landing-pages/meng-to-sketchbook/marina-bay-sands.png>

Save each result **over the same filename** in `assets/plates/`, then re-compose
the spreads (README → Rebuilding). Filenames are stable, so nothing else changes.

Once they're converted, soften or drop the interim treatment — the site
currently presents raw photographs as pasted-in prints, which is deliberate but
temporary.

## 3. Correct the plate notes
`plates.json` has all 18 titles, places, days and altitudes. **I inferred them**
from the Reddit post and your comments — the day-to-photo mapping is guesswork.
Fix it, then `python3 build.py` and re-compose.

## 4. Push and deploy
Nothing is on GitHub yet; I committed locally only, because publishing is yours
to trigger — especially given the Fuleex security findings are on the page
verbatim, as you decided.

```bash
cd ~/adigaproj/dmv-portfolio
gh repo create divija027/portfolio --public --source=. --remote=origin --push
```

Then: Cloudflare Pages → connect the repo → **no build command, output `/`**.

## 5. Claim the domain
Put your `*.pages.dev` subdomain into `deploy/dmv.json`, then fork
`is-a-dev/register`, add it as `domains/dmv.json`, and open the PR **yourself**.
Their README closes AI-generated PRs and blocks the author.

`is-a.dev` is on the Public Suffix List, so the Pages dashboard cannot add the
custom domain — use the Cloudflare API or the helper linked from
<https://docs.is-a.dev/guides/cloudflare-pages/>.

## 6. Later
Swap the Reddit copies for the phone originals (AirDrop from the iPhone 13 Pro
Max) — same filenames, better quality, EXIF dates intact.
