from sys import stdin
from collections import deque
V, E = map(int, stdin.readline().rstrip().split())

g = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(V-1):
    start, end, W = map(int, input().split())
    g[start].append([end, W])
    g[end].append([start, W])


# 1 시작일 때 해 보자

visited = [0] * (V + 1)
Q = deque([(1, 1000000001)])
while Q:
    # 현재 노드 v, weight
    v, weight = Q.popleft()
    # 검사 노드 nod, w
    for nod, w in g[v]:
        if w < weight:
            visited[nod] = w
            q.append((nod, w))
        elif w > weight:
            visited[nod] = weight
            q.append((nod, weight))



# for _ in range(E):
#     k, v = map(int, stdin.readline().rstrip().split())
#     ans_list.append((v, k))
#

