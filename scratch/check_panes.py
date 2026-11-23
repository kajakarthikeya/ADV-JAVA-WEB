import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

panes = re.findall(r'id="(week-\d+-pane)"', text)
print('Found panes in index.html:', len(panes), panes)

sidebar_links = re.findall(r'class="sidebar-week-link"[^>]*', text)
print('Sidebar week links count:', len(sidebar_links))
for s in sidebar_links[:5]:
    print('  ', s)

# Let's check script.js inclusion
scripts = re.findall(r'<script[^>]*src="([^"]+)"', text)
print('Scripts included:', scripts)

