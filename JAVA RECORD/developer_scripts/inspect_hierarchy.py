import hierarchy_metadata

for w in hierarchy_metadata.HIERARCHY_DATA:
    wnum = w["num"]
    tasks = w["tasks"]
    task_info = []
    for t in tasks:
        p_count = len(t.get("programs", []))
        task_info.append(f"{t['id']} ({p_count} progs)")
    print(f"Week {wnum:2d} ({w['name'][:35]}): {len(tasks)} tasks -> {', '.join(task_info)}")

print("\n--- STEP GALLERY DATA COVERAGE ---")
import step_gallery_data
for wk, tasks in step_gallery_data.STEP_GALLERY_DATA.items():
    for tk, steps in tasks.items():
        print(f"  {wk} -> {tk}: {len(steps)} steps")
