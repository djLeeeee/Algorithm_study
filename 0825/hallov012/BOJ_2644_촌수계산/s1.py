import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0] * (n+1)
visited[s] = 1
que = deque([s])
while que:
    v = que.popleft()
    for w in g[v]:
        if not visited[w]:
            visited[w] = visited[v] + 1
            que.append(w)

if visited[e]:
    print(visited[e]-1)
else:
    print(-1)
