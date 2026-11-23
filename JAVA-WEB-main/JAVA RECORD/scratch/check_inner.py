import re

with open('JAVA-WEB-main/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

panes = re.findall(r'id="(week-\d+-pane)"', text)
print('Found panes in inner index.html:', len(panes), panes)

sidebar_links = re.findall(r'class="sidebar-week-link"[^>]*', text)
print('Sidebar week links count in inner:', len(sidebar_links))
for s in sidebar_links[:5]:
    print('  ', s)

