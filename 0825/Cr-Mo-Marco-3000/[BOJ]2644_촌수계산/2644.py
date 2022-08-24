import sys, collections
input = sys.stdin.readline
N = int(input().strip())
start, end = map(int, input().strip().split())
M = int(input().strip())
g = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    parent, child = map(int, input().strip().split())
    g[parent].append(child)
    g[child].append(parent)
Q = collections.deque([start])
visited[start] = 1
while Q:
    v = Q.popleft()
    for w in g[v]:
        if not visited[w]:
            Q.append(w)
            visited[w] = visited[v]+1
print(visited[end]-1)
