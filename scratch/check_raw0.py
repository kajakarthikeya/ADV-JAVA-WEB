with open('raw_bodies.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos0 = text.find('raw_bodies = {')
print('raw_bodies found')
# Let's inspect raw_bodies[0]
import raw_bodies
print('Length of raw_bodies[0]:', len(raw_bodies.raw_bodies[0]))
lines0 = raw_bodies.raw_bodies[0].splitlines()
print('Total lines in raw_bodies[0]:', len(lines0))
for i, l in enumerate(lines0[:40]):
    print(f'{i+1}: {l[:100]}')
