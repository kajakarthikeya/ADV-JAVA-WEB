with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Let's inspect all DOM queries in script.js
import re
queries = re.findall(r'document\.(?:getElementById|querySelector|querySelectorAll)\([\'"]([^\'"]+)[\'"]\)', js)
print("Unique queries in script.js:")
print(set(queries))

