# 도시의 수 N, 여행 계획에 속한 도시들의 수 M
from sys import stdin
from collections import deque
N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())

g = [[] for _ in range(N+1)]

for i in range(1, N+1):
    temp = tuple(map(int, stdin.readline().rstrip().split()))
    for j in range(len(temp)):
        if temp[j]:
            g[i].append(j+1)
visited = [0] * (N + 1)
start, *journey = map(int, stdin.readline().rstrip().split())
my_set = set(journey)
my_set.add(start)
Q = deque([start])
visited[start] = 1
while Q:
    v = Q.popleft()
    for w in g[v]:
        if not visited[w]:
            Q.append(w)
            visited[w] = 1
for j in my_set:
    if not visited[j]:
        print('NO')
        break
else:
    print('YES')