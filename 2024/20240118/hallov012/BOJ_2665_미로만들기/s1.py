import sys, heapq
sys.stdin = open('input.txt')

def dijkstra():
    visited = [[0] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = 1
    while q:
        cnt, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if arr[nx][ny] == '1':
                        heapq.heappush(q, (cnt, nx, ny))
                    else:
                        heapq.heappush(q, (cnt+1, nx, ny))

input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = dijkstra()

print(ans)
