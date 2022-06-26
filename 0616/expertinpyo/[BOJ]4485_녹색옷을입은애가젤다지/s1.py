# 가중치가 있는 문제라고 생각하면 될 듯
# 다익스트라로 접근?
import heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (arr[0][0], 0, 0))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if not visited[x][y]:
            visited[x][y] = 1
            dist[x][y] = weight
            for d in di:
                nx, ny = x + d[1], y + d[0]
                if 0 <= nx < T and 0 <= ny < T and not visited[nx][ny]:
                    heapq.heappush(heap, (weight + arr[nx][ny], nx, ny))

inf = float('inf')
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

tc = 0
while True:
    T = int(input())
    if not T:
        break
    tc += 1
    visited = [[0] * T for _ in range(T)]
    dist = [[0] * T for _ in range(T)]
    arr = [list(map(int, input().split())) for _ in range(T)]
    dijkstra()
    print(f'Problem {tc}: {dist[-1][-1]}')