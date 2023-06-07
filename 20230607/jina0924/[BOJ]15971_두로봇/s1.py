# 백준 15971번 두 로봇 - 41%

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline
from collections import defaultdict
import heapq


def connect():
    heap = [(0, A, A, 0), (0, B, B, 0)]
    visited = [0] * (N + 1)
    cnt = [0] * (N + 1)

    while heap:
        cw, cv, s, total = heapq.heappop(heap)
        cnt[cv] += total
        visited[cv] = s
        for nv, nw in graph[cv]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv, s, total + nw))
            elif visited[nv] and visited[nv] != s:
                return cnt[cv] + cnt[nv]


N, A, B = map(int, input().split())
graph = defaultdict(list)
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
if A == B:
    print(0)
else:
    print(connect())