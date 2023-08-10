# 최대한의 금빼빼로 개수 존재
# 빼빼로의 개수가 일정 이상이면 상관 없음
# 가중치가 크다고 못가는 건 아님

import heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (-10**6, s))
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = -weight
            if node == e:
                print(dist[node])
                break
            for new_n, new_w in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (-min(-weight, new_w), new_n))


n, m = map(int, input().split())
s, e = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    h1, h2, k = map(int, input().split())
    arr[h1].append([h2, k])
    arr[h2].append([h1, k])

dist = [-1] * (n+1)
visited = [0] * (n+1)
dist[s] = 10 ** 6
dijkstra()
