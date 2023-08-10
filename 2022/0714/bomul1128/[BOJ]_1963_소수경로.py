from sys import stdin

input = stdin.readline

prime = [True] * 10000
prime[0], prime[1] = False, False
for i in range(2, 100):
    if prime[i]:
        for j in range(2 * i, 10000, i):
            prime[j] = False
graph = [[] for _ in range(10000)]
for i in range(1000, 10000):
    if prime[i]:
        a = str(i)[::-1]
        for d in range(4):
            for x in range(1, 10 - int(a[d])):
                ni = i + x * 10 ** d
                if prime[ni]:
                    graph[i].append(ni)
                    graph[ni].append(i)
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    result = 0
    visited = [False] * 10000
    visited[x] = True
    point = [x]
    while not visited[y] and point:
        result += 1
        new = []
        for idx in point:
            for adj in graph[idx]:
                if not visited[adj]:
                    visited[adj] = True
                    new.append(adj)
        point = new
    if visited[y]:
        print(result)
    else:
        print("Impossible")

