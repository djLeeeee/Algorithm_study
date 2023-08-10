# 백준 17471_게리맨더링-x

import sys
sys.stdin = open('input6.txt')
from itertools import combinations
from copy import deepcopy


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


def connect(group):
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j and G[group[i]][group[j]]:
                # union(pick, other)
                p[j] = p[i]
    if len(set(p)) > 1:
        return 0
    else:
        total = 0
        for g in group:
            total += population[g]
    return total


N = int(input())
population = [0] + list(map(int, input().split()))
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        G[i][data[j]] = G[data[j]][i] = 1
result = 987987987
for i in range(1, N // 2 + 1):
    for comb in combinations((range(1, N + 1)), i):
        group1 = comb
        if len(group1) == 1:
            total1 = population[group1[0]]
        else:
            p = deepcopy(list(group1))
            total1 = connect(group1)
            if not total1:
                continue
        group2 = list(set(range(1, N + 1)) - set(comb))
        if len(group2) == 1:
            total2 = population[group2[0]]
        else:
            p = deepcopy(group2)
            total2 = connect(group2)
            if not total2:
                continue
        if result > abs(total1 - total2):
            result = abs(total1 - total2)
if result == 987987987:
    result = -1
print(result)