import sys
sys.stdin = open('input.txt')

data = input().rstrip()
stack = []
temp = 1
ans = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
        temp *= 2
    elif data[i] == '[':
        stack.append(data[i])
        temp *= 3
    elif data[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if data[i-1] == '(':
            ans += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if data[i-1] == '[':
            ans += temp
        temp //= 3
        stack.pop()
if stack:
    ans = 0
print(ans)

