import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[] for _ in range(N+1)]
ans = []

for i in range(1, N+1):
    arr[int(input())].append(i)


def dfs(now, flag):
    visited[now] = 1

    for nxt in arr[now]:
        if visited[nxt] == 0:
            dfs(nxt, flag)
        elif visited[nxt] == 1 and nxt == flag:
            ans.append(nxt)


for i in range(1, N+1):
    visited = [0]*(N+1)
    dfs(i, i)


print(len(ans))
for i in ans:
    print(i)