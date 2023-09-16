# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2151
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2151&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict

input = stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]
gate = []
point = {}
cnt = 0
row = [[] for _ in range(n)]
col = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == "#":
            gate.append((i, j))
        if board[i][j] in "!#":
            cnt += 1
            point[(i, j)] = cnt
            row[i].append(j)
            col[j].append(i)
ini, fin = gate
graph = [[] for _ in range(cnt + 1)]
for i in range(n):
    target = row[i]
    l = len(target)
    for j in range(l):
        y1 = target[j]
        p1 = point[(i, y1)]
        for k in range(j + 1, l):
            y2 = target[k]
            p2 = point[(i, y2)]
            flag = True
            for y in range(y1 + 1, y2):
                if board[i][y] == "*":
                    flag = False
                    break
            if flag:
                graph[p1].append(p2)
                graph[p2].append(p1)
    target = col[i]
    l = len(target)
    for j in range(l):
        x1 = target[j]
        p1 = point[(x1, i)]
        for k in range(j + 1, l):
            x2 = target[k]
            p2 = point[(x2, i)]
            flag = True
            for x in range(x1 + 1, x2):
                if board[x][i] == "*":
                    flag = False
                    break
            if flag:
                graph[p1].append(p2)
                graph[p2].append(p1)
cost = defaultdict(lambda: float("inf"))
ini, fin = point[ini], point[fin]
cost[ini] = 0
q = [(0, ini)]
while q:
    c, p = heappop(q)
    if c > cost[p]:
        continue
    for np in graph[p]:
        nc = c + 1
        if nc < cost[np]:
            cost[np] = nc
            heappush(q, (nc, np))
print(cost[fin] - 1)
