# 백준 17471_게리맨더링 -x

import sys
sys.stdin = open('input1.txt')
from itertools import combinations


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


def connect(group):
    total = 0
    if len(group) > 1:
        for pick in group:
            connect = False
            for other in group:
                if pick != other and G[pick][other]:
                    connect = True
                    total += population[pick]
                    break
            if not connect:
                return 0
    else:
        total = population[group[0]]
    return total


def precinct():
    ans = 987987987
    for i in range(1, N // 2 + 1):
        for com in combinations(range(1, N+1), i):
            group1 = com
            total1 = connect(group1)
            if not total1:
                continue
            group2 = list(set(range(1, N+1)) - set(com))
            total2 = connect(group2)
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
print(G)
# for i in range(N+1):
#     p[i] = find_set(p[i])
print(p)
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
