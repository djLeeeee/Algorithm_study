import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

INF = 10**5
n, m = map(int, input().split())
nlst = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    nlst[i][i] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        nlst[u][v] = 0
        nlst[v][u] = 0
    else:
        nlst[u][v] = 0
        nlst[v][u] = 1

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            nlst[s][e] = min(nlst[s][e], nlst[s][m]+nlst[m][e])

k = int(input())
for _ in range(k):
    start, end = map(int, input().split())
    print(nlst[start][end])