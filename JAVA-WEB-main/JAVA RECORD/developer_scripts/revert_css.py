# -*- coding: utf-8 -*-

for filepath, marker in [
    ("style.css", "/* ==========================================================================\n   3-LEVEL HIERARCHICAL NAVIGATION"),
    ("assets/css/topic-page.css", "/* ==========================================================================\n   3-LEVEL HIERARCHICAL NAVIGATION")
]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if marker in content:
        truncated = content.split(marker)[0].rstrip() + "\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(truncated)
        print(f"Reverted {filepath} successfully! Truncated from {len(content)} to {len(truncated)} chars.")
    else:
        print(f"Marker not found in {filepath}.")

