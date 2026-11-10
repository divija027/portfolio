#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
BLOG_DIR="$(cd .. && pwd)"
WRANGLER="$BLOG_DIR/node_modules/.bin/wrangler"

if [[ ! -x "$WRANGLER" ]]; then
	echo "wrangler not found at $WRANGLER; run pnpm install in blog/" >&2
	exit 1
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cp _worker.js wrangler.toml "$TMP/"

cd "$TMP"
CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-0880c9b1488acd73ee21d22224693618}" \
	"$WRANGLER" pages deploy . --project-name dmv-blog-edge --commit-dirty --branch main "$@"
