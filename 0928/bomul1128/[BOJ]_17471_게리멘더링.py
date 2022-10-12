from sys import stdin

input = stdin.readline


def dfs(start):
    if visited[start]:
        return
    visited[start] = group
    for adj in graph[start]:
        dfs(adj)


def dfs_check(start, team):
    if visited[start]:
        return
    visited[start] = True
    for adj in graph[start]:
        if adj in team:
            dfs_check(adj, team)


n = int(input())
house = [0] + list(map(int, input().split()))
graph = [[]]
for _ in range(n):
    _, *connect = list(map(int, input().split()))
    graph.append(connect)
visited = [0] * (n + 1)
group = 0
for i in range(1, n + 1):
    if not visited[i]:
        group += 1
        dfs(i)
if group > 2:
    print(-1)
elif group == 2:
    tot1 = 0
    tot2 = 0
    for j in range(1, n + 1):
        if visited[j] == 1:
            tot1 += house[j]
        else:
            tot2 += house[j]
    print(abs(tot1 - tot2))
else:
    ans = 1000
    for i in range(1 << (n - 1)):
        team1 = [n]
        team2 = []
        for j in range(n - 1):
            if i & (1 << j):
                team1.append(j + 1)
            else:
                team2.append(j + 1)
        check1 = 0
        visited = [False] * (n + 1)
        for s in team1:
            if not visited[s]:
                dfs_check(s, team1)
                check1 += 1
        check2 = 0
        visited = [False] * (n + 1)
        for s in team2:
            if not visited[s]:
                dfs_check(s, team2)
                check2 += 1
        if check1 == check2 == 1:
            tot1 = sum([house[p] for p in team1])
            tot2 = sum([house[q] for q in team2])
            ans = min(ans, abs(tot1 - tot2))
    print(ans)
