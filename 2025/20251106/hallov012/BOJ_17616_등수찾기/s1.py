import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dfs(now, arr):
    cnt = 1
    visited[now] = 1
    for next in arr[now]:
        if not visited[next]:
            cnt += dfs(next, arr)
    return cnt

n, m, x = map(int, input().split())
upper = [[] for _ in range(n+1)]
lower = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    upper[b].append(a)
    lower[a].append(b)

visited = [0] * (n+1)
u, v = 1, n
u += dfs(x, upper) - 1
v -= dfs(x, lower) - 1

print(u, v)
