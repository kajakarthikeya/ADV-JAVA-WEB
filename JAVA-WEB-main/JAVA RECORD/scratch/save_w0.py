import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body

with open('scratch/w0_body_full.html', 'w', encoding='utf-8') as f:
    f.write(w0_body)
