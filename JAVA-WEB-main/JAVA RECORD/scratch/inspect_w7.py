import sys
sys.path.append('JAVA-WEB-main')
from update_week_7_v2 import content as w7_body
import re

out = []
out.append(f"w7_body length: {len(w7_body)}")
out.append("Headings in w7:")
for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', w7_body):
    out.append(f"  - {h}")

with open('scratch/w7_structure.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
