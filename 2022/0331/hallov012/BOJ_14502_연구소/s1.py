import sys
from collections import deque

sys.stdin = open('input.txt')

def virus():
    global ans
    virus_lst = deque([])
    new_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][j]
            if arr[i][j] == 2:
                virus_lst.append([i, j])
    while virus_lst:
        x, y = virus_lst.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = 2
                    virus_lst.append([nx, ny])
    cnt = 0
    for line in new_arr:
        cnt += line.count(0)
    ans = max(ans, cnt)


def wall(wall_cnt):
    if wall_cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                wall(wall_cnt + 1)
                arr[i][j] = 0




input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
wall(0)
print(ans)


