import os
import re

for w in range(14):
    fpath = f"pages/week-{w}.html"
    if os.path.exists(fpath):
        c = open(fpath, encoding="utf-8").read()
        proc = re.search(r'<div class="task-sub-block" id="procedure">([\s\S]*?)</div>\s*<div class="task-sub-block" id="program">', c)
        aim = re.search(r'<div class="task-sub-block" id="aim">([\s\S]*?)</div>\s*<div class="task-sub-block" id="requirements">', c)
        req = re.search(r'<div class="task-sub-block" id="requirements">([\s\S]*?)</div>\s*<div class="task-sub-block" id="procedure">', c)
        print(f"Week {w:2d}: Aim len={len(aim.group(1)) if aim else 0}, Req len={len(req.group(1)) if req else 0}, Proc len={len(proc.group(1)) if proc else 0}")

