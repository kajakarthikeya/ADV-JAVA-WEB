with open('build_all_step_screenshots.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(create_\w+\([^)]+\))', text)
for m in matches[:10]:
    print(m)
    print('-'*40)

