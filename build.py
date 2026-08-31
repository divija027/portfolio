#!/usr/bin/env python3
"""Sync plates.json -> the PAGES array inside index.html.

The site itself needs no build: index.html is static and is what Pages serves.
This only regenerates the inlined plate list after you edit plates.json, so
there is exactly one source of truth for titles, places and notes.

    python3 build.py

NOTE: the notes are ALSO rendered into the spread images, so after editing
plates.json you must re-compose the spreads too - see README, "Rebuilding".
"""
import io, json, re, sys, pathlib

root = pathlib.Path(__file__).parent
data = json.loads((root / 'plates.json').read_text(encoding='utf-8'))
plates = data['plates']

rows = ',\n'.join(
    '  {file:%s, title:%s, place:%s, note:%s}' % (
        json.dumps(p['file'].replace('.jpg', '.jpg')), json.dumps(p['title']),
        json.dumps(p['place']), json.dumps(p['note']))
    for p in plates)
block = '/*PLATES:START*/\nconst PAGES=[\n%s\n];\n/*PLATES:END*/' % rows

html = (root / 'index.html').read_text(encoding='utf-8')
new, n = re.subn(r'/\*PLATES:START\*/.*?/\*PLATES:END\*/', lambda m: block, html, flags=re.S)
if n != 1:
    sys.exit('could not find exactly one PLATES block in index.html (found %d)' % n)

missing = [p['file'] for p in plates if not (root / 'assets' / 'spreads' / p['file']).exists()]
if missing:
    print('warning: no composed spread for: %s' % ', '.join(missing))

if new == html:
    print('index.html already up to date (%d plates)' % len(plates))
else:
    (root / 'index.html').write_text(new, encoding='utf-8')
    print('index.html updated with %d plates' % len(plates))
