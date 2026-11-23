import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

panes = re.findall(r'id=["\'](week-[^"\']*pane)["\']', c)
print(f"Total panes found: {len(panes)}")
print(panes)

