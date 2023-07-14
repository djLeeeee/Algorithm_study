import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

num = 1
while True:
    s = input().rstrip()
    if '-' in s:
        break
    ans = 0
    stack = []
    for char in s:
        if not stack and char == '}':
            ans += 1
            stack.append('{')
        elif stack and char == '}':
            stack.pop()
        else:
            stack.append('{')
    ans += len(stack) // 2
    print(f'{num}. {ans}')
    num += 1