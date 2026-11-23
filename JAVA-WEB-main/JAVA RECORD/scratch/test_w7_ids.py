import sys
sys.path.append('.')
sys.path.append('JAVA-WEB-main')
from update_week_7_v2 import content as w7_body
import re

cleaned = w7_body
for i in range(1, 7):
    cleaned = cleaned.replace('id="activity-%d"' % i, 'id="week-7-task-%d"' % i)

for i in range(1, 7):
    tid = "week-7-task-%d" % i
    target_str = 'id="%s"' % tid
    status = 'FOUND' if target_str in cleaned else 'NOT FOUND'
    print("Checking %s: %s" % (tid, status))
