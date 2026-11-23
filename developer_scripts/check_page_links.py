import re

with open("pages/week-0.html", "r", encoding="utf-8") as f:
    c = f.read()

links = re.findall(r'<a href=["\']([^"\']*)["\'] class=["\']sidebar-week-link["\']', c)
print(f"Total sidebar week links in pages/week-0.html: {len(links)}")
print(links[:5])

