import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, = map(int, input().split())
    g = [[sys.maxsize] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = c
        g[b][a] = c
    for i in range(1, n+1):
        g[i][i] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    p = int(input())
    now = list(map(int, input().split()))
    dist_min = sys.maxsize
    ans = []
    for i in range(n+1):
        cnt = 0
        for room in now:
            cnt += g[room][i]
        if cnt < dist_min:
            dist_min = cnt
            ans = [i]
        elif cnt == dist_min:
            ans.append(i)
    ans.sort()
    print(ans[0])