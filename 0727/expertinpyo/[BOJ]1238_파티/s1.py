# 1238
# dijkstra
import heapq

def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        time, student = heapq.heappop(heap)
        if not visited[student]:
            visited[student] = 1
            dist[student] = time
            for new_student, new_time in arr[student]:
                if not visited[new_student]:
                    heapq.heappush(heap, (dist[student] + new_time, new_student))


n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    arr[start].append([end, weight])

ans_list = [0] * (n+1)
for k in range(1, n+1):
    visited = [0] * (n+1)
    dist = [10**6] * (n+1)
    dijkstra(k)
    if k != x:
        ans_list[k] += dist[x]
    else:
        for j in range(1, n+1):
            ans_list[j] += dist[j]
print(max(ans_list))

