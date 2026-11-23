import sys
sys.path.append('JAVA-WEB-main')
from update_week_7_v2 import content as w7_body
import re

matches = re.findall(r'(<section[^>]*id=["\'](.*?)["\'][^>]*>[\s\S]*?<h2[^>]*>(.*?)</h2>)', w7_body)
lines = []
for m in matches:
    lines.append(f"ID: {m[1]} | Title: {m[2][:60]}")

with open('scratch/w7_sections.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))
