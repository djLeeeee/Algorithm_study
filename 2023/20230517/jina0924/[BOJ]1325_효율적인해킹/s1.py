# 백준 1325번 효율적인 해킹

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(v):
    queue = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1
    cnt = 0

    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                queue.append(nv)
                visited[nv] += 1
                cnt += 1
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
maxV = 0
ans = []
for i in range(1, N + 1):
    result = bfs(i)
    if result > maxV:
        maxV = result
        ans = [i]
    elif result == maxV:
        ans.append(i)
print(*ans)