import re
import os

print("=== VERIFYING REQUESTED CLEANUP ===")

with open('index.html', 'r', encoding='utf-8') as f:
    index_text = f.read()

# 1. Downloads section check
assert 'id="downloads"' not in index_text, "Found id='downloads' in index.html!"
assert 'Authoritative Lab Source Code & Documentation Downloads' not in index_text, "Found downloads title in index.html!"
assert 'LAB REPOSITORY RESOURCES' not in index_text, "Found LAB REPOSITORY RESOURCES in index.html!"
assert 'header-tool-btn">⬇ Downloads<' not in index_text, "Found downloads header button in index.html!"
assert '⬇ All Downloads' not in index_text, "Found downloads footer button in index.html!"
print("1. Downloads section & links successfully removed: PASS")

# 2. Step card action buttons check (Fullscreen & Download)
assert 'step-card-actions' not in index_text, "Found step-card-actions in index.html!"
assert 'ss-zoom-trigger' not in index_text, "Found ss-zoom-trigger button in index.html!"
step_btns = re.findall(r'class="step-btn"', index_text)
print(f"Remaining step-btn count in index.html: {len(step_btns)}")
assert len(step_btns) == 0, f"Found {len(step_btns)} step-btn elements in index.html!"
print("2. Photo Fullscreen and Download buttons successfully removed: PASS")

# 3. Modal check
assert 'id="ssModal"' not in index_text, "Found old ssModal in index.html!"
assert 'Download Full-Res' not in index_text, "Found broken Download Full-Res in index.html!"
assert 'id="zoom-modal"' in index_text, "Missing clean zoom-modal in index.html!"
assert 'class="modal-overlay"' in index_text, "Missing modal-overlay in index.html!"
assert 'class="modal-img"' in index_text, "Missing modal-img in index.html!"
assert 'class="modal-close"' in index_text, "Missing modal-close in index.html!"
print("3. Lightbox zoom modal installed cleanly: PASS")

# 4. Check standalone pages
for w in range(14):
    p_path = f'pages/week-{w}.html'
    with open(p_path, 'r', encoding='utf-8') as pf:
        p_text = pf.read()
    assert 'step-card-actions' not in p_text, f"Found step-card-actions in {p_path}!"
    assert 'id="ssModal"' not in p_text, f"Found ssModal in {p_path}!"
    assert 'Download Full-Res' not in p_text, f"Found Download Full-Res in {p_path}!"
    assert 'id="zoom-modal"' in p_text, f"Missing zoom-modal in {p_path}!"
    assert '24EU08161' in p_text, f"Missing roll number in {p_path}!"
print("4. All 14 standalone pages verified clean: PASS")

# 5. Check script.js zoom handler
with open('script.js', 'r', encoding='utf-8') as sf:
    s_text = sf.read()
assert 'function initZoomModal()' in s_text, "Missing initZoomModal() in script.js!"
assert 'ssModal' not in s_text, "Found old ssModal reference in script.js!"
assert 'step-img-wrap' in s_text, "Missing step-img-wrap in script.js click handler!"
print("5. script.js unified zoom handler verified: PASS")

print("\nALL VERIFICATION CHECKS PASSED (100%)!")
