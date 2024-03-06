import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        g[u][v] = g[v][u] = 0
    else:
        g[u][v] = 0
        g[v][u] = 1

for i in range(1, n+1):
    g[i][i] = 0

for p in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][p] + g[p][j])

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(g[s][e])