import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body, w1_body
import re

out = []
out.append(f"w0_body length: {len(w0_body)}")
out.append(f"Does w0 have result-analysis? {'result-analysis' in w0_body}")
out.append("Headings in w0:")
for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', w0_body):
    out.append(f"  - {h}")

out.append(f"\nw1_body length: {len(w1_body)}")
out.append(f"Does w1 have result-analysis? {'result-analysis' in w1_body}")
out.append("Headings in w1:")
for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', w1_body):
    out.append(f"  - {h}")

with open('scratch/w0_w1_structure.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
