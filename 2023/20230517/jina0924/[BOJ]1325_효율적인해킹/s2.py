# 백준 1325번 효율적인 해킹

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(v):
    queue = deque([v])
    cnt = 0
    visited = [0] * (N + 1)
    visited[v] = 1

    while queue:
        cv = queue.popleft()
        for nv in graph[cv]:
            if not visited[nv]:
                visited[nv] = 1
                queue.append(nv)
                cnt += 1
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    cnt[i] = bfs(i)

for i in range(1, N + 1):
    if cnt[i] == max(cnt):
        print(i, end=' ')
