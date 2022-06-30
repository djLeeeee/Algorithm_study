import heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (-10**6, s))
    while heap:
        weight, node = heapq.heappop(heap)
        weight *= -1
        if not visited[node]:
            visited[node] = weight
            for new_n, new_w in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (-min(weight, new_w), new_n))


n, m = map(int, input().split())
s, e = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    h1, h2, k = map(int, input().split())
    arr[h1].append([h2, k])
    arr[h2].append([h1, k])

visited = [0] * (n+1)
dijkstra()
print(visited[e])