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

## 4. Deploy  — DONE
Live at <https://dmv.pages.dev> (Cloudflare Pages project `dmv`, connected to
`divija027/portfolio`, no build command, output `/`). Pushes to `main` redeploy.
Lighthouse 100 across accessibility, best practices, SEO and agentic browsing.

An earlier Worker at `portfolio.gowdadivija.workers.dev` is redundant and can be
deleted — Workers Custom Domains require the zone to be in your own Cloudflare
account, so a Worker can never serve `dmv.is-a.dev`.

## 5. Domain  — PR OPEN, one step left
is-a.dev PR: <https://github.com/is-a-dev/register/pull/50154> (all CI green).

**Still to do — attach the custom domain.** The Pages dashboard refuses
`dmv.is-a.dev` because is-a.dev is on the Public Suffix List, so use the API
with a token that has **Pages Write**:

```bash
export CF_ACCOUNT_ID=0880c9b1488acd73ee21d22224693618 CF_TOKEN=your_pages_write_token
curl -sS "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/pages/projects/dmv/domains" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  -d '{"name":"dmv.is-a.dev"}'
```

`pending` is the expected result until the PR merges. Then verify:

```bash
dig +short dmv.is-a.dev CNAME && curl -sSI https://dmv.is-a.dev | head -1
```

## 6. Later
Swap the Reddit copies for the phone originals (AirDrop from the iPhone 13 Pro
Max) — same filenames, better quality, EXIF dates intact.

## 7. Blog — deployed, two manual steps left

The EmDash blog is deployed and reachable:

- Worker (D1 + R2 + KV + cron): <https://dmv-blog.gowdadivija.workers.dev>
- Edge proxy: <https://dmv-blog-edge.pages.dev>

`blog.dmv.is-a.dev` is attached to the `dmv-blog-edge` Pages project as a
custom domain and is waiting for its CNAME record. The record is prepared in
`deploy/blog.dmv.json`; submit it to `is-a-dev/register` as
`domains/blog.dmv.json`. **Do this yourself** — is-a.dev rejects AI-generated
pull requests and requires the site owner to submit the change.

Once DNS is live, finish the EmDash setup at
<https://blog.dmv.is-a.dev/_emdash/admin/setup> (passkey). Completing setup
applies the bundled seed (2 collections, 9 posts, 1 page). Until then the blog
renders an empty state.

The portfolio nav no longer links to the blog (commit `57baadd`). Re-add the
link only after the custom domain resolves; `blog.dmv.is-a.dev` is the URL to
use.

Deploy notes for the edge proxy are in `blog/edge/README.md`.
