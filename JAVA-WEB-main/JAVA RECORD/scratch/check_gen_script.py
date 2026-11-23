with open('generate_step_screenshots.py', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of generate_step_screenshots.py:', len(text))
lines = text.splitlines()
print('First 60 lines:')
for l in lines[:60]:
    print(l)
