with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's count { and } in script.js
print("Total { :", text.count('{'))
print("Total } :", text.count('}'))
print("Difference:", text.count('{') - text.count('}'))
