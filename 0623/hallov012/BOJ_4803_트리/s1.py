import sys
sys.stdin = open('input.txt')

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

input = sys.stdin.readline

tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    p = list(range(n+1))
    cycle = []
    for _ in range(m):
        x, y = map(int, input().split())
        if find(x) != find(y):
            union(x, y)
        else:
            cycle.append(x)
    print(cycle)
    print(p)
    for i in range(n+1):
        find(i)

    group = set()
    for x in cycle:
        group.add(p[x])

    ans = 0
    for i in range(1, n+1):
        if p[i] in group:
            continue
        ans += 1
        group.add(p[i])

    if ans == 0:
        print(f'Case {tc}: No trees.')
    elif ans == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {ans} trees.')
