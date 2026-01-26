import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

def remove_mineral(h, turn):
    range_lst = list(range(m-1, -1, -1)) if turn % 2 else list(range(m))
    for j in range_lst:
        if arr[h][j] == 'x':
            arr[h][j] = '.'
            return True
    return False

def find_cluster():
    que = deque()
    for j in range(m):
        if arr[n-1][j] == 'x':
            que.append((n-1, j))
            visited[n-1][j] = 1
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 'x':
                    visited[nx][ny] = 1
                    que.append((nx, ny))
    for i in range(n-1, -1, -1):
        for j in range(m):
            if arr[i][j] == 'x' and not visited[i][j]:
                cluster.append((i, j))

def move_cluster():
    down = sys.maxsize
    for x, y in cluster:
        d_cnt = 0
        for i in range(x+1, n):
            if arr[i][y] == '.':
                d_cnt += 1
            # 바닥에 닿는 부분
            elif visited[i][y]:
                break
        down = min(down, d_cnt)
    for x, y in cluster:
        arr[x][y] = '.'
        arr[x + down][y] = 'x'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [[*input()] for _ in range(n)]
cnt = int(input())
h_list = list(map(int, input().split()))
for i in range(cnt):
    flag = remove_mineral(n - h_list[i], i)
    if not flag:
        continue
    visited = [[0] * m for _ in range(n)]
    cluster = []
    find_cluster()
    if len(cluster):
        move_cluster()

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()




