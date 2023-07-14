from collections import deque
import sys
sys.stdin = open('input.txt')
def bfs(i, j):
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for i in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if s[nx][ny] <= s[i][j] or s[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if s[nx][ny] < s[i][j] and s[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat:
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:
            s[i][j] = 2
            start = [i, j]
exp = 0
cnt = 0
while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1: break
    s[ex][ey] = s[i][j]
    s[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == s[ex][ey]:
        exp = 0
        s[ex][ey] += 1
    cnt += dist
print(cnt)