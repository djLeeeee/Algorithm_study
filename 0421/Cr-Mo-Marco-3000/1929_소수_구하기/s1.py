from sys import stdin


M, N = map(int, stdin.readline().rstrip().split())

g = [1] * (N+1)
i = 2
while i <= N:
    j = i
    k = j
    if j >= M and g[j] == 1:
        print(j)
    while j <= N:
        if g[j] == 1:
            g[j] = 0
        j += k
    i += 1
# 감사합니다