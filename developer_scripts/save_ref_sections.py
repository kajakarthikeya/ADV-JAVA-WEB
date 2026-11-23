with open('ref_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

for sid in ['java-msaccess', 'crud-operations', 'servlets']:
    m = re.search(r'<section id="' + sid + r'"[\s\S]*?</section>', html)
    if m:
        with open(f'ref_{sid}.html', 'w', encoding='utf-8') as f:
            f.write(m.group(0))
        print(f"Saved ref_{sid}.html (length: {len(m.group(0))})")
    else:
        print(f"Section {sid} not found")

