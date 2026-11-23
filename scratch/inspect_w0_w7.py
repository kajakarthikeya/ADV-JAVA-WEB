import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body
from update_week_7_v2 import content as w7_body
import re

out = []
out.append("--- Week 0 sections / headings ---")
for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', w0_body):
    out.append(f"  {m.group(1)}")

out.append("\n--- Week 7 sections / headings ---")
for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', w7_body):
    out.append(f"  {m.group(1)}")

with open('scratch/w0_w7_headings.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Wrote w0_w7_headings.txt")
