import sys
sys.path.insert(0, '.')
from build_sidebar_helpers import WEEKS_META

for w in WEEKS_META:
    print(f"WEEK {w['num']}: {w['title']}")
    for tid, ttitle in w['tasks']:
        print(f"   {tid} -> {ttitle}")
