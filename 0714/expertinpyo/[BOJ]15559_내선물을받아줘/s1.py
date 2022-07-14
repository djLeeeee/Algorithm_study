n, m = map(int, input().split())
MAP = [list(input()) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dic = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

def dfs(y, x, cnt):
    global n, m

    if check[y][x]:
        return check[y][x]

    check[y][x] = cnt
    ny = y + dic[MAP[y][x]][0]
    nx = x + dic[MAP[y][x]][1]
    check[y][x] = dfs(ny, nx, cnt)
    return check[y][x]


result = 0
for i in range(n):
    for j in range(m):
        if not check[i][j]:
            a = dfs(i, j, result + 1)
            result = max(a, result)

print(result)