with open('JAVA-WEB-main/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
week_panes = re.findall(r'<div[^>]*class="[^"]*week-pane[^"]*"[^>]*id="([^"]+)"', text)
print('Inner index week panes:', week_panes)

# Check Week 1 pane
p1_pos = text.find('id="week-1-pane"')
print('week-1-pane position:', p1_pos)
if p1_pos != -1:
    print(text[p1_pos-50:p1_pos+150])

