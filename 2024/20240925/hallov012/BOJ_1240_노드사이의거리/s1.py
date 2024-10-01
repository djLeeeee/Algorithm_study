import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

def bfs(a, b):
    visited = [sys.maxsize] * (n + 1)
    visited[a] = 0
    que = deque([(a, 0)])
    while que:
        now, dist = que.popleft()
        for next, d in g[now]:
            if visited[next] > dist + d:
                visited[next] = dist + d
                que.append((next, visited[next]))
    return visited[b]


input = sys.stdin.readline

n, m = map(int, input().split())

g = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))
