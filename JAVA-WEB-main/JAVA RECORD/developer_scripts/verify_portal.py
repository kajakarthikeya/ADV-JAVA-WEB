import glob
import re

files = ["index.html"] + sorted(glob.glob("pages/week-*.html"))

print(f"=== VERIFYING {len(files)} PORTAL HTML FILES ===")

all_ok = True
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    has_header = "ADVANCED JAVA PROGRAMMING" in c and "24EU08161" in c
    has_sidebar = "portal-sidebar" in c
    has_week_heading = "week-display-title" in c
    has_task_heading = "task-display-title" in c
    has_mac_dots = "editor-dot" in c
    
    # Check count of weeks in sidebar
    week_links = len(re.findall(r'class="sidebar-week-link"', c))
    
    # Check step cards
    step_cards = len(re.findall(r'class="step-card"', c))
    
    status = "OK" if (has_header and has_sidebar and has_week_heading and has_task_heading and not has_mac_dots and week_links == 14) else "WARN"
    if status != "OK":
        all_ok = False
        
    print(f"{f}: [{status}] Header: {has_header} | Sidebar: {week_links}/14 weeks | WeekTitle: {has_week_heading} | TaskTitle: {has_task_heading} | StepCards: {step_cards} | MacDots: {'YES(BAD)' if has_mac_dots else 'NO'}")

print(f"\nALL 15 FILES PERFECT: {all_ok}")

