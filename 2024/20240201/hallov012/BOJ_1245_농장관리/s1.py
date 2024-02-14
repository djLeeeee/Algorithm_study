import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(i, j):
    global ans
    que = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    h = arr[i][j]
    temp = [(i, j)]
    while que:
        x, y = que.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 봉우리가 아니니까 더 이상 볼 필요 없음
                if arr[nx][ny] > h:
                    return
                # 같은 높이면 여기도 봉우리가 될 수 있음
                elif arr[nx][ny] == h:
                    temp.append((nx, ny))
                    visited[nx][ny] = 1
                    que.append((nx, ny))

    # return 안되고 여기까지 왔다면 봉우리임
    for (x, y) in temp:
        check[x][y] = 1
    ans += 1
    return

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not check[i][j]:
            bfs(i, j)

print(ans)



