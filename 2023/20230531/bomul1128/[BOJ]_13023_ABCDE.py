# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/13023
from sys import stdin

input = stdin.readline


def sol(arr):
    if len(arr) < 2:
        return 0
    l = len(arr)
    for i in range(l - 1):
        rawA = graph[arr[i]]
        for j in range(i + 1, l):
            rawB = graph[arr[j]]
            sideA = rawA - {arr[j]}
            sideB = rawB - {arr[i]}
            if len(sideA) > 1 and len(sideB) > 1:
                if len(sideA) == len(sideB) == 2:
                    if len(sideA & sideB) == 1:
                        return 1
                elif len(sideA & sideB):
                    return 1
    return 0


n, m = map(int, input().split())
graph = [set() for _ in range(n)]
deg = [0] * n
entry = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    deg[a] += 1
    deg[b] += 1
    if deg[a] == 2:
        entry.append(a)
    if deg[b] == 2:
        entry.append(b)
print(sol(entry))