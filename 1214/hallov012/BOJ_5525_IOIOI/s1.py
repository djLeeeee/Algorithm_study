import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
s = input().rstrip()
target = deque(['I'] + ['O', 'I'] * n)
que = deque((s[:2*n+1]))
ans = 0
if target == que:
    ans += 1
for i in range(2*n+1, m):
    que.popleft()
    que.append(s[i])
    if target == que:
        ans += 1
print(ans)

