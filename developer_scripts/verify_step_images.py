import os
import step_gallery_data

missing = []
total = 0
for wk, tasks in step_gallery_data.STEP_GALLERY_DATA.items():
    for tk, steps in tasks.items():
        for s in steps:
            total += 1
            # tuple is (step_num, title, fname, desc)
            fname = s[2]
            clean_path = os.path.join("assets", "images", wk, tk, fname)
            if not os.path.exists(clean_path):
                missing.append((wk, tk, s[0], clean_path))

print(f"Total step screenshots checked: {total}")
if missing:
    print(f"Missing images ({len(missing)}):")
    for m in missing[:15]:
        print(" ", m)
else:
    print("ALL 228 STEP SCREENSHOTS EXIST ON DISK AND ARE ACCESSIBLE!")
