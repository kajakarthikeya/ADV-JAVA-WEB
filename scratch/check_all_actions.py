import re

out = []
for fname in ['build_perfect_record.py', 'build_sidebar_helpers.py', 'style.css', 'script.js']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = []
    for i, line in enumerate(text.splitlines()):
        if any(k in line for k in ['step-card-actions', 'step-btn', 'ss-zoom-trigger', 'ss-download-btn', 'ss-replace-btn', 'Download Full-Res', 'Fullscreen screenshot', 'id="downloads"', 'downloads']):
            matches.append((i+1, line.strip()))
    
    out.append(f'=== {fname} ({len(matches)} matches) ===')
    for m in matches:
        out.append(f'  {m[0]}: {m[1]}')

with open('scratch/actions_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Wrote actions_result.txt")
