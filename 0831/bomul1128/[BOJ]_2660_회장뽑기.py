from sys import stdin

input = stdin.readline
INF = float('inf')

n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
while True:
    x, y = map(int, input().split())
    if x == y == -1:
        break
    graph[x][y] = 1
    graph[y][x] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
ms = n
ans = []
for i in range(1, n + 1):
    temp = max(graph[i][1:])
    if temp < ms:
        ms = temp
        ans = [i]
    elif temp == ms:
        ans.append(i)
print(ms, len(ans))
print(*ans)
