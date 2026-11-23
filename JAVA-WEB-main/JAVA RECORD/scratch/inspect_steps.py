import re

content = open('index.html', encoding='utf-8').read()

# Find all week sections
weeks = re.findall(r'<section[^>]*id=["\'](week-\d+)["\'][^>]*>(.*?)</section>', content, re.DOTALL)
print(f"Total week sections found: {len(weeks)}")

for week_id, week_content in weeks:
    # Find all tasks
    tasks = re.findall(r'<div[^>]*id=["\'](task-[^"\']+)["\'][^>]*>(.*?)</div>\s*<!--\s*end task', week_content, re.DOTALL | re.IGNORECASE)
    print(f"\n=== {week_id.upper()} ===")
    
    # Find step cards
    cards = re.findall(r'<div[^>]*class=["\'][^"\']*step-card[^"\']*["\'][^>]*>(.*?)</div>\s*</div>', week_content, re.DOTALL)
    if not cards:
        # try another regex
        cards = re.findall(r'<h4[^>]*class=["\']step-card-title["\'][^>]*>(.*?)</h4>.*?<img[^>]*src=["\']([^"\']+)["\']', week_content, re.DOTALL)
        print(f"  Step count: {len(cards)}")
        for t, img in cards[:3]:
            print(f"    {t.strip()} -> {img}")
    else:
        print(f"  Found {len(cards)} step cards")
