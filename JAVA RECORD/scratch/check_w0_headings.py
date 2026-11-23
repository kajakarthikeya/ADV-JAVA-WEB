import sys
sys.path.insert(0, '.')
from build_weeks_0_to_3_v2 import w0_body
import re

print("Length of w0_body:", len(w0_body))
h2s = re.findall(r'<h[23][^>]*>.*?</h[23]>', w0_body)
print("Headings in w0_body:")
for h in h2s:
    print(" ", h)
