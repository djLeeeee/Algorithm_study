from sys import stdin

input = stdin.readline

n = int(input())
connection = [[] for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    node = a[0]
    p = 1
    while a[p] != -1:
        connection[node].append((a[p], a[p + 1]))
        p += 2
visited = [False] * (n + 1)


def dfs(start, distance):
    visited[start] = True
    end, r = start, distance
    for now, cost in connection[start]:
        if not visited[now]:
            ver, dist = dfs(now, distance + cost)
            if dist > r:
                end = ver
                r = dist
    return end, r


s, _ = dfs(1, 0)
visited = [False] * (n + 1)
_, ans = dfs(s, 0)
print(ans)
