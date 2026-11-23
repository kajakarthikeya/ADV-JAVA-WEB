import glob
import re
import sys

print("=== VERIFYING ALL 14 WEEK PAGES ===")
for f in sorted(glob.glob("pages/week-*.html")):
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    titles = [re.sub(r'[^\x00-\x7F]+', '', re.sub(r'<[^>]+>', '', t)).strip() for t in re.findall(r'<h2 class="content-section-title.*?>(.*?)</h2>', c)]
    has_analysis = "Result Analysis" in c
    has_proof = "proof-card" in c or "proof-container" in c
    has_mac_dots = "editor-dot" in c
    has_roll = "24EU08161" in c
    title_summary = ", ".join(titles[:4])
    last_title = titles[-1] if titles else ""
    print(f"{f}:")
    print(f"  Sections ({len(titles)}): {title_summary}... [{last_title}]")
    print(f"  Result Analysis: {'YES' if has_analysis else 'NO'} | Proof Cards: {'YES' if has_proof else 'NO'} | Mac Dots: {'YES (BAD)' if has_mac_dots else 'NO (CLEAN)'} | Roll 24EU08161: {'YES' if has_roll else 'NO'}")

print("=== ALL CHECKS COMPLETED ===")
