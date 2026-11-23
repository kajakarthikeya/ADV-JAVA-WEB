with open('pages/week-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'<div class="ss-actions">[\s\S]*?</div>', text)
if match:
    print(match.group(0))

