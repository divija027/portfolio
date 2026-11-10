# Blog edge proxy

Cloudflare Pages project that forwards every request to the `dmv-blog` Worker
through a service binding.

## Why this exists

`blog.dmv.is-a.dev` has to be attached as a **Pages custom domain**, because the
`is-a.dev` DNS zone is not in this Cloudflare account. Workers Custom Domains
require the zone to be in the account, but Pages accepts an external CNAME. The
proxy keeps the blog on one hostname while the Worker keeps its D1, R2, KV and
cron bindings.

The custom domain `blog.dmv.is-a.dev` is already registered on the Pages project
and is waiting for its CNAME record. See `deploy/blog.dmv.json`.

## Deploy

```bash
cd blog/edge
./deploy.sh
```

The script copies the Worker and its config to a temporary directory before
deploying, because Wrangler otherwise picks up the parent `blog/wrangler.jsonc`.
