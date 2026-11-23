import os
import hashlib

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Check week-4/task-1 step-01 to step-16
print("Week 4 Task 1 hashes:")
for i in range(1, 17):
    p = f"assets/images/week-4/task-1/step-{i:02d}.png"
    print(f"  step-{i:02d}: {get_hash(p)}")

# Check week-6/task-1 step-01 to step-05
print("\nWeek 6 Task 1 hashes:")
for i in range(1, 6):
    p = f"assets/images/week-6/task-1/step-{i:02d}.png"
    print(f"  step-{i:02d}: {get_hash(p)}")

