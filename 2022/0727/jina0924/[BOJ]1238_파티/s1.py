# 백준 1238번 파티

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


def dijkstra(s, dist, graph):
    heap = []
    heapq.heappush(heap, (0, s))                # 시작 노드 정보를 heap에 넣어줌
    dist[s] = 0                                 # 시작점의 시간 갱신(시작점이니까 걸리는 시간 = 0)

    while heap:
        t, node = heapq.heappop(heap)
        if dist[node] < t:                      # 이미 dist에 저장된 가중치보다 t가 높다면 이전에 방문했으므로 넘어감
            continue
        for neighbor in graph[node]:            # 현재 노드와 인접한 부분 순회
            cost = dist[node] + neighbor[1]     # 인접한 노드까지 갈 때 필요한 가중치 값 계산
            if cost < dist[neighbor[0]]:        # dist에 저장된 값보다 계산한 가중치 값이 적다면
                dist[neighbor[0]] = cost        # dist에 갱신해주고 heap에 담아줌
                heapq.heappush(heap, (cost, neighbor[0]))


N, M, X = map(int, input().split())
INF = int(1e9)
dist1 = [0] + [INF] * (N)                       # X에서 출발할 때 걸리는 시간
dist2 = [0] + [INF] * (N)                       # X로 도착하기까지 걸리는 시간
graph1 = [[] for _ in range(N+1)]               # X로 출발할 때 인접한 도로
graph2 = [[] for _ in range(N+1)]               # X로 도착하기까지 인접한 도로
for _ in range(M):
    start, end, t = map(int, input().split())
    graph1[start].append((end, t))
    graph2[end].append((start, t))

dijkstra(X, dist1, graph1)
dijkstra(X, dist2, graph2)

ans = 0
for i in range(1, N+1):
    ans = max(dist1[i] + dist2[i], ans)

print(ans)