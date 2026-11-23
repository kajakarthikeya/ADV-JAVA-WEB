import sys
sys.path.append('.')
from step_gallery_data import STEP_GALLERY_DATA

out = []
for w in ['week-0', 'week-1']:
    out.append(f"=== {w} ===")
    steps = STEP_GALLERY_DATA.get(w, {}).get('task-1', [])
    out.append(f"Total steps: {len(steps)}")
    for s in steps:
        out.append(f"  Step {s['step']}: {s['title']} | img: {s['img']}")

with open('scratch/w0_w1_gallery.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
