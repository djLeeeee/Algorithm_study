import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[y] = x

input = sys.stdin.readline

n = int(input())
m = int(input())
p = list(range(n+1))
for i in range(1, n+1):
    path = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if path[j]:
            if find(i) != find(j):
                union(i, j)
tour = list(map(int, input().split()))
ans = set([find(country) for country in tour])
if len(ans) == 1:
    print('YES')
else:
    print('NO')