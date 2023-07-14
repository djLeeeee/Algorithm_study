from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
graph = [[100] * (n + 1) for _ in range(n + 1)]
for s in range(n + 1):
    graph[s][s] = 0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
for j in range(1, n + 1):
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            graph[i][k] = min(graph[i][k], graph[i][j] + graph[j][k])
kv = 10000
for idx in range(1, n + 1):
    my_sum = sum(graph[idx][1:])
    if my_sum < kv:
        ans = idx
        kv = my_sum
print(ans)
