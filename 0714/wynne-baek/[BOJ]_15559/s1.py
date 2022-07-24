import sys
sys.stdin = open('input.txt')

dxy = {'S': (1, 0) , 'W': (0, -1) ,'E': (0, 1) ,'N': (-1, 0) , }

def dfs(x, y, i, j):
    nx = x + dxy[map[x][y]][0]
    ny = y + dxy[map[x][y]][1]
    if not check[nx][ny]:
        check[nx][ny] = (i, j)
        dfs(nx, ny, i, j)

N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]
# print(map)
check = [[0]* M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not check[i][j]:
            check[i][j] = (i, j)
            dfs(i, j, i, j)
result = set()
for line in check:
    line_set = set(line)
    result = result.union(line)
print(len(result))