import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

ids = [m for m in re.findall(r'id=["\']([^"\']*)["\']', c) if m.startswith('week-')]
print(f"Total matching ids: {len(ids)}")
print(ids)

