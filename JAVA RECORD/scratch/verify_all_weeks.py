import re
import os

print("=== VERIFYING DIGITAL LAB RECORD ===")

with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Check all 14 week panes in index.html
panes = re.findall(r'id="(week-(\d+)-pane)"', index_html)
print(f"Total week panes found: {len(panes)}")
assert len(panes) == 14, f"Expected 14 panes, found {len(panes)}"
for pane_id, w_num in panes:
    assert int(w_num) in range(14)

# 2. Check sidebar week links in index.html
week_links = re.findall(r'class="sidebar-week-link"[^>]*', index_html)
print(f"Total sidebar week links found: {len(week_links)}")
assert len(week_links) == 14
for i, wl in enumerate(week_links):
    assert f'data-week="{i}"' in wl, f"Missing data-week='{i}' in {wl}"
    assert f'data-week-target="week-{i}-pane"' in wl, f"Missing data-week-target in {wl}"

# 3. Check standalone pages
for w in range(14):
    p_path = f"pages/week-{w}.html"
    assert os.path.exists(p_path), f"Missing {p_path}"
    with open(p_path, "r", encoding="utf-8") as pf:
        p_content = pf.read()
    # Check student info
    assert "24EU08161" in p_content, f"Missing roll number in {p_path}"
    assert "Venkata Sai Karthikeya Kaja" in p_content, f"Missing student name in {p_path}"
    assert "24IT385" in p_content, f"Missing course code in {p_path}"
    # Check mac dots absent
    assert 'dot red' not in p_content and 'window-controls' not in p_content, f"Found mac dots in {p_path}"

# 4. Check Mac dots in index.html and CSS
assert 'dot red' not in index_html and 'window-controls' not in index_html, "Found mac dots in index.html"
with open("style.css", "r", encoding="utf-8") as sf:
    s_css = sf.read()
assert '.window-controls' not in s_css and '.dot.red' not in s_css, "Found mac dots in style.css"

# 5. Check profile dropdown from prompt 7 is NOT in header
assert 'profileDropdownBtn' not in index_html, "Found prompt 7 profileDropdownBtn in index.html"
assert 'header-student-pill' in index_html, "Missing prompt 6 header-student-pill in index.html"
assert 'Roll Number: <span class="roll-badge">24EU08161</span>' in index_html, "Missing prompt 6 header roll sub"

print("ALL AUDIT CHECKS PASSED PERFECTLY (100%)!")

