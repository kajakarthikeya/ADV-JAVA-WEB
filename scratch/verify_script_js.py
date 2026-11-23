with open('script.js', encoding='utf-8') as f:
    code = f.read()

# Check balanced brackets
stack = []
pairs = {')': '(', '}': '{', ']': '['}
lines = code.split('\n')
for line_no, line in enumerate(lines, 1):
    in_str = False
    quote = ''
    for char in line:
        if in_str:
            if char == quote:
                in_str = False
        elif char in ("'", '"', '`'):
            in_str = True
            quote = char
        elif char in '({[':
            stack.append((char, line_no))
        elif char in ')}]':
            if not stack:
                print(f"Unmatched closing {char} at line {line_no}")
                break
            top, top_line = stack.pop()
            if pairs[char] != top:
                print(f"Mismatched {char} at line {line_no}, expected {top} from line {top_line}")
                break

if not stack:
    print("script.js syntax and brackets are perfectly balanced!")
else:
    print(f"Unclosed open brackets: {len(stack)}: {stack[-3:]}")

