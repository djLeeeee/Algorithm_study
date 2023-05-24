# 백준 10159번 저울

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[0] + [INF] * n for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())            # 무게 비교했을 때 a > b
    graph[a][b] = 1

for k in range(1, n + 1):                       # a에서 b로 갈 수 있는 최단 경로 저장
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    cnt = 0
    for b in range(1, n + 1):
        if graph[a][b] == INF and graph[b][a] == INF:       # graph[a][b]: a가 b보다 무거운지, graph[b][a]: b가 a보다 무거운지
            cnt += 1
    print(cnt)
