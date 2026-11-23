import glob
import re

for p in glob.glob("JAVA-WEB-main/pages/*.html"):
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    if "editor-dots" in c:
        c = re.sub(r'<div class="editor-dots">[\s\S]*?</div>', '<div class="ide-tab"><span class="ide-tab-icon">☕</span> Source Code</div>', c)
        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print("Cleaned:", p)

print("Dot cleanup complete.")

