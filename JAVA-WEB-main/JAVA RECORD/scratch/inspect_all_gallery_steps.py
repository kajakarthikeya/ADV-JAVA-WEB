import sys
sys.path.append('.')
from step_gallery_data import STEP_GALLERY_DATA

out = []
for w_key, tasks in STEP_GALLERY_DATA.items():
    out.append(f"=== {w_key} ===")
    for t_key, steps in tasks.items():
        out.append(f"  Task: {t_key} ({len(steps)} steps)")
        for s in steps:
            out.append(f"    {s[0]}: {s[1]} -> file: {s[2]}")

with open('scratch/all_steps_list.txt', 'w', encoding='utf-8') as fp:
    fp.write("\n".join(out))

print("Wrote all steps to scratch/all_steps_list.txt")
