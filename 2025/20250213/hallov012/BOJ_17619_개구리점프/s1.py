import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[y] = x

n, q = map(int, input().split())
trees = []
for i in range(1, n+1):
    a, b, _ = map(int, input().split())
    trees.append((a, b, i))
trees.sort()

p = list(range(n+1))
s1, e1, idx1 = trees[0]

for i in range(1, n):
    s2, e2, idx2 = trees[i]
    if s1 <= s2 <= e1:
        union(idx1, idx2)
        if e1 < e2:
            e1 = e2

    else:
        s1, e1, idx1 = trees[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(1 if p[a] == p[b] else 0)