import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

def dfs(now, start, cnt):
    visited[now] = 1
    for next in g[now]:
        if not visited[next]:
            dfs(next, start, cnt+1)
        elif next == start and cnt > 2:
            cycle[start] = 1
            return

input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

cycle = [0] * (n+1)

for i in range(1, n+1):
    visited = [0] * (n + 1)
    dfs(i, i, 1)

ans = [-1] * (n+1)
que = deque()
for i in range(1, n+1):
    if cycle[i]:
        ans[i] = 0
        que.append(i)
while que:
    x = que.popleft()
    for y in g[x]:
        if ans[y] == -1:
            que.append(y)
            ans[y] = ans[x] + 1
for i in range(1, n+1):
    print(ans[i], end=" ")
