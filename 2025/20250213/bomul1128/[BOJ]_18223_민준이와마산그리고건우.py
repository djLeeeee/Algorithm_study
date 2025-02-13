# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/18223
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=18223&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin
import heapq

input = stdin.readline

def dijkstra(start):
    INF = 1e9
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))
dist_from_start = dijkstra(1)
dist_from_mid = dijkstra(k)
if dist_from_start[k] + dist_from_mid[n] == dist_from_start[n]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
