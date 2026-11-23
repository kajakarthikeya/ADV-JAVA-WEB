import re

with open('pages/week-7.html', 'r', encoding='utf-8') as f:
    c = f.read()

for s in ['aim', 'requirements', 'procedure', 'activity-1', 'activity-2', 'activity-3', 'activity-4', 'activity-5', 'activity-6', 'result-analysis', 'screenshots', 'result']:
    m = re.search(r'<section class="content-section" id="' + s + r'">([\s\S]*?)</section>', c)
    print(f"{s}: {len(m.group(1)) if m else 0} chars")

