from collections import deque
import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
di = ((0, 1), (1, 0), (0, -1), (-1, 0))
flag = 0
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
queue = deque()
r, c = 0, 0
ans = 0

def roll(flag):
    if flag == 0:   #동
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif flag == 1: #남
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif flag == 2: #서
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    else:           #북
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]


def bfs(rr, cc):
    global N, M
    res = mp[rr][cc]
    queue.append((rr, cc))
    visited = [[0]*M for _ in range(N)]
    visited[rr][cc] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and mp[nr][nc] == mp[r][c]:
                visited[nr][nc] = 1
                queue.append((nr, nc))
                res += mp[nr][nc]
    return res


for k in range(K):

    nr, nc = r+di[flag][0], c+di[flag][1]
    if 0 <= nr < N and 0 <= nc < M:
        roll(flag)
        ans += bfs(nr, nc)
    else:
        flag = (flag+2)%4
        roll(flag)
        nr, nc = r+di[flag][0], c+di[flag][1]
        ans += bfs(nr, nc)
    if dice[3][1] > mp[nr][nc]:
        flag = (flag+1)%4
    elif dice[3][1] < mp[nr][nc]:
        flag = (flag+3)%4
    r, c = nr, nc

print(ans)