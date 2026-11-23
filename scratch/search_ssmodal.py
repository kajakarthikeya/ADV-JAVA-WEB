import os
import re

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.js') or f.endswith('.html') or f.endswith('.py'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'ssModal' in c:
                    matches.append((p, [line.strip() for line in c.splitlines() if 'ssModal' in line]))

with open('scratch/ssmodal_matches.txt', 'w', encoding='utf-8') as out:
    for path, lines in matches:
        out.write(f'=== {path} ===\n')
        for l in lines[:10]:
            out.write(f'  {l}\n')

print(f'Done searching, found {len(matches)} files')

