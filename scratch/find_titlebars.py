with open('build_all_step_screenshots.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Ubuntu Terminal|Windows CMD', text)]
for idx in matches[:5]:
    print(text[max(0, idx-50):min(len(text), idx+150)])
    print('='*50)

