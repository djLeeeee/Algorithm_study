import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    words = input()
    stack = []
    ans = True
    for char in words:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                stack.pop()
            else:
                ans = False
                break
    if stack:
        ans = False

    if ans:
        print('YES')
    else:
        print('NO')