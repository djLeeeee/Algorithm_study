import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if not g[i][j] and not g[j][i]:
            cnt += 1
    print(cnt)