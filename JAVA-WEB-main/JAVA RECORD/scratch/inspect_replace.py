with open('pages/week-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Replace', text)]
out = []
for idx in matches[:5]:
    out.append(text[max(0, idx-100):min(len(text), idx+400)])
    out.append('='*50)

with open('scratch/replace_snippets.txt', 'w', encoding='utf-8') as fp:
    fp.write("\n".join(out))
