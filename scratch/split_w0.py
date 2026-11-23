import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body
import re

sections = re.findall(r'<section[^>]*id=["\'](.*?)["\'][^>]*>([\s\S]*?)</section>', w0_body)
print(f"Total sections found in w0_body: {len(sections)}")
for sid, content in sections:
    print(f"Section ID: {sid} (length: {len(content)})")
