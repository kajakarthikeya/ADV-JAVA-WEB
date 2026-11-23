import os
import re

for w in range(14):
    fpath = f"pages/week-{w}.html"
    if os.path.exists(fpath):
        c = open(fpath, encoding="utf-8").read()
        aim = len(re.findall(r'id="aim"', c))
        req = len(re.findall(r'id="requirements"', c))
        proc = len(re.findall(r'id="procedure"', c))
        progs = len(re.findall(r'class="program-card"', c))
        steps = len(re.findall(r'class="step-card"', c))
        res = len(re.findall(r'class="analysis-card"', c))
        print(f"Week {w:2d} ({len(c):6d} B): Aim={aim}, Req={req}, Proc={proc}, Progs={progs}, Steps={steps}, AnalysisCards={res}")

