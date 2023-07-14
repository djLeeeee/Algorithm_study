# 백준 17471_게리맨더링 - 비트연산을 이용한 부분집합(x)

def connect(group):
    if len(group) <= 1:
        ssum = population[group[0]]
    else:
        ssum = 0
        for k in range(len(group)):
            if not (G[group[k]] & set(group)):
                return -1
            ssum += population[group[k]]
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
total = sum(population)
G = [set() for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        G[i].add(data[j])
ans = precinct()
print(ans)
