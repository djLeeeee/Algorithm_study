import sys
sys.stdin = open('input.txt')

dxy = {'S': (1, 0) , 'W': (0, -1) ,'E': (0, 1) ,'N': (-1, 0) , }

def dfs(x, y, cnt):

    if check[x][y]:
        return check[x][y]

    check[x][y] = cnt
    nx = x + dxy[map[x][y]][0]
    ny = y + dxy[map[x][y]][1]
    check[x][y] = dfs(nx, ny, cnt)
    return check[x][y]

N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]
# print(map)
check = [[0]* M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not check[i][j]:
            a = dfs(i, j, cnt + 1)
            cnt = max(cnt, a)
print(cnt)