import sys, heapq, math
input = sys.stdin.readline
N, M = map(int, input().strip().split())
parents = [i for i in range(N+1)]
points = [[] for _ in range(N+1)]

# 총 연결되어야 할 간선의 개수
max_route = N-1
cnt_route = 0
ans = 0

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    parents[find(y)] = find(x)

# 간선의 좌표
for i in range(1, N+1):
    x, y = map(int, input().strip().split())
    points[i] = (x, y)

# 이미 연결된 간선의 개수
for j in range(M):
    a, b = map(int, input().strip().split())
    union(a, b)
    cnt_route += 1

heap = []

for k in range(1, N):
    for l in range(k+1, N+1):
        weight = math.sqrt((points[k][0] - points[l][0]) ** 2 + (points[k][1] - points[l][1]) ** 2)
        heapq.heappush(heap, (weight, k, l))

while cnt_route != max_route and heap:
# while cnt_route != max_route:
    w, x, y = heapq.heappop(heap)
    if find(x) != find(y):
        union(x, y)
        cnt_route += 1
        ans += w

print(f'{ans:0.2f}')