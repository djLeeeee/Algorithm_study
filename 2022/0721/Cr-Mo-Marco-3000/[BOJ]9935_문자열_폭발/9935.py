import sys
input = sys.stdin.readline

stack = []

string = list(map(str, input().strip()))
target = list(map(str, input().strip()))[::-1]

trigger = target[-1]
L = len(target)
while string:
    v = string.pop()
    stack.append(v)
    if v == trigger and len(stack) >= L:
        for i in range(-1, -1-L, -1):
            if stack[i] != target[i]:
                break
        else:
            for _ in range(L):
                stack.pop()
if stack:
    print(''.join(reversed(stack)))
else:
    print('FRULA')

