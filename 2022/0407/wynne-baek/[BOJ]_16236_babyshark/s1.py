# 9시 40분 시작
from collections import deque
import sys
sys.stdin = open('input.txt')


"""
크기 순으로 sort
그 중 먹을 수 있는 놈 check(나보다 작고 가는 길에 방해물 없는지 확인) = 리스트 만들어서 저장, 못 먹는 애들은 위에 두고
거리 check, 거리가 같은 놈이 많다면 젤 앞에꺼 먹어
자신의 크기와 같은 수 물고기 먹을 때마다 크기 1 증가,

"""
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    eat = []
    dist = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append((i, j))
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] <= arr[i][j] or arr[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if arr[nx][ny] < arr[i][j] and arr[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat:
        return -1, -1, -1
    eat.sort(key = lambda x: (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]

N = int(input())
arr = [list(map(int, input().split())) for __ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] and arr[i][j] == 9:
            baby_shark = [i, j]
            arr[i][j] = 2
cnt = 0
eat_cnt = 0
while True:
    x, y = baby_shark[0], baby_shark[1]
    ex, ey, distance = bfs(x, y)
    if ex == -1: break
    arr[ex][ey] = arr[x][y]
    arr[x][y] = 0
    baby_shark = [ex, ey]
    eat_cnt += 1
    if eat_cnt == arr[ex][ey]:
        eat_cnt = 0
        arr[ex][ey] += 1
    cnt += distance
print(cnt)
