#!/usr/bin/env python3
"""Regenerate everything that is derived from plates.json.

The site itself needs no build: index.html is static and is what Pages serves.
This only propagates plates.json into the two places that inline it, so there
is exactly one source of truth for titles, places and notes.

    python3 build.py

  index.html          -> the PAGES array the sketchbook renders from
  tools/compose.html  -> the data the spread compositor renders from

The notes are ALSO rendered into the spread images, so after running this you
must re-compose the spreads. See README, "Rebuilding".
"""
import json, re, sys, pathlib

root = pathlib.Path(__file__).parent
data = json.loads((root / 'plates.json').read_text(encoding='utf-8'))
plates, trek = data['plates'], data['trek']
changed = []

# ---- index.html: the PAGES array -------------------------------------------
rows = ',\n'.join(
    '  {file:%s, title:%s, place:%s, note:%s}' % (
        json.dumps(p['file']), json.dumps(p['title']),
        json.dumps(p['place']), json.dumps(p['note']))
    for p in plates)
block = '/*PLATES:START*/\nconst PAGES=[\n%s\n];\n/*PLATES:END*/' % rows

f = root / 'index.html'
html = f.read_text(encoding='utf-8')
new, n = re.subn(r'/\*PLATES:START\*/.*?/\*PLATES:END\*/', lambda m: block, html, flags=re.S)
if n != 1:
    sys.exit('index.html: expected exactly one PLATES block, found %d' % n)
if new != html:
    f.write_text(new, encoding='utf-8'); changed.append('index.html')

# ---- tools/compose.html: the compositor's input ------------------------------
items = [dict(p, i=i) for i, p in enumerate(plates)]
script = ('<script>window.PLATES=%s;window.TREK=%s;</script>'
          % (json.dumps(items, ensure_ascii=False), json.dumps(trek, ensure_ascii=False)))

f = root / 'tools' / 'compose.html'
comp = f.read_text(encoding='utf-8')
new, n = re.subn(r'<!--PLATEDATA-->|<script>window\.PLATES=.*?</script>',
                 lambda m: script, comp, count=1, flags=re.S)
if n != 1:
    sys.exit('tools/compose.html: could not find the plate-data slot')
if new != comp:
    f.write_text(new, encoding='utf-8'); changed.append('tools/compose.html')

# ---- warn about plates with no composed spread yet ---------------------------
missing = [p['file'] for p in plates
           if not (root / 'assets' / 'spreads' / p['file']).exists()]
if missing:
    print('warning: no composed spread for: %s' % ', '.join(missing))

print('%d plates -> %s' % (len(plates), ', '.join(changed) if changed else 'already up to date'))
