import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body
import re

pos = w0_body.find('Comprehensive Q&A')
if pos != -1:
    with open('scratch/w0_qa.txt', 'w', encoding='utf-8') as out:
        out.write(w0_body[pos:pos+4000])
    print("Found Q&A in w0_body")
