import re
import glob

for f in sorted(glob.glob("pages/week-*.html")):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    sections = re.findall(r'<section class="content-section" id="([^"]+)">', c)
    print(f"{f}: {sections}")
