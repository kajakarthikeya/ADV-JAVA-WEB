import re

with open('scratch/button_search.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
for l in lines:
    safe = l.strip().encode('ascii', errors='replace').decode('ascii')
    out.append(safe)

with open('scratch/button_summary_ascii.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out[:100]))

print("Wrote summary ascii")
