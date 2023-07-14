# 백준 2504번 괄호의 값

import sys
sys.stdin = open('input.txt')

data = list(input())
stack = []
ans, tmp = 0, 1
for i in range(len(data)):
    char = data[i]
    if char == '(':
        stack.append(char)
        tmp *= 2
    elif char == '[':
        stack.append(char)
        tmp *= 3
    elif char == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if data[i - 1] == '(':                  # 제일 안쪽 완성 괄호형에서 누적된 값 더해줌
            ans += tmp
        tmp //= 2
        stack.pop()
    elif char == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if data[i - 1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()
if stack:
    print(0)
else:
    print(ans)