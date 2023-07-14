# 백준 21924번 도시 건설 - 다익스트라

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
import heapq


def dijkstra():
    heap = [(0, 1)]
    result = 0

    while heap:
        cw, cv = heapq.heappop(heap)
        if not visited[cv]:
            visited[cv] = 1
            result += cw
        for nv, nw in graph[cv]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv))
    return result


N, M = map(int, input().split())
total = 0
graph = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split())
    total += w
    graph[a].append((b, w))
    graph[b].append((a, w))
visited = [0] * (N + 1)
cost = dijkstra()
if sum(visited) == N:
    print(total - cost)
else:
    print(-1)