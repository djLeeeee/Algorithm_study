import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt')

# 90도 회전
def rotate(arr):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][4-i] = arr[i][j]
    return tmp

def dfs(idx):
    if idx == 5:
        if maze[4][4][4]:
            bfs(maze)
        return
    for i in range(4):
        if maze[0][0][0]:
            dfs(idx+1)
        maze[idx] = rotate(maze[idx])

def bfs(arr):
    global ans
    q = deque()
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    q.append((0, 0, 0))
    while q:
        h, x, y = q.popleft()
        if (x, y, h) == (4, 4, 4):
            ans = min(ans, visited[4][4][4])
            if ans == 12:
                print(ans)
                exit()
            return
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nh = h + dh[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nh < 5:
                if arr[nh][nx][ny] and not visited[nh][nx][ny]:
                    visited[nh][nx][ny] = visited[h][x][y] + 1
                    q.append((nh, nx, ny))

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
ans = sys.maxsize

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]
for case in permutations(list(range(5))):
    for i in range(5):
        maze[case[i]] = board[i]
    dfs(0)

print(ans-1 if ans != sys.maxsize else -1)