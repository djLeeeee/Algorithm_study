import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dist = [0] * (n+1)
que = deque([1])
dist[1] = 1
while que:
    now = que.popleft()
    for next in g[now]:
        if not dist[next]:
            dist[next] = dist[now] + 1
            que.append(next)
cnt = 0
for i in range(1, n+1):
    if len(g[i]) == 1:
        cnt += dist[i] - 1
if cnt % 2:
    print('Yes')
else:
    print('No')


