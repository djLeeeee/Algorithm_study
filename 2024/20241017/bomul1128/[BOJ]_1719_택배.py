# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1719
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1719&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n, m = map(int, input().split())
INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, input().split())
    tmp = min(dist[x][y], d)
    dist[x][y] = dist[y][x] = tmp
    graph[x].append((y, d))
    graph[y].append((x, d))
for j in range(1, n + 1):
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if dist[i][k] > dist[i][j] + dist[j][k]:
                dist[i][k] = dist[i][j] + dist[j][k]
ans = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    line = []
    for k in range(1, n + 1):
        if i == k:
            line.append("-")
        else:
            for j, d in graph[i]:
                if dist[i][j] == d and dist[i][k] == dist[i][j] + dist[j][k]:
                    line.append(j)
                    break
    print(*line)
