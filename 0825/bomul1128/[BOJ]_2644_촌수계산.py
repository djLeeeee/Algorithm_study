n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [-1] * (n + 1)
visited[a] = 0
point = [a]
while point and visited[b] == -1:
    new = []
    for idx in point:
        for adj in graph[idx]:
            if visited[adj] == -1:
                visited[adj] = visited[idx] + 1
                new.append(adj)
    point = new
print(visited[b])
