# 백준 16947번 서울 지하철 2호선

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(3000)

N = int(input())
graph = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def get_dist(s, e):
    isCycle[e] = True
    nv = p[e]
    while nv != s:                  # 끝점부터 시작해서 사이클여부 저장
        isCycle[nv] = True
        nv = p[nv]

    queue = deque([(s, 0)])         # queue에 정점과 거리 저장(사이클이면 0, 아니면 +1 할 용도)
    visited = [0] * (N + 1)
    visited[s] = 1
    while queue:
        cv, cnt = queue.popleft()
        for nv in graph[cv]:
            if not visited[nv]:
                visited[nv] = 1
                if isCycle[nv]:
                    queue.append((nv, 0))
                else:
                    queue.append((nv, cnt + 1))
                    dist[nv] = cnt + 1

    for i in range(1, N + 1):
        print(dist[i], end=' ')
    sys.exit()


def dfs(v, pv):
    p[v] = pv
    for nv in graph[v]:
        if not p[nv]:               # 아직 부모노드 안봤다면
            dfs(nv, v)
        elif pv != nv:              # 부모가 있는데 서로 다르다면 사이클 연결선
            get_dist(nv, v)
            return


p = [0] * (N + 1)
dist = [0] * (N + 1)
isCycle = [False] * (N + 1)
dfs(1, 1)