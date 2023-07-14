# 백준 13023번 ABCDE

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(2000)


def dfs(v, depth):
    global ans
    if depth >= 5:
        ans = 1
        return
    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = depth + 1
            dfs(nv, depth + 1)
            visited[nv] = 0


n, m = map(int, input().split())
graph = defaultdict(list)
visited = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = 0
for i in range(n):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0
    if ans == 1:
        print(ans)
        sys.exit()
print(ans)