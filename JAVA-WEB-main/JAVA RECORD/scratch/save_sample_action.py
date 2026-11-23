with open('pages/week-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="ss-actions">[\s\S]*?</div>', text)
with open('scratch/sample_ss_action.txt', 'w', encoding='utf-8') as fp:
    if matches:
        fp.write(f"Total matches: {len(matches)}\n")
        fp.write(matches[0])

