import sys, heapq
sys.stdin = open('input.txt')

def dijkstra():
    dist = [[[sys.maxsize] * 4 for _ in range(n)] for _ in range(n)]
    q = []
    for i in range(4):
        dist[sx][sy][i] = 0
        heapq.heappush(q, (0, sx, sy, i))

    while q:
        d, x, y, dir = heapq.heappop(q)
        if (x, y) == (ex, ey):
            return d

        if dist[x][y][dir] < d:
            continue
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] != '*':
                # 현재 케이스가 더 적게 거울을 설치해야 했으면 갱신
                if dist[nx][ny][dir] > d:
                    dist[nx][ny][dir] = d
                    heapq.heappush(q, (d, nx, ny, dir))
                # 거울을 놓을 수 있는 경우
                if arr[nx][ny] == '!':
                    # 상, 하에서 온 경우 => 좌, 우로 전진
                    # 좌, 우에서 온 경우 => 상, 하로 전진
                    if dir < 2:
                        n_dirs = (2, 3)
                    else:
                        n_dirs = (0, 1)
                    for n_dir in n_dirs:
                        if dist[nx][ny][n_dir] > d+1:
                            dist[nx][ny][n_dir] = d+1
                            heapq.heappush(q, (d+1, nx, ny, n_dir))

input = sys.stdin.readline

n = int(input())
arr = []
sx, sy, ex, ey = -1, -1, -1, -1
for i in range(n):
    line = input().rstrip()
    arr.append(line)
    for j in range(n):
        if arr[i][j] == '#':
            if (sx, sy) == (-1, -1):
                sx, sy = i, j
            else:
                ex, ey = i, j

# 상, 하, 오, 왼
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

ans = dijkstra()
print(ans)
