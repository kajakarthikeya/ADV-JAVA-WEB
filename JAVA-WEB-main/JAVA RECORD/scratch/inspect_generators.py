with open('build_all_step_screenshots.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'def create_', text)]
for idx in matches[:5]:
    print(text[idx:idx+800])
    print('='*50)

