with open('scratch/w0_body_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<h[234][^>]*>.*?</h[234]>|<div class="timeline-step">.*?</div>\s*</div>', text, re.DOTALL)
print(f'Found {len(matches)} matches')
for m in matches[:15]:
    first_line = m.strip().splitlines()[0][:100]
    print(" ", first_line)
