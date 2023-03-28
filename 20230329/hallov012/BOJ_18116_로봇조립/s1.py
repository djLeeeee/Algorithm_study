import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        # x의 루트가 y가 됨
        p[x] = y
        s[y] += s[x]
        s[x] = 0
    else:
        p[y] = x
        s[x] += s[y]
        s[y] = 0

input = sys.stdin.readline

n = int(input())
m = 10**6
p = list(range(m+1))
s = [1] * (m+1)
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'I':
        a, b = int(cmd[1]), int(cmd[2])
        if find(a) != find(b):
            union(a, b)
    else:
        root = find(int(cmd[1]))
        print(s[root])