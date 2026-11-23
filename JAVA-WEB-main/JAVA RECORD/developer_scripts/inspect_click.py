with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check sidebar links
import re
week_links = re.findall(r'<a[^>]*class="sidebar-week-link"[^>]*>', html)
print(f"Total sidebar-week-links: {len(week_links)}")
for l in week_links[:5]:
    print(" ", l)

panes = re.findall(r'<div[^>]*class="week-pane[^"]*"[^>]*>', html)
print(f"Total week-panes: {len(panes)}")
for p in panes[:5]:
    print(" ", p)

