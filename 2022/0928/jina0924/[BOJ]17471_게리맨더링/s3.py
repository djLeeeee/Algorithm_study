# 백준 17471_게리맨더링 - ??(x)
import sys
sys.stdin = open('input5.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


def connect(group):
    ssum = 0
    leader = p[group[0]]
    for g in group:
        if p[g] != leader:
            return -1
        ssum += population[g]
    return ssum


def precinct():
    diff = set()
    for i in range(1, 1 << N):
        group1 = []
        for j in range(N):
            if i & (1 << j):
                group1.append(j+1)
        if len(group1) >= N:
            continue
        group2 = list(set(range(1, N+1)) - set(group1))
        sum1 = connect(group1)
        if sum1 < 1:
            continue
        sum2 = connect(group2)
        if sum2 >= 1:
            diff.add(abs(sum1 - sum2))
    if not len(diff):
        return -1
    return min(diff)


N = int(input())
population = [0] + list(map(int, input().split()))
p = list(range(N+1))
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        union(i, data[j])
if len(set(p)) > 3:
    print(-1)
else:
    ans = precinct()
    print(ans)