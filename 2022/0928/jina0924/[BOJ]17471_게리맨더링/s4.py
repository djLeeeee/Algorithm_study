# 백준 17471_게리맨더링-x

import sys
sys.stdin = open('input2.txt')
from itertools import combinations
from copy import deepcopy


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


def is_connect(group):
    head = deepcopy(list(group))
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j and G[group[i]][group[j]]:
                head[j] = head[i]
    total = 0
    if len(set(head)) == 1:
        for g in group:
            total += population[g]
    return total


def precinct():
    ans = 987987987
    for i in range(1, N // 2 + 1):
        for com in combinations(range(1, N+1), i):
            group1 = com
            if len(group1) == 1:
                total1 = population[group1[0]]
            else:
                total1 = is_connect(group1)
            if not total1:
                continue
            group2 = list(set(range(1, N+1)) - set(com))
            if len(group2) == 1:
                total2 = population[group2[0]]
            else:
                total2 = is_connect(group2)
            if not total2:
                continue
            if ans > abs(total1 - total2):
                ans = abs(total1 - total2)
    return ans


N = int(input())
population = [0] + list(map(int, input().split()))
p = list(range(N+1))
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        G[i][data[j]] = G[data[j]][i] = 1
        union(i, data[j])
if len(set(p)) > 3:
    print(-1)
elif len(set(p)) == 3:
    a = p[1]
    sum1, sum2 = 0, 0
    for i in range(1, N+1):
        if p[i] == a:
            sum1 += population[i]
        else:
            sum2 += population[i]
    print(abs(sum1 - sum2))
elif len(set(p)) == 2:
    ans = precinct()
    print(ans)
