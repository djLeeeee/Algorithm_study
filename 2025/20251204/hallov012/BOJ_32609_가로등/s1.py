import sys
from collections import deque
sys.stdin = open('input.txt')

l, n, k = map(int, input().split())
arr = list(map(int, input().split()))

if n >= k:
    for _ in range(k):
       print(0)
    exit()

light = {}
que = deque()
for num in arr:
    light[num] = 0
    que.append(num)

cnt = 0
while que:
    x = que.popleft()
    cnt += 1
    if cnt == k:
        break
    for dx in [-1, 1]:
        nx = x + dx
        if 0 <= nx <= l and nx not in light:
            light[nx] = light[x] + 1
            que.append(nx)

ans = sorted(light.values())
for i in range(k):
    print(ans[i])