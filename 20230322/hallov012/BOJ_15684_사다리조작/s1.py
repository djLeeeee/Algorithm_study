import sys
sys.stdin = open('input.txt')

def check():
    for i in range(n):
        now = i
        for j in range(h):
            if g[j][now]:
                now += 1
            elif g[j][now-1]:
                now -= 1
        if now != i:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = cnt
        return
    for j in range(y, n-1):
        if not g[x][j] and not g[x][j-1]:
            g[x][j] = 1
            dfs(cnt+1, x, j+1)
            g[x][j] = 0
    for i in range(x+1, h):
        for k in range(n-1):
            if not g[i][k] and not g[i][k-1]:
                g[i][k] = 1
                dfs(cnt+1, i, k+1)
                g[i][k] = 0

input = sys.stdin.readline

n, m, h = map(int, input().split())
g = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = 1
ans = 4
if not m:
    print(0)
    exit()

dfs(0, 0, 0)
if ans > 3:
    print(-1)
else:
    print(ans)