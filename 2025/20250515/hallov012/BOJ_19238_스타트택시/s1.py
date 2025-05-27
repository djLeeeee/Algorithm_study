import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find_passenger(sx, sy):
    que = deque([(sx, sy)])
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    min_d = -1
    p_lst = []
    while que:
        x, y = que.popleft()
        if 0 <= min_d < visited[x][y]-1:
            continue
        if arr[x][y] < 0:
            p = -arr[x][y]
            if not arrive[p]:
                min_d = max(min_d, visited[x][y]-1)
                p_lst.append((x, y, p))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    if min_d < 0:
        return 0, 0
    p = sorted(p_lst)[0][2]
    return p, min_d

def find_dist_to_goal(sx, sy, ex, ey):
    que = deque([(sx, sy)])
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    while que:
        x, y = que.popleft()
        if x == ex and y == ey:
            return visited[x][y] - 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1


n, m, f = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda v: int(v)-1, input().split())
passenger = [None]
for i in range(1, m+1):
    ax, ay, bx, by = map(lambda v: int(v)-1, input().split())
    arr[ax][ay] = -i
    passenger.append((ax, ay, bx, by))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
remain = f
arrive = [0] * (m+1)
for _ in range(m):
    p, dist_to_p = find_passenger(x, y)
    if not p:
        print(-1)
        exit()
    sx, sy, ex, ey = passenger[p]
    dist_to_goal = find_dist_to_goal(sx, sy, ex, ey)
    if dist_to_goal < 0:
        print(-1)
        exit()
    dist = dist_to_p + dist_to_goal
    if dist <= remain:
        arrive[p] = 1
        remain -= dist_to_p
        remain += dist_to_goal
        x, y = ex, ey
    else:
        print(-1)
        exit()
print(remain)


