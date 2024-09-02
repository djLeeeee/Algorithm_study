import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x


while True:
    m, n = map(int, input().split())
    if not m+n:
        break
    p = list(range(m+1))
    ans = 0
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])
    for x, y, z in edges:
        if find(x) != find(y):
            union(x, y)
        else:
            ans += z
    print(ans)