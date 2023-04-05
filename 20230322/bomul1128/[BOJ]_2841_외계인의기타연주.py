from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
memo = {}
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    stack = memo.get(x, [])
    while stack and stack[-1] > y:
        ans += 1
        stack.pop()
    if not stack or stack[-1] != y:
        ans += 1
        stack.append(y)
    memo[x] = stack
print(ans)
