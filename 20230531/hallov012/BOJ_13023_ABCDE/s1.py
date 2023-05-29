import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def find(x, cnt):
    if cnt == 5:
        print(1)
        exit()
    for y in g[x]:
        if not visited[y]:
            visited[y] = 1
            find(y, cnt+1)
            visited[y] = 0

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0] * (n+1)
for i in range(1, n+1):
    visited[i] = 1
    find(i, 1)
    visited[i] = 0

print(0)


