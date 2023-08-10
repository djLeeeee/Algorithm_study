import sys
import heapq

sys.stdin = open('input.txt')

N, M, X = map(int, input().split())
dist = [[] for _ in range(N+1)]

for i in range(M):
    s, e, w = map(int, input().split())
    dist[s].append((e, w))

def dijkstra(start):
    queue = []
    distance = [987654321] * (N+1)

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        weight, now = heapq.heappop(queue)

        if distance[now] < weight:
            continue
        for end, node_cost in dist[now]:
            cost = weight + node_cost
            if distance[end] > cost:
                distance[end] = cost
                heapq.heappush(queue, (cost, end))
    return distance

result = []
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    result.append(go[X] + back[i])
print(max(result))
