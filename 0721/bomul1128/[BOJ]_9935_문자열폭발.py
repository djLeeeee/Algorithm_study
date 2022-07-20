a = input()
bomb = input()
l = len(bomb)
tail = bomb[-1]
stack = []
for c in a:
    stack.append(c)
    if tail == c:
        if ''.join(stack[-l:]) == bomb:
            for _ in range(l):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
