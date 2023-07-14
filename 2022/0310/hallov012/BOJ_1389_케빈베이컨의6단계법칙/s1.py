import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(graph, start):
    visited = [0] * (n + 1)
    num = [0] * (n+1)
    que = deque()
    visited[start] = 1
    que.append(start)
    while que:
        a = que.popleft()
        for i in graph[a]:
            if not visited[i]:
                num[i] = num[a] + 1
                que.append(i)
                visited[i] = 1
    return sum(num)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
sum_lst = [0] * (n+1)
for i in range(1, n+1):
    sum_lst[i] = bfs(g, i)
sum_lst = sum_lst[1:]
for i in range(n):
    if sum_lst[i] == min(sum_lst):
        print(i+1)
        break
