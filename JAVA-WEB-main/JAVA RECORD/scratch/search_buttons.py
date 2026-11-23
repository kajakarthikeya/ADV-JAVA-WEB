import os
import re

patterns = ['fullscreen', 'full screen', 'download', 'ss-download', 'ss-replace', 'step-btn', 'ss-btn']

results = []
for fname in ['index.html', 'style.css', 'script.js', 'build_perfect_record.py', 'build_sidebar_helpers.py']:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            l_lower = line.lower()
            for p in patterns:
                if p in l_lower and any(b in l_lower for b in ['btn', 'button', 'modal', 'img', 'photo', 'screen', 'zoom']):
                    results.append(f'{fname}:{idx+1}: {line.strip()[:120]}')

with open('scratch/button_search.txt', 'w', encoding='utf-8') as out:
    for r in results:
        out.write(r + '\n')

print(f'Total search results: {len(results)}')

