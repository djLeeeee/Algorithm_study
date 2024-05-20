import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

v, e = map(int, input().split())
g = [[sys.maxsize] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = sys.maxsize
for i in range(1, v+1):
    ans = min(ans, g[i][i])

print(ans if ans != sys.maxsize else -1)