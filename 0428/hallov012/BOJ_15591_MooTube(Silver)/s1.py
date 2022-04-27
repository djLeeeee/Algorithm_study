import sys
from collections import deque, defaultdict

sys.stdin = open('input.txt')

def bfs(x):
    visited[x] = 1
    que = deque([x])
    while que:
        idx = que.popleft()
        for e, d in g[idx]:
            if not visited[e]:
                if idx == x:
                    visited[e] = d
                    que.append(e)
                else:
                    visited[e] = min(d, visited[idx])
                    que.append(e)

input = sys.stdin.readline

N, Q = map(int, input().split())
g = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int, input().split())
    g[p].append((q, r))
    g[q].append((p, r))
for _ in range(Q):
    k, v = map(int, input().split())
    visited = [0] * (N+1)
    bfs(v)
    ans = 0
    for i in range(1, N+1):
        if i != v and visited[i] >= k:
            ans += 1
    print(ans)


